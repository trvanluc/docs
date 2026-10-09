# Yêu Cầu Về Ma Trận Truy Xuất (Requirements Traceability Matrix - RTM)

## 1. Mục Tiêu Ma Trận Truy Xuất Yêu Cầu (RTM Scope)
Ma trận RTM liên kết 1:1 từ Yêu cầu Mục tiêu Dự án (Project Proposal), Yêu cầu Chức năng/Phi chức năng (PRD Specification), Lớp API/Data Model và Kịch bản Kiểm thử Chấp nhận Người dùng (UAT Test Scenarios). Ma trận đảm bảo **100%** các tính năng cam kết đều được hiện thực hóa kỹ thuật và có test case nghiệm thu tương ứng.

## 2. Bảng Ma Trận Truy Xuất Chi Tiết (Traceability Matrix)

| Mã Yêu Cầu Proposal | Mã Chức Năng PRD | Tên Chức Năng PRD | Endpoints API Liên Quan | Mã Kịch Bản UAT | Trạng Thái Dev |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1: Student** | `FR-STU-01` | Đăng nhập SSO/Local Sinh viên | `POST /api/v1/auth/login` | `UAT-STU-01` | Ready |
| | `FR-STU-02` | Khởi tạo Ticket & Upload minh chứng | `POST /api/v1/tickets` | `UAT-STU-02` | Ready |
| | `FR-STU-03` | Theo dõi tiến độ & Bổ sung hồ sơ | `GET /api/v1/tickets/{id}`<br>`POST /api/v1/tickets/{id}/supplement` | `UAT-STU-03` | Ready |
| | `FR-STU-04` | Xem kết quả giải quyết & Đánh giá CSAT | `POST /api/v1/tickets/{id}/rate` | `UAT-STU-04` | Ready |
| **M2: Staff** | `FR-STF-01` | Đăng nhập Phân hệ Cán bộ | `POST /api/v1/auth/login` | `UAT-STF-01` | Ready |
| | `FR-STF-02` | Tiếp nhận Queue, Phân loại & Priority | `POST /api/v1/staff/tickets/{id}/claim`<br>`PATCH /api/v1/staff/tickets/{id}/priority` | `UAT-STF-02` | Ready |
| | `FR-STF-03` | Chuyển tiếp phòng ban liên quan | `POST /api/v1/staff/tickets/{id}/transfer` | `UAT-STF-03` | Ready |
| | `FR-STF-04` | Yêu cầu Sinh viên bổ sung hồ sơ | `POST /api/v1/staff/tickets/{id}/request-info` | `UAT-STF-04` | Ready |
| | `FR-STF-05` | Hoàn tất giải quyết Ticket | `POST /api/v1/staff/tickets/{id}/resolve` | `UAT-STF-05` | Ready |
| **M3: Manager** | `FR-MNG-01` | Đăng nhập Phân hệ Quản lý | `POST /api/v1/auth/login` | `UAT-MNG-01` | Ready |
| | `FR-MNG-02` | Dashboard Giám sát & Phân công Công việc | `GET /api/v1/reports/dashboard`<br>`POST /api/v1/staff/tickets/{id}/assign` | `UAT-MNG-02` | Ready |
| | `FR-MNG-03` | Báo cáo Thống kê SLA & Bảng điểm CSAT | `GET /api/v1/reports/sla-csat` | `UAT-MNG-03` | Ready |
| | `FR-MNG-04` | Quản trị Tài khoản & Phân quyền Vai trò | `POST/PUT/DELETE /api/v1/users` | `UAT-MNG-04` | Ready |
| **NFR: Bảo mật** | `NFR-SEC-01` | Chống giả mạo & Phân quyền RBAC 4 Vai trò | `AuthMiddleware`, `RoleGuard` | `UAT-SEC-01` | Ready |
| | `NFR-SEC-02` | Bảo mật Stream File & Zero Public Access | `GET /api/v1/attachments/{id}` | `UAT-SEC-02` | Ready |
| | `NFR-SEC-03` | Ghi vết Tra soát Append-Only Audit Log | `GET /api/v1/audit-logs` | `UAT-SEC-03` | Ready |
| **NFR: Hiệu năng** | `NFR-PER-01` | Đảm bảo tải $\ge 150\text{ CCU}$ & $P_{95} < 1\text{s}$ | All Private APIs | `UAT-PER-01` | Ready |