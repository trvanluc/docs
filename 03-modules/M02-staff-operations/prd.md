# Tài Liệu Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Nhân Viên (PRD - M02 Staff Operations)

---

### [FR-STF-01] Đăng nhập tài khoản Nhân viên

**Mô tả**  
Hệ thống cho phép Nhân viên thuộc các phòng ban đăng nhập vào Phân hệ Nhân viên để quản lý và xử lý các Ticket hỗ trợ được phân công.

**Actor**  
Nhân viên (Staff / Support Agent).

**Preconditions**  
- Tài khoản nhân viên đã được Quản trị viên (Admin) khởi tạo và gán thuộc về ít nhất 01 Phòng ban chuyên trách.
- Tài khoản ở trạng thái `Active`.

**Luồng chính**  
1. Nhân viên truy cập cổng đăng nhập nội bộ UniSupport.
2. Hệ thống hiển thị form đăng nhập.
3. Nhân viên nhập **Email công vụ / Mã nhân viên** và **Mật khẩu**.
4. Nhân viên nhấn nút **Đăng nhập**.
5. Hệ thống xác thực tài khoản và kiểm tra vai trò (`Role = STAFF` hoặc `MANAGER`).
6. Hệ thống điều hướng Nhân viên vào **Hòm thư công việc của Phòng ban** (Staff Dashboard).

**Business Rules**  
- Mật khẩu mã hóa theo chuẩn an toàn.
- Khóa tài khoản tạm thời 5 phút nếu đăng nhập sai quá 5 lần liên tiếp.
- Sau khi đăng nhập, hệ thống chỉ nạp dữ liệu Ticket thuộc Phòng ban mà nhân viên đó được phân quyền.

**Alternative / Error Flows**  
- **Sai thông tin xác thực**: Hiển thị lỗi "Thông tin đăng nhập không chính xác".
- **Tài khoản sinh viên cố tình đăng nhập vào cổng Staff**: Hệ thống từ chối truy cập và thông báo "Tài khoản của bạn không có quyền truy cập phân hệ này".

**Acceptance Criteria**  
- **AC-01**: Nhân viên đăng nhập đúng tài khoản -> Hệ thống điều hướng vào Dashboard Nhân viên và hiển thị đúng danh sách Ticket của phòng ban tương ứng.
- **AC-02**: Tài khoản Sinh viên đăng nhập vào form Staff -> Hệ thống ngăn chặn và hiển thị thông báo không đủ quyền hạn.
- **AC-03**: Nhập sai mật khẩu -> Dừng đăng nhập và báo lỗi validation.

**Ví dụ Edge Case**  
Nhân viên thuộc Phòng Đào tạo đăng nhập thành công.  
-> **Expected Result**: Dashboard chỉ hiển thị các Ticket gửi tới Phòng Đào tạo, không hiển thị Ticket của Phòng CTHSSV hay Tài chính.

---

### [FR-STF-02] Tiếp nhận (Claim) & Phân công (Assign) Ticket

**Mô tả**  
Hệ thống cho phép Nhân viên chủ động tiếp nhận một Ticket chưa có người xử lý thuộc phòng ban của mình, hoặc cho phép Trưởng phòng phân công Ticket đó cho một nhân viên cụ thể.

**Actor**  
Nhân viên phụ trách / Trưởng phòng ban (Staff / Manager).

**Preconditions**  
- Ticket đang ở trạng thái `NEW` hoặc `IN_PROGRESS` nhưng trường `assigned_staff_id` đang để trống (`NULL`).
- Ticket thuộc Phòng ban của Nhân viên/Trưởng phòng đó.

**Luồng chính**  
1. Nhân viên mở danh sách **Ticket Mới của Phòng ban**.
2. Nhân viên chọn một Ticket cụ thể để xem tóm tắt.
3. **Trường hợp 1 (Tự tiếp nhận)**: Nhân viên nhấn nút **Tiếp nhận xử lý (Claim)**.
4. **Trường hợp 2 (Trưởng phòng phân công)**: Trưởng phòng chọn tên Nhân viên từ danh sách và nhấn **Phân công (Assign)**.
5. Hệ thống kiểm tra điều kiện khả thi của Ticket.
6. Hệ thống cập nhật trường `assigned_staff_id` bằng ID của nhân viên được gán.
7. Hệ thống tự động chuyển trạng thái Ticket từ `NEW` sang `IN_PROGRESS` (nếu trước đó là `NEW`).
8. Hệ thống ghi nhận sự kiện vào Nhật ký tra soát (Audit Log) và gửi thông báo In-app cho nhân viên được gán.

**Business Rules**  
- Một Ticket chỉ được tiếp nhận/phân công cho **01 nhân viên duy nhất** tại một thời điểm.
- Nhân viên không thể Claim Ticket thuộc phòng ban khác.
- Khi Ticket đã được Claim, nút **Claim** sẽ tự động ẩn đối với các nhân viên khác.

**Alternative / Error Flows**  
- **Ticket đã bị nhân viên khác Claim trước đó 1 giây**: Hệ thống báo lỗi "Ticket này đã được tiếp nhận bởi [Tên nhân viên khác]" và tải lại trang.

**Acceptance Criteria**  
- **AC-01**: Nhân viên bấm **Claim** -> Ticket chuyển sang trạng thái `IN_PROGRESS`, trường người phụ trách hiển thị tên nhân viên đó.
- **AC-02**: Trưởng phòng chọn nhân viên A và bấm **Assign** -> Ticket gắn với tên nhân viên A, gửi thông báo cho nhân viên A.
- **AC-03**: Hai nhân viên cùng bấm Claim 1 Ticket đồng thời -> Hệ thống áp dụng cơ chế khóa dữ liệu (Locking), chỉ ghi nhận người bấm trước, người bấm sau nhận thông báo Ticket đã có người nhận.

**Ví dụ Edge Case**  
Chuyên viên A và Chuyên viên B cùng mở chi tiết Ticket `TK-20261004-001` ở hai máy tính khác nhau. Chuyên viên A bấm nút **Claim** thành công. Chuyên viên B bấm nút **Claim** sau 2 giây.  
-> **Expected Result**: Hệ thống từ chối yêu cầu của Chuyên viên B và thông báo "Ticket đã được tiếp nhận bởi Chuyên viên A".

---

### [FR-STF-03] Phân loại (Triage) & Đánh giá mức độ ưu tiên

**Mô tả**  
Cho phép nhân viên xem xét chi tiết nội dung Ticket để điều chỉnh đúng Nhóm vấn đề / Phân loại chi tiết và thiết lập Mức độ ưu tiên để tính toán thời hạn SLA xử lý.

**Actor**  
Nhân viên phụ trách Ticket (Assigned Staff).

**Preconditions**  
- Ticket đã được tiếp nhận (`IN_PROGRESS`) và do nhân viên đó phụ trách.

**Luồng chính**  
1. Nhân viên mở màn hình Chi tiết Ticket đang phụ trách.
2. Nhân viên chọn chức năng **Phân loại & Mức độ ưu tiên**.
3. Nhân viên chọn lại **Phân loại chi tiết (Sub-category)** phù hợp với nội dung thực tế.
4. Nhân viên thiết lập **Mức độ ưu tiên**: `Thấp (Low)`, `Trung bình (Medium)`, `Cao (High)`, hoặc `Khẩn cấp (Urgent)`.
5. Nhân viên nhấn **Lưu thay đổi**.
6. Hệ thống cập nhật thông tin phân loại và mức độ ưu tiên.
7. Hệ thống tự động tính toán lại mốc thời gian hoàn thành cam kết (`sla_due_at`) dựa trên mức độ ưu tiên mới.
8. Ghi nhận thay đổi vào nhật ký hệ thống.

**Business Rules**  
- Mặc định khi khởi tạo, Ticket có mức độ ưu tiên là `Trung bình (Medium)`.
- Khi thay đổi Mức độ ưu tiên, mốc thời gian SLA (`sla_due_at`) được tính lại tự động từ thời điểm khởi tạo Ticket gốc.
- Mức độ `Khẩn cấp (Urgent)` chỉ áp dụng cho các sự cố gián đoạn hệ thống nghiêm trọng hoặc trùng lịch thi sát giờ.

**Alternative / Error Flows**  
- **Không có quyền chỉnh sửa**: Nếu nhân viên không phải là người phụ trách Ticket đó, các trường chỉnh sửa bị khóa dạng Read-only.

**Acceptance Criteria**  
- **AC-01**: Nhân viên đổi mức ưu tiên từ `Medium` sang `Urgent` -> Mốc thời gian `sla_due_at` rút ngắn tương ứng và hiển thị nhãn màu đỏ cảnh báo.
- **AC-02**: Mọi thay đổi về phân loại và độ ưu tiên được lưu chính xác và ghi vết vào Audit Log.

**Ví dụ Edge Case**  
Nhân viên hạ độ ưu tiên từ `High` xuống `Low` khi Ticket đã gần hết hạn SLA `High`.  
-> **Expected Result**: Hệ thống cập nhật lại thời hạn `sla_due_at` theo chuẩn `Low` và ghi lại lý do điều chỉnh trong nhật ký.

---

### [FR-STF-04] Chuyển phòng ban chuyên trách (Transfer Department)

**Mô tả**  
Khi phát hiện sinh viên gửi nhầm phòng ban hoặc nội dung cần sự giải quyết của đơn vị khác, nhân viên có quyền chuyển Ticket sang Phòng ban chuyên trách kèm theo lý do chuyển.

**Actor**  
Nhân viên phụ trách Ticket.

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS`.
- Sinh viên gửi không đúng phòng ban chuyên trách.

**Luồng chính**  
1. Nhân viên mở màn hình Chi tiết Ticket.
2. Nhân viên chọn chức năng **Chuyển phòng ban**.
3. Hệ thống hiển thị danh sách các Phòng ban chức năng khác trong trường.
4. Nhân viên chọn **Phòng ban đích** cần chuyển tới.
5. Nhân viên nhập **Lý do chuyển phòng ban** (Bắt buộc).
6. Nhân viên nhấn nút **Xác nhận chuyển**.
7. Hệ thống kiểm tra dữ liệu đầu vào.
8. Hệ thống cập nhật `department_id` mới cho Ticket.
9. Hệ thống tự động đặt `assigned_staff_id = NULL` (gỡ bỏ người phụ trách cũ).
10. Trạng thái Ticket vẫn giữ nguyên `IN_PROGRESS`.
11. Hệ thống phát thông báo In-app tới Hòm thư công việc của Phòng ban mới và ghi log sự kiện.

**Business Rules**  
- Bắt buộc nhập Lý do chuyển (Tối thiểu 10 ký tự) theo quy định `BR-XFR-01`.
- Sau khi chuyển, nhân viên phòng ban cũ **mất quyền chỉnh sửa** Ticket đó (chỉ còn quyền xem dạng nhật ký nếu được cấp phép).
- Người phụ trách cũ bị gỡ bỏ để nhân viên phòng ban mới Claim/Assign lại từ đầu.

**Alternative / Error Flows**  
- **Để trống lý do chuyển hoặc nhập ngắn hơn 10 ký tự**: Hệ thống từ chối chuyển và báo lỗi "Vui lòng nhập lý do chuyển chi tiết (tối thiểu 10 ký tự)".
- **Chọn trùng phòng ban hiện tại**: Hệ thống báo lỗi "Phòng ban đích phải khác phòng ban hiện tại".

**Acceptance Criteria**  
- **AC-01**: Nhân viên nhập đủ lý do hợp lệ và chọn Phòng đợt mới -> Ticket chuyển sang Hòm thư phòng ban mới, trường `assigned_staff_id` trở về `NULL`.
- **AC-02**: Nhập lý do dưới 10 ký tự -> Hệ thống không cho phép thực hiện chuyển và hiển thị cảnh báo.
- **AC-03**: Lý do chuyển phòng ban hiển thị công khai trong nhật ký lịch sử để phòng ban mới nắm bối cảnh.

**Ví dụ Edge Case**  
Sinh viên gửi nhầm thắc mắc về Học phí vào Phòng Đào tạo. Chuyên viên Phòng Đào tạo chọn chuyển sang Phòng Tài chính - Kế toán với lý do "Nội dung liên quan đến hóa đơn học phí kìm giữ".  
-> **Expected Result**: Ticket xuất hiện ngay trong Hòm thư chung của Phòng Tài chính - Kế toán, chuyên viên Phòng Đào tạo không còn là người thụ lý.

---

### [FR-STF-05] Yêu cầu sinh viên bổ sung thông tin / hồ sơ

**Mô tả**  
Khi hồ sơ sinh viên gửi kèm bị thiếu, mờ, không hợp lệ hoặc cần làm rõ, nhân viên phát yêu cầu bổ sung thông tin tới sinh viên và hệ thống tạm dừng bộ đếm SLA.

**Actor**  
Nhân viên phụ trách Ticket.

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS`.

**Luồng chính**  
1. Nhân viên mở chi tiết Ticket.
2. Nhân viên chọn chức năng **Yêu cầu bổ sung**.
3. Nhân viên nhập chi tiết nội dung/danh mục giấy tờ cần sinh viên cung cấp thêm.
4. Nhân viên nhấn nút **Gửi yêu cầu bổ sung**.
5. Hệ thống lưu nội dung yêu cầu vào lịch sử trao đổi.
6. Hệ thống chuyển trạng thái Ticket từ `IN_PROGRESS` sang `WAITING_STUDENT`.
7. Hệ thống **TẠM DỪNG** bộ đếm thời gian SLA xử lý theo quy tắc `BR-SUP-01`.
8. Hệ thống phát thông báo In-app và Email cho Sinh viên.

**Business Rules**  
- Nội dung yêu cầu bổ sung là bắt buộc.
- Trạng thái Ticket **bắt buộc** chuyển sang `WAITING_STUDENT`.
- Trong thời gian `WAITING_STUDENT`, thời gian chậm trễ không tính vào chỉ số KPI/SLA của nhân viên.

**Alternative / Error Flows**  
- **Nội dung yêu cầu để trống**: Hệ thống dừng thao tác và báo lỗi "Nội dung yêu cầu bổ sung không được để trống".

**Acceptance Criteria**  
- **AC-01**: Nhân viên gửi yêu cầu bổ sung -> Trạng thái chuyển thành `WAITING_STUDENT`, bộ đếm SLA tạm dừng, sinh viên nhận được thông báo.
- **AC-02**: Khung nhập liệu bị ẩn nếu Ticket không còn ở trạng thái `IN_PROGRESS`.

**Ví dụ Edge Case**  
Nhân viên yêu cầu sinh viên chụp lại mặt sau Thẻ sinh viên do ảnh cũ bị nhòe.  
-> **Expected Result**: Trạng thái chuyển `WAITING_STUDENT`, đồng hồ đếm ngược SLA dừng lại cho đến khi sinh viên upload ảnh mới lên.

---

### [FR-STF-06] Cập nhật kết quả giải quyết & Đóng Ticket (Resolve & Close)

**Mô tả**  
Cho phép nhân viên nhập nội dung trả lời chính thức, đính kèm file kết quả (nếu có) và đánh dấu Ticket là đã giải quyết hoàn tất.

**Actor**  
Nhân viên phụ trách Ticket.

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS`.
- Nhân viên đã hoàn tất các bước kiểm tra/xử lý nghiệp vụ.

**Luồng chính**  
1. Nhân viên mở chi tiết Ticket.
2. Nhân viên chọn chức năng **Hoàn thành & Cập nhật kết quả**.
3. Nhân viên nhập **Nội dung kết quả giải quyết** (Phản hồi chính thức cho sinh viên).
4. Nhân viên đính kèm file kết quả (nếu có, ví dụ: Giấy xác nhận dạng PDF có con dấu, Bảng điểm...).
5. Nhân viên chọn **Ghi nhận hoàn thành (Resolve)**.
6. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
7. Hệ thống lưu nội dung kết quả và file đính kèm.
8. Hệ thống cập nhật trạng thái Ticket sang `RESOLVED`.
9. Hệ thống ghi nhận mốc thời gian `resolved_at` bằng thời gian hiện tại.
10. Hệ thống gửi thông báo kết quả cho Sinh viên và mở form để sinh viên đánh giá CSAT.

**Business Rules**  
- Nội dung kết quả giải quyết là trường thông tin bắt buộc.
- File đính kèm kết quả tuân thủ `BR-FILE-01` & `BR-FILE-02` (chỉ người tạo và nhân viên phòng ban mới tải được).
- Sau **03 ngày làm việc** kể từ khi ở `RESOLVED`, nếu sinh viên không có khiếu nại hoặc không đánh giá, hệ thống tự động chuyển trạng thái sang `CLOSED`.

**Alternative / Error Flows**  
- **Thiếu nội dung kết quả**: Hệ thống không cho hoàn thành và báo lỗi "Vui lòng nhập nội dung giải quyết trước khi đóng Ticket".
- **Upload file sai định dạng hoặc >10MB**: Hiển thị lỗi file và dừng hoàn tất.

**Acceptance Criteria**  
- **AC-01**: Nhân viên nhập kết quả, đính kèm file PDF xác nhận và chọn Resolve -> Ticket chuyển sang `RESOLVED`, mốc thời gian `resolved_at` được lưu, sinh viên nhận thông báo kết quả.
- **AC-02**: Để trống nội dung kết quả -> Hệ thống hiển thị cảnh báo yêu cầu nhập liệu.
- **AC-03**: Ticket ở trạng thái `RESOLVED` sau 3 ngày không có tương tác mới -> Hệ thống tự động chuyển trạng thái thành `CLOSED`.

**Ví dụ Edge Case**  
Nhân viên xử lý xong yêu cầu Cấp lại mật khẩu Portal, nhập kết quả "Đã mút lại mật khẩu mặc định và gửi về email sinh viên", bấm Resolve.  
-> **Expected Result**: Ticket chuyển sang `RESOLVED`, sinh viên thấy nội dung phản hồi và nút chấm điểm CSAT.