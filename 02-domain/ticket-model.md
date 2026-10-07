# Mô Hình Dữ Liệu Ticket (Ticket Model)

## 1. Cấu Trúc Tổng Quan Của Ticket
Ticket là đối tượng dữ liệu trung tâm của hệ thống UniSupport[cite: 1]. Cấu trúc thông tin của một Ticket bao gồm các nhóm trường dữ liệu sau[cite: 1]:

---

## 2. Chi Tiết Các Trường Dữ Liệu (Attributes)

| Nhóm thông tin | Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
| :--- | :--- | :--- | :---: | :--- |
| **Định danh** | `ticket_id` | String | Có | Mã Ticket duy nhất (ví dụ: `TK-20261007-001`)[cite: 1] |
| **Tác giả** | `student_id` | String/FK | Có | ID tài khoản sinh viên gửi yêu cầu[cite: 1] |
| | `student_name` | String | Có | Họ tên sinh viên gửi yêu cầu |
| **Nội dung** | `category_id` | String/FK | Có | Nhóm vấn đề được chọn[cite: 1] |
| | `title` | String | Có | Tiêu đề ngắn gọn của yêu cầu |
| | `description` | Text | Có | Nội dung mô tả chi tiết vấn đề[cite: 1] |
| | `attachments` | List<File> | Không | Danh sách file đính kèm (Ảnh/PDF, tối đa 5MB/file)[cite: 1] |
| **Điều phối** | `department_id` | String/FK | Có | Phòng ban phụ trách thụ lý[cite: 1] |
| | `assignee_id` | String/FK | Không | ID nhân viên trực tiếp xử lý[cite: 1] |
| | `priority` | Enum | Có | Độ ưu tiên: `LOW`, `MEDIUM`, `HIGH`, `URGENT`[cite: 1] |
| **Trạng thái** | `status` | Enum | Có | Trạng thái Ticket (xem file `state-transition.md`)[cite: 1] |
| **Thời gian** | `created_at` | DateTime | Có | Thời điểm khởi tạo Ticket |
| | `updated_at` | DateTime | Có | Thời điểm cập nhật gần nhất |
| | `closed_at` | DateTime | Không | Thời điểm hoàn thành/đóng Ticket |
| **Kết quả & Đánh giá**| `resolution_note` | Text | Không | Nội dung ghi nhận kết quả xử lý của nhân viên[cite: 1] |
| | `rating_score` | Integer (1-5)| Không | Mức độ hài lòng của sinh viên (sau khi đóng Ticket)[cite: 1] |
| | `rating_comment` | Text | Không | Ý kiến phản hồi bổ sung của sinh viên[cite: 1] |