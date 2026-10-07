# Phạm vi sản phẩm và giả định

## 1. Phạm vi chức năng baseline

### M01 - Student Portal

| Capability | Mô tả | Trạng thái |
| :--- | :--- | :--- |
| Login | Sinh viên đăng nhập bằng tài khoản cá nhân. | Baseline |
| Create Support Ticket | Sinh viên chọn nhóm vấn đề, mô tả yêu cầu, đính kèm ảnh/PDF nếu cần, gửi yêu cầu và nhận mã Ticket. | Baseline |
| Track Ticket | Sinh viên xem tiến độ xử lý và lịch sử cập nhật của Ticket do mình tạo. | Baseline |
| Supplement Information | Sinh viên bổ sung thông tin/giấy tờ khi Staff yêu cầu. | Baseline |
| Receive Notification | Sinh viên nhận thông báo trong hệ thống về các cập nhật liên quan đến Ticket của mình. | Derived |
| View Result & Rate | Sinh viên xem kết quả/thông báo và đánh giá mức độ hài lòng sau khi Ticket hoàn tất. | Baseline |
| FAQ / Guidance | Sinh viên tra cứu hướng dẫn trước khi tạo Ticket. | Proposed |

### M02 - Staff Operations

| Capability | Mô tả | Trạng thái |
| :--- | :--- | :--- |
| Login | Staff đăng nhập hệ thống. | Baseline |
| View Ticket Queue | Staff xem Ticket mới và Ticket được giao. | Baseline |
| Search/Filter Queue | Staff tìm kiếm/lọc danh sách Ticket để xử lý hiệu quả. | Derived |
| Classify Ticket | Staff phân loại Ticket theo nhóm vấn đề. | Baseline |
| Review Priority | Staff xem xét mức độ ưu tiên/hạn xử lý. | Baseline |
| Assign / Transfer Ticket | Staff chuyển Ticket sang phòng ban hoặc người phụ trách phù hợp nếu cần. | Baseline |
| Update Status | Staff cập nhật trạng thái xử lý. | Baseline |
| Request Supplement | Staff yêu cầu Student bổ sung thông tin/giấy tờ. | Baseline |
| Record Resolution | Staff ghi nhận kết quả xử lý. | Baseline |
| Close Ticket | Staff đóng Ticket khi hoàn tất. | Baseline |
| Reopen / Advanced Escalation | Mở lại hoặc escalation nâng cao. | Proposed/TBD |

### M03 - Management Dashboard

| Capability | Mô tả | Trạng thái |
| :--- | :--- | :--- |
| Login | Management đăng nhập hệ thống. | Baseline |
| Dashboard Overview | Xem tổng quan Ticket mới, đang xử lý, sắp quá hạn/quá hạn. | Baseline |
| Workload Monitoring | Theo dõi workload theo phòng ban/nhân viên. | Baseline |
| Reports & Statistics | Báo cáo xu hướng, thời gian xử lý trung bình và feedback sinh viên. | Baseline |
| Account Management | Tạo/chỉnh sửa account. | Baseline |
| Role/Permission Assignment | Gán quyền theo vai trò. | Baseline |
| Department/Category Management | Quản lý phòng ban/danh mục phục vụ cấu hình hệ thống. | Derived |
| Export Data | Xuất dữ liệu báo cáo. | Proposed |
| Retention Management | Cấu hình thời hạn lưu trữ. | Proposed/TBD |

## 2. Năng lực dùng chung

| Capability | Mô tả | Trạng thái |
| :--- | :--- | :--- |
| Role-Based Access | User phải login và được kiểm tra quyền theo role/phạm vi dữ liệu. | Baseline |
| Attachment Protection | File đính kèm chỉ người liên quan được xem/tải. | Baseline |
| Basic Audit History | Các thao tác quan trọng được lưu lịch sử để tra soát. | Baseline |
| Notification Center | Hiển thị thông báo nội bộ trong hệ thống. | Derived |
| SLA Calculation Details | Cách tính cụ thể thời hạn, pause/resume và warning threshold. | TBD |

## 3. Giả định dự án

- Hệ thống phục vụ khoảng 3.000 sinh viên.
- Hệ thống là Web Application responsive, không phải mobile app độc lập.
- UI hỗ trợ Tiếng Việt và Tiếng Anh ở mức cơ bản.
- Hạ tầng server, tên miền, SSL và chất lượng vận hành hạ tầng do Aurora University cung cấp.
- Không tích hợp third-party ngoài phạm vi đã thống nhất.
- Không bao gồm chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

## 4. Các tham số cần xác nhận

| Nội dung | Trạng thái | Ghi chú |
| :--- | :--- | :--- |
| Dung lượng tối đa mỗi file và số lượng file mỗi lần upload | TBD | Proposal chỉ nêu ảnh/PDF, chưa chốt giới hạn. |
| Thang điểm CSAT cụ thể | Proposed | Proposal nói đánh giá hài lòng; thang 1-5 sao là đề xuất hợp lý. |
| Mức priority cụ thể và SLA tương ứng | TBD | Proposal nêu xem xét mức ưu tiên/quá hạn, chưa chốt bảng SLA. |
| Auto-close, reopen, cancel | Proposed/TBD | Không có trong proposal baseline. |
| Export data và retention management | Proposed/TBD | Có thể cần cho vận hành nhưng cần xác nhận scope. |
