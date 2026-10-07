# Tài Liệu Đặc Tả Yêu Cầu Sản Phẩm - Dịch Vụ Thông Báo (PRD - M04 Notification Service)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`  
> Phân hệ kỹ thuật này hiện thực hóa trực tiếp chức năng **FR-STU-04: Nhận thông báo trạng thái (19h kế hoạch: BA 3h, UI/UX 1h, FE1 4h, BE1 4h, BE2 4h, QA 3h)** và hạ tầng thông báo phục vụ cảnh báo SLA trong **FR-STF-03 (M2)**.

---

### [FR-NTF-01] Khởi tạo & Phát thông báo nội bộ hệ thống tự động

**Mô tả**  
Hệ thống tự động lắng nghe các sự kiện nghiệp vụ phát sinh trên Ticket, sau đó khởi tạo và gửi thông báo nội bộ (In-app Notification) tới đúng đối tượng người dùng liên quan.

**Actor**  
Hệ thống (System Event Engine).

**Preconditions**  
- Xảy ra một sự kiện nghiệp vụ hợp lệ trên Ticket (Tạo mới, Phân công, Chuyển trạng thái, Bổ sung thông tin, Cập nhật kết quả, Cảnh báo SLA).

**Luồng chính**  
1. Sự kiện nghiệp vụ phát sinh trên hệ thống (Ví dụ: Nhân viên A nhấn nút "Hoàn thành" một Ticket).
2. Dịch vụ Thông báo tiếp nhận thông tin sự kiện.
3. Hệ thống xác định danh sách Người nhận thông báo (Recipients) dựa trên Mã ma trận sự kiện (`EVT-01` đến `EVT-07`).
4. Hệ thống điền các biến dữ liệu (Mã Ticket, Tiêu đề, Tên người thao tác...) vào **Mẫu thông báo (Template)** tương ứng.
5. Hệ thống lưu bản ghi thông báo vào cơ sở dữ liệu.
6. Hệ thống đẩy thông báo tới giao diện người dùng (Client Web) của người nhận theo thời gian thực.

**Business Rules**  
- Mọi thông báo In-app đều chứa liên kết trực tiếp (Deep-link) trỏ về đúng màn hình Chi tiết của Ticket liên quan.
- Nội dung thông báo ngắn gọn, rõ ràng, không quá 150 ký tự.
- Không gửi thông báo cho chính người thực hiện thao tác (Ví dụ: Nhân viên tự Claim ticket thì không nhận thông báo "Bạn vừa claim ticket").

**Alternative / Error Flows**  
- **Người nhận đang Offline**: Thông báo vẫn được lưu vào cơ sở dữ liệu và hiển thị ngay khi người nhận đăng nhập lại hệ thống.

**Acceptance Criteria**  
- **AC-01**: Sinh viên tạo Ticket thành công -> Hệ thống gửi thông báo xác nhận cho Sinh viên và thông báo cho Nhân viên thuộc Phòng ban tiếp nhận.
- **AC-02**: Nhân viên yêu cầu bổ sung thông tin -> Sinh viên nhận ngay thông báo kèm đường dẫn tới form bổ sung hồ sơ.
- **AC-03**: Nhấn vào thông báo -> Hệ thống tự động điều hướng chính xác tới trang chi tiết Ticket tương ứng.

**Ví dụ Edge Case**  
Nhân viên A chuyển Ticket `TK-20261004-001` sang Phòng Tài chính - Kế toán.  
-> **Expected Result**: Toàn bộ nhân viên thuộc Phòng Tài chính - Kế toán nhận được thông báo "Có 01 Ticket mới được chuyển tới phòng ban của bạn". Chuyên viên A (người bấm chuyển) không nhận thông báo này.

---

### [FR-NTF-02] Trung tâm thông báo (Notification Center) & Hiển thị quả chuông

**Mô tả**  
Cung cấp giao diện Trung tâm thông báo dạng biểu tượng quả chuông (Bell Icon) trên thanh điều hướng góc trên màn hình Web Application, cho phép người dùng xem danh sách các thông báo mới nhất.

**Actor**  
Tất cả người dùng đã đăng nhập (Sinh viên, Nhân viên, Quản lý).

**Preconditions**  
- Người dùng đã đăng nhập thành công vào hệ thống.

**Luồng chính**  
1. Người dùng quan sát thanh điều hướng (Header) của ứng dụng.
2. Biểu tượng **Quả chuông** hiển thị một thẻ số đỏ (Badge) phản ánh số lượng thông báo **chưa đọc**.
3. Người dùng nhấn vào biểu tượng Quả chuông.
4. Hệ thống mở bảng danh sách Trung tâm thông báo (Notification Dropdown Menu).
5. Bảng hiển thị danh sách 10 thông báo mới nhất, mỗi thông báo gồm:
   - Tiêu đề tóm tắt.
   - Nội dung ngắn.
   - Mốc thời gian tương đối (Ví dụ: "5 phút trước", "2 giờ trước").
   - Trạng thái Đã đọc / Chưa đọc (Phân biệt bằng màu nền).
6. Người dùng nhấn vào một thông báo cụ thể.
7. Hệ thống tự động đánh dấu thông báo đó là "Đã đọc", giảm số lượng trên Badge và điều hướng người dùng tới trang Chi tiết Ticket tương ứng.

**Business Rules**  
- Số hiển thị trên Badge tối đa là `99+` nếu số thông báo chưa đọc vượt quá 99.
- Danh sách thông báo xếp theo thứ tự thời gian giảm dần (Mới nhất nằm ở trên cùng).

**Alternative / Error Flows**  
- **Người dùng không có thông báo nào**: Hiển thị trạng thái trống (Empty state) với biểu tượng quả chuông xám và dòng chữ "Bạn không có thông báo nào".

**Acceptance Criteria**  
- **AC-01**: Khi có thông báo mới -> Badge trên quả chuông tự động tăng số lượng và phát tiếng/hiệu ứng nổi (Toast notification).
- **AC-02**: Nhấn vào danh sách thông báo -> Hiển thị đúng 10 thông báo gần nhất kèm thời gian tương đối.
- **AC-03**: Bấm nút "Xem tất cả" -> Điều hướng tới trang Quản lý toàn bộ thông báo.

**Ví dụ Edge Case**  
Người dùng có 105 thông báo chưa đọc.  
-> **Expected Result**: Badge trên biểu tượng quả chuông hiển thị chuỗi `99+`.

---

### [FR-NTF-03] Đánh dấu Đã đọc / Chưa đọc (Notification Read Status)

**Mô tả**  
Cho phép người dùng quản lý trạng thái của các thông báo trong Trung tâm thông báo, bao gồm đánh dấu lẻ từng thông báo hoặc đánh dấu tất cả là đã đọc.

**Actor**  
Tất cả người dùng đã đăng nhập.

**Preconditions**  
- Người dùng đang mở Trung tâm thông báo.

**Luồng chính**  
1. Người dùng mở Trung tâm thông báo.
2. **Thao tác 1 (Đọc từng thông báo)**: Người dùng nhấn trực tiếp vào dòng thông báo cần xem.
3. **Thao tác 2 (Đánh dấu tất cả đã đọc)**: Người dùng nhấn nút **"Đánh dấu tất cả là đã đọc"** (Mark all as read) ở góc trên bảng thông báo.
4. Hệ thống cập nhật trạng thái các thông báo thành `READ` trong cơ sở dữ liệu.
5. Số lượng Badge trên biểu tượng Quả chuông tự động giảm về `0`.
6. Màu nền của các dòng thông báo chuyển từ màu nổi (Chưa đọc) sang màu nhạt (Đã đọc).

**Business Rules**  
- Việc đánh dấu "Đã đọc" là thao tác một chiều (không hỗ trợ chuyển ngược lại thành Chưa đọc).
- Cập nhật trạng thái "Đã đọc" diễn ra tức thì trên giao diện mà không cần làm mới toàn bộ trang.

**Alternative / Error Flows**  
- **Mất kết nối mạng khi bấm Đánh dấu tất cả đã đọc**: Hệ thống hiển thị thông báo lỗi "Không thể cập nhật trạng thái thông báo. Vui lòng thử lại" và giữ nguyên số Badge.

**Acceptance Criteria**  
- **AC-01**: Bấm nút "Đánh dấu tất cả là đã đọc" -> Badge hiển thị về 0, tất cả thông báo chuyển sang trạng thái đã đọc.
- **AC-02**: Nhấn vào 01 thông báo chưa đọc -> Chỉ riêng thông báo đó chuyển sang đã đọc và Badge giảm đi 1 đơn vị.

---

### [FR-NTF-04] Thông báo cảnh báo trễ hạn / Cảnh báo thời gian SLA (SLA Warning Alert)

**Mô tả**  
Hệ thống tự động quét và phát thông báo cảnh báo tới Nhân viên phụ trách và Trưởng phòng ban khi một Ticket sắp chạm mốc thời gian cam kết xử lý (SLA Warning) hoặc đã vượt quá thời hạn xử lý (SLA Overdue).

**Actor**  
Hệ thống tự động (SLA Monitor Daemon).

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS` hoặc `NEW`.
- Mốc thời gian cam kết xử lý (`sla_due_at`) đã được thiết lập.

**Luồng chính**  
1. Hệ thống định kỳ quét các Ticket chưa hoàn thành.
2. **Mức 1 (Cảnh báo sắp quá hạn)**: Khi thời gian còn lại đến hạn `sla_due_at` nhỏ hơn hoặc bằng **2 giờ làm việc**:
   - Hệ thống khởi tạo thông báo "CẢNH BÁO SLA: Ticket [Mã Ticket] sắp đến hạn xử lý".
   - Gửi thông báo tới Nhân viên phụ trách.
3. **Mức 2 (Cảnh báo đã quá hạn)**: Khi thời điểm hiện tại vượt quá mốc `sla_due_at`:
   - Hệ thống khởi tạo thông báo "SỰ CỐ SLA: Ticket [Mã Ticket] ĐÃ QUÁ HẠN XỬ LÝ".
   - Gửi thông báo cảnh báo tới Nhân viên phụ trách VÀ Trưởng phòng ban.
4. Hệ thống hiển thị biểu tượng cảnh báo màu đỏ đối với Ticket quá hạn trong Hòm thư công việc.

**Business Rules**  
- Cảnh báo Mức 1 (Sắp quá hạn) chỉ gửi **01 lần duy nhất** cho mỗi Ticket.
- Cảnh báo Mức 2 (Đã quá hạn) gửi cho cả Nhân viên thụ lý và Trưởng phòng ban để hỗ trợ điều phối kịp thời.
- Thời gian tính toán SLA tự động loại trừ khoảng thời gian Ticket nằm ở trạng thái `WAITING_STUDENT` theo quy tắc `BR-SUP-01`.

**Alternative / Error Flows**  
- **Ticket được chuyển sang `RESOLVED` trước khi hết hạn**: Hệ thống hủy các lịch trình cảnh báo trễ hạn còn lại của Ticket đó.

**Acceptance Criteria**  
- **AC-01**: Ticket còn 1.5 giờ là hết hạn SLA -> Nhân viên phụ trách nhận được thông báo cảnh báo sắp quá hạn.
- **AC-02**: Ticket vượt quá hạn SLA 1 phút -> Cả Nhân viên thụ lý và Trưởng phòng ban nhận được thông báo cảnh báo quá hạn.
- **AC-03**: Ticket đang ở trạng thái `WAITING_STUDENT` -> Không phát thông báo cảnh báo SLA.