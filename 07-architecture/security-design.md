# Thiết Kế Bảo Mật & Xác Thực (Security & Access Control)

## 1. Xác Thực & Ủy Quyền (Authentication & Authorization)
* **Xác thực danh tính:** Hệ thống áp dụng cơ chế xác thực dựa trên Token (JWT) hoặc Session bảo mật qua kết nối HTTPS.
* **Chống giả mạo:** Token đăng nhập lưu thông tin ID người dùng, vai trò (`Role`) và ID phòng ban liên kết. Mọi API private bắt buộc phải đi kèm Bearer Token trên header.

---

## 2. Kiểm Soát Truy Cập Phân Quyền (RBAC Middleware)
Backend xây dựng Middleware phân quyền kiểm tra theo ma trận vai trò (`ADR-002`):
* **Đối với Endpoint Sinh viên:** Middleware kiểm tra Token có vai trò `STUDENT`. Kiểm tra ID sinh viên trong Ticket trùng khớp với ID người dùng trong Token.
* **Đối với Endpoint Nhân viên:** Middleware kiểm tra Token có vai trò `STAFF`. Kiểm tra phòng ban xử lý Ticket trùng với phòng ban của nhân viên.
* **Đối với Endpoint Quản lý:** Middleware chặn toàn bộ truy cập không có vai trò `MANAGER` hoặc `ADMIN`.

---

## 3. An Toàn File & Dữ Liệu Nhạy Cảm
* **Bảo mật File đính kèm (`ADR-003`):** Tuyệt đối không lưu file trong thư mục công khai (`/public`). API xem file kiểm tra danh tính và trả dữ liệu dưới dạng FileStream trực tiếp.
* **Lọc dữ liệu độc hại:** Áp dụng Sanitize Input chống các cuộc tấn công Cross-Site Scripting (XSS), SQL Injection và validate dung lượng file strictly dưới 5MB.
* **Nhật ký tra soát (Audit Log):** Tự động ghi lại log thao tác đổi quyền, đổi trạng thái Ticket kèm địa chỉ IP vào bảng `audit_logs`.