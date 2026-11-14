# Ma Trận Truy Xuất Yêu Cầu (RTM)

## 1. Mục Đích

RTM liên kết **Gói công việc → Functional Requirement/Flow → Workflow → UAT** để duy trì khả năng truy xuất giữa kế hoạch nguồn lực, yêu cầu và nghiệm thu.

## 2. M01 - Student

| Gói công việc | Effort | FR / Flow | Workflow | UAT |
| :--- | ---: | :--- | :--- | :--- |
| WP-STU-01 - Tra cứu hướng dẫn & FAQ | 14h | FR-STU-01 | - | TS-STU-01 |
| WP-STU-02 - Tạo & gửi yêu cầu hỗ trợ | 37h | FR-STU-02 | WF-01 | TS-STU-02 |
| WP-STU-03 - Xem & theo dõi yêu cầu | 33h | FR-STU-03 | WF-01, WF-03, WF-06 | TS-STU-03 |
| WP-STU-04 - Nhận thông báo trạng thái | 19h | FR-STU-04 | WF-01, WF-03, WF-04, WF-05, WF-06 | TS-STU-04 |
| WP-STU-05 - Bổ sung thông tin & phản hồi | 25h | FR-STU-05, FR-STU-06, FR-STU-07 | WF-03, WF-06 | TS-STU-05, TS-STU-06, TS-STU-07 |

**Tổng M01: 128h.**

## 3. M02 - Staff

| Gói công việc | Effort | FR / Flow | Workflow | UAT |
| :--- | ---: | :--- | :--- | :--- |
| WP-STF-01 - Tiếp nhận, tìm kiếm & lọc | 33h | FR-STF-01 | WF-02, WF-06 | TS-STF-01, TS-STF-08 |
| WP-STF-02 - Phân loại & phân công | 38h | FR-STF-02 | WF-02 | TS-STF-02 |
| WP-STF-03 - Quản lý ưu tiên & thời hạn | 29h | FR-STF-03 | WF-02 | TS-STF-03 |
| WP-STF-04 - Xử lý & cập nhật yêu cầu | 39h | FR-STF-04 | WF-03 | TS-STF-04 |
| WP-STF-05 - Chuyển xử lý, Escalation & hoàn tất | 32h | FR-STF-05 + luồng ghi nhận kết quả của FR-STF-06 | WF-04, WF-05, WF-07 | TS-STF-05, TS-STF-06, TS-STF-07 |
| WP-STF-06 - Đóng & mở lại yêu cầu | 26h | FR-STF-01 + Luồng B của FR-STF-06 | WF-06 | TS-STF-08 |

**Tổng M02: 197h.**

> WP-STF-06 bao gồm phần tiếp nhận và xử lý lại Ticket sau khi được mở lại. Quyền chuyển trạng thái vẫn tuân theo Ticket Lifecycle.

## 4. M03 - Management

| Gói công việc | Effort | FR / Flow | Workflow | UAT |
| :--- | ---: | :--- | :--- | :--- |
| WP-MGT-01 - Tài khoản, vai trò & RBAC | 64h | FR-MGT-00, FR-MGT-01 + xác thực dùng chung | - | TS-MGT-01 |
| WP-MGT-02 - Phòng ban & danh mục | 26h | FR-MGT-02 | WF-01, WF-02, WF-04 | TS-MGT-02 |
| WP-MGT-03 - Kiểm soát quyền truy cập & Audit Trail | 40h | FR-MGT-03 + kiểm soát quyền xuyên M01-M03 | Tất cả workflow liên quan | TS-MGT-03 + kiểm tra quyền dùng chung |
| WP-MGT-04 - Quản lý thời hạn lưu trữ | 15h | FR-MGT-04 | - | TS-MGT-04 |
| WP-MGT-05 - Dashboard & thống kê quản trị | 33h | FR-MGT-05 | - | TS-MGT-05 |
| WP-MGT-06 - Báo cáo, mức độ hài lòng & xuất dữ liệu | 37h | FR-MGT-06 | WF-06 | TS-MGT-06 |

**Tổng M03: 215h.**

> **Quy ước ánh xạ M3:** nhãn `Admin` trong kế hoạch nguồn lực tương ứng với phạm vi chức năng **Management** trong Product/PRD.

## 5. Năng Lực Dùng Chung Và Hoạt Động Cấp Dự Án

- FR-STU-00 và FR-STF-00 mô tả hành vi truy cập của từng phân hệ nhưng cơ chế xác thực dùng chung được truy xuất về WP-MGT-01, không cộng effort riêng.
- Thông báo cho Staff/Management được truy xuất theo gói công việc nghiệp vụ phát sinh sự kiện tương ứng.
- Hoạt động cấp dự án gồm **305h** (chi tiết theo vai trò ở [ngan-sach-noi-bo.xlsx](../08-project/plans/ngan-sach-noi-bo.xlsx) sheet `Resource`):

| Hoạt động | Effort | Hạng mục báo giá | Mốc | Kiểm chứng |
| :--- | ---: | :--- | :--- | :--- |
| Quản lý dự án & điều phối; demo và thu feedback cuối mốc | 84h | `Q-04` | Khởi động, MS-01…MS-06 | Báo cáo mốc |
| Môi trường, CI/CD; triển khai production, bàn giao mã nguồn | 46h | `Q-05` | MS-01, MS-06 | NFR-DEP |
| Tích hợp toàn hệ thống | 36h | `Q-06` | MS-06 | WF-01…WF-07 |
| Kiểm thử hệ thống, regression mỗi mốc, hỗ trợ UAT | 65h | `Q-07` | MS-01…MS-06 | Toàn bộ TS, NFR |
| Sửa lỗi sau kiểm thử hệ thống và UAT | 32h | `Q-08` | MS-06 | Regression |
| Hướng dẫn sử dụng | 16h | `Q-09` | MS-06 | Tài liệu bàn giao |
| Bảo hành 30 ngày | 26h | `Q-10` | Sau MS-06 | — |

- Dự phòng rủi ro dự án: **40h** (`Q-11`).
- Tổng effort kế hoạch: **885h** (= 540h chức năng + 305h cấp dự án + 40h dự phòng), khớp [quotation.xlsx](../08-project/quotation.xlsx).
