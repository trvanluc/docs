# Ma Trận Chuyển Đổi Trạng Thái Ticket (State Transition Matrix)

## 1. Bảng Ma Trận Chuyển Trạng Thái (State Transition Table)

Bảng dưới đây quy định các trạng thái hợp lệ có thể chuyển đổi, Tác nhân thực hiện (Actor) và Điều kiện kích hoạt tương ứng:

| Trạng Thái Hiện Tại (From) | Trạng Thái Đích (To) | Tác Nhân (Actor) | Điều Kiện & Kịch Bản Kích Hoạt |
| :--- | :--- | :--- | :--- |
| **NONE** | `NEW` | Sinh viên | Sinh viên gửi form tạo Ticket thành công. |
| `NEW` | `IN_PROGRESS` | Nhân viên | Nhân viên nhấn **Claim** (Tiếp nhận) hoặc Trưởng phòng **Assign** (Phân công). |
| `NEW` | `CANCELLED` | Sinh viên / System | Sinh viên chủ động hủy yêu cầu khi chưa ai tiếp nhận, hoặc hệ thống hủy do phát hiện vi phạm. |
| `IN_PROGRESS` | `WAITING_STUDENT` | Nhân viên | Nhân viên gửi nội dung **Yêu cầu bổ sung thông tin/giấy tờ**. |
| `WAITING_STUDENT` | `IN_PROGRESS` | Sinh viên | Sinh viên đăng tải file hoặc phản hồi câu trả lời bổ sung. |
| IN_PROGRESS | NEW | Nhân viên | Nhân viên thực hiện Chuyển phòng ban (Transfer) -> Trạng thái chuyển về NEW (hoặc FORWARDED), cập nhật department_id mới và xóa assigned_staff_id. |
| `IN_PROGRESS` | `RESOLVED` | Nhân viên | Nhân viên cập nhật nội dung giải quyết thành công và chọn **Hoàn tất**. |
| `RESOLVED` | `IN_PROGRESS` | Sinh viên | Sinh viên phản hồi chưa hài lòng/khiếu nại kết quả trong thời hạn cho phép. |
| `RESOLVED` | `CLOSED` | Sinh viên | Sinh viên xác nhận kết quả và thực hiện **Đánh giá hài lòng (CSAT)**. |
| `RESOLVED` | `CLOSED` | System | Hệ thống tự động đóng sau **03 ngày làm việc** kể từ khi ở trạng thái `RESOLVED`. |
| `CLOSED` | *Không đổi* | N/A | **Trạng thái kết thúc (Terminal State)**. Không cho phép bất kỳ chuyển đổi nào khác. |
| `CANCELLED` | *Không đổi* | N/A | **Trạng thái kết thúc (Terminal State)**. Không cho phép bất kỳ chuyển đổi nào khác. |

---

## 2. Quy Tắc Chặn Chuyển Trạng Thái Bất Hợp Lệ (Invalid Transition Rules)

1. **Không cho phép chuyển từ `NEW` thẳng sang `RESOLVED` hoặc `CLOSED`**: Bắt buộc phải qua bước tiếp nhận (`IN_PROGRESS`) để đảm bảo đúng quy trình phân công trách nhiệm.
2. **Không thể chỉnh sửa Ticket khi ở trạng thái `CLOSED` hoặc `CANCELLED`**: Mọi thao tác gửi phản hồi, upload file đính kèm mới đều bị vô hiệu hóa hoàn toàn.
3. **Sinh viên không được tự chuyển trạng thái sang `RESOLVED`**: Chỉ có Nhân viên phụ trách mới có quyền ghi nhận kết quả xử lý.