# Mô Hình Dữ Liệu Ticket (Ticket Data Model)

## Phạm vi đọc tài liệu

Các bảng kiểu dữ liệu/tên trường bên dưới là mô hình kỹ thuật của bản hiện tại, được giữ nguyên trong lần sửa PRD. Chúng còn có chỗ lệch PRD (WAITING_STUDENT/CANCELLED, 10MB, giới hạn tiêu đề 255). Giới hạn **người dùng nhập liệu** lấy theo FR-STU-02/03: tiêu đề 10–150, tệp 5MB và trạng thái cần bổ sung NEED_MORE_INFO. Bảng này không được dùng để tự mở rộng giới hạn hoặc thêm trạng thái/chức năng; xem [ghi nhận sai lệch](../08-project/prd-review-notes.md).

## 1. Thực Thể Cốt Lõi: Ticket (Ticket Entity)

Ticket là thực thể chính trong hệ thống UniSupport. Dưới đây là cấu trúc thuộc tính chi tiết của thực thể Ticket:

| Tên Thuộc Tính (Field) | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả & Quy Tắc Dữ Liệu |
| :--- | :--- | :---: | :--- |
| `id` | BigInt / UUID | Có | Khóa chính tự tăng hoặc chuỗi UUID định danh đằng sau database. |
| `ticket_code` | String(20) | Có | Mã Ticket hiển thị cho người dùng (Format: `TK-YYYYMMDD-XXXX`). Mã này là DUY NHẤT. |
| `title` | String(255) | Có | Tiêu đề tóm tắt yêu cầu do sinh viên nhập (Tối đa 255 ký tự). |
| `description` | Text | Có | Nội dung mô tả chi tiết vấn đề do sinh viên cung cấp. |
| `category_id` | Integer | Có | Khóa ngoại trỏ tới Bảng Nhóm vấn đề (Category). |
| `department_id` | Integer | Có | Khóa ngoại trỏ tới Bảng Phòng ban đang thụ lý. |
| `created_by_student_id` | BigInt | Có | Khóa ngoại trỏ tới Bảng Sinh viên (người tạo). |
| `assigned_staff_id` | BigInt | Không | Khóa ngoại trỏ tới Bảng Nhân viên đang thụ lý (`NULL` nếu chưa có người Claim/Assign). |
| `status` | Enum | Có | Trạng thái hiện tại: `NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`, `CANCELLED`. |
| `priority` | Enum | Có | Mức độ ưu tiên: `LOW`, `MEDIUM`, `HIGH`, `URGENT` (Mặc định: `MEDIUM`). |
| `resolution_note` | Text | Không | Nội dung ghi nhận kết quả giải quyết do Nhân viên nhập khi hoàn thành. |
| `created_at` | Timestamp | Có | Thời điểm khởi tạo Ticket. |
| `updated_at` | Timestamp | Có | Thời điểm cập nhật dữ liệu gần nhất. |
| `first_responded_at` | Timestamp | Không | Thời điểm nhân viên phản hồi đầu tiên. |
| `resolved_at` | Timestamp | Không | Thời điểm nhân viên đánh dấu Hoàn thành (`RESOLVED`). |
| `closed_at` | Timestamp | Không | Thời điểm Ticket chuyển sang Đóng hoàn toàn (`CLOSED`). |
| `sla_due_at` | Timestamp | Không | Thời hạn cam kết xử lý dựa trên độ ưu tiên và quy định phòng ban. |

---

## 2. Thực Thể Liên Quan 1: File Đính Kèm (Ticket Attachment Entity)

Lưu trữ thông tin các tệp tin đính kèm (Hình ảnh, tài liệu PDF) do Sinh viên hoặc Nhân viên tải lên.

| Tên Thuộc Tính | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :---: | :--- |
| `id` | BigInt | Có | Khóa chính tệp đính kèm. |
| `ticket_id` | BigInt | Có | Khóa ngoại liên kết với Ticket. |
| `file_name` | String(255) | Có | Tên gốc của file do người dùng tải lên (Ví dụ: `BangDiem_Ky1.pdf`). |
| `file_path` | String(500) | Có | Đường dẫn lưu trữ file trên hệ thống/bộ nhớ bảo mật. |
| `file_size` | Integer | Có | Dung lượng file (tính bằng Bytes, tối đa 10MB = 10,485,760 Bytes). |
| `mime_type` | String(100) | Có | Định dạng file (`application/pdf`, `image/jpeg`, `image/png`). |
| `uploaded_by_user_id` | BigInt | Có | ID người dùng thực hiện upload file. |
| `created_at` | Timestamp | Có | Thời điểm upload. |

---

## 3. Thực Thể Liên Quan 2: Nhật Ký Trao Đổi / Tra Soát (Ticket Comment & Activity Log)

Lưu vết toàn bộ tiến trình trao đổi giữa Sinh viên và Nhân viên, cũng như các sự kiện hệ thống.

| Tên Thuộc Tính | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :---: | :--- |
| `id` | BigInt | Có | Khóa chính dòng log. |
| `ticket_id` | BigInt | Có | Khóa ngoại trỏ tới Ticket. |
| `sender_type` | Enum | Có | Loại người gửi: `STUDENT`, `STAFF`, `SYSTEM`. |
| `sender_id` | BigInt | Có | ID tài khoản thực hiện thao tác. |
| `content` | Text | Có | Nội dung tin nhắn, yêu cầu bổ sung hoặc mô tả thay đổi trạng thái tự động. |
| `is_internal_note` | Boolean | Có | `TRUE`: Ghi chú nội bộ (chỉ nhân viên thấy); `FALSE`: Phản hồi công khai (sinh viên nhìn thấy). |
| `created_at` | Timestamp | Có | Thời điểm ghi nhận log. |

---

## 4. Thực Thể Liên Quan 3: Đánh Giá Hài Lòng (Ticket Rating Entity)

Lưu trữ đánh giá của sinh viên sau khi Ticket được xử lý xong.

| Tên Thuộc Tính | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :---: | :--- |
| `id` | BigInt | Có | Khóa chính bản ghi đánh giá. |
| `ticket_id` | BigInt | Có | Khóa ngoại trỏ tới Ticket (Mỗi Ticket chỉ có tối đa 01 Rating). |
| `score` | Integer | Có | Điểm số đánh giá từ `1` đến `5` sao. |
| `comment` | Text | Không | Phản hồi/góp ý chi tiết của sinh viên. |
| `created_at` | Timestamp | Có | Thời điểm sinh viên thực hiện đánh giá. |
