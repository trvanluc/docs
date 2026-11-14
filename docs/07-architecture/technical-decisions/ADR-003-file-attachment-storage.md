# ADR-003 - Bảo Vệ File Đính Kèm

## Bối Cảnh

File đính kèm có thể chứa tài liệu của sinh viên và chỉ được cung cấp cho người dùng có quyền đối với Ticket liên quan.

## Quyết Định

- Mỗi file phải liên kết với Ticket và ngữ cảnh nghiệp vụ tương ứng.
- Trước khi cho phép xem/tải file, Backend phải xác định người dùng có quyền đối với Ticket/file.
- Cách lưu file vật lý có thể là local storage hoặc phương án phù hợp hạ tầng Aurora University; lựa chọn này không thay đổi quy tắc quyền.
- Không yêu cầu tích hợp dịch vụ lưu trữ bên thứ ba trong phạm vi hiện tại.

## Hệ Quả

Có thể thay đổi cơ chế lưu trữ khi triển khai mà không phải sửa PRD, miễn quyền truy cập và giới hạn file vẫn đúng.
