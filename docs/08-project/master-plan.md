# Master Plan

Trang này giải thích các quyết định của kế hoạch. Số liệu (ngày, effort, nguồn lực) chỉ nằm trong Excel:

| Phần | Nơi gốc |
| --- | --- |
| Milestones (mã, ngày, phần giao được, kịch bản kiểm tra, điều kiện nghiệm thu) | [plans/master-schedule.xlsx](plans/master-schedule.xlsx), sheet `Milestones` |
| Gantt (vẽ từ cột Bắt đầu/Kết thúc, không tô tay) | `master-schedule.xlsx`, sheet `Master Schedule` |
| WBS | [plans/wbs.xlsx](plans/wbs.xlsx), sheet `WBS` (mỗi dòng có mốc, FR, `Q-xx`, effort, owner, ngày bắt đầu/kết thúc; tổng 885h) và `Từ điển WBS`; việc chi tiết theo mốc: `master-schedule.xlsx` sheet `Chi tiết công việc` |
| Resources | `master-schedule.xlsx` sheet `Resources`: đội thực thi `Mô phỏng` (vai trò, số người, giờ/tuần), giờ theo vai trò × giai đoạn, tỷ lệ sử dụng để kiểm quá tải; nguồn giờ: [plans/ngan-sach-noi-bo.xlsx](plans/ngan-sach-noi-bo.xlsx) sheet `Resource` |
| Change log | `master-schedule.xlsx` sheet `Change log` |
| Giá | [quotation.xlsx](quotation.xlsx) |
| Rủi ro | [risk-register.md](risk-register.md) |

## Thời điểm của dự án

**Quyết định:** dự án đang ở trước ngày khởi động. Proposal `v1.0` đang được hoàn thiện theo góp ý của giảng viên và **chưa gửi khách**, nên [sent/](sent/) chưa có bản nào. Lịch 05/10/2026–08/01/2027 là **lịch đề xuất** trong Proposal, giả định khách duyệt và khởi động ngày 05/10/2026.

**Lý do:** đây là dự án môn học; chuẩn của môn chấm tài liệu, kế hoạch và quy trình, không yêu cầu thực hiện. Nhóm **không mô phỏng tiến độ thực hiện**, vì vậy:

- Mọi parent task trên GitHub để open. Chúng là việc trong kế hoạch, chưa có task nào được làm.
- Không có báo cáo tiến độ hay số giờ thực tế. Ví dụ báo cáo tuần trong [kế hoạch quản trị mục 6.2](../11-governance/ke-hoach-quan-tri-giam-sat.md#62-mẫu-và-ví-dụ-báo-cáo-tuần) ghi `Mô phỏng`, chỉ để minh hoạ mẫu.
- Ngày thực tế trên lịch không được dùng để so tiến độ với kế hoạch.

Nếu khách duyệt muộn hơn 05/10/2026, toàn bộ lịch dời theo ngày khởi động thực tế (Proposal mục 3.1: thời gian chờ khách được điều chỉnh vào tiến độ). Việc dời lịch ghi một dòng vào sheet `Change log`.

## Cách chia milestone

Dự án có **giai đoạn khởi động** (05/10–14/10/2026) và **6 mốc** `MS-01`…`MS-06` chia theo **luồng đi của một Ticket** (nền tảng → tiếp nhận → xử lý → trả kết quả → quản trị → tích hợp và bàn giao), không theo phân hệ hay theo tầng kỹ thuật. Lý do:

- Mỗi mốc giao cho client một phần phần mềm **chạy được trên staging**, gồm cả màn hình Sinh viên lẫn Nhân viên của cùng một đoạn luồng. Client kiểm tra được ngay giá trị nghiệp vụ, không phải chờ "xong phân hệ Sinh viên" mới thấy Ticket được xử lý.
- Giai đoạn khởi động (chốt phạm vi, prototype tương tác 3 vai trò, thiết kế kỹ thuật) **không phải milestone** vì chưa giao phần mềm chạy được. Client vẫn duyệt prototype ở cuối giai đoạn này: đây là điểm dừng rẻ nhất để đổi ý về luồng màn hình trước khi code.
- **MS-01 (Nền tảng hệ thống) được giữ làm mốc đầu, dù sinh viên và nhân viên chưa làm được việc nghiệp vụ nào.** Sau MS-01, người quản lý phía khách đăng nhập bản staging và tự tạo tài khoản, phòng ban, nhóm vấn đề và phòng ban tiếp nhận trên phần mềm thật. Đây là dữ liệu mà luồng Ticket ở MS-02 cần. Client cũng kiểm tra được ngay việc chặn truy cập sai quyền (R-01, rủi ro mức Cao).
  - Đánh đổi: phân quyền được làm chắc trước khi có dữ liệu Ticket, đổi lại sinh viên thấy giá trị nghiệp vụ muộn hơn khoảng 2 tuần (cuối MS-02, 12/11/2026).
  - Phương án đã cân nhắc: đưa một lát mỏng "sinh viên gửi Ticket, nhân viên thấy trong hàng chờ" vào MS-01. Nhóm không chọn vì phương án này phải làm luồng Ticket trên phân quyền chưa xong, dễ phải làm lại khi phân quyền thay đổi.
- Thứ tự mốc khớp thứ tự ưu tiên FR trong PRD (xem [03-modules/README.md](../03-modules/README.md#mức-ưu-tiên-fr)): FR mức Cao nằm ở `MS-01`…`MS-04`. `MS-05` có Dashboard và báo cáo (mức Cao) nhưng phải đi sau vì cần dữ liệu của vòng đời Ticket đầy đủ.

Phần giao được, kịch bản kiểm tra (`TS-xx`) và điều kiện nghiệm thu của từng `MS-xx` ở sheet `Milestones`; bản tóm tắt ở [milestones-and-timeline.md](milestones-and-timeline.md).

## Phụ thuộc giữa các milestone

- Khởi động → `MS-01`: phạm vi, prototype và thiết kế dữ liệu/phân quyền đã duyệt.

- `MS-01` → mọi mốc sau: đăng nhập, phân quyền, phòng ban và Category là điều kiện để tạo Ticket.
- `MS-02` → `MS-03`: xử lý chỉ bắt đầu khi Ticket đã được tiếp nhận và có người phụ trách. Hai mốc chồng nhau 04/11–12/11/2026: phần ưu tiên/thời hạn (BE2, FE2) bắt đầu ngay khi hàng chờ và phân công xong.
- `MS-03` → `MS-04`: ghi kết quả cần Ticket ở `IN_PROGRESS` với thời hạn đã tính đúng.
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

`MS-06` (14 ngày làm việc, trừ ngày nghỉ 01/01/2027 ở sheet `Ngày nghỉ`) có 146h kế hoạch: TL 16h, BA 21h, UI/UX 2h, FE1 7h, FE2 7h, BE1 14h, BE2 14h, QA 40h, DevOps 14h, PM 11h (sheet `Resources`).

Lỗi phát hiện ở MS-01…MS-05 được sửa trong mốc kế tiếp bằng 16h sửa lỗi giữa các mốc, không chờ tới MS-06; vì vậy MS-06 chỉ còn 16h sửa lỗi sau UAT. Nếu lỗi của một mốc vượt 4h, phần vượt lấy từ năng lực còn trống của mốc kế tiếp (xem mục dưới) hoặc từ buffer kỹ thuật của module đó.

Bảo hành **có tính vào giá**: Proposal cam kết sửa lỗi kỹ thuật miễn phí 30 ngày, nên phần công này nằm trong 300 triệu (`Q-10`, 26h ≈ 8,9 triệu).

## Dự phòng cho thay đổi và rủi ro

- **62h dự phòng**, tách khỏi effort sửa lỗi ở trên:
  - 22h buffer kỹ thuật trong các gói chức năng (cột K sheet `Resource`), nằm trong `Q-01`…`Q-03`.
  - 40h dự phòng rủi ro dự án (`Q-11`), dùng khi một rủi ro trong [risk-register.md](risk-register.md) xảy ra.
- Dự phòng **có tính vào giá**. PM quyết định dùng dự phòng trong phạm vi tổng ngân sách ([kế hoạch quản trị](../11-governance/ke-hoach-quan-tri-giam-sat.md#4-chuyển-cấp-vấn-đề-và-quyền-quyết-định)).
- **CR không lấy từ dự phòng.** Mọi CR làm tăng phạm vi được đánh giá tác động và báo giá riêng theo cùng đơn giá trong `quotation.xlsx`, sheet `Đơn giá`.
- **Năng lực cho CR: dùng năng lực còn trống của đội.** Mỗi vai trò có 20h/tuần cho dự án nhưng kế hoạch chỉ dùng 2–88% tuỳ mốc. Phần còn trống theo vai trò × mốc nằm ở `master-schedule.xlsx` sheet `Resources`, bảng "Năng lực còn trống". Cách xếp một CR đã được khách duyệt:
  1. BA và TL ước lượng giờ CR theo từng vai trò, **gồm cả giờ QA để test và regression phần bị ảnh hưởng**.
  2. Nếu tổng giờ CR không quá 16h, và giờ của từng vai trò không vượt năng lực còn trống của vai trò đó ở **mốc kế tiếp**: CR được làm trong mốc kế tiếp, **không dời ngày mốc**. Với MS-02 và MS-03 (chồng nhau 7 ngày), kiểm thêm bảng tỷ lệ sử dụng MS-02 + MS-03 không vượt 100%.
  3. Nếu không thoả bước 2: dời mốc bị ảnh hưởng. PM ghi phiên bản mới vào sheet `Change log` và gửi khách xác nhận ngày mới cùng báo giá CR.
  4. PM quyết định cách xếp theo quy trình CR ([kế hoạch quản trị mục 5](../11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi), bước 2–3).

  Đánh đổi: giữ được ngày bàn giao khi khách đổi ý nhỏ, đổi lại đội làm gần hết năng lực ở mốc có CR. Ngưỡng 16h giữ cho một CR không chiếm quá khoảng 1/3 năng lực còn trống của vai trò bận nhất (BE1 ở MS-02 còn khoảng 15h).
- Tổng: 823h cơ sở + 62h dự phòng = **885h**. Chi phí nội bộ khoảng 263,7 triệu (sheet `BẢNG CHI PHÍ NHÂN SỰ`); giá bán 300 triệu (chênh lệch ≈ 12% cho chi phí chung, công cụ và lợi nhuận).

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

Kế hoạch đã chốt lưu trong `plans/master-schedule.xlsx`. Mỗi CR được duyệt ghi một dòng vào sheet `Change log` (phiên bản, ngày, CR, thay đổi, mốc bị ảnh hưởng, tổng giờ, giá), không ghi đè. Nếu giá đổi thì ghi thêm sheet `Phiên bản` của `quotation.xlsx`. Bản hiện tại là `v1.0` (14/11/2026).

Trước khi gửi proposal cho khách lần đầu, nhóm sửa kế hoạch và báo giá trực tiếp; lịch sử sửa nằm trong PR. Sửa theo feedback của giảng viên không phải là change request. Sau khi khách đã nhận proposal, thay đổi phạm vi, giá hoặc mốc do khách yêu cầu (thật hoặc `Mô phỏng`) mới đi qua CR và ghi Change log.
