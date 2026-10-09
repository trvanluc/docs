# ADR-003: Phương Án Lưu Trữ & Kiểm Soát Truy Cập File Đính Kèm (File Attachment Storage & Access Control)

- **Trạng thái (Status):** Accepted (Đã chấp thuận)
- **Ngày quyết định:** 2026-09-15 (Giai đoạn Thiết kế Kiến trúc)
- **Đối tượng áp dụng:** Backend Engineering Team, Infrastructure / DevOps Team, Security Audit Team

## 1. Bối Cảnh (Context)
Trong hệ thống UniSupport, Sinh viên và Nhân viên thường xuyên tải lên các file đính kèm minh chứng (Bảng điểm, đơn từ, giấy xác nhận, ảnh chụp chứng minh y tế/gia cảnh). Các tài liệu này chứa thông tin cá nhân và dữ liệu học tập nhạy cảm.

Yêu cầu kỹ thuật bắt buộc:
1. **Bảo mật tuyệt đối (Zero Public Access):** Không lưu file ở thư mục Public web root. Ngăn chặn triệt để hành vi truy cập trực tiếp qua Static URL hoặc dò quét file (URL Enumeration Attack).
2. **Kiểm soát truy cập dựa trên Quyền (Contextual Access Control):** Chỉ những người dùng liên quan trực tiếp đến Ticket mới có quyền xem/tải file.
3. **Kiểm tra An toàn File (Security Validation):** Ngăn chặn việc tải lên file độc hại (Executable files, Web shell, Script Injection) giả mạo đuôi file.
4. **Giới hạn Tài nguyên (Resource Limit):** Kiểm soát chặt chẽ dung lượng và số lượng file để tránh tấn công từ chối dịch vụ (DoS Storage).

## 2. Các Phương Án Cân Nhắc (Options Considered)
- **Phương án A: Public Static Direct Link** (Lưu thư mục Public Web Root)
  - *Ưu điểm:* Cấu hình đơn giản, Web Server (Nginx/Apache) phục vụ static file cực nhanh mà không qua Backend processing.
  - *Nhược điểm:* Lỗ hổng bảo mật nghiêm trọng. Bất kỳ ai có đường dẫn URL (kể cả người dùng chưa đăng nhập) đều xem/tải được file nhạy cảm của sinh viên.
- **Phương án B: Presigned URL** (AWS S3 / Cloud Storage - Temporary URL)
  - *Ưu điểm:* Giảm tải I/O cho Backend Server, link tự động hết hạn sau khoảng thời gian ngắn (ví dụ: 15 phút).
  - *Nhược điểm:* Đòi hỏi tích hợp Cloud Storage ngoài; nếu mô hình triển khai của Aurora University sử dụng hạ tầng Server nội bộ (On-Premise) thì không áp dụng được.
- **Phương án C: Private Storage + Authenticated Stream API / Signed Proxy Path** (Được chọn)
  - *Ưu điểm:* Đảm bảo 100% file lưu ở thư mục bảo vệ cách ly hoàn toàn với Web Root. Mọi request truy cập file đều bắt buộc phải qua bước kiểm tra Token và Phân quyền context của Ticket.
  - *Nhược điểm:* Phát sinh I/O và CPU load nhẹ trên Backend Server khi kiểm tra quyền và stream dữ liệu file.

## 3. Quy Định Kỹ Thuật Chi Tiết (Detailed Specifications)

### 3.1. Quy Định Validation File Đính Kèm (File Validation Rules)
Mọi file tải lên (khi Tạo Ticket, Bổ sung hồ sơ, hay Gửi kết quả) đều phải trải qua 2 lớp kiểm tra (Two-tier Validation):

| Tiêu chí kiểm tra | Quy định Validation Phía Client | Quy định Validation Phía Server (Bắt buộc) |
| :--- | :--- | :--- |
| **Số lượng File** | Maximum 5 file / 1 lần request. | Block ngay nếu `files.length > 5`. Trả mã lỗi `400 FILE_COUNT_EXCEEDED`. |
| **Dung lượng File** | Maximum 5MB ($5.242.880\text{ Bytes}$) / 1 file. | Kiểm tra `file.size <= 5242880`. Trả mã lỗi `400 FILE_EXCEEDS_LIMIT`. |
| **Định dạng Mở rộng** | Chỉ cho phép chọn: `.pdf`, `.png`, `.jpg`, `.jpeg`. | Kiểm tra File Extension (Case-insensitive). |
| **MIME Type Thực tế** | Kiểm tra `file.type` từ Browser Input. | Đọc Magic Bytes (Binary Header) của file trên Server để xác thực MIME Type thực tế:<br>- PDF: `application/pdf` (`%PDF`)<br>- PNG: `image/png` (`\x89PNG`)<br>- JPEG/JPG: `image/jpeg` (`\xFF\D8\xFF`)<br>Chống hoàn toàn việc đổi đuôi `.exe` / `.php` thành `.pdf`. |
| **Đổi tên File (Sanitization)** | Giữ nguyên tên gốc hiển thị cho user (`file_name`). | Tự động đổi tên file khi lưu đĩa cứng sang chuỗi UUID v4 ngẫu nhiên để tránh đè file và chặn Path Traversal (`../../`):<br>`stored_filename = {uuid_v4}.{ext}` (VD: `e3b0c442-98fc-11ee-b9d1-0242ac120002.pdf`). |

### 3.2. Cấu Trúc Lưu Trữ (Directory Structure)
File đính kèm được lưu trữ tại thư mục cách ly ngoài Web Root trên Server nội bộ:  
`/var/app/data/attachments/YYYY/MM/DD/{stored_filename}`

### 3.3. Quy Trình Phân Quyền Xem File (Access Control Matrix & Streaming Mechanism)
Khi người dùng click vào link xem/tải file: `GET /api/v1/attachments/{file_id}`

```plaintext
[Client Request] ──(Header: Bearer Token)──> [API Gateway / Backend]
                                                    │
1. Verify JWT Token
                                                    │
2. Query Ticket Owner & Assignee
                                                    │
                                      ┌─────────────┴─────────────┐
                               [CÓ QUYỀN]                     [KHÔNG QUYỀN]
                                    │                               │
3. Read File Chunk & Stream            HTTP 403 Forbidden
                        `Content-Type` matching             `FORBIDDEN_ACCESS`
```
- Ma trận Phân quyền Truy cập File (Access Authorization Matrix):
---
| Vai trò / Tác nhân | Điều kiện được phép tải / xem File (`HTTP 200 OK`) |
| :--- | :--- |
| **Sinh viên (STUDENT)** | Đúng là Chủ sở hữu của Ticket chứa file đó (`student_id == ticket.student_id`). |
| **Nhân viên (STAFF)** | Thuộc Phòng ban đang thụ lý Ticket (`department_id == ticket.department_id`) HOẶC là Người trực tiếp xử lý (`assignee_id == ticket.assignee_id`). |
| **Quản lý / Admin (MANAGER / ADMIN)** | Được phép xem toàn bộ file trong hệ thống để phục vụ giám sát và kiểm tra chất lượng. |
| **Khác (Guest / Staff PB khác)** | Bị chặn hoàn toàn. Hệ thống trả về `HTTP 403 Forbidden`. |
---

## 4. Hệ Quả & Đánh Giá Kỹ Thuật (Consequences)

### Tích cực (Positive)
- **An toàn Bảo mật:** Loại bỏ 100% nguy cơ lộ thông tin cá nhân qua Static URL. Không ai có thể tải file nếu không có Token hợp lệ và không thuộc context của Ticket.
- **Chống Độc hại:** Việc kiểm tra Binary Magic Bytes chặn đứng nguy cơ Upload Malware/Webshell lên Server.
- **Toàn vẹn Dữ liệu:** Đổi tên file sang UUID v4 giúp loại bỏ lỗi trùng tên file, lỗi ký tự tiếng Việt có dấu hoặc ký tự đặc biệt gây hỏng đường dẫn storage.

### Ràng buộc & Tối ưu Hiệu năng (Performance Optimization Specs)
- **Tối ưu Server I/O Stream:** Backend **KHÔNG ĐƯỢC** đọc toàn bộ file 5MB vào RAM (`readFileSync`). Bắt buộc sử dụng Stream / Chunked Transfer Encoding (`createReadStream`) để truyền dữ liệu file về Client, giúp tiết kiệm RAM Backend Server.
- **Cấu hình Caching Control phía Client:** Trả về Header `Cache-Control: private, max-age=3600` để Trình duyệt của người dùng có quyền lưu cache tạm trong 1 giờ cho chính phiên làm việc đó, tránh việc gọi re-fetch API liên tục khi xem lại ảnh/PDF nhiều lần.

## 5. Ràng Buộc Validation & Mã Lỗi Hệ Thống (Error Codes)

| Ràng buộc / Tình huống | Mã lỗi HTTP & Error Code | Message hiển thị cho người dùng |
| :--- | :--- | :--- |
| **File quá dung lượng (> 5MB)** | `400 Bad Request`<br><br>`FILE_EXCEEDS_LIMIT` | "File [Tên_File] vượt quá dung lượng 5MB cho phép." |
| **Số lượng vượt quá 5 file** | `400 Bad Request`<br><br>`FILE_COUNT_EXCEEDED` | "Chỉ được tải lên tối đa 5 file đính kèm trong một lần gửi." |
| **Sai Magic Bytes / Giả mạo đuôi file** | `400 Bad Request`<br><br>`FILE_TYPE_NOT_ALLOWED` | "File không đúng định dạng cho phép (.pdf, .png, .jpg, .jpeg)." |
| **Không có Token xác thực** | `401 Unauthorized`<br><br>`UNAUTHORIZED` | "Phiên đăng nhập hết hạn. Vui lòng đăng nhập lại để xem file." |
| **Không có quyền truy cập file** | `403 Forbidden`<br><br>`FORBIDDEN_ACCESS` | "Bạn không có quyền xem tài liệu đính kèm này." |
| **File bị xóa hoặc không tìm thấy** | `404 Not Found`<br><br>`ATTACHMENT_NOT_FOUND` | "Tài liệu đính kèm không tồn tại trên hệ thống." |