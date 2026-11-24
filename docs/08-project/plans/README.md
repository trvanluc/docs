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

### Lịch sử phiên bản Word và Excel

| File | Nơi ghi lịch sử |
| --- | --- |
| [wbs.xlsx](wbs.xlsx) | Sheet `Change log` |
| [ngan-sach-noi-bo.xlsx](ngan-sach-noi-bo.xlsx) | Sheet `Change log` |
| [master-schedule.xlsx](master-schedule.xlsx) | Sheet `Change log` |
| [quotation.xlsx](../quotation.xlsx) | Sheet `Phiên bản` |
| [Proposal.docx](../Proposal.docx) | Dùng chung sheet `Phiên bản` của báo giá gửi kèm; dòng thay đổi ghi rõ tên Proposal |

Giữ tên file cố định. Mỗi dòng có phiên bản, ngày, nội dung, issue/CR và người duyệt hoặc trạng thái chờ duyệt; xác nhận sau review phải dẫn bằng chứng. Dòng `v1.0-baseline` chỉ ghi nhận hiện trạng ngày 24/11/2026, không suy diễn ngày hay người đã phê duyệt trước đó. Khi CR thêm giờ cho một FR, cập nhật WBS, ngân sách theo vai trò/chi phí, báo giá, nguồn lực/Gantt, truy vết/test và lịch sử các file bị ảnh hưởng theo [quy trình CR mục 5](../../11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi).
