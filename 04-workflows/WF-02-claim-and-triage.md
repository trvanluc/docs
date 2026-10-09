# QTTN 02: Quy Trình Tiếp Nhận, Phân Loại & Gán Mức Độ Ưu Tiên Ticket (WF-02)

## 1. Mục Tiêu Quy Trình
Mô tả chi tiết luồng xử lý kỹ thuật khi Nhân viên phòng ban (STAFF) duyệt Queue công việc chung, kiểm tra nội dung Ticket mới (`NEW` hoặc `TRANSFERRED`), điều chỉnh lại phân loại nhóm vấn đề (`category_id`) nếu cần, gán độ ưu tiên (`priority`) và thực hiện Tiếp nhận (Claim) Ticket về danh sách cá nhân xử lý. Quy trình đảm bảo giải quyết triệt để tranh chấp dữ liệu (Optimistic Locking / Concurrency Control) khi nhiều nhân viên cùng bấm tiếp nhận 1 Ticket tại một thời điểm.

## 2. Tác Nhân Tham Gia (Actors) & Điều Kiện Tiên Quyết
- **Actors:**
  - **Nhân viên phòng ban (Staff):** Người thực hiện kiểm tra và tiếp nhận Ticket.
  - **Client (Staff Workspace Web App):** Giao diện hiển thị Queue phòng ban, hỗ trợ preview nội dung và form Claim/Triage.
  - **Server (Backend API):** Xác thực Token Staff, xử lý DB Lock/Concurrency, cập nhật trạng thái FSM, lưu Audit Log và phát Notification.
- **Preconditions:**
  - Nhân viên đã đăng nhập cổng Staff, có `role == STAFF` hoặc `MANAGER`.
  - Ticket nằm trong Queue thuộc cùng phòng ban với Nhân viên (`ticket.department_id == staff.department_id`).
  - Ticket đang ở trạng thái `NEW` hoặc `TRANSFERRED` (`assignee_id IS NULL`).

## 3. Lược Đồ Quy Trình Tương Tác (Sequence Diagram)
```plaintext
[Nhân viên]          [Client Web Staff]            [Backend API / CSDL]           [Sinh viên Owner]
    │                        │                               │                            │
    │ ── 1. Mở Queue PB ────>│                               │                            │
    │                        │ ── 2. GET /staff/queue ──────>│                            │
    │                        │<── 3. Trả về Danh sách NEW ───│                            │
    │ ── 4. Chọn 1 Ticket ──>│                               │                            │
    │ ── 5. Bấm "Tiếp nhận" ─>│                               │                            │
    │ ── 6. Chỉnh Category   │                               │                            │
    │    & Priority ────────>│                               │                            │
    │ ── 7. Bấm "Xác nhận" ──>│                               │                            │
    │                        │ ── 8. POST /tickets/{id}/claim │                            │
    │                        │    Body: category, priority   │                            │
    │                        │                               │ ── 9. Atomic DB Lock ─────>│
    │                        │                               │    WHERE status IN         │
    │                        │                               │    ('NEW', 'TRANSFERRED')  │
    │                        │                               │                            │
    │                        │                               │ ── 10. Update Assignee &   │
    │                        │                               │      Status=IN_PROGRESS   │
    │                        │                               │ ── 11. Write Audit Log ────│
    │                        │                               │ ── 12. Push Notification ──>│
    │                        │<── 13. HTTP 200 OK ───────────│                            │
    │<── 14. Toast Success ──│                               │                            │
    │    & Move to My List   │                               │                            │
    │                        │                               │                            │
    │                        │ [Ngoại lệ: Đã bị Claim trước] │                            │
    │                        │<── 15. HTTP 409 Conflict ─────│                            │
    │<── 16. Alert & Reload ─│    (TICKET_ALREADY_CLAIMED)   │                            │
```
---
## 4. Các Bước Thực Hiện Chi Tiết (Flow of Events)

### Bước 1: Truy Cập Queue Chờ Tiếp Nhận (Fetch Department Queue)
1. Nhân viên truy cập Tab "Chờ tiếp nhận" tại `/staff/queue`.
2. Client gọi API `GET /api/v1/staff/tickets?status=NEW,TRANSFERRED&department_id={current_staff_dept}`.
3. Server trả về danh sách Ticket chưa có người phụ trách (`assignee_id IS NULL`), sắp xếp theo thứ tự ưu tiên mặc định và thời gian tạo giảm dần (`created_at DESC`).

### Bước 2: Xem Chi Tiết & Khởi Tạo Form Claim (Preview & Triage)
1. Nhân viên click mở một Ticket cụ thể `/staff/tickets/{ticket_id}`.
2. Màn hình hiển thị chi tiết: Tiêu đề, nội dung mô tả, file đính kèm, danh mục ban đầu do sinh viên chọn (`category_id`) và độ ưu tiên mặc định (`priority = MEDIUM`).
3. Nhân viên bấm nút **Tiếp nhận xử lý**.
4. Khung điều chỉnh thông tin (Triage Modal/Panel) xuất hiện gồm:
   - **Dropdown Phân loại lại nhóm vấn đề (`category_id`):** Mặc định giữ giá trị cũ, cho phép chọn lại nhóm vấn đề khác thuộc cùng phòng ban.
   - **Radio buttons Độ ưu tiên (`priority`):** Cho phép chọn 1 trong 4 mức (`LOW`, `MEDIUM`, `HIGH`, `URGENT`).

### Bước 3: Submit Request & Xử Lý Tranh Chấp (Atomic Claim Processing)
1. Nhân viên nhấn **Xác nhận tiếp nhận**. Client vô hiệu hóa nút bấm và chuyển trạng thái Loading.
2. Client gửi request `POST /api/v1/staff/tickets/{ticket_id}/claim` kèm body `{ category_id, priority }`.
3. Thao tác Atomic Update tại Server:
   - Server xác thực Bearer Token: Bắt buộc `user.role IN ('STAFF', 'MANAGER')` và `user.department_id == ticket.department_id`.
   - Server thực hiện câu lệnh Update chống tranh chấp (Optimistic Locking / Conditional Update):
     `UPDATE tickets SET status = 'IN_PROGRESS', assignee_id = {current_staff_id}, category_id = {new_category_id}, priority = {new_priority}, updated_at = CURRENT_TIMESTAMP WHERE ticket_id = {ticket_id} AND status IN ('NEW', 'TRANSFERRED') AND assignee_id IS NULL;`
4. Kiểm tra kết quả Update:
   - **Thành công (Số bản ghi updated == 1):**
     - Ghi 01 bản ghi Audit Log vào `ticket_histories`: `action = CLAIM`, `performer_id = staff_id`, `details = { priority, category_id }`.
     - Phát Notification cho Sinh viên chủ sở hữu: "Yêu cầu [Mã_Ticket] của bạn đã được tiếp nhận bởi nhân viên [Tên_Staff] thuộc [Tên_Phòng_Ban]".
     - Trả về `HTTP 200 OK` chứa object Ticket đã cập nhật.
   - **Thất bại (Số bản ghi updated == 0 - Đã bị người khác Claim trước):**
     - Trả về mã lỗi `HTTP 409 Conflict` kèm Error Code `TICKET_ALREADY_CLAIMED`.

### Bước 4: Cập Nhật Giao Diện Client
1. **Trường hợp thành công (200 OK):**
   - Client hiển thị Toast success: "Tiếp nhận Ticket [Mã_Ticket] thành công!".
   - Ticket tự động chuyển từ Queue chung sang Tab "Ticket của tôi" (`/staff/my-tickets`).
   - Khung thao tác xử lý nghiệp vụ (Cập nhật tiến độ, Yêu cầu bổ sung, Hoàn tất) được kích hoạt cho Nhân viên.
2. **Trường hợp thất bại (409 Conflict):**
   - Client hiển thị Alert lỗi: "Ticket này đã được tiếp nhận xử lý bởi nhân viên [Tên_Staff_Đã_Claim] trước đó ít giây.".
   - Client tự động đóng Modal và reload lại danh sách Queue phòng ban để loại bỏ Ticket đã bị Claim khỏi giao diện.

## 5. Ràng Buộc Kỹ Thuật & Quy Tắc Nghiệp Vụ (Business Rules)

| Tên quy tắc | Mô tả chi tiết & Handling Specs |
| :--- | :--- |
| **Phân quyền Phòng ban** | Nhân viên phòng ban A tuyệt đối **KHÔNG ĐƯỢC** bấm Claim Ticket thuộc phòng ban B. Server bắt buộc verify `staff.department_id == ticket.department_id`. |
| **Ràng buộc Trạng thái FSM** | Chỉ cho phép Claim khi Ticket đang ở trạng thái `NEW` hoặc `TRANSFERRED`. Không cho phép Claim các Ticket đang ở `IN_PROGRESS`, `NEED_MORE_INFO`, `RESOLVED`, `CLOSED`. |
| **Chống Tranh Chấp (Concurrency Control)** | Phải sử dụng Atomic Condition Update ở CSDL để đảm bảo khi 10 Staff bấm Claim cùng 1 millisecond, đúng 01 Staff nhận thành công, 9 Staff còn lại nhận lỗi `409 Conflict`. |
| **Gán Phụ Trách (Assignee Assignment)** | Ngay sau khi Claim thành công, `assignee_id` bắt buộc phải lưu chính xác `user_id` của Nhân viên đang thực hiện request. |
| **Giá trị Mặc định Priority** | Nếu Nhân viên không chọn lại `priority`, hệ thống mặc định lưu `priority = MEDIUM`. Các giá trị hợp lệ: `LOW`, `MEDIUM`, `HIGH`, `URGENT`. |
| **Ghi vết Audit Trail** | Thao tác Claim là điểm mốc quan trọng, phải lưu timestamp `claimed_at` và tạo 1 record trong lịch sử trao đổi/biến động của Ticket. |

## 6. Luồng Ngoại Lệ & Mã Lỗi Hệ Thống (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Nhân viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Tranh chấp tiếp nhận (Đã bị Staff khác claim)** | `409 Conflict`<br><br>`TICKET_ALREADY_CLAIMED` | "Ticket này đã được tiếp nhận bởi nhân viên khác trước đó ít giây." | Hiển thị Alert error, tự động reload lại Queue để cập nhật UI. |
| **Claim Ticket phòng ban khác** | `403 Forbidden`<br><br>`FORBIDDEN_DEPARTMENT_ACCESS` | "Bạn không có quyền tiếp nhận Ticket của phòng ban khác." | Hiển thị Toast error, chặn thao tác Claim. |
| **Ticket đã bị đóng hoặc hủy từ trước** | `400 Bad Request`<br><br>`INVALID_TICKET_STATE` | "Ticket không còn ở trạng thái chờ tiếp nhận." | Reload lại chi tiết Ticket. |
| **Gửi Category ID không tồn tại** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Nhóm vấn đề được chọn không hợp lệ." | Báo lỗi validation trên Form Triage. |
| **Phiên làm việc hết hạn** | `401 Unauthorized`<br><br>`UNAUTHORIZED` | "Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại." | Điều hướng về trang `/staff/login`. |