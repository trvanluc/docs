# ADR-002: Giải Pháp Phân Quyền 3 Vai Trò (Role-Based Access Control)

* **Trạng thái (Status):** Accepted (Đã chấp thuận)
* **Ngày quyết định:** Tuần 3 - Giai đoạn Thiết kế Kiến trúc

---

## 1. Bối Cảnh (Context)
Hệ thống UniSupport yêu cầu cơ chế kiểm soát truy cập phân quyền nghiêm ngặt nhằm đảm bảo mỗi nhóm người dùng chỉ được xem và thao tác trong phạm vi chức năng thuộc thẩm quyền. Theo Project Proposal, hệ thống có 3 nhóm người dùng chính: Sinh viên, Nhân viên phòng ban và Quản lý.

---

## 2. Các Phương Án Cân Nhắc (Options Considered)
1. **Phương án A (Attribute-Based Access Control - ABAC):** Phân quyền dựa trên thuộc tính linh hoạt đa cấp.
   * *Ưu điểm:* Mở rộng cực cao.
   * *Nhược điểm:* Phức tạp không cần thiết, vượt quá phạm vi và ngân sách dự án.
2. **Phương án B (Role-Based Access Control - RBAC Tĩnh - Lựa chọn):** Phân quyền dựa trên 3 vai trò cố định (`Student`, `Staff`, `Manager`/`Admin`).

---

## 3. Quyết Định (Decision)
Thống nhất áp dụng **Mô hình RBAC Tĩnh (Role-Based Access Control)** với 3 vai trò cốt lõi:

1. **`ROLE_STUDENT` (Sinh viên):** Cho phép truy cập Phân hệ Sinh viên. Chỉ xem và thao tác trên các Ticket do chính tài khoản đó sở hữu (`student_id == current_user_id`).
2. **`ROLE_STAFF` (Nhân viên):** Cho phép truy cập Phân hệ Nhân viên. Xem và thao tác trên các Ticket thuộc Phòng ban của nhân viên đó (`department_id == staff_department_id`) hoặc được giao trực tiếp.
3. **`ROLE_MANAGER` / `ROLE_ADMIN` (Quản lý):** Cho phép truy cập Dashboard báo cáo tổng quan toàn trường, báo cáo hiệu suất các phòng ban và chức năng Quản trị tài khoản/phân quyền.

---

## 4. Hệ Quả & Đánh Giá (Consequences)
* **Tích cực:** Kiến trúc đơn giản, an toàn, bám sát chính xác phạm vi yêu cầu, dễ dàng triển khai xác thực JWT/Session-based middleware.
* **Hạn chế:** Không hỗ trợ phân quyền tùy biến sâu nhiều cấp phức tạp (phù hợp với quy định Out of Scope trong Proposal).