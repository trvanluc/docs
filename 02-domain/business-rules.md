# Quy Tắc Nghiệp Vụ Bắt Buộc (Business Rules)

Dưới đây là các quy tắc nghiệp vụ cốt lõi bắt buộc hệ thống UniSupport phải tuân thủ nghiêm ngặt[cite: 1]:

---

## 1. Quy Tắc Khởi Tạo & Trùng Lặp Ticket
* **BR-01 (Bắt buộc thông tin):** Trường **Mô tả vấn đề** và **Nhóm vấn đề** là bắt buộc khi sinh viên tạo Ticket[cite: 1].
* **BR-02 (Tính hợp lệ của nội dung):** Nội dung mô tả chỉ chứa khoảng trắng được tính là không hợp lệ; hệ thống phải báo lỗi validation[cite: 1].
* **BR-03 (Chống trùng lặp do thao tác):** Một thao tác gửi của sinh viên chỉ được tạo tối đa **01 Ticket duy nhất**, kể cả khi nhấn nút gửi nhiều lần liên tiếp (double-click), ấn retry hoặc do nghẽn mạng[cite: 1].
* **BR-04 (Ràng buộc quyền sở hữu):** Ticket sau khi tạo phải được liên kết cố định với tài khoản sinh viên đã đăng nhập gửi yêu cầu[cite: 1].

---

## 2. Quy Tắc Xử Lý & Chuyển Tiếp Phòng Ban
* **BR-05 (Chuyển phòng ban):** Nhân viên chỉ được chuyển Ticket sang phòng ban khác khi Ticket chưa ở trạng thái hoàn thành (`CLOSED`)[cite: 1]. Mọi lần chuyển tiếp phải ghi vết lịch sử.
* **BR-06 (Yêu cầu bổ sung):** Khi Ticket chuyển sang `NEED_MORE_INFO`, hệ thống chỉ cho phép sinh viên đính kèm thêm file hoặc gửi lời nhắn bổ sung; không được sửa tiêu đề hay nhóm vấn đề ban đầu[cite: 1].
* **BR-07 (Đóng Ticket):** Bắt buộc nhân viên phải nhập **Ghi chú kết quả giải quyết** (`resolution_note`) trước khi xác nhận đóng Ticket (`CLOSED`)[cite: 1].

---

## 3. Quy Tắc Phân Quyền Access & File
* **BR-08 (Bảo mật file đính kèm):** File đính kèm (ảnh/PDF) của Ticket chỉ được phép xem/tải bởi: Sinh viên tạo Ticket đó, Nhân viên thuộc phòng ban đang thụ lý và Quản lý hệ thống[cite: 1].
* **BR-09 (Giới hạn loại File):** Hệ thống chỉ chấp nhận file định dạng **PDF** hoặc hình ảnh (**PNG, JPG, JPEG**), dung lượng tối đa **5MB/file**[cite: 1].
* **BR-10 (Đánh giá mức độ hài lòng):** Sinh viên chỉ được đánh giá 01 lần duy nhất cho mỗi Ticket đã hoàn tất (`CLOSED`)[cite: 1].