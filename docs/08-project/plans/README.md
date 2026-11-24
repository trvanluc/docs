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


### Tra từ task về giờ kế hoạch

Mở [wbs.xlsx](wbs.xlsx), sheet `Đối chiếu mã`: tra mã task hoặc số issue để tìm WBS thực, hàng Gantt, dòng công việc chi tiết, WP và hàng ngân sách `Resource`. Sheet `Đối chiếu effort` là cầu nối số giờ giữa hai cách nhóm WBS và WP; 540h chức năng được đối chiếu một lần. Các giờ hiện bên từng task là giờ **gói WBS dùng chung**, không phải effort riêng và không được cộng theo số issue. Xem [phụ lục A.5](../../06-acceptance/traceability-matrix.md#a5-đối-chiếu-wp-với-wbs-và-parent-task) để hiểu ranh giới gói và ví dụ #153.


### Lịch sử phiên bản Word và Excel

| File | Nơi ghi lịch sử |
| --- | --- |
| [wbs.xlsx](wbs.xlsx) | Sheet `Change log` |
| [ngan-sach-noi-bo.xlsx](ngan-sach-noi-bo.xlsx) | Sheet `Change log` |
| [master-schedule.xlsx](master-schedule.xlsx) | Sheet `Change log` |
| [quotation.xlsx](../quotation.xlsx) | Sheet `Phiên bản` |
| [Proposal.docx](../Proposal.docx) | Dùng chung sheet `Phiên bản` của báo giá gửi kèm; dòng thay đổi ghi rõ tên Proposal |

Giữ tên file cố định. Mỗi dòng có phiên bản, ngày, nội dung, issue/CR và người duyệt hoặc trạng thái chờ duyệt; xác nhận sau review phải dẫn bằng chứng. Dòng `v1.0-baseline` chỉ ghi nhận hiện trạng ngày 24/11/2026, không suy diễn ngày hay người đã phê duyệt trước đó. Khi CR thêm giờ cho một FR, cập nhật WBS, ngân sách theo vai trò/chi phí, báo giá, nguồn lực/Gantt, truy vết/test và lịch sử các file bị ảnh hưởng theo [quy trình CR mục 5](../../11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi).

Các cột L:N của sheet `Danh sách issue` giữ ngày bắt đầu/kết thúc và vị trí Gantt MS-04 từ V2-02. Bảng đối chiếu mới dùng cột O:Q (WBS thực, giờ gói dùng chung, liên kết bảng gốc), không ghi đè ngày kế hoạch. RES-02 dẫn tới hàng 44 của `Chi tiết công việc` và hàng 5 của `Gantt MS-04`.
