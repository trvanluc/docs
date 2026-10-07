# Thiết Kế Kiến Trúc & Kỹ Thuật Hệ Thống (System Architecture)

## 1. Tổng Quan
Thư mục này tài liệu hóa chi tiết kiến trúc tổng thể, mô hình dữ liệu, thiết kế RESTful API và cơ chế bảo mật của hệ thống **UniSupport** tại **Aurora University**. Các thiết kế đảm bảo hệ thống đáp ứng tốt quy mô 3.000 sinh viên, bảo mật dữ liệu và triển khai mượt mà trên hạ tầng của nhà trường.

---

## 2. Cấu Trúc Tài Liệu Kiến Trúc

| Mã Tài Liệu | Tên Tài Liệu | Nội Dung Trọng Tâm |
| :--- | :--- | :--- |
| **`system-context.md`** | Sơ Đồ Ngữ Cảnh (System Context) | Vị trí của UniSupport trong hệ sinh thái ứng dụng của Aurora University. |
| **`architecture-overview.md`** | Kiến Trúc Tổng Quan | Mô hình phân tầng Web Application (Frontend Responsive, Backend API Server, CSDL). |
| **`data-model.md`** | Mô Hình Dữ Liệu & ERD | Sơ đồ ERD và chi tiết bảng cơ sở dữ liệu quan hệ (PostgreSQL/MySQL). |
| **`api-design.md`** | Thiết Kế RESTful API | Danh mục end-points chuẩn RESTful cho 3 phân hệ (Sinh viên, Nhân viên, Quản lý). |
| **`security-design.md`** | Thiết Kế Bảo Mật & Xác Thực | Cơ chế xác thực Session/JWT, phân quyền RBAC 3 vai trò và bảo vệ File. |
| **`technical-decisions/`** | Các Quyết Định Kiến Trúc (ADRs) | Báo cáo ADR-001 (Ticket ID), ADR-002 (RBAC), ADR-003 (File Storage). |