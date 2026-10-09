# [NFR-OBS] Yêu cầu về Giám sát & Ghi log (Observability & Logging Requirements)

### 1. Tổng quan
Tài liệu định nghĩa các yêu cầu về khả năng quan sát, theo dõi trạng thái hoạt động và lưu trữ nhật ký hệ thống (System Logs) nhằm hỗ trợ quản trị viên Aurora University dễ dàng tra soát, phát hiện và chẩn đoán sự cố khi vận hành hệ thống Web Application UniSupport.

### 2. Cấu trúc và Quy định Ghi Log (Logging Standards)
Hệ thống triển khai 2 nhóm log chính:

#### 2.1 System & Application Log (Log hệ thống & Ứng dụng)
- **Cấp độ Log (Log Levels):** `INFO`, `WARN`, `ERROR`.
- **Định dạng chuẩn:** JSON/Plain text bao gồm các trường bắt buộc:
  - `timestamp`: Thời gian phát sinh sự cố (định dạng ISO 8601).
  - `level`: Cấp độ nghiêm trọng.
  - `module`: Phân hệ phát sinh log (VD: `M01-student-portal`, `M05-rbac`).
  - `message`: Nội dung mô tả chi tiết.
  - `stack_trace`: Lỗi kỹ thuật chi tiết (chỉ áp dụng đối với cấp độ `ERROR`).

#### 2.2 Audit Log (Log tra soát nghiệp vụ)
- Tự động ghi lại các thao tác ghi/sửa/xóa dữ liệu quan trọng của người dùng.
- Thông tin lưu trữ: `User_ID`, `Role`, `Action_Type`, `Resource_Target` (Ticket ID, Account ID), `IP_Address`, `Timestamp`.

### 3. Giám sát Trạng thái (System Monitoring)
- **Health Check Endpoint:** Cung cấp API `/api/v1/health` công khai ở mức cơ bản để hạ tầng của nhà trường kiểm tra trạng thái hoạt động của Service (Database Connection, File System Storage).
- **Lưu trữ Log:** Nhật ký ứng dụng được ghi ra file log theo ngày và giữ tối thiểu 30 ngày trên máy chủ triển khai.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-OBS-01:** Khi phát sinh lỗi kết nối cơ sở dữ liệu hoặc lỗi ứng dụng (5xx), hệ thống phải ghi vết bản ghi `ERROR` kèm chi tiết lỗi vào file log.
- **NFR-OBS-02:** Truy cập API `/api/v1/health` trả về HTTP status `200 OK` kèm trạng thái hoạt động của cơ sở dữ liệu.
- **NFR-OBS-03:** Thao tác đổi vai trò tài khoản hoặc đổi trạng thái Ticket đều sinh bản ghi Audit Log tra soát chính xác.