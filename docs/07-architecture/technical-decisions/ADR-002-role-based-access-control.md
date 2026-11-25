# ADR-002 - Thực Thi Phân Quyền

## Bối Cảnh

UniSupport có ba nhóm người dùng chính: Sinh viên, Nhân viên và Quản lý. Mỗi nhóm có phạm vi chức năng và dữ liệu khác nhau.

## Quyết Định

- Hệ thống phải kiểm tra cả **quyền chức năng** và **phạm vi dữ liệu**.
- Sinh viên bị giới hạn theo Ticket của chính mình.
- Nhân viên bị giới hạn theo phòng ban/quyền và trách nhiệm xử lý.
- Quản lý bị giới hạn theo phạm vi toàn trường hoặc phòng ban cùng quyền được cấp.
- Việc thực thi bằng session/token, middleware hoặc cơ chế tương đương do thiết kế kỹ thuật xác định.

## Hệ Quả

Kiến trúc không được hardcode theo cách làm mất khả năng gán quyền/phạm vi đã được M03 định nghĩa.


## Giới Hạn Triển Khai Quyền

- Dùng 3 nhóm cố định + các cờ quyền trên tài khoản theo [danh mục hữu hạn](../../01-product/actors-and-roles.md#4-danh-mục-quyền-chức-năng-hữu-hạn), phạm vi và điều kiện state/assignee; không thêm role builder, policy engine hay phân hệ phân quyền mới.
- Quyền cơ sở của assignee khác quyền ủy quyền. Mặc định không có cờ bổ sung; backend deny khi thiếu cờ, sai nhóm, ngoài scope hoặc sai state. Chỉ Staff được resolve; Student/hệ thống đóng theo lifecycle.
- Cấp/thu hồi và đổi nhóm/phạm vi kiểm nguyên tử, audit trước/sau; phiên đang mở dùng quyền mới ở yêu cầu kế tiếp. Không tự tăng quyền, không cấp vượt thẩm quyền quản trị/scope người cấp (ACCOUNT_MANAGE ủy quyền cố định các cờ STAFF, cờ MANAGEMENT cần người cấp đang có), không làm mất quản trị toàn trường cuối cùng. Tài khoản bootstrap toàn trường nạp khi triển khai.
- BA/TL xác nhận danh mục/mặc định và effort hiện hữu trước gửi; mọi vượt phạm vi đi qua CR, không tự bổ sung subsystem chưa dự toán.
