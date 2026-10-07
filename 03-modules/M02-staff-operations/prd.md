# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Nhân Viên (PRD - M02 Staff Operations)

## 1. Tổng Quan Phân Hệ

Phân hệ **Nhân viên (Staff Operations)** là không gian tác nghiệp chuyên môn dành cho cán bộ, chuyên viên thuộc các Phòng ban chức năng tại **Aurora University** (Phòng Đào tạo, Phòng CTHSSV, Phòng Tài chính - Kế toán, Trung tâm CNTT, Thư viện...). Phân hệ hỗ trợ tiếp nhận, phân loại, phân công, điều phối liên phòng ban, xử lý yêu cầu và đóng Ticket theo quy trình chuẩn hóa.

### Danh mục Chức năng & Phân bổ Công sức (Tổng: 197h)

| Mã Chức Năng | Tên Chức Năng | Phạm Vi Nghiệp Vụ | Effort Cơ Sở | Buffer | Effort Kế Hoạch |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **FR-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | Hòm thư công việc phân loại theo tab, tìm kiếm mã Ticket, bộ lọc đa chiều. | 33h | 0h | **33h** |
| **FR-STF-02** | Phân loại & phân công xử lý | Nhân viên tự nhận (`Claim`) hoặc Trưởng phòng phân công (`Assign`) chuyên viên phụ trách. | 37h | 1h | **38h** |
| **FR-STF-03** | Quản lý ưu tiên & thời hạn | Thiết lập độ ưu tiên (`Low`, `Medium`, `High`, `Urgent`), tính toán và theo dõi hạn SLA. | 26h | 3h | **29h** |
| **FR-STF-04** | Xử lý & cập nhật yêu cầu | Ghi chú nội bộ, gửi yêu cầu bổ sung hồ sơ (tạm dừng SLA), cập nhật tiến trình. | 36h | 3h | **39h** |
| **FR-STF-05** | Chuyển xử lý, Escalation & hoàn tất | Chuyển tiếp phòng ban (Transfer), báo cáo vượt cấp (Escalation) và hoàn tất giải quyết (Resolve). | 29h | 3h | **32h** |
| **FR-STF-06** | Đóng & mở lại yêu cầu | Đóng Ticket tự động (sau 3 ngày `RESOLVED`) hoặc thủ công; mở lại Ticket khi có khiếu nại. | 26h | 0h | **26h** |
| **TỔNG CỘNG** | | | **187h** | **10h** | **197h** |

---

## 2. Đặc Tả Chi Tiết Chức Năng

### [FR-STF-01] Tiếp nhận, tìm kiếm & lọc yêu cầu

**Mô tả**  
Cung cấp Hòm thư công việc (Staff Inbox) hiển thị toàn bộ các yêu cầu gửi đến phòng ban, hỗ trợ tìm kiếm nhanh và lọc đa điều kiện.

**Actor**  
Nhân viên phòng ban (Staff / Support Agent).

**Preconditions**  
Nhân viên đã đăng nhập và được gán thuộc ít nhất 01 Phòng ban chuyên trách.

**Luồng chính**  
1. Nhân viên truy cập **Hòm thư công việc**.
2. Hệ thống hiển thị danh sách Ticket chia theo các tab tác nghiệp:
   - **Chưa tiếp nhận (New)**: Ticket mới gửi đến phòng ban chưa có người nhận.
   - **Tôi đang xử lý (My Assigned)**: Ticket do cá nhân nhân viên đang thụ lý.
   - **Chờ sinh viên bổ sung (Pending Student)**: Ticket đang chờ phản hồi từ sinh viên.
   - **Quá hạn / Sắp quá hạn (Overdue / Warning)**: Ticket sắp hoặc đã vượt thời hạn SLA.
3. Nhân viên có thể tìm kiếm theo Mã Ticket hoặc Tên sinh viên.
4. Nhân viên chọn bộ lọc (Mức độ ưu tiên, Khoảng thời gian, Nhóm danh mục).
5. Hệ thống trả về danh sách kết quả phù hợp theo thời gian thực.

**Business Rules**  
- Nhân viên chỉ được xem Ticket thuộc Phòng ban mà tài khoản của mình được phân quyền.

**Alternative / Error Flows**  
- **Không tìm thấy kết quả**: Hiển thị bảng trống kèm thông báo "Không có yêu cầu nào phù hợp với điều kiện tìm kiếm".

**Acceptance Criteria**  
- **AC-01**: Hiển thị chính xác danh sách Ticket thuộc đúng Phòng ban của nhân viên đăng nhập.
- **AC-02**: Bộ lọc tìm kiếm phản hồi nhanh, dữ liệu cập nhật tức thì.

**Ví dụ Edge Case**  
Nhân viên thuộc Phòng Đào tạo đăng nhập hệ thống.  
-> **Expected Result**: Hòm thư chỉ hiển thị Ticket gửi đến Phòng Đào tạo, tuyệt đối không nhìn thấy Ticket của Phòng CTHSSV hay Tài chính.

---

### [FR-STF-02] Phân loại & phân công xử lý

**Mô tả**  
Cho phép nhân viên tự nhận tiếp nhận xử lý Ticket (`Claim`) hoặc Trưởng phòng thực hiện phân công (`Assign`) Ticket cho chuyên viên trong phòng ban.

**Actor**  
Nhân viên phòng ban / Trưởng phòng ban (Manager).

**Preconditions**  
Ticket đang ở trạng thái `NEW` hoặc chưa có người phụ trách.

**Luồng chính**  
1. Người dùng mở chi tiết Ticket cần tiếp nhận/phân công.
2. **Trường hợp Nhân viên tự nhận (Claim):**
   - Nhân viên nhấn nút **Tiếp nhận xử lý (Claim)**.
   - Hệ thống gán `assigned_staff_id = current_user_id`.
   - Trạng thái Ticket chuyển từ `NEW` sang `IN_PROGRESS`.
3. **Trường hợp Trưởng phòng phân công (Assign):**
   - Trưởng phòng chọn chuyên viên từ danh sách nhân sự của phòng ban.
   - Trưởng phòng nhấn **Xác nhận phân công**.
   - Hệ thống cập nhật người phụ trách và gửi thông báo tới chuyên viên đó.
4. Hệ thống ghi nhận lịch sử vào Audit Trail.

**Business Rules**  
- Một Ticket tại một thời điểm chỉ có tối đa **01 người phụ trách chính**.
- Tránh xung đột tiếp nhận (Race condition): Khóa nút Claim nếu một nhân viên khác vừa nhận trước đó 1 tích tắc.

**Alternative / Error Flows**  
- **Hai nhân viên cùng bấm Claim cùng lúc**: Nhân viên gửi request trước sẽ nhận thành công; nhân viên gửi sau nhận thông báo "Ticket này đã được tiếp nhận bởi đồng nghiệp".

**Acceptance Criteria**  
- **AC-01**: Bấm Claim -> Ticket chuyển sang `IN_PROGRESS`, gán đúng tên người phụ trách.
- **AC-02**: Phân công chuyên viên -> Chuyên viên nhận thông báo và Ticket xuất hiện trong tab "Tôi đang xử lý".

**Ví dụ Edge Case**  
Trưởng phòng phân công Ticket cho chuyên viên A khi chuyên viên A đang offline.  
-> **Expected Result**: Ticket được gán thành công, khi chuyên viên A đăng nhập sẽ thấy Ticket ngay trong danh sách cá nhân.

---

### [FR-STF-03] Quản lý ưu tiên & thời hạn

**Mô tả**  
Cho phép thiết lập Mức độ ưu tiên cho Ticket, tự động tính toán thời hạn cam kết xử lý (`sla_due_at`) và kích hoạt cảnh báo khi sắp hoặc đã quá hạn.

**Actor**  
Nhân viên phụ trách Ticket.

**Preconditions**  
Ticket đang ở trạng thái `IN_PROGRESS`.

**Luồng chính**  
1. Nhân viên mở màn hình Chi tiết Ticket.
2. Nhân viên chọn chức năng **Thiết lập mức độ ưu tiên**.
3. Nhân viên chọn một trong 4 mức: `Thấp (Low)`, `Trung bình (Medium)`, `Cao (High)`, hoặc `Khẩn cấp (Urgent)`.
4. Hệ thống tự động tính lại mốc thời gian hoàn thành (`sla_due_at`) căn cứ theo bảng quy chuẩn SLA.
5. Khi thời gian còn lại đến hạn `<= 2 giờ làm việc`, hệ thống gửi thông báo nhắc nhở (SLA Warning).
6. Khi quá hạn, hệ thống đổi màu nhãn sang màu đỏ cảnh báo và thông báo cho Nhân viên cùng Trưởng phòng.

**Business Rules**  
- Mặc định khởi tạo Ticket có mức ưu tiên là `Trung bình (Medium)`.
- Khi Ticket chuyển sang trạng thái `WAITING_STUDENT`, bộ đếm thời gian SLA tự động tạm dừng theo quy tắc `BR-SUP-01`.

**Alternative / Error Flows**  
- **Người dùng không phải người phụ trách**: Khóa quyền thay đổi mức độ ưu tiên (chế độ chỉ xem).

**Acceptance Criteria**  
- **AC-01**: Thay đổi mức ưu tiên sang `Urgent` -> Mốc `sla_due_at` rút ngắn và hiển thị cảnh báo đỏ tương ứng.
- **AC-02**: Bộ đếm SLA dừng chạy khi Ticket ở trạng thái `WAITING_STUDENT`.

**Ví dụ Edge Case**  
Một Ticket có hạn xử lý lúc 16:00. Lúc 16:01 Ticket vẫn chưa chuyển `RESOLVED`.  
-> **Expected Result**: Hệ thống gắn cờ quá hạn (Overdue) và phát thông báo cảnh báo tới Trưởng phòng ban.

---

### [FR-STF-04] Xử lý & cập nhật yêu cầu

**Mô tả**  
Cung cấp các công cụ tác nghiệp chuyên môn: ghi nhận ghi chú nội bộ, yêu cầu sinh viên bổ sung giấy tờ và cập nhật diễn biến xử lý Ticket.

**Actor**  
Nhân viên phụ trách Ticket.

**Preconditions**  
Ticket đang ở trạng thái `IN_PROGRESS`.

**Luồng chính**  
1. Nhân viên mở chi tiết Ticket đang thụ lý.
2. **Ghi chú nội bộ (Internal Notes):**
   - Nhân viên nhập nội dung trao đổi chuyên môn với đồng nghiệp trong phòng.
   - Nhấn **Lưu ghi chú**. Nội dung hiển thị dạng thẻ màu vàng (chỉ nhân viên/quản lý thấy, sinh viên không thấy).
3. **Yêu cầu bổ sung hồ sơ:**
   - Nhân viên nhập danh mục giấy tờ cần làm rõ.
   - Nhấn **Gửi yêu cầu bổ sung**.
   - Hệ thống chuyển Ticket sang `WAITING_STUDENT`, tạm dừng tính SLA và gửi thông báo cho sinh viên.
4. **Tiếp tục xử lý sau bổ sung:**
   - Khi sinh viên tải hồ sơ mới lên, hệ thống tự động đưa Ticket về `IN_PROGRESS` để nhân viên tiếp tục xử lý.

**Business Rules**  
- Ghi chú nội bộ bắt buộc phải được cách ly bảo mật tuyệt đối khỏi giao diện của sinh viên.
- Yêu cầu bổ sung là thông tin bắt buộc, không được để trống.

**Alternative / Error Flows**  
- **Để trống nội dung yêu cầu bổ sung**: Hệ thống cảnh báo "Vui lòng nhập nội dung cần sinh viên bổ sung".

**Acceptance Criteria**  
- **AC-01**: Gửi yêu cầu bổ sung -> Trạng thái đổi sang `WAITING_STUDENT`, sinh viên nhận được thông báo ngay.
- **AC-02**: Ghi chú nội bộ chỉ hiển thị với nhân viên cùng phòng ban.

**Ví dụ Edge Case**  
Sinh viên mở màn hình xem Ticket sau khi nhân viên đã lưu một ghi chú nội bộ.  
-> **Expected Result**: Sinh viên chỉ thấy lịch sử trao đổi công khai, hoàn toàn không nhìn thấy ghi chú nội bộ của nhân viên.

---

### [FR-STF-05] Chuyển xử lý, Escalation & hoàn tất

**Mô tả**  
Hỗ trợ chuyển tiếp Ticket sang Phòng ban khác khi sinh viên gửi nhầm địa chỉ (Transfer), báo cáo lên cấp quản lý khi gặp vướng mắc (Escalation), hoặc cập nhật kết quả giải quyết chính thức (Resolve).

**Actor**  
Nhân viên phụ trách Ticket / Trưởng phòng ban.

**Preconditions**  
Ticket đang ở trạng thái `IN_PROGRESS`.

**Luồng chính (Chuyển phòng ban / Escalation)**  
1. Nhân viên chọn chức năng **Chuyển phòng ban**.
2. Chọn phòng ban đích và nhập **Lý do chuyển** (bắt buộc tối thiểu 10 ký tự).
3. Nhấn **Xác nhận chuyển**.
4. Hệ thống cập nhật `department_id`, đặt `assigned_staff_id = NULL` để phòng ban mới tiếp nhận.

**Luồng chính (Hoàn tất giải quyết - Resolve)**  
1. Nhân viên chọn chức năng **Hoàn thành yêu cầu**.
2. Nhập nội dung kết quả giải quyết và đính kèm file kết quả (nếu có).
3. Nhấn **Xác nhận hoàn thành**.
4. Hệ thống chuyển Ticket sang `RESOLVED`, lưu mốc thời gian `resolved_at` và gửi thông báo kết quả cho sinh viên.

**Business Rules**  
- Bắt buộc nhập lý do khi chuyển phòng ban theo quy định `BR-XFR-01`.
- Nhân viên phòng ban cũ mất quyền chỉnh sửa Ticket sau khi đã chuyển thành công.

**Alternative / Error Flows**  
- **Nhập lý do chuyển dưới 10 ký tự**: Hệ thống báo lỗi và yêu cầu nhập lý do chi tiết hơn.

**Acceptance Criteria**  
- **AC-01**: Chuyển phòng ban thành công -> Ticket chuyển sang hòm thư phòng mới, nhân viên cũ mất quyền chỉnh sửa.
- **AC-02**: Nhấn Hoàn thành -> Ticket chuyển `RESOLVED`, sinh viên nhận được thông báo kèm kết quả.

**Ví dụ Edge Case**  
Sinh viên gửi nhầm thắc mắc học phí vào Phòng Đào tạo. Chuyên viên chuyển sang Phòng Tài chính kèm lý do "Vấn đề liên quan đến công nợ học phí".  
-> **Expected Result**: Ticket xuất hiện ngay trong hòm thư Phòng Tài chính - Kế toán.

---

### [FR-STF-06] Đóng & mở lại yêu cầu

**Mô tả**  
Xử lý việc đóng Ticket tự động hoặc thủ công sau khi hoàn thành, đồng thời hỗ trợ quy trình mở lại yêu cầu (Reopen) khi sinh viên có khiếu nại trong thời hạn quy định.

**Actor**  
Nhân viên / Quản lý / Hệ thống tự động.

**Preconditions**  
Ticket đang ở trạng thái `RESOLVED`.

**Luồng chính**  
1. **Tự động đóng:** Sau 03 ngày làm việc ở trạng thái `RESOLVED`, nếu sinh viên không có khiếu nại hoặc đã hoàn thành đánh giá CSAT, hệ thống tự động chuyển trạng thái Ticket sang `CLOSED`.
2. **Đóng thủ công:** Nhân viên/Quản lý nhấn nút **Đóng Ticket** sau khi kiểm tra xong mọi nghĩa vụ.
3. **Mở lại Ticket (Reopen):** Nếu sinh viên phản hồi khiếu nại trong vòng 03 ngày kể từ khi `RESOLVED`, Ticket được kích hoạt mở lại và chuyển về trạng thái `IN_PROGRESS`.

**Business Rules**  
- Ticket ở trạng thái `CLOSED` là trạng thái kết thúc, hệ thống khóa toàn bộ các chức năng chỉnh sửa nội dung nghiệp vụ.

**Alternative / Error Flows**  
- **Khiếu nại sau khi đã CLOSED quá hạn**: Hệ thống hướng dẫn sinh viên tạo một Ticket mới thay vì mở lại Ticket cũ.

**Acceptance Criteria**  
- **AC-01**: Sau 3 ngày ở `RESOLVED` không tương tác -> Tự động chuyển sang `CLOSED`.
- **AC-02**: Ticket ở trạng thái `CLOSED` hiển thị ở dạng chỉ xem (Read-only).