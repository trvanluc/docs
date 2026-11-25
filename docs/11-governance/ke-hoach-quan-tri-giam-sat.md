# KẾ HOẠCH QUẢN TRỊ VÀ GIÁM SÁT DỰ ÁN

**PROJECT GOVERNANCE & MONITORING PLAN | DỰ ÁN UNISUPPORT – STUDENT SUPPORT MANAGEMENT SYSTEM**

Đơn vị thực hiện: Nhóm 3

## Mục đích và phạm vi

Kế hoạch này quy định cách báo cáo tình hình dự án từ người thực hiện lên quản lý dự án, rồi lên Nhà tài trợ dự án (Project Sponsor) và khách hàng Aurora University. Kế hoạch trả lời bốn câu hỏi: ai báo cáo cho ai, báo cáo khi nào, báo cáo những gì, và khi có vấn đề thì xử lý ra sao. Mục tiêu là để người quản lý luôn biết dự án đang đi đúng hay lệch kế hoạch, từ đó quyết định kịp thời.

Kế hoạch dựa trên cơ cấu vai trò và quy tắc làm việc trong Team Charter, lịch thực hiện trong Master Schedule, kế hoạch giờ công và chi phí trong ngân sách nội bộ và các cam kết với khách hàng trong Proposal.

## 1. Cơ cấu quản trị và tuyến báo cáo

Dự án có bốn cấp báo cáo. Thành viên thực hiện báo cáo cho người phụ trách lĩnh vực của mình; người phụ trách các lĩnh vực báo cáo cho Project Manager (PM); PM tổng hợp và báo cáo lên hai phía. Phía thứ nhất là Nhà tài trợ dự án (Project Sponsor), tức cấp trên trực tiếp của PM trong đơn vị thực hiện: người cung cấp nguồn lực, chịu chi phí và phê duyệt những quyết định vượt thẩm quyền của PM. Phía thứ hai là Aurora University, khách hàng của dự án.

![Tuyến báo cáo của dự án UniSupport](../08-project/plans/images/governance-reporting-lines.png)

*Hình 1. Tuyến báo cáo của dự án UniSupport*

### 1.1. Trách nhiệm báo cáo theo từng cấp

| Cấp | Vai trò | Báo cáo cho | Chịu trách nhiệm báo cáo về |
|---|---|---|---|
| Cấp 1 – Thực hiện | Frontend Developer 1, 2; Backend Developer 1, 2; DevOps Engineer | Technical Lead | Tiến độ từng công việc được giao, số giờ đã làm, vướng mắc kỹ thuật, tình trạng môi trường (DevOps). |
| Cấp 2 – Phụ trách lĩnh vực | Technical Lead (TL) | PM | Tiến độ phát triển chung, mã nguồn đang chờ review, vấn đề và rủi ro kỹ thuật. |
|  | Business Analyst (BA) | PM | Câu hỏi về yêu cầu chưa được giải đáp, yêu cầu thay đổi, các cập nhật PRD. |
|  | QA/QC Engineer | PM | Kết quả kiểm thử, số lỗi đang mở, kết quả đánh giá chất lượng của mốc. |
|  | UI/UX Designer | PM | Tiến độ thiết kế và các phản hồi về giao diện. |
| Cấp 3 – Quản lý dự án | Project Manager (PM) | Nhà tài trợ dự án | Tiến độ, chi phí so với ngân sách, rủi ro lớn và các đề xuất cần Nhà tài trợ dự án quyết định như bổ sung nhân sự hay điều chỉnh ngân sách. |
|  |  | Aurora University | Kết quả từng mốc, rủi ro ảnh hưởng đến khách hàng và các nội dung cần khách hàng xác nhận. |
| Cấp 4 – Nhà tài trợ, khách hàng | Nhà tài trợ dự án; Aurora University | — | Nhận báo cáo, đưa ra quyết định thuộc thẩm quyền và phản hồi cho PM. |

QA/QC báo cáo trực tiếp cho PM, không qua TL, để kết quả kiểm thử được đánh giá độc lập với nhóm phát triển. Khi PM vắng mặt, BA tạm thời nhận báo cáo và điều phối dự án. Nhiệm vụ chi tiết của từng vai trò được quy định trong Team Charter.

**Dữ liệu gốc luôn mở cho cấp trên.** Báo cáo được tổng hợp theo từng cấp, nhưng số liệu không bị lọc qua từng cấp. Mọi số liệu trong báo cáo đều dẫn về dữ liệu gốc trong repo và GitHub: trạng thái issue, lỗi và giờ thực tế trên GitHub Projects, [sổ rủi ro](../08-project/risk-register.md), nhật ký vấn đề (issue nhãn `issue-log`) và [Decision Log](../08-project/decision-log.md). PM và Nhà tài trợ dự án có quyền xem trực tiếp các dữ liệu này bất cứ lúc nào để tự kiểm tra, không phải chờ đến kỳ báo cáo.

### 1.2. Luồng thông tin từ trên xuống

Báo cáo đi lên để cấp trên nắm tình hình; theo chiều ngược lại, thông tin từ cấp trên được truyền xuống như sau:

1. **Tiếp nhận:** PM là đầu mối duy nhất nhận câu hỏi, yêu cầu và quyết định từ Nhà tài trợ dự án và Aurora University, để các thành viên không nhận những chỉ đạo khác nhau.
2. **Truyền đạt:** PM ghi quyết định vào [Decision Log](../08-project/decision-log.md) và thông báo cho người phụ trách lĩnh vực liên quan, nội dung khẩn qua Discord, nội dung thông thường tại buổi họp tuần. Với câu hỏi cần số liệu, PM yêu cầu người phụ trách cung cấp kèm thời hạn, rồi tổng hợp và trả lời cấp trên.
3. **Thực hiện và báo lại:** người phụ trách chuyển quyết định thành issue và phân công; người được giao xác nhận trong thời gian phản hồi của Team Charter. PM báo lại kết quả cho cấp trên trong kỳ báo cáo tiếp theo, khép kín vòng thông tin: báo cáo đi lên, quyết định đi xuống, kết quả được báo lại.

## 2. Quy trình báo cáo

Dự án sử dụng sáu loại báo cáo, từ cập nhật chi tiết hằng ngày đến báo cáo tổng hợp theo mốc. Bảng dưới đây tóm tắt; nội dung của từng loại được trình bày ở các mục tiếp theo.

| Loại báo cáo | Thời điểm | Người lập → người nhận | Hình thức |
|---|---|---|---|
| Họp nhanh và cập nhật hằng ngày | Họp nhanh 15 phút lúc 20h00; cập nhật công việc trước 22h00 | Từng thành viên → người phụ trách lĩnh vực và PM | Họp trực tuyến trên Discord; cập nhật trạng thái issue trên GitHub Projects |
| Báo cáo tuần | Trước buổi họp nhóm tối Chủ Nhật | Người phụ trách lĩnh vực → PM; PM tổng hợp thành báo cáo tình hình dự án | Báo cáo viết, trình bày tại buổi họp |
| Báo cáo tháng | Cuối mỗi tháng | PM → Nhà tài trợ dự án | Báo cáo viết ngắn gọn |
| Báo cáo mốc | Cuối giai đoạn khởi động và ngày cuối mỗi mốc `MS-01`…`MS-06` (master-schedule.xlsx sheet `Milestones`), cùng buổi demo cho client | PM → Aurora University và Nhà tài trợ dự án | Báo cáo viết, kèm biên bản đánh giá chất lượng của mốc |
| Báo cáo cảnh báo | Ngay khi phát hiện vấn đề | Người phát hiện → người phụ trách trực tiếp → PM | Tin nhắn Discord gắn tên người nhận, sau đó tạo GitHub Issue nhãn `issue-log` |
| Báo cáo tổng kết | Khi bàn giao | PM → Nhà tài trợ dự án; phần kết quả sản phẩm gửi Aurora University | Báo cáo viết; phần kết quả sản phẩm nằm trong hồ sơ bàn giao |

### 2.1. Họp nhanh và cập nhật hằng ngày

Vào 20h00 mỗi ngày làm việc, tức đầu khung giờ làm việc chung theo Team Charter, nhóm họp nhanh (daily stand-up) trên Discord trong tối đa 15 phút. PM chủ trì; mỗi thành viên lần lượt trả lời ngắn gọn ba câu hỏi:

1. Từ lần họp trước đến nay mình đã làm xong những gì?
2. Hôm nay mình sẽ làm gì?
3. Mình đang gặp khó khăn hay vướng mắc gì cần người khác hỗ trợ?

Buổi họp nhanh chỉ để nắm tình hình, không giải quyết vấn đề tại chỗ. Vướng mắc được PM ghi lại; người phụ trách lĩnh vực trao đổi riêng với người liên quan ngay sau buổi họp. Thành viên vắng mặt gửi câu trả lời cho ba câu hỏi bằng tin nhắn trong kênh chung trước buổi họp. Vấn đề nghiêm trọng được báo cáo theo hình thức cảnh báo tại mục 2.5.

Trước 22h00, mỗi thành viên cập nhật trạng thái issue trên GitHub Projects theo đúng 5 trạng thái của Team Charter mục 4.3 (To do, Doing, Review, QA verify, Done), đồng thời cộng số giờ đã làm vào trường **Giờ thực tế** của issue trên GitHub Projects. Số giờ này là nguồn dữ liệu để PM tính chi phí thực tế và so sánh với kế hoạch. Giờ thực tế của đội thực thi là `Mô phỏng`.

### 2.2. Báo cáo tuần

Trước buổi họp nhóm tối Chủ Nhật, mỗi người phụ trách lĩnh vực gửi phần báo cáo của mình theo nội dung đã nêu ở mục 1.1; riêng QA/QC báo cáo các chỉ số chất lượng theo Kế hoạch quản lý chất lượng. Theo Team Charter, PM gửi chương trình họp trước buổi họp 4 giờ.

PM tổng hợp các phần trên thành Báo cáo tình hình dự án tuần theo mẫu tại mục 6.2. Tại buổi họp, nhóm cũng rà soát sổ rủi ro theo mục 3.2. Kết luận và các việc cần làm sau buổi họp được ghi vào biên bản họp, có người phụ trách và thời hạn.

### 2.3. Báo cáo tháng cho Nhà tài trợ dự án

Cuối mỗi tháng, PM gửi Nhà tài trợ dự án một báo cáo ngắn gọn, đủ để Nhà tài trợ dự án nắm tình hình mà không cần đọc chi tiết từng công việc. Báo cáo gồm:

- **Tiến độ:** dự án đang ở mốc nào, các mốc đã hoàn thành, dự báo thời điểm bàn giao so với Master Schedule.
- **Chi phí:** số giờ công và chi phí nhân sự thực tế đến thời điểm báo cáo, so với ngân sách nhân sự kế hoạch. Chi phí thực tế được tính bằng số giờ thực tế của từng vai trò nhân với đơn giá giờ trong kế hoạch ngân sách nội bộ.
- **Chất lượng:** kết luận đánh giá chất lượng của các mốc đã qua và số lỗi nghiêm trọng còn mở.
- **Rủi ro và khó khăn lớn:** những vấn đề có thể ảnh hưởng đến tiến độ, chi phí hoặc quan hệ với khách hàng.
- **Đề xuất cần quyết định:** ví dụ bổ sung hoặc điều chuyển nhân sự, sử dụng chi phí dự phòng, điều chỉnh phạm vi hoặc thời hạn với khách hàng.
- **Tình hình với khách hàng:** các nội dung đã được Aurora University xác nhận, các phản hồi đang chờ, và các khoản thanh toán theo hợp đồng.

### 2.4. Báo cáo mốc

Khi kết thúc mỗi mốc `MS-xx` trong Master Schedule, PM gửi Aurora University báo cáo mốc, đồng thời gửi bản sao cho Nhà tài trợ dự án. Nội dung gồm:

- Kết quả đạt được so với phần giao được và điều kiện nghiệm thu của mốc (sheet `Milestones`), kết quả các kịch bản `TS-xx` của mốc và feedback của client sau demo.
- Kết luận đánh giá chất lượng của mốc, theo Kế hoạch quản lý chất lượng.
- Tiến độ tổng thể và dự báo thời điểm bàn giao.
- Số giờ công đã sử dụng so với kế hoạch.
- Rủi ro và vấn đề có thể ảnh hưởng đến khách hàng.
- Những nội dung cần Aurora University xác nhận hoặc cung cấp, ví dụ thông tin nghiệp vụ, điều kiện hạ tầng hoặc ý kiến phản hồi.
- Kế hoạch của mốc tiếp theo.

### 2.5. Báo cáo cảnh báo

Một số tình huống phải được báo cáo ngay, không chờ đến kỳ báo cáo tuần:

- Có nguy cơ trễ hạn công việc. Theo Team Charter, thành viên báo PM ngay khi phát hiện, ưu tiên trước hạn 24–48 giờ.
- Phát hiện lỗi nghiêm trọng, tức lỗi làm gián đoạn chức năng chính.
- Có vấn đề khiến công việc của người khác không thể tiếp tục.
- Xuất hiện rủi ro mới hoặc yêu cầu thay đổi phạm vi.
- Thông tin, phản hồi hoặc hạ tầng từ phía Aurora University bị chậm so với kế hoạch.

Báo cáo cảnh báo cần nêu rõ bốn điều: vấn đề là gì, ảnh hưởng đến công việc và mốc nào, đề xuất cách xử lý, và cần ai quyết định. Báo cáo được gửi qua kênh khẩn cấp trên Discord; theo Team Charter, người nhận phải phản hồi trong 1–2 giờ. Nếu vấn đề có thể làm chậm tiến độ hoặc tăng chi phí, PM báo ngay cho Nhà tài trợ dự án. Nếu vấn đề ảnh hưởng đến cam kết với khách hàng, PM chủ động thông báo cho Aurora University, đúng như Proposal đã cam kết.

### 2.6. Báo cáo tổng kết

Khi bàn giao, PM lập báo cáo tổng kết dự án gồm: kết quả so với kế hoạch về phạm vi, tiến độ, giờ công và chi phí; kết quả kiểm thử và nghiệm thu nội bộ; các vấn đề còn tồn đọng; và bài học kinh nghiệm của nhóm. Báo cáo được gửi Nhà tài trợ dự án; phần kết quả sản phẩm nằm trong hồ sơ bàn giao cho Aurora University.

## 3. Chỉ số giám sát và ngưỡng cảnh báo

### 3.1. Ngưỡng cảnh báo

Mỗi báo cáo tuần, báo cáo tháng và báo cáo mốc đánh giá bốn lĩnh vực theo ba mức: Xanh là đúng kế hoạch, Vàng là có sai lệch nhưng còn kiểm soát được, Đỏ là cần PM xử lý ngay. Trạng thái chung của dự án lấy theo lĩnh vực có mức xấu nhất.

| Lĩnh vực | Chỉ số và cách đo | Xanh | Vàng | Đỏ |
|---|---|---|---|---|
| Tiến độ | Tỷ lệ issue chuyển Done đúng hạn (trường ngày hạn của issue trên GitHub Projects); dự báo ngày kết thúc mốc so với Master Schedule. | Tỷ lệ đúng hạn đạt mức kỳ vọng trong Team Charter và mốc dự kiến kết thúc đúng ngày. | Tỷ lệ đúng hạn thấp hơn mức kỳ vọng, nhưng mốc vẫn dự kiến kết thúc đúng ngày. | Mốc dự kiến kết thúc trễ so với Master Schedule. |
| Giờ công và chi phí | Dự báo tổng giờ = giờ thực tế đã sử dụng + giờ kế hoạch của phần việc còn lại; chi phí tính theo đơn giá giờ của từng vai trò. So sánh với ngân sách trong kế hoạch ngân sách nội bộ. | Dự báo không vượt ngân sách cơ sở. | Dự báo vượt ngân sách cơ sở nhưng không vượt tổng ngân sách, tức đang dùng đến phần dự phòng. | Dự báo vượt tổng ngân sách gồm cả dự phòng. |
| Chất lượng | Số lỗi nghiêm trọng đang mở; các chỉ số và kết luận đánh giá chất lượng theo Kế hoạch quản lý chất lượng. | Không có lỗi nghiêm trọng đang mở; các chỉ số chất lượng đạt ngưỡng. | Có lỗi nghiêm trọng đang được sửa hoặc có chỉ số chưa đạt ngưỡng, chưa đến cuối mốc. | Còn lỗi nghiêm trọng khi kết thúc mốc, hoặc mốc không đạt đánh giá chất lượng. |
| Phạm vi | Số issue `CR-xx` (nhãn `change-request`) đang mở. | Không có yêu cầu thay đổi. | Có yêu cầu thay đổi đang đánh giá. | Có thay đổi ảnh hưởng đến ngày bàn giao hoặc chi phí, cần Aurora University xác nhận. |

Mức kỳ vọng về tỷ lệ đúng hạn lấy theo Team Charter; ngân sách cơ sở, phần dự phòng và tổng ngân sách lấy theo kế hoạch ngân sách nội bộ hiện hành. Khi các tài liệu này được điều chỉnh, ngưỡng cảnh báo áp dụng theo giá trị mới.

**Hành động theo từng mức:**

- **Xanh:** tiếp tục thực hiện theo kế hoạch.
- **Vàng:** người phụ trách lĩnh vực đề xuất hướng khắc phục; PM theo dõi kết quả trong báo cáo tuần tiếp theo.
- **Đỏ:** PM xử lý ngay bằng cách điều chỉnh phân công, thứ tự công việc hoặc sử dụng giờ dự phòng. PM báo cáo Nhà tài trợ dự án khi cần bổ sung nguồn lực hoặc chi phí. Nếu ảnh hưởng đến mốc, phạm vi hoặc chi phí đã cam kết với khách hàng, PM thông báo Aurora University và xử lý theo quy trình kiểm soát thay đổi tại mục 5.

### 3.2. Giám sát rủi ro

Ngoài các vấn đề đã xảy ra, PM theo dõi những rủi ro có thể xảy ra trong [risk-register.md](../08-project/risk-register.md). Mỗi rủi ro có mã `R-xx` và ghi: mô tả, khả năng và tác động (thang 1–5), mức = khả năng × tác động, owner, phòng ngừa, ứng phó, dấu hiệu báo trước, trạng thái và mốc/FR liên quan.

Sổ rủi ro ban đầu được lập từ cột rủi ro chính trong kế hoạch ngân sách nội bộ (R-01 phân quyền, R-02 thời hạn xử lý, R-03 đồng bộ trạng thái Ticket) và bổ sung các rủi ro tích hợp, client, hạ tầng, thiếu người, dữ liệu UAT. Tại buổi họp tuần, nhóm bổ sung rủi ro mới, cập nhật mức độ và đóng các rủi ro không còn khả năng xảy ra. Rủi ro đã xảy ra được chuyển trạng thái `Đã xảy ra`, mở issue nhãn `issue-log` và xử lý theo mục 4; giờ xử lý lấy từ dự phòng `Q-11` (40h) do PM duyệt. Báo cáo tháng nêu các rủi ro mức Cao (≥ 15).

### 3.3. Chỉ số giá trị đạt được (EVM)

Cuối mỗi mốc, PM tính hai chỉ số theo phương pháp giá trị đạt được (Earned Value Management – EVM) để đánh giá cùng lúc tiến độ và chi phí, đơn vị là giờ công. Giá trị kế hoạch (PV) là số giờ kế hoạch của phần việc lẽ ra phải xong; giá trị đạt được (EV) là số giờ kế hoạch của phần việc thực tế đã xong đúng DoD; chi phí thực tế (AC) là số giờ đã sử dụng.

| Chỉ số | Công thức | Ý nghĩa |
|---|---|---|
| SPI | EV ÷ PV | Từ 1 trở lên: đúng hoặc nhanh hơn kế hoạch. Dưới 1: chậm so với kế hoạch. |
| CPI | EV ÷ AC | Từ 1 trở lên: không vượt số giờ kế hoạch. Dưới 1: tốn nhiều giờ hơn kế hoạch. |

Khi SPI hoặc CPI dưới 1, PM nêu nguyên nhân và hướng khắc phục trong báo cáo mốc.

## 4. Chuyển cấp vấn đề và quyền quyết định

Khi gặp vấn đề, thành viên liên hệ người phụ trách trực tiếp của lĩnh vực trước. Vấn đề chỉ được chuyển lên cấp tiếp theo khi người phụ trách trực tiếp không xử lý được, hoặc khi vấn đề ảnh hưởng đến tiến độ, phạm vi hay chất lượng. Tuyến chuyển cấp chi tiết theo từng loại vấn đề và các quyết định trong nội bộ nhóm được quy định trong Team Charter. Bảng dưới đây nêu các cấp quyết định của dự án:

| Loại quyết định | Người quyết định |
|---|---|
| Vấn đề trong nội bộ nhóm: cách triển khai, kỹ thuật, phân công, thời hạn | Theo Team Charter; PM quyết định khi bế tắc hoặc khẩn cấp |
| Sử dụng giờ dự phòng trong phạm vi tổng ngân sách | PM |
| Bổ sung nhân sự, vượt ngân sách nhân sự kế hoạch | Nhà tài trợ dự án, theo đề xuất của PM |
| Thay đổi phạm vi, chi phí hoặc tiến độ đã thống nhất với khách hàng | Aurora University xác nhận bằng văn bản |

Mọi quyết định quan trọng được ghi vào [Decision Log](../08-project/decision-log.md) để các thành viên tra cứu khi cần.

## 5. Kiểm soát thay đổi

Mọi thay đổi về phạm vi, chi phí hoặc tiến độ phải được đánh giá và xác nhận trước khi thực hiện, theo cam kết trong Proposal và ràng buộc dự án trong PRD. Quy trình gồm năm bước:

1. **Ghi nhận.** Người đề xuất, có thể là thành viên nhóm hoặc Aurora University (`Mô phỏng`), gửi yêu cầu cho BA. BA tạo GitHub Issue theo mẫu **Change request**, tiêu đề `[CR-xx]`, nêu nội dung, lý do và link issue Feedback gốc nếu có.
2. **Đánh giá ảnh hưởng.** BA phối hợp với TL điền bảng đánh giá tác động trong issue: phạm vi (FR bị ảnh hưởng), effort theo vai trò, giá (giờ × đơn giá ở `quotation.xlsx` sheet `Đơn giá`), timeline (mốc bị dời), rủi ro mới, kịch bản test cần sửa. CR không dùng dự phòng `Q-11`; phần tăng được báo giá riêng. Về thời gian: CR không quá 16h chỉ được đề xuất làm trong mốc kế tiếp mà không dời hạn khi đã phân bổ đủ giờ từng vai trò vào ngày/slot thực sự còn trống trong `Lịch task-vai trò`, `Tải ngày` và `Năng lực tuần`, không vượt 4h/ngày hoặc 20h/tuần/vai trò, không nằm trước predecessor/gate đầu vào và vẫn đủ QA/regression trước giao. `Resources` chỉ đối soát tổng, không chứng minh riêng tính khả thi; năng lực trống không phải effort đã mua và không thay cho báo giá CR. Nếu không thỏa các điều kiện này thì ghi rõ mốc bị dời và ngày mới ([master-plan.md, mục "Dự phòng cho thay đổi và rủi ro"](../08-project/master-plan.md#dự-phòng-cho-thay-đổi-và-rủi-ro)).
3. **Quyết định.** PM quyết định trong nội bộ. Nếu thay đổi ảnh hưởng đến phạm vi, chi phí hoặc tiến độ đã thống nhất với khách hàng, PM gửi Aurora University xác nhận bằng văn bản trước khi thực hiện.
4. **Cập nhật kế hoạch.** Khi thay đổi được chấp thuận, BA cập nhật PRD và kịch bản test; PM điều phối người phụ trách theo Team Charter cập nhật `quotation.xlsx` (sheet `Phiên bản`, dùng chung cho Proposal), `plans/wbs.xlsx` (sheet `WBS` và `Change log`), `plans/ngan-sach-noi-bo.xlsx` (sheet `Resource`, `BẢNG CHI PHÍ NHÂN SỰ` và `Change log`), `plans/master-schedule.xlsx` (Gantt, `Resources`, `Milestones`, `Danh sách issue`, `Lịch task-vai trò`, `Phân bổ WP`, `Tải ngày`, `Năng lực tuần`, `Change log`), milestone và issue/trường Hạn trên GitHub Projects, sổ rủi ro nếu cần, và lưu Proposal gửi lại vào `08-project/sent/` nếu đổi phạm vi, giá hoặc mốc. Mỗi lịch sử ghi phiên bản, ngày, thay đổi, issue CR và người duyệt kèm bằng chứng; bản chưa duyệt ghi rõ chờ duyệt. Với file không bị ảnh hưởng, checklist CR ghi "Không đổi" và lý do, không tạo số liệu mới. Mọi cập nhật được liệt kê trong mục "Đã cập nhật" của issue CR (link PR). Quyết định được ghi vào [Decision Log](../08-project/decision-log.md).
5. **Theo dõi.** Thay đổi được theo dõi trong báo cáo tuần cho đến khi hoàn thành; issue CR đóng khi mọi mục "Đã cập nhật" có link PR đã merge.

Yêu cầu tính năng mới phát sinh trong thời gian bảo hành không thuộc phạm vi bảo hành và cũng được xử lý theo quy trình này.

## 6. Nhật ký quản trị và mẫu báo cáo

### 6.1. Nhật ký quản trị

| Nhật ký | Nội dung | Người cập nhật | Nơi lưu |
|---|---|---|---|
| Giờ thực tế | Số giờ đã làm theo từng issue. | Từng thành viên; PM tổng hợp | Trường **Giờ thực tế** trên GitHub Projects |
| Nhật ký vấn đề | Mô tả vấn đề, ngày phát hiện, ảnh hưởng, người xử lý, thời hạn, trạng thái. | PM | GitHub Issues nhãn `issue-log` |
| Sổ rủi ro | Mã R-xx, mô tả, khả năng, tác động, mức, owner, phòng ngừa, ứng phó, dấu hiệu báo trước, trạng thái. | PM; owner từng rủi ro | [risk-register.md](../08-project/risk-register.md) |
| Decision Log | Ngày, nội dung quyết định, người quyết định, lý do, tài liệu đã cập nhật. | PM | [decision-log.md](../08-project/decision-log.md) |
| Biên bản họp tuần | Nội dung thảo luận, việc cần làm, người phụ trách, thời hạn. | Thành viên ghi biên bản theo lượt | GitHub Issues nhãn `meeting` |
| Báo cáo tuần, tháng và báo cáo mốc | Theo mục 2.2, 2.3, 2.4 và mẫu tại mục 6.2. | PM | GitHub Issues nhãn `report` (số liệu ghi `Mô phỏng`) |

### 6.1a. Nhãn GitHub

Bộ nhãn chính thức của repo (nơi gốc là bảng này). Mẫu issue trong `.github/ISSUE_TEMPLATE/` tự gắn nhãn loại; người tạo issue gắn thêm nhãn module. Các chỉ số ở mục 3.1 lọc theo nhãn này.

| Nhãn | Dùng cho | Gắn bởi |
| --- | --- | --- |
| `task` | Parent task trong kế hoạch, để open | Mẫu Parent task |
| `bug` | Lỗi | Mẫu Bug |
| `feedback` | Phản hồi của client/người dùng (thật hoặc `Mô phỏng`) | Mẫu Feedback |
| `change-request` | Yêu cầu thay đổi `CR-xx`; chỉ số Phạm vi đếm issue mở có nhãn này | Mẫu Change request |
| `issue-log` | Vấn đề hoặc rủi ro đã xảy ra (nhật ký vấn đề) | PM |
| `report` | Báo cáo tuần, tháng, mốc | PM |
| `meeting` | Biên bản họp | Người ghi biên bản |
| `M01`, `M02`, `M03` | Task thuộc phân hệ Sinh viên, Nhân viên, Quản lý (theo mã FR trong task) | Người tạo task |
| `chung` | Task dùng chung hoặc cấp dự án: đăng nhập, NFR, tích hợp, kiểm thử, triển khai | Người tạo task |

Các nhãn `status:*` có sẵn trên repo không dùng; trạng thái task theo 5 cột của GitHub Projects (Team Charter mục 4.3).

### 6.2. Mẫu và ví dụ báo cáo tuần

Báo cáo tình hình dự án tuần được lập theo mẫu dưới đây. Cột Ví dụ minh họa báo cáo tuần 02/11–08/11/2026 của `MS-02`; toàn bộ số liệu là `Mô phỏng`.

| Mục | Nội dung cần điền | Ví dụ |
|---|---|---|
| Kỳ báo cáo | Tuần báo cáo; mốc hiện tại trong Master Schedule; người lập. | Tuần 02/11–08/11/2026; MS-02 – Tiếp nhận Ticket; PM lập. (`Mô phỏng`) |
| Trạng thái chung | Xanh, Vàng hoặc Đỏ, lấy theo lĩnh vực có mức xấu nhất ở mục 3.1. | Vàng, do tiến độ ở mức Vàng. |
| Tiến độ | Số công việc hoàn thành; tỷ lệ đúng hạn; công việc đang chậm; dự báo ngày kết thúc mốc. | Vàng: 5/7 công việc đúng hạn (71%, thấp hơn mức kỳ vọng 85% trong Team Charter); chức năng sinh mã Ticket (#133) chậm 2 ngày; MS-02 vẫn dự kiến kết thúc đúng ngày 12/11. |
| Giờ công và chi phí | Giờ thực tế trong tuần và lũy kế; chi phí tương ứng; dự báo so với ngân sách cơ sở và tổng ngân sách. | Xanh: tuần này 52 giờ, lũy kế 330 giờ (khoảng 98 triệu đồng); dự báo 818 giờ, chưa vượt ngân sách cơ sở 823 giờ (tổng gồm dự phòng 885 giờ). |
| Chất lượng | Số lỗi đang mở theo mức độ; công việc chờ xác minh; các chỉ số chất lượng. | Xanh: không có lỗi nghiêm trọng; 3 lỗi thông thường đang sửa; 4 công việc chờ xác minh. |
| Phạm vi | Yêu cầu thay đổi mới, đang đánh giá hoặc đã quyết định. | Xanh: không có yêu cầu thay đổi. |
| Rủi ro và vấn đề | Rủi ro ở mức cao; vấn đề mới hoặc chưa xử lý xong, người phụ trách, thời hạn. | R-01 phân quyền (mức 15, Cao): đã bổ sung test case truy cập chéo cho hàng chờ. Chậm sinh mã Ticket: TL hỗ trợ BE1, hạn mới 10/11. |
| Cần quyết định | Nội dung cần PM, nhóm, Nhà tài trợ dự án hoặc Aurora University quyết định. | Không có. |
| Kế hoạch tuần tới | Các công việc chính và mục tiêu của tuần tiếp theo. | Hoàn thành theo dõi Ticket và thông báo; bắt đầu mức ưu tiên và thời hạn xử lý (MS-03); regression MS-01, MS-02 trước demo cuối mốc 12/11. |

## 7. Trạng thái rà soát trước phát hành — 25/11/2026

Bộ hồ sơ `v1.2-draft` **Chờ PM rà soát**, **chưa gửi khách**, chưa có baseline được khách phê duyệt. Đề xuất gửi 30/11/2026, mục tiêu xác nhận 04/12 và chỉ khởi động 07/12/2026 khi khách xác nhận Proposal/phạm vi, đầu mối và nguồn lực. Lịch dự kiến MS-06 kết thúc 18/05/2027; Ngoài cuối tuần, loại 01/01/2027, 30/04 và 01/05/2027; 08–12/02, 16/04 và nghỉ bù 03/05/2027 là giả định đóng cửa trường phục vụ lập kế hoạch, chờ trường xác nhận (16/04 chưa xác minh lịch âm chính thức), không phải lịch nghỉ chính thức đã được duyệt. Đổi giả định phải tính lại lịch ngày làm việc trước baseline; xem [bộ mốc](../08-project/milestones-and-timeline.md).

Ví dụ `Mô phỏng` tuần 02/11–08/11/2026 ở mục 6.2 được giữ như ví dụ lịch sử theo lịch đề xuất cũ, không phải báo cáo đã thực hiện hoặc lịch hiện hành. Không dùng các số liệu/ngày trong ví dụ làm baseline mới.

PR #199/#202 không có recorded approval trước merge như Charter yêu cầu: ghi nhận khoảng trống quy trình, không tạo/backdate approval, không dùng review sau merge để tuyên bố lịch sử đã tuân thủ. Các PR tiếp theo phải có tối thiểu một reviewer đủ chuyên môn approve trước merge, lưu link và thời điểm bằng chứng; thiếu thì dừng merge. Xem [kiểm soát approval](../08-project/team-charter.md#kiểm-soát-approval-trước-merge).

Phía trường, Trưởng bộ phận/phụ trách điều phối hỗ trợ sinh viên được **đề xuất, chờ xác nhận** làm chủ sở hữu sản phẩm, nhận backlog, ưu tiên, roadmap/đợt phát hành và rà soát chỉ số; không phải Sponsor bên giao hàng hoặc nhóm quyền ứng dụng mới. BA bàn giao theo thỏa thuận và kết thúc trách nhiệm sau hỗ trợ/bảo hành; CNTT trường vận hành kỹ thuật. Các quyền ký xác nhận khách hàng vẫn phải do trường chỉ định; không coi đề xuất đầu mối là đã được ủy quyền ký.

Ngày 25/11/2026 đã đồng bộ và đọc lại 6 milestone, ngày/DoD/nghiệm thu tăng dần của 58 parent task, đủ membership và 58 Hạn trên GitHub Projects qua [PR #203](https://github.com/trvanluc/docs/pull/203). State/label/assignee/checklist, Status hiện hữu và giờ thực tế được giữ nguyên; 4 membership mới không tự gán trạng thái hoàn thành. Đây là đồng bộ kế hoạch nháp, chưa phải approval hoặc tiến độ thực. Mỗi lần thay đổi sau khi được phép cần đối chiếu 58 parent task, 885h tổng, 540h chức năng và giá 300 triệu; không suy diễn giờ gói dùng chung thành giờ riêng từng issue. Kiểm tải từng vai trò ở từng task/ngày/tuần và tuần nghỉ trước khi chốt; không tự giảm giờ để hợp lịch.
