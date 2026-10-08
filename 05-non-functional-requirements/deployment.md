# Yêu Cầu Triển Khai Hạ Tầng (Deployment Requirements)

## 1. Môi Trường Triển Khai
* **Hạ tầng triển khai:** Hệ thống UniSupport được triển khai trực tiếp lên hạ tầng máy chủ (Server) do **Aurora University** cung cấp theo thỏa thuận.
* **Môi trường:**
  * **Staging / UAT Environment:** Phục vụ công tác kiểm thử chấp nhận người dùng (UAT) trong 10 ngày làm việc.
  * **Production Environment:** Môi trường vận hành chính thức cho nhà trường.

---

## 2. Đóng Gói & Tên Miền
* **Tên miền (Domain):** Hệ thống được cấu hình chạy trên Tên miền chính thức do nhà trường cấp và trỏ về máy chủ triển khai.
* **Đóng gói phần mềm:** Mã nguồn Frontend và Backend được đóng gói dạng container (như Docker) hoặc các bản build tối ưu để dễ dàng cài đặt và vận hành trên hệ điều hành máy chủ của Client.
* **Tài liệu hướng dẫn:** Cung cấp tài liệu hướng dẫn cài đặt, cấu hình môi trường và vận hành chi tiết cho bộ phận kỹ thuật của nhà trường khi bàn giao.