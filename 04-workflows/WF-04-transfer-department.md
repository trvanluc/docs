# QTTN 04: Quy Trình Chuyển Tiếp Yêu Cầu Sang Phòng Ban Khác (WF-04)

## 1. Mục Tiêu Quy Trình
Mô tả chi tiết luồng xử lý kỹ thuật khi Nhân viên phòng ban (STAFF) hoặc Quản lý (MANAGER) phát hiện Ticket bị gửi nhầm đơn vị hoặc vượt quá thẩm quyền xử lý, cần điều chuyển sang đúng Phòng ban chuyên trách. Quy trình đảm bảo tính toàn vẹn của máy trạng thái FSM (chuyển sang `TRANSFERRED`, xóa `assignee_id` để đưa về Queue chờ của phòng ban mới), bắt buộc ghi vết Audit Trail chi tiết và gửi Notification cảnh báo thời gian thực tới phòng ban tiếp nhận.

## 2. Tác Nhân Tham Gia (Actors) & Điều Kiện Tiên Quyết
- **Actors:**
  - **Nhân viên phòng ban hiện tại (Staff Transferor):** Người khởi tạo thao tác điều chuyển.
  - **Phòng ban tiếp nhận mới (Target Department):** Đơn vị thụ lý mới.
  - **Client (Staff Web App):** Giao diện Modal chuyển phòng ban kèm validation real-time.
  - **Server (Backend API):** Verify quyền hạn, kiểm tra FSM state, cập nhật CSDL, lưu Audit Log và bắn Notification.
- **Preconditions:**
  - Ticket chưa ở trạng thái kết thúc (`status NOT IN ('RESOLVED', 'CLOSED', 'REJECTED')`).
  - Nhân viên thực hiện thuộc phòng ban đang thụ lý Ticket (`staff.department_id == ticket.department_id`) hoặc đúng là người đang phụ trách (`assignee_id == staff.id`).

## 3. Lược Đồ Quy Trình Tương Tác (Sequence Diagram)
```plaintext
[Staff PB Hiện Tại]     [Client Web Staff]            [Backend API / CSDL]         [Queue PB Mới]
        │                       │                              │                         │
        │ ── 1. Chuyển phòng ──>│                              │                         │
        │ ── 2. Chọn PB Đích ──>│                              │                         │
        │ ── 3. Nhập Lý do ────>│                              │                         │
        │ ── 4. Bấm "Xác nhận" ─>│                              │                         │
        │                       │ ── 5. POST /transfer ───────>│                         │
        │                       │    Body: target_dept, reason │                         │
        │                       │                              │ ── 6. Check FSM State ──>│
        │                       │                              │ ── 7. Check Dept ID ────>│
        │                       │                              │                          │
        │                       │                              │ ── 8. UPDATE Ticket ────>│
        │                       │                              │    - dept = target_dept │
        │                       │                              │    - status = TRANSFERRED│
        │                       │                              │    - assignee = NULL     │
        │                       │                              │                          │
        │                       │                              │ ── 9. Write Audit Log ──>│
        │                       │                              │ ── 10. Push Notify PB ──>│
        │                       │<── 11. HTTP 200 OK ──────────│                         │
        │<── 12. Toast Success ─│                              │                         │
        │    & Redirect Queue   │                              │                         │
        │                       │                              │                         │
        │                       │                              │<── 13. Nhận Notify ─────│
        │                       │                              │    & Hiển thị Queue     │
```
---
## 4. Các Bước Thực Hiện Chi Tiết (Flow of Events)

### Bước 1: Mở Modal Chuyển Phòng Ban
1. Tại trang chi tiết Ticket `/staff/tickets/{ticket_id}`, Nhân viên bấm nút **Chuyển phòng ban** (Nút này ẩn khi `status IN ('RESOLVED', 'CLOSED', 'REJECTED')`).
2. Client hiển thị Modal Chuyển tiếp yêu cầu liên phòng ban:
   - **Dropdown Phòng ban đích (`target_department_id`):** Danh sách các phòng ban khả dụng trong hệ thống (Đã vô hiệu hóa / Loại bỏ phòng ban hiện tại của Ticket).
   - **Textarea Lý do chuyển tiếp (`transfer_reason`):** Bắt buộc nhập, độ dài từ $10 - 500\text{ ký tự}$.

### Bước 2: Client Validation & Submit Request
1. Nhân viên chọn Phòng ban đích, nhập lý do điều chuyển và bấm **Xác nhận chuyển**.
2. Client thực hiện validate:
   - Bắt buộc phải chọn `target_department_id`.
   - `transfer_reason` sau khi `trim()` phải có độ dài $\ge 10\text{ ký tự}$.
3. Nếu hợp lệ, Client vô hiệu hóa nút bấm, chuyển trạng thái Loading và gửi request `POST /api/v1/staff/tickets/{ticket_id}/transfer`.

### Bước 3: Server Processing & Database Update
1. **Xác thực & Kiểm tra Quyền:**
   - Verify Bearer Token: User phải có role `STAFF` hoặc `MANAGER`.
   - Kiểm tra phòng ban: User phải thuộc phòng ban đang giữ Ticket.
   - Kiểm tra trạng thái Ticket: Nếu `status IN ('RESOLVED', 'CLOSED', 'REJECTED')`, trả về lỗi `400 INVALID_TICKET_STATE`.
   - Kiểm tra `target_department_id`: Phải tồn tại và khác với `ticket.department_id` hiện tại.
2. **Cập nhật Bản ghi Ticket (Atomic Transaction):**
   - Cập nhật phòng ban thụ lý mới: `department_id = target_department_id`.
   - Cập nhật trạng thái FSM: `status = TRANSFERRED`.
   - Xóa thông tin phụ trách cũ: `assignee_id = NULL` (Đẩy Ticket về dạng chờ tiếp nhận tại Phòng ban mới).
   - Cập nhật timestamp: `updated_at = CURRENT_TIMESTAMP`.
3. **Ghi vết Audit Log (Bắt buộc):**
   - Lưu 01 bản ghi vào bảng `ticket_histories`:
     - `action = TRANSFER`
     - `from_department_id = old_dept_id`
     - `to_department_id = target_department_id`
     - `performed_by = current_staff_id`
     - `reason_note = transfer_reason`
4. **Phát Thông Báo (Push Notification):**
   - Bắn thông báo thời gian thực (In-app WebSocket / Bell Notification) tới Queue công việc chung của Phòng ban mới: "Có 01 Ticket [Mã_Ticket] được chuyển đến từ [Tên_PB_Cũ]. Lý do: [Lý_do]".
   - Bắn thông báo cập nhật cho Sinh viên chủ sở hữu: "Yêu cầu [Mã_Ticket] của bạn đã được chuyển đến [Tên_PB_Mới] để xử lý".

### Bước 4: Cập Nhật Giao Diện Client
1. Server trả về `HTTP 200 OK`.
2. Client tại phía Staff cũ:
   - Hiển thị Toast success: "Đã chuyển Ticket [Mã_Ticket] sang [Tên_PB_Mới] thành công!".
   - Tự động đóng Modal và điều hướng Nhân viên về trang Danh sách công việc `/staff/dashboard`.
3. Tại phía Staff Phòng ban mới:
   - Ticket xuất hiện trong Tab "Ticket chờ tiếp nhận" (`/staff/queue`) với Badge màu vàng đại diện cho trạng thái `TRANSFERRED`.
   - Nhân viên phòng ban mới thực hiện tiếp nhận xử lý theo quy trình WF-02.

## 5. Ràng Buộc Kỹ Thuật & Quy Tắc Nghiệp Vụ (Business Rules)

| Tên quy tắc | Mô tả chi tiết & Handling Specs |
| :--- | :--- |
| **Bắt buộc Lý do chuyển** | `transfer_reason` bắt buộc nhập, độ dài từ $10 - 500\text{ ký tự}$ sau khi `trim()`. Không chấp nhận chuỗi chỉ chứa khoảng trắng. |
| **Phòng ban đích hợp lệ** | `target_department_id` phải khác hoàn toàn với `department_id` hiện tại của Ticket. Vô hiệu hóa Option phòng ban hiện tại trong Dropdown phía UI. |
| **Xóa Assignee cũ** | Ngay khi chuyển phòng ban thành công, `assignee_id` **BẮT BUỘC** phải đưa về `NULL` để Nhân viên cũ không còn quyền thao tác và đưa Ticket vào Queue chờ của Phòng ban mới. |
| **Trạng thái FSM TRANSFERRED** | Trạng thái Ticket đổi sang `TRANSFERRED`. Ticket ở `TRANSFERRED` có hành vi tương tự `NEW` (Nằm trong Queue chung chờ bấm Claim). |
| **Bảo lưu SLA & Lịch sử** | Mốc thời gian `sla_target_at` và toàn bộ Lịch sử trao đổi/File đính kèm cũ **ĐƯỢC GIỮ NGUYÊN** không bị thay đổi hay xóa bỏ. |
| **Ghi vết Audit Trail** | Mọi lượt chuyển phòng ban bắt buộc ghi 1 bản ghi lịch sử cố định vào `ticket_histories` phục vụ tra soát/kiểm toán chất lượng vận hành của Admin. |

## 6. Luồng Ngoại Lệ & Mã Lỗi Hệ Thống (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Nhân viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Bỏ trống lý do / Lý do quá ngắn** | `400 Bad Request`<br><br>`MISSING_TRANSFER_REASON` | "Vui lòng nhập lý do chuyển phòng ban (tối thiểu 10 ký tự)." | Hiển thị lỗi dưới Textarea của Modal, giữ nguyên dữ liệu. |
| **Chọn trùng phòng ban hiện tại** | `400 Bad Request`<br><br>`INVALID_TARGET_DEPARTMENT` | "Phòng ban đích phải khác với phòng ban hiện tại của Ticket." | Vô hiệu hóa lựa chọn trùng trên Dropdown UI. |
| **Ticket đã bị đóng hoặc hoàn thành** | `400 Bad Request`<br><br>`INVALID_TICKET_STATE` | "Ticket đã đóng hoặc hoàn thành, không thể chuyển phòng ban." | Ẩn nút Chuyển phòng ban, reload lại Ticket detail. |
| **Staff không thuộc phòng ban thụ lý** | `403 Forbidden`<br><br>`FORBIDDEN_DEPARTMENT_ACCESS` | "Bạn không có quyền chuyển Ticket của phòng ban khác." | Hiển thị Toast error, chặn gửi request. |
| **Lỗi Server / Database Transaction** | `500 Internal Server Error`<br><br>`INTERNAL_SERVER_ERROR` | "Không thể chuyển phòng ban do sự cố hệ thống. Vui lòng thử lại." | Hiển thị Toast error, giữ nguyên trạng thái Form để thử lại. |