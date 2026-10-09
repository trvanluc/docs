# Ma Trận Chuyển Đổi Trạng Thái Ticket (State Transition Matrix)

## 1. Danh Sách Mã Trạng Thái (State Definitions)

| Mã trạng thái (`status`) | Tên hiển thị (VI) | Mô tả chi tiết & Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- |
| `NEW` | Mới tạo | Ticket vừa tạo thành công, đang nằm trong Queue chung của Phòng ban, chưa có cá nhân Nhân viên tiếp nhận. |
| `IN_PROGRESS` | Đang xử lý | Ticket đã có Nhân viên phụ trách (`assignee_id != NULL`) và đang trong tiến trình giải quyết nghiệp vụ. |
| `NEED_MORE_INFO` | Cần bổ sung | Nhân viên tạm dừng xử lý để chờ Sinh viên cung cấp thêm thông tin hoặc giấy tờ còn thiếu. |
| `TRANSFERRED` | Đã chuyển giao | Ticket đã được điều chuyển sang Phòng ban khác. Đang nằm trong Queue chờ của Phòng ban mới (`assignee_id = NULL`). |
| `REJECTED` | Từ chối xử lý | Ticket bị từ chối do nội dung vi phạm, spam hoặc không đúng quy định nhà trường. Đây là trạng thái kết thúc (Terminal State). |
| `RESOLVED` | Đã giải quyết | Nhân viên đã xử lý xong nghiệp vụ và gửi kết quả cho Sinh viên. Chờ Sinh viên nghiệm thu/đánh giá. |
| `CLOSED` | Đã đóng hoàn tất | Ticket đã kết thúc toàn bộ vòng đời (Đã được đánh giá hoặc tự động đóng sau 3 ngày). Không thể chỉnh sửa hay thay đổi trạng thái. |

---

## 2. Bảng Ma Trận Chuyển Đổi Trạng Thái (State Transition Table)

Các đường chuyển trạng thái **KHÔNG NẰM TRONG BẢNG DƯỚI ĐÂY** đều bị hệ thống cấm (trả về mã lỗi `400 INVALID_TICKET_STATE`).

| Trạng thái hiện tại | Trạng thái chuyển tới | Vai trò thực hiện | Điều kiện kích hoạt & Validation Rules | Hành động phụ kèm theo (Side Effects) |
| :--- | :--- | :--- | :--- | :--- |
| `NEW` | `IN_PROGRESS` | STAFF, MANAGER | Nhân viên bấm Tiếp nhận xử lý. Áp dụng Optimistic Locking chống tranh chấp. | - Gán `assignee_id = current_user_id`<br>- Cập nhật `priority` (nếu có chỉnh sửa). |
| `NEW` | `TRANSFERRED` | STAFF, MANAGER | Bắt buộc nhập lý do chuyển tiếp (10 - 500 ký tự). Chọn phòng ban mới khác phòng ban hiện tại. | - Đổi `department_id = target_department_id`<br>- Gán `assignee_id = NULL`<br>- Ghi vết Audit Log. |
| `NEW` | `REJECTED` | STAFF, MANAGER | Bắt buộc nhập lý do từ chối (10 - 500 ký tự). | - Gửi thông báo từ chối kèm lý do cho Sinh viên.<br>- Cập nhật `closed_at = CURRENT_TIMESTAMP`. |
| `IN_PROGRESS` | `NEED_MORE_INFO` | STAFF (Assignee) | Bắt buộc nhập nội dung yêu cầu bổ sung (10 - 1000 ký tự). | - Lưu tin nhắn vào Conversation log.<br>- Gửi Notification cho Sinh viên. |
| `IN_PROGRESS` | `TRANSFERRED` | STAFF (Assignee) | Bắt buộc nhập lý do chuyển tiếp (10 - 500 ký tự). | - Đổi `department_id = target_department_id`<br>- Gán `assignee_id = NULL`<br>- Ghi vết Audit Log. |
| `IN_PROGRESS` | `RESOLVED` | STAFF (Assignee) | Bắt buộc nhập `resolution_note` (20 - 2000 ký tự). | - Cập nhật `resolved_at = CURRENT_TIMESTAMP`<br>- Gửi thông báo kết quả cho Sinh viên. |
| `NEED_MORE_INFO` | `IN_PROGRESS` | STUDENT (Owner) | Sinh viên gửi đính kèm/lời nhắn bổ sung thành công. | - Lưu file/tin nhắn vào Conversation log.<br>- Phát thông báo cho Nhân viên phụ trách. |
| `TRANSFERRED` | `IN_PROGRESS` | STAFF (PB mới) | Nhân viên phòng ban mới bấm Tiếp nhận xử lý. | - Gán `assignee_id = current_user_id`. |
| `TRANSFERRED` | `REJECTED` | STAFF (PB mới) | Nhân viên phòng ban mới kiểm tra và từ chối. Bắt buộc nhập lý do từ chối. | - Cập nhật `closed_at = CURRENT_TIMESTAMP`. |
| `RESOLVED` | `CLOSED` | STUDENT (Owner) | Sinh viên gửi Đánh giá hài lòng (Rating 1-5 sao). | - Lưu `rating_score`, `rating_comment`, `rated_at`.<br>- Cập nhật `closed_at = CURRENT_TIMESTAMP`. |
| `RESOLVED` | `CLOSED` | SYSTEM (Cronjob) | Ticket ở trạng thái `RESOLVED` quá 03 ngày làm việc không có tương tác mới. | - Cập nhật `closed_at = CURRENT_TIMESTAMP`. |

---

## 3. Quy Tắc Bảo Mật & Phân Quyền Theo Trạng Thái (State-based Security Matrix)

| Trạng thái Ticket | Quyền của Sinh viên (Owner) | Quyền của Nhân viên (Assignee) | Quyền của Quản lý / Admin |
| :--- | :--- | :--- | :--- |
| `NEW` | Xem chi tiết. KHÔNG được chỉnh sửa nội dung. | Xem chi tiết, Claim, Transfer, Reject. | Xem chi tiết, Phân công trực tiếp cho Staff. |
| `IN_PROGRESS` | Xem tiến độ, xem tên Nhân viên phụ trách. | Xem chi tiết, Yêu cầu bổ sung, Transfer, Complete. | Xem chi tiết, Thu hồi Ticket cấp lại cho Staff khác. |
| `NEED_MORE_INFO` | Xem yêu cầu bổ sung, Được upload file / nhắn tin bổ sung. | Xem tiến độ, Chờ sinh viên phản hồi. | Xem chi tiết. |
| `TRANSFERRED` | Xem lịch sử chuyển phòng ban. | **Staff cũ:** Read-only.<br>**Staff phòng ban mới:** Xem & Claim. | Xem chi tiết. |
| `REJECTED` | Xem lý do bị từ chối (Read-only). | Read-only. | Read-only. |
| `RESOLVED` | Xem kết quả giải quyết, Được thực hiện Đánh giá (Rating). | Read-only. | Read-only. |
| `CLOSED` | Xem lại toàn bộ lịch sử & đánh giá đã gửi (Read-only). | Read-only. | Read-only. |

---

## 4. Quy Tắc Chặn Chuyển Trạng Thái Bất Hợp Lệ (Invalid Transition Rules)

1. **Không cho phép chuyển từ `NEW` thẳng sang `RESOLVED` hoặc `CLOSED`**: Bắt buộc phải qua bước tiếp nhận (`IN_PROGRESS`) để đảm bảo đúng quy trình phân công trách nhiệm.
2. **Không thể chỉnh sửa Ticket khi ở trạng thái `CLOSED`, `REJECTED`**: Đây là các Terminal State. Mọi thao tác thay đổi trạng thái đều bị vô hiệu hóa.
3. **Sinh viên không được tự chuyển trạng thái sang `RESOLVED`**: Chỉ có Nhân viên phụ trách mới có quyền ghi nhận kết quả xử lý.
4. **Không hỗ trợ mở lại Ticket đã `CLOSED`**: Nếu có vấn đề phát sinh sau khi đóng, sinh viên tạo Ticket mới.
5. **Mọi chuyển đổi trạng thái không hợp lệ đều trả về**: `400 Bad Request` với Error Code `INVALID_TICKET_STATE`.