# Kịch Bản Kiểm Thử Chấp Nhận Người Dùng (UAT Test Scenarios)

Tài liệu này cung cấp danh sách các test cases tiêu chuẩn phục vụ cho đợt kiểm thử chấp nhận người dùng (UAT 10 ngày làm việc) tại Aurora University.

---

## 1. Phân Hệ Sinh Viên (Student Portal UAT)

### Scenario ID: `UAT-STU-02` - Sinh viên tạo Ticket hỗ trợ mới

* **Mục tiêu:** Kiểm tra sinh viên tạo Ticket thành công kèm file đính kèm và kiểm tra quy tắc chống tạo trùng lặp.
* **Tiền điều kiện:** Sinh viên đã đăng nhập vào hệ thống.

| Các bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi (Expected Result) | Đánh giá |
| :--- | :--- | :--- | :---: |
| 1. Nhấn nút "Tạo Ticket". | - | Hiển thị form tạo Ticket. | Pass |
| 2. Chọn nhóm vấn đề, nhập Tiêu đề, Mô tả và đính kèm file. | Nhóm: "Đào tạo"<br>Mô tả: "Đăng ký hoãn thi môn CSDL"<br>File: `xac_nhan.pdf` (2MB) | Form điền đầy đủ dữ liệu hợp lệ. | Pass |
| 3. Bấm nút "Gửi yêu cầu" 3 lần liên tiếp (Double-click / Retry). | Thao tác nhấp nút liên tục. | Hệ thống chỉ tạo **01 Ticket duy nhất**, cấp Mã Ticket (ví dụ: `TK-20261007-001`) và hiển thị thông báo thành công. | Pass |
| 4. Tạo Ticket mới nhưng để trống trường Mô tả. | Mô tả: `""` (bỏ trống). | Hệ thống từ chối tạo Ticket, hiển thị lỗi validation: "Mô tả vấn đề là bắt buộc". | Pass |

---

## 2. Phân Hệ Nhân Viên (Staff Operations UAT)

### Scenario ID: `UAT-STF-03` - Chuyển tiếp Ticket sang phòng ban khác

* **Mục tiêu:** Kiểm tra chức năng chuyển Ticket sai thẩm quyền sang phòng ban chuyên trách khác.
* **Tiền điều kiện:** Nhân viên Phòng Đào tạo đã đăng nhập, có Ticket ở trạng thái `IN_PROGRESS`.

| Các bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi (Expected Result) | Đánh giá |
| :--- | :--- | :--- | :---: |
| 1. Chọn nút "Chuyển phòng ban". | - | Hiển thị danh sách phòng ban đích. | Pass |
| 2. Chọn phòng ban "Phòng Tài chính" và nhập Lý do chuyển. | PB: "Phòng Tài chính"<br>Lý do: "Yêu cầu liên quan đến miễn giảm học phí". | Hệ thống cập nhật trạng thái Ticket thành `TRANSFERRED`, cập nhật phòng ban thụ lý mới và ghi vết lịch sử. | Pass |
| 3. Kiểm tra danh sách làm việc của Phòng Tài chính. | - | Ticket xuất hiện trong danh sách chờ tiếp nhận của Phòng Tài chính. | Pass |

---

### Scenario ID: `UAT-STF-05` - Ghi nhận kết quả giải quyết và Đóng Ticket

* **Mục tiêu:** Kiểm tra quy tắc bắt buộc nhập ghi chú kết quả giải quyết khi hoàn tất đóng Ticket.
* **Tiền điều kiện:** Nhân viên đang xử lý Ticket ở trạng thái `IN_PROGRESS`.

| Các bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi (Expected Result) | Đánh giá |
| :--- | :--- | :--- | :---: |
| 1. Chọn nút "Hoàn thành & Đóng Ticket". | - | Hiển thị ô nhập Ghi chú kết quả giải quyết. | Pass |
| 2. Nhập dấu khoảng trắng "   " và bấm Xác nhận. | `resolution_note`: `"   "` | Hệ thống chặn thao tác, báo lỗi: "Kết quả giải quyết không được để trống". | Pass |
| 3. Nhập đầy đủ nội dung kết quả xử lý và bấm Xác nhận. | `resolution_note`: "Đã cập nhật miễn giảm học phí cho SV". | Ticket chuyển trạng thái thành `CLOSED`, cập nhật `closed_at` và gửi thông báo kết quả cho Sinh viên. | Pass |

---

## 3. Phân Hệ Bảo Mật & Phân Quyền (Security UAT)

### Scenario ID: `UAT-SEC-02` - Kiểm soát quyền truy cập File đính kèm

* **Mục tiêu:** Đảm bảo file đính kèm không thể bị truy cập công khai bởi người dùng không liên quan.
* **Tiền điều kiện:** Có Ticket `TK-001` chứa file đính kèm `minh_chung.pdf` thuộc về Sinh viên A.

| Các bước thực hiện | Dữ liệu đầu vào | Kết quả mong đợi (Expected Result) | Đánh giá |
| :--- | :--- | :--- | :---: |
| 1. Sinh viên A đăng nhập và nhấn xem/tải file `minh_chung.pdf`. | Tài khoản Sinh viên A. | Tải/Xem file thành công. | Pass |
| 2. Sinh viên B đăng nhập, dùng URL truy cập trực tiếp file `minh_chung.pdf` của Sinh viên A. | URL file đính kèm của Sinh viên A. | Hệ thống từ chối truy cập, trả về lỗi `403 Forbidden`. | Pass |