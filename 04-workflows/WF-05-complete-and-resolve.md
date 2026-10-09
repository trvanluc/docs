# QTTN 05: Quy Trình Cập Nhật Kết Quả & Hoàn Tất Xử Lý Ticket (WF-05)

## 1. Mục Tiêu Quy Trình
Mô tả chi tiết luồng xử lý kỹ thuật khi Nhân viên phụ trách (STAFF Assignee) hoàn thành các thao tác nghiệp vụ chuyên môn và ghi nhận kết quả phản hồi chính thức cho Sinh viên. Quy trình kiểm soát chặt chẽ máy trạng thái FSM (chuyển sang `RESOLVED`, kích hoạt bộ đếm thời gian tự động đóng `closed_at` sau 3 ngày), ràng buộc nhập dữ liệu kết quả giải quyết (`resolution_note`), cho phép đính kèm file kết quả và gửi thông báo thời gian thực tới Sinh viên.

## 2. Tác Nhân Tham Gia (Actors) & Điều Kiện Tiên Quyết
- **Actors:**
  - **Nhân viên phụ trách (Staff Assignee):** Người nhập kết quả và hoàn tất xử lý.
  - **Sinh viên chủ sở hữu (Student Owner):** Người nhận thông báo kết quả và kiểm tra lời giải quyết.
  - **Client (Staff Web App):** Giao diện Modal nhập kết quả giải quyết kèm upload file đính kèm phản hồi.
  - **Server (Backend API):** Verify quyền hạn, kiểm tra FSM state, lưu kết quả, cập nhật timestamp `resolved_at`, phát Notification và khởi chạy bộ đếm Auto-close.
- **Preconditions:**
  - Ticket đang ở trạng thái `IN_PROGRESS`.
  - Nhân viên thực hiện bắt buộc phải đúng là người đang phụ trách Ticket (`assignee_id == current_staff_id`).

## 3. Lược Đồ Quy Trình Tương Tác (Sequence Diagram)
```plaintext
[Staff Assignee]        [Client Web Staff]            [Backend API / Storage]          [Sinh viên Owner]
       │                        │                               │                            │
       │ ── 1. Bấm "Hoàn thành"─>│                               │                            │
       │ ── 2. Nhập Note & File>│                               │                            │
       │ ── 3. Bấm "Xác nhận" ─>│                               │                            │
       │                        │ ── 4. POST /resolve ─────────>│                            │
       │                        │    Body: note, attachments    │                            │
       │                        │                               │ ── 5. Verify Assignee ────>│
       │                        │                               │ ── 6. Check IN_PROGRESS ──>│
       │                        │                               │                            │
       │                        │                               │ ── 7. Save Note & Files ──>│
       │                        │                               │ ── 8. Set STATUS=RESOLVED ─>│
       │                        │                               │ ── 9. Set resolved_at ────>│
       │                        │                               │ ── 10. Push Notification ─>│
       │                        │<── 11. HTTP 200 OK ───────────│                            │
       │<── 12. Toast Success ──│                               │                            │
       │    & Lock UI Controls  │                               │                            │
       │                        │                               │                            │
       │                        │                               │<── 13. Nhận Thông Báo ─────│
       │                        │                               │    & Xem kết quả giải quyết│
```
---
## 4. Các Bước Thực Hiện Chi Tiết (Flow of Events)

### Bước 1: Mở Modal Hoàn Tất Xử Lý
1. Tại trang chi tiết Ticket `/staff/tickets/{ticket_id}`, Nhân viên bấm nút **Hoàn thành & Đóng Ticket** (Nút này chỉ hiển thị khi `status == IN_PROGRESS` và `assignee_id == current_staff_id`).
2. Client hiển thị Modal Ghi nhận kết quả giải quyết:
   - **Textarea Nội dung kết quả giải quyết (`resolution_note`):** Bắt buộc nhập, độ dài từ $20 - 2.000\text{ ký tự}$.
   - **Khung upload File đính kèm kết quả (`resolution_attachments`):** Không bắt buộc (Optional), tối đa $3\text{ file}$, dung lượng $\le 5\text{MB/file}$, định dạng `.pdf`, `.png`, `.jpg`, `.jpeg`.

### Bước 2: Client Validation & Submit Request
1. Nhân viên nhập chi tiết câu trả lời/phương án xử lý, đính kèm file văn bản kết quả (nếu có) và bấm **Xác nhận hoàn tất**.
2. Client thực hiện validate:
   - `resolution_note` sau khi `trim()` bắt buộc có độ dài $\ge 20\text{ ký tự}$.
   - Kiểm tra định dạng và dung lượng danh sách file đính kèm (nếu có).
3. Nếu hợp lệ, Client vô hiệu hóa nút bấm, chuyển trạng thái Loading và gửi request `POST /api/v1/staff/tickets/{ticket_id}/resolve`.

### Bước 3: Server Processing & Database Update
1. **Xác thực & Kiểm tra Quyền:**
   - Verify Bearer Token: User phải là Nhân viên đang trực tiếp phụ trách Ticket (`assignee_id == current_staff_id`).
   - Kiểm tra trạng thái FSM: Bắt buộc `status == IN_PROGRESS`. Nếu Ticket đang ở trạng thái khác, trả về mã lỗi `400 INVALID_TICKET_STATE`.
2. **Upload File Kết Quả (nếu có):**
   - Read Magic Bytes xác thực định dạng file thực tế.
   - Lưu file lên Storage/S3, sinh mảng `resolution_attachments` chứa metadata file.
3. **Cập nhật Bản ghi Ticket (Atomic Transaction):**
   - Lưu câu trả lời: `resolution_note = trim(request.resolution_note)`.
   - Lưu danh sách file: `resolution_attachments = request.attachments`.
   - Chuyển đổi trạng thái FSM: `status = RESOLVED`.
   - Cập nhật timestamp: `resolved_at = CURRENT_TIMESTAMP`, `updated_at = CURRENT_TIMESTAMP`.
4. **Ghi vết Audit Trail:**
   - Ghi 01 bản ghi lịch sử vào `ticket_histories`: `action = RESOLVE`, `performer_id = current_staff_id`, `details = resolution_note`.
5. **Phát Thông Báo (Push Notification):**
   - Bắn thông báo thời gian thực (In-app Bell / Email) tới Sinh viên chủ sở hữu: "Yêu cầu [Mã_Ticket] của bạn đã được giải quyết. Vui lòng kiểm tra kết quả và đánh giá mức độ hài lòng."

### Bước 4: Cập Nhật Giao Diện Client & Luồng Tiếp Theo
1. Server trả về `HTTP 200 OK`.
2. Client tại phía Staff:
   - Hiển thị Toast success: "Đã hoàn tất xử lý Ticket [Mã_Ticket] thành công!".
   - Khóa toàn bộ các nút thao tác xử lý (Disable nút Chuyển phòng ban, Yêu cầu bổ sung, Hoàn thành).
   - Badge trạng thái Ticket chuyển sang màu xanh lá đại diện cho `RESOLVED`.
3. Phía Sinh viên:
   - Nhận thông báo, xem được đầy đủ `resolution_note` và file kết quả.
   - Kích hoạt Component cho phép Sinh viên thực hiện Đánh giá mức độ hài lòng (CSAT $1-5$ sao) theo quy trình WF-06.

## 5. Ràng Buộc Kỹ Thuật & Quy Tắc Nghiệp Vụ (Business Rules)

| Tên quy tắc | Mô tả chi tiết & Handling Specs |
| :--- | :--- |
| **Bắt buộc Kết quả xử lý** | `resolution_note` bắt buộc nhập, độ dài từ $20 - 2.000\text{ ký tự}$ sau khi `trim()`. Không chấp nhận chuỗi chỉ chứa khoảng trắng. |
| **Ràng buộc File kết quả** | Tối đa $3\text{ file/lần hoàn tất}$. Dung lượng $\le 5\text{MB/file}$. Định dạng MIME Type thực tế: `application/pdf`, `image/png`, `image/jpeg`. |
| **Chuyển đổi Trạng thái RESOLVED** | Bắt buộc chuyển trạng thái sang `RESOLVED` (chưa chuyển thẳng sang `CLOSED` để chờ Sinh viên nghiệm thu và đánh giá). |
| **Ghi nhận resolved_at** | Timestamp `resolved_at` được lưu cố định làm căn cứ tính Tổng thời gian xử lý thực tế (Resolution Time) phục vụ Báo cáo SLA của Quản lý. |
| **Khóa thao tác Chỉnh sửa** | Khi Ticket đã chuyển sang `RESOLVED`, Nhân viên **KHÔNG ĐƯỢC PHÉP** chỉnh sửa lại `resolution_note` hoặc thay đổi trạng thái Ticket trừ khi có can thiệp của Admin. |
| **Bộ đếm Auto-Close (Cronjob)** | Ngay khi `status = RESOLVED`, hệ thống bắt đầu tính $3\text{ ngày làm việc}$. Nếu Sinh viên không đánh giá, Cronjob sẽ tự động chuyển `status = CLOSED` (theo quy định tại WF-06). |

## 6. Luồng Ngoại Lệ & Mã Lỗi Hệ Thống (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Nhân viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Để trống kết quả / Kết quả quá ngắn** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng nhập nội dung kết quả giải quyết chi tiết (tối thiểu 20 ký tự)." | Hiển thị lỗi dưới Textarea của Modal, giữ nguyên dữ liệu đã nhập. |
| **Thao tác khi Ticket không ở IN_PROGRESS** | `400 Bad Request`<br><br>`INVALID_TICKET_STATE` | "Ticket không ở trạng thái cho phép hoàn tất xử lý." | Tự động reload lại dữ liệu Ticket để cập nhật UI mới nhất. |
| **Upload file kết quả quá 5MB / sai đuôi** | `400 Bad Request`<br><br>`FILE_EXCEEDS_LIMIT` | "File [Tên_File] vượt quá dung lượng 5MB hoặc sai định dạng (.pdf, .png, .jpg)." | Đánh dấu đỏ file lỗi trên Modal upload, ngăn submit. |
| **Staff không phải người phụ trách (Assignee)** | `403 Forbidden`<br><br>`FORBIDDEN_ACCESS` | "Bạn không phải là người trực tiếp phụ trách xử lý Ticket này." | Vô hiệu hóa nút Hoàn thành trên giao diện Staff. |
| **Lỗi Server / Database Transaction** | `500 Internal Server Error`<br><br>`INTERNAL_SERVER_ERROR` | "Không thể lưu kết quả do sự cố hệ thống. Vui lòng thử lại." | Hiển thị Toast error, giữ nguyên trạng thái Modal để thử lại. |