# Kịch bản Kiểm thử & Test Cases UAT (Test Scenarios & UAT Acceptance)

> Nguồn chuẩn hóa phạm vi & chức năng: `Phan_bo_Resources_Antigravity.md`

### 1. Tổng quan
Tài liệu cung cấp danh sách các kịch bản kiểm thử chấp nhận người dùng (UAT) phục vụ cho giai đoạn nghiệm thu **10 ngày làm việc** của Aurora University sau 14 tuần phát triển (tương ứng với 17 Chức năng Nghiệp vụ).

---

### 2. Danh sách Kịch bản Kiểm thử Nghiệm thu (UAT Test Scenarios)

#### 2.1 Phân hệ Sinh viên (M1 - Student Portal)

##### [TS-STU-01] Kiểm thử Tra cứu hướng dẫn & FAQ (FR-STU-01)
- **Tiền điều kiện:** Người dùng truy cập Cổng hỗ trợ UniSupport.
- **Các bước thực hiện:**
  1. Vào mục Hướng dẫn & FAQ.
  2. Tìm kiếm từ khóa "học phí" hoặc "bảo lưu".
  3. Mở bài viết hướng dẫn chi tiết.
- **Kết quả mong đợi:** Hiển thị bài viết chính xác, có nút điều hướng tạo Ticket nhanh.

##### [TS-STU-02] Kiểm thử Tạo & Gửi yêu cầu hỗ trợ (FR-STU-02)
- **Tiền điều kiện:** Sinh viên đã đăng nhập tài khoản hợp lệ.
- **Các bước thực hiện:**
  1. Vào màn hình **Tạo Ticket**.
  2. Chọn nhóm vấn đề (VD: Phòng Đào tạo), nhập tiêu đề và nội dung mô tả.
  3. Đính kèm 1 tệp tài liệu dạng `.pdf` (dung lượng < 10 MB).
  4. Nhấn **Gửi yêu cầu**.
- **Kết quả mong đợi:** Hệ thống sinh mã Ticket duy nhất (VD: `TK-20261004-001`), chuyển trạng thái Ticket thành `NEW`, hiển thị thông báo thành công.

##### [TS-STU-03] Kiểm thử Xem & Theo dõi yêu cầu (FR-STU-03)
- **Tiền điều kiện:** Sinh viên đã có Ticket trong hệ thống.
- **Các bước thực hiện:**
  1. Vào mục **Danh sách Ticket của tôi**.
  2. Kiểm tra danh sách và bấm vào một Ticket cụ thể để xem Timeline.
- **Kết quả mong đợi:** Hiển thị đầy đủ lịch sử trao đổi, thông tin người phụ trách và tiến độ SLA.

##### [TS-STU-04] Kiểm thử Nhận thông báo trạng thái (FR-STU-04)
- **Tiền điều kiện:** Ticket của sinh viên có biến động (Nhân viên cập nhật tiến độ hoặc yêu cầu bổ sung).
- **Các bước thực hiện:**
  1. Quan sát biểu tượng Quả chuông trên Header.
  2. Nhấn vào thông báo để mở Ticket.
- **Kết quả mong đợi:** Badge quả chuông tăng số lượng, click vào điều hướng chính xác tới Ticket và đổi trạng thái thành "Đã đọc".

##### [TS-STU-05] Kiểm thử Bổ sung thông tin & Đánh giá hài lòng CSAT (FR-STU-05)
- **Tiền điều kiện:** Ticket đã được nhân viên chuyển sang trạng thái `RESOLVED`.
- **Các bước thực hiện:**
  1. Sinh viên mở chi tiết Ticket đã hoàn thành.
  2. Chọn số sao đánh giá (5 sao) và nhập nhận xét: "Xử lý nhanh, nhiệt tình".
  3. Nhấn **Gửi đánh giá**.
- **Kết quả mong đợi:** Hệ thống ghi nhận đánh giá CSAT, chuyển Ticket sang `CLOSED` và khóa form đánh giá.

---

#### 2.2 Phân hệ Nhân viên (M2 - Staff Operations)

##### [TS-STF-01] Kiểm thử Tiếp nhận, Tìm kiếm & Lọc yêu cầu (FR-STF-01)
- **Tiền điều kiện:** Nhân viên đã đăng nhập tài khoản thuộc Phòng Đào tạo.
- **Các bước thực hiện:**
  1. Truy cập Hòm thư công việc của phòng ban.
  2. Lọc theo trạng thái `NEW` và độ ưu tiên `High`.
- **Kết quả mong đợi:** Hiển thị chính xác các Ticket thỏa mãn điều kiện lọc.

##### [TS-STF-02] Kiểm thử Phân loại & Phân công xử lý (FR-STF-02)
- **Tiền điều kiện:** Có Ticket mới ở trạng thái `NEW`.
- **Các bước thực hiện:**
  1. Nhân viên nhấn nút **Tiếp nhận (Claim)** hoặc Trưởng phòng thực hiện **Assign**.
- **Kết quả mong đợi:** Ticket đổi trạng thái thành `IN_PROGRESS`, gán người phụ trách chính thức.

##### [TS-STF-03] Kiểm thử Quản lý ưu tiên & Thời hạn SLA (FR-STF-03)
- **Tiền điều kiện:** Ticket đang `IN_PROGRESS`.
- **Các bước thực hiện:**
  1. Đổi độ ưu tiên sang `Urgent`.
- **Kết quả mong đợi:** Mốc `sla_due_at` tự động tính lại rút ngắn thời gian và hiển thị cảnh báo đỏ.

##### [TS-STF-04] Kiểm thử Xử lý & Cập nhật yêu cầu (FR-STF-04)
- **Tiền điều kiện:** Ticket đang `IN_PROGRESS`.
- **Các bước thực hiện:**
  1. Nhấn **Yêu cầu bổ sung hồ sơ** gửi tới sinh viên.
- **Kết quả mong đợi:** Ticket chuyển sang `WAITING_STUDENT`, đồng hồ đếm SLA tạm dừng.

##### [TS-STF-05] Kiểm thử Chuyển xử lý & Hoàn tất (FR-STF-05)
- **Tiền điều kiện:** Ticket đang `IN_PROGRESS`.
- **Các bước thực hiện:**
  1. Chọn **Chuyển phòng ban**, chọn "Phòng Tài chính - Kế toán", nhập lý do hợp lệ (>10 ký tự).
  2. Xác nhận chuyển.
- **Kết quả mong đợi:** Ticket chuyển sang hòm thư Phòng Tài chính, gỡ bỏ nhân viên phụ trách cũ (`assigned_staff_id = NULL`).

##### [TS-STF-06] Kiểm thử Đóng & Mở lại yêu cầu (FR-STF-06)
- **Tiền điều kiện:** Ticket ở trạng thái `RESOLVED`.
- **Các bước thực hiện:**
  1. Sau 3 ngày không tương tác hoặc nhân viên xác nhận đóng thủ công.
- **Kết quả mong đợi:** Ticket chuyển sang `CLOSED`.

---

#### 2.3 Phân hệ Quản trị & Báo cáo (M3 - Admin / Management)

##### [TS-ADM-01] Kiểm thử Quản lý tài khoản & Phân quyền RBAC (FR-ADM-01)
- **Tiền điều kiện:** Admin đăng nhập.
- **Các bước thực hiện:**
  1. Tạo tài khoản nhân viên mới, gán role `STAFF` và gán Phòng CTHSSV.
  2. Đăng nhập bằng tài khoản mới.
- **Kết quả mong đợi:** Nhân viên mới chỉ thấy Ticket thuộc Phòng CTHSSV.

##### [TS-ADM-02] Kiểm thử Quản lý phòng ban & Danh mục (FR-ADM-02)
- **Tiền điều kiện:** Admin đăng nhập.
- **Các bước thực hiện:**
  1. Thêm nhóm vấn đề "Cấp lại bảng điểm song ngữ" vào Phòng Đào tạo.
- **Kết quả mong đợi:** Nhóm vấn đề mới xuất hiện ngay trên form tạo Ticket của sinh viên.

##### [TS-ADM-03] Kiểm thử Kiểm soát quyền truy cập & Audit Trail (FR-ADM-03)
- **Tiền điều kiện:** Sinh viên A có Ticket kèm file `don_xin_hoc.pdf`. Sinh viên B đăng nhập ở máy khác.
- **Các bước thực hiện:**
  1. Sinh viên B thử truy cập trực tiếp URL download file của Sinh viên A.
- **Kết quả mong đợi:** Hệ thống chặn truy cập, trả lỗi `403 Forbidden` và ghi nhận sự kiện vào Audit Log.

##### [TS-ADM-04] Kiểm thử Quản lý thời hạn lưu trữ (FR-ADM-04)
- **Tiền điều kiện:** Admin cấu hình dọn dẹp file tạm/mồ côi.
- **Các bước thực hiện:**
  1. Kích hoạt tính năng quét dọn tệp rác.
- **Kết quả mong đợi:** Hệ thống thu hồi dung lượng lưu trữ an toàn.

##### [TS-ADM-05] Kiểm thử Dashboard & Thống kê quản trị (FR-ADM-05)
- **Tiền điều kiện:** Người dùng có vai trò `MANAGER` hoặc `ADMIN` đăng nhập.
- **Các bước thực hiện:**
  1. Mở Dashboard, chuyển bộ lọc thời gian "Tháng này".
- **Kết quả mong đợi:** Các thẻ KPI và biểu đồ cập nhật số liệu chính xác theo thời gian thực.

##### [TS-ADM-06] Kiểm thử Báo cáo, Đánh giá hài lòng & Xuất dữ liệu (FR-ADM-06)
- **Tiền điều kiện:** Đã có dữ liệu Ticket hoàn thành và đánh giá CSAT.
- **Các bước thực hiện:**
  1. Chọn Báo cáo CSAT, nhấn nút **Xuất Excel**.
- **Kết quả mong đợi:** File Excel được tải xuống với đầy đủ thông tin số sao và nhận xét chi tiết.