# Ma trận Truy xuất Yêu cầu (Requirements Traceability Matrix - RTM)

### 1. Mục đích
Tài liệu này dùng để truy xuất và đối chiếu mối quan hệ giữa các Yêu cầu Nghiệp vụ (Requirements / Features), Quy trình Thực hiện (Workflows), Phân hệ Phần mềm (Modules) và các Kịch bản Kiểm thử (Test Scenarios) nhằm đảm bảo tất cả các cam kết trong Proposal dự án UniSupport đều được phát triển và kiểm thử đầy đủ.

### 2. Ma trận Truy xuất Chi tiết

| Mã Yêu cầu (Req ID) | Tên Yêu cầu / Tính năng theo scope đã chốt | Phân hệ / Năng lực | Quy trình (Workflow) | Mã Test Scenario | Trạng thái Nghiệm thu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REQ-STU-01** | Tra cứu hướng dẫn & FAQ | M01-student-portal | WF-01 | TS-STU-01 | Chờ UAT |
| **REQ-STU-02** | Tạo & gửi yêu cầu hỗ trợ, chọn nhóm vấn đề, đính kèm file ảnh/PDF và nhận mã Ticket | M01-student-portal | WF-01 | TS-STU-02 | Chờ UAT |
| **REQ-STU-03** | Xem & theo dõi yêu cầu, trạng thái, người/phòng ban phụ trách và lịch sử cập nhật | M01-student-portal | WF-01, WF-03 | TS-STU-03 | Chờ UAT |
| **REQ-STU-04** | Nhận thông báo trạng thái trong hệ thống | Notification dùng chung cho M01-M03 | WF-01, WF-03, WF-05 | TS-NTF-01 | Chờ UAT |
| **REQ-STU-05** | Bổ sung thông tin & phản hồi theo yêu cầu nhân viên | M01-student-portal | WF-03 | TS-STU-04 | Chờ UAT |
| **REQ-STU-06** | Xem kết quả & đánh giá mức độ hài lòng | M01-student-portal | WF-06 | TS-STU-05 | Chờ UAT |
| **REQ-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | M02-staff-operations | WF-02 | TS-STF-01 | Chờ UAT |
| **REQ-STF-02** | Phân loại & phân công xử lý | M02-staff-operations | WF-02 | TS-STF-02 | Chờ UAT |
| **REQ-STF-03** | Quản lý ưu tiên & thời hạn SLA | M02-staff-operations | WF-02, WF-05 | TS-STF-03 | Chờ UAT |
| **REQ-STF-04** | Xử lý, cập nhật tiến độ và yêu cầu sinh viên bổ sung hồ sơ | M02-staff-operations | WF-03, WF-05 | TS-STF-04 | Chờ UAT |
| **REQ-STF-05** | Chuyển xử lý, escalation & hoàn tất | M02-staff-operations | WF-04, WF-05 | TS-STF-05 | Chờ UAT |
| **REQ-STF-06** | Đóng & mở lại yêu cầu trong thời hạn cho phép | M02-staff-operations | WF-06 | TS-STF-06 | Chờ UAT |
| **REQ-MNG-01** | Quản lý tài khoản, vai trò & RBAC | M03-management-dashboard | N/A | TS-MNG-01 | Chờ UAT |
| **REQ-MNG-02** | Quản lý phòng ban & danh mục | M03-management-dashboard | N/A | TS-MNG-02 | Chờ UAT |
| **REQ-MNG-03** | Kiểm soát quyền truy cập & Audit Trail | Security dùng chung cho M01-M03 | N/A | TS-SEC-01 | Chờ UAT |
| **REQ-MNG-04** | Quản lý thời hạn lưu trữ | M03-management-dashboard | N/A | TS-MNG-03 | Chờ UAT |
| **REQ-MNG-05** | Dashboard & thống kê quản trị | M03-management-dashboard | N/A | TS-MNG-04 | Chờ UAT |
| **REQ-MNG-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | M03-management-dashboard | N/A | TS-MNG-05 | Chờ UAT |

---
