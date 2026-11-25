# PRJ-05 - Vấn Đề Chờ Làm Rõ

Các quy tắc nghiệp vụ cốt lõi về Ticket, Category, Transfer, Escalation, reopen, CSAT, tài khoản và quyền được quản lý tại Product, Domain và PRD.

## 1. Nguyên Tắc

Chỉ ghi tại đây các vấn đề chưa được tài liệu hiện hành xác định và có khả năng ảnh hưởng đến triển khai.

## 2. Danh Sách Hiện Tại

| ID | Vấn đề | Ảnh hưởng | Trạng thái |
| :--- | :--- | :--- | :--- |
| OQ-01 | Thông số kỹ thuật cụ thể của hạ tầng máy chủ Aurora University cung cấp | Ảnh hưởng cách đóng gói/cấu hình triển khai, không thay đổi nghiệp vụ | Chờ xác nhận khi triển khai |
| OQ-02 | Công nghệ/framework/database triển khai | Ảnh hưởng Architecture/Implementation, không thay đổi PRD | Chờ quyết định kỹ thuật |
| OQ-06 | Trường xác nhận chủ sở hữu sản phẩm/đầu mối có thẩm quyền: đề xuất Trưởng bộ phận/phụ trách điều phối hỗ trợ sinh viên | Nhận backlog, ưu tiên, roadmap và phát hành sau bàn giao; không thêm role ứng dụng | Đề xuất 25/11/2026, chờ trường xác nhận |
| OQ-07 | Trường xác nhận ngày đóng cửa dịp Tết; 08–12/02/2027 hiện chỉ là giả định lập kế hoạch | Tính lại lịch ngày làm việc, nghiệm thu và năng lực trước baseline nếu khác giả định | Chờ trường xác nhận; không phải lịch nghỉ chính thức |
| OQ-08 | Xác nhận Proposal/phạm vi, đầu mối và nguồn lực trước khởi động | Đề xuất gửi 30/11, mục tiêu xác nhận 04/12, khởi động có điều kiện 07/12/2026 | Chưa gửi, chưa có phê duyệt baseline |

## 3. Vấn Đề Đã Xác Nhận

| ID | Vấn đề | Quyết định | Ngày xác nhận | Cập nhật tại |
| :--- | :--- | :--- | :--- | :--- |
| OQ-03 | Nguồn và cách cập nhật nội dung FAQ dùng cho FR-STU-01 | Nạp sẵn dữ liệu FAQ khi triển khai; không bổ sung chức năng quản lý FAQ | 27/10/2026 | FR-STU-01 mục 6 |
| OQ-04 | Định dạng file xuất báo cáo của FR-MGT-06 | CSV (UTF-8) | 27/10/2026 | FR-MGT-06 mục 3, FR-MGT-06/AC-08 |
| OQ-05 | Danh sách ngày nghỉ lễ/ngày nghỉ chính thức của Aurora University | Nạp sẵn danh sách ngày nghỉ khi triển khai; không bổ sung chức năng cấu hình ngày nghỉ | 27/10/2026 | `BR-DUE-02` |

OQ-05 chỉ chốt cách nạp danh sách ngày nghỉ khi triển khai, không xác nhận nội dung lịch nghỉ 2027; lịch đóng cửa cụ thể còn chờ OQ-07.

Các câu hỏi mới nếu làm thay đổi phạm vi, effort hoặc tiến độ phải được đưa qua quy trình quản lý thay đổi thay vì tự bổ sung vào PRD.
