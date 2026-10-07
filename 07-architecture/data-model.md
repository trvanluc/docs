# Mô Hình Dữ Liệu & ERD (Data Model)

## 1. Sơ Đồ Quan Hệ Entiy (ERD Overview)

```text
 ┌─────────────────┐       1:N       ┌─────────────────┐
 │      users      │─────────────────┤     tickets     │
 └────────┬────────┘                 └────────┬────────┘
          │                                   │ 1:N
          │ 1:N                               ▼
          │                          ┌─────────────────┐
          │                          │   attachments   │
          ▼                          └─────────────────┘
 ┌─────────────────┐                          │ 1:N
 │   audit_logs    │                          ▼
 └─────────────────┘                 ┌─────────────────┐
                                     │  notifications  │
                                     └─────────────────┘
```

## 2. Cấu Trúc Các Bảng Cơ Sở Dữ Liệu

### 2.1. Bảng `users` (Tài khoản người dùng)

- `id` (VARCHAR/UUID, Primary Key): ID người dùng.
- `username` (VARCHAR, Unique): Tên đăng nhập / Mã sinh viên / Email công vụ.
- `password_hash` (VARCHAR): Mật khẩu đã mã hóa.
- `full_name` (VARCHAR): Họ và tên.
- `role` (ENUM): Vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`).
- `department_id` (VARCHAR, Foreign Key): ID phòng ban (nếu là Nhân viên).
- `status` (VARCHAR): Trạng thái tài khoản (`ACTIVE`, `INACTIVE`).

### 2.2. Bảng `tickets` (Thông tin Phiếu hỗ trợ)

- `ticket_id` (VARCHAR, Primary Key): Mã Ticket duy nhất (ví dụ: `TK-20261007-001`).
- `student_id` (VARCHAR, Foreign Key → `users.id`): Sinh viên khởi tạo.
- `category_id` (VARCHAR): Nhóm vấn đề chọn xử lý.
- `title` (VARCHAR): Tiêu đề ngắn gọn.
- `description` (TEXT): Nội dung mô tả chi tiết vấn đề.
- `department_id` (VARCHAR): Phòng ban chịu trách nhiệm thụ lý.
- `assignee_id` (VARCHAR, Foreign Key → `users.id`): Nhân viên được gán xử lý.
- `priority` (ENUM): Độ ưu tiên (`LOW`, `MEDIUM`, `HIGH`, `URGENT`).
- `status` (ENUM): Trạng thái (`NEW`, `IN_PROGRESS`, `NEED_MORE_INFO`, `TRANSFERRED`, `CLOSED`, `REJECTED`).
- `resolution_note` (TEXT): Kết quả giải quyết của nhân viên.
- `rating_score` (INT): Đánh giá sao của sinh viên (1-5 sao).
- `rating_comment` (TEXT): Nhận xét đánh giá hài lòng.
- `created_at`, `updated_at`, `closed_at` (TIMESTAMP): Các mốc thời gian.

### 2.3. Bảng `attachments` (File đính kèm)

- `id` (VARCHAR/UUID, Primary Key): ID bản ghi file.
- `ticket_id` (VARCHAR, Foreign Key → `tickets.ticket_id`): Mã Ticket liên kết.
- `file_name` (VARCHAR): Tên file gốc.
- `file_path` (VARCHAR): Đường dẫn lưu file riêng tư trên Server.
- `file_size` (INT): Dung lượng file tính bằng bytes (Max 5MB).
- `file_type` (VARCHAR): Định dạng MIME (`application/pdf`, `image/png`, `image/jpeg`).
- `uploaded_by` (VARCHAR, Foreign Key → `users.id`): Người đăng file.

### 2.4. Bảng `audit_logs` (Nhật ký rà soát)

- `id` (BIGINT, Primary Key, Auto Increment).
- `user_id` (VARCHAR, Foreign Key → `users.id`): Người thực hiện.
- `action` (VARCHAR): Hành động (`CREATE_TICKET`, `TRANSFER_DEPT`, `CLOSE_TICKET`, ...).
- `target_id` (VARCHAR): Đối tượng chịu tác động (Mã Ticket, User ID).
- `ip_address` (VARCHAR): Địa chỉ IP truy cập.
- `timestamp` (TIMESTAMP): Thời điểm thực hiện.
