# ARC-03 - Nguyên Tắc Thiết Kế API

## 1. Mục Đích

Tài liệu này quy định cách Frontend và Backend giao tiếp ở mức nguyên tắc. Tên endpoint, framework và cơ chế token cụ thể là quyết định triển khai.

## 2. Nguyên Tắc Chung

- API phải phản ánh đúng quyền và Business Rules trong PRD/Domain.
- Không tin cậy dữ liệu quyền/phạm vi chỉ từ giao diện; Backend phải kiểm tra lại.
- Một thao tác nghiệp vụ phải trả kết quả rõ thành công/thất bại và không tạo dữ liệu dở dang.
- Các thao tác thay đổi Ticket phải sử dụng trạng thái hiện tại để kiểm tra tính hợp lệ.
- Dữ liệu trả về phải giới hạn theo actor và phạm vi quyền.

## 3. Nhóm Chức Năng

API có thể được tổ chức theo:
- xác thực/tài khoản;
- Student Ticket/FAQ/notification;
- Staff queue/assignment/processing/Transfer/Escalation;
- Management account/configuration/dashboard/report/audit;
- attachment.

Cấu trúc route cụ thể được xác định trong giai đoạn triển khai và không làm thay đổi hành vi nghiệp vụ.

## 4. Lỗi Và Validation

- Dữ liệu không hợp lệ phải trả thông tin đủ để giao diện hiển thị lỗi phù hợp.
- Không tiết lộ dữ liệu của người dùng khác trong nội dung lỗi.
- Xung đột do Ticket đã thay đổi phải yêu cầu người dùng tải trạng thái mới nhất trước khi thao tác lại.
