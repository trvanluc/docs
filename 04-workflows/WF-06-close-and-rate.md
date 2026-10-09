# QTTN 06: Quy Trình Sinh Viên Nhận Kết Quả & Đánh Giá Mức Độ Hài Lòng (WF-06)

## 1. Mục Tiêu Quy Trình
Mô tả chi tiết luồng xử lý kỹ thuật khi Sinh viên tiếp nhận kết quả xử lý từ nhà trường và thực hiện đánh giá chất lượng phục vụ (CSAT - Customer Satisfaction). Quy trình đảm bảo tính toàn vẹn FSM (chuyển đổi từ `RESOLVED` sang `CLOSED`), khóa form đánh giá chống gửi lặp (Read-only state), xử lý tranh chấp khi mở nhiều tab (Race Condition) và tự động đóng Ticket qua hệ thống Cronjob sau 3 ngày làm việc.

## 2. Tác Nhân Tham Gia (Actors) & Điều Kiện Tiên Quyết
- **Actors:**
  - **Sinh viên sở hữu Ticket (Student Owner):** Người đọc kết quả và gửi đánh giá.
  - **Client (Web App):** Giao diện hiển thị kết quả giải quyết và Component đánh giá sao/nhận xét.
  - **Server (Backend API):** Xác thực quyền, kiểm tra ràng buộc 1 lần đánh giá, cập nhật CSDL, chuyển trạng thái `CLOSED` và phát Notification.
  - **System Cronjob:** Tiến trình chạy ngầm tự động đóng các Ticket ở trạng thái `RESOLVED` quá 3 ngày làm việc.
- **Preconditions:**
  - Ticket có trạng thái `RESOLVED` hoặc `CLOSED`.
  - Sinh viên đăng nhập đúng tài khoản sở hữu Ticket (`student_id == ticket.student_id`).

## 3. Lược Đồ Quy Trình Tương Tác (Sequence Diagram)
```plaintext
[Sinh viên]            [Client Web]              [Backend API / CSDL]           [System Cronjob]
    │                       │                             │                            │
    │ ── 1. Mở Ticket ─────>│                             │                            │
    │                       │ ── 2. GET /tickets/{id} ───>│                            │
    │                       │<── 3. Trả về Detail ────────│                            │
    │ ── 4. Xem Kết quả ───>│    (Bao gồm Resolution Note)│                            │
    │                       │                             │                            │
    │                       │ [Kiểm tra rating_score]     │                            │
    │                       │ - Nếu NULL: Hiện Form ĐG    │                            │
    │                       │ - Nếu HAS: Hiện Read-only   │                            │
    │                       │                             │                            │
    │ ── 5. Chọn 1-5 Sao ──>│                             │                            │
    │ ── 6. Nhập Comment ──>│                             │                            │
    │ ── 7. Bấm "Gửi ĐG" ──>│                             │                            │
    │                       │ ── 8. POST /rate ──────────>│                            │
    │                       │    (Check rating_score NULL)│                            │
    │                       │                             │ ── 9. Save Rating Data ───>│
    │                       │                             │ ── 10. Set STATUS=CLOSED ─>│
    │                       │                             │ ── 11. Set rated_at, closed_at
    │                       │<── 12. HTTP 200 OK ─────────│                            │
    │<── 13. Toast Cảm ơn ──│                             │                            │
    │    & Render Read-only │                             │                            │
    │                       │                             │                            │
    │                       │                             │<── 14. Quá 3 ngày làm việc ─│
    │                       │                             │    (Chưa đánh giá)        │
    │                       │                             │ ── 15. Auto SET CLOSED ───│
```
---
## 4. Các Bước Thực Hiện Chi Tiết (Flow of Events)

### Nhánh 1: Sinh viên thực hiện đánh giá thành công (Main Flow)
1. **Truy cập Chi tiết Ticket:** Sinh viên click thông báo hoặc truy cập đường dẫn `/tickets/{ticket_id}`.
2. **Hiển thị Kết quả & Form Đánh giá:**
   - Hệ thống hiển thị Khung Kết quả giải quyết gồm: Nội dung phản hồi của Nhân viên (`resolution_note`), danh sách File đính kèm kết quả (`resolution_attachments`) và thời gian hoàn thành (`resolved_at`).
   - Client kiểm tra trường `rating_score` trong response data:
     - Nếu `rating_score == NULL`: Hiển thị Component Đánh giá (5 Ngôi sao tương tác + Textarea nhập `rating_comment` + Nút Gửi đánh giá).
     - Nếu `rating_score != NULL`: Chuyển Component Đánh giá sang dạng Read-Only (Hiển thị số sao đã chọn và nhận xét cũ, vô hiệu hóa toàn bộ input).
3. **Thao tác Đánh giá:**
   - Sinh viên chọn số sao từ $1$ đến $5$ sao (`rating_score` Bắt buộc).
   - Sinh viên nhập nhận xét bổ sung (`rating_comment` Không bắt buộc, tối đa $500\text{ ký tự}$).
4. **Submit Request:** Sinh viên bấm **Gửi đánh giá**. Client chuyển nút sang Loading để chống double click.
5. **Server Processing & Atomic Update:**
   - Server kiểm tra JWT Token: Xác thực `student_id == ticket.student_id`.
   - Server kiểm tra trạng thái đánh giá hiện tại:
     - Thực hiện query kiểm tra `SELECT rating_score FROM tickets WHERE ticket_id = ? FOR UPDATE`.
     - Nếu `rating_score IS NOT NULL` (Đã được đánh giá trước đó): Trả về mã lỗi `409 ALREADY_RATED`.
   - Cập nhật dữ liệu vào bản ghi Ticket:
     - `rating_score = request.rating_score`
     - `rating_comment = trim(request.rating_comment)`
     - `rated_at = CURRENT_TIMESTAMP`
     - `status = CLOSED` (Nếu trạng thái hiện tại đang là `RESOLVED`)
     - `closed_at = CURRENT_TIMESTAMP` (Nếu `closed_at` đang `NULL`)
6. **Cập nhật UI:**
   - Server trả về `HTTP 200 OK`.
   - Client hiển thị Toast thông báo: *"Cảm ơn bạn đã gửi đánh giá chất lượng dịch vụ!"*.
   - Component Đánh giá tự động chuyển sang dạng Read-Only (Không thể chỉnh sửa hay gửi lại).

### Nhánh 2: Tự động đóng Ticket qua Cronjob (System Auto-Close Flow)
1. **Lịch chạy định kỳ:** Hệ thống Cronjob chạy tự động vào $23:00$ mỗi ngày làm việc.
2. **Xác định bản ghi:** Cronjob quét các Ticket đáp ứng đầy đủ điều kiện:
   - `status == RESOLVED`
   - `rating_score IS NULL`
   - Thời gian từ `resolved_at` đến thời điểm hiện tại $> 3\text{ ngày làm việc}$ ($72\text{ giờ làm việc}$, loại trừ Thứ 7, Chủ Nhật và ngày Lễ).
3. **Xử lý cập nhật hàng loạt (Batch Processing):**
   - Cập nhật trạng thái: `status = CLOSED`.
   - Cập nhật timestamp: `closed_at = CURRENT_TIMESTAMP`.
   - Ghi log hệ thống (Audit Log): `action = SYSTEM_AUTO_CLOSE`.
4. **Trạng thái sau Auto-close:**
   - Khi Sinh viên mở lại Ticket đã bị Auto-close, hệ thống **VẪN CHO PHÉP** Sinh viên đánh giá hài lòng nếu `rating_score` vẫn đang `NULL`.
   - Sau khi Sinh viên đánh giá xong, hệ thống cập nhật `rating_score`, `rating_comment`, `rated_at` và giữ nguyên trạng thái `CLOSED`.

## 5. Ràng Buộc Kỹ Thuật & Quy Tắc Nghiệp Vụ (Business Rules)

| Tên quy tắc | Mô tả chi tiết & Handling Specs |
| :--- | :--- |
| **Bắt buộc số sao** | `rating_score` bắt buộc chọn, nhận giá trị số nguyên từ $1$ đến $5$. Không được gửi request khi chưa chọn số sao. |
| **Ghi chú đánh giá** | `rating_comment` không bắt buộc (Optional), độ dài tối đa $500\text{ ký tự}$. Tự động `trim()` khoảng trắng thừa. |
| **Giới hạn số lần đánh giá** | Mỗi Ticket chỉ được gửi đánh giá duy nhất $01\text{ lần}$. Sau khi ghi nhận thành công, dữ liệu đánh giá là bất biến (Immutable - không cho sửa/xóa). |
| **Chuyển đổi trạng thái FSM** | Khi Sinh viên gửi đánh giá cho Ticket `RESOLVED`, Backend phải tự động cập nhật `status = CLOSED` và ghi nhận `closed_at`. |
| **Xử lý Race Condition (Nhiều tab)** | Nếu Sinh viên mở 2 tab cùng 1 Ticket: Tab A bấm gửi trước $\rightarrow$ Thành công; Tab B bấm gửi sau $\rightarrow$ Server trả lỗi `409 ALREADY_RATED`. Tab B nhận lỗi sẽ tự động fetch lại data và chuyển giao diện sang dạng Read-only. |
| **Quy tắc Auto-Close** | Sau $3\text{ ngày làm việc}$ kể từ khi `status = RESOLVED`, nếu Sinh viên không đánh giá, Hệ thống tự chuyển `status = CLOSED`. Sinh viên mở lại Ticket vẫn có thể bổ sung Đánh giá. |

## 6. Luồng Ngoại Lệ & Mã Lỗi Hệ Thống (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Sinh viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Chưa chọn số sao mà bấm Gửi** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng chọn mức độ hài lòng (từ 1 đến 5 sao) trước khi gửi." | Báo lỗi validation trực tiếp trên UI, không phát request. |
| **Gửi đánh giá 2 lần (Trùng lặp/Nhiều tab)** | `409 Conflict`<br><br>`ALREADY_RATED` | "Ticket này đã được gửi đánh giá trước đó." | Reload lại dữ liệu Ticket, ẩn nút Gửi, chuyển Form sang dạng Read-only. |
| **Nhập nhận xét vượt quá 500 ký tự** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Nhận xét không được vượt quá 500 ký tự." | Chặn không cho nhập tiếp trên Textarea (Counter max length = 500). |
| **Gửi đánh giá cho Ticket của sinh viên khác** | `403 Forbidden`<br><br>`FORBIDDEN_ACCESS` | "Bạn không có quyền đánh giá Ticket này." | Ẩn hoàn toàn Component Đánh giá, hiển thị thông báo không có quyền. |
| **Mạng ngắt kết nối khi gửi đánh giá** | `500 Internal Server Error`<br><br>`INTERNAL_SERVER_ERROR` | "Không thể lưu đánh giá do lỗi kết nối. Vui lòng thử lại." | Hiển thị Toast error, giữ nguyên số sao và nhận xét đã chọn để Sinh viên bấm thử lại. |