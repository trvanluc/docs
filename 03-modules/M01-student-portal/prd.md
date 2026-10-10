# Phân Hệ Sinh Viên (M01 - Student Portal)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Student Portal** cung cấp giao diện để sinh viên Aurora University tra cứu hướng dẫn, tạo yêu cầu hỗ trợ, theo dõi tiến độ xử lý, bổ sung thông tin/tài liệu, nhận kết quả và đánh giá mức độ hài lòng.

- **Actor chính:** Sinh viên (Student).
- **Phạm vi dữ liệu:** Sinh viên chỉ được xem và thao tác trên Ticket do chính tài khoản của mình tạo.
- **Điều kiện truy cập:** Các chức năng nghiệp vụ yêu cầu người dùng đã đăng nhập bằng tài khoản hợp lệ.
- **Phạm vi quyền:** Sinh viên không được truy cập dữ liệu hoặc chức năng thuộc Staff Operations hoặc Management Dashboard.

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STU-00] Đăng nhập và truy cập Student Portal

#### 1. Mô tả & Phạm vi
Cho phép sinh viên đăng nhập vào UniSupport bằng tài khoản hợp lệ và truy cập Student Portal theo đúng phạm vi quyền.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên.
- **Preconditions:** Tài khoản sinh viên tồn tại và đang hoạt động.

#### 3. Quy tắc Dữ liệu & Validation
- **Tên đăng nhập:** bắt buộc, sử dụng tài khoản do nhà trường cấp cho sinh viên.
- **Mật khẩu:** bắt buộc.
- Không chấp nhận dữ liệu chỉ chứa khoảng trắng.

#### 4. Luồng xử lý chi tiết
1. Sinh viên truy cập UniSupport.
2. Hệ thống yêu cầu đăng nhập nếu chưa có phiên hợp lệ.
3. Sinh viên nhập thông tin đăng nhập.
4. Hệ thống kiểm tra thông tin tài khoản và trạng thái hoạt động.
5. Nếu hợp lệ, hệ thống tạo phiên làm việc và cho phép truy cập Student Portal.
6. Sinh viên có thể đăng xuất khi kết thúc phiên sử dụng.

#### 5. Luồng ngoại lệ
- Thông tin đăng nhập không hợp lệ: từ chối truy cập và hiển thị thông báo phù hợp.
- Tài khoản bị khóa hoặc vô hiệu hóa: không tạo phiên đăng nhập.
- Phiên hết hạn: yêu cầu người dùng xác thực lại.

#### 6. Quy tắc nghiệp vụ
- Sinh viên không được truy cập dữ liệu hoặc chức năng ngoài phạm vi Student.
- Cơ chế xác thực và quản lý phiên được dùng chung với các phân hệ khác.

#### 7. Tiêu chí nghiệm thu
- **AC-00-01:** Tài khoản hợp lệ và đang hoạt động đăng nhập thành công vào Student Portal.
- **AC-00-02:** Thông tin đăng nhập sai hoặc tài khoản bị vô hiệu hóa không tạo được phiên hợp lệ.
- **AC-00-03:** Phiên Student không cho phép truy cập dữ liệu vượt phạm vi quyền.
- **AC-00-04:** Phiên hết hạn yêu cầu người dùng đăng nhập lại trước khi tiếp tục thao tác được bảo vệ.

---

### [FR-STU-01] Tra cứu hướng dẫn và FAQ

#### 1. Mô tả & Phạm vi
Giúp sinh viên tra cứu các vấn đề thường gặp và thông tin cần chuẩn bị trước khi tạo Ticket.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Dữ liệu FAQ và nhóm vấn đề đang hoạt động.

#### 3. Quy tắc Dữ liệu & Validation
- Từ khóa tìm kiếm: không bắt buộc.
- Nhóm vấn đề: không bắt buộc khi chỉ duyệt danh sách FAQ.

#### 4. Luồng xử lý chi tiết
1. Sinh viên mở mục **Hướng dẫn / FAQ**.
2. Hệ thống hiển thị nội dung FAQ theo nhóm vấn đề.
3. Sinh viên chọn nhóm vấn đề hoặc tìm nội dung liên quan.
4. Hệ thống hiển thị câu trả lời, đơn vị phụ trách và thông tin/tài liệu cần chuẩn bị nếu có.
5. Nếu FAQ chưa giải quyết được vấn đề, sinh viên chuyển sang chức năng tạo Ticket.

#### 5. Luồng ngoại lệ
- Không có kết quả phù hợp: hệ thống hiển thị trạng thái không tìm thấy và vẫn cho phép chuyển sang tạo Ticket.
- Dữ liệu FAQ tạm thời không khả dụng: hệ thống hiển thị thông báo phù hợp và không tự động tạo Ticket.

#### 6. Quy tắc nghiệp vụ
- FAQ chỉ hỗ trợ tra cứu, không thay thế quy trình xử lý Ticket.
- Không bao gồm chatbot AI hoặc hệ thống CMS FAQ chuyên biệt.

#### 7. Tiêu chí nghiệm thu
- **AC-01-01:** Sinh viên xem được danh sách FAQ theo nhóm vấn đề.
- **AC-01-02:** Tìm kiếm hoặc chọn nhóm vấn đề trả về nội dung phù hợp với dữ liệu FAQ hiện có.
- **AC-01-03:** Sinh viên có thể chuyển từ FAQ sang chức năng tạo Ticket khi cần hỗ trợ thêm.

---

### [FR-STU-02] Tạo và gửi yêu cầu hỗ trợ

#### 1. Mô tả & Phạm vi
Cho phép sinh viên tạo Ticket mới bằng cách chọn một **Nhóm vấn đề (Category)** từ danh mục có sẵn do hệ thống cung cấp, nhập nội dung mô tả chi tiết vấn đề và đính kèm tài liệu minh chứng khi cần. Mỗi Nhóm vấn đề được cấu hình gắn với phòng ban tiếp nhận phù hợp để hệ thống xác định nơi tiếp nhận Ticket sau khi gửi.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Danh mục nhóm vấn đề và ánh xạ phòng ban phụ trách đang hoạt động.

#### 3. Quy tắc Dữ liệu & Validation
- **Nhóm vấn đề (Category):**
  - Bắt buộc chọn một giá trị từ danh mục Nhóm vấn đề đang hoạt động do hệ thống cung cấp.
  - Sinh viên không được tự tạo, sửa hoặc nhập tự do Nhóm vấn đề khi tạo Ticket.
  - Mỗi Nhóm vấn đề được cấu hình với một phòng ban tiếp nhận phù hợp.
  - Hệ thống sử dụng Nhóm vấn đề đã chọn để xác định phòng ban tiếp nhận Ticket.
- **Nội dung yêu cầu:** bắt buộc, từ **20 đến 2.000 ký tự**, không chấp nhận nội dung chỉ chứa khoảng trắng.
- **File đính kèm:** không bắt buộc.
- Tối đa **03 file/lần**.
- Dung lượng tối đa **10 MB/file**.
- Định dạng cho phép: PDF, PNG, JPG/JPEG.

#### 4. Luồng xử lý chi tiết
1. Sinh viên mở chức năng **Tạo yêu cầu**.
2. Hệ thống hiển thị biểu mẫu tạo Ticket.
3. Sinh viên chọn một Nhóm vấn đề từ danh mục có sẵn và nhập nội dung mô tả chi tiết yêu cầu.
4. Sinh viên đính kèm file minh chứng nếu cần.
5. Sinh viên xác nhận gửi.
6. Hệ thống kiểm tra dữ liệu bắt buộc và file đính kèm.
7. Hệ thống xác định phòng ban tiếp nhận dựa trên cấu hình của Nhóm vấn đề đã chọn.
8. Hệ thống tạo Ticket, cấp mã Ticket duy nhất và ghi nhận thời điểm tạo.
9. Ticket được khởi tạo ở trạng thái `NEW`, mức ưu tiên mặc định `MEDIUM` và thời hạn xử lý tương ứng.
10. Hệ thống thông báo tạo Ticket thành công và hiển thị mã Ticket cho sinh viên.

#### 5. Luồng ngoại lệ
- Thiếu nhóm vấn đề hoặc nội dung yêu cầu: không tạo Ticket và chỉ rõ thông tin cần bổ sung.
- File sai định dạng, vượt 10 MB hoặc vượt quá 03 file: từ chối file không hợp lệ.
- Nhóm vấn đề không còn hoạt động: không tạo Ticket và yêu cầu sinh viên chọn lại.
- Thao tác gửi lặp: không làm phát sinh nhiều Ticket từ cùng một lần gửi.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-FILE-01`, `BR-FILE-02` và `BR-DUE-01`.
- Ticket phải gắn với sinh viên tạo Ticket.
- Sinh viên không tự chọn người phụ trách.
- Mã Ticket phải duy nhất trong hệ thống.

#### 7. Tiêu chí nghiệm thu
- **AC-02-01:** Dữ liệu hợp lệ tạo đúng một Ticket ở trạng thái `NEW`.
- **AC-02-02:** Ticket mới có mã Ticket duy nhất và thuộc đúng sinh viên tạo.
- **AC-02-03:** Ticket mới được gắn nhóm vấn đề, phòng ban tiếp nhận, priority `MEDIUM` và thời hạn xử lý tương ứng.
- **AC-02-04:** Dữ liệu bắt buộc không hợp lệ không làm phát sinh Ticket.
- **AC-02-05:** File không đáp ứng quy tắc định dạng, dung lượng hoặc số lượng không được chấp nhận.
- **AC-02-06:** Thao tác gửi lặp không tạo nhiều Ticket từ cùng một lần gửi.

---

### [FR-STU-03] Xem và theo dõi Ticket

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem danh sách Ticket của mình và theo dõi trạng thái, trách nhiệm xử lý, thời hạn và lịch sử cập nhật.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Sinh viên có phiên làm việc hợp lệ.

#### 3. Quy tắc Dữ liệu & Validation
- Bộ lọc trạng thái: không bắt buộc.
- Mã Ticket hoặc từ khóa tìm kiếm: không bắt buộc.
- Hệ thống chỉ trả về dữ liệu thuộc sinh viên đang đăng nhập.
- Bộ trạng thái hiển thị: `NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`.

#### 4. Luồng xử lý chi tiết
1. Sinh viên mở **Ticket của tôi**.
2. Hệ thống hiển thị các Ticket thuộc sinh viên, ưu tiên Ticket cập nhật gần nhất.
3. Mỗi Ticket hiển thị tối thiểu mã Ticket, nhóm vấn đề, thời điểm tạo và trạng thái hiện tại.
4. Sinh viên mở một Ticket để xem chi tiết.
5. Hệ thống hiển thị nội dung yêu cầu, phòng ban/người phụ trách nếu đã được phân công, thời hạn xử lý dự kiến, file được phép truy cập, kết quả nếu đã có và lịch sử xử lý được phép hiển thị cho sinh viên.

#### 5. Luồng ngoại lệ
- Không có Ticket: hiển thị trạng thái danh sách trống.
- Ticket không thuộc sinh viên đang đăng nhập: từ chối truy cập và không hiển thị dữ liệu Ticket.

#### 6. Quy tắc nghiệp vụ
- Transfer và Escalation được thể hiện trong lịch sử xử lý, không phải trạng thái Ticket.
- Lịch sử hiển thị cho sinh viên tối thiểu gồm: tạo Ticket, thay đổi trạng thái, yêu cầu bổ sung, sinh viên bổ sung thông tin/tài liệu, chuyển phòng ban, ghi nhận kết quả, mở lại và đóng Ticket.
- Các sự kiện quản trị hoặc Audit Trail không liên quan trực tiếp đến quá trình hỗ trợ của sinh viên không hiển thị trong Student Portal.

#### 7. Tiêu chí nghiệm thu
- **AC-03-01:** Danh sách chỉ chứa Ticket thuộc sinh viên đang đăng nhập.
- **AC-03-02:** Chi tiết Ticket hiển thị đúng trạng thái hiện tại và lịch sử xử lý được phép xem.
- **AC-03-03:** Ticket của sinh viên khác không thể được truy cập thông qua đường dẫn hoặc mã Ticket.
- **AC-03-04:** Khi trạng thái, phòng ban hoặc người phụ trách thay đổi hợp lệ, thông tin theo dõi phản ánh giá trị mới.

---

### [FR-STU-04] Nhận và xem thông báo Ticket

#### 1. Mô tả & Phạm vi
Thông báo cho sinh viên khi Ticket của mình có sự kiện nghiệp vụ cần biết hoặc cần hành động.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket và người nhận thông báo được xác định hợp lệ.

#### 3. Quy tắc Dữ liệu & Validation
- Thông báo phải liên kết với đúng Ticket và đúng sinh viên nhận.
- Trạng thái đã đọc/chưa đọc phải được ghi nhận nhất quán.

#### 4. Luồng xử lý chi tiết
1. Một sự kiện cần thông báo xảy ra.
2. Hệ thống tạo thông báo cho sinh viên sở hữu Ticket.
3. Sinh viên thấy thông báo mới trong Student Portal.
4. Sinh viên mở thông báo.
5. Hệ thống hiển thị nội dung phù hợp và cho phép điều hướng đến Ticket liên quan.
6. Sinh viên có thể đánh dấu thông báo đã đọc.

Các sự kiện chính gồm:
- Ticket được tạo thành công.
- Trạng thái Ticket thay đổi.
- Nhân viên yêu cầu bổ sung thông tin hoặc tài liệu.
- Ticket được chuyển sang phòng ban khác.
- Ticket có kết quả xử lý.
- Ticket được mở lại hoặc đóng.

#### 5. Luồng ngoại lệ
- Ticket không còn thuộc phạm vi truy cập: không cho phép mở chi tiết thông qua thông báo.
- Thông báo không còn liên kết đến dữ liệu hợp lệ: hiển thị thông báo phù hợp và không làm lộ dữ liệu.

#### 6. Quy tắc nghiệp vụ
- Chỉ gửi thông báo đến sinh viên sở hữu Ticket.
- Thông báo không được làm lộ dữ liệu của Ticket khác.
- Thông báo của M01 là **thông báo trong hệ thống (in-app notification)**.

#### 7. Tiêu chí nghiệm thu
- **AC-04-01:** Sự kiện hợp lệ tạo thông báo cho đúng sinh viên.
- **AC-04-02:** Thông báo liên kết đúng Ticket và chỉ mở được khi người dùng có quyền.
- **AC-04-03:** Trạng thái đã đọc/chưa đọc được ghi nhận nhất quán.
- **AC-04-04:** Sinh viên không xem được thông báo thuộc tài khoản khác.

---

### [FR-STU-05] Bổ sung thông tin và tài liệu

#### 1. Mô tả & Phạm vi
Cho phép sinh viên cung cấp thông tin hoặc tài liệu còn thiếu khi nhân viên yêu cầu.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket thuộc sinh viên và đang ở trạng thái `WAITING_STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation
- Phải có ít nhất một trong hai: nội dung bổ sung hoặc file đính kèm.
- Nội dung bổ sung, nếu có: tối đa **2.000 ký tự**, không chấp nhận nội dung chỉ chứa khoảng trắng.
- File đính kèm: PDF/PNG/JPG/JPEG, tối đa 10 MB/file và tối đa 03 file/lần.

#### 4. Luồng xử lý chi tiết
1. Sinh viên mở Ticket có yêu cầu bổ sung.
2. Hệ thống hiển thị nội dung cần bổ sung.
3. Sinh viên nhập nội dung phản hồi và/hoặc đính kèm tài liệu.
4. Sinh viên xác nhận gửi bổ sung.
5. Hệ thống kiểm tra trạng thái Ticket và tính hợp lệ của dữ liệu/file.
6. Hệ thống lưu nội dung bổ sung vào lịch sử Ticket.
7. Ticket chuyển từ `WAITING_STUDENT` về `IN_PROGRESS`.
8. Thời gian xử lý tiếp tục được tính từ phần thời gian còn lại.

#### 5. Luồng ngoại lệ
- Không có nội dung và không có file: từ chối gửi bổ sung.
- Ticket không còn ở `WAITING_STUDENT`: từ chối thao tác và hiển thị trạng thái mới nhất.
- File không hợp lệ: áp dụng quy tắc file dùng chung.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-SUP-01`, `BR-FILE-02` và `BR-DUE-02`.
- Bổ sung thành công phải được ghi nhận trong lịch sử Ticket.

#### 7. Tiêu chí nghiệm thu
- **AC-05-01:** Ticket `WAITING_STUDENT` nhận bổ sung hợp lệ và chuyển về `IN_PROGRESS`.
- **AC-05-02:** Nội dung/file bổ sung được lưu đúng Ticket và nhân viên có quyền có thể truy cập.
- **AC-05-03:** Ticket ngoài `WAITING_STUDENT` không chấp nhận bổ sung theo luồng này.
- **AC-05-04:** Thời gian chờ sinh viên không bị tính vào thời gian xử lý.

---

### [FR-STU-06] Xem kết quả, phản hồi và yêu cầu mở lại

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem nội dung kết quả xử lý và tài liệu kết quả nếu có, sau đó xác nhận Ticket đã được giải quyết hoặc phản hồi rằng vấn đề vẫn chưa được giải quyết.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket thuộc sinh viên.
- Ticket ở `RESOLVED` hoặc `CLOSED` để xem kết quả.
- Phản hồi và mở lại chỉ áp dụng khi Ticket đang ở `RESOLVED` và còn trong thời hạn phản hồi.

#### 3. Quy tắc Dữ liệu & Validation
- Xác nhận kết quả: không yêu cầu nội dung bổ sung.
- Yêu cầu mở lại: bắt buộc có lý do từ **10 đến 1.000 ký tự**, không chấp nhận nội dung chỉ chứa khoảng trắng.
- Hệ thống phải kiểm tra trạng thái Ticket và thời hạn phản hồi trước khi chấp nhận thao tác.

#### 4. Luồng xử lý chi tiết

**Luồng A — Chấp nhận kết quả**
1. Sinh viên mở Ticket `RESOLVED`.
2. Hệ thống hiển thị nội dung kết quả xử lý, tài liệu kết quả nếu có và thời hạn phản hồi còn lại.
3. Sinh viên xác nhận kết quả đã giải quyết vấn đề.
4. Hệ thống chuyển Ticket sang `CLOSED` và ghi nhận thời điểm đóng.

**Luồng B — Yêu cầu mở lại**
1. Sinh viên mở Ticket `RESOLVED` trong thời hạn phản hồi.
2. Sinh viên chọn **Vấn đề chưa được giải quyết**.
3. Sinh viên nhập lý do mở lại.
4. Hệ thống kiểm tra trạng thái và thời hạn phản hồi.
5. Nếu hợp lệ, hệ thống ghi nhận lý do và chuyển Ticket về `IN_PROGRESS`.
6. Hệ thống thông báo cho người phụ trách hiện tại hoặc phòng ban đang phụ trách Ticket.

**Luồng C — Tự động đóng**
1. Ticket ở `RESOLVED`.
2. Hết 03 ngày làm việc mà sinh viên không yêu cầu xử lý tiếp.
3. Hệ thống chuyển Ticket sang `CLOSED`.

#### 5. Luồng ngoại lệ
- Yêu cầu mở lại thiếu lý do: từ chối thao tác.
- Ticket đã `CLOSED` hoặc hết thời hạn phản hồi: không cho phép mở lại.
- Ticket không thuộc sinh viên: từ chối truy cập và thao tác.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-LIFE-01`, `BR-LIFE-02`, `BR-LIFE-03`.
- Reopen chỉ thực hiện từ `RESOLVED` về `IN_PROGRESS`.
- Ticket `CLOSED` không được mở lại.
- Mọi lần chấp nhận, mở lại và tự động đóng phải được ghi nhận trong lịch sử.

#### 7. Tiêu chí nghiệm thu
- **AC-06-01:** Sinh viên xem được kết quả của Ticket `RESOLVED` hoặc `CLOSED` thuộc mình.
- **AC-06-02:** Xác nhận kết quả khi Ticket đang `RESOLVED` làm Ticket chuyển sang `CLOSED`.
- **AC-06-03:** Yêu cầu mở lại hợp lệ trong 03 ngày làm việc chuyển Ticket từ `RESOLVED` về `IN_PROGRESS`.
- **AC-06-04:** Reopen thiếu lý do, hết thời hạn hoặc Ticket đã `CLOSED` bị từ chối.
- **AC-06-05:** Ticket `RESOLVED` không có yêu cầu xử lý tiếp được tự động đóng khi hết thời hạn phản hồi.

---

### [FR-STU-07] Đánh giá mức độ hài lòng (CSAT)

#### 1. Mô tả & Phạm vi
Ghi nhận mức độ hài lòng của sinh viên sau khi Ticket đã kết thúc vòng đời xử lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket thuộc sinh viên, đang ở `CLOSED`, chưa có đánh giá và còn trong thời hạn đánh giá.

#### 3. Quy tắc Dữ liệu & Validation
- Điểm đánh giá: bắt buộc, từ 1 đến 5 sao.
- Nhận xét: không bắt buộc, tối đa **500 ký tự**.
- Mỗi Ticket chỉ được đánh giá một lần.

#### 4. Luồng xử lý chi tiết
1. Sinh viên mở Ticket `CLOSED`.
2. Hệ thống hiển thị chức năng đánh giá nếu Ticket còn đủ điều kiện.
3. Sinh viên chọn điểm từ 1 đến 5 sao.
4. Sinh viên nhập nhận xét nếu muốn.
5. Sinh viên gửi đánh giá.
6. Hệ thống kiểm tra quyền, thời hạn và việc Ticket đã được đánh giá trước đó.
7. Hệ thống lưu đánh giá và xác nhận gửi thành công.

#### 5. Luồng ngoại lệ
- Không chọn điểm: từ chối gửi.
- Ticket đã có đánh giá: không cho gửi lần hai.
- Quá 07 ngày theo lịch kể từ khi Ticket chuyển sang `CLOSED`: không cho gửi đánh giá mới.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-CSAT-01`.
- Đánh giá không làm thay đổi trạng thái Ticket.

#### 7. Tiêu chí nghiệm thu
- **AC-07-01:** Ticket `CLOSED` còn trong thời hạn cho phép nhận đánh giá 1-5 sao.
- **AC-07-02:** Đánh giá hợp lệ được lưu đúng Ticket và sử dụng cho báo cáo CSAT.
- **AC-07-03:** Không thể gửi đánh giá lần thứ hai cho cùng Ticket.
- **AC-07-04:** Ticket quá thời hạn 07 ngày theo lịch không nhận đánh giá mới.
- **AC-07-05:** Gửi CSAT không thay đổi trạng thái `CLOSED`.

---

## III. QUY TẮC THAM CHIẾU

Các Functional Requirements của M01 phải tuân thủ thống nhất với:

- [Ticket Lifecycle](../../02-domain/ticket-lifecycle.md)
- [State Transition](../../02-domain/state-transition.md)
- [Business Rules](../../02-domain/business-rules.md)
