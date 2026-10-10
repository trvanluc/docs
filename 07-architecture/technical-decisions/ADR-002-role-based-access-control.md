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
