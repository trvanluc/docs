# NFR-REL - Độ Ổn Định Và Tin Cậy

## 1. Mục Tiêu

Đảm bảo các thao tác nghiệp vụ quan trọng không tạo dữ liệu dở dang hoặc làm sai vòng đời Ticket.

## 2. Yêu Cầu

- Tạo Ticket thành công phải tạo đầy đủ Ticket, mã Ticket, Category, phòng ban và trạng thái ban đầu.
- Các thao tác thay đổi đồng thời nhiều dữ liệu nghiệp vụ, ví dụ Transfer cập nhật Category + phòng ban, phải hoàn tất nhất quán hoặc không ghi nhận thay đổi.
- Lỗi khi lưu dữ liệu không được để Ticket ở trạng thái không hợp lệ so với Domain.
- Lịch sử xử lý đã ghi nhận không bị mất khi Transfer, reopen hoặc cập nhật kết quả.
- Hệ thống phải hiển thị thông báo lỗi dễ hiểu cho người dùng, không để lỗi kỹ thuật thay thế kết quả nghiệp vụ.
- Khả năng vận hành thực tế phụ thuộc hạ tầng máy chủ, mạng và tên miền do Aurora University cung cấp.

## 3. Nghiệm Thu

- Các trường hợp lỗi trong luồng tạo, phân công, Transfer, bổ sung và ghi kết quả không tạo trạng thái dữ liệu trái Business Rules.
- Sau lỗi, người dùng có thể tải lại và thấy trạng thái nghiệp vụ cuối cùng đã được ghi nhận thành công.
