# Kịch bản Kiểm thử & Test Cases UAT (Test Scenarios & UAT Acceptance)

### 1. Tổng quan
Tài liệu cung cấp danh sách các kịch bản kiểm thử chấp nhận người dùng (UAT) phục vụ cho giai đoạn nghiệm thu **10 ngày làm việc** của Aurora University (theo Mục 5.2 trong Proposal).

### 2. Danh sách Kịch bản Kiểm thử Nghiệm thu (UAT Test Scenarios)

#### 2.1 Phân hệ Sinh viên (M01 - Student Portal)

##### [TS-STU-02] Kiểm thử Chức năng Tạo Ticket hỗ trợ
- **Tiền điều kiện:** Sinh viên đã đăng nhập tài khoản hợp lệ.
- **Các bước thực hiện:**
  1. Vào màn hình **Tạo Ticket**.
  2. Chọn nhóm vấn đề (VD: Phòng Đào tạo), nhập tiêu đề và nội dung mô tả.
  3. Đính kèm 1 tệp tài liệu dạng `.pdf` (dung lượng < 10 MB).
  4. Nhấn **Gửi yêu cầu**.
- **Kết quả mong đợi:** 
  - Hệ thống sinh mã Ticket duy nhất, chuyển trạng thái Ticket thành `Mới`.
  - Hiển thị thông báo tạo thành công và đính kèm tệp PDF chính xác.
- **Tiêu chí Chấp nhận (Pass Criteria):** Đạt tiêu chuẩn AC-01 đến AC-07 trong `WF-01`.

##### [TS-STU-05] Kiểm thử Chức năng Đánh giá hài lòng
- **Tiền điều kiện:** Ticket đã được nhân viên chuyển sang trạng thái `Hoàn thành`.
- **Các bước thực hiện:**
  1. Sinh viên mở chi tiết Ticket đã hoàn thành.
  2. Chọn số sao đánh giá (4/5 sao) và nhập nhận xét: "Xử lý nhanh, nhiệt tình".
  3. Nhấn **Gửi đánh giá**.
- **Kết quả mong đợi:** Hệ thống ghi nhận đánh giá, khóa form không cho phép gửi lại.

---

#### 2.2 Phân hệ Nhân viên (M02 - Staff Operations)

##### [TS-STF-01] Kiểm thử Tiếp nhận và Phân loại Ticket
- **Tiền điều kiện:** Đã có Ticket mới ở trạng thái `Mới`.
- **Các bước thực hiện:**
  1. Nhân viên truy cập danh sách tiếp nhận.
  2. Nhấn nút **Tiếp nhận** (Claim) trên Ticket.
  3. Thay đổi độ ưu tiên thành `Cao`.
- **Kết quả mong đợi:** Ticket đổi trạng thái thành `Đang xử lý`, tài khoản nhân viên được gán làm người phụ trách chính.

##### [TS-STF-02] Kiểm thử Chuyển tiếp phòng ban
- **Tiền điều kiện:** Ticket đang thuộc phòng Công tác sinh viên.
- **Các bước thực hiện:**
  1. Nhân viên chọn nút **Chuyển phòng ban**.
  2. Chọn phòng đích là "Phòng Tài chính - Kế toán" và nhập lý do: "Yêu cầu liên quan đến học phí".
  3. Nhấn **Xác nhận chuyển**.
- **Kết quả mong đợi:** Ticket được chuyển sang danh sách phòng Tài chính - Kế toán, ghi nhận đầy đủ nhật ký chuyển đổi.

---

#### 2.3 Phân hệ Quản lý & Bảo mật (M03 & M05)

##### [TS-SEC-01] Kiểm thử Bảo mật Truy cập File đính kèm
- **Tiền điều kiện:** Sinh viên A sở hữu Ticket chứa file đính kèm `docA.pdf`. Sinh viên B đăng nhập ở trình duyệt khác.
- **Các bước thực hiện:**
  1. Copy đường dẫn truy cập trực tiếp file `docA.pdf`.
  2. Dán đường dẫn vào trình duyệt đã đăng nhập tài khoản Sinh viên B.
- **Kết quả mong đợi:** Hệ thống từ chối truy cập và trả về màn hình báo lỗi `403 Forbidden`.