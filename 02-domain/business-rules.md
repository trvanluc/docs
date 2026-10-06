# Quy Tắc Nghiệp Vụ Cốt Lõi (Business Rules)

Tài liệu này tổng hợp toàn bộ các Quy tắc nghiệp vụ (Business Rules - BR) áp dụng bắt buộc trên toàn hệ thống UniSupport.

---

## 1. Nhóm Quy Tắc Quản Lý File Đính Kèm & Bảo Mật (`BR-FILE`)

### `BR-FILE-01`: Phân quyền truy cập tệp đính kèm (Attachment Access Control)
- **Nội dung**: File đính kèm của Ticket không được lưu trữ ở đường dẫn public công khai.
- **Quy tắc**:
  - Chỉ **Sinh viên tạo ra Ticket đó** và **Nhân viên thuộc Phòng ban thụ lý Ticket** mới có quyền tải/xem file.
  - Quản trị viên hệ thống có quyền xem phục vụ mục đích kiểm tra Audit Log.
  - Mọi yêu cầu tải file phải thông qua một Secured API Endpoint có xác thực Token và kiểm tra vai trò người dùng.

### `BR-FILE-02`: Định dạng và dung lượng file hợp lệ
- **Nội dung**: Kiểm soát loại file tải lên để bảo đảm an toàn hệ thống và tối ưu bộ nhớ.
- **Quy tắc**:
  - Chỉ chấp nhận các định dạng tệp: `.pdf`, `.png`, `.jpg`, `.jpeg`.
  - Dung lượng tối đa cho mỗi tệp: **10 MB (10,485,760 Bytes)**.
  - Tối đa **03 tệp đính kèm** cho một lần khởi tạo hoặc bổ sung Ticket.

---

## 2. Nhóm Quy Tắc Chuyển Phòng Ban & Phân Công (`BR-XFR`)

### `BR-XFR-01`: Điều kiện và Luồng chuyển phòng ban (Department Transfer)
- **Nội dung**: Cho phép chuyển Ticket sang phòng ban khác nếu sinh viên chọn nhầm đơn vị xử lý.
- **Quy tắc**:
  - Bắt buộc nhân viên phải nhập **Lý do chuyển phòng ban** (Tối thiểu 10 ký tự).
  - Ngay khi chuyển phòng ban thành công:
    1. Trường `department_id` cập nhật sang Phòng ban mới.
    2. Trường `assigned_staff_id` tự động đặt về `NULL` (chờ nhân viên phòng ban mới Claim/Assign).
    3. Hệ thống gửi thông báo In-app tới Hòm thư công việc của Phòng ban mới.
    4. Trạng thái Ticket vẫn giữ nguyên là `IN_PROGRESS`.

---

## 3. Nhóm Quy Tắc Yêu Cầu Bổ Sung Hồ Sơ (`BR-SUP`)

### `BR-SUP-01`: Tạm dừng đếm giờ SLA khi chờ sinh viên bổ sung
- **Nội dung**: Bảo vệ KPI xử lý của nhân viên khi nguyên nhân chậm trễ do sinh viên chưa cung cấp đủ hồ sơ.
- **Quy tắc**:
  - Khi nhân viên phát yêu cầu bổ sung, trạng thái chuyển sang `WAITING_STUDENT`.
  - Bộ đếm thời gian SLA (SLA Timer) tạm thời **ĐỪNG/TẠM DỪNG**.
  - Ngay khi sinh viên gửi câu trả lời hoặc đăng tải file bổ sung, trạng thái tự động chuyển về `IN_PROGRESS` và bộ đếm SLA tiếp tục chạy tiếp.

---

## 4. Nhóm Quy Tắc Đánh Giá Hài Lòng (`BR-RAT`)

### `BR-RAT-01`: Điều kiện và thời hạn đánh giá hài lòng
- **Nội dung**: Đảm bảo sinh viên chỉ đánh giá đúng trải nghiệm thực tế sau khi yêu cầu đã giải quyết.
- **Quy tắc**:
  - Tính năng đánh giá (1-5 sao) chỉ hiển thị khi Ticket ở trạng thái `RESOLVED` hoặc `CLOSED`.
  - Mỗi Ticket chỉ được phép gửi đánh giá **Duy nhất 01 lần**.
  - Thời hạn sinh viên được thực hiện đánh giá là trong vòng **07 ngày** kể từ mốc thời gian `resolved_at`. Quá thời hạn này, tính năng đánh giá sẽ tự động khóa.

---

## 5. Nhóm Quy Tắc Tra Soát Hệ Thống (`BR-AUD`)

### `BR-AUD-01`: Bất biến dữ liệu nhật ký tra soát (Audit Trail Integrity)
- **Nội dung**: Đảm bảo tính toàn vẹn của lịch sử thao tác phục vụ tra soát khi có khiếu nại.
- **Quy tắc**:
  - Toàn bộ các bản ghi trong Bảng Nhật ký (`Activity Log / Audit Log`) là **chỉ ghi (Append-only)**.
  - Nghiêm cấm mọi hành vi sửa (UPDATE) hoặc xóa (DELETE) dữ liệu nhật ký, kể cả tài khoản Quản trị viên (Admin).
  - Tất cả các mốc thời gian ghi nhận trong log bắt buộc lưu trữ dưới chuẩn **UTC / ISO-8601** và quy đổi hiển thị theo múi giờ local (`GMT+7`).