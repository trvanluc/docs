# Specification - Notification Service dùng chung

Notification Service là năng lực dùng chung hỗ trợ các baseline workflow. PRD này chỉ mô tả requirement sản phẩm; cơ chế WebSocket/SSE/polling/event bus là quyết định Architecture.

## FR-NTF-01 - Ticket Update Notification

- **Status**: Derived
- **Actor**: System
- **Description / Goal**: Gửi thông báo trong hệ thống cho người liên quan khi Ticket có cập nhật quan trọng.
- **Events baseline/derived**:
  - Staff tiếp nhận/phân công Ticket -> Student được thông báo.
  - Staff yêu cầu bổ sung -> Student được thông báo.
  - Student bổ sung thông tin -> Staff phụ trách được thông báo.
  - Staff ghi nhận kết quả/đóng Ticket -> Student được thông báo.
  - Transfer Ticket -> phòng ban/người phụ trách mới được thông báo.
- **Inputs**: Event type, Ticket ID, recipient, message summary.
- **Output/Postcondition**: Notification được hiển thị trong tài khoản người nhận.
- **Acceptance Criteria**:
  - AC1: Notification chỉ gửi cho người liên quan.
  - AC2: Notification dẫn tới đúng Ticket.
  - AC3: Người thực hiện thao tác không bắt buộc nhận lại thông báo của chính thao tác đó.
- **Related FR**: FR-STU-05, FR-STA-04, FR-STA-07, FR-STA-08, FR-STA-09
- **Related Test Scenario**: TS-NTF-01-01, TS-NTF-01-02

## FR-NTF-P01 - Notification Center Enhancements

- **Status**: Proposed
- **Description / Goal**: Badge số lượng chưa đọc, đánh dấu đã đọc, xem tất cả notification.
- **Reason**: Hợp lý cho UI nhưng proposal chỉ yêu cầu thông báo/nhận cập nhật ở mức nghiệp vụ.

## FR-NTF-P02 - SLA Warning Notification

- **Status**: Proposed/TBD
- **Description / Goal**: Gửi cảnh báo khi Ticket sắp/quá hạn.
- **Reason**: Proposal có theo dõi sắp/quá hạn/quá hạn ở Management, nhưng rule cảnh báo, ngưỡng thời gian và recipient cần xác nhận cùng SLA.
