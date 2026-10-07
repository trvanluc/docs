# Phân Hệ Nhân Viên (M02 - Staff Operations)

## I. TỔNG QUAN PHÂN HỆ
Phân hệ Nhân viên tối ưu hóa quy trình tiếp nhận, phân loại, đánh giá độ ưu tiên, điều phối công việc liên phòng ban, nhắn yêu cầu sinh viên bổ sung thông tin/giấy tờ còn thiếu, cập nhật tiến độ, ghi lại kết quả và đóng yêu cầu sau khi hoàn thành[cite: 1].

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STF-01] Nhân viên đăng nhập hệ thống

**Mô tả**  
Nhân viên đăng nhập hệ thống bằng tài khoản nghiệp vụ riêng để thực hiện công tác quản lý, tiếp nhận và xử lý các yêu cầu hỗ trợ[cite: 1].

**Actor**  
Nhân viên phòng ban (Staff)[cite: 1].

**Preconditions**  
- Tài khoản nhân viên đã được Quản lý khởi tạo và cấp quyền phù hợp trong hệ thống[cite: 1].

**Luồng chính**  
1. Nhân viên truy cập cổng UniSupport, chọn trang đăng nhập nhân viên[cite: 1].
2. Nhập **Tên đăng nhập / Email công vụ** và **Mật khẩu**[cite: 1].
3. Nhấn **Đăng nhập**.
4. Hệ thống xác thực thông tin và chuyển hướng đến giao diện công việc của Nhân viên.

**Business Rules**  
- Người dùng đăng nhập bằng tài khoản và mật khẩu riêng[cite: 1].
- Mỗi vai trò chỉ thấy và thao tác được trong phạm vi quyền của mình[cite: 1].

**Alternative / Error Flows**  
- Đăng nhập thất bại do sai thông tin -> Hệ thống hiển thị thông báo lỗi validation.

**Acceptance Criteria**  
- **AC-01:** Đăng nhập thành công với tài khoản nhân viên -> Hiển thị danh sách yêu cầu mới và các yêu cầu đang được giao cho mình[cite: 1].

---

### [FR-STF-02] Tiếp nhận và phân loại yêu cầu

**Mô tả**  
Cho phép nhân viên xem danh sách yêu cầu mới, phân loại yêu cầu theo từng nhóm vấn đề và xem xét mức độ cần ưu tiên[cite: 1].

**Actor**  
Nhân viên đã đăng nhập hệ thống[cite: 1].

**Preconditions**  
- Có Ticket mới (`NEW`) gửi đến phòng ban của nhân viên[cite: 1].

**Luồng chính**  
1. Nhân viên mở danh sách yêu cầu mới[cite: 1].
2. Chọn một Ticket để xem chi tiết nội dung và file đính kèm[cite: 1].
3. Nhấn nút **Tiếp nhận xử lý**.
4. Phân loại yêu cầu theo từng nhóm vấn đề và xem xét mức độ cần ưu tiên (`LOW`, `MEDIUM`, `HIGH`, `URGENT`)[cite: 1].
5. Nhấn **Xác nhận**.
6. Hệ thống chuyển trạng thái Ticket sang `IN_PROGRESS` và gán cá nhân nhân viên làm người phụ trách trực tiếp[cite: 1].

**Business Rules**  
- Nhân viên tiếp nhận sẽ trở thành người phụ trách chính của Ticket đó[cite: 1].

**Alternative / Error Flows**  
- Nếu Ticket đã bị nhân viên khác trong cùng phòng ban tiếp nhận trước, hệ thống báo lỗi: "Yêu cầu này đã được tiếp nhận bởi nhân viên khác".

**Acceptance Criteria**  
- **AC-01:** Tiếp nhận thành công -> Trạng thái đổi thành `IN_PROGRESS`, hiển thị tên người phụ trách[cite: 1].

---

### [FR-STF-03] Chuyển sang đúng phòng ban hoặc người phụ trách

**Mô tả**  
Cho phép nhân viên chuyển sang đúng phòng ban hoặc người phụ trách nếu yêu cầu không thuộc phần việc của mình[cite: 1].

**Actor**  
Nhân viên đang tiếp nhận hoặc phụ trách Ticket[cite: 1].

**Preconditions**  
- Ticket chưa ở trạng thái đóng/hoàn thành (`CLOSED`)[cite: 1].

**Luồng chính**  
1. Trong màn hình chi tiết Ticket, nhân viên chọn **Chuyển phòng ban**[cite: 1].
2. Hệ thống hiển thị danh sách các phòng ban khả dụng.
3. Nhân viên chọn **Phòng ban / Người phụ trách mới** và nhập lý do chuyển tiếp[cite: 1].
4. Nhấn **Xác nhận chuyển**.
5. Hệ thống đổi trạng thái Ticket thành `TRANSFERRED`, cập nhật đơn vị phụ trách mới[cite: 1].
6. Hệ thống phát thông báo nội bộ tới phòng ban/người phụ trách mới[cite: 1].

**Business Rules**  
- Phải nhập lý do chuyển giao mới được hoàn tất thao tác.
- Lịch sử chuyển tiếp phòng ban phải được ghi vết để tra soát khi cần[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Chuyển phòng ban thành công -> Ticket xuất hiện trong danh sách của phòng ban mới[cite: 1].

---

### [FR-STF-04] Cập nhật tiến độ & Yêu cầu bổ sung thông tin

**Mô tả**  
Nhân viên cập nhật trạng thái để sinh viên biết yêu cầu đang được xử lý đến đâu và nhắn yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ còn thiếu nếu cần[cite: 1].

**Actor**  
Nhân viên phụ trách Ticket[cite: 1].

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS`[cite: 1].

**Luồng chính**  
1. Nhân viên chọn nút **Cập nhật tiến độ / Yêu cầu bổ sung**[cite: 1].
2. Nhắn yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ còn thiếu nếu cần[cite: 1].
3. Nhấn **Gửi yêu cầu**.
4. Hệ thống đổi trạng thái Ticket thành `NEED_MORE_INFO` và gửi thông báo cho sinh viên[cite: 1].

**Business Rules**  
- Chỉ gửi được yêu cầu bổ sung khi Ticket đang ở trạng thái xử lý[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Gửi tin nhắn bổ sung -> Trạng thái đổi sang `NEED_MORE_INFO`, sinh viên nhận được thông báo[cite: 1].

---

### [FR-STF-05] Ghi lại kết quả và đóng yêu cầu

**Mô tả**  
Nhân viên ghi lại kết quả và đóng yêu cầu sau khi hoàn thành[cite: 1].

**Actor**  
Nhân viên phụ trách Ticket[cite: 1].

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS`[cite: 1].

**Luồng chính**  
1. Nhân viên chọn nút **Ghi lại kết quả & Đóng yêu cầu**[cite: 1].
2. Hệ thống hiển thị ô nhập ghi lại kết quả giải quyết[cite: 1].
3. Nhân viên nhập chi tiết kết quả giải quyết[cite: 1].
4. Nhấn **Đóng yêu cầu**.
5. Hệ thống chuyển trạng thái Ticket sang `CLOSED`, lưu lại thời gian đóng và gửi thông báo kết quả cho sinh viên[cite: 1].

**Business Rules**  
- Ghi lại kết quả giải quyết là thông tin bắt buộc, không được để trống hoặc chỉ chứa khoảng trắng[cite: 1].

**Alternative / Error Flows**  
- Nếu bỏ trống kết quả giải quyết, hệ thống không cho phép đóng yêu cầu và hiển thị thông báo lỗi validation.

**Acceptance Criteria**  
- **AC-01:** Nhập đầy đủ kết quả và đóng -> Trạng thái đổi thành `CLOSED`, sinh viên xem được kết quả giải quyết[cite: 1].
- **AC-02:** Để trống kết quả -> Hệ thống báo lỗi, không cho đóng Ticket.

**Ví dụ Edge Case**  
Nhân viên chỉ nhập khoảng trắng "   " vào ô kết quả giải quyết.

**Expected Result:** Hệ thống báo lỗi "Kết quả giải quyết không được để trống" và ngăn thao tác đóng yêu cầu.