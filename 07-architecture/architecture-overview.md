# Kiến Trúc Tổng Quan (Architecture Overview)

## 1. Mô Hình Mẫu Kiến Trúc (Architectural Pattern)
UniSupport được thiết kế theo mô hình kiến trúc Phân tầng tiêu chuẩn (3-Tier Layered Architecture) dành cho Web Application:

```text
[ Presentation Layer ] ──> Responsive Single Page Application (SPA / Web Client)
           │
           ▼ (HTTPS / RESTful APIs)
[ Application Layer ]  ──> Backend API Server (Node.js / Java Spring / Python)
           │
           ▼
[ Data Layer ]         ──> Relational Database (PostgreSQL / MySQL) + Private File Storage
```

---

## 2. Chi Tiết Các Tầng Kỹ Thuật
### 2.1. Presentation Layer (Frontend)

- **Công nghệ:** HTML5, CSS3, JavaScript Framework (ReactJS / Vue.js) chuẩn hóa Responsive.
- **Đặc điểm:** Hoạt động linh hoạt trên cả trình duyệt máy tính và thiết bị di động. Tích hợp mô-đun chuyển đổi 2 ngôn ngữ Tiếng Việt & Tiếng Anh.

### 2.2. Application Layer (Backend)

- **Công nghệ:** RESTful API Service kết nối bảo mật HTTPS.
- **Các dịch vụ cốt lõi:**
  - **Auth & Security Service:** Xác thực người dùng, cấp Token/Session và kiểm tra quyền RBAC.
  - **Ticket Core Service:** Xử lý nghiệp vụ tạo Ticket, sinh mã Ticket duy nhất (`ADR-001`), chuyển đổi trạng thái và đóng Ticket.
  - **File Management Service:** Tiếp nhận upload, xác thực định dạng/dung lượng file (PDF/Image <= 5MB) và kiểm soát quyền truy cập file (`ADR-003`).
  - **Notification Service:** Phát thông báo nội bộ hệ thống (In-app Notification) cho người dùng.
  - **Reporting Service:** Tổng hợp số liệu Dashboard, thời gian xử lý trung bình và chỉ số hài lòng.

### 2.3. Data Layer (Database & Storage)

- **Cơ sở dữ liệu:** RDBMS (PostgreSQL hoặc MySQL) lưu trữ dữ liệu quan hệ.
- **Lưu trữ File:** Thư mục bảo vệ (Private Folder) trên Server của nhà trường, ngăn chặn truy cập trực tiếp qua Public URL (`ADR-003`).