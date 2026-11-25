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


## 7. Kiểm Soát Cấp/Thu Hồi Và Bằng Chứng Sớm

Áp dụng [danh mục/mặc định/nhóm đủ điều kiện](../01-product/actors-and-roles.md#4-danh-mục-quyền-chức-năng-hữu-hạn): chỉ MANAGEMENT có ACCOUNT_MANAGE được cấp/thu hồi cờ hữu hạn trong thẩm quyền quản trị/scope chính mình: ACCOUNT_MANAGE ủy quyền cố định cấp cờ STAFF nhưng không dùng chúng; cờ MANAGEMENT chỉ cấp nếu người cấp đang có. Cấm tự tăng quyền, sai nhóm/mã lạ và làm mất quản trị toàn trường cuối cùng. Thu hồi có hiệu lực ở yêu cầu được bảo vệ tiếp theo, không chờ đăng nhập lại. Không có quyền đóng/mở lại vượt lifecycle; chỉ STAFF ghi kết quả/RESOLVED.

MS-01 kiểm nền tảng audit bằng TS-AUTH-05: DevOps/TL cung cấp truy vấn hoặc trích xuất chỉ đọc có phân quyền từ môi trường kiểm thử; QA đối chiếu sự kiện thật của các chức năng đã có, actor/thời điểm/giá trị trước–sau. Che mật khẩu, token và dữ liệu nhạy cảm; không cung cấp quyền sửa/xóa hoặc DB access đại trà. Không dùng màn hình tra soát chưa giao làm bằng chứng. UI tra soát vẫn MS-05 (TS-MGT-03/09); mỗi sự kiện mới được kiểm audit tại mốc triển khai rồi regression.
