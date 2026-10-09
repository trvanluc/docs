# 1. Tổng Quan Kiến Trúc Bảo Mật (Security Architecture)
Hệ thống UniSupport áp dụng mô hình bảo mật đa lớp (Defense in Depth), bao gồm các trụ cột chính: Xác thực tập trung dựa trên Token (JWT Stateless Authentication), Phân quyền theo ngữ cảnh & phạm vi dữ liệu (RBAC & Data Isolation Middleware), Bảo mật tài nguyên lưu trữ File (Private Storage Streaming), Chống tấn công lỗ hổng OWASP Top 10 và Nhật ký tra soát vĩnh viễn (Append-Only Audit Trail).

---

# 2. Xác Thực & Quản Lý Phiên (Authentication & Session Management)

## 2.1. Cấu Trúc Mã Xác Thực JWT (JSON Web Token Specification)
Mọi request thành công từ phía Client đều phải gửi kèm Header: `Authorization: Bearer <JWT_Access_Token>`.
- **Thuật toán mã hóa:** HMAC-SHA256 (HS256) hoặc RSA-256 (RS256).
- **Thời hạn hiệu lực:**
  - **Access Token:** Hết hạn sau 15 phút (`exp = 900s`).
  - **Refresh Token:** Hết hạn sau 7 ngày (`exp = 604800s`), lưu trữ trong HTTP-Only, Secure, `SameSite=Strict` Cookie để chống tấn công XSS/CSRF.
- **Payload Chuẩn của JWT Access Token:**
```json
{
  "sub": "usr_stu_20260001",
  "iss": "unisupport-auth-service",
  "iat": 1791523200,
  "exp": 1791524100,
  "user_code": "SV20260001",
  "full_name": "Nguyễn Văn A",
  "email": "a.nguyen@aurora.edu.vn",
  "role": "STUDENT",
  "department_id": null
}
```
---
## 2.2. Cơ Chế Vô Hiệu Hóa Token Tức Thì (Token Revocation / Blacklisting)
Khi Admin thực hiện khóa tài khoản (`status = INACTIVE`) hoặc người dùng bấm Đăng xuất, Backend bắt buộc phải lưu `jti` (Token ID) hoặc `user_id` vào Redis Blacklist kèm theo thời gian hết hạn TTL (bằng thời gian còn lại của Access Token).

Mọi API Private khi verify JWT phải kiểm tra sự tồn tại của Token/User trong Redis Blacklist. Nếu có $\rightarrow$ Trả về lỗi `401 UNAUTHORIZED`.

# 3. Lớp Middleware Phân Quyền & Isolate Dữ Liệu (RBAC & Data Isolation Middleware)
Hệ thống cài đặt 3 Lớp Middleware bảo mật kiểm soát theo thứ tự:

```plaintext
[Incoming Request] ──> [1. AuthMiddleware] ──> [2. RoleGuardMiddleware] ──> [3. DataScopeMiddleware] ──> [Controller]
```
---
1. **AuthMiddleware (Xác thực Identity):** Decrypt Bearer Token, kiểm tra chữ ký và Hạn sử dụng (`exp`). Trích xuất `user_id`, `role`, `department_id` gắn vào Context Request.
2. **RoleGuardMiddleware (Xác thực Quyền vai trò):**
   - Chặn các request vi phạm vai trò (Ví dụ: `STUDENT` cố gọi Endpoint `/api/v1/staff/*` $\rightarrow$ Trả về `403 FORBIDDEN_ACCESS`).
3. **DataScopeMiddleware (Isolate Phạm vi Dữ liệu):**
   - **Đối với STUDENT:** Tự động chèn điều kiện Query CSDL: `WHERE student_id = current_user.id`. Nếu `student_id` trên Ticket khác `current_user.id` $\rightarrow$ Trả về `403 FORBIDDEN_ACCESS` (Chống lừa đảo đổi ID URL).
   - **Đối với STAFF:** Tự động chèn điều kiện Query CSDL: `WHERE department_id = current_user.department_id`. Nhân viên chỉ thao tác được trên Ticket thuộc phòng ban mình.
   - **Đối với MANAGER / ADMIN:** Cho phép bypass điều kiện kiểm tra `department_id` theo phạm vi ủy quyền.

## 4. An Toàn File, Sanitize Input & Chống OWASP Top 10

### 4.1. Sanitize Input & Chống Injection (SQLi / XSS)
- **Chống SQL Injection:** 100% các câu lệnh truy vấn CSDL bắt buộc sử dụng Parameterized Queries hoặc qua ORM / Query Builder. Tuyệt đối không cộng chuỗi SQL.
- **Chống Cross-Site Scripting (XSS):** Mọi trường dữ liệu dạng Text đầu vào (`title`, `description`, `resolution_note`) phải qua thư viện Sanitize (loại bỏ toàn bộ các thẻ `<script>`, `<iframe>`, `javascript:` protocol) trước khi lưu CSDL.
- **Cấu hình Security Headers (Helmet Middleware):** Trả về đầy đủ các Header an toàn:
  - `Content-Security-Policy` (CSP)
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY` (Chống Clickjacking)
  - `Strict-Transport-Security` (HSTS)

### 4.2. Bảo Mật File Đính Kèm (Thực Thi Theo ADR-003)
- File lưu ngoài Web Root tại đĩa cứng private server (`/var/app/data/attachments/`).
- API phục vụ xem file (`GET /api/v1/attachments/{file_id}`) bắt buộc đi qua `AuthMiddleware` và `DataScopeMiddleware`.
- **Kiểm tra Binary Magic Bytes:** Backend đọc header nhị phân để xác minh file đúng là PDF/PNG/JPG trước khi lưu, chặn đứng file giả mạo extension.
- **Randomize File Name:** Tên file lưu trên đĩa cứng tự động đổi sang UUID v4 để loại bỏ lỗ hổng Path Traversal (`../../`).

## 5. Bảng Mã Lỗi Bảo Mật Chuẩn (Security Error Codes)

| HTTP Status | Error Code | Message Hiển Thị Cho Người Dùng | Kịch Bản Áp Dụng |
| :--- | :--- | :--- | :--- |
| **401** | `UNAUTHORIZED` | "Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại." | Token không hợp lệ, hết hạn hoặc thiếu Bearer Token. |
| **401** | `ACCOUNT_DISABLED` | "Tài khoản của bạn đã bị vô hiệu hóa. Vui lòng liên hệ Admin." | Admin khóa tài khoản, Token bị đẩy vào Blacklist. |
| **403** | `FORBIDDEN_ACCESS` | "Bạn không có quyền truy cập vào tài nguyên này." | Khác vai trò hoặc xem Ticket của người khác. |
| **403** | `FORBIDDEN_DEPARTMENT` | "Bạn không có quyền thao tác trên Ticket thuộc phòng ban khác." | Staff cố truy cập Ticket phòng ban khác. |
| **429** | `TOO_MANY_REQUESTS` | "Bạn đã thao tác quá nhiều lần. Vui lòng thử lại sau 1 phút." | Vi phạm Rate Limit (Spam request / brute-force). |