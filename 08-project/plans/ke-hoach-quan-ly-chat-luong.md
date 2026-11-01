# KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG

**QUALITY MANAGEMENT PLAN | DỰ ÁN UNISUPPORT – STUDENT SUPPORT MANAGEMENT SYSTEM**

Đơn vị thực hiện: Nhóm 3

## Mục đích và phạm vi

Kế hoạch này mô tả cách nhóm dự án bảo đảm hệ thống UniSupport đạt chất lượng trong suốt quá trình phát triển cho đến khi bàn giao cho Aurora University. Kế hoạch áp dụng cho ba phân hệ Student Portal, Staff Operations, Management Dashboard và các chức năng dùng chung như đăng nhập, phân quyền, thông báo, file đính kèm và nhật ký thao tác.

Mọi yêu cầu về sản phẩm được lấy từ tài liệu yêu cầu sản phẩm (PRD) và bản thiết kế đã thống nhất; kế hoạch này không đặt thêm yêu cầu mới cho sản phẩm. Kế hoạch quy định các nguyên tắc chất lượng, chỉ số đo lường, cổng chất lượng và các quy trình đảm bảo chất lượng, kiểm soát chất lượng, xử lý lỗi, xử lý sự cố, cải tiến chất lượng áp dụng trong toàn bộ vòng đời dự án.

## 1. Hoạch định chất lượng (Quality Planning – Plan)

### 1.1. Nguyên tắc chất lượng

Mọi thành viên dự án tuân thủ các nguyên tắc sau:

1. **Kiểm soát liên tục:** mỗi kết quả công việc phải qua các cổng chất lượng tại mục 1.4 trước khi chuyển sang bước tiếp theo.
2. **Tuân thủ yêu cầu:** sản phẩm được xây dựng đúng PRD và thiết kế đã thống nhất. Mọi điểm chưa rõ về yêu cầu được BA làm rõ trước khi thực hiện.
3. **Review bắt buộc:** mã nguồn chỉ được gộp vào nhánh chính sau khi được ít nhất một thành viên khác review và chấp thuận.
4. **Bao phủ kiểm thử:** mỗi yêu cầu trong PRD có test case tương ứng, bao gồm trường hợp hợp lệ, dữ liệu không hợp lệ và truy cập trái quyền.
5. **Kiểm tra độc lập:** người thực hiện không tự review mã nguồn và không tự xác nhận hoàn thành công việc của mình.
6. **Ưu tiên theo mức độ:** lỗi được xử lý theo mức độ nghiêm trọng; lỗi nghiêm trọng được ưu tiên trước các công việc khác.
7. **Đánh giá dựa trên số liệu:** chất lượng được đánh giá qua các chỉ số đo lường tại mục 1.3.

### 1.2. Vai trò và trách nhiệm

Chất lượng là trách nhiệm chung của cả nhóm. Bảng dưới đây nêu phần việc liên quan đến chất lượng của từng vai trò, theo cơ cấu tổ chức tại Team Charter.

| Vai trò | Trách nhiệm về chất lượng |
|---|---|
| Project Manager (PM) | Kết luận đánh giá chất lượng cuối mỗi mốc và trước khi bàn giao. Quyết định các thay đổi về phạm vi. |
| Business Analyst (BA) | Bảo đảm PRD chính xác và nhất quán. Giải đáp khi có thắc mắc về tiêu chí chấp nhận. Rà soát test case đối chiếu với PRD và đối chiếu kết quả nghiệp vụ trước khi đóng issue. Xác nhận kết quả kiểm thử nghiệm thu và kết quả đo các chỉ tiêu thành công. Phân định một vấn đề là lỗi hay là yêu cầu thay đổi. |
| QA/QC Engineer | Xây dựng test case. Kiểm tra và xác nhận từng issue trước khi đóng. Ghi nhận và phân loại lỗi, kiểm thử lại sau khi sửa. Đo các chỉ tiêu thành công. Lập biên bản đánh giá chất lượng cuối mỗi mốc và báo cáo chất lượng. |
| Technical Lead (TL) | Review các thay đổi ảnh hưởng đến kiến trúc, bảo mật hoặc nhiều module. Quyết định khi có bất đồng về mức độ của lỗi kỹ thuật. |
| Frontend / Backend Developer | Tự kiểm tra sản phẩm của mình theo tiêu chí chấp nhận trước khi gửi review. Lập trình viên backend viết Unit Test. Review chéo mã nguồn của nhau và sửa các lỗi được giao. |
| UI/UX Designer | Đối chiếu giao diện với thiết kế trước khi đóng issue; kiểm tra giao diện hiển thị tốt trên máy tính và điện thoại, có đủ tiếng Việt và tiếng Anh, và thông báo lỗi rõ ràng. |
| DevOps Engineer | Duy trì môi trường kiểm thử ổn định, ghi lại phiên bản được kiểm thử, hỗ trợ kiểm tra độ ổn định và kiểm tra hệ thống sau khi triển khai. |

### 1.3. Chỉ số đánh giá chất lượng

Số liệu được lấy từ GitHub (issue, lỗi, Pull Request) và kết quả kiểm thử; QA/QC tổng hợp hằng tuần và cuối mỗi mốc.

| Chỉ số | Cách đo | Ngưỡng đạt |
|---|---|---|
| Mức độ bao phủ PRD | Số tiêu chí chấp nhận (AC) trong PRD đã có test case chạy đạt, chia cho tổng số AC của phạm vi kiểm tra. Mỗi quyền trong ma trận phân quyền có test cho cả trường hợp được phép và bị từ chối. | 100% AC của issue trước khi đóng; 100% AC của toàn bộ FR khi bàn giao. |
| Lỗi nghiêm trọng đang mở | Số lỗi mức nghiêm trọng chưa được khắc phục (định nghĩa tại mục 2.2). | 0 khi kết thúc mỗi mốc và khi bàn giao. |
| Bảo mật và phân quyền | Số lần truy cập thành công vào Ticket, file hoặc chức năng ngoài phạm vi quyền khi kiểm thử phân quyền (chỉ tiêu SM-07); số mật khẩu được lưu ở dạng đọc được. | 0 trường hợp. |
| Chỉ tiêu thành công SM-01 đến SM-07 | Đo theo phương pháp trong PRD, dùng dữ liệu giả lập và kết quả đúng được tính trước. | Đạt ngưỡng của từng chỉ tiêu. |
| Mã nguồn được review trước khi gộp | Số Pull Request được người khác chấp thuận trước khi gộp, chia cho tổng số Pull Request đã gộp. | 100%. |
| Hiệu năng | Thời gian phản hồi của các thao tác chính (đăng nhập, tạo Ticket, xem danh sách Ticket, xem Dashboard), đo trên môi trường kiểm thử với dữ liệu khoảng 3.000 sinh viên. | Ít nhất 95% lượt đo phản hồi trong 3 giây; không có tình trạng treo. |
| Lỗi phát hiện sau khi đã đóng issue | Số lỗi tìm thấy trong chức năng đã được xác minh và đóng, chia cho tổng số lỗi của mốc. | Không quá 10%. |
| Lỗi phải mở lại sau khi sửa | Số lỗi chưa đạt ở lần kiểm thử lại đầu tiên, chia cho tổng số lỗi đã sửa trong mốc. | Không quá 10%. |

Các ngưỡng về hiệu năng, lỗi phát hiện sau khi đóng issue và lỗi phải mở lại là mục tiêu kiểm soát nội bộ của nhóm dự án, không thuộc tiêu chí nghiệm thu của Aurora University. Các ngưỡng này được rà soát lại khi kết thúc Mốc 1 dựa trên số liệu thực tế; mọi điều chỉnh do PM quyết định và được ghi vào Decision Log.

### 1.4. Cổng chất lượng

Các cổng dưới đây là quy tắc bắt buộc đối với mọi hạng mục công việc (issue). Hạng mục không đáp ứng quy tắc của cổng được trả lại người thực hiện và không chuyển sang bước tiếp theo.

| Cổng | Quy tắc đi tiếp | Người thực hiện / bằng chứng |
|---|---|---|
| Trước khi phát triển (Definition of Ready) | Yêu cầu và tiêu chí chấp nhận (AC) trong PRD rõ ràng, không mâu thuẫn; có luồng ngoại lệ, quy tắc phân quyền và thiết kế giao diện. | BA xác nhận yêu cầu; QA/QC xác nhận kiểm thử được. Bằng chứng: issue có AC và liên kết PRD. |
| Trước khi gộp mã nguồn (Merge) | Ít nhất một thành viên khác review và approve Pull Request; Unit Test đạt; mã nguồn đúng PRD và thiết kế. | Người review approve trên GitHub; TL review thay đổi quan trọng. |
| Trước khi triển khai (Deploy) | Unit Test và kiểm thử tích hợp chạy đạt đầy đủ trên bản build; không còn lỗi nghiêm trọng đang mở. | DevOps triển khai; QA/QC xác nhận kết quả kiểm thử. |
| Trước khi đóng issue (Definition of Done) | Toàn bộ AC được kiểm chứng; kết quả đúng PRD và thiết kế; đáp ứng DoD tại mục 5. | QA/QC xác minh và cập nhật RTM; BA, UI/UX đối chiếu. |
| Trước khi bàn giao | Kiểm thử hồi quy toàn bộ đạt; các chỉ số tại mục 1.3 đạt ngưỡng; không còn lỗi nghiêm trọng. | QA/QC báo cáo kiểm thử; PM đối chiếu phạm vi; Aurora University nghiệm thu. |

Cuối mỗi mốc trong Master Schedule, QA/QC tổng hợp kết quả qua cổng và các chỉ số thành biên bản đánh giá chất lượng của mốc; PM kết luận mốc đạt hoặc chưa đạt.

## 2. Đảm bảo chất lượng (Quality Assurance – Do)

Đảm bảo chất lượng tập trung vào quy trình làm việc, nhằm phát hiện và xử lý các điểm chưa rõ hoặc sai sót trước khi chúng trở thành lỗi trong sản phẩm.

### 2.1. Quy trình và trách nhiệm

| Thời điểm | Hoạt động | Người thực hiện / kiểm chứng |
|---|---|---|
| Trước khi phát triển | Rà soát PRD, AC, luồng ngoại lệ, phân quyền và điều kiện Definition of Ready; lập test case từ AC. | BA, QA/QC; UI/UX cung cấp thiết kế; Developer làm rõ điểm triển khai |
| Khi phát triển | Developer tự kiểm tra theo AC, viết Unit Test, tạo Pull Request; kiểm tra xử lý lỗi và không để lộ thông tin bí mật. | Developer; QA/QC theo dõi việc áp dụng checklist review |
| Trước khi gộp / triển khai | Review thay đổi, kết quả test liên quan, cấu hình và thông tin nhạy cảm; kiểm tra quyền truy cập ở phía máy chủ. | Người review; TL với thay đổi quan trọng; QA/QC kiểm tra kết quả test liên quan |
| Cuối mỗi mốc | Đối chiếu AC, cập nhật RTM, kiểm tra ngẫu nhiên issue đã đóng; tổng hợp lỗi và các điểm cần cải tiến. | QA/QC tổng hợp; PM đối chiếu phạm vi và kết luận |

### 2.2. Quy trình xử lý lỗi

Mọi lỗi phát hiện trong quá trình kiểm thử được ghi nhận thành issue trên GitHub, gắn nhãn "bug" và liên kết với issue chức năng liên quan. Issue lỗi gồm các thông tin: yêu cầu liên quan trong PRD, mức độ nghiêm trọng, môi trường và phiên bản kiểm thử, các bước tái hiện, kết quả mong đợi, kết quả thực tế và bằng chứng.

**Mức độ lỗi:** lỗi được phân thành hai mức, thống nhất với tiêu chí đánh giá lỗi trong PRD và Master Schedule.

| Mức độ | Định nghĩa và ví dụ | Cách xử lý |
|---|---|---|
| Lỗi nghiêm trọng | Lỗi làm gián đoạn chức năng chính: luồng chính không thực hiện được hoặc cho kết quả sai so với PRD, làm mất dữ liệu, hoặc cho phép truy cập dữ liệu ngoài quyền. Ví dụ: sinh viên không tạo được Ticket; nhân viên xem được Ticket của phòng ban khác; số Ticket quá hạn trên Dashboard bị sai. | Được ưu tiên xử lý trước các công việc khác. Issue liên quan không được đóng và sản phẩm không được bàn giao khi lỗi chưa được khắc phục. |
| Lỗi thông thường | Lỗi không ảnh hưởng chức năng chính: kết quả nghiệp vụ vẫn đúng nhưng cách hiển thị hoặc thao tác chưa tốt. Ví dụ: thông báo lỗi chưa chỉ rõ trường cần sửa; một nhãn chưa có bản tiếng Anh; lỗi chính tả, căn lề. | Được ghi nhận và lập kế hoạch khắc phục. Mốc vẫn được kết thúc nếu lỗi đã có người phụ trách và thời hạn khắc phục. |

**Các bước xử lý một lỗi:**

1. **Ghi nhận và phân loại.** QA/QC tạo issue lỗi và xác định mức độ theo ảnh hưởng thực tế. Khi có bất đồng về mức độ, TL quyết định đối với lỗi kỹ thuật, BA quyết định đối với vấn đề về cách hiểu yêu cầu. Trường hợp hệ thống hoạt động đúng PRD, BA xác nhận không phải lỗi; nếu cần thay đổi yêu cầu, đề xuất được xử lý theo quy trình kiểm soát thay đổi.
2. **Sửa lỗi.** PM hoặc TL phân công người sửa. Bản sửa được thực hiện trên nhánh riêng và được review trước khi gộp.
3. **Kiểm thử lại.** Sau khi bản sửa được gộp, QA/QC thực hiện lại các bước tái hiện và kiểm thử hồi quy các chức năng liên quan.
4. **Đóng hoặc mở lại.** Nếu đạt, QA/QC ghi phiên bản đã kiểm tra và đóng issue lỗi. Nếu chưa đạt, issue được mở lại và chuyển cho người sửa kèm bằng chứng mới.

Chỉ lỗi thông thường mới được phép quyết định không khắc phục; PM ghi rõ lý do và đưa lỗi vào danh sách lỗi tồn đọng trong hồ sơ bàn giao. Lỗi quá thời hạn xử lý hoặc có bất đồng được QA/QC báo cáo lên TL hoặc PM theo tuyến chuyển cấp trong Team Charter.

### 2.3. Quy trình xử lý sự cố

Sự cố là sự kiện làm gián đoạn hoặc gây ảnh hưởng đến hệ thống đang vận hành, bao gồm: môi trường ngừng hoạt động, triển khai thất bại, dữ liệu bị mất hoặc sai lệch, dữ liệu bị truy cập trái quyền. Quy trình áp dụng cho môi trường kiểm thử chung, môi trường bàn giao và trong thời gian bảo hành 30 ngày.

1. **Báo sự cố.** Người phát hiện báo ngay trên kênh khẩn cấp của nhóm, nêu thời điểm, hiện tượng và phạm vi ảnh hưởng, rồi ghi thành issue lỗi mức nghiêm trọng.
2. **Đánh giá và thông báo.** TL xác định phạm vi ảnh hưởng và người xử lý. PM thông báo cho các bên bị ảnh hưởng; sự cố trên môi trường bàn giao hoặc trong thời gian bảo hành được báo cho Aurora University.
3. **Khôi phục hoạt động.** DevOps khôi phục hệ thống trước khi khắc phục nguyên nhân, ví dụ quay về phiên bản ổn định gần nhất. Với sự cố truy cập trái quyền, quyền truy cập liên quan được chặn ngay.
4. **Khắc phục nguyên nhân.** Nguyên nhân gốc được khắc phục theo quy trình xử lý lỗi tại mục 2.2, gồm review, kiểm thử lại và kiểm thử hồi quy.
5. **Đóng sự cố và rút kinh nghiệm.** Nguyên nhân, cách khắc phục và biện pháp phòng ngừa được ghi vào issue và đưa vào nội dung rút kinh nghiệm tại mục 4.

### 2.4. Môi trường và dữ liệu kiểm thử

Việc kiểm thử được thực hiện trên môi trường kiểm thử nội bộ do DevOps duy trì. Phiên bản cuối cùng được kiểm tra lại trên môi trường bàn giao. Mỗi lần kiểm thử đều ghi lại phiên bản hệ thống, trình duyệt và thiết bị đã sử dụng.

Theo PRD, môi trường kiểm thử chỉ sử dụng dữ liệu giả lập, không dùng thông tin cá nhân thật. Bộ dữ liệu đại diện cho quy mô khoảng 3.000 sinh viên, có đủ ba nhóm người dùng và ít nhất hai phòng ban để kiểm tra được việc phân quyền. Với các chỉ tiêu cần so sánh số liệu, QA/QC tính trước kết quả đúng từ bộ dữ liệu rồi đối chiếu với số liệu hệ thống hiển thị.

## 3. Kiểm soát chất lượng (Quality Control – Check)

Kiểm soát chất lượng là kiểm tra trực tiếp sản phẩm để phát hiện lỗi. Việc kiểm thử được chia thành ba trọng tâm theo tiến trình dự án. Mỗi test case đều ghi rõ yêu cầu hoặc kịch bản mà nó kiểm tra và được cập nhật vào ma trận truy xuất yêu cầu (RTM).

### 3.1. Trọng tâm 1 — Kiểm thử trong quá trình phát triển (M1–M5)

- **Developer:** viết Unit Test cho các xử lý nghiệp vụ quan trọng như tính thời hạn, chuyển trạng thái Ticket và kiểm tra quyền; tự kiểm tra theo tiêu chí chấp nhận trước khi gửi review.
- **QA/QC:** kiểm tra từng issue theo tiêu chí chấp nhận của issue đó; khi các chức năng của một luồng nghiệp vụ hoàn thành, kiểm thử tích hợp luồng đó; cuối mỗi mốc, chạy các test case của mốc và chạy lại các chức năng của giai đoạn trước để bảo đảm không bị ảnh hưởng (kiểm thử hồi quy).
- **Các trường hợp cần kiểm tra:** dữ liệu hợp lệ; thiếu thông tin bắt buộc; giá trị ở ngưỡng giới hạn, ví dụ file đúng 10 MB; thao tác lặp lại; người dùng thử truy cập dữ liệu của vai trò hoặc phòng ban khác; chuyển trạng thái Ticket không đúng quy tắc.
- **Bằng chứng:** tiêu chí chấp nhận được đánh dấu kèm ảnh chụp hoặc kết quả kiểm thử; mã nguồn đã được review.

### 3.2. Trọng tâm 2 — Kiểm thử toàn hệ thống trước bàn giao

- **Kiểm thử đầu cuối:** chạy toàn bộ vòng đời một Ticket, từ khi sinh viên gửi đến khi Ticket được đóng, qua đủ các luồng nghiệp vụ; kiểm tra dữ liệu xử lý được phản ánh đúng trên Dashboard và báo cáo.
- **Kiểm thử chức năng:** chạy lại toàn bộ test case của các FR trên phiên bản bàn giao; mỗi test case không đạt phải có issue lỗi tương ứng.
- **Kiểm thử phân quyền:** với mỗi quyền trong ma trận phân quyền của PRD, kiểm tra cả trường hợp được phép và trường hợp bị từ chối; thử truy cập Ticket, file đính kèm và chức năng quản trị ngoài phạm vi qua giao diện, đường dẫn trực tiếp và API.
- **Kiểm thử hồi quy:** chạy lại các chức năng liên quan sau mỗi lần sửa lỗi nghiêm trọng, và chạy toàn bộ trên phiên bản bàn giao.
- **Kiểm tra độ ổn định:** thực hiện các thao tác chính trên bộ dữ liệu kiểm thử, bảo đảm hệ thống không bị treo và không có lỗi làm gián đoạn.
- **Kiểm tra sau triển khai:** xác nhận hệ thống truy cập được và các luồng chính hoạt động trên môi trường bàn giao.

### 3.3. Trọng tâm 3 — Kiểm thử nghiệm thu người dùng (UAT)

Kịch bản nghiệm thu được lấy từ PRD, theo từng vai trò sinh viên, nhân viên và quản lý. Trước khi bàn giao, QA/QC chạy toàn bộ kịch bản nghiệm thu và đo bảy chỉ tiêu thành công; BA xác nhận kết quả. Mỗi kịch bản ghi lại dữ liệu đầu vào, kết quả mong đợi, kết quả thực tế, bằng chứng và các lỗi còn tồn tại.

Sau khi bàn giao, Aurora University nghiệm thu chính thức dựa trên các kịch bản này trong 10 ngày làm việc. Các lỗi kỹ thuật thuộc trách nhiệm của nhóm dự án được bảo hành trong 30 ngày kể từ ngày nghiệm thu.

### 3.4. Kiểm chứng yêu cầu phi chức năng

| Yêu cầu | Nội dung theo PRD | Bằng chứng |
|---|---|---|
| Hiệu năng | Các luồng chính hoạt động ổn định với dữ liệu đại diện khoảng 3.000 sinh viên, không bị treo. File đính kèm tối đa 10 MB. | Kết quả đo thời gian phản hồi theo mục 1.3, ghi kèm quy mô dữ liệu và điều kiện môi trường |
| Bảo mật | Người dùng không truy cập được Ticket và file ngoài phạm vi quyền. Tài khoản bị khóa không đăng nhập được. Mật khẩu không được lưu ở dạng đọc được. | Bảng kết quả kiểm thử phân quyền |
| Độ tin cậy | Khi thao tác gặp lỗi, hệ thống không để lại dữ liệu dở dang hoặc trạng thái sai quy tắc. Tải lại trang vẫn thấy đúng trạng thái đã lưu. | Kết quả các test case mô phỏng lỗi giữa chừng |
| Tính dễ sử dụng | Dùng được trên máy tính và điện thoại; có tiếng Việt và tiếng Anh ở mức cơ bản; thông báo lỗi chỉ rõ thông tin cần sửa. | Ảnh chụp các luồng chính trên hai loại thiết bị |
| Ghi nhật ký | Mọi thao tác quan trọng theo quy định đều được ghi nhật ký; nhật ký không thể sửa hoặc xóa bằng chức năng thông thường. | Đối chiếu thao tác đã thực hiện với nhật ký |
| Triển khai | Hệ thống truy cập được trên môi trường bàn giao và đủ các hạng mục bàn giao. | Kết quả kiểm tra sau triển khai; danh mục bàn giao |

Phạm vi kiểm tra bảo mật gồm phân quyền, đăng nhập và lưu trữ mật khẩu. Kiểm thử thâm nhập (pentest) và chứng nhận bảo mật nằm ngoài phạm vi dự án theo PRD.

## 4. Cải tiến chất lượng (Quality Improvement – Act)

Cuối mỗi mốc, nhóm rút kinh nghiệm tại buổi họp tuần kế tiếp. Nội dung xem xét gồm: các chỉ số tại mục 1.3 chưa đạt ngưỡng hoặc giảm so với giai đoạn trước; lỗi lặp lại; lỗi phải mở lại; lỗi phát hiện sau khi đã đóng issue; và các sự cố đã xảy ra. Với lỗi nghiêm trọng hoặc lặp lại, nhóm phân tích nguyên nhân gốc thuộc về yêu cầu, thiết kế, mã nguồn hay kiểm thử. Việc phân tích nhằm phòng ngừa lỗi tái diễn, không nhằm quy trách nhiệm cá nhân.

Các hành động cải tiến được ghi vào biên bản họp, có người phụ trách và thời hạn, ví dụ bổ sung nội dung kiểm tra khi review hoặc thêm test case hồi quy. Cuối mốc tiếp theo, QA/QC kiểm tra loại lỗi đó còn lặp lại hay không. Đề xuất làm thay đổi phạm vi, chi phí hoặc tiến độ phải qua quy trình kiểm soát thay đổi và được ghi vào Decision Log.

## 5. Definition of Done (DoD) — Tiêu chuẩn hoàn thành

DoD cụ thể hóa chuẩn hoàn thành trong Team Charter và được ghi trong từng issue trên GitHub. Một issue chỉ được đóng khi:

- Kết quả nằm đúng phạm vi của issue, đúng PRD và thiết kế; mọi tiêu chí chấp nhận đã được người xác minh đánh dấu kèm bằng chứng.
- Mã nguồn (nếu có) đã được người khác review và gộp vào nhánh chính; các góp ý quan trọng đã được xử lý; Unit Test liên quan đã chạy.
- Không còn lỗi nghiêm trọng nào liên quan đến issue chưa được khắc phục.
- Issue có liên kết đến yêu cầu trong PRD; tài liệu liên quan đã được cập nhật.
- Kết quả kiểm thử được lưu lại làm bằng chứng.

## 6. Quản lý rủi ro chất lượng

Các rủi ro chính ảnh hưởng đến chất lượng sản phẩm và biện pháp kiểm soát:

| Rủi ro | Ảnh hưởng | Biện pháp kiểm soát và người phụ trách |
|---|---|---|
| Phân quyền sai đối với Ticket hoặc file đính kèm | Người dùng xem hoặc sửa được dữ liệu ngoài quyền. | Kiểm tra quyền ở phía máy chủ; kiểm thử phân quyền ngay từ Mốc 1 và lặp lại ở giai đoạn cuối. Phụ trách: Backend Developer, QA/QC. |
| Tính sai thời hạn xử lý | Cảnh báo sắp quá hạn và quá hạn không chính xác. | Kiểm thử các trường hợp đặc biệt: tạm dừng khi chờ sinh viên bổ sung, ngày nghỉ, thay đổi mức ưu tiên. Phụ trách: Backend Developer, QA/QC. |
| Thao tác chuyển phòng ban hoặc cập nhật bị lỗi giữa chừng | Dữ liệu dở dang, mất lịch sử xử lý. | Kiểm tra kỹ khi review mã nguồn; kiểm thử các tình huống lỗi giữa chừng. Phụ trách: TL, QA/QC. |
| Số liệu Dashboard và báo cáo không khớp dữ liệu | Quản lý ra quyết định dựa trên số liệu sai. | Đối chiếu 100% với kết quả đúng tính trước. Phụ trách: Backend Developer, QA/QC. |
| Thay đổi yêu cầu sát thời điểm bàn giao | Phát sinh lỗi mới, ảnh hưởng tiến độ. | Chỉ nhận thay đổi đã được duyệt theo quy trình; đánh giá phạm vi cần kiểm thử lại. Phụ trách: PM, BA, QA/QC. |
| Hiệu năng phụ thuộc hạ tầng do Aurora University cung cấp | Kết quả trên môi trường kiểm thử khác với môi trường thật. | Ghi rõ điều kiện môi trường khi đo; kiểm tra lại sau khi triển khai. Phụ trách: DevOps. |

## 7. Hồ sơ chất lượng và công cụ

Hồ sơ chất lượng được lưu trên các công cụ đã quy định trong Team Charter như sau:

| Hồ sơ | Nội dung | Nơi lưu | Người phụ trách |
|---|---|---|---|
| Ma trận truy xuất yêu cầu | Liên kết giữa yêu cầu, công việc, kịch bản kiểm thử và kết quả. | PRD trên GitHub | BA, QA/QC |
| Test case, kết quả kiểm thử và kết quả đo chỉ tiêu | Các bước, dữ liệu, kết quả, phiên bản hệ thống, người thực hiện; số liệu đo các chỉ tiêu thành công. | Google Drive | QA/QC; BA xác nhận |
| Danh sách lỗi | Mức độ, trạng thái, người xử lý và kết quả kiểm thử lại của từng lỗi. | GitHub Issues | QA/QC, Developer |
| Biên bản đánh giá chất lượng của mốc | Kết quả qua cổng của các issue, các chỉ số, kết luận và việc cần làm. | Google Drive | QA/QC lập, PM kết luận |
| Biên bản họp và Decision Log | Các việc cần làm kèm người phụ trách, thời hạn; các quyết định quan trọng. | Google Drive | Người ghi biên bản, PM |
| Báo cáo kiểm thử cuối và hồ sơ bàn giao | Kết quả kiểm thử toàn bộ, kết quả các chỉ tiêu, danh sách lỗi còn lại. | Bộ tài liệu bàn giao | QA/QC, PM, DevOps, TL |
| Biên bản nghiệm thu | Các kịch bản đã thực hiện, kết quả, tồn đọng và xác nhận nghiệm thu. | Bộ tài liệu bàn giao | PM, đại diện Aurora University |
