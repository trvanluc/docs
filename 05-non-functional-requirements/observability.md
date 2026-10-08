# Yêu Cầu Về Ghi Vết & Giám Sát (Observability Requirements)

## 1. Ghi Nhận Lỗi Hệ Thống (System Error Logging)
* **Error Log:** Hệ thống Backend bắt buộc phải tự động ghi nhận nhật ký lỗi chi tiết (System Error Logs) vào file log hoặc CSDL khi xảy ra các ngoại lệ (Exceptions, lỗi 500, lỗi kết nối CSDL).
* **Cấu trúc bản ghi Lỗi:** Một bản ghi lỗi bắt buộc gồm: **Timestamp**, **Error Level** (INFO, WARN, ERROR), **Module/API**, **ErrorMessage** và **StackTrace**.

---

## 2. Nhật Ký Thao Tác Người Dùng (Audit Logging)
* **Nhật ký thao tác cơ bản:** Lưu trữ thông tin tra soát các hành động quan trọng trên hệ thống:
  * Đăng nhập / Đăng xuất hệ thống.
  * Khởi tạo Ticket, chuyển phòng ban thụ lý, đóng Ticket.
  * Tạo mới, chỉnh sửa thông tin hoặc phân quyền tài khoản.
* **Trường dữ liệu Audit:** Mỗi bản ghi Audit log bao gồm: `user_id`, `action`, `target_object_id`, `ip_address`, `timestamp`.
* **Phạm vi Audit log (Non-Goal):** Không triển khai hệ thống ghi log thao tác nâng cao ở cấp độ sâu chi tiết mọi sự kiện truy vấn dữ liệu.