# Tổng quan sản phẩm - UniSupport

## 1. Tóm tắt

**UniSupport** là Web Application hỗ trợ Aurora University quản lý tập trung quy trình tiếp nhận, xử lý, theo dõi và đánh giá các yêu cầu hỗ trợ sinh viên. Hệ thống phục vụ quy mô khoảng **3.000 sinh viên**, cùng đội ngũ nhân viên phòng ban và nhóm quản lý nhà trường.

Tài liệu PRD/specification này dùng proposal đã nộp làm baseline scope. Các chi tiết cần thiết để triển khai baseline được đánh dấu **Derived**. Các hạng mục chỉ xuất hiện trong bảng effort nội bộ hoặc cần xác nhận thêm được đánh dấu **Proposed** hoặc **TBD**.

## 2. Bối cảnh

Trước UniSupport, sinh viên gửi yêu cầu qua nhiều kênh như email, điện thoại, biểu mẫu trực tuyến, tin nhắn mạng xã hội hoặc trao đổi trực tiếp. Cách vận hành này làm phát sinh các vấn đề:

- Sinh viên khó biết cần liên hệ phòng ban nào.
- Sinh viên khó theo dõi yêu cầu đã được tiếp nhận, ai đang xử lý và tiến độ hiện tại.
- Nhân viên phải xử lý yêu cầu từ nhiều kênh, dễ bỏ sót hoặc xử lý trùng.
- Quản lý thiếu dữ liệu đáng tin cậy để theo dõi workload, thời gian xử lý và chất lượng dịch vụ.

## 3. Mục tiêu sản phẩm

| ID | Mục tiêu | Trạng thái |
| :--- | :--- | :--- |
| **G-01** | Tập trung hóa các yêu cầu hỗ trợ trực tuyến của sinh viên vào một hệ thống chung. | Baseline |
| **G-02** | Giúp sinh viên theo dõi trạng thái, lịch sử cập nhật và kết quả xử lý của yêu cầu. | Baseline |
| **G-03** | Hỗ trợ nhân viên tiếp nhận, phân loại, điều phối và cập nhật tiến độ xử lý rõ ràng hơn. | Baseline |
| **G-04** | Cung cấp dashboard/báo cáo để quản lý theo dõi khối lượng công việc, xu hướng vấn đề và phản hồi sinh viên. | Baseline |
| **G-05** | Bảo vệ dữ liệu theo vai trò, giới hạn quyền xem file đính kèm và lưu vết các thao tác quan trọng để tra soát. | Baseline |

## 4. Phân hệ sản phẩm

Proposal đã chốt **3 business module chính**. Notification, RBAC, bảo mật file và audit log là năng lực dùng chung trong hệ thống, không phải business module độc lập.

| Mã | Phân hệ | Scope chính | Trạng thái |
| :--- | :--- | :--- | :--- |
| **M01** | Student Portal | Login, tạo Ticket, chọn nhóm vấn đề, mô tả yêu cầu, đính kèm ảnh/PDF, nhận mã Ticket, theo dõi tiến độ/lịch sử, bổ sung thông tin, xem kết quả/thông báo và đánh giá hài lòng. | Baseline |
| **M02** | Staff Operations | Login, xem Ticket mới/được giao, phân loại, xem xét ưu tiên, chuyển phòng ban/người phụ trách, cập nhật trạng thái, yêu cầu bổ sung, ghi nhận kết quả và đóng Ticket. | Baseline |
| **M03** | Management Dashboard | Login, dashboard tổng quan, theo dõi Ticket mới/đang xử lý/sắp quá hạn/quá hạn, workload theo phòng ban/nhân viên, báo cáo xu hướng, thời gian xử lý trung bình, feedback, tạo/chỉnh sửa account và gán quyền. | Baseline |
| **Shared** | Notification | Thông báo trong hệ thống khi có thay đổi quan trọng liên quan đến Ticket. | Derived |
| **Shared** | RBAC, Attachment Security, Audit | Kiểm soát truy cập theo vai trò/phạm vi dữ liệu, bảo vệ file đính kèm và lưu lịch sử thao tác quan trọng. | Baseline/Derived |

## 5. Baseline dự án

- **Loại ứng dụng**: Web Application, responsive trên desktop/mobile browser.
- **Quy mô phục vụ**: khoảng 3.000 sinh viên.
- **Ngôn ngữ giao diện**: Tiếng Việt và Tiếng Anh ở mức cơ bản.
- **Thời gian triển khai**: 14 tuần.
- **Nghiệm thu chính thức**: 10 ngày làm việc sau bàn giao.
- **Bảo hành kỹ thuật**: 30 ngày sau nghiệm thu.
- **Ngân sách proposal**: 300.000.000 VNĐ.

## 6. Ghi chú về effort nội bộ

Bảng chi phí/effort nội bộ dùng để kiểm tra năng lực và kế hoạch thực hiện của team:

| Module effort | Effort kế hoạch |
| :--- | :---: |
| M1 - Student | 128h |
| M2 - Staff | 197h |
| M3 - Admin/Management | 215h |
| Hoạt động cấp dự án | 100h |
| **Tổng toàn dự án** | **640h** |

Các dòng effort như FAQ, export, retention hoặc cấu hình nâng cao không tự động trở thành baseline client scope nếu proposal chưa chốt. Những nội dung này được phân loại Proposed/TBD ở các tài liệu chi tiết.
