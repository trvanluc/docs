# ADR-002: Giải Pháp Phân Quyền Vai Trò (Role-Based Access Control Strategy)

- **Trạng thái (Status):** Accepted (Đã chấp thuận)
- **Ngày quyết định:** 2026-09-15 (Giai đoạn Thiết kế Kiến trúc)
- **Đối tượng áp dụng:** Backend Engineering Team, Frontend Engineering Team

## 1. Bối Cảnh (Context)
Hệ thống UniSupport phục vụ 3 nhóm đối tượng người dùng có trách nhiệm và quyền hạn hoàn toàn tách biệt: Sinh viên, Nhân viên các phòng ban và Ban Quản lý/Admin.

Hệ thống cần một cơ chế kiểm soát truy cập (Access Control) đảm bảo:
1. **Tính đóng gói và an toàn dữ liệu:** Sinh viên không thấy yêu cầu của nhau, Nhân viên không can thiệp phòng ban khác.
2. **Hiệu năng cao:** Kiểm tra quyền nhanh ($< 1\text{ms}$) trên mỗi request.
3. **Đơn giản, dễ bảo trì, dễ triển khai kiểm thử tự động.**

## 2. Các Phương Án Cân Nhắc (Options Considered)

### Phương án A: Attribute-Based Access Control (ABAC - Phân quyền theo Thuộc tính)
- **Ưu điểm:** Cực kỳ linh hoạt, cho phép định nghĩa luật truy cập phức tạp dựa trên ngữ cảnh (Ví dụ: Chỉ cho sửa Ticket vào giờ hành chính, hoặc khi nhiệt độ phòng máy $< 30^\circ\text{C}$).
- **Nhược điểm:** Phức tạp quá mức cần thiết; tốn thời gian phát triển và chi phí tính toán CPU cho từng request; vượt quá ngân sách và phạm vi dự án UniSupport.

### Phương án B: Static Role-Based Access Control (RBAC - Phân quyền 4 Vai trò Cố định - Được chọn)
- **Ưu điểm:** Cấu trúc phân cấp minh bạch, tích hợp hoàn hảo với JWT Claims, chi phí kiểm tra quyền cực thấp, bám sát 100% yêu cầu bài toán.
- **Nhược điểm:** Không hỗ trợ việc tạo thêm các Vai trò tùy biến động (Custom Dynamic Roles) do người dùng tự định nghĩa trên UI (Phù hợp hoàn toàn với phạm vi Out of Scope của dự án).

## 3. Quy Định Kỹ Thuật Chi Tiết (Detailed Specifications)

### 3.1. Danh Mục 4 Vai Trò Hệ Thống (System Role Definitions)

| Mã Vai Trò (`role`) | Tên Vai Trò | Phạm Vi Quyền Hạn Chi Tiết | Phạm Vi Dữ Liệu TRUY CẬP (Data Scope) |
| :--- | :--- | :--- | :--- |
| **STUDENT** | Sinh viên | Tạo Ticket, xem tiến độ, gửi bổ sung file, gửi đánh giá CSAT ($1-5$ sao). | Chỉ dữ liệu cá nhân: `student_id == current_user.id`. |
| **STAFF** | Nhân viên | Tiếp nhận (Claim), phân loại priority, chuyển phòng ban, yêu cầu bổ sung, ghi kết quả và giải quyết Ticket. | Chỉ dữ liệu phòng ban phụ trách: `department_id == current_user.department_id`. |
| **MANAGER** | Quản lý Phòng ban | Toàn bộ quyền của STAFF + Phân công/Thu hồi Ticket, xem Dashboard chỉ số SLA & CSAT phòng ban. | Dữ liệu thuộc phòng ban phụ trách: `department_id == current_user.department_id`. |
| **ADMIN** | Quản trị Hệ thống | Toàn quyền Quản trị Tài khoản (Tạo, sửa, khóa user), xem Dashboard/Báo cáo toàn trường, xem Audit Log. | Toàn bộ hệ thống (Global Scope): Không bị giới hạn `department_id`. |

### 3.2. Thiết Kế Ma Trận Phân Quyền Middleware (RBAC Authorization Matrix)
Backend triển khai lớp Annotation/Decorator `@RequireRole(...)` hoặc Middleware kiểm tra quyền truy cập trên từng API Endpoint:

| API Endpoint / Chức năng | STUDENT | STAFF | MANAGER | ADMIN |
| :--- | :---: | :---: | :---: | :---: |
| `POST /api/v1/tickets` | X | - | - | - |
| `GET /api/v1/tickets/my-tickets` | X | - | - | - |
| `POST /api/v1/tickets/{id}/rate` | X | - | - | - |
| `GET /api/v1/staff/queue` | - | X | X | X |
| `POST /api/v1/staff/tickets/{id}/*` | - | X | X | X |
| `POST /api/v1/staff/assign` | - | - | X | X |
| `GET /api/v1/reports/department` | - | - | X | X |
| `GET /api/v1/reports/system` | - | - | - | X |
| `POST/PUT/DELETE /api/v1/users` | - | - | - | X |
| `GET /api/v1/audit-logs` | - | - | - | X |

## 4. Hệ Quả & Đánh Giá Kỹ Thuật (Consequences)

### Tích cực (Positive)
- **Hiệu năng vượt trội:** Lớp Guard Middleware chỉ cần kiểm tra chuỗi `user.role` từ JWT Payload thu được ngay sau khi giải mã token mà không cần query lại Database.
- **An toàn triệt để:** Tránh hoàn toàn việc lộ chéo dữ liệu giữa Sinh viên với nhau và giữa các Phòng ban với nhau.
- **Đơn giản hóa Codebase:** Giúp các lập trình viên Frontend và Backend dễ dàng nắm bắt các annotation phân quyền khi viết code.

### Ràng buộc & Lưu ý Bảo trì (Constraints)
- Trường `role` và `department_id` được ghi cố định vào JWT Token tại thời điểm Đăng nhập. Nếu Admin thực hiện đổi Role hoặc Phòng ban của một User, Admin phải kích hoạt API Revoke Token/Session (Redis Blacklist) để ép User đó đăng nhập lại và nhận JWT Token mang vai trò mới.