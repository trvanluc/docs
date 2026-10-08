# Yêu Cầu Về Độ Ổn Định & Tin Cậy (Reliability Requirements)

## 1. Tính Sẵn Sàng Của Hệ Thống (Availability)
* **Thời gian hoạt động (Uptime):** Hệ thống hướng tới duy trì độ sẵn sàng khoảng 98.5% trong thời gian vận hành chính thức tại nhà trường.
* **Phụ thuộc hạ tầng:** Tính ổn định và độ sẵn sàng của hệ thống phụ thuộc trực tiếp vào chất lượng hạ tầng máy chủ, đường truyền mạng và Tên miền do Aurora University cung cấp.

---

## 2. Toàn Vẹn Dữ Liệu & Xử Lý Sự Cố
* **Toàn vẹn giao dịch:** Các thao tác quan trọng như tạo Ticket, chuyển phòng ban, đóng Ticket phải đảm bảo tính toàn vẹn dữ liệu (Atomic Transaction). Nếu có lỗi xảy ra giữa chừng, hệ thống phải Rollback hoàn toàn dữ liệu về trạng thái trước đó.
* **Khôi phục trạng thái:** Khi gặp sự cố ngắt kết nối mạng hoặc treo máy chủ, hệ thống không được làm mất mát dữ liệu đang ở trạng thái đã lưu thành công trước đó.
* **Bảo trì & Sao lưu (Out of Scope):** Việc thiết lập cơ chế tự động sao lưu định kỳ (Auto Backup) và theo dõi vận hành máy chủ không thuộc phạm vi trách nhiệm của đơn vị phát triển.