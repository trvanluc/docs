# [ARC-05] Thiết kế Bảo mật & Phân quyền (Security & RBAC Design)

Tài liệu này chi tiết hóa kiến trúc bảo mật của hệ thống **UniSupport**, mô hình phân quyền dựa trên vai trò (Role-Based Access Control - RBAC), cơ chế mã hóa và phương án bảo vệ tài nguyên tệp đính kèm.

---

## 🔒 1. Cơ chế Xác thực & Quản lý Phiên (Authentication & Session)

1. **Phương thức xác thực:**
   * Hệ thống áp dụng cơ chế xác thực **JSON Web Token (JWT)** Stateless hoặc **Session Token**.
   * Khi đăng nhập thành công qua `/api/v1/auth/login`, Backend trả về `AccessToken` kèm thời gian hết hạn (Expiration Time).
2. **Quản lý Token:**
   * Token được gửi kèm trong HTTP Header của mỗi request dưới dạng: `Authorization: Bearer <JWT_TOKEN>`.
   * Mật khẩu lưu trữ trong Cơ sở dữ liệu bắt buộc phải mã hóa bằng thuật toán băm an toàn **Bcrypt** (với Salt Factor >= 10).

---

## 👥 2. Ma trận Phân quyền Vai trò (RBAC Matrix)

Hệ thống UniSupport định nghĩa **3 Vai trò chính (Roles)** với phạm vi quyền thao tác rõ ràng:

| Phân hệ / Chức năng | Sinh viên (`STUDENT`) | Nhân viên (`STAFF`) | Quản lý (`MANAGEMENT`) |
| :--- | :---: | :---: | :---: |
| **Đăng nhập hệ thống** |  |  |  |
| **Gửi Ticket & Up file** |  (Chỉ của mình) | ❌ | ❌ |
| **Xem danh sách Ticket** |  (Chỉ của mình) |  (Thuộc Phòng ban) |  (Toàn trường) |
| **Tiếp nhận / Phân loại** | ❌ |  |  |
| **Chuyển phòng ban** | ❌ |  |  |
| **Yêu cầu bổ sung hồ sơ** | ❌ |  | ❌ |
| **Cập nhật kết quả / Đóng**| ❌ |  | ❌ |
| **Đánh giá hài lòng** |  (Ticket của mình) | ❌ | ❌ |
| **Xem Dashboard Báo cáo** | ❌ | ❌ |  |
| **Quản trị Tài khoản/Quyền**| ❌ | ❌ |  |

---

## 📎 3. Bảo mật Tệp đính kèm (File Attachment Security)

Tệp đính kèm (Ảnh/PDF) do sinh viên gửi chứa các thông tin cá nhân và giấy tờ quan trọng. Hệ thống thực hiện phương án bảo mật 3 lớp:

1. **Lưu trữ An toàn (Static Storage Isolation):**
   * Tệp đính kèm không lưu trong thư mục Web công khai (`public/`).
   * Tên tệp được mã hóa ngẫu nhiên bằng **UUIDv4** khi ghi vào đĩa đĩa để tránh dò tìm tệp (Directory Traversal attack).
2. **Kiểm tra Quyền xem tệp (Access Control Middleware):**
   * Mọi yêu cầu xem/tải tệp đính kèm phải thông qua API Proxy: `GET /api/v1/attachments/{file_id}`.
   * Middleware sẽ verify JWT Token và kiểm tra người dùng có quyền truy cập:
     * **Sinh viên:** Chỉ xem được tệp thuộc Ticket do chính mình tạo.
     * **Nhân viên:** Chỉ xem được tệp thuộc Ticket gán cho phòng ban của mình.
     * **Quản lý:** Có quyền xem tra soát toàn bộ.
3. **Validate Định dạng & Dung lượng (Input Sanitization):**
   * Chỉ chấp nhận các định dạng MIME allowed: `image/png`, `image/jpeg`, `application/pdf`.
   * Chặn hoàn toàn các file thực thi (`.exe`, `.php`, `.js`, `.sh`...).
   * Giới hạn dung lượng tối đa 5MB/file (hoặc theo cấu hình thống nhất).

---

## 📜 4. Nhật ký Tra soát (Audit Logging)

Để phục vụ công tác tra soát khi có khiếu nại hoặc sự cố bảo mật, hệ thống ghi chép **Audit Log** cơ bản đối với các thao tác quan trọng vào bảng `audit_logs`:
* **Các sự kiện được Log:** Đăng nhập thất bại/thành công, Chuyển tiếp phòng ban, Xóa/Khóa tài khoản, Thay đổi quyền hạn.
* **Thông tin ghi nhận:** `User_ID`, `IP_Address`, `Action_Type`, `Timestamp`, `Old_Value`, `New_Value`.