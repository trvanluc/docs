# Kịch Bản Kiểm Thử Chấp Nhận Người Dùng (UAT Test Scenarios Specification)

## 1. Tiêu Chuẩn Đánh Giá UAT (Acceptance Criteria & Test Standards)
- **Môi trường thử nghiệm:** Staging Environment (`https://staging-unisupport.aurora.edu.vn`).
- **Thời gian UAT:** 10 ngày làm việc.
- **Quy tắc Đạt (Pass Criteria):** $100\%$ các Test Case mức Critical/High đạt Pass, không còn lỗi An toàn thông tin hoặc Lỗi gián đoạn Luồng công việc (Blocking Issues).

## 2. Phân Hệ Sinh Viên (Student Portal UAT)

### Scenario ID: `UAT-STU-02` - Sinh viên Khởi tạo Ticket & Kiểm soát Idempotency
- **Mục tiêu:** Kiểm tra sinh viên tạo Ticket mới thành công kèm file đính kèm, kiểm tra validation Form và cơ chế Idempotency Key chống ghi nhận trùng dữ liệu.
- **Tiền điều kiện:** Sinh viên `stu01` đã đăng nhập vào hệ thống.

| Step | Thao Tác Kiểm Thử | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi (Expected Result) | HTTP / DB Check | Pass/Fail |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | Bấm nút "Tạo Ticket" | - | Hiển thị Form Modal tạo Ticket kèm `client_request_id` sinh tự động. | UI Render | Pass |
| 2 | Nhập Form hợp lệ và đính kèm file | Category: "Đào tạo"<br><br>Title: "Xin hoãn thi môn CSDL"<br><br>Desc: "Do sự cố sức khỏe..."<br><br>File: `xac_nhan.pdf` ($2\text{MB}$) | Form điền đầy đủ dữ liệu, file đính kèm hợp lệ. | Client Validation Pass | Pass |
| 3 | Click đúp nút "Gửi yêu cầu" 3 lần liên tiếp | Thao tác click liên tục ($< 500\text{ ms}$) | Hệ thống chỉ tạo 01 Ticket duy nhất (VD: `TK-20261009-0001`), hiển thị Toast thành công. | HTTP 201<br><br>`tickets COUNT = 1` | Pass |
| 4 | Thử tạo Ticket với file vượt $5\text{MB}$ | File: `video_minh_chung.mp4` ($12\text{MB}$) | Hệ thống từ chối file ngay tại Client, báo lỗi: "Dung lượng file vượt quá giới hạn 5MB." | 400 Bad Request<br><br>`FILE_EXCEEDS_LIMIT` | Pass |
| 5 | Thử tạo Ticket để trống Mô tả | Title: "Cần hỗ trợ"<br><br>Desc: "" (bỏ trống) | Hệ thống chặn submit, hiển thị lỗi validation dưới trường Mô tả. | Client Form Validation | Pass |

## 3. Phân Hệ Nhân Viên (Staff Operations UAT)

### Scenario ID: `UAT-STF-03` - Chuyển Tiếp Ticket Sang Phòng Ban Khác
- **Mục tiêu:** Kiểm tra chức năng chuyển Ticket không đúng thẩm quyền sang phòng ban chuyên trách, xác minh FSM state chuyển `TRANSFERRED` và `assignee_id` bị xóa về `NULL`.
- **Tiền điều kiện:** Nhân viên Phòng Đào tạo `staff_edu` đang mở Ticket `TK-20261009-0002` ở trạng thái `IN_PROGRESS`.

| Step | Thao Tác Kiểm Thử | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi (Expected Result) | HTTP / DB Check | Pass/Fail |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | Bấm nút "Chuyển phòng ban" | - | Hiển thị Modal chọn phòng ban đích và nhập lý do. | UI Render | Pass |
| 2 | Chọn trùng phòng ban hiện tại | Target Dept: "Phòng Đào tạo" | Option "Phòng Đào tạo" bị disable hoặc hệ thống báo lỗi nếu cố chọn. | Client Guard | Pass |
| 3 | Nhập lý do quá ngắn ($< 10$ ký tự) | Lý do: "Sai phong" | Báo lỗi dưới Textarea: "Lý do chuyển tiếp tối thiểu 10 ký tự." | Client Validation | Pass |
| 4 | Nhập thông tin hợp lệ và bấm "Xác nhận" | Target Dept: "Phòng Tài chính"<br><br>Lý do: "Yêu cầu liên quan đến miễn giảm học phí." | Chuyển phòng thành công, Toast thông báo thành công, tự động điều hướng về Queue làm việc. | HTTP 200 OK<br><br>`status = TRANSFERRED`<br><br>`assignee_id = NULL` | Pass |
| 5 | Kiểm tra Queue Phòng Tài chính | Log in bằng `staff_fin` | Ticket `TK-20261009-0002` xuất hiện trong Tab "Ticket chờ tiếp nhận" của Phòng Tài chính. | HTTP 200 OK | Pass |

### Scenario ID: `UAT-STF-05` - Ghi Nhận Kết Quả & Hoàn Tất Giải Quyết Ticket
- **Mục tiêu:** Kiểm tra quy tắc bắt buộc nhập `resolution_note`, chuyển trạng thái FSM sang `RESOLVED` và khởi chạy bộ đếm thời gian.
- **Tiền điều kiện:** Nhân viên `staff_fin` đang phụ trách Ticket `TK-20261009-0003` ở trạng thái `IN_PROGRESS`.

| Step | Thao Tác Kiểm Thử | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi (Expected Result) | HTTP / DB Check | Pass/Fail |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | Bấm nút "Hoàn thành & Đóng Ticket" | - | Hiển thị Modal nhập kết quả giải quyết. | UI Render | Pass |
| 2 | Nhập chuỗi chỉ chứa khoảng trắng | `resolution_note`: "   " | Hệ thống chặn submit, báo lỗi: "Kết quả giải quyết không được để trống." | 400 Bad Request<br><br>`INVALID_INPUT` | Pass |
| 3 | Nhập đầy đủ nội dung giải quyết hợp lệ | `resolution_note`: "Đã miễn giảm 50% học phí kỳ 1 cho sinh viên theo QĐ #123." | Lưu kết quả thành công, Ticket đổi trạng thái thành `RESOLVED`, lưu `resolved_at`. | HTTP 200 OK<br><br>`status = RESOLVED`<br><br>`resolved_at IS NOT NULL` | Pass |
| 4 | Kiểm tra quyền chỉnh sửa sau khi Complete | `staff_fin` bấm sửa nội dung kết quả | Hệ thống vô hiệu hóa toàn bộ các nút chỉnh sửa/thao tác trên Ticket. | UI Readonly Mode | Pass |

## 4. Phân Hệ Bảo Mật & Phân Quyền (Security & Privacy UAT)

### Scenario ID: `UAT-SEC-02` - Kiểm Soát Quyền Xem & Stream File Đính Kèm (Zero Public Access)
- **Mục tiêu:** Đảm bảo file đính kèm lưu ở thư mục Private, bắt buộc xác thực token và chỉ cho phép người dùng có quyền hợp lệ xem/stream file.
- **Tiền điều kiện:** Sinh viên A (`stu_A`) có Ticket chứa file `minh_chung_A.pdf` (ID: `att_1001`). Sinh viên B (`stu_B`) không sở hữu Ticket này.

| Step | Thao Tác Kiểm Thử | Dữ Liệu Đầu Vào | Kết Quả Mong Đợi (Expected Result) | HTTP / DB Check | Pass/Fail |
| :---: | :--- | :--- | :--- | :--- | :---: |
| 1 | Sinh viên A xem file đính kèm của mình | Session Sinh viên A | Backend stream thành công dữ liệu file `minh_chung_A.pdf`. | HTTP 200 OK<br><br>`Content-Type: application/pdf` | Pass |
| 2 | Truy cập URL file trực tiếp không qua Token | `GET /api/v1/attachments/att_1001` (Không gửi Bearer Token) | Hệ thống từ chối truy cập. | HTTP 401 Unauthorized | Pass |
| 3 | Sinh viên B dùng Token của mình truy cập URL file của Sinh viên A | Session Sinh viên B<br><br>`GET /api/v1/attachments/att_1001` | Hệ thống chặn phân quyền dữ liệu. | HTTP 403 Forbidden<br><br>`FORBIDDEN_ACCESS` | Pass |
| 4 | Nhân viên thuộc phòng ban thụ lý Ticket xem file | Session Nhân viên `staff_edu` | Tải/Xem file thành công do đúng phạm vi phòng ban. | HTTP 200 OK | Pass |