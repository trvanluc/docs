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

Trong `master-schedule.xlsx`, `Danh sách issue` giữ ngày riêng của 58 parent task; `Gantt MS-04` thể hiện bảy task #149–#155 trong mốc mới 12–25/03/2027. `Master Schedule` là nhóm tổng hợp, không gán toàn bộ giờ nhóm cho từng task. Tra ngày RES-02, RES-03, REOPEN-01/02 từ `Danh sách issue` và `Lịch task-vai trò`, không dùng ví dụ ngày tháng 1 của bản nháp trước.

`Lịch task-vai trò` là lịch theo bước × vai trò; `Phân bổ WP` nối giờ về WP–vai trò gốc; `Tải ngày` và `Năng lực tuần` cộng từ cùng lịch đó. Có hoạt động cấp dự án ngoài parent task, buffer kỹ thuật và giữ chỗ rủi ro riêng, không tạo parent task mới. Các bước NOTI-01 và REL-01 có gate từng mốc nhưng parent chỉ hoàn tất ở MS-04. SEC-02 có nền tảng MS-01, kiểm file thật theo chức năng nguồn MS-02…MS-04; không tuyên bố kiểm chức năng tương lai ở MS-01. Đây là ước lượng v1.2 chờ PM/TL rà soát; ngày 25/11/2026 đã đồng bộ và đọc lại 6 milestone, 58 parent task cùng membership/Hạn trên Projects qua [PR #203](https://github.com/trvanluc/docs/pull/203). Không đổi trạng thái hoàn thành hoặc giờ thực tế; đồng bộ không phải phê duyệt kế hoạch.


### Tra từ task về giờ kế hoạch

Mở [wbs.xlsx](wbs.xlsx), sheet `Đối chiếu mã`: tra mã task hoặc số issue để tìm WBS thực, hàng Gantt, dòng công việc chi tiết, WP và hàng ngân sách `Resource`. Sheet `Đối chiếu effort` là cầu nối số giờ giữa hai cách nhóm WBS và WP; 540h chức năng được đối chiếu một lần. Giờ gói trong bảng crosswalk là **gói WBS dùng chung**, không được cộng theo số issue; giờ riêng từng bước/task mới được phân rã và đối soát ở `Phân bổ WP`/`Lịch task-vai trò`. Xem [phụ lục A.5](../../06-acceptance/traceability-matrix.md#a5-đối-chiếu-wp-với-wbs-và-parent-task) để hiểu ranh giới gói và ví dụ #153.


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
