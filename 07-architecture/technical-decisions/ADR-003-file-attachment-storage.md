# [ADR-003] Phương án lưu trữ & Phân quyền xem file đính kèm (File Attachment Storage Strategy)

* **Trạng thái:** Đã phê duyệt (Accepted)
* **Ngày quyết định:** 2026-10-05
* **Người quyết định:** Infrastructure Lead / Backend Lead
* **Phân hệ liên quan:** `M01-student-portal`, `M02-staff-operations`, `05-non-functional-requirements/security.md`

---

## 1. Bối cảnh (Context)
Sinh viên và Nhân viên có nhu cầu tải lên tệp đính kèm (định dạng PDF, PNG, JPG) chứa giấy tờ cá nhân hoặc kết quả xử lý.
- Giả định hệ thống triển khai trên hạ tầng máy chủ của Client (Aurora University).
- Tệp đính kèm chứa thông tin nhạy cảm của sinh viên, **tuyệt đối không được công khai (Public URL)** để tránh truy cập trái phép.

## 2. Các phương án xem xét (Options Considered)
1. **Phương án 1: Lưu file vào thư mục `public/` của Web Server**
   - *Ưu điểm:* Dễ triển khai, trả về URL tĩnh cho Frontend dùng ngay.
   - *Nhược điểm:* Mất an toàn thông tin, ai có link cũng tải được file (Lỗ hổng Direct Access).
2. **Phương án 2: Lưu tệp trong Local Storage/NAS của Server + Truy xuất qua Proxy Stream API**
   - *Ưu điểm:* Chi phí hạ tầng $0$ (dùng trực tiếp ổ cứng máy chủ), kiểm soát phân quyền 100% qua API Backend.
   - *Nhược điểm:* Tốn băng thông Backend khi phải stream file.
3. **Phương án 3: Dùng Object Storage (S3 / MinIO) + Presigned URL**
   - *Ưu điểm:* Hiệu năng cao, bảo mật tốt, chuẩn enterprise.
   - *Nhược điểm:* Yêu cầu Client phải trang bị thêm hạ tầng S3 hoặc cài đặt MinIO, vượt ngoài giả định hạ tầng cơ bản.

## 3. Quyết định (Decision)
Lựa chọn **Phương án 2**:
- Tệp đính kèm được lưu trong thư mục riêng biệt của Server (nằm ngoài thư mục Web Public).
- Tên tệp trên đĩa được đổi thành chuỗi ngẫu nhiên (UUID) để tránh trùng tên và dò đoán file.
- **Cơ chế truy cập:**
  1. Client gọi API `GET /api/v1/attachments/{file_id}`.
  2. Backend kiểm tra quyền (User có phải chủ Ticket hoặc Nhân viên phòng ban xử lý hay không).
  3. Nếu hợp lệ, Backend đọc file và stream trực tiếp về Client (hoặc trả về chuỗi Base64 / File Blob).
  4. Nếu không có quyền, trả về lỗi `403 Forbidden`.

## 4. Hệ quả (Consequences)
* **Tích cực:** Đảm bảo an toàn tuyệt đối cho hồ sơ sinh viên, tuân thủ tiêu chí NFR-SEC-01, tương thích tốt với hạ tầng VPS/Server của nhà trường.
* **Tiêu cực:** Tăng nhẹ tải CPU/RAM của Backend Service khi đọc/ghi file.