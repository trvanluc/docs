# 03 - Functional Modules

Thư mục `03-modules` đặc tả yêu cầu chức năng của **UniSupport** theo ba phân hệ nghiệp vụ chính. Nội dung tại đây được xây dựng trên các quy tắc và mô hình nghiệp vụ đã xác lập trong `02-domain`.

## Các Phân Hệ Nghiệp Vụ Chính

| Phân hệ | Phạm vi |
| :--- | :--- |
| [M01 - Student Portal](./M01-student-portal/) | Tra cứu hướng dẫn, tạo Ticket, theo dõi tiến độ, bổ sung thông tin, nhận kết quả và đánh giá mức độ hài lòng. |
| [M02 - Staff Operations](./M02-staff-operations/) | Tiếp nhận, phân loại, phân công, xử lý, chuyển xử lý/chuyển cấp, yêu cầu bổ sung và ghi nhận kết quả Ticket. |
| [M03 - Management Dashboard](./M03-management-dashboard/) | Giám sát hoạt động hỗ trợ, Dashboard/báo cáo và các chức năng quản trị được phân quyền. |

## Năng Lực Dùng Chung

Một số chức năng được áp dụng xuyên suốt các phân hệ và không được xem là phân hệ nghiệp vụ độc lập:

- **Notification:** tạo và hiển thị thông báo khi phát sinh các sự kiện Ticket liên quan.
- **Authentication, RBAC & Security:** xác thực, kiểm soát quyền truy cập và bảo vệ dữ liệu theo vai trò/phạm vi trách nhiệm.

Các năng lực dùng chung được đặc tả tại Domain, Workflows, yêu cầu phi chức năng và thiết kế hệ thống, đồng thời được áp dụng xuyên suốt M01, M02 và M03.

## Cấu Trúc Đặc Tả

Mỗi phân hệ gồm:

- `README.md`: phạm vi, đối tượng sử dụng, danh sách yêu cầu chức năng, luồng nghiệp vụ chính và quan hệ với các phần còn lại.
- `prd.md`: Functional Requirements, điều kiện tiên quyết, luồng chính, luồng ngoại lệ, Business Rules và Acceptance Criteria.

Các trạng thái Ticket, thời hạn xử lý, quy tắc file đính kèm, mở lại Ticket và CSAT phải tuân thủ thống nhất theo [02-domain](../02-domain/).
