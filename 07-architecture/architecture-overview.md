# [ARC-02] Kiến trúc tổng quan Hệ thống (Architecture Overview)

> Nguồn chuẩn hóa nhân sự & phân bổ công sức: `Phan_bo_Resources_Antigravity.md`

Tài liệu này chi tiết hóa kiến trúc tổng thể phần mềm của ứng dụng Web Application **UniSupport**, bao gồm mô hình phân lớp, kiến trúc Frontend, Backend, chiến lược quản lý dữ liệu và luồng giao tiếp dữ liệu giữa các thành phần.

---

## 1. Mô hình Kiến trúc Tổng quan (High-Level Architecture)

UniSupport được xây dựng theo mô hình **Layered Monolithic Architecture (Kiến trúc đơn khối phân lớp)** nhằm đảm bảo tính đơn giản, dễ bảo trì, tối ưu thời gian phát triển trong **14 tuần (640h kế hoạch)** và hoạt động mượt mà trên hạ tầng phục vụ **3.000 sinh viên**.

```
+-----------------------------------------------------------------------------------+
|                                 CLIENT LAYER                                      |
|   Web Browser (PC Desktop & Mobile Browsers - Responsive Web UI / VI-EN)           |
+-----------------------------------------------------------------------------------+
                              |
                              | HTTPS / REST API (JSON)
                              v
+-----------------------------------------------------------------------------------+
|                                PRESENTATION LAYER                                 |
|   - Student UI Module     - Staff UI Module      - Management Dashboard UI        |
+-----------------------------------------------------------------------------------+
                              |
                              | Internal API Calls
                              v
+-----------------------------------------------------------------------------------+
|                               APPLICATION / SERVICE LAYER                         |
|   +-------------------+  +-------------------+  +------------------------------+  |
|   | Student Service   |  | Staff Service     |  | Management & Admin Service   |  |
|   +-------------------+  +-------------------+  +------------------------------+  |
|   | Notification Svc  |  | RBAC & Auth Svc   |  | Ticket Lifecycle Engine      |  |
|   +-------------------+  +-------------------+  +------------------------------+  |
+-----------------------------------------------------------------------------------+
                              |
                              | ORM / Data Access Layer
                              v
+-----------------------------------------------------------------------------------+
|                                  DATA LAYER                                       |
|   +---------------------------------------+  +---------------------------------+  |
|   | Relational DB (PostgreSQL / MySQL)    |  | Local File Storage / Storage    |  |
|   | (Ticket, Users, Audit Log, Metrics)   |  | (Attachments: PDF, PNG, JPG)    |  |
|   +---------------------------------------+  +---------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Kiến trúc Frontend (Presentation Layer)

### 2.1 Công nghệ & Đặc điểm
* **Kiến trúc:** Single Page Application (SPA) hoặc Server-Side Rendering (SSR) tùy chọn tối ưu UI.
* **Giao diện:** Responsive Design (tương thích máy tính để bàn và thiết bị di động).
* **Đa ngôn ngữ:** Hỗ trợ Tiếng Việt (Default) và Tiếng Anh ở mức cơ bản.

### 2.2 Phân chia Phân hệ UI
1. **Student Portal (Phân hệ Sinh viên - M1):**
   * Tra cứu hướng dẫn & FAQ.
   * Form gửi Ticket đơn giản, hỗ trợ upload đính kèm (Image/PDF).
   * Màn hình tra cứu tiến độ chi tiết và khung bổ sung hồ sơ.
   * Giao diện đánh giá độ hài lòng (Rating CSAT & Feedback) sau khi hoàn thành.
2. **Staff Operations (Phân hệ Nhân viên - M2):**
   * Hòm thư Ticket theo phân loại và phòng ban.
   * Tool điều phối, tiếp nhận (Claim), chuyển phòng ban, cập nhật trạng thái và yêu cầu bổ sung thông tin.
3. **Management Dashboard (Phân hệ Quản trị & Báo cáo - M3):**
   * Báo cáo thống kê trực quan (Biểu đồ số lượng Ticket, tỷ lệ quá hạn, thời gian xử lý trung bình).
   * Giao diện quản trị tài khoản, phân quyền vai trò (RBAC) và kiểm tra Audit Log.

---

## 3. Kiến trúc Backend (Application Service Layer)

Backend của UniSupport được phân rã theo 3 phân hệ nghiệp vụ cốt lõi (17 Functions) và 2 dịch vụ kỹ thuật phụ trợ:

### 3.1 Phân hệ M01 - Student Portal Module (M1: 128h kế hoạch)
* Xử lý tra cứu FAQ/Knowledge base.
* Tạo mới Ticket, tự động sinh Mã Ticket duy nhất (theo quy tắc ADR-001).
* Quản lý thông tin hồ sơ Ticket của sinh viên.
* Cho phép đính kèm tệp và cập nhật thông tin bổ sung khi Nhân viên yêu cầu.

### 3.2 Phân hệ M02 - Staff Operations Module (M2: 197h kế hoạch)
* Cung cấp logic tiếp nhận (Claim), phân loại (Triage) và thiết lập độ ưu tiên & thời hạn SLA.
* Xử lý luồng chuyển giao phòng ban (Transfer Department) và yêu cầu bổ sung hồ sơ (tạm dừng SLA).
* Quản lý việc cập nhật trạng thái xử lý và ghi nhận kết quả cuối cùng.

### 3.3 Phân hệ M03 - Management Dashboard Module (M3: 215h kế hoạch)
* Tính toán các chỉ số đo lường hiệu năng xử lý (SLA, thời gian giải quyết trung bình).
* Tổng hợp dữ liệu thống kê theo nhóm vấn đề và báo cáo đánh giá CSAT.
* Cung cấp các API quản trị tài khoản người dùng, sơ đồ phòng ban và chính sách lưu trữ.

### 3.4 Dịch vụ kỹ thuật phụ trợ: Notification Service (M04)
* Quản lý và phát thông báo nội bộ hệ thống (In-app Notifications) cho Sinh viên và Nhân viên khi Ticket có sự thay đổi trạng thái hoặc nhận phản hồi mới (hiện thực hóa FR-STU-04).

### 3.5 Dịch vụ kỹ thuật phụ trợ: RBAC & Security Module (M05)
* Quản lý xác thực JWT / Session Token.
* Kiểm soát quyền truy cập theo vai trò (Role-Based Access Control).
* Kiểm soát an toàn tệp đính kèm: Chỉ cho phép tài khoản liên quan (Sinh viên sở hữu Ticket, Nhân viên phòng ban xử lý, Quản lý) được tải hoặc xem file.
* Ghi chép nhật ký thao tác quan trọng (Audit Logging bất biến).

---

## 4. Kiến trúc Lưu trữ & Dữ liệu (Data Layer)

### 4.1 Cơ sở dữ liệu quan hệ (Relational Database)
* Sử dụng RDBMS (PostgreSQL/MySQL) để đảm bảo tính toàn vẹn dữ liệu (ACID).
* Quản lý các thông tin: Người dùng, Phòng ban, Ticket, Lịch sử chuyển trạng thái, Đánh giá hài lòng, Audit Log.

### 4.2 Lưu trữ Tệp đính kèm (Attachment Storage)
* Tệp đính kèm (PDF, PNG, JPG) được lưu trữ tại cấu trúc thư mục bảo mật trên Server.
* Tên file được mã hóa/đổi tên ngẫu nhiên (UUID) để tránh dò quét trực tiếp.
* Không công khai URL trực tiếp (Public Storage); mọi yêu cầu xem/tải file phải đi qua API kiểm tra quyền ở Phân hệ M05.

---

## 5. Tương tác Kỹ thuật & Bảo mật cơ bản

1. **Giao tiếp API:** Tất cả truy xuất dữ liệu giữa Frontend và Backend sử dụng giao thức HTTPS với dữ liệu định dạng JSON.
2. **Bảo vệ thao tác trùng lặp:** Áp dụng cơ chế kiểm tra Request Token / Idempotency tại Backend để tránh tình trạng trùng lặp Ticket khi người dùng click liên tục hoặc gặp lỗi mạng (Retry).
3. **Mã hóa mật khẩu:** Mật khẩu người dùng được mã hóa bằng thuật toán hashing an toàn (như Bcrypt/Argon2) trước khi lưu trữ.