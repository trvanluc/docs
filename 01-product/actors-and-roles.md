# Định Nghĩa Vai Trò & Phân Quyền Hệ Thống (Actors & Roles)

## 1. Tổng Quan Kiến Trúc Phân Quyền (RBAC Architecture)
Hệ thống UniSupport áp dụng mô hình phân quyền dựa trên vai trò (Role-Based Access Control - RBAC). Mỗi người dùng khi đăng nhập sẽ được cấp một danh tính định danh duy nhất (`user_id`), thuộc về một vai trò chính (`role`) và có thể liên kết với một đơn vị phòng ban (`department_id`).

Quyền hạn của người dùng được xác thực tập trung thông qua JWT Access Token trên từng API Endpoint và được kiểm soát phạm vi dữ liệu (Data Isolation) ở cấp CSDL.

## 2. Chi Tiết Danh Mục Vai Trò (System Roles Specification)

### 2.1. Sinh Viên (`role = STUDENT`)
- **Mô tả:** Sinh viên đang theo học tại Aurora University có nhu cầu gửi yêu cầu giải đáp, hỗ trợ các thủ tục hành chính, đào tạo, tài chính hoặc kỹ thuật.
- **Phạm vi Dữ liệu (Data Scope):** Chỉ xem và thao tác trên dữ liệu do chính mình tạo ra (`WHERE student_id == current_user_id`). Tuyệt đối không có quyền xem Ticket của sinh viên khác.
- **Danh mục Quyền chi tiết (Permissions):**
  - Khởi tạo Ticket mới kèm file đính kèm (Ảnh/PDF $\le 10\text{MB}$, tối đa 3 file).
  - Tra cứu danh sách, tiến độ và lịch sử cập nhật Ticket cá nhân.
  - Bổ sung thông tin/file đính kèm khi Ticket ở trạng thái `NEED_MORE_INFO`.
  - Xem kết quả giải quyết và thực hiện Đánh giá chất lượng dịch vụ (CSAT $1-5$ sao, tối đa 01 lần/Ticket).
  - Nhận thông báo tự động (In-app Bell Notification / Email) khi Ticket có thay đổi trạng thái.

### 2.2. Nhân Viên Phòng Ban (`role = STAFF`)
- **Mô tả:** Cán bộ/Nhân viên thuộc các phòng ban nghiệp vụ (Phòng Đào tạo, Phòng Công tác sinh viên, Phòng Tài chính, Phòng Kế toán,...).
- **Phạm vi Dữ liệu (Data Scope):**
  - Xem danh sách Ticket nằm trong Queue chung của Phòng ban mình phụ trách (`WHERE department_id == current_staff_department_id`).
  - Thao tác trực tiếp trên các Ticket do cá nhân mình tiếp nhận xử lý (`WHERE assignee_id == current_staff_id`).
  - Không có quyền xem hoặc can thiệp vào Ticket của phòng ban khác (khi chưa được chuyển giao).
- **Danh mục Quyền chi tiết (Permissions):**
  - Tiếp nhận (Claim) Ticket mới (`NEW` / `TRANSFERRED`) từ Queue phòng ban về danh sách cá nhân xử lý.
  - Điều chỉnh Phân loại nhóm vấn đề (`category_id`) và Mức độ ưu tiên (`priority`: `LOW`, `MEDIUM`, `HIGH`, `URGENT`).
  - Chuyển tiếp Ticket sang phòng ban khác (`TRANSFERRED`) kèm lý do bắt buộc ($10-500\text{ ký tự}$).
  - Phát yêu cầu bổ sung hồ sơ/giấy tờ tới sinh viên (`NEED_MORE_INFO`).
  - Ghi nhận kết quả xử lý ($20-2000\text{ ký tự}$), đính kèm file kết quả và hoàn tất/giải quyết Ticket (`RESOLVED`).
  - Từ chối Ticket không hợp lệ (`REJECTED`) kèm lý do từ chối ($10-500\text{ ký tự}$).

### 2.3. Quản Lý Phòng Ban (`role = MANAGER`)
- **Mô tả:** Trưởng/Phó phòng ban chuyên môn chịu trách nhiệm giám sát tiến độ giải quyết công việc, phân công nhân sự và theo dõi chỉ số hài lòng trong phạm vi phòng ban.
- **Phạm vi Dữ liệu (Data Scope):** Toàn bộ dữ liệu Ticket, Báo cáo và Nhân sự thuộc `department_id` của mình phụ trách.
- **Danh mục Quyền chi tiết (Permissions):**
  - Toàn bộ quyền của STAFF trong phòng ban.
  - Phân công trực tiếp Ticket cho một Nhân viên cụ thể trong phòng ban hoặc thu hồi (Unassign/Reassign) Ticket cấp lại cho người khác.
  - Xem Dashboard tổng quan chỉ số SLA, cảnh báo quá hạn (SLA Breached) của phòng ban theo thời gian thực.
  - Báo cáo phân tích hiệu năng xử lý của từng nhân viên và điểm CSAT của phòng ban.
  - Export báo cáo thống kê phòng ban ra file Excel/CSV (Tối đa 10.000 dòng/lần).

### 2.4. Quản Trị Hệ Thống (`role = ADMIN`)
- **Mô tả:** Quản trị viên hệ thống UniSupport (Ban Giám hiệu, Phòng CNTT/Vận hành hệ thống).
- **Phạm vi Dữ liệu (Data Scope):** Toàn quyền hệ thống (Global Scope) trên toàn bộ Phòng ban, User, Ticket, Báo cáo và System Logs.
- **Danh mục Quyền chi tiết (Permissions):**
  - Quản lý danh mục Tài khoản người dùng: Tạo mới, Chỉnh sửa thông tin, Đổi vai trò (Role), Gán phòng ban (Department), Khóa/Mở khóa tài khoản (`ACTIVE`/`INACTIVE`).
  - Vô hiệu hóa phiên làm việc (Revoke Session/Token) ngay lập tức khi khóa tài khoản.
  - Xem Dashboard và Báo cáo tổng quan toàn trường (Cross-department Analytics).
  - Cấu hình danh mục nhóm vấn đề (Categories) và Khung thời gian SLA.
  - Xem và tra cứu Nhật ký hệ thống (Audit Trail Log) đối với các thao tác quản trị nhạy cảm.

## 3. Ma Trận Phân Quyền Chi Tiết (Access Control Matrix)

| Chức năng / API Endpoint | STUDENT | STAFF | MANAGER | ADMIN |
| :--- | :---: | :---: | :---: | :---: |
| **Đăng nhập & Lấy Profile** | X | X | X | X |
| **Tạo Ticket hỗ trợ mới** | X | - | - | - |
| **Xem danh sách Ticket cá nhân** | X | - | - | - |
| **Gửi bổ sung hồ sơ (File/Note)** | X | - | - | - |
| **Gửi Đánh giá hài lòng (CSAT)** | X | - | - | - |
| **Xem Queue Ticket Phòng ban** | - | X | X | X |
| **Tiếp nhận xử lý Ticket (Claim)** | - | X | X | X |
| **Chuyển phòng ban / Yêu cầu bổ sung** | - | X | X | X |
| **Ghi kết quả & Hoàn tất Ticket** | - | X | X | X |
| **Phân công / Thu hồi Ticket người khác** | - | - | X | X |
| **Xem Dashboard & Báo cáo Phòng ban** | - | - | X | X |
| **Xem Dashboard & Báo cáo Toàn trường** | - | - | - | X |
| **Tạo / Sửa / Khóa Tài khoản User** | - | - | - | X |
| **Xem Audit Log hệ thống** | - | - | - | X |

## 4. Ràng Buộc Kỹ Thuật & Mã Lỗi Truy Cập (Security & Error Handling Specs)

| Ràng buộc Kỹ thuật | Xử lý vi phạm | Mã lỗi HTTP & Error Code | Message hiển thị cho người dùng |
| :--- | :--- | :--- | :--- |
| **Chưa xác thực (Unauthenticated)** | Không gửi Bearer Token hoặc Token hết hạn. | `401 Unauthorized`<br><br>`UNAUTHORIZED` | "Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại." |
| **Sai vai trò (Role Mismatch)** | Student cố truy cập API Staff/Admin. | `403 Forbidden`<br><br>`FORBIDDEN_ACCESS` | "Bạn không có quyền truy cập vào chức năng này." |
| **Thao tác ngoài Scope Dữ liệu** | Staff cố xem/sửa Ticket của Phòng ban khác. | `403 Forbidden`<br><br>`FORBIDDEN_DEPARTMENT_ACCESS` | "Bạn không có quyền thao tác trên Ticket thuộc phòng ban khác." |
| **Student truy cập Ticket người khác** | Đổi `ticket_id` trên URL sang Ticket của bạn học. | `403 Forbidden`<br><br>`FORBIDDEN_ACCESS` | "Không tìm thấy yêu cầu hoặc bạn không có quyền truy cập." |
| **Tài khoản bị khóa (INACTIVE)** | Dùng Token của tài khoản đã bị Admin vô hiệu hóa. | `403 Forbidden`<br><br>`ACCOUNT_DISABLED` | "Tài khoản của bạn đã bị vô hiệu hóa. Vui lòng liên hệ Admin." |