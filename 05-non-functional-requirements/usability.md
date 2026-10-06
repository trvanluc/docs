# [NFR-USA] Yêu cầu về Tính dễ sử dụng (Usability Requirements)

### 1. Tổng quan
Tài liệu quy định các tiêu chuẩn về thiết kế giao diện (UI) và trải nghiệm người dùng (UX) đối với hệ thống Web Application UniSupport, đảm bảo sự thân thiện và thuận tiện cho cả 3 nhóm vai trò.

### 2. Tiêu chuẩn Giao diện & Trải nghiệm

| Tiêu chí | Mô tả chi tiết |
| :--- | :--- |
| **Thiết kế Responsive** | Tối ưu hiển thị linh hoạt trên cả trình duyệt máy tính (Desktop) và thiết bị di động (Mobile Web / Tablet). |
| **Đa ngôn ngữ (Multilingual)** | Hỗ trợ 2 ngôn ngữ giao diện ở mức cơ bản: **Tiếng Việt** và **Tiếng Anh**. Người dùng có thể chuyển đổi ngôn ngữ nhanh trên thanh điều hướng. |
| **Tính nhất quán (Consistency)** | Thống nhất về màu sắc nhận diện, font chữ, kích thước nút bấm và quy chuẩn bảng biểu trên toàn bộ các trang. |
| **Trạng thái thao tác** | Luôn hiển thị phản hồi tức thì cho người dùng khi thực hiện tác vụ (VD: hiệu ứng Loading khi gửi biểu mẫu, Toast notification khi thành công/thất bại). |

### 3. Quy chuẩn Đồ họa & Điều hướng
- **Đơn giản hóa form nhập:** Form tạo Ticket cho sinh viên không quá 5 trường thông tin bắt buộc nhằm tối ưu thời gian thao tác.
- **Phân loại rõ ràng:** Sử dụng màu sắc mã hóa cho các trạng thái Ticket (VD: `Mới` - Xanh dương, `Đang xử lý` - Cam, `Hoàn thành` - Xanh lá, `Quá hạn` - Đỏ).

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-USA-01:** Giao diện phân hệ Sinh viên hiển thị đầy đủ, không bị đè chữ hay tràn khung hình khi truy cập trên trình duyệt điện thoại di động (Mobile Web).
- **NFR-USA-02:** Khi chuyển đổi ngôn ngữ giao diện sang Tiếng Anh, toàn bộ các nhãn nút bấm, tiêu đề trang và thông báo chính chuyển sang Tiếng Anh tương ứng.
- **NFR-USA-03:** Sinh viên hoàn thành việc gửi một Ticket hỗ trợ trong vòng dưới 3 phút mà không cần hướng dẫn trực tiếp.