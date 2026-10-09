# 07-architecture/technical-decisions: Quyết định Kiến trúc Kỹ thuật (ADR)

Thư mục này lưu trữ các **Bản ghi Quyết định Kiến trúc (Architecture Decision Records - ADR)** cho hệ thống UniSupport. Mỗi ADR ghi lại một quyết định kỹ thuật quan trọng, bối cảnh lựa chọn, các phương án cân nhắc và hệ quả đi kèm.

---

## Danh sách các Báo cáo ADR

| Mã ADR | Tiêu đề Quyết định | Trạng thái | Tóm tắt Giải pháp |
| :--- | :--- | :--- | :--- |
| **[ADR-001](./ADR-001-ticket-id-generation.md)** | Quy tắc sinh mã Ticket duy nhất | Accepted | Sinh mã hiển thị ngắn gọn `TK-YYYYMM-XXXX` cho người dùng; dùng UUID/BigInt cho Primary Key CSDL. |
| **[ADR-002](./ADR-002-role-based-access-control.md)** | Giải pháp phân quyền 3 vai trò (RBAC) | Accepted | Sử dụng RBAC dựa trên JWT với 3 Role chính kết hợp lọc dữ liệu ở cấp độ context (`student_id`, `department_id`). |
| **[ADR-003](./ADR-003-file-attachment-storage.md)** | Phương án lưu trữ & Phân quyền xem file | Accepted | Lưu tệp trong thư mục bảo mật trên máy chủ local, đổi tên file dạng UUID và kiểm soát truy cập qua API Stream Proxy (trả về 403 nếu sai quyền). |

---

## Quy chuẩn Cấu trúc một Báo cáo ADR
Mỗi file ADR tuân thủ thống nhất 4 phần chính:
1. **Bối cảnh (Context):** Vấn đề kỹ thuật hoặc nghiệp vụ cần giải quyết.
2. **Các phương án xem xét (Options Considered):** So sánh ưu/nhược điểm của từng lựa chọn.
3. **Quyết định (Decision):** Giải pháp được thống nhất lựa chọn.
4. **Hệ quả (Consequences):** Các tác động tích cực và hạn chế cần lưu ý khi triển khai.