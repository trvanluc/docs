# Quy tắc nghiệp vụ cốt lõi

Tài liệu này chỉ mô tả business rules. Chi tiết kỹ thuật như JWT/session, secured endpoint, database constraint, timestamp format, append-only implementation hoặc encryption nằm trong `07-architecture`.

## 1. Attachment access

| ID | Rule | Trạng thái |
| :--- | :--- | :--- |
| **BR-FILE-01** | File đính kèm của Ticket chỉ được xem/tải bởi Student tạo Ticket, Staff trong phạm vi xử lý liên quan, hoặc Management có quyền tra soát. | Baseline |
| **BR-FILE-02** | Attachment được dùng cho ảnh/PDF theo proposal. Giới hạn dung lượng, số file và định dạng chi tiết cần xác nhận. | Baseline/TBD |

## 2. Ticket ownership và access

| ID | Rule | Trạng thái |
| :--- | :--- | :--- |
| **BR-ACC-01** | Student chỉ xem và thao tác với Ticket do chính mình tạo. | Baseline |
| **BR-ACC-02** | Staff chỉ xem/xử lý Ticket thuộc phòng ban/phạm vi được giao. | Baseline |
| **BR-ACC-03** | Management chỉ xem/quản trị dữ liệu theo quyền được cấp. | Baseline |

## 3. Transfer

| ID | Rule | Trạng thái |
| :--- | :--- | :--- |
| **BR-XFR-01** | Khi cần chuyển đơn vị xử lý, Ticket được cập nhật department/phạm vi xử lý mới, clear assignee hiện tại và quay về `NEW` để đơn vị mới tiếp nhận/phân công. | Baseline |
| **BR-XFR-02** | Lịch sử transfer phải lưu người thực hiện, đơn vị cũ, đơn vị mới và thời điểm. | Baseline |
| **BR-XFR-03** | Lý do chuyển là bắt buộc hay không, và độ dài tối thiểu nếu có, là TBD. | TBD |

## 4. Supplement request

| ID | Rule | Trạng thái |
| :--- | :--- | :--- |
| **BR-SUP-01** | Khi Staff yêu cầu bổ sung, Ticket chuyển từ `IN_PROGRESS` sang `WAITING_STUDENT`. | Baseline |
| **BR-SUP-02** | Khi Student bổ sung hợp lệ, Ticket chuyển từ `WAITING_STUDENT` về `IN_PROGRESS`. | Baseline |
| **BR-SUP-03** | Cách tính SLA trong thời gian `WAITING_STUDENT` là TBD. | TBD |

## 5. Resolution, close và rating

| ID | Rule | Trạng thái |
| :--- | :--- | :--- |
| **BR-RES-01** | Staff phải ghi nhận kết quả xử lý trước khi Ticket chuyển sang `RESOLVED`. | Baseline |
| **BR-CLS-01** | Ticket chỉ được đóng sau khi đã có kết quả xử lý. | Baseline |
| **BR-RAT-01** | Student chỉ đánh giá mức độ hài lòng sau khi Ticket hoàn tất/đóng. | Baseline |
| **BR-RAT-02** | Thang điểm 1-5 sao và rule mỗi Ticket chỉ được đánh giá một lần là Proposed cho đến khi được xác nhận. | Proposed |
| **BR-RAT-03** | Thời hạn đánh giá sau khi hoàn tất là TBD. | TBD |

## 6. History / audit

| ID | Rule | Trạng thái |
| :--- | :--- | :--- |
| **BR-HIS-01** | Các thao tác quan trọng như tạo Ticket, claim/assign, transfer, yêu cầu bổ sung, bổ sung, ghi nhận kết quả, đóng Ticket và thay đổi account/permission phải được lưu lịch sử. | Baseline |
| **BR-HIS-02** | Mức độ bất biến log, retention, IP/device metadata và cơ chế lưu cụ thể thuộc Architecture/NFR và cần xác nhận nếu muốn dùng làm cam kết nghiệm thu. | Derived/TBD |
