# Tài Liệu Đặc Tả Yêu Cầu - Phân Quyền & Bảo Mật Dùng Chung (RBAC & Security)

> Ghi chú: RBAC & Security là năng lực dùng chung trong phạm vi 3 phân hệ chính M01-M03 theo proposal và bảng chi phí nội bộ đã chốt; không tách thành module bàn giao/effort độc lập.

---

### [FR-SEC-01] Xác thực tài khoản & Quản lý phiên làm việc (Authentication & Session Management)

**Mô tả**  
Hệ thống xử lý quá trình đăng nhập, mã hóa thông tin xác thực, khởi tạo Token phiên làm việc an toàn và quản lý đăng xuất đối với tất cả các nhóm người dùng.

**Actor**  
Tất cả người dùng hệ thống (Sinh viên, Nhân viên, Quản lý).

**Preconditions**  
- Người dùng truy cập trang Đăng nhập hệ thống UniSupport.

**Luồng chính**  
1. Người dùng nhập tên đăng nhập (Mã SV/Mã NV/Email) và mật khẩu.
2. Hệ thống mã hóa mật khẩu đầu vào (chuẩn Argon2 hoặc BCrypt) và so sánh với giá trị lưu trong cơ sở dữ liệu.
3. Nếu thông tin chính xác, hệ thống kiểm tra trạng thái tài khoản (`status = ACTIVE`).
4. Hệ thống khởi tạo chuỗi xác thực Token (JWT/Session Token) chứa thông tin: `user_id`, `role`, `department_id`, `exp_time`.
5. Hệ thống trả Token về Client và lưu trữ an toàn (HttpOnly Secure Cookie hoặc Secure Storage).
6. Khi người dùng bấm **Đăng xuất**, hệ thống thu hồi (Revoke/Invalidate) Token hiện tại và xóa phiên làm việc ở Client.

**Business Rules**  
- Mật khẩu lưu trong cơ sở dữ liệu **bắt buộc** phải mã hóa một chiều (Salted Hash), tuyệt đối không lưu dạng plain-text.
- Thời gian hết hạn của Token phiên làm việc tối đa là **24 giờ**.
- Nếu tài khoản chuyển trạng thái `INACTIVE` (bị khóa), toàn bộ các Token đang hoạt động của tài khoản đó phải lập tức bị vô hiệu hóa.

**Alternative / Error Flows**  
- **Mật khẩu không chính xác**: Hệ thống hiển thị thông báo lỗi chung "Tên đăng nhập hoặc mật khẩu không đúng".
- **Tài khoản đang bị khóa (`INACTIVE`)**: Hệ thống hiển thị lỗi "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ Quản lý".
- **Token hết hạn (Expired Token)**: Khi người dùng thao tác, hệ thống trả về mã lỗi HTTP `401 Unauthorized` và điều hướng người dùng về màn hình Đăng nhập.

**Acceptance Criteria**  
- **AC-01**: Đăng nhập với tài khoản hợp lệ -> Khởi tạo Token an toàn, cho phép truy cập các API được phân quyền.
- **AC-02**: Đăng xuất thành công -> Token cũ bị vô hiệu hóa, nhấn nút Back trên trình duyệt không thể xem lại trang nội bộ.
- **AC-03**: Nhập sai mật khẩu -> Dừng đăng nhập, không cấp Token.

**Ví dụ Edge Case**  
Người dùng đổi mật khẩu ở thiết bị A.  
-> **Expected Result**: Phiên làm việc trên thiết bị B tự động bị vô hiệu hóa ở thao tác tiếp theo do Token cũ không còn hợp lệ.

---

### [FR-SEC-02] Phân quyền truy cập theo vai trò (Role-Based Access Control - RBAC)

**Mô tả**  
Hệ thống tự động kiểm tra Vai trò (`Role`) và Phạm vi Phòng ban (`Department Scope`) của người dùng trên từng API Request để cho phép hoặc chặn quyền truy cập tài nguyên.

**Actor**  
Hệ thống (RBAC Middleware).

**Preconditions**  
- Người dùng đã đăng nhập thành công và gửi request đính kèm Token xác thực.

**Luồng chính**  
1. Client gửi request tới API Endpoint (Ví dụ: `GET /api/v1/tickets/{id}`).
2. Middleware kiểm tra và giải mã Token xác thực.
3. Middleware kiểm tra **Vai trò (Role)** của người dùng với yêu cầu của Endpoint:
   - Nếu Endpoint yêu cầu quyền `MANAGER` mà người dùng là `STUDENT` -> Từ chối.
4. Middleware kiểm tra **Phạm vi dữ liệu (Data Scope / Ownership)**:
   - Nếu là `STUDENT`: Ticket `{id}` bắt buộc phải có `created_by_student_id` = ID người dùng.
   - Nếu là `STAFF`: Ticket `{id}` bắt buộc phải có `department_id` = ID Phòng ban của Nhân viên.
5. Nếu tất cả điều kiện hợp lệ, Request được chuyển tiếp cho Business Logic xử lý.
6. Nếu vi phạm, hệ thống chặn lại và trả về mã lỗi HTTP `403 Forbidden`.

**Business Rules**  
- Kiểm tra phân quyền phải diễn ra tại lớp Backend (Server-side Enforcement), không tin tưởng hoàn toàn vào việc ẩn/hiện nút bấm trên giao diện Frontend.
- Nhân viên thuộc Phòng A tuyệt đối không thể xem, chuyển trạng thái hoặc can thiệp Ticket thuộc Phòng B trừ khi Ticket đó được chuyển phòng ban sang Phòng A.

**Alternative / Error Flows**  
- **Truy cập tài nguyên không thuộc quyền quản lý**: Hệ thống trả về lỗi `403 Forbidden` kèm thông báo "Bạn không có quyền thực hiện thao tác này".

**Acceptance Criteria**  
- **AC-01**: Sinh viên A gửi request xem Ticket của Sinh viên B -> Hệ thống trả về lỗi `403 Forbidden`.
- **AC-02**: Nhân viên Phòng Đào tạo thực hiện Claim Ticket của Phòng CTHSSV -> Hệ thống từ chối thao tác và báo lỗi không đúng phòng ban.
- **AC-03**: Quản lý gửi request -> Hệ thống cho phép truy cập theo đúng thẩm quyền quản trị.

**Ví dụ Edge Case**  
Sinh viên cố tình thay đổi tham số ID trên URL từ `/tickets/101` thành `/tickets/102` (mã ticket của người khác).  
-> **Expected Result**: Backend phát hiện người tạo Ticket 102 khác với ID người dùng trong Token, lập tức trả về `403 Forbidden`.

---

### [FR-SEC-03] Bảo mật & Kiểm soát truy cập tệp đính kèm (Secure File Access Control)

**Mô tả**  
Đảm bảo các file đính kèm (PDF, Ảnh minh chứng, Giấy xác nhận) lưu trên hệ thống được bảo vệ an toàn, không thể truy cập qua đường dẫn tĩnh công khai (Public URL).

**Actor**  
Tất cả người dùng có nhu cầu Tải/Xem file đính kèm.

**Preconditions**  
- File đính kèm đã được tải lên và lưu trữ trong thư mục bảo mật của hệ thống.
- Người dùng đã đăng nhập.

**Luồng chính**  
1. Người dùng nhấn vào liên kết Xem/Tải file đính kèm trên giao diện Ticket.
2. Client gửi request tới Secured File API Proxy: `GET /api/v1/attachments/{file_id}/download`.
3. Backend tiếp nhận request và giải mã Token người dùng.
4. Backend truy vấn cơ sở dữ liệu để tìm Ticket chứa `file_id` tương ứng.
5. Backend kiểm tra quyền truy cập của người dùng đối với Ticket đó theo quy tắc `BR-FILE-01`:
   - Người dùng là Sinh viên tạo Ticket.
   - HOẶC Người dùng là Nhân viên/Quản lý thuộc Phòng ban thụ lý Ticket.
   - HOẶC Người dùng là Quản lý (Manager).
6. Nếu hợp lệ, Backend đọc luồng dữ liệu file (Stream) từ thư mục lưu trữ bảo mật và trả về cho Client.
7. Nếu không hợp lệ, Backend chặn truy cập và từ chối tải file.

**Business Rules**  
- Đường dẫn lưu file trên máy chủ (`file_path`) không được hiển thị trực tiếp ra phía Client.
- Nghiêm cấm cấu hình thư mục chứa file ở chế độ Static Public Web Access (Ví dụ: `http://domain.com/uploads/file.pdf` bị cấm hoàn toàn).
- Mọi yêu cầu tải file bắt buộc phải đi qua API Proxy có xác thực Token.

**Alternative / Error Flows**  
- **Thử truy cập trực tiếp URL file tĩnh (nếu có)**: Hệ thống trả về lỗi `404 Not Found` hoặc `403 Forbidden`.
- **Người dùng không liên quan bấm tải file**: Hệ thống chặn và báo lỗi "Bạn không có quyền truy cập tệp đính kèm này".

**Acceptance Criteria**  
- **AC-01**: Sinh viên chủ sở hữu nhấn xem file đính kèm -> File tải/hiển thị thành công.
- **AC-02**: Sinh viên khác copy link download file đính kèm đó và paste sang trình duyệt -> Hệ thống chặn và trả lỗi `403 Forbidden`.
- **AC-03**: Nhân viên thuộc phòng ban phụ trách nhấn tải file -> File tải thành công.

**Ví dụ Edge Case**  
Người dùng chưa đăng nhập paste trực tiếp đường dẫn API download file `https://unisupport.aurora.edu.vn/api/v1/attachments/88/download` vào trình duyệt.  
-> **Expected Result**: Hệ thống từ chối do thiếu Token xác thực, trả lỗi `401 Unauthorized` và không tải bất kỳ dữ liệu file nào.

---

### [FR-SEC-04] Ghi nhận nhật ký tra soát hệ thống cơ bản (Basic Audit Logging)

**Mô tả**  
Hệ thống tự động ghi lại toàn bộ nhật ký lịch sử cho các sự kiện biến động dữ liệu hoặc thay đổi trạng thái quan trọng nhằm phục vụ tra soát độc lập.

**Actor**  
Hệ thống (Audit Log Engine).

**Preconditions**  
- Xảy ra một hành động quan trọng trên hệ thống (Ví dụ: Thay đổi trạng thái Ticket, Chuyển phòng ban, Phân công nhân viên, Tạo/Khóa tài khoản).

**Luồng chính**  
1. Một hành động nghiệp vụ được thực hiện thành công trong hệ thống.
2. Module Audit Log được kích hoạt tự động.
3. Module trích xuất thông tin bối cảnh giao dịch:
   - `user_id`: ID người thực hiện.
   - `action`: Mã hành động (Ví dụ: `TICKET_STATUS_UPDATED`, `DEPARTMENT_TRANSFERRED`).
   - `resource_type`: Loại tài nguyên (`TICKET`, `USER`, `ATTACHMENT`).
   - `resource_id`: ID tài nguyên bị tác động.
   - `old_value` / `new_value`: Dữ liệu trước và sau khi thay đổi (dạng JSON).
   - `ip_address`: Địa chỉ IP của Client.
   - `timestamp`: Thời gian thực hiện (UTC).
4. Module ghi bản ghi log vào cơ sở dữ liệu nhật ký (`audit_logs` table).

**Business Rules**  
- Bảng nhật ký `audit_logs` được thiết lập theo quy tắc `BR-AUD-01`: Chỉ cho phép chèn dữ liệu mới (Append-only).
- Tuyệt đối không cung cấp API hoặc chức năng trên giao diện cho phép SỬA (UPDATE) hoặc XÓA (DELETE) bản ghi nhật ký.
- Thời gian lưu vết bắt buộc theo định dạng chuẩn UTC/ISO-8601.

**Alternative / Error Flows**  
- **Ghi log thất bại**: Nếu quá trình ghi log gặp sự cố, giao dịch chính vẫn đảm bảo tính nhất quán (Rollback nếu quy định bắt buộc) hoặc cảnh báo lỗi hệ thống log.

**Acceptance Criteria**  
- **AC-01**: Nhân viên thực hiện chuyển trạng thái Ticket từ `IN_PROGRESS` sang `RESOLVED` -> Một dòng log được tạo tự động lưu rõ ID nhân viên, giá trị cũ `IN_PROGRESS`, giá trị mới `RESOLVED` và thời điểm thực hiện.
- **AC-02**: Nhật ký chỉ ở dạng truy vấn xem (Read-only), không có bất kỳ lệnh sửa/xóa nào trên hệ thống.

**Ví dụ Edge Case**  
Tài khoản Quản lý thử gửi lệnh xóa dữ liệu bảng `audit_logs` qua giao diện.  
-> **Expected Result**: Hệ thống không cung cấp chức năng xóa, mọi truy cập trực tiếp bị chặn ở mức phân quyền database.
