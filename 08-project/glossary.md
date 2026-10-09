# Thuật Ngữ & Giải Thích Khái Niệm Dự Án (Project Glossary & Technical Terms)

## 1. Mục Tiêu Chuẩn Hóa
Tài liệu Project Glossary đóng vai trò là từ điển thuật ngữ thống nhất (Single Source of Truth - SSOT) cho toàn bộ dự án UniSupport tại Aurora University. Việc chuẩn hóa danh mục từ khóa này giúp toàn bộ các bên liên quan (Chủ đầu tư, Ban Quản lý Dự án, Business Analyst, Tech Lead, Lập trình viên Backend/Frontend, QA/Tester và Đội ngũ Vận hành) sử dụng chung một ngôn ngữ kỹ thuật, tránh hiểu nhầm nghiệp vụ trong quá trình phát triển, kiểm thử UAT và bàn giao.

## 2. Bảng Danh Mục Thuật Ngữ Kỹ Thuật & Quản Lý Dự Án

| Thuật Ngữ | Tên Đầy Đủ / Khái Niệm | Giải Thích Kỹ Thuật Chi Tiết & Phạm Vi Áp Dụng |
| :--- | :--- | :--- |
| **UniSupport** | University Support Platform | Hệ thống phần mềm Web Application quản lý, điều phối và giải quyết các yêu cầu hỗ trợ sinh viên tại Aurora University, triển khai trong **14 tuần** với ngân sách **300 triệu VNĐ**. |
| **Ticket** | Support Ticket / Phiếu hỗ trợ | Đơn vị dữ liệu cốt lõi (Core Entity) đại diện cho 01 yêu cầu hỗ trợ do Sinh viên gửi. Chứa thông tin mô tả, trạng thái FSM, file đính kèm, lịch sử trao đổi và đánh giá CSAT. |
| **Ticket ID** | Ticket Identifier | Mã định danh duy nhất của Ticket có dạng `TK-YYYYMMDD-XXXX` (VD: `TK-20261009-0001`), độ dài **15 ký tự**, sinh tự động qua Redis Atomic Counter và là duy nhất trên toàn hệ thống. |
| **RBAC** | Role-Based Access Control | Cơ chế kiểm soát truy cập phân quyền tĩnh với 4 Vai trò: `STUDENT`, `STAFF`, `MANAGER`, `ADMIN` (ADR-002). Xác thực qua JWT và Middleware phân quyền theo Data Scope. |
| **FSM** | Finite State Machine | Máy trạng thái hữu hạn quản lý 6 trạng thái vòng đời Ticket: `NEW`, `IN_PROGRESS`, `NEED_MORE_INFO`, `TRANSFERRED`, `RESOLVED`, `CLOSED` (Cùng trạng thái terminal `REJECTED`). |
| **SLA** | Service Level Agreement | Cam kết thời gian giải quyết Ticket tối đa **24 giờ làm việc** (Chỉ tính từ 08:00 đến 17:00 từ Thứ 2 đến Thứ 6). Quản lý qua 3 trạng thái chỉ báo: `ON_TRACK`, `WARNING`, `BREACHED`. |
| **CSAT** | Customer Satisfaction Score | Điểm số đánh giá mức độ hài lòng của Sinh viên sau khi Ticket được giải quyết, tính theo thang điểm **1–5 sao** kèm nhận xét tùy chọn. |
| **Idempotency Key** | Client Request Identifier | Mã UUID v4 ngẫu nhiên gửi trong Request Header `X-Client-Request-ID` khi bấm gửi Ticket nhằm chống tạo trùng dữ liệu do mạng gián đoạn hoặc click đúp. |
| **Zero Public Access** | Private File Storage Policy | Kiến trúc bảo mật lưu trữ file đính kèm ngoài Web Root (`/var/app/data/attachments/`). File chỉ được truy cập qua API Check Authentication & Stream Binary Chunk. |
| **Audit Trail** | Audit Logging | Bảng nhật ký ghi vết tự động (`audit_logs`) dạng Append-Only, lưu vĩnh viễn các thao tác quản trị nhạy cảm (Đăng nhập, Phân quyền, Khóa tài khoản, Chuyển phòng ban). |
| **JWT** | JSON Web Token | Mã định danh xác thực Stateless sử dụng thuật toán HMAC-SHA256 (HS256). Access Token có hiệu lực **15 phút**, Refresh Token lưu Cookie HTTP-Only có hiệu lực **7 ngày**. |
| **Redis Cache** | Remote Dictionary Server | Hệ thống bộ nhớ In-Memory Data Store dùng để đếm Atomic Ticket ID, lưu JWT Blacklist khi Logout/Khóa account, và Cache dữ liệu thống kê Dashboard (TTL = 30–60 giây). |
| **UAT** | User Acceptance Testing | Kiểm thử chấp nhận người dùng do Cán bộ và Ban Quản lý Aurora University trực tiếp thực hiện trong **10 ngày làm việc** trước khi nghiệm thu chính thức. |
| **RTM** | Requirements Traceability Matrix | Ma trận truy xuất yêu cầu liên kết 1:1 từ Proposal $\rightarrow$ PRD Feature $\rightarrow$ API Endpoint $\rightarrow$ UAT Test Scenario nhằm đảm bảo **100%** tính bao phủ nghiệm thu. |
| **Responsive UI** | Responsive User Interface | Thiết kế giao diện đa nền tảng (Desktop & Mobile) áp dụng Tailwind CSS / Ant Design Breakpoints, tối ưu trải nghiệm cho 3.000 sinh viên và nhân viên. |
| **Out of Scope** | Ngoài phạm vi dự án | Các tính năng không nằm trong cam kết Hợp đồng dự án (VD: Gọi điện/Video call trực tiếp, Tích hợp AI Chatbot tự động trả lời, Dynamic ABAC Custom Roles, Mobile App Native). |

## 3. Ma Trận Áp Dụng Thuật Ngữ Theo Tài Liệu Hệ Thống

| Nhóm Tài Liệu | Danh Mục Thuật Ngữ Cốt Lõi Áp Dụng |
| :--- | :--- |
| **01-product / 02-domain** | Ticket, Ticket ID, FSM, SLA, CSAT, Responsive UI, Out of Scope |
| **03-modules (M01–M03)** | RBAC, SLA, CSAT, Idempotency Key, Zero Public Access |
| **04-workflows (WF-01 – WF-06)** | FSM, Ticket ID, Audit Trail, Zero Public Access, SLA |
| **05-nfr / 07-architecture** | RBAC, JWT, Redis Cache, Zero Public Access, Idempotency Key, Audit Trail |
| **06-acceptance / 08-project** | UAT, RTM, UniSupport, Out of Scope |