# [WF-04] Chuyển tiếp yêu cầu sang phòng ban khác (Transfer Department)

### [FR-STF-02] Chuyển tiếp Ticket giữa các phòng ban

**Mô tả**
Hệ thống cho phép nhân viên chuyển tiếp Ticket sang đúng phòng ban hoặc người phụ trách khác nếu nội dung yêu cầu thuộc phạm vi giải quyết của đơn vị đó.

**Actor**
Nhân viên đang phụ trách Ticket (Staff).

**Preconditions**
- Ticket đang ở trạng thái `Mới` hoặc `Đang xử lý`.
- Nhân viên thực hiện có quyền xử lý Ticket hiện tại.

**Luồng chính**
1. Nhân viên mở chi tiết Ticket và chọn chức năng **Chuyển phòng ban**.
2. Hệ thống hiển thị danh sách các phòng ban chuyên trách tại Aurora University (VD: Phòng Đào tạo, Phòng Công tác sinh viên, Phòng Tài chính - Kế toán,...).
3. Nhân viên chọn **Phòng ban đích** và nhập **Lý do chuyển tiếp** (bắt buộc).
4. Nhân viên chọn **Xác nhận chuyển**.
5. Hệ thống cập nhật phòng ban phụ trách mới cho Ticket, hủy bỏ gán cá nhân phụ trách cũ, và chuyển trạng thái Ticket về `Mới` (hoặc `Đã chuyển tiếp`).
6. Hệ thống lưu lại lịch sử chuyển tiếp (phòng ban cũ, phòng ban mới, lý do, người chuyển, thời gian).
7. Hệ thống gửi thông báo nội bộ đến nhân viên/quản lý của phòng ban mới.

**Business Rules**
- Lý do chuyển tiếp là thông tin bắt buộc nhằm đảm bảo minh bạch nghiệp vụ.
- Không cho phép chuyển tiếp Ticket về chính phòng ban hiện tại.
- Mọi tài liệu đính kèm, lịch sử trao đổi trước đó của Ticket phải được giữ nguyên vẹn khi chuyển sang phòng ban mới.
- Nhân viên ở phòng ban cũ sau khi chuyển đi sẽ chuyển sang chế độ chỉ xem (Read-only) đối với Ticket đó, trừ khi được phân quyền quản trị.

**Alternative / Error Flows**
- **Không nhập lý do chuyển:** Hệ thống chặn thao tác và báo lỗi "Lý do chuyển tiếp không được để trống".
- **Chọn phòng ban đích trùng với phòng ban hiện tại:** Hệ thống hiển thị cảnh báo và không cho phép thực hiện.

**Acceptance Criteria**
- **AC-01:** Nhân viên chọn phòng ban mới và nhập lý do chuyển đầy đủ -> Hệ thống cập nhật đơn vị phụ trách mới thành công, ghi log lịch sử.
- **AC-02:** Nhân viên không nhập lý do chuyển -> Hệ thống hiển thị báo lỗi validation và dừng thao tác.
- **AC-03:** Ticket sau khi chuyển xuất hiện trong danh sách tiếp nhận của phòng ban mới.
- **AC-04:** Nhân viên phòng ban cũ không thể chỉnh sửa hay cập nhật trạng thái của Ticket sau khi đã chuyển thành công.

**Ví dụ Edge Case**
Nhân viên chọn phòng ban đích là "Phòng Tài chính" nhưng để trống ô "Lý do chuyển tiếp" rồi nhấn nút **Xác nhận chuyển**.

**Expected Result:** Hệ thống không thực hiện chuyển phòng ban, hiển thị thông báo lỗi màu đỏ ngay dưới trường Lý do chuyển: "Vui lòng nhập lý do chuyển tiếp yêu cầu" và giữ nguyên đơn vị xử lý hiện tại.