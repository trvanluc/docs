# Yêu Cầu Phi Chức Năng (Non-Functional Requirements)

## 1. Tổng Quan
Thư mục này xác định các tiêu chuẩn và yêu cầu phi chức năng (NFR) bắt buộc cho hệ thống **UniSupport** tại **Aurora University**. Các tiêu chuẩn này đảm bảo hệ thống vận hành ổn định, an toàn, dễ sử dụng và phù hợp với quy mô cùng hạ tầng đã thỏa thuận.

---

## 2. Danh Sách Các Hạng Mục Yêu Cầu Phi Chức Năng

| Mã Tài Liệu | Hạng Mục NFR | Nội Dung Trọng Tâm |
| :--- | :--- | :--- |
| **`performance.md`** | Hiệu năng (Performance) | Đáp ứng tối đa 3.000 sinh viên, thời gian phản hồi API < 2 giây. |
| **`security.md`** | Bảo mật (Security) | Đăng nhập tài khoản cá nhân, bảo mật file đính kèm, phân quyền RBAC. |
| **`reliability.md`** | Độ ổn định (Reliability) | Tính sẵn sàng của hệ thống trên môi trường máy chủ của Client. |
| **`usability.md`** | Tính dễ sử dụng (Usability) | Giao diện Responsive (PC & Mobile), hỗ trợ 2 ngôn ngữ VI/EN. |
| **`observability.md`** | Ghi vết & Giám sát (Observability) | Nhật ký hoạt động (Audit log) cơ bản và ghi nhận lỗi hệ thống. |
| **`deployment.md`** | Triển khai (Deployment) | Quy trình đóng gói và bàn giao triển khai trên Server/Domain của Client. |