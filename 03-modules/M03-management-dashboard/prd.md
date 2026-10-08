# Phân Hệ Quản Lý (M03 - Management Dashboard)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ Quản lý cung cấp trung tâm điều hành cho Ban Quản lý và Quản trị viên hệ thống (Admin). Phân hệ bao gồm các nhóm chức năng chính: Bảng theo dõi chỉ số thời gian thực (Real-time Metrics), Giám sát tuân thủ SLA, Báo cáo phân tích xu hướng & chất lượng dịch vụ, Quản lý tài khoản người dùng & Phân quyền (RBAC), và Nhật ký hệ thống (Audit Logs).

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-MNG-01] Quản lý đăng nhập & Xác thực phân quyền

#### 1. Mô tả & Phạm vi
Cho phép Trưởng phòng ban (Manager) và Quản trị hệ thống (Admin) đăng nhập vào Cổng Quản trị UniSupport, xác thực hai yếu tố (nếu bật) và phân luồng dữ liệu theo cấp quản lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Quản lý phòng ban (MANAGER), Quản trị viên hệ thống (ADMIN).
- **Preconditions:** Tài khoản tồn tại trên CSDL, `status = ACTIVE`, thuộc nhóm vai trò `MANAGER` hoặc `ADMIN`.

#### 3. Scope & Phân quyền Dữ liệu (Data Isolation Rules)
- **Cấp Quản lý Phòng ban (MANAGER):**
  - Chỉ xem được Dashboard, Metric, Báo cáo và Danh sách Ticket thuộc `department_id` của mình phụ trách.
  - Không có quyền truy cập vào menu Quản trị tài khoản toàn hệ thống.
- **Cấp Quản trị Hệ thống (ADMIN):**
  - Xem toàn bộ Dashboard, Báo cáo toàn trường (All departments).
  - Toàn quyền tạo, sửa, vô hiệu hóa tài khoản và gán quyền.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Redirect Rule:**
  - ADMIN đăng nhập thành công -> Điều hướng về `/admin/dashboard`.
  - MANAGER đăng nhập thành công -> Điều hướng về `/manager/dashboard` (Mặc định filter theo phòng ban cá nhân).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Quản lý truy cập `/admin/login`.
2. Kiểm tra Token: Nếu hợp lệ và có role `MANAGER`/`ADMIN` -> Chuyển thẳng vào Dashboard.
3. Nhập Username/Email và Password, nhấn Đăng nhập.
4. Client validate form -> Gửi request đăng nhập.
5. Server xác thực thông tin, cấp JWT Access Token chứa: `user_id`, `role`, `department_id`, `permissions_list`.
6. Client lưu Token an toàn, chuyển hướng dựa theo role.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Credential không đúng (401 Unauthorized):** Hiển thị Alert error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản Student/Staff cố truy cập (403 Forbidden):** Hiển thị Alert error: *"Bạn không có quyền truy cập vào Cổng Quản trị."*
- **Tài khoản bị khóa (403 Forbidden):** Hiển thị Alert error: *"Tài khoản quản trị đã bị vô hiệu hóa."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập đúng tài khoản `MANAGER` -> Truy cập Dashboard chỉ hiển thị dữ liệu phòng ban phụ trách.
- **AC-02:** Đăng nhập đúng tài khoản `ADMIN` -> Truy cập Dashboard hiển thị dữ liệu toàn trường và đầy đủ Menu Quản trị.
- **AC-03:** Đăng nhập từ tài khoản không phải Admin/Manager -> Trả về lỗi 403, từ chối cấp token.

---

### [FR-MNG-02] Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision)

#### 1. Mô tả & Phạm vi
Cung cấp màn hình Tổng quan chỉ số hoạt động (KPIs), giám sát phân bổ công việc theo Nhân viên/Phòng ban và cảnh báo các Ticket vi phạm hoặc nguy cơ vi phạm thời gian cam kết xử lý (SLA).

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** `MANAGER`, `ADMIN`.
- **Preconditions:** Đã đăng nhập thành công.

#### 3. Quy tắc Dữ liệu & Logic SLA (SLA Calculation Rules)
- **Quy định Khung giờ SLA (SLA Target):** Mặc định thời hạn xử lý Ticket là 24 giờ làm việc kể từ khi tiếp nhận (không tính Thứ 7, Chủ nhật và ngày Lễ).
- **Phân loại Trạng thái SLA:**
  - **Trong hạn (On-Track):** Thời gian còn lại > 25% tổng thời hạn SLA.
  - **Sắp quá hạn (Warning):** Thời gian còn lại <= 25% tổng thời hạn SLA (Ví dụ: Còn dưới 6 giờ).
  - **Đã quá hạn (Breached/Overdue):** Thời gian xử lý thực tế đã vượt quá thời hạn SLA nhưng Ticket chưa ở trạng thái `RESOLVED`/`CLOSED`.
- **Thống kê Chỉ số Cốt lõi (Summary Cards):**
  - **Total Received:** Tổng số Ticket tiếp nhận trong kỳ chọn.
  - **In-Progress:** Số Ticket đang xử lý.
  - **SLA Warning:** Số Ticket đang ở ngưỡng sắp quá hạn.
  - **SLA Breached:** Số Ticket đã quá hạn chưa xử lý xong.
  - **Avg Resolution Time:** Thời gian xử lý trung bình (Giờ).

#### 4. Cơ chế Cập nhật Dữ liệu (Data Refresh Specs)
- **Mặc định:** Dashboard tự động làm mới dữ liệu (Auto-refresh) sau mỗi 60 giây hoặc cung cấp nút Làm mới dữ liệu (Refresh) thủ công.
- **Tối ưu Hiệu năng Query:** Server không query trực tiếp full CSDL cho mỗi lần render. Các chỉ số Tổng quan phải được tính toán qua Aggregation Query hoặc Cached (Redis Cache duration: 30–60s).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Quản lý mở trang Dashboard (`/admin/dashboard`).
2. Mặc định hệ thống tải dữ liệu theo Bộ lọc thời gian: 7 ngày gần nhất.
3. Hiển thị 5 Thẻ chỉ số tổng quan (Summary Cards).
4. Hiển thị Bảng phân bổ workload: Số lượng Ticket đang gán cho từng Nhân viên (Assignee) và Trạng thái tương ứng.
5. Hiển thị Danh sách Cảnh báo SLA: Liệt kê các Ticket ở trạng thái `Warning` và `Breached` lên trên cùng.
6. Quản lý có thể thay đổi Bộ lọc thời gian (Hôm nay, 7 ngày, 30 ngày, Tùy chỉnh khoảng ngày).
7. Client gửi request fetch lại data theo khoảng thời gian đã chọn.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Chọn khoảng thời gian không hợp lệ (400 Bad Request):** Ví dụ Ngày bắt đầu > Ngày kết thúc -> Hiển thị lỗi ngay trên Date Picker: *"Khoảng thời gian không hợp lệ."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Số liệu trên Thẻ chỉ số phản ánh chính xác trạng thái thực tế dưới Database.
- **AC-02:** Click vào thẻ `SLA Breached` -> Chuyển hướng đến danh sách chi tiết các Ticket đã quá hạn.
- **AC-03:** Nhân viên A được gán 5 Ticket -> Bảng phân bổ workload hiển thị đúng 5 Ticket dưới tên Nhân viên A.
- **AC-04:** Bấm nút Refresh -> Dữ liệu cập nhật mới nhất trong dưới 1 giây.

---

### [FR-MNG-03] Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export)

#### 1. Mô tả & Phạm vi
Cho phép Quản lý xem các biểu đồ phân tích chuyên sâu về xu hướng nhóm vấn đề, hiệu năng xử lý của phòng ban/nhân viên, phân bố điểm đánh giá mức độ hài lòng (CSAT) và xuất báo cáo ra file Excel/CSV.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** `MANAGER`, `ADMIN`.
- **Preconditions:** Đã đăng nhập thành công.

#### 3. Báo cáo Chi tiết & Loại Biểu đồ (Report Specifications)
- **Báo cáo Xu hướng Yêu cầu (Volume Trend):** Biểu đồ đường (Line Chart) thể hiện biến động số lượng Ticket theo ngày/tuần/tháng, phân loại theo Category.
- **Báo cáo Thời gian Xử lý (Performance Report):** Biểu đồ cột (Bar Chart) so sánh Thời gian xử lý trung bình giữa các Phòng ban hoặc giữa các Nhân viên trong cùng phòng.
- **Báo cáo Đánh giá Hài lòng (CSAT Report):**
  - Biểu đồ tròn (Pie Chart) tỷ lệ % đánh giá 1 sao đến 5 sao.
  - Điểm CSAT trung bình = (Tổng số sao / (Tổng số lượt đánh giá * 5)) * 100%.
  - Bảng danh sách phản hồi chi tiết (Gồm: Mã Ticket, Tên Sinh viên, Số sao, Nhận xét, Tên Nhân viên phụ trách).

#### 4. Quy tắc Xuất Dữ liệu (Export Rules)
- **Định dạng hỗ trợ:** Microsoft Excel (`.xlsx`), CSV (`.csv`).
- **Nội dung file xuất:** Chứa đầy đủ các bản ghi theo đúng bộ lọc đang chọn trên giao diện.
- **Giới hạn số lượng (Pagination / Export Limit):** Tối đa 10.000 bản ghi / 1 lần xuất. Nếu vượt quá 10.000 bản ghi, hệ thống yêu cầu người dùng hẹp khoảng thời gian lọc.
- **Đặt tên File tự động:** `[Ma_Bao_Cao]_[Tu_Ngay]_[Den_Ngay].[xlsx]` (Ví dụ: `CSAT_Report_20261001_20261009.xlsx`).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Quản lý truy cập menu Báo cáo & Thống kê (`/admin/reports`).
2. Chọn Tab báo cáo cần xem (Xu hướng / Hiệu năng / CSAT).
3. Chọn Bộ lọc: Khoảng thời gian, Phòng ban, Nhóm vấn đề. Bấm Xem báo cáo.
4. Client gửi request fetch data -> Server trả về data dạng JSON -> Client render Biểu đồ và Bảng số liệu.
5. Quản lý bấm nút Xuất Báo Cáo (Export) -> Chọn định dạng Excel hoặc CSV.
6. Client gọi API Export -> Server sinh file async/stream -> Trả về link download file.
7. Trình duyệt tự động tải file về máy người dùng.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Không có dữ liệu trong kỳ báo cáo (200 OK Data Empty):** Biểu đồ hiển thị trạng thái Empty State: *"Không có dữ liệu trong khoảng thời gian đã chọn"*. Nút Export bị vô hiệu hóa.
- **Xuất vượt quá 10.000 record (400 Bad Request):** Alert error: *"Dữ liệu xuất vượt quá 10.000 dòng. Vui lòng thu hẹp khoảng thời gian lọc."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Điểm CSAT trung bình và tỷ lệ % phân bố sao tính toán chính xác theo công thức quy định.
- **AC-02:** Xuất file Excel mở ra đầy đủ các cột dữ liệu, không bị lỗi font Tiếng Việt, định dạng ngày tháng chuẩn `YYYY-MM-DD HH:mm:ss`.
- **AC-03:** Lọc báo cáo theo Phòng Đào Tạo -> Toàn bộ số liệu và danh sách phản hồi chỉ liên quan đến Phòng Đào Tạo.

---

### [FR-MNG-04] Quản trị người dùng & Phân quyền (User Management & RBAC)

#### 1. Mô tả & Phạm vi
Cung cấp công cụ quản lý toàn bộ tài khoản người dùng trong hệ thống (Tạo mới, Cập nhật thông tin, Khóa/Mở khóa tài khoản, Đổi mật khẩu) và phân quyền chi tiết theo vai trò.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** CHỈ ADMIN (Quản trị viên hệ thống).
- **Preconditions:** Đăng nhập thành công với vai trò `ADMIN`.

#### 3. Ma trận Phân quyền Vai trò (RBAC Matrix)

| Chức năng / Quyền | STUDENT | STAFF | MANAGER | ADMIN |
| :--- | :---: | :---: | :---: | :---: |
| **Tạo Ticket cá nhân** | X | — | — | — |
| **Xem / Đánh giá Ticket cá nhân** | X | — | — | — |
| **Tiếp nhận / Xử lý Ticket phòng ban** | — | X | X | X |
| **Chuyển phòng ban / Yêu cầu bổ sung** | — | X | X | X |
| **Xem Dashboard & Báo cáo phòng ban** | — | — | X | X |
| **Xem Báo cáo toàn trường** | — | — | — | X |
| **Quản lý Tài khoản & Phân quyền** | — | — | — | X |
| **Xem Audit Log hệ thống** | — | — | — | X |

#### 4. Quy tắc Dữ liệu & Validation Tài khoản (Data Contracts)
- **Tạo Tài khoản mới (Create User):**
  - **Username / Student ID / Staff ID:** Bắt buộc, duy nhất (Unique), 6-20 ký tự, không chứa ký tự đặc biệt.
  - **Email công vụ:** Bắt buộc, duy nhất, đúng định dạng Email (`@aurora.edu.vn`).
  - **Full Name:** Bắt buộc, 2-50 ký tự.
  - **Role:** Dropdown bắt buộc chọn 1 (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`).
  - **Department:** Bắt buộc chọn nếu Role là `STAFF` hoặc `MANAGER`.
  - **Password:** Độ dài tối thiểu 8 ký tự, gồm ít nhất 1 chữ hoa, 1 chữ thường, 1 số.
- **Trạng thái Tài khoản (Account Status):** `ACTIVE` (Hoạt động), `INACTIVE` (Khóa/Vô hiệu hóa).
- **Quy tắc vô hiệu hóa (Revoke Session):** Khi Admin chuyển trạng thái tài khoản sang `INACTIVE`, hệ thống phải ngay lập tức hủy toàn bộ Active Tokens/Sessions của tài khoản đó. Người dùng bị khóa sẽ bị đẩy văng ra trang Login nếu đang thao tác.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Admin truy cập trang Quản lý Tài khoản (`/admin/users`).
2. Hệ thống hiển thị Bảng danh sách người dùng (Phân trang 15 user/trang, có ô Tìm kiếm theo Name/Email/Code, Filter theo Role/Department).
3. **Thao tác Tạo mới:**
   - Admin bấm **+ Tạo tài khoản mới**.
   - Hiển thị Modal nhập thông tin -> Điền dữ liệu -> Bấm Lưu.
   - Server validate trùng lặp Username/Email -> Tạo record -> Trả về HTTP 201 Created.
4. **Thao tác Khóa tài khoản:**
   - Admin chọn 1 user -> Bấm Vô hiệu hóa.
   - Hiển thị Modal xác nhận: *"Bạn có chắc chắn muốn khóa tài khoản [Tên_User]?"*
   - Admin bấm Xác nhận khóa.
   - Server cập nhật `status = INACTIVE`, xóa Redis Session/Token của user đó -> Trả về HTTP 200 OK.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Trùng Username/Email (409 Conflict):** Hiển thị lỗi dưới field tương ứng: *"Username hoặc Email này đã tồn tại trên hệ thống."*
- **Self-Deactivation Prevention (400 Bad Request):** Admin không được phép tự khóa tài khoản chính mình đang đăng nhập. Nếu bấm khóa chính mình -> Alert error: *"Bạn không thể tự vô hiệu hóa tài khoản của chính mình."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Tạo thành công user role `STAFF` gán cho Phòng Tài chính -> User mới đăng nhập đúng cổng Staff và thấy Queue của Phòng Tài chính.
- **AC-02:** Khóa tài khoản Staff B đang online -> Trong vòng 5 giây, Staff B bị logout ra màn hình Đăng nhập và không thể đăng nhập lại.
- **AC-03:** Nhập Email trùng với user đã có -> Báo lỗi validation 409 rõ ràng, không lưu DB.
- **AC-04:** Tìm kiếm tên "Nguyễn Văn A" -> Bảng kết quả trả về đúng các user có chứa chuỗi tìm kiếm.

---

### [FR-MNG-05] Ghi nhận Nhật ký Hệ thống (Audit Trail / Activity Log)

#### 1. Mô tả & Phạm vi
Tự động ghi nhận lại toàn bộ các thao tác quản trị quan trọng và sự thay đổi dữ liệu cấu hình hệ thống để phục vụ công tác tra soát, an ninh bảo mật.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** System / ADMIN.

#### 3. Quy tắc Dữ liệu Audit Log (Audit Specs)
- **CÁC THAO TÁC BẮT BUỘC GHI LOG:**
  - `USER_CREATE`: Tạo tài khoản mới.
  - `USER_UPDATE_ROLE`: Thay đổi quyền/vai trò user.
  - `USER_DISABLE`: Khóa tài khoản.
  - `TICKET_TRANSFER`: Chuyển phòng ban Ticket (Ghi vết người chuyển, phòng ban gốc, phòng ban đích).
  - `TICKET_DELETE` / `FORCE_CLOSE`: Quản lý can thiệp đóng hoặc xóa Ticket.
- **Cấu trúc 1 Record Audit Log:** `log_id`, `actor_id` (Người thực hiện), `actor_ip`, `action_type`, `target_object` (User ID hoặc Ticket ID), `description` (Chi tiết thay đổi Old Value -> New Value), `created_at`.
- **Ràng buộc Toàn vẹn:** Log chỉ được phép ghi mới (Append-Only) và ĐỌC (Read-Only). Tuyệt đối không cho phép bất kỳ ai (kể cả Admin) sửa hoặc xóa các record Audit Log trên giao diện.

#### 4. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Khi Admin đổi role của User X từ `STAFF` sang `MANAGER` -> Bảng Audit Log lập tức xuất hiện 01 record ghi nhận đúng IP, thời gian, người thực hiện và nội dung thay đổi.
- **AC-02:** Giao diện xem Audit Log không có nút Sửa hoặc Xóa.

---

## III. BẢNG MÃ LỖI CHUẨN DÙNG CHUNG PHÂN HỆ MANAGEMENT (SYSTEM ERROR CODES)

| HTTP Status | Error Code | Message hiển thị người dùng | Kịch bản áp dụng |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_DATE_RANGE` | *"Khoảng thời gian lọc không hợp lệ."* | Ngày bắt đầu lớn hơn ngày kết thúc. |
| **400** | `EXPORT_LIMIT_EXCEEDED` | *"Dữ liệu xuất vượt quá 10.000 dòng. Vui lòng thu hẹp bộ lọc."* | Xuất file quá giới hạn số dòng. |
| **400** | `CANNOT_DISABLE_SELF` | *"Bạn không thể tự vô hiệu hóa tài khoản của chính mình."* | Admin tự khóa chính mình. |
| **401** | `UNAUTHORIZED` | *"Phiên làm việc hết hạn. Vui lòng đăng nhập lại."* | Token hết hạn. |
| **403** | `FORBIDDEN_ADMIN_ONLY` | *"Chức năng này chỉ dành cho Quản trị viên hệ thống (Admin)."* | Manager cố truy cập chức năng Quản lý User. |
| **409** | `USERNAME_EXISTS` | *"Tên đăng nhập / Mã định danh đã tồn tại trên hệ thống."* | Tạo trùng Username/Student ID. |
| **409** | `EMAIL_EXISTS` | *"Địa chỉ Email này đã được đăng ký cho tài khoản khác."* | Tạo trùng Email. |
| **500** | `INTERNAL_SERVER_ERROR` | *"Hệ thống gặp sự cố kỹ thuật. Vui lòng thử lại sau."* | Lỗi Server/Database unhandled. |