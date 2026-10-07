# Tài Liệu Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Sinh Viên (PRD - M01 Student Portal)

## 1. Tổng Quan Phân Hệ & Cơ Cấu Effort Baseline

Phân hệ **Sinh viên (Student Portal)** là điểm giao tiếp số duy nhất dành cho khoảng 3.000 sinh viên tại **Aurora University**. Phân hệ này cho phép sinh viên khởi tạo, theo dõi, tương tác và đánh giá toàn bộ các yêu cầu hỗ trợ (Ticket) từ hành chính, đào tạo, học phí cho đến kỹ thuật.

### Bảng Phân Rã Chức Năng & Baseline Effort (Tổng: 128h)

| Mã FR | Tên Chức Năng | Tóm Tắt Scope Nghiệp Vụ | Effort (Giờ) |
| :--- | :--- | :--- | :---: |
| **FR-STU-01** | Đăng nhập tài khoản Sinh viên | Đăng nhập xác thực tài khoản sinh viên do nhà trường cấp. | **16h** |
| **FR-STU-02** | Gửi yêu cầu hỗ trợ | Chọn loại dịch vụ, nhập thông tin, đính kèm file, sinh Mã Ticket duy nhất. | **36h** |
| **FR-STU-03** | Xem tiến độ & Lịch sử xử lý Ticket | Lọc/xem danh sách Ticket cá nhân, chi tiết timeline xử lý real-time. | **32h** |
| **FR-STU-04** | Phản hồi & Bổ sung thông tin / Hồ sơ | Cập nhật câu trả lời/file minh chứng khi Ticket ở trạng thái `WAITING_STUDENT`. | **20h** |
| **FR-STU-05** | Xem kết quả giải quyết & Đánh giá (CSAT) | Xem kết quả xử lý chính thức, tải file đáp ứng, chấm điểm CSAT (1-5 sao). | **24h** |
| **TỔNG CỘNG** | | | **128h** |

---

### [FR-STU-01] Đăng nhập tài khoản Sinh viên

**Mô tả**  
Hệ thống cho phép Sinh viên xác thực tài khoản cá nhân do Aurora University cấp để truy cập vào Phân hệ Sinh viên.

**Actor**  
Sinh viên (Student).

**Preconditions**  
- Sinh viên có tài khoản được cấp trong hệ thống UniSupport.
- Tài khoản đang ở trạng thái hoạt động (`Active`).

**Luồng chính**  
1. Sinh viên truy cập vào địa chỉ trang web UniSupport.
2. Hệ thống hiển thị màn hình Đăng nhập.
3. Sinh viên nhập **Mã sinh viên / Email sinh viên** và **Mật khẩu**.
4. Sinh viên nhấn nút **Đăng nhập**.
5. Hệ thống kiểm tra thông tin xác thực.
6. Khi xác thực thành công, hệ thống điều hướng Sinh viên vào Màn hình chính (Dashboard Sinh viên).

**Business Rules**  
- Mật khẩu phải được mã hóa an toàn trên đường truyền và cơ sở dữ liệu.
- Hệ thống khóa tài khoản tạm thời (5 phút) nếu nhập sai mật khẩu quá 5 lần liên tiếp.
- Phiên đăng nhập (Session/Token) duy trì tối đa 24 giờ nếu không đăng xuất.

**Alternative / Error Flows**  
- **Nhập sai tài khoản hoặc mật khẩu**: Hệ thống hiển thị thông báo "Tên đăng nhập hoặc mật khẩu không chính xác" (không chỉ rõ sai trường nào để bảo mật).
- **Tài khoản bị khóa**: Hệ thống hiển thị thông báo "Tài khoản của bạn tạm thời bị khóa. Vui lòng liên hệ Admin".

**Acceptance Criteria**  
- **AC-01**: Sinh viên nhập đúng tên tài khoản và mật khẩu -> Đăng nhập thành công và vào trang Dashboard.
- **AC-02**: Sinh viên nhập sai mật khẩu -> Dừng đăng nhập, hiển thị thông báo lỗi và không tạo phiên làm việc.
- **AC-03**: Sinh viên để trống tên tài khoản hoặc mật khẩu -> Nút Đăng nhập không hoạt động hoặc báo lỗi validation trường dữ liệu.

**Ví dụ Edge Case**  
Sinh viên nhập sai mật khẩu liên tiếp 5 lần.  
-> **Expected Result**: Hệ thống từ chối đăng nhập ở lần thứ 6 và hiển thị thông báo khóa tài khoản tạm thời 5 phút.

---

### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ

**Mô tả**  
Hệ thống cho phép sinh viên tạo một Ticket hỗ trợ bằng cách nhập thông tin mô tả vấn đề gặp phải, chọn phòng ban/nhóm vấn đề và đính kèm file minh chứng (nếu có), sau đó gửi yêu cầu đến bộ phận phụ trách.

**Actor**  
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**  
- Sinh viên đã đăng nhập thành công.
- Sinh viên có quyền tạo Ticket.

**Luồng chính**  
1. Sinh viên mở chức năng **Tạo Ticket**.
2. Hệ thống hiển thị form tạo Ticket.
3. Sinh viên chọn **Phòng ban / Nhóm vấn đề**, nhập **Tiêu đề** và **Mô tả chi tiết**.
4. Sinh viên đính kèm file minh chứng (nếu có, hỗ trợ PDF/PNG/JPG, tối đa 10MB/file, tối đa 3 file).
5. Sinh viên nhấn nút **Gửi yêu cầu**.
6. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
7. Nếu dữ liệu hợp lệ, hệ thống tạo Ticket mới, sinh **Mã Ticket duy nhất** (Ví dụ: `TK-20261004-001`).
8. Hệ thống lưu file đính kèm vào bộ nhớ bảo mật và liên kết với Ticket.
9. Hệ thống chuyển Ticket về trạng thái `NEW` và phát thông báo cho Phòng ban phụ trách.
10. Hệ thống hiển thị thông báo tạo Ticket thành công và cung cấp Mã Ticket cho sinh viên.

**Business Rules**  
- Tiêu đề và Mô tả vấn đề là các trường thông tin bắt buộc.
- Nội dung chỉ chứa khoảng trắng được xem là không hợp lệ.
- File đính kèm chỉ chấp nhận định dạng `.pdf`, `.png`, `.jpg`, `.jpeg` với dung lượng tối đa 10MB/file.
- Thao tác gửi của sinh viên chỉ tạo tối đa **một Ticket**, kể cả khi nhấn nút gửi nhiều lần do double-click, gián đoạn mạng hoặc retry.
- Ticket sau khi tạo phải được liên kết cố định với tài khoản sinh viên gửi yêu cầu.

**Alternative / Error Flows**  
- **Thiếu thông tin bắt buộc**: Hệ thống không tạo Ticket và hiển thị thông báo yêu cầu sinh viên bổ sung thông tin.
- **File đính kèm không hợp lệ (sai định dạng hoặc >10MB)**: Hệ thống hiển thị lỗi cụ thể bên dưới ô upload file và dừng quá trình gửi.
- **Sự cố hệ thống / Database**: Hệ thống hiển thị thông báo lỗi kỹ thuật, hoàn tác giao dịch và không lưu dữ liệu không hoàn chỉnh.

**Acceptance Criteria**  
- **AC-01**: Sinh viên nhập đầy đủ thông tin hợp lệ và chọn **Gửi yêu cầu** -> Hệ thống tạo đúng một Ticket với Mã duy nhất và hiển thị thông báo thành công.
- **AC-02**: Sinh viên để trống trường mô tả -> Hệ thống không tạo Ticket và hiển thị lỗi validation.
- **AC-03**: Sinh viên đính kèm file vượt quá 10MB -> Hệ thống báo lỗi file quá dung lượng cho phép.
- **AC-04**: Sinh viên nhấn nút **Gửi yêu cầu** nhiều lần liên tiếp -> Hệ thống chỉ tạo duy nhất 01 Ticket.
- **AC-05**: Ticket được tạo lưu đúng thông tin sinh viên gửi và xuất hiện trong danh sách Ticket cá nhân.

**Ví dụ Edge Case**  
Sinh viên nhấn nút **Gửi yêu cầu** 5 lần liên tiếp trong thời gian ngắn do gián đoạn mạng.  
-> **Expected Result**: Hệ thống xử lý request đầu tiên, vô hiệu hóa nút bấm (Disable) và chỉ ghi nhận **duy nhất một Ticket** cho thao tác gửi đó.

---

### [FR-STU-03] Xem danh sách & Theo dõi tiến độ xử lý Ticket

**Mô tả**  
Hệ thống hiển thị danh sách các Ticket do sinh viên tạo ra và cho phép xem chi tiết tiến độ xử lý, lịch sử phản hồi theo thời gian thực.

**Actor**  
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**  
- Sinh viên đã đăng nhập thành công.

**Luồng chính**  
1. Sinh viên truy cập vào mục **Danh sách Ticket của tôi**.
2. Hệ thống hiển thị danh sách tất cả các Ticket sinh viên đã gửi, sắp xếp theo thời gian tạo mới nhất.
3. Sinh viên xem được các thông tin tóm tắt: Mã Ticket, Tiêu đề, Ngày tạo, Phòng ban phụ trách, Trạng thái hiện tại (`NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`).
4. Sinh viên nhấn vào một Ticket cụ thể để xem **Chi tiết Ticket**.
5. Hệ thống hiển thị toàn bộ nội dung yêu cầu, file đính kèm, thông tin nhân viên thụ lý (nếu có) và dòng thời gian (Timeline) các bước xử lý.

**Business Rules**  
- Sinh viên **chỉ nhìn thấy và truy cập được** các Ticket do chính tài khoản của mình khởi tạo.
- Trạng thái Ticket được cập nhật thời gian thực (Real-time hoặc khi tải lại trang).
- Mọi nhật ký trao đổi công khai đều được sắp xếp theo trình tự thời gian tăng dần.

**Alternative / Error Flows**  
- **Sinh viên không có Ticket nào**: Hệ thống hiển thị giao diện trống (Empty state) kèm gợi ý "Bạn chưa có yêu cầu hỗ trợ nào. Nhấn vào đây để tạo mới".
- **Sinh viên cố tình nhập URL Ticket của người khác**: Hệ thống từ chối truy cập (Lỗi `403 Forbidden`) và điều hướng về danh sách cá nhân.

**Acceptance Criteria**  
- **AC-01**: Màn hình danh sách hiển thị đúng và đủ các Ticket thuộc sở hữu của sinh viên đăng nhập.
- **AC-02**: Khi nhấn vào 01 Ticket, màn hình chi tiết hiển thị đầy đủ thông tin lịch sử xử lý và file đính kèm gốc.
- **AC-03**: Sinh viên truy cập trái phép Ticket của sinh viên khác -> Hệ thống báo lỗi không có quyền truy cập.

**Ví dụ Edge Case**  
Sinh viên copy đường dẫn chi tiết Ticket `TK-20261004-001` gửi cho một sinh viên khác đăng nhập xem thử.  
-> **Expected Result**: Hệ thống phát hiện tài khoản truy cập không phải người tạo, chặn hiển thị và báo lỗi "Bạn không có quyền xem Ticket này".

---

### [FR-STU-04] Phản hồi & Bổ sung thông tin / Hồ sơ theo yêu cầu

**Mô tả**  
Khi Ticket ở trạng thái `WAITING_STUDENT`, sinh viên có thể nhập câu trả lời bổ sung và tải lên các file giấy tờ theo yêu cầu của nhân viên.

**Actor**  
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**  
- Sinh viên đã đăng nhập thành công.
- Ticket tương ứng đang ở trạng thái `WAITING_STUDENT`.

**Luồng chính**  
1. Sinh viên mở màn hình Chi tiết Ticket đang ở trạng thái `WAITING_STUDENT`.
2. Sinh viên xem nội dung ghi chú/yêu cầu bổ sung từ nhân viên.
3. Sinh viên nhập câu trả lời bổ sung vào khung phản hồi.
4. Sinh viên chọn file đính kèm mới (nếu nhân viên yêu cầu bổ sung giấy tờ/ảnh chụp).
5. Sinh viên nhấn nút **Gửi phản hồi bổ sung**.
6. Hệ thống lưu nội dung phản hồi, lưu file đính kèm bổ sung.
7. Hệ thống tự động chuyển trạng thái Ticket từ `WAITING_STUDENT` về `IN_PROGRESS`.
8. Bộ đếm thời gian SLA xử lý của nhân viên tiếp tục chạy lại.

**Business Rules**  
- Tính năng gửi bổ sung chỉ kích hoạt khi Ticket ở trạng thái `WAITING_STUDENT`.
- Ngay khi sinh viên gửi bổ sung thành công, trạng thái **bắt buộc** phải chuyển về `IN_PROGRESS`.
- Nội dung phản hồi bổ sung không được để trống.

**Alternative / Error Flows**  
- **Sinh viên gửi phản hồi nhưng để trống nội dung và không có file**: Hệ thống báo lỗi "Vui lòng nhập nội dung trả lời hoặc tải lên file đính kèm".
- **Ticket đã bị đóng hoặc chuyển trạng thái trước khi gửi**: Hệ thống thông báo trạng thái Ticket đã thay đổi và làm mới lại trang.

**Acceptance Criteria**  
- **AC-01**: Sinh viên nhập thông tin bổ sung và nhấn gửi -> Phản hồi hiển thị trong lịch sử, trạng thái Ticket chuyển thành `IN_PROGRESS`.
- **AC-02**: Sinh viên đính kèm thêm file minh chứng -> File được tải lên thành công và nhân viên phụ trách xem được.
- **AC-03**: Nút gửi phản hồi bổ sung bị ẩn/khóa nếu Ticket không ở trạng thái `WAITING_STUDENT`.

**Ví dụ Edge Case**  
Sinh viên đang soạn nội dung bổ sung thì nhân viên chủ động hủy hoặc chuyển trạng thái Ticket. Khi sinh viên bấm Gửi phản hồi:  
-> **Expected Result**: Hệ thống báo lỗi "Trạng thái Ticket đã thay đổi. Vui lòng tải lại trang", không lưu dữ liệu thừa.

---

### [FR-STU-05] Xem kết quả giải quyết & Đánh giá mức độ hài lòng (CSAT)

**Mô tả**  
Cho phép sinh viên xem nội dung kết quả xử lý chính thức từ nhà trường, nhận file đính kèm kết quả (nếu có) và thực hiện chấm điểm hài lòng đối với dịch vụ hỗ trợ.

**Actor**  
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**  
- Ticket của sinh viên đã được nhân viên chuyển sang trạng thái `RESOLVED` hoặc `CLOSED`.

**Luồng chính**  
1. Sinh viên mở chi tiết Ticket đã giải quyết.
2. Sinh viên xem nội dung kết quả giải quyết và tải file phản hồi (nếu có).
3. Hệ thống hiển thị khung **Đánh giá mức độ hài lòng (CSAT)**.
4. Sinh viên chọn số sao đánh giá (từ 1 đến 5 sao).
5. Sinh viên nhập nhận xét/góp ý thêm (không bắt buộc).
6. Sinh viên nhấn nút **Gửi đánh giá**.
7. Hệ thống lưu kết quả đánh giá, ghi nhận mốc thời gian.
8. Hệ thống chuyển trạng thái Ticket thành `CLOSED` (nếu trước đó đang ở `RESOLVED`).
9. Hệ thống hiển thị thông báo "Cảm ơn bạn đã gửi đánh giá dịch vụ".

**Business Rules**  
- Điểm đánh giá bắt buộc từ 1 đến 5 sao.
- Mỗi Ticket chỉ được phép đánh giá **Duy nhất 01 lần**.
- Thời hạn thực hiện đánh giá là trong vòng **07 ngày** kể từ khi Ticket ở trạng thái `RESOLVED`. Quá 7 ngày, hệ thống tự động khóa tính năng đánh giá.
- Sau khi gửi đánh giá, điểm số và nhận xét không thể chỉnh sửa.

**Alternative / Error Flows**  
- **Sinh viên không bấm gửi đánh giá**: Sau 03 ngày làm việc ở trạng thái `RESOLVED`, hệ thống tự động chuyển Ticket sang `CLOSED`. Sinh viên vẫn có thể đánh giá trong hạn 7 ngày còn lại.
- **Sinh viên cố tình gửi đánh giá lần 2**: Hệ thống ẩn form đánh giá và hiển thị điểm số đã chấm trước đó.

**Acceptance Criteria**  
- **AC-01**: Sinh viên chọn số sao (ví dụ: 5 sao), nhập nhận xét và bấm gửi -> Đánh giá được lưu thành công, Ticket chuyển sang `CLOSED`.
- **AC-02**: Sinh viên không chọn số sao mà bấm gửi -> Hệ thống nhắc nhở chọn điểm số đánh giá.
- **AC-03**: Sau khi đã gửi đánh giá -> Form đánh giá chuyển sang dạng chỉ xem (Read-only), hiển thị điểm đã chấm.

**Ví dụ Edge Case**  
Sinh viên mở form đánh giá của Ticket đã được giải quyết từ 10 ngày trước (đã quá thời hạn 7 ngày).  
-> **Expected Result**: Hệ thống hiển thị thông báo "Đã quá thời hạn gửi đánh giá cho Ticket này" và khóa form nhập liệu.