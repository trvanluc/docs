# ADR-003: Phương Án Lưu Trữ & Phân Quyền Xem File Đính Kèm

* **Trạng thái (Status):** Accepted (Đã chấp thuận)[cite: 1]
* **Ngày quyết định:** Tuần 3 - Giai đoạn Thiết kế Kiến trúc[cite: 1]

---

## 1. Bối Cảnh (Context)
Khi tạo Ticket hoặc bổ sung hồ sơ, sinh viên và nhân viên có thể tải lên các file đính kèm minh chứng (ảnh PNG/JPG hoặc PDF, dung lượng <= 5MB)[cite: 1]. Các tài liệu này chứa thông tin cá nhân/học tập nhạy cảm của sinh viên, do đó bắt buộc phải đảm bảo an toàn, không được lộ đường dẫn công khai (Public Access)[cite: 1].

---

## 2. Các Phương Án Cân Nhắc (Options Considered)
1. **Phương án A (Public Direct Link):** Lưu file vào thư mục Web public (`/public/uploads/...`) và lưu URL trực tiếp trong CSDL.
   * *Ưu điểm:* Dễ cài đặt.
   * *Nhược điểm:* Lộ bảo mật nghiêm trọng; bất kỳ ai có đường dẫn URL đều xem/tải được file.
2. **Phương án B (Private Storage + Stream API Check - Lựa chọn):** Lưu file vào thư mục bảo vệ (Private Folder) trên server hoặc Object Storage riêng biệt. File chỉ được tải thông qua một API xác thực[cite: 1].

---

## 3. Quyết Định (Decision)
Hệ thống chốt áp dụng **Phương án B (Private Storage + Stream API Check)**[cite: 1]:

* **Lưu trữ:** File đính kèm được lưu ở thư mục bảo vệ ngoài Web Root trên Server của Aurora University[cite: 1].
* **Giới hạn định dạng & dung lượng:** Bắt buộc kiểm tra định dạng file (**PDF, PNG, JPG, JPEG**) và dung lượng tối đa **5MB/file** từ cả Client và Backend Validator[cite: 1].
* **Kiểm soát truy cập:** Người dùng nhấn xem file sẽ gọi đến API `/api/v1/attachments/{file_id}`.
* Backend kiểm tra quyền trước khi trả fileStream:
  * Cho phép: Nếu người dùng là Sinh viên sở hữu Ticket, Nhân viên thuộc phòng ban đang thụ lý Ticket, hoặc Quản lý hệ thống[cite: 1].
  * Chặn (Trả về lỗi `403 Forbidden`): Nếu là người dùng khác hoặc chưa đăng nhập[cite: 1].

---

## 4. Hệ Quả & Đánh Giá (Consequences)
* **Tích cực:** Đảm bảo bảo mật tuyệt đối cho dữ liệu cá nhân của sinh viên, ngăn chặn việc thu thập dữ liệu trái phép qua URL tĩnh[cite: 1].
* **Hạn chế:** Tạo thêm tải xử lý nhẹ cho Server Backend khi phải đọc và stream file qua API kiểm tra xác thực.