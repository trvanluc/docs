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

## 3. Các Phân Hệ Chính Theo Proposal Đã Chốt

Theo proposal và bảng chi phí nội bộ đã chốt, phạm vi bàn giao chính của UniSupport gồm **3 phân hệ sản phẩm**. Các yêu cầu về thông báo, bảo mật, phân quyền và audit log là năng lực hỗ trợ/xuyên suốt được triển khai trong 3 phân hệ này, không tách thành module bàn giao độc lập trong bảng chi phí.

| Mã Phân Hệ | Tên Phân Hệ | Chức Năng Cốt Lõi | Effort kế hoạch |
| :--- | :--- | :--- | :---: |
| **M01** | **Sinh viên (Student Portal)** | Đăng nhập, gửi yêu cầu hỗ trợ, đính kèm file ảnh/PDF, nhận mã Ticket, theo dõi tiến độ, bổ sung hồ sơ, nhận thông báo trạng thái, xem kết quả và đánh giá mức độ hài lòng. | **128h** |
| **M02** | **Nhân viên (Staff Operations)** | Đăng nhập, xem danh sách yêu cầu mới/được giao, tìm kiếm/lọc Ticket, tiếp nhận, phân loại, phân công, quản lý ưu tiên/SLA, yêu cầu bổ sung hồ sơ, chuyển xử lý, cập nhật tiến độ, hoàn tất/đóng/mở lại yêu cầu. | **197h** |
| **M03** | **Quản lý / Admin (Management Dashboard)** | Dashboard tổng quan, báo cáo xu hướng và CSAT, quản lý tài khoản, vai trò, RBAC, phòng ban/danh mục, audit trail, thời hạn lưu trữ và xuất dữ liệu. | **215h** |

### Năng lực xuyên suốt
- **Thông báo nội bộ hệ thống**: In-app notification khi Ticket được tạo, chuyển trạng thái, chuyển phòng ban, yêu cầu bổ sung, hoàn tất hoặc có cảnh báo SLA.
- **Bảo mật & phân quyền**: Đăng nhập bằng tài khoản riêng, phân quyền theo vai trò, giới hạn dữ liệu theo phạm vi người dùng/phòng ban, bảo vệ file đính kèm và ghi nhận thao tác quan trọng để tra soát.

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
