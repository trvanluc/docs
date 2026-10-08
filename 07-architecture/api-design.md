# Thiết Kế RESTful API (API Design)

Danh mục các API Endpoints cốt lõi của hệ thống UniSupport, sử dụng chuẩn dữ liệu JSON truyền nhận qua HTTPS:

---

## 1. Phân Hệ Xác Thực (`/api/v1/auth`)
* `POST /api/v1/auth/login`: Đăng nhập hệ thống, trả về Token xác thực và Vai trò (`Role`).
* `POST /api/v1/auth/logout`: Đăng xuất và hủy phiên làm việc.

---

## 2. Phân Hệ Sinh Viên (`/api/v1/student`)
* `POST /api/v1/student/tickets`: Tạo mới Ticket hỗ trợ (FormData chứa file đính kèm).
* `GET /api/v1/student/tickets`: Lấy danh sách Ticket cá nhân của sinh viên.
* `GET /api/v1/student/tickets/{ticket_id}`: Xem chi tiết trạng thái và lịch sử xử lý Ticket.
* `POST /api/v1/student/tickets/{ticket_id}/supplement`: Upload bổ sung tài liệu khi có yêu cầu (`NEED_MORE_INFO`).
* `POST /api/v1/student/tickets/{ticket_id}/rating`: Gửi đánh giá sao và nhận xét cho Ticket đã đóng (`CLOSED`).

---

## 3. Phân Hệ Nhân Viên (`/api/v1/staff`)
* `GET /api/v1/staff/tickets`: Lấy danh sách Ticket thuộc phòng ban / gán cho nhân viên.
* `PUT /api/v1/staff/tickets/{ticket_id}/claim`: Tiếp nhận xử lý Ticket và gán mức độ ưu tiên.
* `PUT /api/v1/staff/tickets/{ticket_id}/transfer`: Chuyển tiếp Ticket sang phòng ban khác.
* `PUT /api/v1/staff/tickets/{ticket_id}/request-more-info`: Gửi yêu cầu sinh viên bổ sung thông tin.
* `PUT /api/v1/staff/tickets/{ticket_id}/close`: Nhập ghi chú kết quả giải quyết và chính thức đóng Ticket.

---

## 4. Phân Hệ Quản Lý (`/api/v1/manager`)
* `GET /api/v1/manager/dashboard/summary`: Lấy các chỉ số KPI tổng quan (Số Ticket mới, đang xử lý, quá hạn).
* `GET /api/v1/manager/reports/trends`: Lấy số liệu thống kê nhóm sự cố phổ biến.
* `GET /api/v1/manager/reports/satisfaction`: Lấy điểm số đánh giá hài lòng trung bình.
* `GET /api/v1/manager/users`: Danh sách tài khoản người dùng.
* `POST /api/v1/manager/users`: Tạo mới tài khoản và phân quyền vai trò.

---

## 5. File & Thông Báo (`/api/v1/common`)
* `GET /api/v1/attachments/{file_id}`: Stream file đính kèm (có kiểm tra quyền sở hữu `ADR-003`).
* `GET /api/v1/notifications`: Lấy danh sách thông báo in-app của người dùng.