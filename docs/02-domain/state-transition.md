# Ma Trận Chuyển Đổi Trạng Thái Ticket (State Transition Matrix)

Tài liệu này quy định các chuyển đổi trạng thái hợp lệ của Ticket trong **UniSupport**. Mọi thay đổi trạng thái phải tuân thủ vòng đời Ticket và được ghi nhận trong lịch sử xử lý.

## 1. Ma Trận Chuyển Trạng Thái

| Trạng thái hiện tại | Trạng thái đích | Tác nhân | Điều kiện chuyển trạng thái |
| :--- | :--- | :--- | :--- |
| Chưa tồn tại | `NEW` | Sinh viên / Hệ thống | Sinh viên gửi yêu cầu hợp lệ và hệ thống tạo Ticket thành công. |
| `NEW` | `IN_PROGRESS` | Người dùng có quyền xử lý | Ticket được tiếp nhận hoặc phân công cho phạm vi xử lý phù hợp. |
| `IN_PROGRESS` | `WAITING_STUDENT` | Người dùng có quyền xử lý | Cần sinh viên bổ sung thông tin hoặc tài liệu trước khi tiếp tục xử lý. |
| `WAITING_STUDENT` | `IN_PROGRESS` | Sinh viên / Hệ thống | Sinh viên gửi bổ sung hợp lệ và Ticket sẵn sàng tiếp tục xử lý. |
| `IN_PROGRESS` | `RESOLVED` | Người dùng có quyền xử lý | Kết quả xử lý đã được ghi nhận đầy đủ cho Ticket. |
| `RESOLVED` | `IN_PROGRESS` | Sinh viên / Hệ thống | Sinh viên phản hồi rằng vấn đề chưa được giải quyết trong thời hạn và đáp ứng điều kiện mở lại. |
| `RESOLVED` | `CLOSED` | Sinh viên / Hệ thống | Sinh viên chấp nhận kết quả hoặc hết thời hạn phản hồi theo quy định. |
| `CLOSED` | Không chuyển tiếp | Hệ thống | Ticket đã kết thúc vòng đời xử lý. |

---

## 2. Hành Động Không Làm Thay Đổi Trạng Thái

Một số hành động nghiệp vụ có thể làm thay đổi trách nhiệm xử lý hoặc thông tin của Ticket nhưng không nhất thiết tạo ra trạng thái mới.

| Hành động | Ảnh hưởng đến trạng thái | Quy tắc |
| :--- | :--- | :--- |
| **Phân công lại** | Giữ nguyên trạng thái hiện tại | Thay đổi người phụ trách và ghi nhận lịch sử. |
| **Chuyển xử lý (Transfer)** | Giữ nguyên trạng thái nghiệp vụ hiện tại phù hợp | Cập nhật Nhóm vấn đề và phòng ban theo cấu hình, gỡ người phụ trách hiện tại và bảo toàn lịch sử trước đó. |
| **Escalation** | Giữ nguyên trạng thái hiện tại | Gửi yêu cầu hỗ trợ tới Quản lý phù hợp; không tự thay đổi Nhóm vấn đề, phòng ban hoặc người phụ trách và phải ghi nhận sự kiện chuyển cấp. |
| **Thay đổi mức độ ưu tiên** | Giữ nguyên trạng thái hiện tại | Cập nhật mức độ ưu tiên theo quyền và quy tắc nghiệp vụ. |
| **Cập nhật thời hạn xử lý** | Giữ nguyên trạng thái hiện tại | Thời hạn mới phải tuân thủ quy tắc nghiệp vụ và được ghi nhận trong lịch sử. |

---

## 3. Quy Tắc Chuyển Trạng Thái

1. Ticket chỉ được chuyển giữa các trạng thái được quy định trong ma trận này.
2. `NEW` không được chuyển trực tiếp sang `RESOLVED` hoặc `CLOSED`; Ticket phải được tiếp nhận và đi vào quá trình xử lý trước khi có thể hoàn tất.
3. `WAITING_STUDENT` chỉ quay lại `IN_PROGRESS` sau khi sinh viên đã cung cấp thông tin hoặc tài liệu bổ sung hợp lệ.
4. Chỉ người dùng có quyền xử lý Ticket mới được ghi nhận kết quả và chuyển Ticket từ `IN_PROGRESS` sang `RESOLVED`.
5. Mở lại Ticket được thực hiện từ `RESOLVED` về `IN_PROGRESS`, không thực hiện từ `CLOSED`.
6. `CLOSED` là trạng thái kết thúc vòng đời xử lý. Trường hợp phát sinh nhu cầu hỗ trợ mới sau khi Ticket đã đóng được xử lý theo quy tắc nghiệp vụ tương ứng.
7. Mọi chuyển đổi trạng thái phải ghi nhận trạng thái trước, trạng thái sau, tác nhân thực hiện và thời điểm phát sinh vào lịch sử Ticket.

---

## 4. Quan Hệ Với Các Quy Tắc Nghiệp Vụ

Các điều kiện chi tiết liên quan đến thời hạn phản hồi, mở lại Ticket, thời hạn xử lý, yêu cầu bổ sung và đánh giá mức độ hài lòng được quy định tại `business-rules.md`.

Ma trận này chỉ xác định các chuyển đổi trạng thái hợp lệ; các điều kiện chi tiết để cho phép một chuyển đổi được áp dụng theo các quy tắc nghiệp vụ tương ứng.
