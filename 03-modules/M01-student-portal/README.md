# M01 — Chỉ mục PRD và đối chiếu Resources

## Danh mục yêu cầu đã chốt

Nguồn mô tả chi tiết: [prd.md](./prd.md). Danh mục dưới đây dùng mã FR của PRD, không lấy số thứ tự công việc Resources làm mã FR.

| Mã FR | Tên yêu cầu |
| --- | --- |
| FR-STU-01 | Đăng nhập tài khoản sinh viên |
| FR-STU-02 | Gửi yêu cầu hỗ trợ (Tạo Ticket) |
| FR-STU-03 | Theo dõi tiến độ & Bổ sung thông tin/giấy tờ |
| FR-STU-04 | Xem kết quả giải quyết & Đánh giá mức độ hài lòng |

## Luồng người dùng

ADMIN cấp tài khoản → Sinh viên đăng nhập (FR-STU-01) → Gửi yêu cầu (FR-STU-02) → Theo dõi/bổ sung khi cần (FR-STU-03) → Xem kết quả và đánh giá (FR-STU-04).

Nhóm vấn đề là danh mục nội dung yêu cầu do ADMIN quản lý và gắn phòng ban mặc định. Tệp sinh viên tối đa 5 tệp, 5MB/tệp; tệp kết quả nhân viên tối đa 3 tệp, 5MB/tệp; định dạng PDF, PNG, JPG, JPEG theo PRD. “Cần bổ sung” dùng mã NEED_MORE_INFO; “Đã giải quyết” dùng RESOLVED, “Đã đóng” dùng CLOSED. Xem lại trang Ticket không phải mở lại xử lý.

## Đối chiếu giờ Resources

Nguồn là sheet **Resource** của workbook, không có sheet riêng mang tên M1/M2/M3. Tổng nhóm 124 giờ cơ sở + 4 giờ dự phòng = **128 giờ kế hoạch**. Một dòng giờ có thể được nhiều FR dùng chung; không cộng lại hay tự chia giờ giữa các FR.

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-STU-01 | 3 | Tra cứu hướng dẫn & FAQ | 3 | 3 | 0 | 4 | 0 | 0 | 0 | 4 | 14 | 0 | 14 | Chưa có FR FAQ được chốt; giữ dòng nguồn, không thay mã đăng nhập |
| R-STU-02 | 4 | Tạo & gửi yêu cầu hỗ trợ | 5 | 5 | 1 | 10 | 1 | 6 | 1 | 5 | 34 | 3 | 37 | FR-STU-02 |
| R-STU-03 | 5 | Xem & theo dõi yêu cầu | 4 | 3 | 1 | 8 | 3 | 5 | 3 | 5 | 32 | 1 | 33 | FR-STU-03 |
| R-STU-04 | 6 | Nhận thông báo trạng thái | 3 | 1 | 0 | 4 | 0 | 4 | 4 | 3 | 19 | 0 | 19 | FR-STU-03; thông báo trạng thái đã có |
| R-STU-05 | 7 | Bổ sung thông tin & phản hồi | 3 | 1 | 0 | 5 | 3 | 5 | 3 | 5 | 25 | 0 | 25 | FR-STU-03; FR-STU-04 (đối chiếu phần phản hồi/đánh giá; chưa có phân bổ riêng) |
| Tổng | — | Mỗi dòng tính một lần | 18 | 13 | 2 | 31 | 7 | 20 | 11 | 22 | 124 | 4 | 128 | Không cộng lại khi nhiều FR dùng chung |

Xem [giới hạn và những tên công việc chưa có đặc tả thống nhất](../../Phan_bo_Resources_Antigravity.md). Không tự bổ sung FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ hoặc UI dọn dẹp chỉ vì tên công việc có trong bảng nguồn.
