# Phân Hệ Sinh Viên (M01 - Student Portal)

## I. TỔNG QUAN PHÂN HỆ
Phân hệ Sinh viên cung cấp giao diện trực quan, thân thiện trên cả máy tính và thiết bị di động[cite: 1]. Phân hệ cho phép sinh viên Aurora University chủ động tạo yêu cầu hỗ trợ, đính kèm file minh chứng (ảnh hoặc PDF), theo dõi tiến độ xử lý theo thời gian thực qua mã Ticket duy nhất, bổ sung giấy tờ khi có yêu cầu, nhận kết quả và đánh giá mức độ hài lòng[cite: 1].

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STU-01] Sinh viên đăng nhập hệ thống

**Mô tả**  
Hệ thống cho phép sinh viên đăng nhập vào cổng UniSupport bằng tài khoản cá nhân do nhà trường cấp để thực hiện các giao dịch hỗ trợ[cite: 1].

**Actor**  
Sinh viên Aurora University[cite: 1].

**Preconditions**  
- Sinh viên có tài khoản được cấp hợp lệ trên hệ thống UniSupport[cite: 1].

**Luồng chính**  
1. Sinh viên truy cập vào địa chỉ web hệ thống UniSupport[cite: 1].
2. Hệ thống hiển thị màn hình đăng nhập.
3. Sinh viên nhập **Tên đăng nhập / Mã sinh viên** và **Mật khẩu**[cite: 1].
4. Sinh viên nhấn nút **Đăng nhập**.
5. Hệ thống xác thực thông tin đăng nhập.
6. Hệ thống chuyển hướng sinh viên đến giao diện trang chủ Phân hệ Sinh viên.

**Business Rules**  
- Tài khoản đăng nhập phải trùng khớp với dữ liệu sinh viên trong hệ thống[cite: 1].
- Mỗi vai trò sau khi đăng nhập thành công chỉ truy cập được giao diện và chức năng tương ứng với vai trò của mình[cite: 1].

**Alternative / Error Flows**  
- Nếu nhập sai thông tin đăng nhập, hệ thống hiển thị thông báo lỗi: "Tài khoản hoặc mật khẩu không chính xác" và yêu cầu nhập lại.
- Nếu tài khoản bị khóa, hệ thống hiển thị thông báo: "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ quản trị viên."

**Acceptance Criteria**  
- **AC-01:** Sinh viên nhập đúng thông tin tài khoản -> Hệ thống đăng nhập thành công và chuyển vào trang chính.
- **AC-02:** Sinh viên nhập sai tài khoản/mật khẩu -> Hệ thống không cho đăng nhập và hiển thị thông báo lỗi validation.

**Ví dụ Edge Case**  
Sinh viên nhấn nút **Đăng nhập** liên tiếp 5 lần khi mạng bị lag.

**Expected Result:** Hệ thống vô hiệu hóa nút bấm tạm thời và gửi 01 request xác thực duy nhất, không gây treo giao diện.

---

### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ

**Mô tả**  
Hệ thống cho phép sinh viên tạo một Ticket hỗ trợ bằng cách chọn nhóm vấn đề, nhập thông tin mô tả và đính kèm file minh chứng (ảnh hoặc PDF)[cite: 1].

**Actor**  
Sinh viên đã đăng nhập vào hệ thống[cite: 1].

**Preconditions**  
- Sinh viên đã đăng nhập thành công[cite: 1].
- Sinh viên có quyền tạo Ticket[cite: 1].

**Luồng chính**  
1. Sinh viên mở chức năng **Tạo Ticket**[cite: 1].
2. Hệ thống hiển thị form tạo Ticket.
3. Sinh viên nhập các thông tin bắt buộc của Ticket, bao gồm mô tả vấn đề[cite: 1].
4. Sinh viên chọn **Gửi yêu cầu**[cite: 1].
5. Hệ thống kiểm tra tính hợp lệ của dữ liệu[cite: 1].
6. Nếu dữ liệu hợp lệ, hệ thống tạo Ticket mới[cite: 1].
7. Hệ thống hiển thị thông báo tạo Ticket thành công và cung cấp mã Ticket cho sinh viên[cite: 1].

**Business Rules**  
- Mô tả vấn đề là thông tin bắt buộc[cite: 1].
- Nội dung chỉ chứa khoảng trắng được xem là không hợp lệ[cite: 1].
- Một thao tác gửi của sinh viên chỉ được tạo tối đa **một Ticket**, kể cả khi yêu cầu bị gửi nhiều lần do double-click, retry hoặc vấn đề mạng[cite: 1].
- Ticket sau khi được tạo phải được liên kết với tài khoản sinh viên đã gửi yêu cầu[cite: 1].
- File đính kèm chỉ chấp nhận định dạng **PDF, PNG, JPG, JPEG**, dung lượng tối đa **5MB/file**[cite: 1].

**Alternative / Error Flows**  
- Nếu thiếu thông tin bắt buộc, hệ thống không tạo Ticket và hiển thị thông báo yêu cầu sinh viên bổ sung thông tin[cite: 1].
- Nếu quá trình tạo Ticket thất bại, hệ thống thông báo lỗi và không được tạo Ticket ở trạng thái dữ liệu không hoàn chỉnh[cite: 1].
- Nếu cùng một yêu cầu được gửi lại nhiều lần, hệ thống không tạo thêm Ticket trùng lập[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Sinh viên nhập đầy đủ thông tin hợp lệ và chọn **Gửi yêu cầu** -> hệ thống tạo đúng một Ticket và hiển thị thông báo thành công[cite: 1].
- **AC-02:** Sinh viên để trống trường mô tả -> hệ thống không tạo Ticket và hiển thị lỗi validation[cite: 1].
- **AC-03:** Sinh viên nhập nội dung chỉ gồm khoảng trắng -> hệ thống không tạo Ticket[cite: 1].
- **AC-04:** Sinh viên nhấn nút **Gửi yêu cầu** nhiều lần liên tiếp -> hệ thống chỉ tạo một Ticket[cite: 1].
- **AC-05:** Cùng một request được gửi lại do retry/network retry -> hệ thống không tạo Ticket trùng lập[cite: 1].
- **AC-06:** Ticket được tạo phải lưu đúng thông tin sinh viên gửi yêu cầu[cite: 1].

**Ví dụ Edge Case**  
Sinh viên nhấn nút **Gửi yêu cầu** 5 lần liên tiếp trong thời gian ngắn[cite: 1].

**Expected Result:** Hệ thống chỉ ghi nhận **một Ticket duy nhất** cho thao tác gửi đó[cite: 1].

---

### [FR-STU-03] Sinh viên theo dõi tiến độ & bổ sung hồ sơ

**Mô tả**  
Cho phép sinh viên xem chi tiết trạng thái xử lý, lịch sử cập nhật, người/phòng ban phụ trách và gửi bổ sung file/giấy tờ theo yêu cầu của nhân viên[cite: 1].

**Actor**  
Sinh viên đã đăng nhập hệ thống[cite: 1].

**Preconditions**  
- Sinh viên đã tạo Ticket thành công trước đó[cite: 1].

**Luồng chính**  
1. Sinh viên chọn chức năng **Danh sách Ticket của tôi**.
2. Hệ thống hiển thị danh sách các Ticket kèm mã Ticket và trạng thái hiện tại (`NEW`, `IN_PROGRESS`, `NEED_MORE_INFO`, `CLOSED`)[cite: 1].
3. Sinh viên chọn một Ticket để xem chi tiết tiến độ và lịch sử cập nhật[cite: 1].
4. Hệ thống hiển thị người/phòng ban đang phụ trách và tin nhắn nhắn yêu cầu sinh viên bổ sung thông tin[cite: 1].
5. Nếu Ticket ở trạng thái `NEED_MORE_INFO`, sinh viên chọn nút **Bổ sung thông tin**[cite: 1].
6. Sinh viên đính kèm thêm giấy tờ/file đính kèm còn thiếu và nhấn **Xác nhận gửi**[cite: 1].
7. Hệ thống lưu tài liệu bổ sung, tự động chuyển trạng thái Ticket về `IN_PROGRESS` và thông báo cho nhân viên[cite: 1].

**Business Rules**  
- Sinh viên chỉ được xem Ticket do chính tài khoản của mình gửi yêu cầu[cite: 1].
- Chỉ cho phép upload bổ sung file khi Ticket đang ở trạng thái `NEED_MORE_INFO`[cite: 1].
- Không cho phép chỉnh sửa tiêu đề hay nhóm vấn đề ban đầu của Ticket trong quá trình bổ sung[cite: 1].

**Alternative / Error Flows**  
- Nếu đính kèm file vượt quá 5MB hoặc sai định dạng, hệ thống từ chối tải lên và thông báo lỗi cấu trúc file[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Sinh viên truy cập xem đúng danh sách Ticket của mình[cite: 1].
- **AC-02:** Sinh viên upload đủ file khi Ticket ở trạng thái `NEED_MORE_INFO` -> hệ thống chuyển trạng thái Ticket sang `IN_PROGRESS` thành công[cite: 1].

**Ví dụ Edge Case**  
Sinh viên cố gắng upload file đuôi `.exe` khi bổ sung hồ sơ.

**Expected Result:** Hệ thống chặn file, hiển thị lỗi "Chỉ chấp nhận file định dạng PDF hoặc hình ảnh (PNG, JPG)".

---

### [FR-STU-04] Xem kết quả giải quyết & Đánh giá mức độ hài lòng

**Mô tả**  
Sinh viên xem kết quả giải quyết và các thông báo liên quan đến yêu cầu của mình, đồng thời đánh giá mức độ hài lòng sau khi yêu cầu được hoàn tất[cite: 1].

**Actor**  
Sinh viên đã đăng nhập hệ thống[cite: 1].

**Preconditions**  
- Ticket của sinh viên đã được nhân viên hoàn tất và chuyển sang trạng thái `CLOSED`[cite: 1].

**Luồng chính**  
1. Sinh viên mở thông báo hoặc truy cập vào Ticket có trạng thái `CLOSED`[cite: 1].
2. Hệ thống hiển thị nội dung xem kết quả giải quyết và các thông báo liên quan[cite: 1].
3. Hệ thống hiển thị biểu mẫu đánh giá mức độ hài lòng sau khi yêu cầu được hoàn tất[cite: 1].
4. Sinh viên chọn số sao đánh giá (từ 1 đến 5 sao) và nhập nhận xét[cite: 1].
5. Sinh viên nhấn nút **Gửi đánh giá**.
6. Hệ thống lưu kết quả đánh giá và cập nhật trạng thái đã hoàn tất đánh giá cho Ticket[cite: 1].

**Business Rules**  
- Mỗi Ticket ở trạng thái `CLOSED` chỉ được đánh giá duy nhất **01 lần**[cite: 1].
- Thang điểm đánh giá là số nguyên từ 1 đến 5[cite: 1].

**Alternative / Error Flows**  
- Nếu Ticket chưa ở trạng thái `CLOSED`, biểu mẫu đánh giá sẽ bị ẩn/khóa.

**Acceptance Criteria**  
- **AC-01:** Xem đầy đủ thông tin kết quả giải quyết từ nhân viên[cite: 1].
- **AC-02:** Chọn 5 sao và gửi đánh giá -> Hệ thống ghi nhận thành công và ẩn biểu mẫu đánh giá[cite: 1].

**Ví dụ Edge Case**  
Sinh viên mở 2 tab trình duyệt cùng lúc để gửi đánh giá cho 1 Ticket.

**Expected Result:** Hệ thống chỉ ghi nhận lượt đánh giá ở tab gửi trước, tab còn lại báo lỗi "Ticket đã được đánh giá".