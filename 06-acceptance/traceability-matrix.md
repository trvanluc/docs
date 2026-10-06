# Ma trận Truy xuất Yêu cầu (Requirements Traceability Matrix - RTM)

### 1. Mục đích
Tài liệu này dùng để truy xuất và đối chiếu mối quan hệ giữa các Yêu cầu Nghiệp vụ (Requirements / Features), Quy trình Thực hiện (Workflows), Phân hệ Phần mềm (Modules) và các Kịch bản Kiểm thử (Test Scenarios) nhằm đảm bảo tất cả các cam kết trong Proposal dự án UniSupport đều được phát triển và kiểm thử đầy đủ.

### 2. Ma trận Truy xuất Chi tiết

| Mã Yêu cầu (Req ID) | Tên Yêu cầu / Tính năng | Phân hệ (Module) | Quy trình (Workflow) | Mã Test Scenario | Trạng thái Nghiệm thu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REQ-STU-01** | Đăng nhập tài khoản Sinh viên | M01-student-portal | WF-01 | TS-STU-01 | Chờ UAT |
| **REQ-STU-02** | Tạo Ticket, chọn nhóm vấn đề & đính kèm file (PDF/Ảnh) | M01-student-portal | WF-01 | TS-STU-02 | Chờ UAT |
| **REQ-STU-03** | Xem danh sách & tiến độ xử lý Ticket | M01-student-portal | WF-01, WF-03 | TS-STU-03 | Chờ UAT |
| **REQ-STU-04** | Bổ sung thông tin/giấy tờ theo yêu cầu | M01-student-portal | WF-03 | TS-STU-04 | Chờ UAT |
| **REQ-STU-05** | Xem kết quả & Đánh giá mức độ hài lòng (1–5 sao) | M01-student-portal | WF-06 | TS-STU-05 | Chờ UAT |
| **REQ-STF-01** | Tiếp nhận (Claim) & Phân loại mức độ ưu tiên Ticket | M02-staff-operations | WF-02 | TS-STF-01 | Chờ UAT |
| **REQ-STF-02** | Chuyển tiếp Ticket sang phòng ban khác | M02-staff-operations | WF-04 | TS-STF-02 | Chờ UAT |
| **REQ-STF-03** | Gửi yêu cầu sinh viên bổ sung hồ sơ | M02-staff-operations | WF-03 | TS-STF-03 | Chờ UAT |
| **REQ-STF-04** | Cập nhật kết quả giải quyết & Đóng Ticket | M02-staff-operations | WF-05 | TS-STF-04 | Chờ UAT |
| **REQ-MNG-01** | Xem Dashboard báo cáo tổng quan & xu hướng | M03-management-dashboard | N/A | TS-MNG-01 | Chờ UAT |
| **REQ-MNG-02** | Quản lý tài khoản & Phân quyền người dùng (RBAC) | M03-management-dashboard / M05 | N/A | TS-MNG-02 | Chờ UAT |
| **REQ-SEC-01** | Bảo mật tệp đính kèm theo phân quyền người liên quan | M05-rbac-security | N/A | TS-SEC-01 | Chờ UAT |

---