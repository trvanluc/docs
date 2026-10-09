# QTTN 03: Quy Trình Yêu Cầu & Bổ Sung Thông Tin/Giấy Tờ (WF-03)

## 1. Mục Tiêu Quy Trình
Mô tả chi tiết luồng xử lý kỹ thuật hai chiều giữa Nhân viên và Sinh viên khi Ticket thiếu thông tin, sai hồ sơ hoặc cần bổ sung giấy tờ minh chứng. Quy trình đảm bảo tính toàn vẹn của State Machine (chuyển đổi tự động giữa `IN_PROGRESS` và `NEED_MORE_INFO`), đồng bộ thời gian thực qua Notification, kiểm soát dung lượng/định dạng file bổ sung và ghi vết toàn bộ lịch sử tương tác vào Conversation Log.

## 2. Tác Nhân Tham Gia (Actors) & Điều Kiện Tiên Quyết
- **Actors:**
  - **Nhân viên phụ trách (Staff Assignee):** Người phát yêu cầu bổ sung.
  - **Sinh viên sở hữu Ticket (Student Owner):** Người nhận thông báo và upload hồ sơ bổ sung.
  - **Client (Web App):** Giao diện xử lý hiển thị form động theo trạng thái Ticket.
  - **Server (Backend API):** Kiểm tra quyền hạn, validate file, chuyển đổi trạng thái FSM, lưu Conversation Log và phát Notification.
- **Preconditions:**
  - Ticket đang ở trạng thái `IN_PROGRESS`.
  - Nhân viên thực hiện thao tác phải đúng là người đang phụ trách Ticket (`assignee_id == current_user_id`).

## 3. Lược Đồ Quy Trình Tương Tác (Sequence Diagram)
```plaintext
[Nhân viên]          [Client Web]              [Backend API / Storage]            [Sinh viên]
    │                     │                               │                            │
    │ ── 1. Yêu cầu BS ──>│                               │                            │
    │ ── 2. Nhập ghi chú ─>│                               │                            │
    │ ── 3. Bấm Gửi ─────>│                               │                            │
    │                     │ ── 4. POST /request-more ────>│                            │
    │                     │    (Check status IN_PROGRESS) │                            │
    │                     │                               │ ── 5. Set NEED_MORE_INFO ──>│
    │                     │                               │ ── 6. Save Conversation ──>│
    │                     │                               │ ── 7. Push Notification ──>│
    │<── 8. HTTP 200 OK ──│                               │                            │
    │                     │                               │                            │
    │                     │                               │<── 9. Nhận Thông Báo ──────│
    │                     │                               │ ── 10. Mở Ticket Detail ──>│
    │                     │                               │ ── 11. Upload File + Note ─>│
    │                     │                               │ ── 12. Bấm Gửi bổ sung ────│
    │                     │                               │                            │
    │                     │                               │ ── 13. POST /supplement ──>│
    │                     │                               │    (Check NEED_MORE_INFO)  │
    │                     │                               │ ── 14. Set IN_PROGRESS ────│
    │                     │                               │ ── 15. Save Files & Log ───│
    │                     │                               │ ── 16. Push Notify Staff ──>│
    │                     │                               │<── 17. HTTP 200 OK ────────│
    │<── 18. Notify Web ──│                               │                            │
```
---
## 4. Các Bước Thực Hiện Chi Tiết (Flow of Events)

### Nhánh 1: Nhân viên phát yêu cầu bổ sung thông tin (Staff Request)
1. **Mở Modal Yêu cầu:** Tại trang chi tiết Ticket `/staff/tickets/{ticket_id}`, Nhân viên bấm nút **Yêu cầu bổ sung hồ sơ** (Nút này chỉ xuất hiện khi `status == IN_PROGRESS` và `assignee_id == current_staff_id`).
2. **Nhập Nội dung:** Nhân viên nhập chi tiết các giấy tờ/thông tin cần Sinh viên giải trình hoặc đính kèm thêm vào Textarea (`request_note`).
3. **Client Validation:**
   - Đảm bảo `request_note` không để trống và có độ dài từ $10 - 1.000\text{ ký tự}$ sau khi `trim()`.
4. **Gửi Request:** Client gửi request `POST /api/v1/staff/tickets/{ticket_id}/request-more-info`.
5. **Server Processing:**
   - Xác thực Token Staff và kiểm tra quyền phụ trách (`assignee_id`).
   - Kiểm tra trạng thái hiện tại: Nếu `status != IN_PROGRESS`, trả về lỗi `400 INVALID_TICKET_STATE`.
   - Cập nhật trạng thái Ticket: `status = NEED_MORE_INFO`.
   - Ghi nhận 1 bản ghi vào bảng `ticket_conversations`: `sender_role = STAFF`, `message_type = PUBLIC_MESSAGE`, `message_text = request_note`.
   - Phát Notification (In-app Bell / Email) cho Sinh viên sở hữu Ticket.
6. **Cập nhật UI Staff:** Modal đóng, hiển thị Toast success: "Đã gửi yêu cầu bổ sung tới sinh viên", Badge trạng thái Ticket đổi sang `NEED_MORE_INFO`.

### Nhánh 2: Sinh viên thực hiện bổ sung hồ sơ (Student Supplement)
1. **Tiếp nhận Thông báo:** Sinh viên nhận Notification, click mở trang chi tiết Ticket `/tickets/{ticket_id}`.
2. **Hiển thị Form Bổ sung:**
   - Hệ thống phát hiện `status == NEED_MORE_INFO`, tự động mở Khung Bổ sung thông tin kèm hộp thông điệp yêu cầu từ Nhân viên.
   - Các trường thông tin ban đầu (`title`, `category_id`) ở trạng thái Read-Only (Không cho sửa).
3. **Tải File & Nhập Ghi chú:**
   - Sinh viên nhập lời nhắn giải trình bổ sung (`supplement_note` Optional, max $1.000\text{ ký tự}$).
   - Sinh viên kéo thả/chọn file đính kèm bổ sung (Tối đa $5\text{ file}$, dung lượng $\le 5\text{MB/file}$, định dạng `.pdf`, `.png`, `.jpg`, `.jpeg`).
4. **Submit Request:** Sinh viên bấm Xác nhận gửi bổ sung. Client chuyển nút sang Loading để chống double-click.
5. **Server Processing:**
   - Xác thực Token Sinh viên (`student_id == ticket.student_id`).
   - Kiểm tra trạng thái Ticket: Bắt buộc `status == NEED_MORE_INFO`. Nếu trạng thái đã bị đổi (ví dụ: Staff đã hủy/đóng), trả về `400 INVALID_TICKET_STATE`.
   - Validate và Upload các file đính kèm bổ sung lên S3/Storage.
   - Tự động chuyển đổi trạng thái FSM: Cập nhật `status = IN_PROGRESS`.
   - Ghi bản ghi vào `ticket_conversations`: `sender_role = STUDENT`, `message_text = supplement_note`, `attachments = new_files_list`.
   - Phát Notification báo cho Nhân viên phụ trách: "Sinh viên [Tên_SV] đã nộp bổ sung hồ sơ cho Ticket [Mã_Ticket]".
6. **Cập nhật UI Student:** Hiển thị Toast thành công: "Đã gửi hồ sơ bổ sung thành công!". Form bổ sung tự động ẩn/khóa, Badge trạng thái cập nhật thành `IN_PROGRESS`.

## 5. Ràng Buộc Kỹ Thuật & Quy Tắc Nghiệp Vụ (Business Rules)

| Tên quy tắc | Mô tả chi tiết & Handling Specs |
| :--- | :--- |
| **Ràng buộc Quyền thao tác** | Chỉ Nhân viên đang phụ trách trực tiếp (`assignee_id`) mới có quyền phát yêu cầu bổ sung. Chỉ Sinh viên chủ sở hữu (`student_id`) mới có quyền nộp bổ sung. |
| **Giao diện động (Dynamic UI)** | Khung upload file bổ sung **CHỈ** hiển thị phía Sinh viên khi `status == NEED_MORE_INFO`. Khi Ticket ở trạng thái khác, khu vực này hoàn toàn bị ẩn hoặc khóa. |
| **Không cho sửa nội dung gốc** | Trong suốt quá trình bổ sung, Sinh viên **KHÔNG ĐƯỢC PHÉP** chỉnh sửa `title`, `description` hoặc `category_id` đã khởi tạo ban đầu. |
| **Quy tắc File bổ sung** | Tối đa $5\text{ file}$ cho mỗi lần gửi bổ sung. Dung lượng $\le 5\text{MB/file}$. Định dạng MIME: `application/pdf`, `image/png`, `image/jpeg`. |
| **Chuyển đổi trạng thái tự động** | Ngay sau khi Sinh viên bấm Xác nhận gửi bổ sung thành công, Backend phải tự động đổi `status` từ `NEED_MORE_INFO` $\rightarrow$ `IN_PROGRESS` mà không cần thao tác thủ công của Nhân viên. |
| **Lưu vết Conversation Log** | Toàn bộ lời nhắn yêu cầu của Staff và file/ghi chú bổ sung của Student phải được lưu vào bảng `ticket_conversations` theo đúng thứ tự thời gian (`created_at ASC`). |

## 6. Luồng Ngoại Lệ & Mã Lỗi Hệ Thống (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho người dùng | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Nhân viên để trống ghi chú yêu cầu** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng nhập nội dung chi tiết cần sinh viên bổ sung (tối thiểu 10 ký tự)." | Hiển thị lỗi dưới Textarea của Modal Staff, giữ nguyên dữ liệu. |
| **Thao tác sai trạng thái FSM** | `400 Bad Request`<br><br>`INVALID_TICKET_STATE` | "Trạng thái Ticket đã thay đổi. Không thể thực hiện thao tác này." | Tự động reload lại dữ liệu Ticket để cập nhật UI mới nhất. |
| **Sinh viên gửi bổ sung nhưng không có file & note** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng tải lên ít nhất 01 file đính kèm hoặc nhập lời nhắn bổ sung." | Báo lỗi validation trên Form của Sinh viên, không phát request. |
| **Upload file bổ sung sai định dạng/quá 5MB** | `400 Bad Request`<br><br>`FILE_EXCEEDS_LIMIT` | "File [Tên_File] vượt quá 5MB hoặc không đúng định dạng (.pdf, .png, .jpg)." | Đánh dấu đỏ file lỗi, ngăn thao tác submit. |
| **Staff không có quyền phụ trách Ticket** | `403 Forbidden`<br><br>`FORBIDDEN_ACCESS` | "Bạn không phải là người phụ trách xử lý Ticket này." | Vô hiệu hóa nút bấm trên giao diện Staff. |