# [WF-02] Tiếp nhận & Phân loại yêu cầu (Claim and Triage)

### [FR-STF-01] Nhân viên tiếp nhận và phân loại yêu cầu

**Mô tả**
Hệ thống cho phép nhân viên phụ trách xem danh sách yêu cầu mới gửi đến, tiếp nhận yêu cầu (claim), phân loại theo từng nhóm vấn đề và đánh giá mức độ ưu tiên để chuẩn bị cho quá trình xử lý.

**Actor**
Nhân viên phòng ban (Staff) đã đăng nhập vào hệ thống.

**Preconditions**
- Nhân viên đã đăng nhập thành công.
- Nhân viên có quyền truy cập và xử lý các Ticket thuộc phòng ban của mình.
- Tồn tại các Ticket ở trạng thái `Mới` (New) hoặc chưa được tiếp nhận.

**Luồng chính**
1. Nhân viên truy cập danh sách **Tiếp nhận yêu cầu**.
2. Hệ thống hiển thị danh sách các Ticket mới chưa có người tiếp nhận hoặc đang chờ phân loại.
3. Nhân viên chọn xem chi tiết một Ticket.
4. Nhân viên xem xét nội dung, tệp đính kèm và thực hiện thao tác **Tiếp nhận** (Claim) hoặc phân công cho bản thân/đồng nghiệp.
5. Nhân viên cập nhật **Mức độ ưu tiên** (Priority: Thấp, Trung bình, Cao, Khẩn cấp) và điều chỉnh **Nhóm vấn đề** (nếu sinh viên chọn chưa chính xác).
6. Nhân viên xác nhận lưu thông tin phân loại.
7. Hệ thống cập nhật trạng thái Ticket sang `Đang xử lý` (In Progress), ghi nhận người phụ trách (Assignee) và lưu lịch sử thao tác.
8. Hệ thống gửi thông báo nội bộ cho sinh viên về việc Ticket đã được tiếp nhận.

**Business Rules**
- Một Ticket tại một thời điểm chỉ có tối đa **một nhân viên** chịu trách nhiệm chính (Assignee).
- Khi nhân viên bấm **Tiếp nhận**, hệ thống phải khóa trạng thái tiếp nhận đối với các nhân viên khác để tránh tranh chấp (race condition).
- Việc thay đổi mức độ ưu tiên và nhóm vấn đề phải được ghi lại trong lịch sử tra soát (Audit log).

**Alternative / Error Flows**
- **Xảy ra tranh chấp tiếp nhận (Race condition):** Nếu hai nhân viên cùng bấm tiếp nhận một Ticket gần như đồng thời, hệ thống duyệt cho người nhấn trước; người nhấn sau sẽ nhận được thông báo "Ticket đã được tiếp nhận bởi nhân viên khác" và danh sách tự động cập nhật lại.
- **Thao tác thất bại do mất kết nối:** Hệ thống hiển thị thông báo lỗi và giữ nguyên trạng thái cũ của Ticket.

**Acceptance Criteria**
- **AC-01:** Nhân viên chọn **Tiếp nhận** một Ticket mới -> Hệ thống gán tài khoản nhân viên đó làm người phụ trách và chuyển trạng thái sang `Đang xử lý`.
- **AC-02:** Nhân viên cập nhật mức độ ưu tiên cho Ticket -> Hệ thống lưu giá trị ưu tiên mới và cập nhật danh sách hiển thị.
- **AC-03:** Sinh viên nhận được thông báo trong hệ thống ngay khi Ticket chuyển sang trạng thái `Đang xử lý` kèm tên nhân viên/phòng ban phụ trách.
- **AC-04:** Hai nhân viên tiếp nhận cùng 1 Ticket đồng thời -> Hệ thống chỉ ghi nhận cho 1 người và báo lỗi hợp lệ cho người còn lại.

**Ví dụ Edge Case**
Nhân viên A và Nhân viên B cùng mở chi tiết Ticket #TK-1002 và nhấn nút **Tiếp nhận** cách nhau 0.2 giây.

**Expected Result:** Hệ thống phân công Ticket #TK-1002 cho Nhân viên A. Nhân viên B nhận thông báo "Ticket này đã được Nhân viên A tiếp nhận trước đó" và giao diện hiển thị thông tin cập nhật mới nhất.