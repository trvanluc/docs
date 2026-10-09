# Mục Tiêu Dự Án & Các Mục Nằm Ngoài Phạm Vi (Goals & Non-Goals)

## 1. Mục Tiêu Cốt Lõi (Core Goals)

### G-01: Tập trung hóa đầu mối tiếp nhận
- **Mục tiêu**: Tập trung 100% các yêu cầu hỗ trợ trực tuyến của sinh viên Aurora University vào hệ thống UniSupport.
- **Tiêu chí đo lường**: 100% yêu cầu khởi tạo trên hệ thống đều được cấp mã Ticket định danh duy nhất (ví dụ: `TK-20261004-0001`).

### G-02: Minh bạch hóa tiến độ xử lý
- **Mục tiêu**: Giúp sinh viên dễ dàng tra cứu trạng thái xử lý và đơn vị/nhân viên đang thụ lý yêu cầu.
- **Tiêu chí đo lường**: Sinh viên xem được tiến độ theo thời gian thực (Real-time status) ngay trên trang cá nhân mà không cần gọi điện hay gửi email truy vấn.

### G-03: Tối ưu quy trình vận hành phòng ban
- **Mục tiêu**: Chuẩn hóa luồng làm việc của nhân viên từ khâu tiếp nhận, phân loại, chuyển phòng ban đến cập nhật kết quả.
- **Tiêu chí đo lường**: Giảm tỷ lệ bỏ sót yêu cầu xuống **0%**; giảm thời gian chuyển tiếp công việc giữa các phòng ban.

### G-04: Cung cấp năng lực giám sát cho Ban quản lý
- **Mục tiêu**: Cung cấp Dashboard tổng quan và Báo cáo chi tiết về khối lượng công việc, tỷ lệ hoàn thành, thời gian xử lý trung bình và chỉ số hài lòng.
- **Tiêu chí đo lường**: Xuất được báo cáo trực quan theo khoảng thời gian và theo từng phòng ban.

### G-05: Bảo mật và Phân quyền truy cập
- **Mục tiêu**: Đảm bảo đúng người đúng việc, file đính kèm chỉ người có thẩm quyền mới được truy cập.
- **Tiêu chí đo lường**: Áp dụng mô hình RBAC cho 4 vai trò đã có (STUDENT, STAFF, MANAGER, ADMIN), tra soát log thao tác cho các hành động quan trọng.

---

## 2. Các Mục Nằm Ngoài Phạm Vi Hiện Tại (Out of Scope / Non-Goals)

Để đảm bảo dự án hoàn thành đúng tiến độ **14 tuần** và ngân sách **300 triệu VNĐ**, các hạng mục sau **KHÔNG** thuộc phạm vi triển khai của hợp đồng này:

| STT | Hạng Mục Nằm Ngoài Phạm Vi | Lý Do / Giải Thích |
| :---: | :--- | :--- |
| **NG-01** | **Mobile App độc lập (iOS / Android)** | Hệ thống chỉ phát triển dạng **Web Application** (Responsive giao diện trên di động). Không phát triển app native trên App Store / Google Play. |
| **NG-02** | **Tích hợp hệ thống bên thứ ba nâng cao** | Không tích hợp với hệ thống quản lý đào tạo (ERP), phần mềm kế toán, hay hệ thống SSO phức tạp ngoài phạm vi thống nhất. |
| **NG-03** | **Quản trị hạ tầng máy chủ & Backup tự động** | Đơn vị phát triển bàn giao script/tài liệu cài đặt. Việc thiết lập tự động sao lưu, giám sát hạ tầng máy chủ lâu dài do Aurora University tự đảm nhận. |
| **NG-04** | **Phân quyền nhiều cấp & Audit Log nâng cao** | Chỉ hỗ trợ mô hình phân quyền 4 vai trò đã có (STUDENT, STAFF, MANAGER, ADMIN) và lưu log thao tác cơ bản. Không hỗ trợ phân quyền ma trận đa cấp độ hoặc ghi log chi tiết mức dữ liệu sâu. |
| **NG-05** | **Chat trực tiếp (Livechat) / Gọi thoại (VoIP)** | Không tích hợp khung chat real-time hoặc gọi điện trực tiếp trong hệ thống. Mọi trao đổi diễn ra qua tính năng nhắn/gửi yêu cầu bổ sung thông tin trên Ticket. |
| **NG-06** | **Tối ưu chịu tải lớn (> 3.000 sinh viên)** | Hệ thống được thiết kế tối ưu cho quy mô 3.000 sinh viên của Aurora University, không chịu trách nhiệm tối ưu kiến trúc Microservices/Load Balancing phức tạp cho hàng trăm nghìn truy cập đồng thời. |
| **NG-07** | **Kiểm thử thâm nhập (Pentest) & Chứng nhận bảo mật** | Không bao gồm chi phí thuê bên thứ ba đánh giá an toàn thông tin chuyên sâu hoặc cấp chứng chỉ bảo mật quốc tế (ISO/IEC 27001, SOC2...). |
