# 04 - Quy Trình Nghiệp Vụ (Workflows)

Thư mục `04-workflows` mô tả các **luồng nghiệp vụ xuyên chức năng hoặc xuyên phân hệ** của UniSupport bằng sơ đồ Mermaid. Workflow không tạo thêm chức năng mới; mọi bước trong sơ đồ phải truy xuất được về Functional Requirements và Business Rules đã xác lập trong M01, M02, M03 và `02-domain`.

## 1. Danh Sách Workflow

| Mã | Quy trình | Vai trò tham gia chính | Phạm vi |
| :--- | :--- | :--- | :--- |
| **[WF-01](./WF-01-submit-support-request.md)** | Gửi yêu cầu hỗ trợ | Sinh viên | Tạo Ticket, xác định phòng ban từ Nhóm vấn đề và nhận mã Ticket. |
| **[WF-02](./WF-02-claim-and-triage.md)** | Tiếp nhận, phân loại và phân công | Nhân viên | Tiếp nhận Ticket mới, kiểm tra Nhóm vấn đề, mức độ ưu tiên và người phụ trách. |
| **[WF-03](./WF-03-request-supplement.md)** | Yêu cầu và tiếp nhận bổ sung | Nhân viên, Sinh viên | Chuyển `IN_PROGRESS ↔ WAITING_STUDENT` và tạm dừng/tiếp tục thời hạn xử lý. |
| **[WF-04](./WF-04-transfer-department.md)** | Chuyển xử lý sang phòng ban khác | Nhân viên, Quản lý có quyền | Chọn Nhóm vấn đề đích, xác định phòng ban đích và gỡ người phụ trách cũ. |
| **[WF-05](./WF-05-complete-and-resolve.md)** | Ghi nhận kết quả | Nhân viên, Sinh viên | Ghi nhận kết quả và chuyển `IN_PROGRESS → RESOLVED`. |
| **[WF-06](./WF-06-close-and-rate.md)** | Phản hồi kết quả, mở lại, đóng và đánh giá | Sinh viên, Nhân viên, Hệ thống | Xử lý `RESOLVED → IN_PROGRESS/CLOSED` và CSAT sau khi Ticket đóng. |
| **[WF-07](./WF-07-escalation.md)** | Chuyển cấp hỗ trợ | Nhân viên, Quản lý | Gửi yêu cầu hỗ trợ nội bộ tới Quản lý mà không thay đổi trách nhiệm xử lý Ticket. |

## 2. Nguyên Tắc Sử Dụng

- Mỗi file Workflow sử dụng **Mermaid flowchart** làm nội dung chính.
- Sơ đồ thể hiện **luồng nghiệp vụ**, không phải mô hình kỹ thuật hoặc sơ đồ API.
- Bộ trạng thái Ticket chỉ gồm `NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`.
- Chuyển xử lý (Transfer) và chuyển cấp hỗ trợ (Escalation) là hành động nghiệp vụ, không phải trạng thái.
- Điều kiện chi tiết về dữ liệu, quyền, thời hạn, file, mở lại và CSAT vẫn tuân theo PRD và Domain.
- Không đưa API, HTTP status, JWT, cấu trúc database hoặc cơ chế kỹ thuật vào Workflow.

## 3. Cấu Trúc Mỗi Workflow

Mỗi file Workflow gồm:
1. Mục đích và phạm vi.
2. Sơ đồ Mermaid.
3. Ghi chú nghiệp vụ quan trọng.
4. Tài liệu tham chiếu.
