# Tổng Quan Sản Phẩm - UniSupport (Product Overview)

## 1. Tóm Tắt Dự Án (Executive Summary)
**UniSupport** là hệ thống Web Application quản lý và hỗ trợ sinh viên tập trung được phát triển dành riêng cho **Aurora University**. Hệ thống ra đời nhằm chuẩn hóa toàn bộ quy trình tiếp nhận, phân loại, điều phối và xử lý các yêu cầu hỗ trợ từ sinh viên, thay thế cho các kênh truyền thống rời rạc (email cá nhân/phòng ban, form trực tuyến, tin nhắn rải rác).

Hệ thống phục vụ quy mô khoảng **3.000 sinh viên** cùng đội ngũ nhân viên vận hành và ban quản lý nhà trường, hướng tới mục tiêu tối ưu hóa thời gian xử lý yêu cầu, nâng cao tính minh bạch và nâng cao mức độ hài lòng của sinh viên.

---

## 2. Bối Cảnh & Tầm Nhìn Dự Án (Context & Vision)

### 2.1 Bối cảnh
Tại Aurora University, công tác hỗ trợ sinh viên (thủ tục hành chính, xác nhận học tập, miễn giảm học phí, tư vấn đào tạo, hỗ trợ kỹ thuật...) đang được thực hiện qua nhiều kênh thủ công. Điều này dẫn đến tình trạng trôi thông tin, xử lý trùng lặp, thiếu công cụ theo dõi tiến độ và gây khó khăn cho Ban giám hiệu trong việc đánh giá hiệu suất vận hành của các phòng ban.

### 2.2 Tầm nhìn sản phẩm
Trở thành **đầu mối giao tiếp số duy nhất** giữa Sinh viên và Các phòng ban chức năng tại Aurora University. Tất cả yêu cầu hỗ trợ đều được định danh bằng mã Ticket duy nhất, luồng xử lý được chuẩn hóa minh bạch, số liệu báo cáo được cập nhật theo thời gian thực.

---

## 3. Các Phân Hệ Chính (Core Product Modules)

| Mã Phân Hệ | Tên Phân Hệ | Chức Năng Cốt Lõi |
| :--- | :--- | :--- |
| **M01** | **Sinh viên (Student Portal)** | Đăng nhập, tạo yêu cầu hỗ trợ (kèm file PDF/ảnh), nhận Mã Ticket, theo dõi tiến độ xử lý, bổ sung hồ sơ, nhận kết quả và đánh giá mức độ hài lòng. |
| **M02** | **Nhân viên (Staff Operations)** | Đăng nhập, tiếp nhận (Claim), phân loại (Triage), đánh giá độ ưu tiên, chuyển phòng ban, yêu cầu sinh viên bổ sung giấy tờ, cập nhật tiến độ và đóng ticket. |
| **M03** | **Quản lý (Management Dashboard)** | Dashboard tổng quan KPI, báo cáo thời gian xử lý trung bình/xu hướng sự cố, tổng hợp chỉ số hài lòng, quản lý tài khoản & phân quyền vai trò. |
| **M04** | **Dịch vụ Thông báo (Notification Service)** | Gửi thông báo nội bộ hệ thống (In-app notification) khi trạng thái ticket thay đổi, có phản hồi mới hoặc yêu cầu bổ sung thông tin. |
| **M05** | **Phân quyền & Bảo mật (RBAC & Security)** | Đăng nhập bằng tài khoản cá nhân, phân quyền 3 vai trò (Sinh viên, Nhân viên, Quản lý), bảo mật file đính kèm, tra soát log thao tác cơ bản (Audit Log). |

---

## 4. Hình Thức Triển Khai & Hạ Tầng
- **Loại hình ứng dụng**: Web Application (Responsive trên Máy tính desktop và Thiết bị di động).
- **Hạ tầng triển khai**: Triển khai trực tiếp trên hạ tầng máy chủ và tên miền do Aurora University cung cấp.
- **Hỗ trợ ngôn ngữ**: Tiếng Việt và Tiếng Anh (mức cơ bản).

---

## 5. Tóm Tắt Thông Số Dự Án (Project Snapshot)
- **Tổng kinh phí**: 300.000.000 VNĐ.
- **Thời gian thực hiện**: 14 tuần (tương đương 70 ngày làm việc).
- **Thời gian nghiệm thu**: 10 ngày làm việc sau bàn giao.
- **Thời gian bảo hành kỹ thuật**: 30 ngày kể từ ngày nghiệm thu chính thức.