# Kịch bản nghiệm thu theo PRD đã chốt

Phạm vi: 14 FR trong M01–M03; 17 dòng Resources là công sức, không phải 17 FR. Các ca dưới đây là kịch bản dự kiến, **chưa phải kết quả chạy thử hoặc chứng nhận Pass**. Chi tiết giới hạn, lỗi và hiệu năng vẫn lấy từ Acceptance Criteria của từng FR. Không cộng estimate QA/UAT ngoài Resources.

## [TS-STU-01] FR-STU-01 — Đăng nhập tài khoản sinh viên

- **Điều kiện:** ADMIN đã cấp tài khoản Student hoạt động.
- **Thao tác:** Đăng nhập bằng tài khoản hợp lệ; thử sai mật khẩu hoặc tài khoản khóa.
- **Kết quả mong đợi:** Vào danh sách Ticket cá nhân khi hợp lệ; bị từ chối với thông báo khi không hợp lệ.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STU-02] FR-STU-02 — Gửi yêu cầu hỗ trợ (Tạo Ticket)

- **Điều kiện:** Student đã đăng nhập, danh mục nhóm vấn đề đã có.
- **Thao tác:** Chọn một nhóm vấn đề, tiêu đề 10–150 và mô tả 20–2000; chọn PDF/PNG/JPG/JPEG ≤5MB; gửi.
- **Kết quả mong đợi:** Tạo đúng một Ticket NEW ở phòng ban mặc định, hiển thị mã duy nhất. Thiếu trường, tệp >5MB, sai loại hoặc quá 5 tệp bị từ chối; bấm nhiều lần không tạo trùng.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STU-03] FR-STU-03 — Theo dõi tiến độ & Bổ sung thông tin/giấy tờ

- **Điều kiện:** Có Ticket của Student; khi bổ sung phải NEED_MORE_INFO.
- **Thao tác:** Xem danh sách/chi tiết; đọc yêu cầu bổ sung từ Staff rồi gửi tệp/lời nhắn đúng giới hạn.
- **Kết quả mong đợi:** Chỉ xem Ticket của mình; bổ sung trên cùng mã Ticket và quay lại IN_PROGRESS. Không sửa nội dung gốc; không được gửi bổ sung sai trạng thái.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STU-04] FR-STU-04 — Xem kết quả giải quyết & Đánh giá mức độ hài lòng

- **Điều kiện:** Ticket của Student ở RESOLVED/CLOSED.
- **Thao tác:** Xem kết quả; chọn 1–5 sao và nhận xét tối đa 500 ký tự nếu muốn; gửi.
- **Kết quả mong đợi:** Kết quả, tệp và thời gian hoàn thành đúng; lưu đánh giá một lần, dạng chỉ đọc sau gửi. RESOLVED sang CLOSED; không mở lại xử lý. Lỗi mạng giữ nội dung để thử lại.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-01] FR-STF-01 — Nhân viên đăng nhập hệ thống

- **Điều kiện:** ADMIN đã cấp tài khoản STAFF và gán phòng ban.
- **Thao tác:** Đăng nhập hợp lệ; thử tài khoản Student ở cổng Staff.
- **Kết quả mong đợi:** Staff vào đúng Queue phòng ban; sai vai trò bị từ chối. Không cấp thêm quyền tạo tài khoản hoặc Assign đồng nghiệp cho Staff.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-02] FR-STF-02 — Tiếp nhận và phân loại yêu cầu (Claim & Triage)

- **Điều kiện:** Ticket NEW/TRANSFERRED thuộc phòng ban Staff.
- **Thao tác:** Đọc nội dung; chọn nhóm vấn đề và mức ưu tiên nếu cần; tiếp nhận; thử hai Staff cùng tiếp nhận.
- **Kết quả mong đợi:** Một người được giao phụ trách, Ticket IN_PROGRESS; người đến sau nhận thông báo và dữ liệu cập nhật. Không nghiệm thu tự đổi thời hạn SLA chỉ do đổi priority.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-03] FR-STF-03 — Chuyển yêu cầu sang đúng phòng ban

- **Điều kiện:** Ticket thuộc quyền thao tác và trạng thái theo FR-STF-03.
- **Thao tác:** Chọn phòng ban khác, lý do 10–500 ký tự, xác nhận chuyển.
- **Kết quả mong đợi:** Ticket TRANSFERRED trong Queue phòng ban mới, bỏ phụ trách cũ và giữ lịch sử/tệp. Lý do trống/toàn khoảng trắng hoặc cùng phòng ban bị từ chối.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-04] FR-STF-04 — Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement)

- **Điều kiện:** Nhân viên đang phụ trách Ticket IN_PROGRESS.
- **Thao tác:** Nhập yêu cầu bổ sung 10–1000 ký tự rồi gửi; Student mở cùng Ticket.
- **Kết quả mong đợi:** Ticket NEED_MORE_INFO; Student thấy đúng nội dung và nhận thông báo theo phạm vi có sẵn. Không có phép đo nghiệm thu mới về tạm dừng SLA.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-05] FR-STF-05 — Ghi kết quả và hoàn tất xử lý yêu cầu

- **Điều kiện:** Nhân viên phụ trách Ticket IN_PROGRESS.
- **Thao tác:** Nhập kết quả 20–2000 ký tự; tệp tùy chọn tối đa 3 tệp, 5MB/tệp; xác nhận hoàn tất.
- **Kết quả mong đợi:** Ticket RESOLVED, ghi thời gian và sinh viên xem được kết quả. Kết quả trống/quá ngắn bị từ chối; lỗi upload giữ form. Nhãn giải quyết/đóng khớp trạng thái thật.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-01] FR-MNG-01 — Quản lý đăng nhập & Xác thực phân quyền

- **Điều kiện:** Tài khoản MANAGER/ADMIN hoạt động.
- **Thao tác:** Đăng nhập từng vai trò; thử Student/Staff vào cổng quản trị.
- **Kết quả mong đợi:** MANAGER chỉ dữ liệu phòng ban; ADMIN dữ liệu toàn trường; vai trò không phù hợp bị từ chối.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-02] FR-MNG-02 — Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision)

- **Điều kiện:** Có dữ liệu Ticket trong kỳ và phạm vi được phép.
- **Thao tác:** Xem các thẻ, workload, cảnh báo; đổi kỳ và mở thẻ quá hạn.
- **Kết quả mong đợi:** Số liệu/danh sách đúng trạng thái và phạm vi, theo SLA hiện có; làm mới theo AC gốc. Không nghiệm thu luồng Escalation hoặc deadline mới.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-03] FR-MNG-03 — Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export)

- **Điều kiện:** Có dữ liệu báo cáo/đánh giá và vai trò phù hợp.
- **Thao tác:** Chọn Xu hướng/Hiệu năng/CSAT, bộ lọc; xuất Excel/CSV; thử không có dữ liệu hoặc >10.000 dòng.
- **Kết quả mong đợi:** Báo cáo và file đúng bộ lọc/quyền; CSAT dùng đánh giá đã gửi. Không dữ liệu vô hiệu hóa xuất; vượt giới hạn báo thu hẹp kỳ. Font/ngày tháng theo AC gốc.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-04] FR-MNG-04 — Quản trị người dùng & Phân quyền (User Management & RBAC)

- **Điều kiện:** ADMIN đã đăng nhập.
- **Thao tác:** Cấp tài khoản Student/Staff, gán vai trò/phòng ban theo yêu cầu; khóa/mở khóa; thử trùng email hoặc tự khóa.
- **Kết quả mong đợi:** Đăng nhập đúng cổng và scope; khóa/mở theo phiên hiện có. Trùng thông tin/tự khóa bị từ chối; MANAGER không được quản trị tài khoản. Không yêu cầu import Excel hay gửi mật khẩu tự động.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-05] FR-MNG-05 — Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail)

- **Điều kiện:** Có thao tác quản trị và Ticket/tệp thuộc người khác.
- **Thao tác:** ADMIN xem nhật ký; người không có quyền thử mở tệp; kiểm tra giao diện log.
- **Kết quả mong đợi:** Nhật ký ghi đúng các thao tác hiện có, chỉ đọc; truy cập tệp ngoài quyền bị từ chối. Không thử UI dọn dẹp/archiving chưa được chốt.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## Các dòng công sức chưa đủ đặc tả để coi là ca nghiệm thu mới

FAQ, mở lại xử lý, Escalation nhiều cấp và màn hình quản lý lưu trữ chưa có FR nghiệp vụ được chốt. Giữ giờ nguồn nhưng không đặt ca kiểm thử mới chứng minh đã có những chức năng này. Thông báo và phân quyền được kiểm tra trong luồng FR hiện có; không cộng mã FR-NTF/FR-SEC hoặc cộng giờ lần thứ hai.
