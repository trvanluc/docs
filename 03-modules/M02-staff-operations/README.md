# M02 — Chỉ mục PRD và đối chiếu Resources

## Danh mục yêu cầu đã chốt

Nguồn mô tả chi tiết: [prd.md](./prd.md). Danh mục dưới đây dùng mã FR của PRD, không lấy số thứ tự công việc Resources làm mã FR.

| Mã FR | Tên yêu cầu |
| --- | --- |
| FR-STF-01 | Nhân viên đăng nhập hệ thống |
| FR-STF-02 | Tiếp nhận và phân loại yêu cầu (Claim & Triage) |
| FR-STF-03 | Chuyển yêu cầu sang đúng phòng ban |
| FR-STF-04 | Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement) |
| FR-STF-05 | Ghi kết quả và hoàn tất xử lý yêu cầu |

## Luồng người dùng

Nhân viên đăng nhập (FR-STF-01) → Tiếp nhận/phân loại (FR-STF-02) → Chuyển phòng nếu cần (FR-STF-03), hoặc yêu cầu bổ sung (FR-STF-04) → Ghi kết quả/hoàn tất (FR-STF-05).

Nhóm vấn đề là danh mục nội dung yêu cầu do ADMIN quản lý và gắn phòng ban mặc định. Tệp sinh viên tối đa 5 tệp, 5MB/tệp; tệp kết quả nhân viên tối đa 3 tệp, 5MB/tệp; định dạng PDF, PNG, JPG, JPEG theo PRD. “Cần bổ sung” dùng mã NEED_MORE_INFO; “Đã giải quyết” dùng RESOLVED, “Đã đóng” dùng CLOSED. Xem lại trang Ticket không phải mở lại xử lý.

## Đối chiếu giờ Resources

Nguồn là sheet **Resource** của workbook, không có sheet riêng mang tên M1/M2/M3. Tổng nhóm 187 giờ cơ sở + 10 giờ dự phòng = **197 giờ kế hoạch**. Một dòng giờ có thể được nhiều FR dùng chung; không cộng lại hay tự chia giờ giữa các FR.

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-STF-01 | 12 | Tiếp nhận, tìm kiếm & lọc yêu cầu | 3 | 3 | 1 | 4 | 5 | 8 | 3 | 6 | 33 | 0 | 33 | FR-STF-02; Queue phòng ban đã có |
| R-STF-02 | 13 | Phân loại & phân công xử lý | 4 | 0 | 3 | 4 | 3 | 9 | 5 | 9 | 37 | 1 | 38 | FR-STF-02; quyền phân công MANAGER/ADMIN đã có |
| R-STF-03 | 14 | Quản lý ưu tiên & thời hạn | 4 | 0 | 4 | 3 | 3 | 6 | 3 | 3 | 26 | 3 | 29 | FR-STF-02; FR-MNG-02 |
| R-STF-04 | 15 | Xử lý & cập nhật yêu cầu | 4 | 1 | 1 | 4 | 4 | 9 | 4 | 9 | 36 | 3 | 39 | FR-STF-04 |
| R-STF-05 | 16 | Chuyển xử lý, Escalation & hoàn tất | 3 | 0 | 3 | 3 | 3 | 8 | 4 | 5 | 29 | 3 | 32 | FR-STF-03; FR-STF-05 |
| R-STF-06 | 17 | Đóng & mở lại yêu cầu | 3 | 0 | 1 | 3 | 3 | 8 | 3 | 5 | 26 | 0 | 26 | FR-STF-05; FR-STU-04; không chốt phần mở lại xử lý |
| Tổng | — | Mỗi dòng tính một lần | 21 | 4 | 13 | 21 | 21 | 48 | 22 | 37 | 187 | 10 | 197 | Không cộng lại khi nhiều FR dùng chung |

Xem [giới hạn và những tên công việc chưa có đặc tả thống nhất](../../Phan_bo_Resources_Antigravity.md). Không tự bổ sung FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ hoặc UI dọn dẹp chỉ vì tên công việc có trong bảng nguồn.
