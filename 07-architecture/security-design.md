# ARC-05 - Thiết Kế Bảo Mật

## 1. Mục Tiêu

Thực thi các yêu cầu tại NFR Security, Product Roles và Business Rules mà không mở rộng phạm vi thành hệ thống bảo mật chuyên sâu.

## 2. Xác Thực

- Người dùng xác thực bằng tài khoản/mật khẩu.
- Backend duy trì phiên đăng nhập bằng cơ chế kỹ thuật phù hợp.
- Tài khoản bị khóa/vô hiệu hóa không được tạo hoặc tiếp tục phiên hợp lệ.
- Mật khẩu phải được lưu bằng cơ chế một chiều phù hợp; thuật toán cụ thể do đội kỹ thuật lựa chọn.

## 3. Phân Quyền

Kiểm tra quyền phải gồm:
- **Vai trò/chức năng:** người dùng có được phép thực hiện hành động hay không.
- **Phạm vi dữ liệu:** Ticket/tài khoản/phòng ban có nằm trong phạm vi được phép hay không.
- **Điều kiện nghiệp vụ:** state, assignee, Category, thời hạn hoặc điều kiện liên quan có hợp lệ hay không.

Ba nhóm người dùng chính là `STUDENT`, `STAFF`, `MANAGEMENT`.

## 4. File Đính Kèm

- File không được cung cấp cho người không có quyền.
- Mọi yêu cầu xem/tải file phải kiểm tra quyền đối với Ticket liên quan.
- Cách lưu file vật lý có thể thay đổi nhưng không được làm mất kiểm soát quyền.

## 5. Audit

Các thao tác quan trọng phải sinh Audit theo M03/`BR-AUD`. Audit không sửa/xóa bằng chức năng thông thường của ứng dụng.

## 6. Giới Hạn

Phạm vi bảo mật không bao gồm penetration testing chuyên sâu hoặc chứng nhận bảo mật quốc tế.
