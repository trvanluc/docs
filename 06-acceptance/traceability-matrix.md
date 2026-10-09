# Ma trận truy xuất PRD đã chốt

14 FR có cùng mã/ý nghĩa với 3 PRD chi tiết. Mã R là dòng công sức trong [bảng Resources](../Phan_bo_Resources_Antigravity.md), không phải FR. Những mã FR-ADM-01..06, FR-STU-05, FR-STF-06 từng dùng thay cho dòng công sức đã được chuyển thành R-ADM/R-STU/R-STF trong bảng đối chiếu; không có chức năng mới từ việc đổi mã.

| FR | Tên yêu cầu | PRD | Luồng | Kịch bản | Dòng công sức đối chiếu | Kiểm chứng |
| --- | --- | --- | --- | --- | --- | --- |
| FR-STU-01 | Đăng nhập tài khoản sinh viên | [M01](../03-modules/M01-student-portal/prd.md) | — | TS-STU-01 | R-ADM-01 | Chưa chạy |
| FR-STU-02 | Gửi yêu cầu hỗ trợ (Tạo Ticket) | [M01](../03-modules/M01-student-portal/prd.md) | WF-01 | TS-STU-02 | R-STU-02 | Chưa chạy |
| FR-STU-03 | Theo dõi tiến độ & Bổ sung thông tin/giấy tờ | [M01](../03-modules/M01-student-portal/prd.md) | WF-01, WF-03 | TS-STU-03 | R-STU-03, R-STU-04, R-STU-05 | Chưa chạy |
| FR-STU-04 | Xem kết quả giải quyết & Đánh giá mức độ hài lòng | [M01](../03-modules/M01-student-portal/prd.md) | WF-06 | TS-STU-04 | R-STU-05, R-STF-06, R-ADM-06 | Chưa chạy |
| FR-STF-01 | Nhân viên đăng nhập hệ thống | [M02](../03-modules/M02-staff-operations/prd.md) | — | TS-STF-01 | R-ADM-01 | Chưa chạy |
| FR-STF-02 | Tiếp nhận và phân loại yêu cầu (Claim & Triage) | [M02](../03-modules/M02-staff-operations/prd.md) | WF-02 | TS-STF-02 | R-STF-01, R-STF-02, R-STF-03 | Chưa chạy |
| FR-STF-03 | Chuyển yêu cầu sang đúng phòng ban | [M02](../03-modules/M02-staff-operations/prd.md) | WF-04 | TS-STF-03 | R-STF-05 | Chưa chạy |
| FR-STF-04 | Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement) | [M02](../03-modules/M02-staff-operations/prd.md) | WF-03 | TS-STF-04 | R-STF-04 | Chưa chạy |
| FR-STF-05 | Ghi kết quả và hoàn tất xử lý yêu cầu | [M02](../03-modules/M02-staff-operations/prd.md) | WF-05 | TS-STF-05 | R-STF-05, R-STF-06 | Chưa chạy |
| FR-MNG-01 | Quản lý đăng nhập & Xác thực phân quyền | [M03](../03-modules/M03-management-dashboard/prd.md) | — | TS-MNG-01 | R-ADM-01 | Chưa chạy |
| FR-MNG-02 | Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision) | [M03](../03-modules/M03-management-dashboard/prd.md) | Giám sát đầu ra WF-02/WF-05 | TS-MNG-02 | R-STF-03, R-ADM-05 | Chưa chạy |
| FR-MNG-03 | Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export) | [M03](../03-modules/M03-management-dashboard/prd.md) | Báo cáo đầu ra WF-06 | TS-MNG-03 | R-ADM-06 | Chưa chạy |
| FR-MNG-04 | Quản trị người dùng & Phân quyền (User Management & RBAC) | [M03](../03-modules/M03-management-dashboard/prd.md) | Cấp tài khoản liên cổng | TS-MNG-04 | R-ADM-01, R-ADM-03 | Chưa chạy |
| FR-MNG-05 | Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail) | [M03](../03-modules/M03-management-dashboard/prd.md) | Tra soát đầu ra các luồng | TS-MNG-05 | R-ADM-03 | Chưa chạy |

Không cộng tổng giờ theo các hàng FR này: nhiều FR dùng chung một dòng công sức. Tổng giờ chỉ tính theo 17 dòng Resource cộng PM/DevOps, bằng 640. Ánh xạ CSAT với R-STU-05 là đối chiếu chưa tách effort riêng; không xác nhận một chức năng FAQ/mở lại/lưu trữ đã hoàn tất khi chưa có đặc tả.
