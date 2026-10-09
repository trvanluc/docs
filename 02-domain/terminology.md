# Thuật Ngữ Nghiệp Vụ & Chỉ Số Quản Trị (Terminology & Metrics Specification)

## 1. Tổng Quan
Tài liệu này định nghĩa chính xác danh mục thuật ngữ nghiệp vụ, mã trạng thái kỹ thuật và các chỉ số quản trị cốt lõi (KPIs/Metrics) được áp dụng đồng bộ trong hệ thống UniSupport. Việc chuẩn hóa này đảm bảo tính nhất quán giữa tài liệu PRD, thiết kế CSDL, định nghĩa API Response và giao diện hiển thị Dashboard.

## 2. Bảng Danh Mục Thuật Ngữ Cốt Lõi (Core Terminology)

| Thuật ngữ | Mã Kỹ Thuật / Field Name | Mô Tả & Giải Thích Kỹ Thuật Chi Tiết |
| :--- | :--- | :--- |
| **Ticket (Phiếu hỗ trợ)** | `ticket` | Đơn vị dữ liệu trung tâm (Core Entity) đại diện cho một giao dịch hỗ trợ do Sinh viên khởi tạo, chứa toàn bộ lịch sử biến động, file đính kèm, phản hồi và đánh giá. |
| **Ticket ID (Mã Ticket)** | `ticket_id` | Mã định danh duy nhất hiển thị dạng `TK-YYYYMMDD-XXXX` (VD: `TK-20261009-0001`). Sinh tự động, bất biến (Immutable), độ dài cố định $15\text{ ký tự}$. |
| **Idempotency Key** | `client_request_id` | Mã UUID v4 ngẫu nhiên do Client sinh ra khi mở Form tạo Ticket, gửi kèm trong Request Header để Server chống ghi nhận trùng dữ liệu do click đúp/mạng gián đoạn. |
| **Category (Nhóm vấn đề)** | `category_id` | Phân loại nghiệp vụ của yêu cầu (VD: Học phí, Đăng ký môn học, Giấy xác nhận). Mỗi Category liên kết mặc định với 01 Phòng ban (`department_id`). |
| **Priority (Độ ưu tiên)** | `priority` | Mức độ khẩn cấp xử lý Ticket. Enum gồm 4 giá trị: `LOW` (Thấp), `MEDIUM` (Trung bình - Mặc định), `HIGH` (Cao), `URGENT` (Khẩn cấp). |
| **Assignee (Người phụ trách)** | `assignee_id` | Mã định danh (`user_id`) của Nhân viên phòng ban trực tiếp chịu trách nhiệm thụ lý và giải quyết Ticket. Trả về `NULL` khi Ticket ở Queue chờ chung. |
| **Department (Phòng ban)** | `department_id` | Đơn vị nghiệp vụ thụ lý Ticket (VD: Phòng Đào tạo, Phòng Công tác Sinh viên, Phòng Tài chính). |
| **Attachment (File đính kèm)** | `attachments` | Tài liệu/hình ảnh minh chứng do Sinh viên hoặc Nhân viên tải lên. Ràng buộc: Định dạng `.pdf`, `.png`, `.jpg`, `.jpeg`; dung lượng $\le 5\text{MB/file}$; lưu ở thư mục Private. |
| **Conversation Log** | `ticket_conversations` | Bảng nhật ký ghi lại toàn bộ các câu trao đổi, lời nhắn yêu cầu bổ sung hồ sơ và phản hồi giữa Sinh viên và Nhân viên theo thứ tự thời gian (`created_at ASC`). |
| **Audit Trail (Nhật ký tra soát)** | `audit_logs` | Bảng nhật ký Append-Only ghi nhận vĩnh viễn các thao tác quản trị nhạy cảm (Tạo/khóa tài khoản, Phân quyền, Chuyển phòng ban) phục vụ kiểm toán an toàn thông tin. |
| **UAT (User Acceptance Testing)** | `uat` | Kiểm thử chấp nhận người dùng do Ban quản lý và Cán bộ Aurora University thực hiện trước khi nghiệm thu chính thức đưa hệ thống vào vận hành. |

## 3. Danh Mục Chỉ Số Quản Trị & SLA (Management Metrics & SLA Specifications)
Các chỉ số dưới đây được tính toán và hiển thị trực tiếp trên Phân hệ Quản lý (M03 - Management Dashboard):

| Tên Chỉ Số / Thuật Ngữ | Mã Chỉ Số | Công Thức Tính Toán & Specs Kỹ Thuật | Ý Nghĩa Quản Trị & Cảnh Báo |
| :--- | :--- | :--- | :--- |
| **SLA Target (Hạn chót SLA)** | `sla_target_at` | `created_at` + $24\text{ giờ làm việc}$ (Chỉ tính từ $08:00 - 17:00$ các ngày Thứ 2 đến Thứ 6, loại trừ T7, CN và Ngày lễ). | Mốc thời gian cam kết nhà trường phải hoàn tất giải quyết Ticket cho sinh viên. |
| **SLA On-Track (Trong hạn)** | `ON_TRACK` | Thời gian còn lại đến `sla_target_at` $> 25\%$ tổng quỹ thời gian SLA ($> 6\text{ giờ làm việc}$). | Ticket đang trong tiến độ xử lý an toàn. Hiển thị Badge màu xanh lá trên Dashboard. |
| **SLA Warning (Sắp quá hạn)** | `WARNING` | Thời gian còn lại đến `sla_target_at` $\le 25\%$ tổng quỹ thời gian SLA ($\le 6\text{ giờ làm việc}$). | Cảnh báo Nhân viên cần ưu tiên xử lý ngay. Hiển thị Badge màu vàng trên Dashboard. |
| **SLA Breached / Overdue** | `BREACHED` | Thời gian xử lý thực tế vượt quá `sla_target_at` nhưng Ticket chưa ở trạng thái `RESOLVED`/`CLOSED`. | Vi phạm cam kết dịch vụ. Dashboard Quản lý gom nhóm đẩy lên đầu trang kèm Badge màu đỏ. |
| **Avg Resolution Time** | `avg_resolution_time` | $\frac{\sum (\text{resolved\_at} - \text{created\_at})}{\text{Tổng số Ticket RESOLVED trong kỳ}}$ (Đơn vị: Giờ). | Đo lường năng suất và tốc độ giải quyết công việc trung bình của từng Phòng ban / Nhân viên. |
| **CSAT Score (Điểm Hài lòng)** | `csat_score` | $\frac{\text{Tổng số sao thu được}}{\text{Tổng số lượt đánh giá} \times 5} \times 100\%$ (Đơn vị: $\%$) | Chỉ số đánh giá chất lượng phục vụ của nhà trường dựa trên phản hồi của sinh viên ($1-5$ sao). |
| **Workload Distribution** | `workload_count` | `COUNT(ticket_id) WHERE assignee_id = {staff_id} AND status = 'IN_PROGRESS'` | Đo lường số lượng công việc thực tế đang gán cho từng Nhân viên để Quản lý điều phối cân bằng. |
| **Aggregation Cache** | `aggregation_cache` | Dữ liệu chỉ số Dashboard được tính toán trước và lưu tạm trên Redis (TTL: $30 - 60\text{ giây}$). | Tối ưu hiệu năng Query, tránh quá tải CSDL khi Quản lý truy cập Dashboard liên tục. |

## 4. Ma Trận Áp Dụng Thuật Ngữ Trong CSDL & APIs (Data Mapping)

| Thuật ngữ Nghiệp vụ | Bảng CSDL (Database Table) | Tên Trường CSDL (Column Name) | Enum Values / Data Type |
| :--- | :--- | :--- | :--- |
| **Mã Ticket** | `tickets` | `ticket_id` | `VARCHAR(15) PRIMARY KEY` |
| **Trạng thái Ticket** | `tickets` | `status` | `ENUM('NEW', 'IN_PROGRESS', 'NEED_MORE_INFO', 'TRANSFERRED', 'RESOLVED', 'CLOSED', 'REJECTED')` |
| **Độ ưu tiên** | `tickets` | `priority` | `ENUM('LOW', 'MEDIUM', 'HIGH', 'URGENT')` |
| **Trạng thái SLA** | `tickets` | `sla_status` | `ENUM('ON_TRACK', 'WARNING', 'BREACHED')` |
| **Điểm Đánh giá CSAT** | `tickets` | `rating_score` | `INTEGER` (Giá trị từ $1$ đến $5$) |
| **Vai trò Người dùng** | `users` | `role` | `ENUM('STUDENT', 'STAFF', 'MANAGER', 'ADMIN')` |
| **Trạng thái Tài khoản** | `users` | `status` | `ENUM('ACTIVE', 'INACTIVE')` |