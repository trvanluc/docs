# [NFR-SEC] Yêu cầu về Bảo mật (Security Requirements)

### 1. Tổng quan
Tài liệu quy định các nguyên tắc bảo mật thông tin, phân quyền truy cập và an toàn dữ liệu áp dụng cho hệ thống UniSupport. Theo giả định dự án, hệ thống tuân thủ các quy chuẩn bảo mật cơ bản, không bao gồm kiểm thử bảo mật chuyên sâu hay chứng nhận bảo mật quốc tế.

### 2. Xác thực và Phân quyền (Authentication & Authorization)
- **Đăng nhập:** Người dùng đăng nhập bằng tài khoản và mật khẩu riêng. Mật khẩu phải được mã hóa dạng hash (ví dụ: Bcrypt/Argon2) trước khi lưu vào CSDL.
- **Mô hình RBAC (Role-Based Access Control):**
  - **Sinh viên (Student):** Chỉ được xem, tạo và tương tác với các Ticket do chính tài khoản đó tạo ra.
  - **Nhân viên (Staff):** Xem và xử lý các Ticket thuộc phòng ban được gán thẩm quyền.
  - **Quản lý (Manager):** Xem báo cáo tổng quan, quản lý tài khoản và phân quyền hệ thống.
- **Bảo mật tệp đính kèm:** Đường dẫn tệp đính kèm (PDF/Ảnh) phải được bảo vệ. Hệ thống xác thực quyền truy cập trước khi cho phép tải xuống/xem tệp; không công khai đường dẫn trực tiếp (Direct URL).

### 3. Tra soát và Nhật ký hoạt động (Audit Logging)
- Hệ thống tự động ghi lại lịch sử đối với các thao tác quan trọng:
  - Đăng nhập / Đăng xuất / Thay đổi mật khẩu.
  - Thay đổi trạng thái Ticket, chuyển tiếp phòng ban.
  - Cập nhật kết quả giải quyết và tạo/sửa tài khoản.
- Nhật ký tra soát (Audit Log) bao gồm các thông tin: `User_ID`, `Action`, `Timestamp`, `IP_Address`, `Target_ID`.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-SEC-01:** Sinh viên A nhập đường dẫn URL tệp đính kèm của Sinh viên B -> Hệ thống chặn truy cập và trả về lỗi `403 Forbidden`.
- **NFR-SEC-02:** Tất cả mật khẩu trong cơ sở dữ liệu phải được lưu dưới dạng chuỗi mã hóa hash, không hiển thị plain-text.
- **NFR-SEC-03:** Mọi thao tác đổi trạng thái Ticket đều sinh bản ghi trong bảng Audit Log.