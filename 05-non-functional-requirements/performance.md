# [NFR-PERF] Yêu cầu về Hiệu năng (Performance Requirements)

### 1. Tổng quan
Tài liệu này xác định các chỉ số hiệu năng mục tiêu cho hệ thống UniSupport. Hệ thống được thiết kế tối ưu cho quy mô **3.000 sinh viên** tại Aurora University và không bao gồm yêu cầu tối ưu cho kiến trúc chịu tải lớn vượt quá phạm vi này.

### 2. Chỉ số hiệu năng chính (KPIs)

| Chỉ số | Mục tiêu | Điều kiện thử nghiệm |
| :--- | :--- | :--- |
| **Thời gian phản hồi trang (Page Load Time)** | $\le 2.0$ giây | Tải trang trên kết nối mạng tiêu chuẩn ($\ge 10$ Mbps) |
| **Thời gian xử lý API (API Response Time)** | $\le 500$ ms | Cho 95% các tác vụ CRUD thông thường (Read/Write Ticket) |
| **Tải concurrent (Concurrent Users)** | 100 - 150 người dùng đồng thời | Tương ứng đỉnh điểm giờ cao điểm của trường |
| **Dung lượng tệp đính kèm (File Attachment)** | Tối đa 10 MB / tệp | Định dạng cho phép: `.pdf`, `.jpg`, `.png` |
| **Thời gian tải lên tệp (Upload Speed)** | $\le 5.0$ giây | Đối với tệp dung lượng tối đa 10 MB |

### 3. Quy định về Giới hạn Tải (Load & Capacity Limits)
- **Quy mô người dùng:** Hệ thống đảm bảo hoạt động mượt mà với cơ sở dữ liệu lên đến 3.000 tài khoản sinh viên và khoảng 50-100 tài khoản cán bộ/quản lý.
- **Giới hạn chịu tải:** Hệ thống không cam kết duy trì hiệu năng nếu lượng truy cập đồng thời vượt quá 300 người dùng cùng thời điểm.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-PERF-01:** Khi 100 người dùng thực hiện thao tác gửi/xem Ticket cùng lúc, thời gian phản hồi trung bình của API không vượt quá 1.0 giây.
- **NFR-PERF-02:** Thao tác tải lên tệp đính kèm PDF dung lượng 5 MB hoàn tất trong thời gian dưới 3 giây.