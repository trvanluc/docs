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

**Priority:** Cao: mọi chức năng của Student Portal cần đăng nhập và phân quyền. **Mốc giao:** MS-01.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Thông tin đăng nhập không hợp lệ: từ chối truy cập và hiển thị thông báo phù hợp.
- Tài khoản bị khóa hoặc vô hiệu hóa: không tạo phiên đăng nhập.
- Phiên hết hạn: yêu cầu người dùng xác thực lại.

#### 6. Quy tắc nghiệp vụ
- Sinh viên không được truy cập dữ liệu hoặc chức năng ngoài phạm vi Student.
- Cơ chế xác thực và quản lý phiên được dùng chung với các phân hệ khác.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-00/AC-01:** Tài khoản sinh viên hợp lệ, đang hoạt động đăng nhập thành công và được đưa vào Student Portal.
- **FR-STU-00/AC-02:** Sai tên đăng nhập hoặc mật khẩu: màn hình hiển thị thông báo "thông tin đăng nhập không đúng" (không nói rõ sai trường nào), không tạo phiên, người dùng vẫn ở màn hình đăng nhập.
- **FR-STU-00/AC-03:** Tài khoản bị khóa hoặc vô hiệu hóa nhập đúng mật khẩu: hiển thị thông báo "tài khoản đã bị khóa", không tạo phiên.
- **FR-STU-00/AC-04:** Bỏ trống hoặc chỉ nhập khoảng trắng ở tên đăng nhập/mật khẩu: thông báo chỉ rõ trường bắt buộc, yêu cầu đăng nhập không được gửi.
- **FR-STU-00/AC-05:** Phiên Student mở đường dẫn hoặc gọi chức năng của Staff Operations/Management Dashboard: hiển thị trang "không có quyền truy cập", không hiển thị dữ liệu nào của phân hệ đó.
- **FR-STU-00/AC-06:** Phiên hết hạn: thao tác được bảo vệ tiếp theo đưa người dùng về màn hình đăng nhập kèm thông báo "phiên đã hết hạn"; dữ liệu chưa lưu không được ghi.
- **FR-STU-00/AC-07:** Sinh viên đăng nhập trên cùng màn hình đăng nhập dùng chung với Nhân viên và Quản lý, và được điều hướng tới Student Portal theo vai trò.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Đã có phiên hợp lệ:** sinh viên mở UniSupport khi phiên còn hiệu lực; hệ thống bỏ qua bước đăng nhập và vào thẳng Student Portal.
- **A2 — Đăng xuất chủ động (bước 6):** phiên kết thúc; mọi truy cập sau đó yêu cầu đăng nhập lại.

#### 9. Ví dụ Edge Case
- Tên đăng nhập có khoảng trắng ở đầu/cuối: hệ thống bỏ khoảng trắng trước khi kiểm tra; chỉ toàn khoảng trắng thì báo thiếu dữ liệu (mục 3).
- Tài khoản bị khóa trong lúc đang có phiên: thao tác được bảo vệ tiếp theo bị từ chối và yêu cầu đăng nhập lại (FR-STU-00/AC-03, FR-STU-00/AC-06).
- Tài khoản Staff đăng nhập và cố mở URL của Student Portal: bị từ chối (FR-STU-00/AC-05).

---

### [FR-STU-01] Tra cứu hướng dẫn và FAQ

**Priority:** Trung bình: giúp giảm Ticket không cần thiết nhưng luồng Ticket vẫn chạy khi chưa có FAQ; là FR cắt giảm đầu tiên nếu thiếu thời gian (qua CR). **Mốc giao:** MS-02.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Dữ liệu FAQ tạm thời không khả dụng: hệ thống hiển thị thông báo phù hợp và không tự động tạo Ticket.

#### 6. Quy tắc nghiệp vụ
- FAQ chỉ hỗ trợ tra cứu, không thay thế quy trình xử lý Ticket.
- Không bao gồm chatbot AI hoặc hệ thống CMS FAQ chuyên biệt.
- Nội dung FAQ được nạp sẵn khi triển khai; phạm vi hiện tại không bao gồm chức năng thêm, sửa hoặc xóa FAQ trên giao diện.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-01/AC-01:** Sinh viên xem được danh sách FAQ theo các nhóm vấn đề đang hoạt động.
- **FR-STU-01/AC-02:** Tìm theo từ khóa hoặc chọn nhóm vấn đề trả về các FAQ khớp; không có kết quả thì hiển thị "không tìm thấy" kèm nút chuyển sang tạo Ticket.
- **FR-STU-01/AC-03:** Từ một FAQ hoặc từ màn hình không tìm thấy, sinh viên chuyển được sang màn hình tạo Ticket.
- **FR-STU-01/AC-04:** Khi dữ liệu FAQ không tải được, màn hình hiển thị thông báo "chưa thể tải hướng dẫn, vui lòng thử lại" và không có Ticket nào được tạo tự động.
- **FR-STU-01/AC-05:** Xem và tìm FAQ không tạo hay thay đổi Ticket nào; Student Portal không có chức năng thêm, sửa, xóa FAQ và không có chatbot.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Không tìm thấy nội dung phù hợp:** hệ thống hiển thị trạng thái không tìm thấy và nút chuyển sang tạo Ticket (chuyển từ mục 5).
- **A2 — Duyệt theo nhóm, không tìm kiếm:** sinh viên chỉ chọn Nhóm vấn đề trong danh sách mà không nhập từ khóa; hệ thống hiển thị toàn bộ FAQ của nhóm.

#### 9. Ví dụ Edge Case
- Từ khóa chỉ có khoảng trắng hoặc rỗng: hiển thị toàn bộ FAQ theo nhóm, không báo lỗi.
- Từ khóa có dấu/không dấu ("hoc phi" và "học phí"): cả hai trả về FAQ học phí.
- Nhóm vấn đề đã bị vô hiệu hóa: FAQ của nhóm đó không hiển thị.

---

### [FR-STU-02] Tạo và gửi yêu cầu hỗ trợ

**Priority:** Cao: là điểm khởi đầu của toàn bộ vòng đời Ticket. **Mốc giao:** MS-02.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
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
- **FR-STU-02/AC-01:** Dữ liệu hợp lệ tạo đúng một Ticket ở trạng thái `NEW`; màn hình hiển thị thông báo thành công kèm mã Ticket vừa tạo.
- **FR-STU-02/AC-02:** Ticket mới có mã duy nhất trong hệ thống và thuộc đúng sinh viên tạo.
- **FR-STU-02/AC-03:** Ticket mới được gắn đúng Category, phòng ban tiếp nhận theo cấu hình, priority `MEDIUM` và Deadline 03 ngày làm việc (`BR-DUE-01`).
- **FR-STU-02/AC-04:** Thiếu Category, hoặc nội dung rỗng, chỉ có khoảng trắng, dưới 20 hoặc trên 2.000 ký tự: không tạo Ticket; form giữ nguyên dữ liệu đã nhập và hiển thị thông báo ngay tại trường cần sửa.
- **FR-STU-02/AC-05:** File sai định dạng (ngoài PDF/PNG/JPG/JPEG), trên 10 MB hoặc vượt 03 file: file đó bị loại kèm thông báo nêu tên file và lý do; các file hợp lệ vẫn được giữ trên form.
- **FR-STU-02/AC-06:** Bấm gửi nhiều lần hoặc gửi lại cùng một form chỉ tạo một Ticket.
- **FR-STU-02/AC-07:** Category bị vô hiệu hóa sau khi sinh viên mở form: lúc gửi không tạo Ticket, hiển thị thông báo yêu cầu chọn lại Category, danh sách Category chỉ còn các mục đang hoạt động.
- **FR-STU-02/AC-08:** Form tạo Ticket không có trường chọn người phụ trách; Ticket mới chưa có người phụ trách.
- **FR-STU-02/AC-09:** File đính kèm của Ticket chỉ xem/tải được bởi sinh viên tạo Ticket và người có quyền xử lý (`BR-FILE-01`); người khác mở đường dẫn file nhận thông báo "không có quyền truy cập".

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Tạo Ticket không có file:** sinh viên bỏ qua bước 4; Ticket vẫn được tạo bình thường.
- **A2 — Có cả file hợp lệ và file không hợp lệ:** hệ thống loại file sai quy định, giữ file hợp lệ trên form và cho sinh viên gửi lại mà không phải nhập lại nội dung.

#### 9. Ví dụ Edge Case
- Nội dung đúng 19 ký tự: từ chối; đúng 20 ký tự: chấp nhận; 2.000 ký tự: chấp nhận; 2.001 ký tự: từ chối.
- File đúng 10 MB: chấp nhận; 10 MB + 1 byte: từ chối. Chọn 4 file: chỉ nhận 3 và báo vượt số lượng.
- File `.docx` hoặc `.zip`: bị từ chối vì ngoài định dạng PDF/PNG/JPG/JPEG (`BR-FILE-02`).
- Bấm Gửi hai lần liên tiếp hoặc mạng chậm rồi gửi lại: chỉ một Ticket được tạo (FR-STU-02/AC-06).
- Category bị vô hiệu hóa giữa lúc sinh viên đang điền form: lúc gửi bị từ chối và yêu cầu chọn lại.

---

### [FR-STU-03] Xem và theo dõi Ticket

**Priority:** Cao: sinh viên phải theo dõi được Ticket; là mục tiêu minh bạch tiến độ của dự án. **Mốc giao:** MS-02 (nền tảng), MS-03/MS-04 (sự kiện theo chức năng nguồn).

**Nghiệm thu tăng dần của FR-STU-03/04:** MS-02 kiểm tạo/tiếp nhận (NEW → IN_PROGRESS), danh sách/chi tiết, lịch sử và thông báo in-app, mở/đánh dấu đã đọc cùng kiểm quyền. MS-03 thêm yêu cầu/bổ sung thông tin, chuyển phòng ban và thay đổi trạng thái tương ứng; Escalation/ghi chú xử lý vẫn nội bộ. MS-04 thêm kết quả/RESOLVED, mở lại, xác nhận và tự đóng; chạy regression đủ các sự kiện. AC bao quát vòng đời chỉ hoàn tất khi sự kiện cuối được giao, không yêu cầu bổ sung/Transfer/resolve/reopen/close ở MS-02. Không thêm email/SMS. Deadline và kết quả chỉ nghiệm thu khi chức năng nguồn tương ứng đã được giao.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Không có Ticket: hiển thị trạng thái danh sách trống.
- Ticket không thuộc sinh viên đang đăng nhập: từ chối truy cập và không hiển thị dữ liệu Ticket.

#### 6. Quy tắc nghiệp vụ
- Transfer và Escalation là hành động được ghi trong lịch sử xử lý, không phải trạng thái Ticket. Trong Student Portal, sinh viên thấy sự kiện chuyển phòng ban; Escalation là sự kiện nội bộ (`BR-OWN-03`) và không hiển thị cho sinh viên.
- Lịch sử hiển thị cho sinh viên tối thiểu gồm: tạo Ticket, thay đổi trạng thái, yêu cầu bổ sung, sinh viên bổ sung thông tin/tài liệu, chuyển phòng ban, ghi nhận kết quả, mở lại và đóng Ticket.
- Ghi chú xử lý là nội bộ, không công bố cho sinh viên. Sinh viên thấy trạng thái vòng đời, đơn vị/người phụ trách, yêu cầu bổ sung/kết quả và sự kiện được phép, không phải toàn bộ trao đổi nội bộ.
- Các sự kiện quản trị hoặc Audit Trail không liên quan trực tiếp đến quá trình hỗ trợ của sinh viên không hiển thị trong Student Portal.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-03/AC-01:** Danh sách chỉ chứa Ticket của sinh viên đang đăng nhập, Ticket cập nhật gần nhất ở đầu, mỗi dòng có mã, Category, thời điểm tạo và trạng thái.
- **FR-STU-03/AC-02:** Chi tiết Ticket hiển thị đúng trạng thái hiện tại, phòng ban/người phụ trách (nếu đã phân công), Deadline, file được phép xem và kết quả nếu có.
- **FR-STU-03/AC-03:** Mở Ticket của sinh viên khác bằng đường dẫn hoặc mã Ticket: hiển thị trang "không tìm thấy hoặc không có quyền", không hiện mã, nội dung hay file của Ticket đó.
- **FR-STU-03/AC-04:** Khi trạng thái, phòng ban hoặc người phụ trách thay đổi hợp lệ, lần tải tiếp theo hiển thị giá trị mới.
- **FR-STU-03/AC-05:** Sinh viên chưa có Ticket nào: hiển thị danh sách trống kèm nút tạo Ticket.
- **FR-STU-03/AC-06:** Lịch sử hiển thị sự kiện chuyển phòng ban nhưng không hiển thị sự kiện Escalation (`BR-OWN-03`).
- **FR-STU-03/AC-07:** Lịch sử có đủ các sự kiện tối thiểu (tạo, đổi trạng thái, yêu cầu bổ sung, sinh viên bổ sung, chuyển phòng ban, ghi kết quả, mở lại, đóng); không hiển thị ghi chú xử lý nội bộ hoặc sự kiện quản trị như thay đổi tài khoản hay cấu hình, kể cả nội dung trả về từ API chi tiết/lịch sử cho sinh viên.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Tìm theo mã Ticket:** sinh viên nhập mã; hệ thống chỉ trả kết quả nếu Ticket thuộc sinh viên.
- **A2 — Lọc theo trạng thái:** danh sách chỉ hiển thị Ticket ở trạng thái đã chọn, vẫn ưu tiên Ticket cập nhật gần nhất.
- **A3 — Mở từ thông báo:** sinh viên mở chi tiết Ticket qua thông báo (FR-STU-04).

#### 9. Ví dụ Edge Case
- Sinh viên chưa có Ticket nào: hiển thị danh sách trống kèm nút tạo Ticket.
- Đổi ID trên URL sang Ticket của sinh viên khác: bị từ chối, không lộ mã hay tiêu đề Ticket (FR-STU-03/AC-03).
- Ticket vừa Transfer: sinh viên thấy phòng ban mới, không thấy người phụ trách cũ; không thấy sự kiện Escalation.
- Ticket có trên 100 sự kiện lịch sử: vẫn hiển thị đủ, theo thứ tự thời gian.

---

### [FR-STU-04] Nhận và xem thông báo Ticket

**Priority:** Trung bình: sinh viên vẫn theo dõi được bằng FR-STU-03 khi thông báo chậm; thông báo cải thiện trải nghiệm nhưng không chặn luồng Ticket. **Mốc giao:** MS-02 (nền tảng), MS-03 (bổ sung/Transfer), MS-04 (kết quả/mở lại/đóng và regression đầy đủ).

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Ticket không còn thuộc phạm vi truy cập: không cho phép mở chi tiết thông qua thông báo.
- Thông báo không còn liên kết đến dữ liệu hợp lệ: hiển thị thông báo phù hợp và không làm lộ dữ liệu.

#### 6. Quy tắc nghiệp vụ
- Chỉ gửi thông báo đến sinh viên sở hữu Ticket.
- Thông báo không được làm lộ dữ liệu của Ticket khác.
- Thông báo của M01 là **thông báo trong hệ thống (in-app notification)**.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-04/AC-01:** Mỗi sự kiện trong danh sách ở mục 4 (tạo, đổi trạng thái, yêu cầu bổ sung, chuyển phòng ban, có kết quả, mở lại, đóng) tạo đúng một thông báo trong hệ thống cho sinh viên sở hữu Ticket.
- **FR-STU-04/AC-02:** Bấm vào thông báo mở đúng chi tiết Ticket liên quan.
- **FR-STU-04/AC-03:** Mở thông báo hoặc đánh dấu đã đọc làm thông báo chuyển sang "đã đọc" và số thông báo chưa đọc giảm tương ứng, giống nhau trên mọi thiết bị.
- **FR-STU-04/AC-04:** Sinh viên không thấy thông báo của tài khoản khác; mở thông báo của người khác bằng đường dẫn nhận trang "không có quyền truy cập".
- **FR-STU-04/AC-05:** Thông báo trỏ tới Ticket không còn truy cập được hoặc không còn tồn tại: hiển thị "nội dung không còn khả dụng", không hiện mã hay nội dung Ticket.
- **FR-STU-04/AC-06:** Thông báo chỉ hiển thị trong Student Portal (in-app); hệ thống không gửi email hay SMS.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Mở lại thông báo đã đọc:** vẫn điều hướng đến Ticket liên quan; trạng thái giữ là đã đọc.
- **A2 — Nhiều sự kiện liên tiếp trên cùng Ticket:** mỗi sự kiện tạo một thông báo riêng, sắp theo thời gian.

#### 9. Ví dụ Edge Case
- Thông báo của Ticket đã bị Transfer: vẫn mở được vì Ticket vẫn thuộc sinh viên.
- Mở thông báo trên hai thiết bị: trạng thái đã đọc đồng bộ ở cả hai (FR-STU-04/AC-03).
- Sự kiện Escalation: không tạo thông báo cho sinh viên.
- Đổi ID thông báo trên URL sang thông báo của tài khoản khác: bị từ chối (FR-STU-04/AC-04).

---

### [FR-STU-05] Bổ sung thông tin và tài liệu

**Priority:** Cao: không có bước bổ sung thì Ticket `WAITING_STUDENT` bị kẹt và thời hạn xử lý tính sai. **Mốc giao:** MS-03.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Không có nội dung và không có file: từ chối gửi bổ sung.
- Ticket không còn ở `WAITING_STUDENT`: từ chối thao tác và hiển thị trạng thái mới nhất.
- File không hợp lệ: áp dụng quy tắc file dùng chung.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-SUP-01`, `BR-FILE-02` và `BR-DUE-02`.
- Bổ sung thành công phải được ghi nhận trong lịch sử Ticket.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-05/AC-01:** Ticket `WAITING_STUDENT` nhận bổ sung hợp lệ (nội dung, file hoặc cả hai) và chuyển về `IN_PROGRESS`.
- **FR-STU-05/AC-02:** Nội dung/file bổ sung được lưu đúng Ticket, hiện trong lịch sử Ticket và nhân viên có quyền mở được.
- **FR-STU-05/AC-03:** Gửi bổ sung khi Ticket không còn ở `WAITING_STUDENT`: hiển thị thông báo kèm trạng thái mới nhất của Ticket; không có nội dung hay file nào được lưu.
- **FR-STU-05/AC-04:** Thời gian Ticket ở `WAITING_STUDENT` không tính vào thời gian xử lý; Deadline sau khi bổ sung bằng thời điểm bổ sung cộng phần thời hạn còn lại (`BR-DUE-02`).
- **FR-STU-05/AC-05:** Không nhập nội dung và không đính kèm file: hiển thị thông báo "cần nhập nội dung hoặc đính kèm file", Ticket giữ `WAITING_STUDENT`.
- **FR-STU-05/AC-06:** Nội dung trên 2.000 ký tự hoặc file sai quy tắc (`BR-FILE-02`): thông báo nêu lý do tại trường/file đó; file sai bị loại, phần hợp lệ được giữ trên form.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Chỉ gửi nội dung, không có file** hoặc **A2 — chỉ gửi file, không có nội dung:** đều hợp lệ vì đủ "ít nhất một trong hai".
- **A3 — Bổ sung khi Ticket đã được Transfer:** yêu cầu bổ sung vẫn còn hiệu lực; nội dung bổ sung đến phòng ban mới.

#### 9. Ví dụ Edge Case
- Nội dung 2.000 ký tự: chấp nhận; 2.001: từ chối.
- Hai tab cùng gửi bổ sung: tab đầu thành công, tab sau bị từ chối vì Ticket đã về `IN_PROGRESS`.
- Ticket ở `WAITING_STUDENT` 5 ngày rồi được bổ sung: phần thời hạn còn lại giữ nguyên như lúc tạm dừng (FR-STU-05/AC-04).

---

### [FR-STU-06] Xem kết quả, phản hồi và yêu cầu mở lại

**Priority:** Cao: hoàn tất vòng đời Ticket; thiếu FR này Ticket không bao giờ `CLOSED`. **Mốc giao:** MS-04.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Yêu cầu mở lại thiếu lý do: từ chối thao tác.
- Ticket đã `CLOSED` hoặc hết thời hạn phản hồi: không cho phép mở lại.
- Ticket không thuộc sinh viên: từ chối truy cập và thao tác.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-LIFE-01`, `BR-LIFE-02`, `BR-LIFE-03`.
- Reopen chỉ thực hiện từ `RESOLVED` về `IN_PROGRESS`.
- Ticket `CLOSED` không được mở lại.
- Mọi lần chấp nhận, mở lại và tự động đóng phải được ghi nhận trong lịch sử.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-06/AC-01:** Sinh viên xem được nội dung kết quả, tài liệu kết quả và thời hạn phản hồi còn lại của Ticket `RESOLVED` hoặc `CLOSED` thuộc mình.
- **FR-STU-06/AC-02:** Xác nhận kết quả khi Ticket đang `RESOLVED` chuyển Ticket sang `CLOSED` và ghi thời điểm đóng.
- **FR-STU-06/AC-03:** Yêu cầu mở lại có lý do 10–1.000 ký tự và không chỉ chứa khoảng trắng, gửi trong 03 ngày làm việc, chuyển Ticket từ `RESOLVED` về `IN_PROGRESS` và tạo thông báo cho người phụ trách hoặc phòng ban hiện tại.
- **FR-STU-06/AC-04:** Yêu cầu mở lại thiếu lý do, lý do dưới 10 hay trên 1.000 ký tự, hoặc chỉ chứa khoảng trắng dù độ dài đầu vào nằm trong 10–1.000 ký tự: hệ thống từ chối, kể cả yêu cầu gửi trực tiếp, với thông báo nêu yêu cầu về lý do; Ticket giữ `RESOLVED`, không ghi sự kiện mở lại hoặc gửi thông báo mở lại.
- **FR-STU-06/AC-05:** Ticket `RESOLVED` quá 03 ngày làm việc mà không có yêu cầu xử lý tiếp được hệ thống tự chuyển sang `CLOSED`.
- **FR-STU-06/AC-06:** Ticket đã `CLOSED` hoặc đã hết thời hạn phản hồi: không còn nút mở lại; yêu cầu mở lại gửi trực tiếp bị từ chối với thông báo "Ticket đã đóng hoặc hết thời hạn phản hồi", trạng thái không đổi.
- **FR-STU-06/AC-07:** Sinh viên mở hoặc thao tác trên Ticket của người khác: trang "không có quyền truy cập", không hiển thị kết quả, trạng thái Ticket không đổi.
- **FR-STU-06/AC-08:** Mỗi lần chấp nhận, mở lại và tự động đóng tạo một sự kiện trong lịch sử Ticket, ghi người thực hiện (hoặc "hệ thống") và thời điểm.
- **FR-STU-06/AC-09:** Mở lại hợp lệ giữ nguyên kết quả, tài liệu kết quả, thời điểm giải quyết và lịch sử của vòng trước; chỉ thêm sự kiện mở lại và bắt đầu/tiếp tục vòng xử lý theo BR-DUE-02, không ghi đè/xóa bằng chứng cũ khi ghi kết quả vòng sau.

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (mở lại) và Luồng C (tự động đóng) ở mục 4 là luồng thay thế của Luồng A (chấp nhận kết quả).
- **A1 — Xem kết quả của Ticket đã `CLOSED`:** sinh viên chỉ xem được, không còn nút chấp nhận hay mở lại.

#### 9. Ví dụ Edge Case
- Yêu cầu mở lại ngay trước khi đủ 03 ngày làm việc (24 giờ làm việc theo `BR-DUE-02`) kể từ `RESOLVED`: chấp nhận; ngay sau thời điểm đó: từ chối. Cuối tuần và ngoài giờ không tính.
- Với lý do không chỉ chứa khoảng trắng và các điều kiện mở lại khác hợp lệ: 9 ký tự bị từ chối; 10 và 1.000 ký tự được chấp nhận; 1.001 ký tự bị từ chối. Đầu vào gồm toàn 10 hoặc 1.000 dấu cách vẫn bị từ chối.
- Sinh viên bấm "Chấp nhận" đúng lúc job tự động đóng chạy: Ticket chỉ chuyển `CLOSED` một lần, lịch sử chỉ có một sự kiện đóng.
- Ticket đã mở lại một lần và được `RESOLVED` lần hai: sinh viên vẫn được mở lại trong thời hạn mới.

---

### [FR-STU-07] Đánh giá mức độ hài lòng (CSAT)

**Priority:** Trung bình: cung cấp dữ liệu CSAT cho báo cáo nhưng không ảnh hưởng xử lý Ticket. **Mốc giao:** MS-04.

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

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Không chọn điểm: từ chối gửi.
- Ticket đã có đánh giá: không cho gửi lần hai.
- Quá 07 ngày theo lịch kể từ khi Ticket chuyển sang `CLOSED`: không cho gửi đánh giá mới.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-CSAT-01`.
- Đánh giá không làm thay đổi trạng thái Ticket.

#### 7. Tiêu chí nghiệm thu
- **FR-STU-07/AC-01:** Ticket `CLOSED` thuộc sinh viên, chưa có đánh giá, trong 07 ngày theo lịch kể từ khi đóng, nhận đánh giá 1–5 sao kèm nhận xét tùy chọn tối đa 500 ký tự.
- **FR-STU-07/AC-02:** Đánh giá hợp lệ được lưu đúng Ticket và được tính vào báo cáo CSAT (FR-MGT-06).
- **FR-STU-07/AC-03:** Ticket đã có đánh giá: không còn form đánh giá; đánh giá gửi lần hai bị từ chối với thông báo "Ticket đã được đánh giá", đánh giá cũ giữ nguyên.
- **FR-STU-07/AC-04:** Quá 07 ngày theo lịch kể từ khi `CLOSED`: không còn form đánh giá; đánh giá gửi trực tiếp bị từ chối với thông báo hết thời hạn, không có đánh giá nào được lưu.
- **FR-STU-07/AC-05:** Gửi CSAT không làm thay đổi trạng thái `CLOSED`.
- **FR-STU-07/AC-06:** Gửi mà không chọn số sao, hoặc nhận xét trên 500 ký tự: thông báo nêu trường cần sửa, không lưu đánh giá.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Đánh giá không kèm nhận xét:** chỉ chọn số sao rồi gửi.
- **A2 — Ticket tự động đóng:** sinh viên vẫn được đánh giá trong 07 ngày kể từ lúc tự đóng.

#### 9. Ví dụ Edge Case
- Gửi đánh giá ở ngày thứ 7 theo lịch: chấp nhận; ngày thứ 8: từ chối (FR-STU-07/AC-04).
- Nhận xét 500 ký tự: chấp nhận; 501: từ chối.
- Gửi đánh giá đồng thời từ hai tab: chỉ một đánh giá được lưu (FR-STU-07/AC-03).
- Điểm 0 hoặc 6 gửi trực tiếp qua API: bị từ chối.

---

## III. QUY TẮC THAM CHIẾU

Các Functional Requirements của M01 phải tuân thủ thống nhất với:

- [Ticket Lifecycle](../../02-domain/ticket-lifecycle.md)
- [State Transition](../../02-domain/state-transition.md)
- [Business Rules](../../02-domain/business-rules.md)
