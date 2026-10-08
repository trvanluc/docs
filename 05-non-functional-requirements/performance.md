# Yêu Cầu Về Hiệu Năng (Performance Requirements)

## 1. Quy Mô & Sức Chịu Tải
* **Tải mục tiêu:** Hệ thống được thiết kế và tối ưu cho quy mô khoảng **3.000 sinh viên** của Aurora University cùng cán bộ nhân viên liên quan.
* **Tải đồng thời (Concurrent Users):** Hệ thống đáp ứng khoảng 100 - 150 người dùng thao tác đồng thời trong các thời điểm cao điểm (ví dụ: đợt đăng ký học phần, đợt xét tốt nghiệp).
* **Giới hạn phạm vi (Non-Goal):** Hệ thống không tối ưu và không chịu trách nhiệm cho các bài kiểm thử chịu tải lớn (Load test/Stress test) vượt quá quy mô 3.000 sinh viên.

---

## 2. Chỉ Số Thời Gian Phản Hồi (Response Time)
* **Tải trang & Giao diện:** Thời gian tải giao diện lần đầu < 2.5 giây trên kết nối mạng tiêu chuẩn.
* **Thao tác API thông thường:** Thời gian phản hồi đối với các tác vụ truy vấn dữ liệu (xem danh sách Ticket, xem chi tiết) < 1 giây.
* **Tác vụ xử lý dữ liệu (Tạo Ticket, đính kèm file):** Thời gian phản hồi < 2 giây.

---

## 3. Tối Ưu Hóa Dữ Liệu & Lưu Trữ
* **Dung lượng File:** Giới hạn dung lượng tối đa **5MB/file** đính kèm để tránh gây quá tải đường truyền và tài nguyên lưu trữ của máy chủ.
* **Phân trang dữ liệu:** Mọi danh sách (danh sách Ticket, danh sách thông báo, danh sách tài khoản) bắt buộc phải sử dụng phân trang (Pagination) với kích thước tối đa 20 - 50 bản ghi/trang.