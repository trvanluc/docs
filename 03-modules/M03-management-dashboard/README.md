# M03 — Chỉ mục PRD và đối chiếu Resources

## Danh mục yêu cầu đã chốt

Nguồn mô tả chi tiết: [prd.md](./prd.md). Danh mục dưới đây dùng mã FR của PRD, không lấy số thứ tự công việc Resources làm mã FR.

| Mã FR | Tên yêu cầu |
| --- | --- |
| FR-MNG-01 | Quản lý đăng nhập & Xác thực phân quyền |
| FR-MNG-02 | Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision) |
| FR-MNG-03 | Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export) |
| FR-MNG-04 | Quản trị người dùng & Phân quyền (User Management & RBAC) |
| FR-MNG-05 | Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail) |

## Luồng người dùng

MANAGER/ADMIN đăng nhập (FR-MNG-01) → Xem tình hình và SLA (FR-MNG-02), phân tích/xuất báo cáo (FR-MNG-03). Riêng ADMIN quản trị tài khoản (FR-MNG-04) và xem nhật ký/quyền dữ liệu (FR-MNG-05).

Nhóm vấn đề là danh mục nội dung yêu cầu do ADMIN quản lý và gắn phòng ban mặc định. Tệp sinh viên tối đa 5 tệp, 5MB/tệp; tệp kết quả nhân viên tối đa 3 tệp, 5MB/tệp; định dạng PDF, PNG, JPG, JPEG theo PRD. “Cần bổ sung” dùng mã NEED_MORE_INFO; “Đã giải quyết” dùng RESOLVED, “Đã đóng” dùng CLOSED. Xem lại trang Ticket không phải mở lại xử lý.

## Đối chiếu giờ Resources

Nguồn là sheet **Resource** của workbook, không có sheet riêng mang tên M1/M2/M3. Tổng nhóm 207 giờ cơ sở + 8 giờ dự phòng = **215 giờ kế hoạch**. Một dòng giờ có thể được nhiều FR dùng chung; không cộng lại hay tự chia giờ giữa các FR.

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-ADM-01 | 22 | Quản lý tài khoản, vai trò & RBAC | 5 | 3 | 6 | 3 | 8 | 13 | 9 | 13 | 60 | 4 | 64 | FR-MNG-04; FR-STU-01, FR-STF-01, FR-MNG-01 dùng chung |
| R-ADM-02 | 23 | Quản lý phòng ban & danh mục | 4 | 1 | 3 | 0 | 4 | 5 | 5 | 4 | 26 | 0 | 26 | Danh mục ADMIN quản lý tại Actors & Roles / Terminology; không thêm FR |
| R-ADM-03 | 24 | Kiểm soát quyền truy cập & Audit Trail | 4 | 0 | 4 | 1 | 4 | 9 | 5 | 9 | 36 | 4 | 40 | FR-MNG-04; FR-MNG-05; quyền dữ liệu đã có |
| R-ADM-04 | 25 | Quản lý thời hạn lưu trữ | 3 | 0 | 1 | 0 | 0 | 4 | 4 | 3 | 15 | 0 | 15 | Giữ giờ nguồn; chưa có FR nghiệp vụ riêng về cấu hình/dọn dẹp lưu trữ |
| R-ADM-05 | 26 | Dashboard & thống kê quản trị | 4 | 3 | 1 | 0 | 9 | 3 | 9 | 4 | 33 | 0 | 33 | FR-MNG-02 |
| R-ADM-06 | 27 | Báo cáo, mức độ hài lòng & xuất dữ liệu | 4 | 3 | 1 | 0 | 8 | 5 | 10 | 6 | 37 | 0 | 37 | FR-MNG-03; sử dụng dữ liệu FR-STU-04 |
| Tổng | — | Mỗi dòng tính một lần | 24 | 10 | 16 | 4 | 33 | 39 | 42 | 39 | 207 | 8 | 215 | Không cộng lại khi nhiều FR dùng chung |

Xem [giới hạn và những tên công việc chưa có đặc tả thống nhất](../../Phan_bo_Resources_Antigravity.md). Không tự bổ sung FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ hoặc UI dọn dẹp chỉ vì tên công việc có trong bảng nguồn.
