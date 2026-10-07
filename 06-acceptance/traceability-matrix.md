# Ma trận Truy xuất Yêu cầu (Requirements Traceability Matrix - RTM)

> Nguồn chuẩn hóa nhân sự & phạm vi: `Phan_bo_Resources_Antigravity.md`

### 1. Mục đích
Tài liệu này dùng để truy xuất và đối chiếu mối quan hệ giữa 17 Chức năng Nghiệp vụ chuẩn hóa từ Bảng phân bổ Resource (`Phan_bo_Resources_Antigravity.md`), Quy trình Nghiệp vụ (Workflows), Phân hệ Phần mềm (Modules) và các Kịch bản Kiểm thử UAT (Test Scenarios).

### 2. Ma trận Truy xuất Chi tiết (17 Business Functions)

| Mã Yêu Cầu | Tên Chức Năng (Function) | Effort KH | Phân Hệ Phụ Trách | Quy Trình (Workflow) | Mã Test Scenario | Trạng Thái Nghiệm Thu |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **FR-STU-01** | Tra cứu hướng dẫn & FAQ | 14h | M01-student-portal | N/A | TS-STU-01 | Chờ UAT |
| **FR-STU-02** | Tạo & gửi yêu cầu hỗ trợ | 37h | M01-student-portal | WF-01 | TS-STU-02 | Chờ UAT |
| **FR-STU-03** | Xem & theo dõi yêu cầu | 33h | M01-student-portal | WF-01, WF-03 | TS-STU-03 | Chờ UAT |
| **FR-STU-04** | Nhận thông báo trạng thái | 19h | M01 / M04-notification | WF-01 đến WF-06 | TS-STU-04 | Chờ UAT |
| **FR-STU-05** | Bổ sung thông tin & phản hồi (CSAT) | 25h | M01-student-portal | WF-03, WF-06 | TS-STU-05 | Chờ UAT |
| **FR-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | 33h | M02-staff-operations | WF-02 | TS-STF-01 | Chờ UAT |
| **FR-STF-02** | Phân loại & phân công xử lý | 38h | M02-staff-operations | WF-02 | TS-STF-02 | Chờ UAT |
| **FR-STF-03** | Quản lý ưu tiên & thời hạn (SLA) | 29h | M02-staff-operations | WF-02, WF-05 | TS-STF-03 | Chờ UAT |
| **FR-STF-04** | Xử lý & cập nhật yêu cầu | 39h | M02-staff-operations | WF-03 | TS-STF-04 | Chờ UAT |
| **FR-STF-05** | Chuyển xử lý, Escalation & hoàn tất | 32h | M02-staff-operations | WF-04, WF-05 | TS-STF-05 | Chờ UAT |
| **FR-STF-06** | Đóng & mở lại yêu cầu | 26h | M02-staff-operations | WF-05, WF-06 | TS-STF-06 | Chờ UAT |
| **FR-ADM-01** | Quản lý tài khoản, vai trò & RBAC | 64h | M03 / M05-rbac | N/A | TS-ADM-01 | Chờ UAT |
| **FR-ADM-02** | Quản lý phòng ban & danh mục | 26h | M03-management | N/A | TS-ADM-02 | Chờ UAT |
| **FR-ADM-03** | Kiểm soát quyền truy cập & Audit Trail | 40h | M03 / M05-rbac | N/A | TS-ADM-03 | Chờ UAT |
| **FR-ADM-04** | Quản lý thời hạn lưu trữ | 15h | M03 / M05-rbac | N/A | TS-ADM-04 | Chờ UAT |
| **FR-ADM-05** | Dashboard & thống kê quản trị | 33h | M03-management | N/A | TS-ADM-05 | Chờ UAT |
| **FR-ADM-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | 37h | M03-management | N/A | TS-ADM-06 | Chờ UAT |

---