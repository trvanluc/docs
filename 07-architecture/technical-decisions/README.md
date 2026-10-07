# Quyết Định Kiến Trúc & Kỹ Thuật (Architecture Decision Records - ADR)

## 1. Tổng Quan
Thư mục này lưu trữ các Quyết định Kiến trúc & Kỹ thuật quan trọng (ADR) trong quá trình thiết kế và phát triển hệ thống **UniSupport** cho **Aurora University**[cite: 1]. Mỗi tài liệu ADR ghi nhận bối cảnh, lý do lựa chọn giải pháp, cũng như ưu/nhược điểm và hệ quả của quyết định đó[cite: 1].

---

## 2. Danh Sách Các Báo Cáo ADR

| Mã ADR | Tiêu Đề Quyết Định | Trạng Thái | Tóm Tắt Giải Pháp |
| :--- | :--- | :---: | :--- |
| **`ADR-001`** | Quy tắc sinh mã Ticket duy nhất (Ticket ID Generation) | **ACCEPTED** | Định dạng `TK-YYYYMMDD-XXXX` tự sinh, đảm bảo duy nhất và hỗ trợ tra cứu[cite: 1]. |
| **`ADR-002`** | Giải pháp phân quyền 3 vai trò (Role-Based Access Control) | **ACCEPTED** | Mô hình RBAC tĩnh với 3 vai trò: Sinh viên, Nhân viên, Quản lý[cite: 1]. |
| **`ADR-003`** | Phương án lưu trữ & Phân quyền xem File đính kèm | **ACCEPTED** | Lưu trữ Private Storage, kiểm soát quyền xem qua Chống truy cập trực tiếp URL[cite: 1]. |