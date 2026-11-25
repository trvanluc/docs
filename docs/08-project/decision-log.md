# Decision Log

**Dẫn chiếu cấu trúc hiện tại:** mục "Out of Scope" được D-05 nhắc tới nay là mục **2.5** của [Proposal.docx](Proposal.docx); giả định ở **2.4**, phạm vi chức năng ở **2.1–2.3**. V3-04 chỉ đổi cấu trúc và số mục, giữ nguyên nội dung quyết định lịch sử bên dưới.

Nơi gốc của các quyết định quan trọng (thay cho bản trên Google Drive). PM ghi; mỗi quyết định một dòng, không sửa dòng cũ. Quyết định thuộc một CR thì ghi mã `CR-xx` và link issue; quyết định đổi mốc, giờ hoặc giá thì ghi thêm sheet `Change log` của [master-schedule.xlsx](plans/master-schedule.xlsx).

| Mã | Ngày | Quyết định | Người quyết định | Lý do | Tài liệu đã cập nhật |
| --- | --- | --- | --- | --- | --- |
| `D-01` | 14/11/2026 | Chốt một bộ mốc chung 6 mốc `MS-01`…`MS-06` theo luồng Ticket cho Proposal, Master Schedule và GitHub (góp ý R1-01); 05/10–14/10/2026 là giai đoạn khởi động, không phải milestone. GitHub Milestones chỉ chứa task dev. | Ban quản lý (PM) | GitHub và 54 task đã theo bộ mốc này; mỗi milestone phải giao được phần phần mềm chạy được, giai đoạn khởi động chỉ giao prototype và thiết kế. | Proposal.docx, milestones-and-timeline.md, master-schedule.xlsx, master-plan.md |
| `D-02` | 14/11/2026 | Giữ giá 300.000.000 VNĐ, lập báo giá từ effort 885h × đơn giá theo vai trò; bảo hành 30 ngày tính vào giá (góp ý R1-02, R1-03). | Ban quản lý (PM) | Giá phải tính lại được khi có CR; Proposal cam kết bảo hành miễn phí. | quotation.xlsx, ngan-sach-noi-bo.xlsx, wbs.xlsx, Proposal.docx |
| `D-03` | 14/11/2026 | Dùng GitHub Issues + Projects làm công cụ quản lý task duy nhất với 5 trạng thái To do/Doing/Review/QA verify/Done; bỏ ClickUp (góp ý R1-06). | Ban quản lý (PM) | Kế hoạch quản trị và chất lượng lấy số liệu từ GitHub. | team-charter.md, ke-hoach-quan-tri-giam-sat.md, quality-plan.md |
| `D-04` | 14/11/2026 | Chia giờ phát triển trong từng chức năng theo đúng người được giao trên Gantt (BE1/FE1: Sinh viên, tài khoản, Dashboard, báo cáo; BE2/FE2: Nhân viên, cấu hình, Audit, lưu trữ); chỉnh đơn giá bán (hệ số khoảng 1,14–1,15 so với chi phí nội bộ, từng vai trò ở quotation.xlsx sheet Đơn giá cột E) để giữ tổng 300.000.000 VNĐ đã nêu trong Proposal. Đơn giá vẫn là chi phí nội bộ × hệ số cho chi phí chung, công cụ và lợi nhuận; hệ số của các vai trò dev/QA tăng từ ~1,14 lên ~1,15 vì giờ dồn sang vai trò có lương thấp hơn (BE2, FE2) làm chi phí nội bộ giảm còn 261,4 triệu. Thay đổi trong PR #178. | Ban quản lý (PM) | Tự review nhất quán: giờ ở sheet Resource lệch người làm trên Gantt/task, làm bảng năng lực cho CR sai. Tổng giờ từng chức năng không đổi. | ngan-sach-noi-bo.xlsx, quotation.xlsx, master-schedule.xlsx (Resources), Proposal.docx mục 4, master-plan.md |
| `D-05` | 16/11/2026 | Proposal.docx mục 2 "Phạm Vi Chức Năng" và mục "Out of Scope" là nơi gốc của phạm vi với khách. Mục 2 bổ sung các chức năng đã có Q-xx và mốc nhưng còn thiếu (FAQ, mở lại và tự động đóng, Escalation, xuất CSV, khóa tài khoản, phòng ban và nhóm vấn đề, tra soát, chính sách lưu trữ), ghi Q-01…Q-03 cho từng phân hệ. product-scope.md và goals-and-non-goals.md dẫn về Proposal. | Ban quản lý (PM) | Tự review r1: mục 2 hẹp hơn báo giá và lịch mốc, phạm vi viết ở 3 nơi nên khi tranh luận CR không rõ căn cứ. Không đổi giờ, giá hay mốc. | Proposal.docx, product-scope.md, goals-and-non-goals.md, docs/README.md |

## Ghi chú bản nháp v1.1 đã được thay thế — 25/11/2026, Chờ PM rà soát

Các dòng D-01…D-05 phía trên là lịch sử, giữ nguyên ngày, lý do và người ghi; không sửa ngược lịch sử. Ghi chú này là **đề xuất `v1.1-draft`**, không phải một quyết định đã được PM/khách phê duyệt.

- Thay cách trình bày hiện hành dựa trên lý do học vụ bằng rà soát nội bộ trước phát hành; giữ nhãn `Mô phỏng` cho khách hàng, Sponsor, đội thực thi, dữ liệu và ví dụ báo cáo/feedback/CR. Lý do lịch sử không bị xóa.
- D-01 ghi 54 task và lịch khởi động cũ theo hiện trạng lúc đó. Hiện tại giữ **58 parent task**, tổng **885h**, cầu nối chức năng **540h**, giá **300.000.000 VNĐ**. Đề xuất gửi 30/11/2026, mục tiêu xác nhận 04/12 và khởi động có điều kiện 07/12; lịch theo ngày làm việc tới MS-06 19/03/2027, chưa phải baseline được duyệt. Chi tiết và giả định nghỉ tại [milestones-and-timeline.md](milestones-and-timeline.md).
- MS-03 bắt đầu **07/01/2027**, là ngày làm việc thứ 23 từ 07/12/2026 (loại cuối tuần và 01/01), tương ứng 04/11 ở lịch cũ; 13/01 không bảo toàn ordinal. Giữ chồng lấn MS-02/MS-03 7 ngày làm việc và kết thúc MS-03 22/01.
- Chủ sở hữu sản phẩm phía trường được đề xuất là Trưởng bộ phận/phụ trách điều phối hỗ trợ sinh viên, **chờ trường xác nhận**; không phải Sponsor phía giao hàng hoặc vai trò ứng dụng mới. BA bàn giao theo thỏa thuận và kết thúc trách nhiệm sau hỗ trợ/bảo hành; xem [kế hoạch sản phẩm](../10-product-management/ke-hoach-quan-ly-san-pham.md#3-chỉ-số-đánh-giá-sản-phẩm).
- **Khoảng trống quy trình:** PR #199 và #202 đã merge nhưng không có recorded approval theo yêu cầu Charter. Chưa đủ bằng chứng review/approve trước merge; không tạo approval, không backdate và không coi review bổ sung sau merge là đã tuân thủ quy trình lịch sử. Biện pháp phòng ngừa cho PR tiếp theo tại [Team Charter](team-charter.md#kiểm-soát-approval-trước-merge).
- Đồng bộ file nhị phân và lịch sử từng file do đầu mối tương ứng thực hiện; không suy diễn từ ghi chú Markdown rằng Excel/Proposal đã được phê duyệt. **Chưa đồng bộ GitHub**, chưa gửi bản Proposal nào; chỉ cập nhật remote/gửi khách khi được cho phép riêng.

## Đề xuất v1.2 thay bản nháp v1.1 — 25/11/2026, Chờ PM/TL rà soát

Không sửa các dòng lịch sử phía trên. Bản v1.1 giữ ordinal/chồng mốc nhưng chưa chứng minh tải trong cửa sổ task: UI/UX 27h/5 ngày và DevOps 30h/3 ngày vượt 4h/ngày. Bản v1.2 thay cách xếp đó bằng phân bổ task–vai trò từ budget nguồn, scope gate trước thiết kế, tách đầu ra môi trường tối thiểu và CI/CD, QA sau đầu ra có thể kiểm. Bỏ chồng mốc; khởi động 07–18/12/2026, MS-06 kết thúc 18/05/2027, tổng 108 ngày làm việc/163 ngày lịch; nghiệm thu dự kiến 01/06, bảo hành 01–30/06 khi nghiệm thu đúng mục tiêu. Các ngày ở ghi chú v1.1 không còn là lịch hiện hành.

Giữ 58 parent task, 885h = 823h cơ sở + 62h dự phòng, 540h chức năng và 300 triệu; không cộng lại 78h khởi động. NOTI-01 #139 và REL-01 #148 hoàn tất MS-04 theo chức năng nguồn. Audit kỹ thuật dùng TS-AUTH-05 ở MS-01; UI và quyền Audit/lưu trữ/xuất báo cáo kiểm ở MS-05. Lịch nghỉ, phân bổ chi tiết và dependency là giả định chờ xác nhận, không phải approval. Đối chiếu [Master Plan](master-plan.md), [bộ mốc](milestones-and-timeline.md) và Change log từng file Office. GitHub chưa đồng bộ, Proposal chưa gửi, không backdate approval.

## Bổ sung v1.2.1-draft — 25/11/2026, Chờ PM/TL review

Không đổi lịch hoặc số liệu của v1.2 và không sửa các quyết định lịch sử. [PR #203](https://github.com/trvanluc/docs/pull/203) là bản nháp chờ review, không phải approval.

- Dashboard dùng quyền cơ sở MANAGEMENT trong scope: không thêm biến thể chỉ xem tổng hợp nhưng cấm mọi Ticket cùng scope; phiên hết hiệu lực/khóa/hạ nhóm bị từ chối cả tổng hợp và danh sách. AC/test đồng bộ với mô hình quyền hữu hạn.
- TS-NFR-02 có bộ ca failure/reload/error theo phần chức năng MS-02, MS-03, MS-04 và kiểm toàn hệ thống MS-06; RTM, Milestones và DoD task nguồn được nối lại. Bộ ca cạnh tranh không thay kiểm lỗi giữa chừng; chưa có test result thực tế.
- AC hiển thị lịch sử Student nêu rõ không trả ghi chú xử lý nội bộ. Quy trình CR phải kiểm slot/ngày/tuần, predecessor và QA gate; tổng Resources hoặc ngưỡng 16h không đủ để hứa giữ hạn, năng lực trống không thay báo giá phần tăng.
- Sửa căn cột metadata dòng v1.2 trong Change log kế hoạch, ghi 885h/300 triệu đúng cột và chờ rà soát đúng cột người duyệt. Proposal đọc độc lập có nhãn khách/Sponsor/đội thực thi Mô phỏng; sổ phiên bản chung ở quotation.xlsx.

Nhánh tài liệu đã được đưa lên PR; **milestone, nội dung parent task và trường Hạn của GitHub Projects chưa được đồng bộ**. Không dùng PR này hoặc bản nháp đã push để suy diễn remote kế hoạch đã khớp, Proposal đã gửi hay khách đã phê duyệt. Các phần chưa áp dụng phải được đọc lại và đối chiếu live trước cập nhật.
