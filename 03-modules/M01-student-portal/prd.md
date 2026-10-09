# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Sinh Viên (PRD - M01 Student Portal)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Sinh viên (Student Portal)** là cổng giao tiếp số tập trung dành cho khoảng 3.000 sinh viên tại **Aurora University**. Phân hệ cho phép sinh viên đăng nhập bằng tài khoản do ADMIN cấp, tạo phiếu hỗ trợ (Ticket), theo dõi tiến độ giải quyết, bổ sung giấy tờ khi được yêu cầu, nhận thông báo cập nhật và đánh giá chất lượng dịch vụ.

### Luồng sử dụng và trách nhiệm

Sinh viên đăng nhập bằng tài khoản ADMIN cấp tại cổng sinh viên. Sinh viên tạo yêu cầu hỗ trợ và theo dõi tiến độ tại đây. Khi nhân viên yêu cầu bổ sung, sinh viên nộp tại FR-STU-03. Khi yêu cầu được giải quyết, sinh viên xem kết quả và đánh giá tại FR-STU-04.

Hệ thống không hỗ trợ tự đăng ký tài khoản. Sinh viên không được chỉnh sửa nội dung Ticket (`title`, `category_id`, `description`) sau khi đã gửi, kể cả khi Ticket đang ở `NEED_MORE_INFO`.

### Danh mục Chức năng Cốt lõi

- **[FR-STU-01]** Đăng nhập tài khoản sinh viên.
- **[FR-STU-02]** Gửi yêu cầu hỗ trợ (Tạo Ticket kèm file đính kèm ảnh/PDF).
- **[FR-STU-03]** Theo dõi tiến độ, xem lịch sử xử lý & bổ sung thông tin/giấy tờ theo yêu cầu.
- **[FR-STU-04]** Xem kết quả giải quyết & Đánh giá mức độ hài lòng.

---

### Nhóm vấn đề và phòng ban tiếp nhận

| Nội dung | Quy tắc đã có trong PRD gốc |
| --- | --- |
| Ý nghĩa nhóm vấn đề | Phân loại nội dung yêu cầu, ví dụ Học phí, Đăng ký môn học, Giấy xác nhận; đây là ví dụ, không phải danh mục mới cố định. |
| Nguồn và chủ sở hữu | Danh mục hệ thống do ADMIN quản lý; sinh viên chọn từ danh sách có sẵn, không tự tạo danh mục tại form gửi yêu cầu. |
| Phòng ban | Mỗi nhóm vấn đề gắn mặc định với một phòng ban nhận yêu cầu. Sinh viên chọn nhóm vấn đề; không nhầm tên phòng ban với tên nhóm vấn đề. |
| Nhân viên | Phân loại lại bằng danh mục phòng ban tại FR-STF-02; chuyển phòng ban tại FR-STF-03 khi cần. |

### Giới hạn công sức và mã yêu cầu

Mã FR trong danh mục dưới đây giữ nguyên theo PRD đã chốt. Giờ M01 được đối chiếu theo các dòng Resource!3:7: **124 giờ cơ sở + 4 giờ dự phòng = 128 giờ kế hoạch**. Xem [bảng Resources](../../Phan_bo_Resources_Antigravity.md); số thứ tự dòng công sức không phải mã FR. Đăng nhập các cổng dùng chung R-ADM-01, không có estimate bổ sung. Những tên công việc nguồn chưa có đặc tả thống nhất không tự trở thành chức năng mới.

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STU-01] Đăng nhập tài khoản sinh viên

#### 1. Mô tả & Phạm vi
Cho phép Sinh viên đăng nhập vào Cổng Sinh viên UniSupport bằng tài khoản cá nhân (Mã sinh viên / Email trường) do Quản trị viên hệ thống (ADMIN) khởi tạo và cấp sẵn.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên dùng tài khoản đã được ADMIN cấp để đăng nhập vào cổng sinh viên.
2. Đăng nhập thành công thì vào trang danh sách yêu cầu cá nhân.
3. Sai thông tin hoặc tài khoản bị khóa thì hiển thị thông báo tương ứng; không tạo phiên làm việc.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên Aurora University.
- **Preconditions:** Tài khoản đã được ADMIN khởi tạo theo FR-MNG-04, ở trạng thái `ACTIVE`, có `role = STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Trường dữ liệu đầu vào:**
  - **Username / Email:** Bắt buộc, tự động `trim()` khoảng trắng hai đầu.
  - **Password:** Bắt buộc, độ dài 6 - 50 ký tự.
- **Scope & Session Context:** Sau khi xác thực thành công, Token phải chứa: `user_id`, `role = STUDENT`, `department_id = NULL`, `permissions_list`.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Trạng thái Nút Đăng nhập:** Disable khi thông tin trống. Chuyển Loading (kèm spinner) và khóa toàn bộ Form khi request đang xử lý.
- **Redirect Rule:** Đăng nhập thành công → Tự động điều hướng về `/student/tickets`.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập `/student/login`.
2. Kiểm tra phiên làm việc: Nếu Token hợp lệ → Chuyển hướng sang `/student/tickets`.
3. Nhập Username/Email và Password, nhấn Đăng nhập (hoặc phím Enter).
4. Client validate form → Gửi request đăng nhập.
5. Server xác thực thông tin, kiểm tra vai trò `STUDENT`:
   - Trả về Token xác thực (JWT) + Profile (`student_id`, `full_name`).
6. Client lưu Token an toàn, chuyển hướng sang `/student/tickets`.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Credential không đúng (401 Unauthorized):** Hiển thị Alert error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản không phải STUDENT (403 Forbidden):** Hiển thị Alert error: *"Tài khoản của bạn không có quyền truy cập cổng Sinh viên."*
- **Tài khoản bị khóa (403 Forbidden / INACTIVE):** Hiển thị Alert error: *"Tài khoản đã bị vô hiệu hóa. Vui lòng liên hệ Quản trị viên."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập đúng tài khoản Student → Chuyển sang trang danh sách Ticket cá nhân trong dưới 1.5s.
- **AC-02:** Tài khoản Staff/Manager cố gắng đăng nhập tại cổng Student → Báo lỗi 403 từ chối truy cập.
- **AC-03:** Click Đăng nhập liên tiếp → Chỉ phát sinh 01 request duy nhất.

---

### [FR-STU-02] Gửi yêu cầu hỗ trợ (Tạo Ticket)

#### 1. Mô tả & Phạm vi
Cho phép sinh viên khởi tạo một yêu cầu hỗ trợ mới bằng cách chọn nhóm vấn đề (Category), nhập tiêu đề, nội dung chi tiết và đính kèm tài liệu minh chứng. Hệ thống tự động sinh mã Ticket duy nhất và phân tuyến đến đúng phòng ban phụ trách theo danh mục đã chọn.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên bấm tạo yêu cầu mới, chọn nhóm vấn đề từ danh mục phòng ban cung cấp, nhập tiêu đề và nội dung, đính kèm file nếu cần.
2. Bấm Gửi; nút vô hiệu hóa ngay để chống bấm đúp. Thành công thì hiển thị mã Ticket và thông báo.
3. Ticket vào hàng đợi đúng phòng ban theo danh mục đã chọn; sinh viên theo dõi tiến độ tại FR-STU-03.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Tài khoản `ACTIVE`, có `role = STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Nhóm vấn đề (`category_id`):** Bắt buộc chọn từ Dropdown danh mục được cấu hình bởi ADMIN.
- **Tiêu đề (`title`):** Bắt buộc, 10 - 150 ký tự. Tự động `trim()`.
- **Nội dung mô tả (`description`):** Bắt buộc, 20 - 2000 ký tự. Tự động `trim()`.
- **File đính kèm (`attachments`):** Không bắt buộc. Tối đa **5 file/Ticket**. Mỗi file ≤ **5MB (5.242.880 Bytes)**. Định dạng MIME thực tế (Magic Bytes): `.pdf`, `.png`, `.jpg`, `.jpeg`.
- **Chống trùng lặp (Idempotency):** Client sinh `Client-Request-ID` (UUID v4) khi mở form, gửi kèm trong Header. Server khóa Redis Key trong 30 giây.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Nút Gửi:** Vô hiệu hóa ngay khi bấm lần đầu, chuyển trạng thái Loading để chống đúp click.
- **Thành công:** Hiển thị Toast: *"Yêu cầu [Mã_Ticket] đã được gửi thành công!"* và điều hướng sang trang chi tiết Ticket.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập `/student/tickets/new`.
2. Client sinh `Client-Request-ID` (UUID v4) và gắn vào state form.
3. Sinh viên chọn `category_id`, nhập `title` và `description`, đính kèm file (nếu có).
4. Sinh viên nhấn **Gửi yêu cầu**. Client vô hiệu hóa nút và chuyển Loading.
5. Client validate client-side (độ dài, file type, file size).
6. Client gửi request `POST /api/v1/student/tickets` kèm Header `X-Client-Request-ID`.
7. Server xử lý:
   - Kiểm tra `Client-Request-ID` trong Redis → Nếu trùng, trả về `409 DUPLICATE_REQUEST`.
   - Đọc `student_id` từ JWT (bỏ qua mọi `student_id` gửi từ body).
   - Sinh mã Ticket `TK-YYYYMMDD-XXXX` qua Redis Atomic Counter.
   - Lưu Ticket, upload file lên Private Storage, ghi Audit Log.
   - Phát Notification tới Queue phòng ban tương ứng.
8. Server trả về `HTTP 201 Created` kèm `ticket_id`, `status = NEW`, `sla_target_at`.
9. Client hiển thị Toast thành công và điều hướng sang `/student/tickets/{ticket_id}`.

#### 6. Luồng ngoại lệ & Mã lỗi (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Sinh viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Thiếu thông tin bắt buộc / Nhập toàn space** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng chọn nhóm vấn đề, nhập tiêu đề từ 10 đến 150 ký tự và mô tả từ 20 đến 2000 ký tự." | Hiển thị lỗi dưới input field tương ứng, kích hoạt lại nút Gửi. |
| **File quá dung lượng (> 5MB)** | `400 Bad Request`<br><br>`FILE_EXCEEDS_LIMIT` | "File [Tên_File] vượt quá dung lượng cho phép (tối đa 5MB)." | Đánh dấu đỏ file lỗi trong danh sách upload, từ chối gửi request. |
| **File sai định dạng / Giả mạo đuôi file** | `400 Bad Request`<br><br>`FILE_TYPE_NOT_ALLOWED` | "Chỉ chấp nhận file định dạng PDF hoặc hình ảnh (PNG, JPG, JPEG)." | Loại bỏ file không hợp lệ khỏi danh sách đính kèm. |
| **Mạng lag / Bấm gửi nhiều lần liên tiếp** | `409 Conflict`<br><br>`DUPLICATE_REQUEST` | "Yêu cầu của bạn đang được xử lý. Vui lòng không bấm liên tục." | Client giữ nguyên giao diện Loading, chặn gửi request trùng thứ hai. |
| **Lỗi Server / Storage ngắt kết nối** | `500 Internal Server Error`<br><br>`INTERNAL_SERVER_ERROR` | "Không thể tạo yêu cầu do sự cố hệ thống. Vui lòng thử lại sau." | Báo Toast error, giữ nguyên dữ liệu đã nhập trên Form để bấm thử lại. |

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Nhập đúng và đủ thông tin → Tạo đúng 01 Ticket với mã duy nhất `TK-YYYYMMDD-XXXX`, trạng thái `NEW`.
- **AC-02:** Click Gửi liên tục nhiều lần → Hệ thống chỉ tạo 01 Ticket duy nhất (kiểm tra cả Client-side disable lẫn Server-side idempotency).
- **AC-03:** File đính kèm lưu an toàn ở Private Storage và hiển thị đúng trong chi tiết Ticket.
- **AC-04:** Upload file 12MB → Client chặn ngay với thông báo *"Dung lượng tệp vượt quá 5MB cho phép"*.
- **AC-05:** Upload file `.mp4` → Client/Server từ chối với thông báo định dạng không hợp lệ.

---

### [FR-STU-03] Theo dõi tiến độ & Bổ sung thông tin/giấy tờ

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem danh sách Ticket cá nhân, theo dõi trạng thái xử lý theo thời gian thực và thực hiện bổ sung thông tin/file đính kèm khi Ticket ở trạng thái `NEED_MORE_INFO`.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên mở danh sách yêu cầu, lọc hoặc tìm theo mã, mở chi tiết để đọc lịch sử cập nhật và thông tin người phụ trách.
2. Khi nhận thông báo cần bổ sung, sinh viên mở yêu cầu đang ở `NEED_MORE_INFO`, đọc nội dung nhân viên yêu cầu, tải file và/hoặc nhập lời nhắn bổ sung rồi gửi.
3. Gửi thành công thì trạng thái tự động đổi về `IN_PROGRESS` và nhân viên nhận thông báo; sinh viên tiếp tục theo dõi.
4. Trong suốt quá trình bổ sung, sinh viên không được chỉnh sửa `title`, `category_id` hay `description` ban đầu.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions (xem danh sách):** Tài khoản `ACTIVE`, có `role = STUDENT`.
- **Preconditions (bổ sung):** Ticket đang ở trạng thái `NEED_MORE_INFO` và `student_id == current_user.id`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Phân quyền dữ liệu:** Sinh viên chỉ xem và thao tác trên Ticket do chính mình tạo (`WHERE student_id == current_user_id`).
- **Nội dung bổ sung (`supplement_note`):** Không bắt buộc, tối đa 1.000 ký tự. Tự động `trim()`.
- **File bổ sung:** Tối đa **5 file** mỗi lần gửi. Mỗi file ≤ **5MB**. Định dạng MIME: `.pdf`, `.png`, `.jpg`, `.jpeg`.
- **Ràng buộc:** Phải có ít nhất 01 file đính kèm hoặc 01 lời nhắn bổ sung (không được gửi trống hoàn toàn).
- **Không cho chỉnh sửa nội dung gốc:** `title`, `description`, `category_id` ở trạng thái Read-Only trong mọi trường hợp.

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập `/student/tickets` → Xem danh sách Ticket sắp xếp theo `created_at DESC`.
2. Sinh viên lọc theo trạng thái (`NEW`, `IN_PROGRESS`, `NEED_MORE_INFO`, `TRANSFERRED`, `RESOLVED`, `CLOSED`, `REJECTED`) hoặc tìm theo mã Ticket.
3. Sinh viên nhấn vào một Ticket để mở trang Chi tiết `/student/tickets/{ticket_id}`.
4. Trang chi tiết hiển thị: Tiêu đề, mô tả, trạng thái, nhân viên phụ trách (nếu có), Timeline lịch sử, file đính kèm gốc.
5. **Nếu Ticket ở `NEED_MORE_INFO`:**
   - Hệ thống tự động mở Khung Bổ sung thông tin kèm nội dung yêu cầu từ Nhân viên.
   - Các trường `title`, `category_id` hiển thị Read-Only.
   - Sinh viên nhập `supplement_note` (tùy chọn) và/hoặc đính kèm file bổ sung.
   - Sinh viên nhấn **Xác nhận gửi bổ sung**.
   - Client validate, gửi `POST /api/v1/student/tickets/{ticket_id}/supplement`.
   - Server kiểm tra `status == NEED_MORE_INFO`, cập nhật `status = IN_PROGRESS`, lưu Conversation log, phát Notification cho Nhân viên.
   - Client hiển thị Toast: *"Đã gửi hồ sơ bổ sung thành công!"*, đóng Khung bổ sung và cập nhật Badge trạng thái.

#### 5. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Truy cập Ticket của người khác:** Server trả `403 FORBIDDEN_ACCESS`. Message: *"Không tìm thấy yêu cầu hoặc bạn không có quyền truy cập."*
- **Gửi bổ sung mà không có file và note:** Báo lỗi validation: *"Vui lòng tải lên ít nhất 01 file đính kèm hoặc nhập lời nhắn bổ sung."*
- **Upload file bổ sung sai định dạng/quá 5MB:** Sai định dạng hiển thị lỗi `400 FILE_TYPE_NOT_ALLOWED`; quá 5MB hiển thị lỗi `400 FILE_EXCEEDS_LIMIT`, theo bảng mã lỗi đã có. Đánh dấu đỏ file lỗi, ngăn submit.
- **Ticket không còn ở `NEED_MORE_INFO` khi submit:** `400 INVALID_TICKET_STATE`. Reload lại dữ liệu Ticket để cập nhật UI.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Danh sách Ticket chỉ hiển thị đúng Ticket của sinh viên đang đăng nhập.
- **AC-02:** Timeline hiển thị đúng trình tự thời gian các bước chuyển trạng thái và lịch sử trao đổi.
- **AC-03:** Sinh viên sao chép URL Ticket của bạn học và mở → Hệ thống trả về lỗi `403 Forbidden`.
- **AC-04:** Gửi bổ sung thành công → Trạng thái Ticket tự động đổi sang `IN_PROGRESS`, nhân viên nhận được thông báo.
- **AC-05:** Nhân viên gửi yêu cầu bổ sung theo FR-STF-04 → Sinh viên thấy đúng nội dung cần bổ sung tại cùng mã Ticket; gửi bổ sung thành công → Nhân viên xem được phần bổ sung trong lịch sử của Ticket đó.

---

### [FR-STU-04] Xem kết quả giải quyết & Đánh giá mức độ hài lòng

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem nội dung phản hồi kết quả xử lý cuối cùng từ nhà trường và thực hiện đánh giá chất lượng dịch vụ cho Ticket đã hoàn tất.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên mở yêu cầu đã giải quyết/đã đóng của mình và đọc câu trả lời, tệp kết quả nếu có và thời gian hoàn thành.
2. Nếu chưa đánh giá, sinh viên chọn 1–5 sao, nhập nhận xét nếu muốn rồi gửi; nếu đã đánh giá thì chỉ xem lại đánh giá đã lưu.
3. Gửi thành công thì hiển thị lời cảm ơn và đánh giá ở chế độ chỉ đọc. Khi lỗi mạng, giữ số sao và nhận xét để thử lại theo AC-04.
4. Mở lại trang chi tiết để xem hoặc đánh giá không có nghĩa mở lại quá trình xử lý Ticket.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket của sinh viên đã được Nhân viên/Quản lý xử lý xong và chuyển sang trạng thái `RESOLVED` hoặc `CLOSED`.

#### 3. Quy tắc Dữ liệu & Đánh giá (Business & Validation Rules)
- **Trường thông tin Đánh giá:**
  - **Rating (`rating_score`):** Bắt buộc, số nguyên từ 1 đến 5 (tương ứng từ 1 sao đến 5 sao).
  - **Feedback / Comment (`rating_comment`):** Không bắt buộc, tối đa 500 ký tự. Tự động `trim()`.
- **Ràng buộc số lần đánh giá:** Mỗi Ticket chỉ được đánh giá duy nhất **01 lần**.
- **Khóa biểu mẫu:** Khi Ticket đã có dữ liệu đánh giá, hệ thống chuyển Form đánh giá sang trạng thái Read-Only (Hiển thị số sao và nhận xét đã gửi, không cho thao tác bấm gửi lại).

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên mở chi tiết Ticket đã xử lý xong tại `/student/tickets/{ticket_id}`.
2. Hệ thống hiển thị rõ ràng phần Kết quả giải quyết (Gồm câu trả lời, file đính kèm kết quả từ nhân viên nếu có, thời gian hoàn thành).
3. Kiểm tra trạng thái đánh giá của Ticket:
   - Chưa đánh giá: Hiển thị Component Đánh giá (5 ngôi sao tương tác + Textarea nhập nhận xét + Nút Gửi đánh giá).
   - Đã đánh giá: Hiển thị kết quả đánh giá cũ dạng Read-only.
4. Sinh viên chọn số sao, nhập nhận xét và bấm **Gửi đánh giá**.
5. Client gửi request `POST /api/v1/student/tickets/{ticket_id}/rate`.
6. Server ghi nhận thông tin đánh giá, chuyển trạng thái Ticket từ `RESOLVED` sang `CLOSED` (nếu đang ở `RESOLVED`), lưu timestamp `rated_at`.
7. Client hiển thị Toast thông báo: *"Cảm ơn bạn đã đánh giá dịch vụ!"*, đồng thời chuyển Component đánh giá sang dạng Read-only.

#### 5. Luồng ngoại lệ & Race Condition Handling
- **Lỗi mạng khi gửi đánh giá:** Hiển thị *"Chưa gửi được đánh giá. Vui lòng thử lại."* và giữ nguyên số sao, nhận xét đã nhập theo AC-04.
- **Đánh giá đồng thời nhiều tab (Race Condition):** Nếu sinh viên mở 2 tab cùng 1 Ticket và bấm gửi ở tab A trước:
  - **Tab A:** Gửi thành công.
  - **Tab B:** Khi bấm gửi, Server trả về mã lỗi `409 ALREADY_RATED` với message: *"Ticket này đã được đánh giá trước đó."*
  - **Client tại Tab B nhận lỗi:** Tự động ẩn form nhập và fetch lại dữ liệu đánh giá đã lưu để hiển thị dạng Read-only.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đánh giá 5 sao + nhận xét hợp lệ → Lưu chính xác dữ liệu vào hệ thống, hiển thị đúng trạng thái đã đánh giá.
- **AC-02:** Không chọn số sao mà bấm Gửi → Báo lỗi validation: *"Vui lòng chọn mức độ hài lòng (từ 1 đến 5 sao)"*.
- **AC-03:** Sau khi gửi đánh giá thành công, F5 lại trang hoặc mở lại trang chi tiết Ticket → Form đánh giá ở trạng thái Read-only, không thể chỉnh sửa hay gửi lại.
- **AC-04:** Lỗi mạng khi gửi đánh giá → Thông báo lỗi, giữ nguyên số sao và nhận xét sinh viên đã nhập trên giao diện để sinh viên bấm thử lại.

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
