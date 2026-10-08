# Phân Hệ Sinh Viên (M01 - Student Portal)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ Sinh viên cung cấp giao diện Web Responsive (tương thích Desktop và Mobile) cho sinh viên Aurora University. Phân hệ bao gồm các nhóm chức năng chính: Xác thực tài khoản, Khởi tạo yêu cầu hỗ trợ, Quản lý & Theo dõi tiến độ Ticket, Bổ sung hồ sơ theo yêu cầu, Xem kết quả và Đánh giá chất lượng phục vụ.

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STU-01] Sinh viên đăng nhập hệ thống

#### 1. Mô tả & Phạm vi
Cho phép sinh viên đăng nhập vào hệ thống UniSupport bằng tài khoản cá nhân do nhà trường cấp. Hệ thống áp dụng cơ chế xác thực tập trung và trả về token quản lý phiên làm việc.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên.
- **Preconditions:** Tài khoản sinh viên đã tồn tại trên cơ sở dữ liệu hệ thống, ở trạng thái hoạt động (ACTIVE).

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Trường dữ liệu đầu vào:**
  - **Username / Student ID:** Bắt buộc, chuỗi không khoảng trắng, độ dài từ 6 - 20 ký tự, tự động `trim()` khoảng trắng hai đầu.
  - **Password:** Bắt buộc, độ dài từ 6 - 50 ký tự, phân biệt chữ hoa/chữ thường.
- **Xử lý khoảng trắng:** Tự động loại bỏ khoảng trắng thừa đầu/cuối của Username trước khi gửi request.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Trạng thái Nút Đăng nhập:**
  - Vô hiệu hóa (Disabled) khi Username hoặc Password đang trống.
  - Khi nhấn Đăng nhập, nút chuyển sang trạng thái Loading (hiển thị spinner, disable tương tác), đồng thời vô hiệu hóa toàn bộ các input field trên form.
- **Cơ chế chống gửi lặp (Debounce/Throttle):** Áp dụng Debounce/Disable form ngay khi gửi request để chặn hoàn toàn thao tác click liên tiếp (double click, spam click).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập trang `/login`.
2. Hệ thống kiểm tra phiên làm việc hiện tại:
   - Nếu đã có Token hợp lệ và còn hạn -> Tự động chuyển hướng sang `/dashboard`.
   - Nếu chưa -> Hiển thị form đăng nhập.
3. Sinh viên nhập Username, Password và nhấn Đăng nhập (hoặc bấm phím Enter).
4. Client thực hiện validate dữ liệu đầu vào. Nếu hợp lệ, gửi request đăng nhập.
5. Server xác thực thông tin:
   - Trả về Token xác thực (JWT Access Token & Refresh Token) và thông tin Profile cơ bản (`student_id`, `full_name`, `email`, `role`).
6. Client lưu trữ Token an toàn (HTTP-Only Cookie hoặc Storage có bảo mật) và chuyển hướng người dùng đến trang `/dashboard`.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Lỗi Validation Client:** Hiển thị message bên dưới field tương ứng: *"Vui lòng nhập tên đăng nhập / mật khẩu"*.
- **Thông tin đăng nhập sai (Mã lỗi 401 Unauthorized):** Hiển thị Alert/Toast error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản bị khóa (403 Forbidden / INACTIVE / BLOCKED):** Hiển thị Alert error: *"Tài khoản của bạn đã bị khóa. Vui lòng liên hệ Quản trị viên."*
- **Lỗi kết nối / Server lỗi (500 / 503):** Hiển thị Toast error: *"Hệ thống đang gặp sự cố. Vui lòng thử lại sau ít phút."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập thành công với credential đúng -> Lưu phiên làm việc và chuyển đến `/dashboard` trong dưới 1.5 giây.
- **AC-02:** Sai credential -> Hiển thị thông báo lỗi chi tiết, không lưu session, mật khẩu bị xóa khỏi input field.
- **AC-03:** Click nút Đăng nhập nhiều lần liên tiếp -> Chỉ gửi đúng 01 request duy nhất lên Server.
- **AC-04:** Chuyển đổi thiết bị / Resize màn hình -> Giao diện form hiển thị chuẩn responsive trên Mobile (khoảng cách lề, font size, button size chuẩn touch point).

---

### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ (Tạo Ticket)

#### 1. Mô tả & Phạm vi
Cung cấp biểu mẫu cho phép sinh viên tạo yêu cầu hỗ trợ mới gửi đến các phòng ban, kèm theo tài liệu/hình ảnh minh chứng.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Phiên làm việc hợp lệ.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Danh mục nhóm vấn đề (Category):** Dropdown bắt buộc chọn. Dữ liệu category lấy từ API danh mục của hệ thống.
- **Tiêu đề yêu cầu (Title):** Bắt buộc, chuỗi từ 10 đến 150 ký tự. Không chấp nhận chuỗi chỉ chứa khoảng trắng.
- **Nội dung chi tiết (Description):** Bắt buộc, chuỗi từ 20 đến 2000 ký tự. Tự động `trim()` khoảng trắng hai đầu. Không chấp nhận chuỗi chỉ chứa ký tự trắng.
- **File đính kèm (Attachments):**
  - **Số lượng:** Tối đa 5 file / 1 Ticket.
  - **Dung lượng:** Tối đa 5MB / 1 file.
  - **Định dạng cho phép:** `.pdf`, `.png`, `.jpg`, `.jpeg` (Kiểm tra cả file extension và MIME type thực tế của file).

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Form Validation Real-time:** Báo lỗi ngay dưới input field khi người dùng blur khỏi field hoặc khi bấm Gửi yêu cầu.
- **Upload File UI:** Hiển thị danh sách file đã chọn kèm tên file, dung lượng, nút Xóa file. Hiển thị thanh progress bar trong quá trình tải file lên.
- **Nút Gửi yêu cầu:** Đổi sang trạng thái Loading ngay khi bấm. Disable form để tránh thao tác chỉnh sửa trong lúc request đang xử lý.

#### 5. Cơ chế chống trùng lặp dữ liệu (Idempotency)
- **Idempotency Key:** Client tự động sinh một mã `Client-Request-ID` (UUID v4) ngay khi render form tạo ticket. Mã này được gắn vào Header của request gửi Ticket.
- **Xử lý phía Server:** Server kiểm tra `Client-Request-ID`. Nếu trùng trong thời gian timeout (ví dụ: 30 giây), Server từ chối ghi nhận record mới và trả về kết quả của Ticket đã tạo trước đó.
- **Handling Retry/Lag Network:** Trường hợp mất mạng hoặc timeout từ Client, nếu Client bấm gửi lại với cùng `Client-Request-ID`, hệ thống không bao giờ sinh ra Ticket thứ 2.

#### 6. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên bấm nút Tạo yêu cầu mới.
2. Hệ thống tải danh mục Category và render Form. Sinh ngữ cảnh `Client-Request-ID`.
3. Sinh viên điền các trường thông tin và tải file đính kèm (nếu có).
4. Client kiểm tra validation toàn bộ form.
5. Sinh viên nhấn Gửi yêu cầu.
6. Client gọi API upload file (hoặc gửi multipart) kèm theo `Client-Request-ID`.
7. Server khởi tạo Ticket với trạng thái mặc định là `NEW`, ghi nhận log khởi tạo, trả về mã Ticket dạng chuẩn (VD: `TK-20261009-0001`).
8. Client nhận phản hồi thành công, hiển thị Modal/Toast thông báo thành công kèm mã Ticket, tự động chuyển về trang `/tickets/{ticket_id}`.

#### 7. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **File sai định dạng/Quá dung lượng:** Block file ngay tại Client, hiển thị message error dưới khu vực upload: *"File [Tên_File] vượt quá 5MB hoặc không đúng định dạng (.pdf, .png, .jpg)"*.
- **Upload thất bại:** Nếu API upload file lỗi, ngắt toàn bộ tiến trình tạo Ticket, hiển thị lỗi: *"Không thể tải file lên. Vui lòng thử lại"*.
- **Request bị trùng lặp (409 Conflict):** Trả về thông tin Ticket đã tạo, chuyển người dùng đến chi tiết Ticket đó.

#### 8. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Điền đầy đủ thông tin + File hợp lệ -> Tạo 01 Ticket duy nhất trạng thái `NEW`, sinh đúng định dạng Mã Ticket.
- **AC-02:** Nhập khoảng trắng vào tiêu đề/mô tả -> Nút gửi bị khóa hoặc hiển thị lỗi validation *"Nội dung không được để trống"*.
- **AC-03:** Kéo thả 6 file hoặc file `.exe` / `.docx` -> Hệ thống từ chối nhận file và hiển thị lý do rõ ràng.
- **AC-04:** Bấm nút Gửi liên tục 5 lần / F5 gửi lại request -> Chỉ duy nhất 01 Ticket được tạo trên Database.

---

### [FR-STU-03] Sinh viên theo dõi tiến độ & bổ sung hồ sơ

#### 1. Mô tả & Phạm vi
Cung cấp giao diện xem danh sách các Ticket cá nhân, tra cứu chi tiết luồng xử lý, xem lịch sử phản hồi từ nhân viên và thực hiện bổ sung file/giấy tờ khi có yêu cầu.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Đã có dữ liệu Ticket trong hệ thống.

#### 3. Phân trang, Bộ lọc & Sắp xếp (List View Rules)
- **Phân trang:** Mặc định 10 Ticket / trang. Có bộ chọn chuyển trang (Pagination).
- **Bộ lọc Trạng thái:** Filter theo danh sách: Tất cả, `NEW` (Mới tạo), `IN_PROGRESS` (Đang xử lý), `NEED_MORE_INFO` (Cần bổ sung), `RESOLVED` (Đã xử lý), `CLOSED` (Đã đóng).
- **Sắp xếp:** Mặc định xếp theo thời gian cập nhật mới nhất (`updated_at DESC`).
- **Phân quyền truy cập dữ liệu:** Query dữ liệu cứng theo `student_id` của tài khoản đang đăng nhập. Không cho phép đổi ID trên URL để xem Ticket của sinh viên khác.

#### 4. Quy tắc Bổ sung Hồ sơ (Ticket State Machine)
- **Điều kiện hiển thị Form Bổ sung:** Nút Bổ sung thông tin VÀ khu vực upload file CHỈ hiển thị khi Ticket có trạng thái chính xác là `NEED_MORE_INFO`.
- **Ràng buộc chỉnh sửa:** Không cho phép sửa Title, Category, hay các phản hồi trước đó. Chỉ được nhập thêm Lời nhắn bổ sung (Optional, max 1000 ký tự) và File đính kèm bổ sung (Max 5 file, tuân thủ rule dung lượng/định dạng như FR-STU-02).
- **Chuyển đổi trạng thái (State Transition):** Sau khi sinh viên gửi bổ sung thành công, hệ thống tự động chuyển trạng thái Ticket từ `NEED_MORE_INFO` sang `IN_PROGRESS`.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập trang `/tickets`. Hệ thống hiển thị danh sách Ticket cá nhân.
2. Sinh viên click chọn 1 Ticket. Client chuyển hướng sang `/tickets/{ticket_id}`.
3. Hệ thống hiển thị chi tiết Ticket: Mã ticket, Ngày tạo, Trạng thái, Phòng ban phụ trách, Timeline các bước xử lý và Lịch sử trao đổi (Conversation log).
4. Nếu trạng thái là `NEED_MORE_INFO`:
   - Hiển thị hộp thông điệp yêu cầu từ nhân viên và khung upload bổ sung.
   - Sinh viên chọn file đính kèm, nhập lời nhắn (nếu có) và nhấn Gửi bổ sung.
   - Client gửi request cập nhật.
   - Server lưu file, ghi nhận tin nhắn mới vào Conversation log, cập nhật `status = IN_PROGRESS`, gửi notify cho Nhân viên phụ trách.
5. Giao diện Client cập nhật lại trạng thái Ticket thành `IN_PROGRESS`, ẩn Form bổ sung thông tin.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Truy cập Ticket của người khác (403 Forbidden / 404 Not Found):** Hiển thị màn hình lỗi: *"Không tìm thấy yêu cầu hoặc bạn không có quyền truy cập."* kèm nút Quay lại danh sách.
- **Gửi bổ sung khi Ticket đã chuyển trạng thái khác (400 Bad Request):** Nếu nhân viên đã hủy hoặc đổi trạng thái Ticket ở tab khác, khi sinh viên bấm gửi sẽ báo lỗi: *"Trạng thái Ticket đã thay đổi, không thể bổ sung hồ sơ vào lúc này."* và tự động reload lại dữ liệu Ticket.

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Trang danh sách phân trang chuẩn 10 item/trang, filter đúng theo từng trạng thái chọn.
- **AC-02:** Thay đổi Ticket ID trên URL sang ID thuộc về sinh viên khác -> Trả về lỗi 403/404, không lộ dữ liệu.
- **AC-03:** Bổ sung file thành công khi Ticket ở `NEED_MORE_INFO` -> Trạng thái Ticket lập tức đổi sang `IN_PROGRESS` trên cả giao diện và Database.
- **AC-04:** Ticket ở trạng thái `IN_PROGRESS`, `RESOLVED`, `CLOSED` -> Ẩn hoàn toàn tính năng upload/gửi file bổ sung.

---

### [FR-STU-04] Xem kết quả giải quyết & Đánh giá mức độ hài lòng

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem nội dung phản hồi kết quả xử lý cuối cùng từ nhà trường và thực hiện đánh giá chất lượng dịch vụ cho Ticket đã hoàn tất.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket của sinh viên đã được Nhân viên/Quản lý xử lý xong và chuyển sang trạng thái `RESOLVED` hoặc `CLOSED`.

#### 3. Quy tắc Dữ liệu & Đánh giá (Business & Validation Rules)
- **Trường thông tin Đánh giá:**
  - **Rating:** Bắt buộc, số nguyên từ 1 đến 5 (tương ứng từ 1 sao đến 5 sao).
  - **Feedback / Comment:** Không bắt buộc, tối đa 500 ký tự. Tự động `trim()`.
- **Ràng buộc số lần đánh giá:** Mỗi Ticket chỉ được đánh giá duy nhất 01 lần.
- **Khóa biểu mẫu:** Khi Ticket đã có dữ liệu đánh giá, hệ thống chuyển Form đánh giá sang trạng thái Read-Only (Hiển thị số sao và nhận xét đã gửi, không cho thao tác bấm gửi lại).

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên mở chi tiết Ticket đã xử lý xong tại `/tickets/{ticket_id}`.
2. Hệ thống hiển thị rõ ràng phần Kết quả giải quyết (Gồm câu trả lời, file đính kèm kết quả từ nhân viên nếu có, thời gian hoàn thành).
3. Kiểm tra trạng thái đánh giá của Ticket:
   - Chưa đánh giá: Hiển thị Component Đánh giá (5 ngôi sao tương tác + Textarea nhập nhận xét + Nút Gửi đánh giá).
   - Đã đánh giá: Hiển thị kết quả đánh giá cũ dạng Read-only.
4. Sinh viên chọn số sao, nhập nhận xét và bấm Gửi đánh giá.
5. Client gửi request lưu đánh giá.
6. Server ghi nhận thông tin đánh giá, chuyển trạng thái Ticket từ `RESOLVED` sang `CLOSED` (nếu đang ở `RESOLVED`), lưu timestamp `rated_at`.
7. Client hiển thị Toast thông báo: *"Cảm ơn bạn đã đánh giá dịch vụ!"*, đồng thời chuyển Component đánh giá sang dạng Read-only.

#### 5. Luồng ngoại lệ & Race Condition Handling
- **Đánh giá đồng thời nhiều tab (Race Condition):** Nếu sinh viên mở 2 tab cùng 1 Ticket và bấm gửi ở tab A trước:
  - **Tab A:** Gửi thành công.
  - **Tab B:** Khi bấm gửi, Server trả về mã lỗi 409 Conflict hoặc 400 Bad Request với message: *"Ticket này đã được đánh giá trước đó."*
  - **Client tại Tab B nhận lỗi:** Tự động ẩn form nhập và fetch lại dữ liệu đánh giá đã lưu để hiển thị dạng Read-only.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đánh giá 5 sao + nhận xét hợp lệ -> Lưu chính xác dữ liệu vào hệ thống, hiển thị đúng trạng thái đã đánh giá.
- **AC-02:** Không chọn số sao mà bấm Gửi -> Báo lỗi validation: *"Vui lòng chọn mức độ hài lòng (từ 1 đến 5 sao)"*.
- **AC-03:** Sau khi gửi đánh giá thành công, F5 lại trang hoặc mở lại Ticket -> Form đánh giá ở trạng thái Read-only, không thể chỉnh sửa hay gửi lại.
- **AC-04:** Lỗi mạng khi gửi đánh giá -> Thông báo lỗi, giữ nguyên số sao và nhận xét sinh viên đã nhập trên giao diện để sinh viên bấm thử lại.

---

## III. BẢNG MÃ LỖI CHUẨN DÙNG CHUNG CHO DEV (SYSTEM ERROR CODES)

Để Frontend và Backend đồng bộ xử lý không cần trao đổi thêm, phân hệ áp dụng chuẩn response lỗi như sau:

| HTTP Status | Error Code | Message hiển thị người dùng | Kịch bản áp dụng |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | *"Dữ liệu nhập vào không hợp lệ. Vui lòng kiểm tra lại."* | Lỗi validation trường dữ liệu đầu vào. |
| **400** | `FILE_EXCEEDS_LIMIT` | *"File đính kèm vượt quá dung lượng 5MB."* | Upload file > 5MB. |
| **400** | `FILE_TYPE_NOT_ALLOWED` | *"Chỉ chấp nhận file .pdf, .png, .jpg, .jpeg."* | Upload sai định dạng file. |
| **401** | `UNAUTHORIZED` | *"Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại."* | Token hết hạn hoặc không hợp lệ. |
| **403** | `FORBIDDEN_ACCESS` | *"Bạn không có quyền truy cập vào tài nguyên này."* | Sinh viên xem Ticket của người khác. |
| **404** | `TICKET_NOT_FOUND` | *"Không tìm thấy dữ liệu Ticket yêu cầu."* | Ticket ID không tồn tại. |
| **409** | `ALREADY_RATED` | *"Ticket này đã được đánh giá trước đó."* | Gửi đánh giá 2 lần cho 1 Ticket. |
| **409** | `DUPLICATE_REQUEST` | *"Yêu cầu đang được xử lý, vui lòng không thao tác lặp lại."* | Trùng Client-Request-ID. |
| **500** | `INTERNAL_SERVER_ERROR` | *"Hệ thống gặp sự cố kỹ thuật. Vui lòng thử lại sau."* | Lỗi Server/Database unhandled. |