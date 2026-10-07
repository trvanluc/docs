# [WF-06] Sinh viên nhận kết quả & Đánh giá mức độ hài lòng (Close and Rate)

### [FR-STU-05 / FR-STF-06] Sinh viên xem kết quả, đánh giá chất lượng dịch vụ (CSAT) & Đóng Ticket

**Mô tả**
Hệ thống cho phép sinh viên xem chi tiết kết quả xử lý của Ticket và gửi đánh giá mức độ hài lòng (số sao và góp ý) sau khi yêu cầu đã hoàn thành.

**Actor**
Sinh viên sở hữu Ticket (Student).

**Preconditions**
- Ticket đang ở trạng thái `Hoàn thành` (Resolved / Closed).
- Sinh viên đã đăng nhập vào hệ thống.

**Luồng chính**
1. Sinh viên nhận thông báo hoặc truy cập danh sách Ticket cá nhân, chọn Ticket đã hoàn thành.
2. Sinh viên xem nội dung kết quả giải quyết và các tệp đính kèm (nếu có) từ nhân viên.
3. Sinh viên chọn mức **Đánh giá hài lòng** (thang điểm từ 1 đến 5 sao).
4. Sinh viên nhập **Nhận xét / Góp ý** (không bắt buộc).
5. Sinh viên nhấn nút **Gửi đánh giá**.
6. Hệ thống lưu nhận xét, số sao đánh giá gắn liền với Ticket và cập nhật trạng thái đánh giá.
7. Hệ thống hiển thị thông báo cảm ơn sinh viên và khóa form đánh giá cho Ticket này.

**Business Rules**
- Mỗi Ticket chỉ được phép gửi đánh giá **duy nhất 1 lần**.
- Việc đánh giá là tự nguyện, sinh viên có thể xem kết quả mà không bắt buộc phải đánh giá ngay.
- Kết quả đánh giá được tổng hợp tự động vào Dashboard báo cáo cho Ban quản lý.

**Alternative / Error Flows**
- **Sinh viên gửi đánh giá lại cho Ticket đã đánh giá:** Hệ thống ẩn form đánh giá và chỉ hiển thị kết quả đánh giá đã gửi trước đó.
- **Mất kết nối khi gửi đánh giá:** Hệ thống hiển thị thông báo thử lại và không ghi nhận dữ liệu lỗi.

**Acceptance Criteria**
- **AC-01:** Sinh viên chọn số sao (1–5 sao), nhập nhận xét và bấm **Gửi đánh giá** -> Hệ thống lưu đánh giá thành công và hiển thị thông báo ghi nhận.
- **AC-02:** Sinh viên chọn số sao và để trống nhận xét -> Hệ thống vẫn chấp nhận và lưu đánh giá thành công.
- **AC-03:** Sau khi đã gửi đánh giá, giao diện Ticket hiển thị đánh giá cũ và không cho phép chỉnh sửa/gửi lại.
- **AC-04:** Sinh viên khác không sở hữu Ticket không thể thực hiện đánh giá (HTTP 403).

**Ví dụ Edge Case**
Sinh viên mở hai tab trình duyệt cùng lúc cho Ticket đã hoàn thành và bấm **Gửi đánh giá** trên cả hai tab.

**Expected Result:** Tab gửi đầu tiên ghi nhận đánh giá thành công. Tab thứ hai gửi sau sẽ nhận thông báo "Ticket này đã được đánh giá trước đó" và tự động làm mới lại giao diện hiển thị đánh giá cũ.