# [NFR-DEP] Yêu cầu về Triển khai & Hạ tầng (Deployment Requirements)

### 1. Tổng quan
Tài liệu quy định các điều kiện hạ tầng, môi trường chạy và quy trình triển khai ứng dụng Web UniSupport lên hệ thống của Aurora University theo thỏa thuận cam kết.

### 2. Điều kiện Hạ tầng do Client (Aurora University) Cung cấp
Phù hợp với các Giả định dự án (Assumptions), hạ tầng máy chủ và tên miền hoàn toàn do nhà trường bàn giao:
- **Máy chủ Web/Database:** Máy chủ ảo (VPS) hoặc máy chủ vật lý chạy OS Linux (Ubuntu Server 20.04/22.04 LTS) hoặc Windows Server.
- **Cấu hình tối thiểu đề xuất:** 
  - CPU: 2 Core vCPU.
  - RAM: 4 GB.
  - Dung lượng đĩa cứng: Tối thiểu 50 GB SSD khả dụng (phục vụ lưu trữ dữ liệu và tệp đính kèm).
- **Mạng & Tên miền:**
  - Tên miền/Tên miền phụ chính thức (VD: `unisupport.aurora.edu.vn`).
  - Cấu hình địa chỉ IP Public và chứng chỉ bảo mật SSL/TLS (HTTPS).

### 3. Phương án Triển khai (Deployment Strategy)
- **Đóng gói ứng dụng:** Hệ thống được đóng gói chuẩn hóa bằng Docker / Docker Compose (bao gồm Frontend, Backend API, Database) giúp việc cài đặt lên hạ tầng của nhà trường diễn ra nhanh chóng, độc lập với môi trường.
- **Môi trường:**
  - **Staging/UAT Environment:** Phục vụ kiểm thử nghiệm thu 10 ngày với nhà trường.
  - **Production Environment:** Môi trường vận hành chính thức sau khi ký nghiệm thu.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-DEP-01:** Hệ thống triển khai thành công trên hạ tầng của Aurora University và truy cập ổn định thông qua tên miền/HTTPS do nhà trường cung cấp.
- **NFR-DEP-02:** Đội ngũ phát triển bàn giao đầy đủ Tài liệu hướng dẫn Cài đặt & Vận hành (Deployment Guide) giúp cán bộ IT nhà trường có thể chủ động khởi động lại service khi cần.