# Ma trận chuyển trạng thái Ticket

## 1. Baseline transitions

| From | To | Actor | Điều kiện kích hoạt | FR liên quan |
| :--- | :--- | :--- | :--- | :--- |
| `NONE` | `NEW` | Student/System | Student gửi Ticket hợp lệ, hệ thống cấp Ticket ID. | FR-STU-02 |
| `NEW` | `IN_PROGRESS` | Staff | Staff claim hoặc Ticket được assign cho Staff. | FR-STA-04 |
| `IN_PROGRESS` | `WAITING_STUDENT` | Staff | Staff yêu cầu Student bổ sung thông tin/giấy tờ. | FR-STA-07 |
| `WAITING_STUDENT` | `IN_PROGRESS` | Student/System | Student gửi bổ sung hợp lệ. | FR-STU-04 |
| `IN_PROGRESS` | `NEW` | Staff | Ticket được transfer sang phòng ban/người phụ trách khác; assignee bị clear. | FR-STA-04 |
| `IN_PROGRESS` | `RESOLVED` | Staff | Staff ghi nhận kết quả xử lý. | FR-STA-08 |
| `RESOLVED` | `CLOSED` | Staff/System rule TBD | Ticket được đóng sau khi đã có kết quả xử lý. | FR-STA-09 |

## 2. Invalid transitions baseline

- Student không được tự chuyển Ticket sang `RESOLVED` hoặc `CLOSED`.
- Ticket không được chuyển thẳng từ `NEW` sang `RESOLVED` nếu chưa qua bước tiếp nhận/phân công.
- Ticket đã `CLOSED` không được cập nhật nội dung xử lý baseline; mọi thay đổi sau đó cần rule reopen riêng và hiện là Proposed/TBD.

## 3. Transitions không thuộc baseline

| Transition | Trạng thái | Lý do |
| :--- | :--- | :--- |
| `NEW` -> `CANCELLED` | Proposed/TBD | Proposal chưa nêu hủy Ticket. |
| `RESOLVED` -> `IN_PROGRESS` | Proposed/TBD | Proposal chưa nêu khiếu nại/mở lại. |
| Auto-close sau N ngày | Proposed/TBD | Proposal chưa chốt số ngày hoặc điều kiện. |
