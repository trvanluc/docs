# 07 - Kiến trúc Hệ thống UniSupport (System Architecture)

Thư mục này chứa toàn bộ các tài liệu thiết kế kiến trúc kỹ thuật của hệ thống **UniSupport** (Aurora University Student Support System). Tài liệu đóng vai trò làm kim chỉ nam kỹ thuật cho đội ngũ phát triển, kiểm thử, cũng như hỗ trợ việc bàn giao và vận hành hệ thống.

---

## 📋 Danh mục tài liệu

| STT | Tên File | Mô tả nội dung |
| :---: | :--- | :--- |
| **01** | [`system-context.md`](./system-context.md) | Sơ đồ ngữ cảnh hệ thống (System Context Diagram - C4 Model Level 1), định nghĩa ranh giới hệ thống, các Actor tương tác và các tương tác ngoại vi. |
| **02** | [`architecture-overview.md`](./architecture-overview.md) | Kiến trúc tổng quan hệ thống Web Application (Frontend & Backend), mô hình Layered Architecture, giao tiếp API và lưu trữ dữ liệu. |
| **03** | [`data-model.md`](./data-model.md) | Mô hình cơ sở dữ liệu quan hệ (Relational Database Schema) và sơ đồ ERD chi tiết cho toàn bộ thực thể. |
| **04** | [`api-design.md`](./api-design.md) | Quy chuẩn thiết kế RESTful API cho 3 phân hệ (Sinh viên, Nhân viên, Quản lý) và dịch vụ hệ thống. |
| **05** | [`security-design.md`](./security-design.md) | Thiết kế bảo mật, xác thực tài khoản (Authentication), phân quyền 3 vai trò (RBAC) và bảo mật file đính kèm. |
| **06** | [`technical-decisions/`](./technical-decisions/README.md) | Thư mục lưu trữ các quyết định kiến trúc quan trọng (Architectural Decision Records - ADR). |

---

## 🎯 Nguyên tắc thiết kế cốt lõi (Architecture Principles)

1. **Đơn giản & Tập trung (KISS Principle):**
   * Hệ thống được thiết kế tối ưu cho quy mô **3.000 sinh viên**, tập trung vào tính đúng đắn và ổn định của quy trình xử lý Ticket thay vì áp dụng các kiến trúc phân tán phức tạp không cần thiết (như Microservices/Event-driven).
2. **Bảo mật theo lớp (Defense in Depth):**
   * Áp dụng mô hình **RBAC (Role-Based Access Control)** nghiêm ngặt cho 3 vai trò: Sinh viên, Nhân viên, Quản lý.
   * Kiểm soát quyền truy cập chi tiết đến từng đối tượng Ticket và tệp đính kèm (PDF, PNG/JPG).
3. **Mô-đun hóa cao (Modular Monolith):**
   * Cấu trúc Backend phân tách rõ ràng giữa 3 module nghiệp vụ đã chốt trong proposal (Student, Staff, Management/Admin), kèm các service dùng chung cho Notification, RBAC và Audit Log.
4. **Phù hợp hạ tầng Client:**
   * Tối ưu hóa việc đóng gói và triển khai (Docker Containerized / Node.js Runtime) nhằm đáp ứng linh hoạt trên hạ tầng máy chủ nội bộ hoặc Cloud do Aurora University cung cấp.

---

## 👥 Vai trò sử dụng tài liệu
* **Software Architect / Lead Dev:** Tham chiếu để định hướng phát triển và kiểm soát tuân thủ kiến trúc.
* **Backend / Frontend Developers:** Căn cứ triển khai chi tiết các chức năng, API và cấu trúc dữ liệu.
* **QA / QC Team:** Tham chiếu để xây dựng kịch bản kiểm thử hiệu năng, bảo mật và luồng dữ liệu.
