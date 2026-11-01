# PROJECT PROPOSAL – UniSupport

## 1. Mục tiêu dự án

Dự án hướng tới xây dựng nền tảng UniSupport nhằm chuẩn hóa và tập trung hóa quy trình tiếp nhận, xử lý và theo dõi các yêu cầu hỗ trợ của sinh viên tại Aurora University, giảm sự phụ thuộc vào các kênh rời rạc hiện tại như email, biểu mẫu trực tuyến hoặc tin nhắn.

Hệ thống tập trung vào các mục tiêu cốt lõi sau:

- Tập trung hóa đầu mối: Cung cấp một kênh thống nhất để sinh viên gửi yêu cầu hỗ trợ và theo dõi tiến độ xử lý một cách minh bạch, bao gồm trạng thái hiện tại và đơn vị/người phụ trách xử lý.
- Tối ưu quy trình vận hành: Hỗ trợ nhân viên phân loại, phân công và xử lý yêu cầu rõ ràng hơn, từ đó giảm tình trạng bỏ sót, xử lý trùng lặp hoặc phản hồi không thống nhất giữa các phòng ban.
- Nâng cao năng lực giám sát: Cung cấp số liệu trực quan cho ban quản lý về khối lượng công việc, tình trạng xử lý, yêu cầu quá hạn và các nhóm vấn đề sinh viên thường gặp để hỗ trợ điều phối nhân sự.

### Giải pháp đề xuất

**UniSupport** là hệ thống Web Application đóng vai trò làm đầu mối tập trung để quản lý toàn bộ yêu cầu hỗ trợ của sinh viên. Thông qua hệ thống, sinh viên có thể chủ động tạo phiếu hỗ trợ, kiểm tra tiến độ xử lý và nhận thông báo phản hồi trong hệ thống từ nhà trường.

Ở phía vận hành, nhân viên các phòng ban thực hiện phân loại, điều phối công việc và cập nhật kết quả giải quyết trực tiếp trên phần mềm. Đồng thời, ban quản lý dễ dàng theo dõi số liệu và đánh giá hiệu quả xử lý thông qua Dashboard báo cáo trực quan.

Giao diện hệ thống được tối ưu để sử dụng linh hoạt trên cả máy tính lẫn thiết bị di động, tập trung triển khai đúng các nghiệp vụ trọng tâm theo phạm vi đã xác định.

### Assumptions (Giả định)

- Hệ thống phục vụ quy mô khoảng 3.000 sinh viên, không tối ưu cho kiến trúc tải lớn.
- Hệ thống được triển khai dưới dạng web application, không phải mobile app độc lập.
- Giao diện hỗ trợ Tiếng Việt và Tiếng Anh ở mức cơ bản.
- Thời gian triển khai không bao gồm thời gian chờ phản hồi hoặc phê duyệt từ phía Client.
- Hiệu năng và tính ổn định phụ thuộc vào hạ tầng máy chủ và tên miền do client cung cấp.
- Không yêu cầu tích hợp bên thứ ba
- Không yêu cầu chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

### Các hạng mục ngoài phạm vi hiện tại (Out of Scope)

Các hạng mục sau không nằm trong phạm vi hiện tại:

- Mobile app độc lập (iOS/Android)
- Tích hợp bên thứ ba ngoài phạm vi đã thống nhất.
- Thiết lập sao lưu tự động, theo dõi vận hành máy chủ và hỗ trợ hạ tầng lâu dài
- Phân quyền nhiều cấp và ghi lịch sử thao tác chi tiết ở mức nâng cao.
- Chat trực tiếp, gọi thoại trong hệ thống.
- Tối ưu chịu tải lớn vượt quá quy mô 3.000 sinh viên

## 2. Phạm Vi Chức Năng

### Module 1: Sinh viên

- Đăng nhập hệ thống
- Gửi yêu cầu hỗ trợ:
  - Chọn đúng nhóm vấn đề, mô tả tình huống và đính kèm file nếu cần (ảnh hoặc PDF)
  - Gửi yêu cầu và nhận mã Ticket để tiện theo dõi về sau
  - Xem tiến độ xử lý, lịch sử cập nhật và bổ sung thêm giấy tờ nếu nhân viên yêu cầu
- Nhận kết quả và đánh giá:
  - Xem kết quả giải quyết và các thông báo liên quan đến yêu cầu của mình
  - Đánh giá mức độ hài lòng sau khi yêu cầu được hoàn tất

### Module 2: Nhân viên

- Đăng nhập hệ thống
- Tiếp nhận và phân loại yêu cầu:
  - Xem danh sách yêu cầu mới và các yêu cầu đang được giao cho mình
  - Phân loại yêu cầu theo từng nhóm vấn đề và xem xét mức độ cần ưu tiên
  - Chuyển sang đúng phòng ban hoặc người phụ trách nếu không thuộc phần việc của mình
- Xử lý và cập nhật tiến độ:
  - Cập nhật trạng thái để sinh viên biết yêu cầu đang được xử lý đến đâu
  - Nhắn yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ còn thiếu nếu cần
  - Ghi lại kết quả và đóng yêu cầu sau khi hoàn thành

### Module 3: Quản lý

- Đăng nhập hệ thống
- Nắm tổng quan tình hình:
  - Xem số lượng yêu cầu mới, đang xử lý và những yêu cầu sắp hoặc đã quá hạn
  - Theo dõi tiến độ và khối lượng công việc theo từng phòng ban hoặc nhân viên
- Xem báo cáo:
  - Biết được nhóm yêu cầu nào đang nhiều nhất và có xu hướng tăng giảm ra sao
  - Xem thời gian xử lý trung bình và tổng hợp phản hồi của sinh viên theo từng giai đoạn
- Quản trị hệ thống:
  - Tạo, chỉnh sửa tài khoản và gán quyền phù hợp với từng vai trò

### Bảo mật và phân quyền

- Người dùng đăng nhập bằng tài khoản và mật khẩu riêng
- Mỗi vai trò chỉ thấy và thao tác được trong phạm vi quyền của mình
- File đính kèm chỉ người liên quan mới xem được
- Các thao tác quan trọng trong hệ thống đều được ghi lại để tra soát khi cần

## 3. Thời gian và quy trình thực hiện

### 3.1 Kế hoạch thực hiện theo giai đoạn

- **Thời gian thực hiện**: 14 tuần, tương đương khoảng 70 ngày làm việc, tính từ thời điểm khởi động dự án đến khi hoàn tất bàn giao chính thức. Thời gian này đã bao gồm kiểm thử nội bộ và UAT trong quá trình phát triển; thời gian nghiệm thu chính thức 10 ngày làm việc của nhà trường theo mục 5.2 được tính sau thời điểm bàn giao. Thời gian chờ phản hồi/phê duyệt từ phía Client sẽ được điều chỉnh tương ứng vào tiến độ nếu vượt thời gian đã thống nhất. .

| Giai đoạn | Thời gian | Nội dung chính |
|---|---|---|
| Giai đoạn 1 – Thu thập yêu cầu | Tuần 1–2 | Thu thập và phân tích yêu cầu, xác định phạm vi, luồng nghiệp vụ và tiêu chí nghiệm thu |
| Giai đoạn 2 – Thiết kế | Tuần 3–4 | Thiết kế giao diện, prototype, kiến trúc hệ thống, cơ sở dữ liệu, API và phân quyền |
| Giai đoạn 3 – Phát triển chính | Tuần 5–9 |  |
| &nbsp;&nbsp;– Module Sinh viên | Tuần 5–6 | Đăng nhập, gửi yêu cầu hỗ trợ, theo dõi trạng thái, nhận kết quả và đánh giá |
| &nbsp;&nbsp;– Module Nhân viên | Tuần 7–8 | Tiếp nhận, phân loại, xử lý yêu cầu và cập nhật tiến độ |
| &nbsp;&nbsp;– Module Quản lý | Tuần 9 | Thống kê, báo cáo, quản trị tài khoản và phân quyền |
| Giai đoạn 4 – Tích hợp hệ thống | Tuần 10–11 | Tích hợp giao diện và backend, xây dựng dashboard, báo cáo và kiểm tra phân quyền truy cập |
| Giai đoạn 5 – Kiểm thử & Nghiệm thu | Tuần 12–13 | Kiểm thử chức năng, kiểm thử tích hợp, kiểm thử hồi quy, UAT với client và sửa lỗi |
| Giai đoạn 6 – Hoàn thiện & Bàn giao | Tuần 14 | Sửa lỗi cuối, triển khai hệ thống, hoàn thiện tài liệu và bàn giao |

### 3.2 Các cột mốc quan trọng

- **Mốc 0 (Tuần 1)**: Ký xác nhận hợp tác và đặt cọc triển khai dự án
- **Mốc 1 (cuối Tuần 2):** Chốt phạm vi và yêu cầu dự án
- **Mốc 2 (cuối Tuần 4)**: Duyệt thiết kế giao diện & prototype
- **Mốc 3 (cuối Tuần 9):** Hoàn thành phát triển 3 phân hệ, demo nội bộ
- **Mốc 4 (Tuần 13):** Hoàn thành UAT và tổng hợp kết quả phản hồi từ client
- **Mốc 5 (Tuần 14):** Hoàn tất xử lý các lỗi thuộc phạm vi, triển khai và bàn giao chính thức.

## 4. Kinh phí

- Tổng kinh phí: **300 Triệu VNĐ**
- Chi tiết mốc thanh toán, bao gồm đặt cọc, sẽ được thống nhất trong hợp đồng triển khai chính thức.

## 5. Bàn giao & nghiệm thu

### 5.1 Nội dung bàn giao

Cuối dự án, các hạng mục sau sẽ được bàn giao chính thức cho Aurora University:

#### Hệ thống web UniSupport

- Phần mềm UniSupport hoàn chỉnh, hỗ trợ sử dụng trên trình duyệt máy tính và thiết bị di động
- Triển khai lên môi trường của client theo thỏa thuận

#### Mã nguồn

- Source code frontend và backend của toàn bộ hệ thống
- Tài liệu hướng dẫn cài đặt và vận hành hệ thống

#### Cơ sở dữ liệu

- Cấu trúc database và ERD
- Dữ liệu mẫu phục vụ kiểm thử

#### Tài liệu

- Tài liệu phạm vi và yêu cầu đã được xác nhận
- Hướng dẫn sử dụng cho từng vai trò trong hệ thống
- Test cases và kết quả kiểm thử

### 5.2 Nghiệm thu

Quý trường có **10 ngày** làm việc để tiến hành kiểm thử kể từ khi nhận bàn giao chính thức.

**Tiêu chí nghiệm thu:**

- Các luồng chính của ba phân hệ hoạt động đúng và ổn định
- Phân quyền hoạt động đúng theo từng vai trò
- Không còn lỗi làm gián đoạn chức năng chính
- Tài liệu bàn giao đầy đủ theo cam kết
- Các lỗi phát sinh do phía đơn vị phát triển (nếu có) được ghi nhận và có kế hoạch khắc phục cụ thể, không tính là điều kiện từ chối nghiệm thu nếu không ảnh hưởng chức năng chính.

### 5.3 Bảo hành

Hệ thống được hỗ trợ sửa lỗi kỹ thuật phát sinh từ phía đội phát triển, miễn phí trong vòng 30 ngày kể từ ngày hai bên xác nhận nghiệm thu. Không áp dụng cho yêu cầu tính năng mới hoặc thay đổi ngoài phạm vi đã thống nhất.

## 6. Cam kết

Trong suốt quá trình triển khai, hai bên thống nhất làm việc trên cơ sở trao đổi cởi mở và cùng hướng đến mục tiêu chung. Bất kỳ điều chỉnh nào về phạm vi, chi phí hay tiến độ đều cần được hai bên xác nhận lại bằng văn bản trước khi áp dụng.

**Về phía Aurora University:**

- Cung cấp thông tin nghiệp vụ, dữ liệu và điều kiện hạ tầng cần thiết theo đúng lịch trình tại mục 3.1.
- Tham gia đánh giá và nghiệm thu trong thời hạn quy định tại mục 5.2.
- Nếu việc cung cấp thông tin hoặc phản hồi bị kéo dài, lịch trình chung sẽ được điều chỉnh phù hợp với thời gian thực tế bị ảnh hưởng.

**Về phía đơn vị thực hiện:**

- Bám sát phạm vi và chất lượng đã xác nhận ngay sau giai đoạn thu thập yêu cầu (cuối Tuần 2).
- Chủ động cảnh báo khi phát hiện nguy cơ ảnh hưởng đến tiến độ.
- Giữ an toàn cho dữ liệu do nhà trường cung cấp.
- Tiếp tục hỗ trợ khắc phục sự cố kỹ thuật trong giai đoạn bảo hành nêu tại mục 5.3.
