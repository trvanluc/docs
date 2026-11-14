# NFR-USA - Tính Dễ Sử Dụng

## Mã yêu cầu

Nơi gốc của mã và ngưỡng. Kịch bản test (`06-acceptance/test-scenarios.md`) và các tài liệu khác chỉ dẫn mã.

| Mã | Yêu cầu | Ngưỡng / cách đo | Loại |
| --- | --- | --- | --- |
| `NFR-USA-01` | Giao diện responsive | Luồng chính dùng được ở màn hình rộng 360 px (điện thoại) và 1366 px (máy tính) trên Chrome và Edge bản mới: không mất nội dung, không phải cuộn ngang. | Cam kết với khách |
| `NFR-USA-02` | Tiếng Việt và Tiếng Anh ở mức cơ bản | 100% nhãn, menu và thông báo của luồng chính có bản Việt và Anh; đổi ngôn ngữ không làm mất dữ liệu đang nhập. | Cam kết với khách |
| `NFR-USA-03` | Thông báo lỗi validation chỉ rõ thông tin cần sửa | 100% lỗi validation trong kịch bản test hiển thị ngay tại trường sai và nêu lý do. | Cam kết với khách |
| `NFR-USA-04` | Thông tin chính hiển thị trực tiếp, không cần hiểu mã kỹ thuật | Sinh viên thấy mã Ticket, trạng thái, phòng ban/người phụ trách (khi được phép) và kết quả ngay ở chi tiết Ticket; Nhân viên thấy người phụ trách, Priority, Deadline ngay trên hàng chờ; trạng thái hiển thị bằng chữ thường (ví dụ "Đang xử lý"), không hiển thị mã như `IN_PROGRESS`. | Cam kết với khách |

## 1. Phạm Vi

Giao diện UniSupport là Web Application và phải sử dụng được trên trình duyệt máy tính và thiết bị di động.

## 2. Yêu Cầu

- Giao diện responsive cho màn hình máy tính và thiết bị di động.
- Hỗ trợ **Tiếng Việt và Tiếng Anh ở mức cơ bản**.
- Trạng thái Ticket và hành động chính phải được trình bày rõ ràng, không yêu cầu người dùng hiểu mã kỹ thuật để thao tác.
- Biểu mẫu phải chỉ rõ trường bắt buộc và lý do khi dữ liệu không hợp lệ.
- Thông tin chính của Sinh viên và Nhân viên hiển thị trực tiếp theo `NFR-USA-04`.
- Quản lý phải xem được các chỉ số/báo cáo đúng phạm vi quyền.

## 3. Nghiệm Thu

- Các luồng chính không bị mất nội dung hoặc không thể thao tác khi sử dụng trên trình duyệt máy tính và thiết bị di động.
- Các nhãn/chức năng chính có phiên bản Việt/Anh ở mức phù hợp phạm vi dự án.
- Thông báo lỗi validation chỉ rõ thông tin cần sửa.
