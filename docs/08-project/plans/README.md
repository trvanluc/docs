# Kế hoạch quản lý dự án

Thư mục này chứa các kế hoạch quản lý của dự án UniSupport – Student Support Management System.

| Tài liệu | Nội dung |
|---|---|
| [wbs.xlsx](wbs.xlsx) | Cấu trúc phân rã công việc (WBS): sơ đồ, bảng WBS (mốc, FR, Q-xx, effort, ngày), từ điển WBS và thuật ngữ. |
| [ngan-sach-noi-bo.xlsx](ngan-sach-noi-bo.xlsx) | Kế hoạch ngân sách nội bộ: nguồn lực, giờ công và chi phí nhân sự. |
| [master-schedule.xlsx](master-schedule.xlsx) | Master Plan: Mục lục, Milestones (MS-01…MS-06), Resources (năng lực và tỷ lệ sử dụng), Master Schedule (Gantt vẽ từ ngày), Chi tiết công việc, Danh sách issue, Change log. Giải thích: [master-plan.md](../master-plan.md). |
| [quality-plan.md](../../09-quality/quality-plan.md) | Kế hoạch quản lý chất lượng: nguyên tắc, chỉ số, cổng chất lượng, quy trình xử lý lỗi và sự cố, kiểm thử, DoD. |
| [ke-hoach-quan-tri-giam-sat.md](../../11-governance/ke-hoach-quan-tri-giam-sat.md) | Kế hoạch quản trị và giám sát: tuyến báo cáo, quy trình báo cáo, ngưỡng cảnh báo, chuyển cấp, kiểm soát thay đổi. |
| [ke-hoach-quan-ly-san-pham.md](../../10-product-management/ke-hoach-quan-ly-san-pham.md) | Kế hoạch quản lý sản phẩm: người dùng và giá trị, chỉ số sản phẩm, ra mắt, đo lường, định hướng phát triển. |

Hình minh họa được lưu trong thư mục [images](images/).

### Đối chiếu Gantt với parent task

Trong `master-schedule.xlsx`, sheet `Gantt MS-04` là chi tiết theo bảy parent task #149–#155: cùng người và ngày với GitHub. Hai hàng 24–25 của `Master Schedule` là nhóm tổng hợp, không phải giao mọi task cho mọi người trong nhóm. `Chi tiết công việc` tách RES-02 (xem kết quả, 20–24/11) khỏi RES-03/REOPEN-01 (phản hồi, 25–30/11), ghi riêng REOPEN-02 phía nhân viên.

Đã rà các mốc khác theo ngày và người trong parent task #118–#171: các task có khoảng ngày riêng thuộc nhóm Gantt tương ứng. PERF-01 #171 có DevOps hỗ trợ QA, đã làm rõ ở hàng 33. SEC-02 #128, OBS-01 #129, UI-01 #130, UI-02 #140 và REL-01 #148 được issue khai báo làm song song cả mốc, không có thanh riêng; chúng không phải các task MS-04 bị lệch phân công. Việc thiếu parent task cho phần hoàn thiện thông báo/lịch sử ở hàng 27 được xử lý riêng theo V2-01, không đổi trong V2-02.
