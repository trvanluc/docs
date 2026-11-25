# Master Plan

Trang này giải thích các quyết định của kế hoạch. Số liệu (ngày, effort, nguồn lực) chỉ nằm trong Excel:

| Phần | Nơi gốc |
| --- | --- |
| Milestones (mã, ngày, phần giao được, kịch bản kiểm tra, điều kiện nghiệm thu) | [plans/master-schedule.xlsx](plans/master-schedule.xlsx), sheet `Milestones` |
| Gantt (vẽ từ cột Bắt đầu/Kết thúc, không tô tay) | `master-schedule.xlsx`, sheet `Master Schedule` |
| WBS | [plans/wbs.xlsx](plans/wbs.xlsx), sheet `WBS` (mỗi dòng có mốc, FR, `Q-xx`, effort, owner, ngày bắt đầu/kết thúc; tổng 885h) và `Từ điển WBS`; việc chi tiết theo mốc: `master-schedule.xlsx` sheet `Chi tiết công việc` |
| Resources | `master-schedule.xlsx` sheet `Resources`: đội thực thi `Mô phỏng` (vai trò, số người, giờ/tuần), giờ theo vai trò × giai đoạn, tỷ lệ sử dụng để kiểm quá tải; nguồn giờ: [plans/ngan-sach-noi-bo.xlsx](plans/ngan-sach-noi-bo.xlsx) sheet `Resource` |
| Task–vai trò và kiểm tải | `master-schedule.xlsx`: `Lịch task-vai trò`, `Phân bổ WP`, `Tải ngày`, `Năng lực tuần`, `Giả định lịch` |
| Change log | `master-schedule.xlsx` sheet `Change log` |
| Giá | [quotation.xlsx](quotation.xlsx) |
| Rủi ro | [risk-register.md](risk-register.md) |

## Thời điểm của dự án

**Trạng thái đề xuất ngày 25/11/2026:** Proposal `v1.2-draft` đang rà soát nội bộ trước phát hành, **Chờ PM rà soát**, **chưa gửi khách**, nên [sent/](sent/) chưa có bản nào. Đề xuất gửi 30/11/2026, mục tiêu xác nhận 04/12/2026 và khởi động có điều kiện 07/12/2026. Chỉ khởi động khi khách xác nhận Proposal/phạm vi, đầu mối và nguồn lực; chưa có phê duyệt baseline. Lịch dự kiến kết thúc MS-06 ngày 18/05/2027.

**Căn cứ:** hồ sơ chưa phát hành và chưa được khách xác nhận; không trình bày kế hoạch hoặc ví dụ `Mô phỏng` như bằng chứng đã thực hiện.

- 58 parent task trên GitHub là công việc kế hoạch; không suy diễn trạng thái thực hiện từ ngày kế hoạch.
- Không có báo cáo tiến độ hay số giờ thực tế. Ví dụ báo cáo tuần trong [kế hoạch quản trị mục 6.2](../11-governance/ke-hoach-quan-tri-giam-sat.md#62-mẫu-và-ví-dụ-báo-cáo-tuần) ghi `Mô phỏng`, chỉ minh hoạ mẫu.
- Chưa đủ điều kiện khởi động thì PM tính lại theo **thứ tự ngày làm việc**, giữ giờ công, kiểm lại thời lượng và phụ thuộc theo năng lực từng vai trò; không cộng offset ngày lịch.

Ngoài cuối tuần, loại 01/01/2027, 30/04 và 01/05/2027; 08–12/02, 16/04 và nghỉ bù 03/05/2027 là giả định đóng cửa trường phục vụ lập kế hoạch, chờ trường xác nhận (16/04 chưa xác minh lịch âm chính thức), không phải lịch nghỉ chính thức đã được duyệt. Đổi ngày nghỉ phải tính lại trước baseline và ghi `Change log`. Excel, Proposal và GitHub phải được đối chiếu; đợt sửa local này **chưa đồng bộ GitHub**.

## Cách chia milestone

Dự án có **giai đoạn khởi động** (07/12–18/12/2026; 10 ngày làm việc: chốt phạm vi trước prototype và thiết kế phụ thuộc; 27h UI/UX có đủ cửa sổ 7 ngày làm việc sau gate) và **6 mốc** `MS-01`…`MS-06` chia theo **luồng đi của một Ticket** (nền tảng → tiếp nhận → xử lý → trả kết quả → quản trị → tích hợp và bàn giao), không theo phân hệ hay theo tầng kỹ thuật. Lý do:

- Mỗi mốc giao cho client một phần phần mềm **chạy được trên staging**, gồm cả màn hình Sinh viên lẫn Nhân viên của cùng một đoạn luồng. Client kiểm tra được ngay giá trị nghiệp vụ, không phải chờ "xong phân hệ Sinh viên" mới thấy Ticket được xử lý.
- Giai đoạn khởi động (chốt phạm vi, prototype tương tác 3 vai trò, thiết kế kỹ thuật) **không phải milestone** vì chưa giao phần mềm chạy được. Client vẫn duyệt prototype ở cuối giai đoạn này: đây là điểm dừng rẻ nhất để đổi ý về luồng màn hình trước khi code.
- **MS-01 (Nền tảng hệ thống) được giữ làm mốc đầu, dù sinh viên và nhân viên chưa làm được việc nghiệp vụ nào.** Sau MS-01, người quản lý phía khách đăng nhập bản staging và tự tạo tài khoản, phòng ban, nhóm vấn đề và phòng ban tiếp nhận trên phần mềm thật. Đây là dữ liệu mà luồng Ticket ở MS-02 cần. Client cũng kiểm tra được ngay việc chặn truy cập sai quyền (R-01, rủi ro mức Cao).
  - Đánh đổi: phân quyền được làm chắc trước khi có dữ liệu Ticket, đổi lại sinh viên thấy giá trị nghiệp vụ ở cuối MS-02 (17/02/2027), sau nền tảng MS-01 (14/01/2027).
  - Phương án đã cân nhắc: đưa một lát mỏng "sinh viên gửi Ticket, nhân viên thấy trong hàng chờ" vào MS-01. Nhóm không chọn vì phương án này phải làm luồng Ticket trên phân quyền chưa xong, dễ phải làm lại khi phân quyền thay đổi.
- Thứ tự mốc khớp thứ tự ưu tiên FR trong PRD (xem [03-modules/README.md](../03-modules/README.md#mức-ưu-tiên-fr)): FR mức Cao nằm ở `MS-01`…`MS-04`. `MS-05` có Dashboard và báo cáo (mức Cao) nhưng phải đi sau vì cần dữ liệu của vòng đời Ticket đầy đủ.

Phần giao được, kịch bản kiểm tra (`TS-xx`) và điều kiện nghiệm thu của từng `MS-xx` ở sheet `Milestones`; bản tóm tắt ở [milestones-and-timeline.md](milestones-and-timeline.md).

## Ai làm việc gì

Người làm từng chức năng lấy theo Gantt (`master-schedule.xlsx` sheet `Master Schedule`, cột Phụ trách), và giờ trong sheet `Resource` của ngân sách được chia theo đúng người đó:

- **BE1, FE1:** luồng Sinh viên (FAQ, tạo và theo dõi Ticket, bổ sung, kết quả, CSAT), tài khoản và phân quyền, Dashboard, báo cáo.
- **BE2, FE2:** luồng Nhân viên (hàng chờ, phân công, ưu tiên và thời hạn, xử lý, Transfer, Escalation, ghi kết quả), phòng ban và Category, Audit, chính sách lưu trữ.
- **BE1 và BE2 cùng làm:** thông báo xuyên suốt vòng đời Ticket.

Parent task trên GitHub ghi cùng người phụ trách. Đổi người làm một chức năng là đổi cả giờ ở `Resource`, Gantt, task và có thể đổi giá (đơn giá BE1/FE1 khác BE2/FE2), nên đi qua quy trình CR nếu proposal đã gửi.

## Phụ thuộc giữa các milestone

- Khởi động → `MS-01`: phạm vi, prototype và thiết kế dữ liệu/phân quyền đã duyệt. Theo dõi tại [PLN-01 #183](https://github.com/trvanluc/docs/issues/183), [UX-01 #184](https://github.com/trvanluc/docs/issues/184), [ARCH-01 #185](https://github.com/trvanluc/docs/issues/185), [ARCH-02 #186](https://github.com/trvanluc/docs/issues/186). Các parent task này không gắn MS-xx nhưng vẫn được đếm trong tiến độ toàn dự án; người có thẩm quyền xác minh đầu ra và bằng chứng duyệt trong issue trước khi đóng.

- `MS-01` → mọi mốc sau: đăng nhập, phân quyền, phòng ban và Category là điều kiện để tạo Ticket.
- `MS-02` → `MS-03`: xử lý chỉ bắt đầu khi Ticket đã được tiếp nhận và có người phụ trách. Phương án v1.2 không chồng hai mốc: MS-02 kết thúc 17/02, MS-03 bắt đầu 18/02/2027. Trong mỗi mốc, BE/FE chỉ chạy song song khi đã có hợp đồng API/fixture; QA đợi đầu ra cần kiểm.
- `MS-03` → `MS-04`: ghi kết quả cần Ticket ở `IN_PROGRESS` với thời hạn đã tính đúng.
- **Task thông báo xuyên mốc NOTI-01 #139:** nền tảng được kiểm ở MS-02, sự kiện bổ sung/chuyển phòng ở MS-03, hoàn tất ở MS-04. Milestone hoàn tất đề xuất của parent task là **MS-04**, không phải MS-02; chỉ đóng task khi đủ DoD toàn vòng đời. MS-02 vẫn nghiệm thu phần nền tảng qua test/bằng chứng bàn giao, không đợi chức năng MS-04 và không giả đóng task sớm. Sheet `Danh sách issue` ghi đích MS-04; việc chuyển milestone của #139 trên GitHub **chưa thực hiện**, nằm trong danh sách chờ đồng bộ.
- **REL-01 #148:** nền tảng tin cậy ở MS-03; kiểm đủ resolve/reopen ở MS-04, parent hoàn tất MS-04. Không buộc MS-03 phụ thuộc phần hoàn thiện tương lai của chính REL-01; GitHub chờ đồng bộ.
- `MS-04` → `MS-05`: Dashboard, báo cáo thời gian xử lý và CSAT cần dữ liệu của vòng đời đầy đủ.
- `MS-05` → `MS-06`: tích hợp và kiểm thử hệ thống chạy trên bản đủ chức năng.

## Effort cho test, regression và sửa lỗi

Đây là việc biết trước nên đã nằm trong WBS và báo giá:

| Việc | Giờ | Dòng WBS | Hạng mục báo giá |
| --- | ---: | --- | --- |
| Test chức năng trong từng gói chức năng (QA) | 98h | 1.7.2 | trong `Q-01`, `Q-02`, `Q-03` |
| Regression trước mỗi lần giao mốc, tăng theo số kịch bản phải chạy lại: 1h, 2h, 3h, 4h, 5h ở MS-01…MS-05 | 15h | 1.7.2 | `Q-07` |
| Kiểm thử hệ thống: chức năng, tích hợp, phân quyền, hiệu năng (MS-06) | 34h | 1.7.2 | `Q-07` |
| Hỗ trợ UAT (MS-06) | 16h | 1.7.3 | `Q-07` |
| Tích hợp toàn hệ thống (MS-06) | 36h | 1.7.1 | `Q-06` |
| Sửa lỗi giữa các mốc: lỗi do regression hoặc feedback của client ở mốc trước, sửa trong mốc kế tiếp (MS-02…MS-05, mỗi mốc 4h: BE1, BE2, FE1, FE2 mỗi người 1h) | 16h | 1.7.2 | `Q-08` |
| Sửa lỗi sau kiểm thử hệ thống và UAT (MS-06) | 16h | 1.7.2 | `Q-08` |
| Triển khai production, bàn giao mã nguồn (MS-06) | 16h | 1.8.1, 1.8.2 | `Q-05` |
| Hướng dẫn sử dụng (MS-06) | 16h | 1.8.4 | `Q-09` |
| Bảo hành 30 ngày sau nghiệm thu | 26h | 1.8.5 | `Q-10` |

**Tích hợp không dồn vào mốc cuối.** Mỗi mốc giao một luồng chạy xuyên cổng Sinh viên ↔ Nhân viên (↔ Quản lý), nên tích hợp FE–BE và giữa các cổng của luồng đó làm ngay trong mốc, giờ nằm trong gói chức năng của mốc (WBS 1.3–1.6), và được regression trước khi giao. `Q-06` (36h) ở MS-06 chỉ dành cho tích hợp end-to-end toàn bộ luồng và nối dữ liệu vận hành vào Dashboard/báo cáo.

`MS-06` (22 ngày làm việc, dự kiến 14/04–18/05/2027) có 146h cơ sở: TL 16h, BA 21h, UI/UX 2h, FE1 7h, FE2 7h, BE1 14h, BE2 14h, QA 40h, DevOps 14h, PM 11h. Ngoài ra giữ chỗ 40h dự phòng rủi ro trước tích hợp, tách khỏi việc đã cam kết; tổng cửa sổ MS-06 giữ 186h trong bảng tải, không phải đã thực hiện 40h rủi ro. Sửa lỗi/retest và regression được xếp trước UAT/nghiệm thu theo gate trong `Lịch task-vai trò`.

Lỗi Nghiêm trọng phải được sửa và kiểm lại trước khi giao mốc; giờ chức năng và buffer kỹ thuật đã giữ chỗ không được coi là giờ miễn phí. 16h sửa lỗi giữa các mốc dành cho feedback/lỗi không chặn giao mốc trước; MS-06 có 16h sửa lỗi/retest sau kiểm thử hệ thống và UAT. Nếu vượt giờ được phân bổ, PM đánh giá dùng dự phòng theo quyền hạn hoặc tính lại mốc; năng lực trống tự nó không tạo ngân sách effort.

Bảo hành **có tính vào giá**: Proposal cam kết sửa lỗi kỹ thuật miễn phí 30 ngày, nên phần công này nằm trong 300 triệu (`Q-10`, 26h ≈ 8,9 triệu).

## Dự phòng cho thay đổi và rủi ro

- **62h dự phòng**, tách khỏi effort sửa lỗi ở trên:
  - 22h buffer kỹ thuật trong các gói chức năng (cột K sheet `Resource`), nằm trong `Q-01`…`Q-03`.
  - 40h dự phòng rủi ro dự án (`Q-11`), dùng khi một rủi ro trong [risk-register.md](risk-register.md) xảy ra.
- Dự phòng **có tính vào giá**. PM quyết định dùng dự phòng trong phạm vi tổng ngân sách ([kế hoạch quản trị](../11-governance/ke-hoach-quan-tri-giam-sat.md#4-chuyển-cấp-vấn-đề-và-quyền-quyết-định)).
- **CR không lấy từ dự phòng.** Mọi CR làm tăng phạm vi được đánh giá tác động và báo giá riêng theo cùng đơn giá trong `quotation.xlsx`, sheet `Đơn giá`.
- **Năng lực cho CR phải kiểm tới task/ngày.** Mỗi vai trò tối đa 4h/ngày, 20h/tuần; ngày nghỉ giảm năng lực tuần. `Lịch task-vai trò`, `Phân bổ WP`, `Tải ngày` và `Năng lực tuần` thay bảng giữ chỗ cấp giai đoạn trước đây. Tổng tải được tính từ cùng một lịch chi tiết, không chia đều giờ phase hoặc xếp trước ngày task bắt đầu.
  1. BA/TL ước lượng CR theo vai trò, gồm QA, regression và phụ thuộc; báo giá riêng, không dùng dự phòng để tăng phạm vi.
  2. Với CR không quá 16h, chỉ giữ ngày mốc nếu xếp được vào cửa sổ còn trống thực sự, không trùng slot, vẫn qua gate và regression trước giao. Kiểm cả ngày/tuần, không chỉ tổng phần trăm mốc.
  3. Không đủ cửa sổ hoặc vượt ngưỡng thì tính lại mốc bị ảnh hưởng, báo giá và xin khách xác nhận theo quy trình CR; không tự hứa giữ ngày.
  4. PM quyết định theo [quy trình CR](../11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi).
- **Đánh đổi của lịch v1.2:** bỏ chồng mốc, tăng từ bản nháp 69 lên **108 ngày làm việc / 163 ngày lịch** (07/12/2026–18/05/2027) để chứa cửa sổ thiết kế, môi trường, phụ thuộc, QA và dự phòng. Không đổi 885h hay giá. Đây là phương án bảo thủ, không tuyên bố tối ưu thời gian; độ phân giải 15 phút trong lịch chỉ phục vụ kiểm cộng giờ/phụ thuộc, không phải giờ hẹn hoặc độ chính xác ước lượng đã được xác nhận.
- **Căn cứ và giới hạn:** phân bổ task–vai trò là ước lượng nháp từ WP–vai trò gốc, cần PM/TL rà soát lý do phân bổ và đủ dependency. Lịch vượt qua kiểm không trùng slot, tải ngày/tuần và predecessor đã khai báo; không phải bằng chứng đội đã làm, khách đã duyệt hoặc mọi phụ thuộc thực tế đã được phát hiện. 22h buffer chức năng và 40h rủi ro có giữ chỗ nhưng chưa là actual.
- Tổng: 823h cơ sở + 62h dự phòng = **885h**. Chi phí nội bộ khoảng 261,4 triệu (sheet `BẢNG CHI PHÍ NHÂN SỰ`); giá bán 300 triệu (chênh lệch ≈ 12,9% cho chi phí chung, công cụ và lợi nhuận).

## Cách nhận feedback của client sau mỗi milestone

1. Ngày cuối mốc, PM và BA demo trên staging theo kịch bản của mốc (1h PM + 1h BA, nằm trong `Q-04`).
2. Client (`Mô phỏng`) tự dùng thử và gửi phản hồi trong 02 ngày làm việc (giả định `A-16`).
3. PM ghi mỗi phản hồi thành một GitHub Issue theo mẫu **Feedback**, ghi mã `MS-xx` trong nội dung. Issue Feedback không gắn GitHub milestone, vì milestone trên GitHub chỉ chứa task dev.
4. BA phân loại phản hồi theo [ke-hoach-quan-ly-san-pham.md](../10-product-management/ke-hoach-quan-ly-san-pham.md#42-đo-lường-và-thu-thập-phản-hồi):
   - Lỗi: tạo issue **Bug**, sửa trong mốc kế tiếp bằng giờ "sửa lỗi giữa các mốc" (`Q-08`, 4h mỗi mốc MS-02…MS-05).
   - Thay đổi phạm vi: tạo issue **Change request** `CR-xx`, đi theo quy trình ở [mục 5 kế hoạch quản trị](../11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi).
   - Làm rõ: trả lời ngay trong issue.
5. GitHub milestone `MS-01`…`MS-06` được đóng khi mọi task dev đạt DoD và kịch bản test của mốc đạt; việc client nghiệm thu mốc và UAT được theo dõi trong báo cáo mốc, không trên GitHub.

## Thay đổi kế hoạch

Kế hoạch chi tiết, chưa phải baseline đã duyệt, lưu trong `plans/master-schedule.xlsx`. Mỗi CR được duyệt ghi một dòng vào sheet `Change log` (phiên bản, ngày, CR, thay đổi, mốc bị ảnh hưởng, tổng giờ, giá), không ghi đè. Nếu giá đổi thì ghi thêm sheet `Phiên bản` của `quotation.xlsx`. Bản sửa hiện tại là `v1.2-draft` (25/11/2026), **Chờ PM rà soát**; giữ nguyên các dòng lịch sử, không coi nhãn `v1.0-baseline` là bằng chứng phê duyệt.

Trước khi gửi proposal cho khách lần đầu, nhóm sửa kế hoạch và báo giá trực tiếp; lịch sử sửa nằm trong PR. Rà soát nội bộ trước phát hành không phải là change request. Sau khi khách đã nhận proposal, thay đổi phạm vi, giá hoặc mốc do khách yêu cầu (thật hoặc `Mô phỏng`) mới đi qua CR và ghi Change log.
