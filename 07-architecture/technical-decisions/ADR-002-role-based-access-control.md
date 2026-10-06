# [ADR-002] Giải pháp phân quyền 3 vai trò (RBAC Strategy)

* **Trạng thái:** Đã phê duyệt (Accepted)
* **Ngày quyết định:** 2026-10-05
* **Người quyết định:** Security Architect / Tech Lead
* **Phân hệ liên quan:** `M05-rbac-security`, `05-non-functional-requirements/security.md`

---

## 1. Bối cảnh (Context)
UniSupport phục vụ 3 nhóm đối tượng chính tại Aurora University với thẩm quyền khác nhau:
1. **Sinh viên (Student):** Chỉ truy cập và tương tác với các Ticket của chính mình.
2. **Nhân viên (Staff):** Truy cập, phân loại, chuyển tiếp và xử lý Ticket thuộc phòng ban được gán.
3. **Quản lý (Manager):** Xem báo cáo tổng quan, quản lý danh mục và tài khoản hệ thống.

Cần một mô hình phân quyền vừa đảm bảo an toàn dữ liệu, vừa linh hoạt, đơn giản để triển khai trong quy mô dự án 14 tuần.

## 2. Các phương án xem xét (Options Considered)
1. **Phương án 1: Hardcode phân quyền trực tiếp trong code theo Role Name (Simple RBAC)**
   - *Ưu điểm:* Phát triển nhanh, logic đơn giản.
   - *Nhược điểm:* Cứng nhắc, khó mở rộng nếu sau này nhà trường chia thêm vai trò nhỏ (VD: Trưởng phòng vs Nhân viên).
2. **Phương án 2: Mô hình RBAC dựa trên Quyền (Permission-based / ABAC)**
   - *Ưu điểm:* Rất linh hoạt, phân quyền tới từng nút bấm/API.
   - *Nhược điểm:* Phức tạp, tốn thời gian thiết kế cơ sở dữ liệu và middleware kiểm tra quyền.

## 3. Quyết định (Decision)
Lựa chọn **Phương án 1 kết hợp Scoping theo Context**:
- Định nghĩa 3 Role cố định: `ROLE_STUDENT`, `ROLE_STAFF`, `ROLE_MANAGER`.
- **JWT (JSON Web Token)** chứa thông tin `user_id`, `role`, và `department_id` (đối với Staff).
- Sử dụng **Middleware / Interceptor** tại Backend API để kiểm tra:
  - **Role Level:** Quyền truy cập API (VD: API xem Dashboard chỉ cho `ROLE_MANAGER`).
  - **Data Level (Data Scoping):**
    - `ROLE_STUDENT`: Query ép điều kiện `WHERE student_id = current_user_id`.
    - `ROLE_STAFF`: Query ép điều kiện `WHERE department_id = current_staff_department_id`.

## 4. Hệ quả (Consequences)
* **Tích cực:** Tối ưu thời gian phát triển, đáp ứng hoàn hảo phạm vi dự án, bảo mật dữ liệu ở cả 2 cấp độ (Route & Data).
* **Tiêu cực:** Nếu nhà trường muốn tùy chỉnh phân quyền chi tiết cho từng cá nhân trong tương lai sẽ cần nâng cấp mô hình DB.