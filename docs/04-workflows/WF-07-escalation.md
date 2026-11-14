# WF-07 - Chuyển Cấp Hỗ Trợ (Escalation)

## 1. Mục Đích Và Phạm Vi

Mô tả cách nhân viên yêu cầu hỗ trợ từ Quản lý khi Ticket vượt thẩm quyền hiện tại, cần hỗ trợ điều phối hoặc có nguy cơ không đáp ứng thời hạn. Escalation không thay thế Transfer.

## 2. Sơ Đồ Nghiệp Vụ

```mermaid
flowchart TD
    A[Ticket NEW / IN_PROGRESS / WAITING_STUDENT] --> B[Nhân viên chọn Chuyển cấp hỗ trợ]
    B --> C[Hệ thống hiển thị Quản lý hợp lệ]
    C --> D[Chọn người nhận và nhập lý do]
    D --> E{Quyền, người nhận và lý do hợp lệ?}
    E -->|Không| F[Từ chối thao tác]
    E -->|Có| G[Ghi nhận người gửi, người nhận, lý do và thời điểm]
    G --> H[Giữ nguyên Nhóm vấn đề]
    H --> I[Giữ nguyên phòng ban]
    I --> J[Giữ nguyên người phụ trách]
    J --> K[Giữ nguyên trạng thái Ticket]
    K --> L[Thông báo Quản lý nhận Escalation]
    L --> M[Thông báo người phụ trách hiện tại]
    M --> N[Người phụ trách tiếp tục xử lý]
```

## 3. Ghi Chú Nghiệp Vụ

- Escalation không đổi Category, phòng ban, assignee hoặc trạng thái.
- Sinh viên không nhận thông báo chỉ vì Escalation nội bộ.
- Nếu cần đổi phòng ban, sử dụng WF-04.
- Nếu cần đổi người phụ trách trong cùng phòng ban, sử dụng luồng phân công lại của M02.
- Lý do Escalation từ 10 đến 1.000 ký tự.

## 4. Tài Liệu Tham Chiếu

- M02: `FR-STF-05`.
- M03: phạm vi Quản lý và quyền liên quan.
- Domain: `BR-OWN-03`.
