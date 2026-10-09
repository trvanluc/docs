# Tổng Quan Sản Phẩm - UniSupport (Product Overview)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`

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

## 3. Các Phân Hệ & Phân Bổ Công Sức (Modules & Effort Allocation)

Hệ thống có 3 cổng nghiệp vụ với 14 FR chi tiết. Resources phân bổ 17 dòng công việc theo Student/Staff/Admin và PM/DevOps; số dòng công sức không phải số FR.

| Nhóm | Phạm vi PRD hiện có | Cơ sở | Dự phòng | Kế hoạch |
| --- | --- | --- | --- | --- |
| M01 Student | Đăng nhập, gửi yêu cầu, theo dõi/bổ sung, xem kết quả/CSAT | 124 | 4 | 128 |
| M02 Staff | Đăng nhập, tiếp nhận/phân loại, chuyển phòng, yêu cầu bổ sung, hoàn tất | 187 | 10 | 197 |
| M03 Management | Đăng nhập/quyền, dashboard/SLA, báo cáo/xuất, tài khoản, tra soát | 207 | 8 | 215 |
| PM/DevOps | Giữ đúng hoạt động cấp dự án nguồn | 100 | 0 | 100 |
| Tổng | Mỗi dòng nguồn tính một lần | 618 | 22 | 640 |

Xem [đối chiếu Resources](../Phan_bo_Resources_Antigravity.md) và [phạm vi sản phẩm](./product-scope.md). M04/M05 là tài liệu kỹ thuật dùng chung, được giữ nguyên; không bổ sung effort hoặc mở rộng chức năng từ mô tả kỹ thuật đó.

---

## 4. Hình Thức Triển Khai & Hạ Tầng
- **Loại hình ứng dụng**: Web Application (Responsive trên Máy tính desktop và Thiết bị di động).
- **Hạ tầng triển khai**: Triển khai trực tiếp trên hạ tầng máy chủ và tên miền do Aurora University cung cấp.
- **Hỗ trợ ngôn ngữ**: Tiếng Việt và Tiếng Anh (mức cơ bản).

---

## 5. Tóm Tắt Thông Số Dự Án (Project Snapshot)
- **Tổng kinh phí hợp đồng**: 300.000.000 VNĐ.
- **Chi phí nhân sự nội bộ cơ sở (618h)**: 186.557.727 VNĐ (Lương gross: 153.545.455 đ + BH 21.5%: 33.012.273 đ).
- **Chi phí dự phòng rủi ro ước tính (22h)**: 6.641.214 VNĐ.
- **Tổng chi phí nhân sự kế hoạch (640h)**: 193.198.941 VNĐ.
- **Quy mô đội ngũ**: 10 vị trí chuyên môn (PM, BA, UI/UX, TL, FE1, FE2, BE1, BE2, QA, DevOps).
- **Thời gian thực hiện**: 14 tuần phát triển (tương đương 70 ngày làm việc).
- **Thời gian nghiệm thu**: 10 ngày làm việc UAT sau bàn giao.
- **Thời gian bảo hành kỹ thuật**: 30 ngày kể từ ngày nghiệm thu chính thức.
