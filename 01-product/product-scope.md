# Phạm Vi Sản Phẩm & Phân Bổ Nguồn Lực (Product Scope & Resource Allocation)

> Nguồn chuẩn hóa nhân sự & phạm vi: `Phan_bo_Resources_Antigravity.md`

## 1. Phạm Vi Chức Năng Sản Phẩm (Functional Scope)

Dự án UniSupport đóng gói trọn gói các chức năng trong **3 Phân hệ nghiệp vụ chính (17 Chức năng)** và **Hoạt động cấp dự án**:

### 1.1 Phân hệ Sinh viên (M1 – Student Portal: 128h kế hoạch)
- **FR-STU-01: Tra cứu hướng dẫn & FAQ (14h)**: Tra cứu nhanh câu hỏi thường gặp, quy trình thủ tục theo từng phòng ban.
- **FR-STU-02: Tạo & gửi yêu cầu hỗ trợ (37h)**: Chọn phòng ban/danh mục, nhập tiêu đề/mô tả, đính kèm file minh chứng (PDF/Ảnh tối đa 10MB), sinh Mã Ticket duy nhất.
- **FR-STU-03: Xem & theo dõi yêu cầu (33h)**: Danh sách Ticket cá nhân, bộ lọc trạng thái, timeline xử lý thời gian thực.
- **FR-STU-04: Nhận thông báo trạng thái (19h)**: Trung tâm thông báo quả chuông, cập nhật tức thì khi Ticket đổi trạng thái hoặc có phản hồi.
- **FR-STU-05: Bổ sung thông tin & phản hồi (25h)**: Tải giấy tờ bổ sung khi `WAITING_STUDENT`, xem kết quả chính thức và đánh giá CSAT (1-5 sao).

### 1.2 Phân hệ Nhân viên (M2 – Staff Operations: 197h kế hoạch)
- **FR-STF-01: Tiếp nhận, tìm kiếm & lọc yêu cầu (33h)**: Hòm thư công việc phân loại theo tab, tìm kiếm mã Ticket, lọc theo phòng ban/ưu tiên/trạng thái.
- **FR-STF-02: Phân loại & phân công xử lý (38h)**: Tự tiếp nhận (`Claim`) hoặc Trưởng phòng phân công (`Assign`) chuyên viên thụ lý.
- **FR-STF-03: Quản lý ưu tiên & thời hạn (29h)**: Gán độ ưu tiên (`Low`, `Medium`, `High`, `Urgent`), tính toán và theo dõi cảnh báo hạn SLA.
- **FR-STF-04: Xử lý & cập nhật yêu cầu (39h)**: Ghi chú nội bộ, yêu cầu sinh viên bổ sung hồ sơ (tạm dừng SLA), cập nhật tiến độ.
- **FR-STF-05: Chuyển xử lý, Escalation & hoàn tất (32h)**: Chuyển tiếp phòng ban (Transfer), báo cáo vượt cấp (Escalation), hoàn tất giải quyết (Resolve).
- **FR-STF-06: Đóng & mở lại yêu cầu (26h)**: Đóng Ticket tự động (sau 3 ngày `RESOLVED`) hoặc thủ công; mở lại Ticket khi có khiếu nại.

### 1.3 Phân hệ Quản trị & Báo cáo (M3 – Admin / Management: 215h kế hoạch)
- **FR-ADM-01: Quản lý tài khoản, vai trò & RBAC (64h)**: Quản lý vòng đời tài khoản, xác thực mã hóa, phân quyền vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`).
- **FR-ADM-02: Quản lý phòng ban & danh mục (26h)**: Thiết lập cơ cấu phòng ban, quản lý danh mục nhóm vấn đề và luồng tiếp nhận.
- **FR-ADM-03: Kiểm soát quyền truy cập & Audit Trail (40h)**: Bảo mật tệp đính kèm qua Secured API Proxy, ghi vết nhật ký hệ thống bất biến (Append-only).
- **FR-ADM-04: Quản lý thời hạn lưu trữ (15h)**: Thiết lập chính sách lưu trữ dữ liệu (Retention), dọn dẹp file tạm, archiving ticket cũ.
- **FR-ADM-05: Dashboard & thống kê quản trị (33h)**: Thẻ chỉ số KPI thời gian thực, biểu đồ phân bố trạng thái và khối lượng theo phòng ban.
- **FR-ADM-06: Báo cáo, mức độ hài lòng & xuất dữ liệu (37h)**: Báo cáo thời gian xử lý trung bình, top nhóm sự cố, tổng hợp CSAT, xuất Excel/CSV.

### 1.4 Hoạt động Cấp dự án (Project Management & DevOps: 100h kế hoạch)
- **Quản lý dự án & điều phối (PM)**: 70h.
- **Môi trường, CI/CD, triển khai & bàn giao (DevOps)**: 30h.

---

## 2. Giả Định Dự Án (Project Assumptions)

1. **Quy mô người dùng**: Hệ thống phục vụ khoảng **3.000 sinh viên** và khoảng **50 - 100 nhân viên/quản lý** tại Aurora University.
2. **Nền tảng vận hành**: Hệ thống là ứng dụng Web (Web Application), tối ưu hiển thị responsive cho trình duyệt PC và Thiết bị di động. Không yêu cầu xây dựng Mobile App cài đặt trên Android/iOS.
3. **Ngôn ngữ giao diện**: Giao diện người dùng hỗ trợ 2 ngôn ngữ **Tiếng Việt và Tiếng Anh** ở mức cơ bản (Static localization).
4. **Hạ tầng & Tên miền**: Aurora University (Client) chịu trách nhiệm cung cấp máy chủ, tên miền và SSL.
5. **Thời gian phê duyệt**: Lịch trình thực hiện không bao gồm thời gian chờ phản hồi vượt quá 03 ngày làm việc từ phía Client.
6. **An toàn thông tin**: Bảo mật cơ bản (OWASP Top 10, RBAC, hash password, API Proxy file). Không bao gồm chi phí thuê bên thứ ba Pentest độc lập.

---

## 3. Ràng Buộc Dự Án (Project Constraints)

- **Thời gian**: **14 tuần (70 ngày làm việc)** phát triển và kiểm thử nội bộ + **10 ngày làm việc** UAT chính thức.
- **Ngân sách hợp đồng**: **300.000.000 VNĐ** (Ba trăm triệu đồng chẵn).
- **Chi phí nhân sự nội bộ cơ sở (618h)**: **186.557.727 VNĐ**.
- **Dự phòng rủi ro công sức**: **22h** (tương đương **6.641.214 VNĐ**).
- **Tổng công sức kế hoạch**: **640h** (tương đương **193.198.941 VNĐ** chi phí nhân sự kế hoạch).
- **Phạm vi thay đổi (Change Requests)**: Mọi yêu cầu thay đổi tính năng ngoài phạm vi thống nhất sẽ được đánh giá lại về chi phí và tiến độ bằng văn bản bổ sung.