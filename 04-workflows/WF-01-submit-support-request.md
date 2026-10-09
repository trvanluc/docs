# QTTN 01: Quy Trình Sinh Viên Gửi Yêu Cầu Hỗ Trợ & Sinh Mã Ticket (WF-01)

## 1. Mục Tiêu Quy Trình
Mô tả chi tiết luồng tương tác và xử lý kỹ thuật từng bước giữa Client (Web Frontend) và Server (Backend API) khi Sinh viên tạo một yêu cầu hỗ trợ mới. Quy trình đảm bảo tính chính xác của dữ liệu, kiểm tra dung lượng/định dạng file đính kèm, áp dụng cơ chế chống ghi nhận trùng lặp (Idempotency Key / Debounce) và tự động tính toán mốc thời hạn giải quyết SLA.

## 2. Tác Nhân Tham Gia (Actors) & Điều Kiện Tiên Quyết
- **Actors:**
  - **Sinh viên (Student):** Người dùng đã được xác thực, khởi tạo yêu cầu.
  - **Client (Web Frontend):** Giao diện Web Responsive hỗ trợ validate real-time và tạo UUID Idempotency.
  - **Server (Backend API):** Xử lý business logic, upload file, sinh mã Ticket, tính SLA và lưu CSDL.
- **Preconditions:**
  - Sinh viên đã đăng nhập thành công vào cổng UniSupport (Có JWT Access Token hợp lệ).
  - Tài khoản sinh viên ở trạng thái `ACTIVE`.

## 3. Lược Đồ Quy Trình Tương Tác (Sequence Diagram)
```plaintext
[Sinh viên]             [Client Frontend]             [Backend API / Storage]           [Database]
    │                           │                                │                           │
    │ ── 1. Mở Form Tạo Ticket ─>│                                │                           │
    │                           │ ── 2. Sinh UUID Client-ID ────>│                           │
    │                           │ ── 3. Fetch Danh mục Category >│                           │
    │                           │<── 4. Trả về Category List ────│                           │
    │ ── 5. Điền Form & File ──>│                                │                           │
    │ ── 6. Nhấn "Gửi yêu cầu" ─>│                                │                           │
    │                           │ ── 7. Validate Form Realtime ─>│                           │
    │                           │    (Nút Gửi chuyển Loading)    │                           │
    │                           │                                │                           │
    │                           │ ── 8. POST /api/v1/tickets ───>│                           │
    │                           │    Header: Client-Request-ID   │                           │
    │                           │    Body: Form Data + Files     │                           │
    │                           │                                │ ── 9. Check Unique Key ──>│
    │                           │                                │ ── 10. Validate & Upload ─>│
    │                           │                                │ ── 11. Calc SLA (+24h) ───>│
    │                           │                                │ ── 12. Save Ticket (NEW) ─>│
    │                           │<── 13. HTTP 201 Created ───────│                           │
    │                           │    (Mã Ticket: TK-20261009-0001)│                           │
    │<── 14. Hiển thị Toast ────│                                │                           │
    │    & Redirect sang Detail │                                │                           │
```

---

## 4. Các Bước Thực Hiện Chi Tiết (Flow of Events)

### Bước 1: Mở Form Tạo Ticket & Khởi Tạo Ngữ Cảnh
1. Sinh viên nhấn nút **Tạo yêu cầu mới** trên giao diện `/tickets`.
2. Client tự động sinh mã `Client-Request-ID` dạng UUID v4 (Ví dụ: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`) để phục vụ kiểm soát Idempotency Key.
3. Client gọi API `GET /api/v1/categories` để lấy danh sách nhóm vấn đề khả dụng.

### Bước 2: Nhập Thông Tin & Đính Kèm File
1. Sinh viên chọn Nhóm vấn đề (`category_id`) từ Dropdown.
2. Sinh viên nhập Tiêu đề (`title`) và Mô tả chi tiết (`description`).
3. Sinh viên chọn các file đính kèm (nếu có). Client thực hiện kiểm tra sơ bộ:
   - **File extension:** Chỉ chấp nhận `.pdf`, `.png`, `.jpg`, `.jpeg`.
   - **Dung lượng:** $\le 5\text{MB}$ ($5.242.880\text{ Byte}$) mỗi file.
   - **Số lượng:** Tối đa $5\text{ file}$.

### Bước 3: Client Validation & Gửi Request
1. Sinh viên nhấn nút **Gửi yêu cầu**.
2. Client vô hiệu hóa (Disable) nút Gửi yêu cầu, chuyển trạng thái sang Loading (hiển thị Spinner).
3. Client validate toàn bộ trường dữ liệu. Nếu có lỗi, hiển thị thông báo lỗi ngay dưới input tương ứng và ngắt tiến trình.
4. Nếu hợp lệ, Client gửi request `POST /api/v1/tickets` dạng `multipart/form-data` kèm Header `Client-Request-ID`.

### Bước 4: Server Processing & Lưu CSDL
1. **Kiểm tra Idempotency Key:** Server tìm `client_request_id` trong Database hoặc Cache:
   - Nếu đã tồn tại trong vòng $30\text{ giây}$ gần nhất: Từ chối xử lý request mới, trả về thông tin Ticket đã tạo trước đó (HTTP 200 OK / HTTP 409 Conflict).
2. **Validate Phía Server:**
   - Kiểm tra MIME Type thực tế của file (Binary Magic Bytes) để ngăn chặn giả mạo extension.
   - Sanitize chuỗi HTML/Script injection trong `title` và `description`.
   - Thực hiện `trim()` toàn bộ chuỗi đầu vào.
3. **Upload File:** Đẩy các file đính kèm hợp lệ lên Cloud Storage/S3, thu về danh sách `file_id` và `file_url`.
4. **Sinh Mã Ticket:** Sinh mã `ticket_id` theo chuẩn `TK-YYYYMMDD-XXXX` (Sequential number trong ngày).
5. **Tính Toán SLA:**
   - Xác định `department_id` mặc định dựa vào `category_id`.
   - Tính toán `sla_target_at` = Thời điểm hiện tại + $24\text{ giờ làm việc}$ (Loại trừ Thứ 7, Chủ Nhật và Ngày lễ nhà trường).
   - Đặt `sla_status` = `ON_TRACK`.
6. **Lưu CSDL:** Ghi nhận bản ghi Ticket mới với `status` = `NEW`, `assignee_id` = `NULL`, gắn liền với `student_id` từ Token.

### Bước 5: Trả Về Kết Quả
1. Server trả về `HTTP 201 Created` chứa object Ticket hoàn chỉnh.
2. Client nhận phản hồi, hiển thị Toast thông báo: *"Tạo yêu cầu hỗ trợ thành công! Mã Ticket: TK-20261009-0001"*.
3. Client tự động chuyển hướng người dùng sang trang chi tiết Ticket `/tickets/{ticket_id}`.

## 5. Ràng Buộc Kỹ Thuật & Quy Tắc Nghiệp Vụ (Business Rules)

| Tên quy tắc | Mô tả chi tiết & Handling Specs |
| :--- | :--- |
| **Bắt buộc nhập dữ liệu** | `category_id` (Dropdown bắt buộc chọn), `title` ($10 - 150\text{ ký tự}$), `description` ($20 - 2.000\text{ ký tự}$). |
| **Kiểm tra khoảng trắng** | Chuỗi nhập vào chỉ gồm toàn ký tự trắng (space, tab, newline) bị coi là không hợp lệ (`INVALID_INPUT`). |
| **Giới hạn File** | Tối đa $5\text{ file/Ticket}$. Mỗi file $\le 5\text{MB}$. Định dạng MIME Type: `application/pdf`, `image/png`, `image/jpeg`. |
| **Chống gửi trùng (Idempotency)** | Mọi request gửi lên phải kèm `Client-Request-ID`. Nếu trùng Key trong $30\text{ giây}$, Server từ chối ghi nhận record mới. |
| **UI State Control** | Ngay khi bấm Gửi yêu cầu, nút bị Disable và đổi trạng thái Loading. Loại bỏ hoàn toàn khả năng double click từ người dùng. |
| **Mã Ticket duy nhất** | Mã định danh dạng `TK-YYYYMMDD-XXXX` sinh tự động phía Server. `XXXX` là số thứ tự tăng dần từ 0001 mỗi ngày. |
| **Tính thời hạn SLA** | Hạn chót xử lý mặc định là $24\text{ giờ làm việc}$. Hệ thống tự động bỏ qua giờ nghỉ lễ và cuối tuần khi tính `sla_target_at`. |

## 6. Luồng Ngoại Lệ & Mã Lỗi Hệ Thống (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Sinh viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Thiếu thông tin bắt buộc / Nhập toàn space** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng điền đầy đủ tiêu đề và nội dung mô tả (tối thiểu 20 ký tự)." | Hiển thị lỗi dưới input field tương ứng, kích hoạt lại nút Gửi. |
| **File quá dung lượng (> 5MB)** | `400 Bad Request`<br><br>`FILE_EXCEEDS_LIMIT` | "File [Tên_File] vượt quá dung lượng cho phép (tối đa 5MB)." | Đánh dấu đỏ file lỗi trong danh sách upload, từ chối gửi request. |
| **File sai định dạng / Giả mạo đuôi file** | `400 Bad Request`<br><br>`FILE_TYPE_NOT_ALLOWED` | "Chỉ chấp nhận file định dạng PDF hoặc hình ảnh (PNG, JPG)." | Loại bỏ file không hợp lệ khỏi danh sách đính kèm. |
| **Mạng lag / Bấm gửi nhiều lần liên tiếp** | `409 Conflict`<br><br>`DUPLICATE_REQUEST` | "Yêu cầu của bạn đang được xử lý. Vui lòng không bấm liên tục." | Client giữ nguyên giao diện Loading, chặn gửi request trùng thứ hai. |
| **Lỗi Server / Storage ngắt kết nối** | `500 Internal Server Error`<br><br>`INTERNAL_SERVER_ERROR` | "Không thể tạo yêu cầu do sự cố hệ thống. Vui lòng thử lại sau." | Báo Toast error, giữ nguyên dữ liệu đã nhập trên Form để người dùng bấm thử lại. |