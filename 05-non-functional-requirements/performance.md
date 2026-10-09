# Yêu Cầu Về Hiệu Năng & Tối Ưu Hệ Thống (Performance Requirements)

## 1. Tổng Quan Sức Chịu Tải & Quy Mô (Capacity Planning & Workload Specs)
Hệ thống UniSupport được thiết kế, tối ưu kiến trúc và kiểm thử hiệu năng bám sát quy mô vận hành thực tế tại Aurora University:
- **Dung lượng Người dùng (Target Capacity):** Phục vụ toàn bộ 3.000 sinh viên cùng khoảng 100 cán bộ, nhân viên, quản lý các phòng ban.
- **Tải Đồng Thời Cao Điểm (Peak Concurrent Users - CCU):** Đáp ứng tối thiểu 150 CCU thao tác đồng thời trên giao diện Web trong các đợt cao điểm (Đợt nộp đơn phúc khảo, đăng ký tốt nghiệp, đầu kỳ học).
- **Tải Tác Vụ API Cao Điểm (Peak API Throughput):** Đạt ngưỡng $50 - 80\text{ Requests/Second (RPS)}$ đối với các tác vụ đọc/ghi tổng hợp mà không làm sụt giảm thời gian phản hồi hoặc gây tràn bộ nhớ CSDL.
- **Phạm Vi Tải Ngoài Mục Tiêu (Out-of-Scope / Non-Goal):** Hệ thống không thiết kế cho quy mô đại chúng (Public Load) và không chịu trách nhiệm xử lý các bài kiểm thử chịu tải cực hạn (Stress Test) vượt quá 500 CCU hoặc $> 200\text{ RPS}$.

## 2. Cam Kết Chỉ Số Thời Gian Phản Hồi (SLA Response Time Matrix)
Toàn bộ các chỉ số đo lường dưới đây được tính toán tại Percentile 95th ($P_{95}$) dưới điều kiện mạng tiêu chuẩn (Băng thông $\ge 10\text{ Mbps}$, RTT Latency $\le 50\text{ ms}$):

| Nhóm Thao Tác / Endpoint Type | Hạn Mức Phản Hồi Tối Đa ($P_{95}$) | Quy Định Tối Ưu Phía Backend & Database |
| :--- | :--- | :--- |
| **First Page Load (Tải trang đầu)** | $< 2.5\text{ giây}$ | Tối ưu Frontend Asset Bundle ($\le 2\text{MB}$ Gzip/Brotli), áp dụng Lazy Loading cho các Component phụ, CDN Caching static files. |
| **API Truy vấn tĩnh (Filter / Detail)** | $< 500\text{ ms}$ | Bắt buộc đánh Index B-Tree cho Foreign Keys, Cache danh mục tĩnh (Categories, Departments) trên Redis Cache. |
| **API Danh sách (Pagination Listing)** | $< 1.000\text{ ms}$ | Bắt buộc Phân trang (Page / Limit). Query CSDL không sử dụng `SELECT *`, bắt buộc liệt kê danh sách cột cần thiết. |
| **API Tạo Ticket / Bổ sung hồ sơ** | $< 1.500\text{ ms}$ | Đọc Stream File upload trực tiếp sang Storage, validate Form bằng Memory Buffer, ghi CSDL trong $1\text{ Transaction}$. |
| **API Xuất Báo Cáo (Excel / CSV)** | $< 3.000\text{ ms}$ | Stream data trả về Client theo Chunk (Tối đa $10.000\text{ bản ghi/lần xuất}$). Không nạp toàn bộ dataset vào RAM Backend. |
| **Dashboard Metrics (Aggregate)** | $< 800\text{ ms}$ | Không Query trực tiếp Aggregate SQL ($COUNT/SUM$) trên toàn bảng `tickets`. Đọc dữ liệu từ Redis Aggregate Cache (TTL $30 - 60\text{ giây}$). |

## 3. Chiến Lược Tối Ưu Hóa Dữ Liệu & Tài Nguyên Storage

### 3.1. Phân Trang Dữ Liệu Chuẩn (Pagination Standards)
Tất cả các API trả về danh sách bản ghi (`tickets`, `conversations`, `users`, `audit_logs`) bắt buộc áp dụng cơ chế Phân trang phía Server (Server-side Pagination):
- **Kích thước Trang Mặc định (Default Limit):** $10$ đến $20\text{ bản ghi/trang}$.
- **Kích thước Trang Tối đa (Max Limit Guard):** Tối đa $50\text{ bản ghi/trang}$. Nếu Client gửi limit > 50, Server tự động ghi đè `limit = 50`.
- **Cấu trúc Response Chuẩn:**
```json
{
  "data": [...],
  "pagination": {
    "current_page": 1,
    "limit": 20,
    "total_records": 150,
    "total_pages": 8
  }
}
```
---
### 3.2. Giới Hạn & Quản Lý Luồng Tải File (File I/O Optimization)
- **Giới Hạn Dung Lượng Strict:** Tối đa $5\text{MB}$ ($5.242.880\text{ Bytes}$) mỗi file. Server ngắt kết nối HTTP ngay khi phát hiện `Content-Length > 5MB` để bảo vệ tài nguyên băng thông.
- **Streaming File Process:** Khâu xem/tải file qua API `/api/v1/attachments/{file_id}` bắt buộc sử dụng Stream Read Chunk ($64\text{KB/Chunk}$) đẩy về HTTP Response Stream. Tuyệt đối không đọc toàn bộ dung lượng file vào bộ nhớ RAM (`readFileSync` is BANNED).

## 4. Chỉ Số Hiệu Năng CSDL & Cấu Hình Cache (Database & Redis Specs)

### 4.1. Tối Ưu Truy Vấn & Indexing CSDL
- **Chỉ mục B-Tree bắt buộc cài đặt:**
  - `tickets`: `(student_id, created_at DESC)`, `(department_id, status)`, `(sla_status, status)`.
  - `ticket_conversations`: `(ticket_id, created_at ASC)`.
  - `audit_logs`: `(timestamp DESC)`, `(actor_id)`.
- **Kiểm Soát Slow Query:** Mọi câu lệnh SQL thực thi $> 200\text{ ms}$ phải được tự động bắt giữ và ghi vào Slow Query Log của CSDL để lập trình viên tối ưu lại Index.
- **Connection Pooling:** Thiết lập Database Connection Pool phía Backend với cấu hình: `min_connections = 5`, `max_connections = 20`, `idle_timeout = 30000ms`.

### 4.2. Chiến Lược Caching Trực Tiếp Trên Redis
- **Session & Token Blacklist Cache:** Lưu trữ JWT Blacklist ID khi logout/khóa tài khoản. Key `blacklist:{jti}`, TTL bằng thời gian sống còn lại của Token.
- **Category & System Config Cache:** Lưu danh mục Categories, Departments. Key `config:categories`, TTL = $24\text{ giờ}$ (Tự động Purge Cache khi Admin sửa danh mục).
- **Dashboard Aggregate Metrics Cache:** Lưu số liệu Summary Cards trên Dashboard Manager/Admin. Key `metrics:dept:{dept_id}`, TTL = $60\text{ giây}$.