# [ARC-03] Mô hình Dữ liệu & Cơ sở Dữ liệu (Data Model & Schema)

Tài liệu này mô tả chi tiết mô hình dữ liệu quan hệ (Relational Database Schema) cho hệ thống **UniSupport**, bao gồm sơ đồ ERD, định nghĩa các bảng (Tables), quan hệ giữa các thực thể và chiến lược đánh chỉ mục (Indexing).

---

## 🗂️ 1. Sơ đồ Quan hệ Thực thể (Entity Relationship Diagram - ERD)

```text
+-------------------+       1:N       +-------------------+       1:N       +-------------------+
|    departments    |----------------<|       users       |----------------<|      tickets      |
+-------------------+                 +-------------------+                 +-------------------+
| id (PK)           |                 | id (PK)           |                 | id (PK)           |
| code              |                 | department_id(FK) |                 | ticket_code (UQ)  |
| name              |                 | email (UQ)        |                 | student_id (FK)   |
| description       |                 | password_hash     |                 | department_id(FK) |
| created_at        |                 | full_name         |                 | assigned_staff(FK)|
+-------------------+                 | role (ENUM)       |                 | category_id (FK)  |
                                      | status            |                 | priority (ENUM)   |
                                      +-------------------+                 | status (ENUM)     |
                                                |                           | title             |
                                                | 1:N                       | description       |
                                                |                           | created_at        |
                                                v                           +-------------------+
                                      +-------------------+                   |     |     |
                                      |    audit_logs     |                   |     |     |
                                      +-------------------+                   |     |     |
                                      | id (PK)           |                   |     |     |
                                      | user_id (FK)      |                   |     |     |
                                      | action            |                   |     |     |
                                      | details (JSONB)   |                   |     |     |
                                      | created_at        |                   |     |     |
                                      +-------------------+                   |     |     |
                                                                              |     |     |
           +------------------------------------------------------------------+     |     +-----------------------------------+
           | 1:N                                                                    | 1:N                                     | 1:1
           v                                                                        v                                         v
+-------------------+                                                     +-------------------+                     +-------------------+
|ticket_attachments |                                                     |ticket_histories   |                     |  ticket_ratings   |
+-------------------+                                                     +-------------------+                     +-------------------+
| id (PK)           |                                                     | id (PK)           |                     | id (PK)           |
| ticket_id (FK)    |                                                     | ticket_id (FK)    |                     | ticket_id (FK, UQ)|
| file_name         |                                                     | actor_id (FK)     |                     | student_id (FK)   |
| file_path         |                                                     | action_type       |                     | rating_score      |
| file_type         |                                                     | old_status        |                     | comment           |
| file_size         |                                                     | new_status        |                     | created_at        |
| created_at        |                                                     | note              |                     +-------------------+
+-------------------+                                                     | created_at        |
                                                                          +-------------------+
```
# 2. Chi tiết Cấu trúc các Bảng (Table Schemas)

## 2.1. Bảng `departments` (Phòng ban)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key, Auto-increment | Mã định danh phòng ban |
| **code** | VARCHAR(20) | Unique, Not Null | Mã ngắn phòng ban (VD: DT, CTSV, HC) |
| **name** | VARCHAR(100) | Not Null | Tên phòng ban |
| **description** | TEXT | Nullable | Mô tả chức năng nhiệm vụ |
| **created_at** | TIMESTAMP | Default NOW() | Thời gian tạo |

---

## 2.2. Bảng `users` (Người dùng)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key, Auto-increment | Mã người dùng |
| **department_id** | UUID / BIGINT | Foreign Key (`departments.id`), Nullable | Phòng ban công tác (Null đối với Sinh viên) |
| **email** | VARCHAR(100) | Unique, Not Null | Email cá nhân/trường |
| **password_hash** | VARCHAR(255) | Not Null | Mật khẩu mã hóa (Bcrypt) |
| **full_name** | VARCHAR(100) | Not Null | Họ và tên |
| **role** | ENUM | Not Null | Vai trò: `'STUDENT'`, `'STAFF'`, `'MANAGEMENT'` |
| **status** | VARCHAR(20) | Default `'ACTIVE'` | Trạng thái tài khoản (ACTIVE, INACTIVE) |
| **created_at** | TIMESTAMP | Default NOW() | Thời gian khởi tạo |

---

## 2.3. Bảng `tickets` (Phiếu hỗ trợ)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key, Auto-increment | ID kỹ thuật |
| **ticket_code** | VARCHAR(30) | Unique, Not Null | Mã Ticket hiển thị (VD: TK-20261005-001) |
| **student_id** | UUID / BIGINT | Foreign Key (`users.id`), Not Null | Người tạo Ticket |
| **department_id** | UUID / BIGINT | Foreign Key (`departments.id`), Nullable | Phòng ban tiếp nhận xử lý |
| **assigned_staff_id**| UUID / BIGINT | Foreign Key (`users.id`), Nullable | Nhân viên trực tiếp phụ trách |
| **priority** | ENUM | Default `'MEDIUM'` | Mức độ ưu tiên: `'LOW'`, `'MEDIUM'`, `'HIGH'`, `'URGENT'` |
| **status** | ENUM | Default `'NEW'` | Trạng thái: `'NEW'`, `'IN_PROGRESS'`, `'PENDING_INFO'`, `'RESOLVED'`, `'CLOSED'` |
| **title** | VARCHAR(255) | Not Null | Tiêu đề yêu cầu |
| **description** | TEXT | Not Null | Nội dung chi tiết |
| **created_at** | TIMESTAMP | Default NOW() | Thời điểm gửi Ticket |
| **updated_at** | TIMESTAMP | Default NOW() | Thời điểm cập nhật cuối |

---

## 2.4. Bảng `ticket_attachments` (Tệp đính kèm)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key | ID tệp đính kèm |
| **ticket_id** | UUID / BIGINT | Foreign Key (`tickets.id`), Not Null | Tệp thuộc Ticket nào |
| **file_name** | VARCHAR(255) | Not Null | Tên file gốc người dùng tải lên |
| **file_path** | VARCHAR(255) | Not Null | Đường dẫn lưu trữ hệ thống (UUID-renamed) |
| **file_type** | VARCHAR(50) | Not Null | Định dạng MIME (image/png, application/pdf) |
| **file_size** | INTEGER | Not Null | Dung lượng file tính bằng Bytes |
| **created_at** | TIMESTAMP | Default NOW() | Thời gian tải lên |

---

## 2.5. Bảng `ticket_histories` (Lịch sử xử lý Ticket)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key | ID nhật ký |
| **ticket_id** | UUID / BIGINT | Foreign Key (`tickets.id`), Not Null | Ticket liên quan |
| **actor_id** | UUID / BIGINT | Foreign Key (`users.id`), Not Null | Người thực hiện thao tác |
| **action_type** | VARCHAR(50) | Not Null | Loại thao tác (CREATE, ASSIGN, TRANSFER, RESOLVE...) |
| **old_status** | VARCHAR(20) | Nullable | Trạng thái trước thao tác |
| **new_status** | VARCHAR(20) | Nullable | Trạng thái sau thao tác |
| **note** | TEXT | Nullable | Ghi chú/Nội dung phản hồi |
| **created_at** | TIMESTAMP | Default NOW() | Thời điểm thực hiện |

---

## 2.6. Bảng `ticket_ratings` (Đánh giá mức độ hài lòng)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key | ID đánh giá |
| **ticket_id** | UUID / BIGINT | Foreign Key (`tickets.id`), Unique, Not Null | Ticket được đánh giá (1:1) |
| **student_id** | UUID / BIGINT | Foreign Key (`users.id`), Not Null | Sinh viên đánh giá |
| **rating_score** | SMALLINT | Not Null, Check ($1 \le \text{rating\_score} \le 5$) | Điểm số đánh giá (1 đến 5 sao) |
| **comment** | TEXT | Nullable | Ý kiến đóng góp |
| **created_at** | TIMESTAMP | Default NOW() | Thời điểm gửi đánh giá |

---

# ⚡ 3. Chỉ mục (Indexes) & Tối ưu hóa truy vấn

Nhằm đảm bảo tốc độ truy xuất mượt mà trên quy mô 3.000 sinh viên, hệ thống thiết lập các Index cơ bản:

- **`idx_tickets_student_id`**: Tối ưu danh sách Ticket cá nhân của Sinh viên (`tickets.student_id`).
- **`idx_tickets_department_status`**: Tối ưu lọc Ticket theo phòng ban & trạng thái cho Nhân viên (`tickets.department_id`, `tickets.status`).
- **`idx_tickets_code`**: Truy vấn nhanh bằng Mã Ticket (`tickets.ticket_code`).
- **`idx_histories_ticket_id`**: Lấy mượt mà tiến độ/lịch sử thay đổi (`ticket_histories.ticket_id`).