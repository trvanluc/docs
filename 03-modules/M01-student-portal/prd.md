# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Sinh Viên (PRD - M01 Student Portal)

## 1. Tổng Quan Phân Hệ

Phân hệ **Sinh viên (Student Portal)** là cổng giao tiếp số tập trung dành cho khoảng 3.000 sinh viên tại **Aurora University**. Phân hệ cho phép sinh viên chủ động tra cứu thông tin hướng dẫn, tạo phiếu hỗ trợ (Ticket), theo dõi tiến độ giải quyết, nhận thông báo cập nhật và phản hồi/đánh giá chất lượng dịch vụ.

### Danh mục Chức năng & Phân bổ Công sức (Tổng: 128h)

| Mã Chức Năng | Tên Chức Năng | Phạm Vi Nghiệp Vụ | Effort Cơ Sở | Buffer | Effort Kế Hoạch |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **FR-STU-01** | Tra cứu hướng dẫn & FAQ | Tìm kiếm bài viết hướng dẫn, quy trình thủ tục và câu hỏi thường gặp theo Phòng ban. | 14h | 0h | **14h** |
| **FR-STU-02** | Tạo & gửi yêu cầu hỗ trợ | Chọn nhóm vấn đề, nhập mô tả, đính kèm file (PDF/Ảnh), sinh mã Ticket duy nhất. | 34h | 3h | **37h** |
| **FR-STU-03** | Xem & theo dõi yêu cầu | Xem danh sách Ticket cá nhân, bộ lọc trạng thái, timeline xử lý thời gian thực. | 32h | 1h | **33h** |
| **FR-STU-04** | Nhận thông báo trạng thái | Trung tâm thông báo quả chuông, nhận thông báo tức thời khi Ticket có cập nhật. | 19h | 0h | **19h** |
| **FR-STU-05** | Bổ sung thông tin & phản hồi | Gửi giấy tờ bổ sung khi có yêu cầu, xem kết quả giải quyết và đánh giá CSAT (1–5 sao). | 25h | 0h | **25h** |
| **TỔNG CỘNG** | | | **124h** | **4h** | **128h** |

---

## 2. Đặc Tả Chi Tiết Chức Năng

### [FR-STU-01] Tra cứu hướng dẫn & FAQ

**Mô tả**  
Cung cấp trang tra cứu thông tin tĩnh và câu hỏi thường gặp (FAQ) theo từng Phòng ban chức năng, giúp sinh viên tự giải quyết các thắc mắc phổ biến trước khi gửi yêu cầu hỗ trợ.

**Actor**  
Sinh viên (Student).

**Preconditions**  
Người dùng truy cập vào cổng thông tin UniSupport.

**Luồng chính**  
1. Sinh viên chọn mục **Hướng dẫn & FAQ**.
2. Hệ thống hiển thị danh sách câu hỏi theo các phòng ban (Đào tạo, CTHSSV, Tài chính - Kế toán, Trung tâm CNTT, Thư viện).
3. Sinh viên nhập từ khóa tìm kiếm (hỗ trợ tiếng Việt có dấu và không dấu).
4. Hệ thống lọc và trả về danh sách các bài viết phù hợp.
5. Sinh viên chọn xem chi tiết bài hướng dẫn.
6. Nếu bài viết chưa giải quyết được vấn đề, sinh viên nhấn nút **Gửi yêu cầu hỗ trợ** để chuyển thẳng sang form tạo Ticket với danh mục được điền sẵn.

**Business Rules**  
- Bài viết FAQ được sắp xếp theo mức độ quan tâm và chuyên mục phòng ban.
- Kết quả tìm kiếm trả về thời gian thực khi người dùng nhập từ khóa.

**Alternative / Error Flows**  
- **Không tìm thấy kết quả**: Hệ thống hiển thị gợi ý "Không tìm thấy nội dung phù hợp. Bạn có muốn tạo yêu cầu hỗ trợ gửi đến phòng ban không?" kèm nút tạo Ticket.

**Acceptance Criteria**  
- **AC-01**: Tìm kiếm trả kết quả chính xác theo từ khóa trong vòng dưới 1 giây.
- **AC-02**: Nhấn nút "Gửi yêu cầu hỗ trợ" từ bài viết -> Chuyển đúng sang form tạo Ticket kèm danh mục tương ứng.

**Ví dụ Edge Case**  
Sinh viên nhập từ khóa có ký tự đặc biệt hoặc chỉ có khoảng trắng.  
-> **Expected Result**: Hệ thống xử lý an toàn, loại bỏ ký tự rác và hiển thị thông báo phù hợp mà không gây lỗi giao diện.

---

### [FR-STU-02] Tạo & gửi yêu cầu hỗ trợ

**Mô tả**  
Cho phép sinh viên khởi tạo một yêu cầu hỗ trợ mới bằng cách chọn phòng ban, nhập tiêu đề, nội dung chi tiết và đính kèm tài liệu minh chứng.

**Actor**  
Sinh viên đã đăng nhập hệ thống.

**Preconditions**  
- Sinh viên có tài khoản ở trạng thái hoạt động (`ACTIVE`).

**Luồng chính**  
1. Sinh viên mở chức năng **Tạo yêu cầu**.
2. Hệ thống hiển thị biểu mẫu tạo Ticket.
3. Sinh viên chọn **Phòng ban / Nhóm vấn đề**, nhập **Tiêu đề** và **Nội dung mô tả**.
4. Sinh viên chọn đính kèm file (PDF, PNG, JPG; dung lượng tối đa 10MB/file, tối đa 3 file).
5. Sinh viên nhấn nút **Gửi yêu cầu**.
6. Hệ thống kiểm tra dữ liệu đầu vào và tính hợp lệ của file.
7. Hệ thống tạo bản ghi Ticket mới, sinh **Mã Ticket duy nhất** (ví dụ: `TK-20261004-001`), gán trạng thái `NEW`.
8. Hệ thống lưu trữ file vào thư mục bảo mật và gắn liên kết với Ticket.
9. Hệ thống gửi thông báo tạo thành công cho sinh viên và thông báo đến Hòm thư của phòng ban phụ trách.

**Business Rules**  
- Tiêu đề và Mô tả là các trường bắt buộc, không được để trống hoặc chỉ chứa khoảng trắng.
- Định dạng tệp đính kèm được phép: `.pdf`, `.png`, `.jpg`, `.jpeg`.
- Cơ chế chống gửi lặp (Idempotency / Debounce): Một lần gửi chỉ tạo duy nhất 01 Ticket dù người dùng nhấn nút nhiều lần do mạng chậm.

**Alternative / Error Flows**  
- **Thiếu thông tin bắt buộc**: Báo lỗi validation tại các trường còn thiếu và không gửi form.
- **File vượt quá dung lượng (hoặc sai định dạng)**: Hiển thị thông báo lỗi cụ thể bên dưới khung tải file.
- **Lỗi đường truyền khi upload**: Hệ thống rollback giao dịch, không lưu bản ghi dở dang và thông báo sinh viên thử lại.

**Acceptance Criteria**  
- **AC-01**: Nhập đúng và đủ thông tin -> Tạo đúng 01 Ticket với mã duy nhất, trạng thái `NEW`.
- **AC-02**: Nhấn nút gửi liên tục nhiều lần -> Hệ thống chỉ tạo 01 Ticket duy nhất.
- **AC-03**: File đính kèm lưu an toàn và hiển thị đúng trong chi tiết Ticket.

**Ví dụ Edge Case**  
Sinh viên chọn đính kèm file ảnh 12MB.  
-> **Expected Result**: Hệ thống chặn ngay tại client và hiển thị cảnh báo "Dung lượng tệp vượt quá 10MB cho phép".

---

### [FR-STU-03] Xem & theo dõi yêu cầu

**Mô tả**  
Hiển thị danh sách các Ticket của cá nhân sinh viên và cho phép xem chi tiết tiến độ xử lý, lịch sử phản hồi theo thời gian thực.

**Actor**  
Sinh viên đã đăng nhập hệ thống.

**Preconditions**  
Sinh viên đã đăng nhập tài khoản hợp lệ.

**Luồng chính**  
1. Sinh viên vào mục **Yêu cầu của tôi**.
2. Hệ thống hiển thị bảng danh sách các Ticket do sinh viên tạo: Mã Ticket, Tiêu đề, Phòng ban, Trạng thái (`NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`), Ngày gửi.
3. Sinh viên có thể lọc Ticket theo trạng thái hoặc tìm kiếm theo mã Ticket.
4. Sinh viên nhấn vào một Ticket để xem màn hình **Chi tiết yêu cầu**.
5. Hệ thống hiển thị nội dung yêu cầu, file đính kèm, nhân viên phụ trách (nếu có) và dòng thời gian (Timeline) các bước xử lý.

**Business Rules**  
- Phân quyền dữ liệu nghiêm ngặt: Sinh viên **chỉ nhìn thấy và truy cập** các Ticket do chính tài khoản của mình tạo ra (`created_by_student_id = current_user_id`).
- Mọi nỗ lực truy cập Ticket của người khác qua đường dẫn URL đều bị chặn với mã lỗi `403 Forbidden`.

**Alternative / Error Flows**  
- **Chưa có Ticket nào**: Hiển thị màn hình trống (Empty state) kèm gợi ý tạo yêu cầu mới.
- **Truy cập sai ID**: Hiển thị thông báo không tìm thấy yêu cầu hoặc không có quyền truy cập.

**Acceptance Criteria**  
- **AC-01**: Hiển thị đầy đủ và chính xác danh sách Ticket của sinh viên đăng nhập.
- **AC-02**: Timeline hiển thị đúng trình tự thời gian các bước chuyển trạng thái và phản hồi công khai từ nhân viên.

**Ví dụ Edge Case**  
Sinh viên sao chép liên kết Ticket của bạn học và mở trên trình duyệt của mình.  
-> **Expected Result**: Hệ thống phát hiện không trùng khớp ID người tạo và trả về lỗi `403 Forbidden`.

---

### [FR-STU-04] Nhận thông báo trạng thái

**Mô tả**  
Tiếp nhận và hiển thị các thông báo nội bộ hệ thống (In-app Notification) tức thời khi Ticket có sự thay đổi trạng thái hoặc nhận phản hồi từ phía nhà trường.

**Actor**  
Sinh viên đã đăng nhập hệ thống.

**Preconditions**  
Có sự kiện phát sinh liên quan đến Ticket của sinh viên.

**Luồng chính**  
1. Khi có sự kiện trên Ticket (được tiếp nhận, yêu cầu bổ sung giấy tờ, hoàn thành giải quyết), hệ thống tự động sinh thông báo.
2. Biểu tượng **Quả chuông** trên thanh điều hướng hiển thị số thông báo chưa đọc.
3. Sinh viên nhấn vào Quả chuông để xem danh sách 10 thông báo mới nhất.
4. Sinh viên nhấn vào một thông báo cụ thể.
5. Hệ thống đánh dấu thông báo là "Đã đọc", giảm số lượng trên quả chuông và điều hướng thẳng đến chi tiết Ticket tương ứng.
6. Sinh viên có thể chọn **Đánh dấu tất cả là đã đọc**.

**Business Rules**  
- Thông báo được đẩy về giao diện thời gian thực (độ trễ dưới 2 giây).
- Không phát sinh thông báo cho chính người thực hiện hành động.

**Alternative / Error Flows**  
- **Sinh viên đang offline**: Thông báo được lưu vào cơ sở dữ liệu và hiển thị ngay khi sinh viên đăng nhập lại.

**Acceptance Criteria**  
- **AC-01**: Khi nhân viên cập nhật kết quả -> Sinh viên nhận thông báo tức thì trên giao diện.
- **AC-02**: Nhấn vào thông báo -> Mở đúng chi tiết Ticket liên quan.

**Ví dụ Edge Case**  
Sinh viên có nhiều hơn 99 thông báo chưa đọc.  
-> **Expected Result**: Badge số lượng hiển thị `99+` và danh sách sắp xếp theo thời gian mới nhất lên đầu.

---

### [FR-STU-05] Bổ sung thông tin & phản hồi

**Mô tả**  
Cho phép sinh viên gửi bổ sung thông tin/giấy tờ khi Ticket ở trạng thái `WAITING_STUDENT`, đồng thời xem kết quả giải quyết chính thức và thực hiện đánh giá mức độ hài lòng (CSAT) sau khi yêu cầu hoàn tất.

**Actor**  
Sinh viên đã đăng nhập hệ thống.

**Preconditions**  
- Đối với bổ sung thông tin: Ticket đang ở trạng thái `WAITING_STUDENT`.
- Đối với đánh giá CSAT: Ticket đang ở trạng thái `RESOLVED` hoặc `CLOSED`.

**Luồng chính (Bổ sung thông tin hồ sơ)**  
1. Sinh viên mở chi tiết Ticket đang ở trạng thái `WAITING_STUDENT`.
2. Sinh viên đọc ghi chú yêu cầu bổ sung từ nhân viên.
3. Sinh viên nhập nội dung phản hồi và đính kèm file giấy tờ mới (nếu có).
4. Sinh viên nhấn **Gửi phản hồi bổ sung**.
5. Hệ thống lưu thông tin, tự động chuyển Ticket về `IN_PROGRESS` và kích hoạt lại đồng hồ tính hạn SLA.

**Luồng chính (Xem kết quả & Đánh giá CSAT)**  
1. Sinh viên mở Ticket đã có kết quả (`RESOLVED`).
2. Sinh viên xem nội dung phản hồi chính thức và tải file kết quả (nếu có).
3. Hệ thống hiển thị khung đánh giá mức độ hài lòng.
4. Sinh viên chọn số sao đánh giá (từ 1 đến 5 sao) và nhập nhận xét góp ý.
5. Sinh viên nhấn **Gửi đánh giá**.
6. Hệ thống lưu kết quả đánh giá, chuyển Ticket sang `CLOSED` và khóa form đánh giá.

**Business Rules**  
- Tính năng gửi bổ sung chỉ hiển thị khi Ticket ở `WAITING_STUDENT`.
- Đánh giá CSAT chỉ được thực hiện **duy nhất 01 lần** trong vòng 07 ngày kể từ khi Ticket chuyển sang `RESOLVED`. Quá 7 ngày, form đánh giá tự động khóa.

**Alternative / Error Flows**  
- **Gửi đánh giá nhưng chưa chọn số sao**: Hệ thống nhắc nhở sinh viên chọn số sao trước khi gửi.
- **Sinh viên không đánh giá**: Sau 03 ngày làm việc ở trạng thái `RESOLVED`, hệ thống tự động chuyển Ticket sang `CLOSED`.

**Acceptance Criteria**  
- **AC-01**: Gửi bổ sung thành công -> Trạng thái Ticket tự động đổi từ `WAITING_STUDENT` sang `IN_PROGRESS`.
- **AC-02**: Gửi đánh giá 5 sao -> Ghi nhận điểm CSAT thành công, form chuyển sang dạng chỉ xem (Read-only).