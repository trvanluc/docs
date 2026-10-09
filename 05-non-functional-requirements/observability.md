# Yêu Cầu Về Ghi Vết & Giám Sát (Observability Requirements)

## 1. Tổng Quan Kiến Trúc Giám Sát (Observability Architecture)
Hệ thống UniSupport bắt buộc phải triển khai cơ chế Giám sát & Ghi vết tập trung nhằm đảm bảo khả năng tra soát sự cố, kiểm toán an toàn thông tin và theo dõi hiệu năng hệ thống theo thời gian thực. Hệ thống Observability bao gồm 3 trụ cột chính:
1. **System Error & Exception Logging:** Ghi nhận lỗi phần mềm, ngoại lệ hệ thống phục vụ Debugging.
2. **Business Audit Trail (Audit Logging):** Ghi vết các biến động dữ liệu nghiệp vụ nhạy cảm và thao tác quản trị.
3. **Application Performance & Metric Monitoring:** Giám sát thời gian phản hồi API và trạng thái vận hành tài nguyên.

## 2. Ghi Nhận Lỗi Hệ Thống (System Error Logging Specs)

### 2.1. Cấu Trúc Bản Ghi Log Chuẩn (Structured JSON Logging Format)
Mọi bản ghi Log hệ thống do Backend xuất ra BẮT BUỘC phải tuân thủ chuẩn Structured JSON Format (một dòng JSON duy nhất cho mỗi sự kiện log) để phục vụ thu thập và truy vấn tự động:

| Trường Dữ Liệu | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả & Rules Kỹ Thuật |
| :--- | :--- | :---: | :--- |
| `timestamp` | String (ISO 8601) | Có | Định dạng UTC chuẩn `YYYY-MM-DDTHH:mm:ss.SSSZ` (Ví dụ: `2026-10-09T14:30:00.123Z`). |
| `level` | Enum | Có | Cấp độ Log: `INFO`, `WARN`, `ERROR`, `FATAL`. |
| `trace_id` | UUID v4 | Có | Mã định danh luồng xử lý duy nhất truyền xuyên suốt từ API Gateway $\rightarrow$ Service $\rightarrow$ Database query. |
| `service_name` | String | Có | Tên Service phát sinh log (Ví dụ: `unisupport-backend-api`). |
| `endpoint` | String | Không | Đường dẫn API / Function thực thi (Ví dụ: `POST /api/v1/tickets`). |
| `user_id` | String | Không | ID của người dùng thực hiện request (Mặc định `ANONYMOUS` nếu chưa đăng nhập). |
| `ip_address` | String | Có | Địa chỉ Client IP thực tế (Đọc từ HTTP Header `X-Forwarded-For` hoặc `X-Real-IP`). |
| `message` | String | Có | Thông điệp lỗi / mô tả vắn tắt sự kiện. |
| `exception_class` | String | Không | Tên Class ngoại lệ (Ví dụ: `NullPointerException`, `DatabaseConnectionException`). |
| `stack_trace` | Text | Không | Toàn bộ thông tin Stack trace kỹ thuật khi có lỗi Unhandled Exception (`level = ERROR` hoặc `FATAL`). |

### 2.2. Phân Cấp Mức Độ Log (Log Levels Policy)
- **INFO:** Ghi nhận các sự kiện vận hành bình thường (Khởi động Server, Scheduled Cronjob hoàn thành, API Healthcheck).
- **WARN:** Ghi nhận các bất thường không gây gián đoạn dịch vụ (Request bị từ chối do Client Validation lỗi, Retry kết nối Redis/DB thành công, File upload cận ngưỡng 5MB).
- **ERROR:** Ghi nhận toàn bộ lỗi ngoại lệ không mong muốn (HTTP 500, Lỗi Query CSDL, Lỗi kết nối Storage, Lỗi Timeout API bên ngoài).
- **FATAL:** Lỗi nghiêm trọng khiến hệ thống bị sập hoặc ngừng dịch vụ hoàn toàn (Database crash, Out of Memory).

## 3. Nhật Ký Thao Tác & Kiểm Toán (Audit Logging Specs)

### 3.1. Danh Mục Thao Tác Bắt Buộc Ghi Audit Log
Audit Log lưu trữ vĩnh viễn dữ liệu tra soát các hành động làm thay đổi trạng thái hệ thống hoặc dữ liệu nhạy cảm. Tuyệt đối không được phép chỉnh sửa hay xóa bản ghi Audit Log (Append-Only Data Store):

| Nhóm Thao Tác | Mã Hành Động (`action_code`) | Đối Tượng Tác Động (`target_type`) | Mô Tả Dữ Liệu Cần Lưu |
| :--- | :--- | :--- | :--- |
| **Xác thực** | `AUTH_LOGIN_SUCCESS` | USER | Ghi nhận Đăng nhập thành công, IP, Device User-Agent. |
| | `AUTH_LOGIN_FAILED` | USER | Ghi nhận Đăng nhập thất bại, Lý do sai mật khẩu/khóa tài khoản. |
| | `AUTH_LOGOUT` | USER | Đăng xuất, vô hiệu hóa Token. |
| **Nghiệp vụ Ticket** | `TICKET_CREATE` | TICKET | Khởi tạo Ticket mới (`ticket_id`, `student_id`, `category_id`). |
| | `TICKET_CLAIM` | TICKET | Nhân viên tiếp nhận xử lý (`staff_id`, `priority`). |
| | `TICKET_TRANSFER` | TICKET | Chuyển phòng ban (`from_dept`, `to_dept`, `transfer_reason`). |
| | `TICKET_REQUEST_MORE` | TICKET | Yêu cầu sinh viên bổ sung hồ sơ (`request_note`). |
| | `TICKET_SUPPLEMENT` | TICKET | Sinh viên gửi bổ sung file/ghi chú (`attachments_count`). |
| | `TICKET_RESOLVE` | TICKET | Hoàn tất xử lý (`resolution_note`). |
| | `TICKET_RATE` | TICKET | Sinh viên gửi đánh giá CSAT (`rating_score`, `rating_comment`). |
| **Quản trị Tài khoản** | `USER_CREATE` | USER | Admin tạo tài khoản mới (`created_user_id`, `role`, `dept`). |
| | `USER_UPDATE_ROLE` | USER | Admin thay đổi Role/Department (`old_role` $\rightarrow$ `new_role`). |
| | `USER_DISABLE` | USER | Admin khóa tài khoản (`disabled_user_id`, `reason`). |
| | `USER_ENABLE` | USER | Admin mở khóa tài khoản. |

### 3.2. Cấu Trúc Bảng CSDL Audit Log (`audit_logs`)
```sql
CREATE TABLE audit_logs (
    log_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    trace_id        UUID NOT NULL,
    timestamp       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    actor_id        VARCHAR(50) NOT NULL,
    actor_role      VARCHAR(20) NOT NULL,
    action_code     VARCHAR(50) NOT NULL,
    target_type     VARCHAR(50) NOT NULL,
    target_id       VARCHAR(50) NOT NULL,
    ip_address      VARCHAR(45) NOT NULL,
    user_agent      TEXT,
    old_value       JSONB,
    new_value       JSONB,
    description     TEXT
);
```
---
## 4. Quản Lý Thời Gian Lưu Trữ & An Toàn Dữ Liệu (Retention & Security Specs)

### 4.1. Chính Sách Lưu Trữ File Log (Retention Policy)
- **Error Log Files:** Lưu giữ trong vòng 30 ngày trên đĩa cứng Server/Storage. Tự động nén log cũ (`.gz`) mỗi ngày và tự động xóa bớt các file log quá 30 ngày qua Cronjob hệ thống.
- **Audit Log Database:** Lưu trữ vĩnh viễn trong CSDL tối thiểu 12 tháng phục vụ công tác thanh tra, kiểm toán của nhà trường.

### 4.2. Bảo Mật & Sanitize Dữ Liệu Nhạy Cảm (Masking Sensitive Data)
Trước khi ghi bất kỳ chuỗi thông tin nào vào File Log hoặc Audit Log, hệ thống Backend BẮT BUỘC phải lọc và mã hóa (Masking) các dữ liệu nhạy cảm sau:
- **Mật khẩu người dùng (`password`):** Tự động thay thế bằng `********`.
- **Token xác thực (`Authorization` / `JWT`):** Chỉ ghi 10 ký tự đầu và 5 ký tự cuối (Ví dụ: `eyJhbGciOi...xYZ123`).
- **Nội dung nhạy cảm:** Bỏ qua hoàn toàn dữ liệu mã hóa mật khẩu hoặc thông tin thẻ/tài khoản ngân hàng (nếu có).

## 5. Phạm Vi Không Triển Khai (Non-Goals)
1. **Không triển khai Full-Tracing APM phức tạp:** Không cài đặt các hệ thống APM đắt đỏ (như Datadog, New Relic) cho quy mô hiện tại.
2. **Không ghi Log SQL Query đọc dữ liệu (`SELECT`):** Chỉ ghi Audit Log cho các lệnh làm biến động dữ liệu (`INSERT`, `UPDATE`, `DELETE`). Không ghi log cho các hành vi xem/tra cứu danh sách thông thường để tránh làm quá tải dung lượng CSDL.