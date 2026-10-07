# [WF-05] Cập nhật kết quả & Đóng yêu cầu (Complete and Resolve)

### [FR-STF-05 / FR-STF-06] Nhân viên cập nhật kết quả giải quyết và hoàn thành Ticket

**Mô tả**
Hệ thống cho phép nhân viên phụ trách ghi nhận kết quả xử lý, tải lên các tài liệu/kết quả giải quyết (nếu có) và đóng Ticket sau khi đã hoàn thành xử lý cho sinh viên.

**Actor**
Nhân viên phụ trách Ticket (Staff).

**Preconditions**
- Ticket đang ở trạng thái `Đang xử lý` (In Progress).
- Nhân viên thực hiện là người đang trực tiếp phụ trách Ticket đó.

**Luồng chính**
1. Nhân viên truy cập chi tiết Ticket cần hoàn thành.
2. Nhân viên chọn chức năng **Hoàn thành / Giải quyết**.
3. Nhân viên nhập nội dung **Kết quả giải quyết** (bắt buộc) và đính kèm file kết quả (nếu có).
4. Nhân viên bấm chọn **Xác nhận hoàn thành**.
5. Hệ thống ghi nhận nội dung giải quyết, cập nhật trạng thái Ticket sang `Hoàn thành` (Resolved / Closed).
6. Hệ thống lưu mốc thời gian hoàn thành, tính toán thời gian xử lý thực tế phục vụ báo cáo SLA.
7. Hệ thống tự động gửi thông báo nội bộ cho sinh viên về việc Ticket đã được xử lý xong kèm kết quả giải quyết.

**Business Rules**
- Nội dung kết quả giải quyết là bắt buộc, không được để trống hoặc chỉ chứa khoảng trắng.
- Sau khi Ticket chuyển sang trạng thái `Hoàn thành`, thông tin kết quả không được phép chỉnh sửa trừ khi có quyền Quản lý (Admin/Manager).
- Lịch sử cập nhật và tệp kết quả được lưu trữ nguyên vẹn để tra soát.

**Alternative / Error Flows**
- **Để trống nội dung kết quả:** Hệ thống chặn thao tác, hiển thị thông báo "Vui lòng nhập nội dung kết quả giải quyết trước khi hoàn thành Ticket".
- **Lỗi lưu dữ liệu:** Hệ thống thông báo lỗi, giữ nguyên trạng thái `Đang xử lý` của Ticket.

**Acceptance Criteria**
- **AC-01:** Nhân viên nhập đầy đủ nội dung kết quả và xác nhận -> Hệ thống chuyển trạng thái Ticket thành `Hoàn thành`, ghi nhận mốc thời gian và gửi thông báo cho sinh viên.
- **AC-02:** Nhân viên để trống ô kết quả giải quyết -> Hệ thống hiển thị lỗi validation và dừng thao tác.
- **AC-03:** Sinh viên nhận được thông báo nội bộ ngay sau khi nhân viên bấm hoàn thành Ticket.
- **AC-04:** Nhân viên không phụ trách Ticket này tìm cách hoàn thành Ticket -> Hệ thống chặn truy cập (HTTP 403).

**Ví dụ Edge Case**
Nhân viên nhấn **Xác nhận hoàn thành** khi ô nội dung giải quyết chỉ chứa các dấu khoảng trắng "   ".

**Expected Result:** Hệ thống coi đây là nội dung không hợp lệ, không chuyển trạng thái Ticket và hiển thị lỗi validation: "Nội dung kết quả giải quyết không được để trống".