# Yêu Cầu Về Bảo Mật (Security Requirements)

## 1. Xác Thực & Phân Quyền (Authentication & Authorization)
* **Xác thực:** Người dùng bắt buộc phải đăng nhập bằng tài khoản và mật khẩu riêng trước khi sử dụng các chức năng hệ thống.
* **Phân quyền 3 vai trò (RBAC):** Kiểm soát quyền hạn chặt chẽ dựa trên 3 vai trò: Sinh viên, Nhân viên và Quản lý. Sinh viên chỉ được phép xem/thao tác trên Ticket do chính mình tạo.
* **Mã hóa mật khẩu:** Mật khẩu người dùng phải được mã hóa bằng thuật toán băm an toàn (như Bcrypt) trước khi lưu vào cơ sở dữ liệu.

---

## 2. Kiểm Soát Quyền Truy Cập File Đính Kèm
* **Private Storage:** Các file đính kèm (ảnh PNG/JPG, file PDF) tuyệt đối không được để công khai qua các đường dẫn tĩnh công cộng (Public URL).
* **Xác thực quyền xem File:** Mỗi truy vấn xem/tải file đính kèm đều phải thông qua API kiểm tra quyền truy cập: Chỉ Sinh viên tạo Ticket, Nhân viên thuộc phòng ban phụ trách và Quản lý hệ thống mới có quyền truy cập file.

---

## 3. An Toàn Dữ Liệu & Tra Soát
* **Chống tạo dữ liệu rác/trùng lặp:** Áp dụng cơ chế Idempotency/Token để chặn việc bấm nút gửi nhiều lần (double-click) hoặc gửi lại request trùng lặp.
* **Nhật ký tra soát (Audit Log):** Ghi vết các thao tác quan trọng (đăng nhập, chuyển phòng ban, đóng Ticket, thay đổi quyền) để phục vụ tra soát khi có sự cố.
* **Phạm vi bảo mật:** Không bắt buộc các chứng nhận bảo mật quốc tế chuyên sâu (như ISO 27001, PCI-DSS) hay kiểm thử thâm nhập sâu (Penetration Testing) ngoài các quy định đã thống nhất.