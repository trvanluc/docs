# Mô Hình Dữ Liệu Ticket (Ticket Model)

## 1. Cấu Trúc Tổng Quan Của Ticket
Ticket là đối tượng dữ liệu trung tâm (Core Domain Entity) của hệ thống UniSupport. Mỗi Ticket phản ánh toàn bộ vòng đời tương tác giữa Sinh viên và Các phòng ban nghiệp vụ, bao gồm: Thông tin khởi tạo, Phân loại điều phối, File đính kèm, Lịch sử trao đổi/Bổ sung, Cảnh báo SLA, Kết quả giải quyết và Đánh giá chất lượng dịch vụ (CSAT).

## 2. Chi Tiết Danh Mục Trường Dữ Liệu (Data Dictionary)

| Nhóm thông tin | Tên trường (Database / API) | Kiểu dữ liệu | Bắt buộc | Ràng buộc Validation & Specs kỹ thuật |
| :--- | :--- | :--- | :--- | :--- |
| **Định danh** | ticket_id | String | Có | Primary Key. Mã hiển thị chuẩn TK-YYYYMMDD-XXXX (VD: TK-20261009-0001). Sinh tự động phía Server. Read-only. |
| | client_request_id | UUID v4 | Có | Mã định danh Idempotency Key gửi từ Client để chống trùng lặp dữ liệu khi mạng lag hoặc bấm gửi nhiều lần. |
| **Sinh viên gửi** | student_id | String / FK | Có | Foreign Key liên kết bảng Users. Lấy tự động từ Session Token của Sinh viên đang đăng nhập. Không cho phép giả mạo. |
| | student_name | String | Có | Snapshot họ tên sinh viên tại thời điểm tạo Ticket (Độ dài 2–100 ký tự). Read-only. |
| | student_email | String | Có | Snapshot Email công vụ của sinh viên @aurora.edu.vn. |
| **Nội dung** | category_id | String / FK | Có | Foreign Key liên kết bảng Categories. Lấy từ Dropdown danh mục khả dụng. |
| | title | String | Có | Tiêu đề Ticket. Độ dài: 10 – 150 ký tự. Tự động trim(). Không chấp nhận chuỗi chỉ chứa khoảng trắng. |
| | description | Text | Có | Nội dung mô tả chi tiết. Độ dài: 20 – 2.000 ký tự. Tự động trim(). Không chấp nhận chuỗi chỉ chứa khoảng trắng. |
| **Đính kèm** | attachments | JSONB / Array | Không | Danh sách đối tượng File đính kèm do Sinh viên tải lên lúc tạo Ticket. Tối đa 5 file/Ticket. |
| **Điều phối** | department_id | String / FK | Có | Foreign Key liên kết bảng Departments. Mặc định gán theo category_id, có thể cập nhật khi Chuyển phòng ban. |
| | assignee_id | String / FK | Không | Foreign Key liên kết Users (Nhân viên). Mặc định NULL khi mới tạo (NEW / TRANSFERRED). Gán ID khi Staff bấm Claim. |
| | priority | Enum | Có | Giá trị Enum: LOW, MEDIUM, HIGH, URGENT. Mặc định MEDIUM. Cán bộ có thể điều chỉnh khi Claim/Triage. |
| **Trạng thái & SLA** | status | Enum | Có | Giá trị Enum: NEW, IN_PROGRESS, NEED_MORE_INFO, TRANSFERRED, RESOLVED, CLOSED. Mặc định NEW. |
| | sla_target_at | DateTime | Có | Mốc thời gian hạn chót giải quyết theo SLA (Timestamp). Sinh tự động = created_at + 24 giờ làm việc. |
| | sla_status | Enum | Có | Giá trị Enum: ON_TRACK, WARNING, BREACHED. Sinh tự động dựa trên sla_target_at và status. |
| **Thời gian** | created_at | DateTime | Có | Timestamp thời điểm tạo Ticket. Server tự động sinh (CURRENT_TIMESTAMP). |
| | updated_at | DateTime | Có | Timestamp thời điểm có cập nhật mới nhất. Server tự động cập nhật khi record thay đổi. |
| | resolved_at | DateTime | Không | Timestamp thời điểm Nhân viên hoàn tất xử lý (status đổi sang RESOLVED). Mặc định NULL. |
| | closed_at | DateTime | Không | Timestamp thời điểm Ticket đóng hoàn toàn (status đổi sang CLOSED). Mặc định NULL. |
| **Kết quả xử lý** | resolution_note | Text | Không | Bắt buộc khi đóng/hoàn thành Ticket. Độ dài: 20 – 2.000 ký tự. Tự động trim(). |
| | resolution_attachments | JSONB / Array | Không | Danh sách đối tượng File đính kèm kết quả do Nhân viên gửi (Tối đa 3 file/Ticket). |
| **Đánh giá CSAT** | rating_score | Integer | Không | Điểm số đánh giá của sinh viên. Giá trị số nguyên từ 1 đến 5 (Mặc định NULL khi chưa đánh giá). |
| | rating_comment | Text | Không | Ý kiến nhận xét bổ sung của sinh viên khi đánh giá. Độ dài tối đa 500 ký tự. |
| | rated_at | DateTime | Không | Timestamp thời điểm sinh viên gửi đánh giá thành công. |

## 3. Cấu Trúc Chi Tiết Của File Đính Kèm (Attachment Object)
Mỗi phần tử trong danh sách attachments và resolution_attachments phải tuân thủ chính xác cấu trúc dữ liệu JSON sau:

| Tên thuộc tính | Kiểu dữ liệu | Bắt buộc | Mô tả & Ràng buộc |
| :--- | :--- | :--- | :--- |
| file_id | String | Có | Mã định danh duy nhất của file do Hệ thống Storage sinh ra (UUID v4). |
| file_name | String | Có | Tên gốc của file do người dùng upload (Ví dụ: Bang_Diem_Chuyen_Truong.pdf). Max 255 ký tự. |
| file_size | Integer | Có | Dung lượng file tính bằng Byte. Ràng buộc: file_size <= 5,242,880 (Tương đương 5MB). |
| file_type | String | Có | MIME Type thực tế kiểm tra phía Server (application/pdf, image/png, image/jpeg). |
| file_url | String | Có | Đường dẫn CDN/S3 an toàn để tải hoặc xem file. |
| uploaded_by | String / FK | Có | ID người dùng thực hiện upload file (user_id). |
| uploaded_at | DateTime | Có | Timestamp thời điểm tải file lên thành công. |

## 4. Cấu Trúc Nhật Ký Trao Đổi & Bổ Sung (Conversation & Activity Log)
Dữ liệu trao đổi bổ sung thông tin giữa Sinh viên và Nhân viên không lưu trực tiếp vào bảng Ticket chính mà lưu ở bảng phụ ticket_conversations (1-n) nối tới ticket_id:

| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả & Ràng buộc Validation |
| :--- | :--- | :--- | :--- |
| conversation_id | String / PK | Có | Mã Primary Key duy nhất của bản ghi nhật ký. |
| ticket_id | String / FK | Có | Foreign Key tham chiếu đến Ticket tương ứng. |
| sender_id | String / FK | Có | Foreign Key người gửi (Sinh viên hoặc Nhân viên). |
| sender_role | Enum | Có | Vai trò người gửi: STUDENT, STAFF, SYSTEM. |
| message_type | Enum | Có | Loại bản ghi: PUBLIC_MESSAGE (Hiển thị cho cả SV và Staff), INTERNAL_NOTE (Chỉ hiển thị nội bộ giữa Staff/Manager). |
| message_text | Text | Có | Nội dung trao đổi hoặc yêu cầu bổ sung. Độ dài: 10 – 1.000 ký tự. |
| attachments | JSONB / Array | Không | Cấu trúc mảng File đính kèm bổ sung (Tuân thủ Attachment Object ở Mục 3). |
| created_at | DateTime | Có | Timestamp thời điểm phát sinh tin nhắn/nhật ký. |

## 5. Các Ràng Buộc Dữ Liệu Ở Cấp CSDL (Database Constraints & Indexing)
Để đảm bảo hiệu năng query và tính toàn vẹn dữ liệu, Database phải cài đặt các chỉ mục và ràng buộc sau:

1. **Unique Constraints:**
   - `UNIQUE(ticket_id)`
   - `UNIQUE(client_request_id)` (Chống ghi nhận Ticket trùng lặp).

2. **Database Indexes:**
   - `INDEX(student_id, status)`: Tối ưu query danh sách Ticket cá nhân của Sinh viên.
   - `INDEX(department_id, status, assignee_id)`: Tối ưu query Queue công việc của Nhân viên phòng ban.
   - `INDEX(sla_status, status)`: Tối ưu query Dashboard Quản lý cảnh báo quá hạn.
   - `INDEX(created_at)`: Tối ưu cho việc lọc báo cáo theo mốc thời gian.

3. **Foreign Key Integrity:**
   - Ngoại trừ các trường Audit/Snapshot (`student_name`, `student_email`), toàn bộ các trường `_id` (`student_id`, `category_id`, `department_id`, `assignee_id`) đều có ràng buộc Foreign Key cứng, từ chối hành vi xóa mờ (Soft Delete required).