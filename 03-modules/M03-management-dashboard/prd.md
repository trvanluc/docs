# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Quản Lý (PRD - M03 Management Dashboard)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Quản lý (Management Dashboard)** cung cấp trung tâm điều hành cho Ban Quản lý và Quản trị viên hệ thống (Admin). Phân hệ bao gồm các nhóm chức năng chính: Bảng theo dõi chỉ số thời gian thực (Real-time Metrics), Giám sát tuân thủ SLA, Báo cáo phân tích xu hướng & chất lượng dịch vụ, Quản lý tài khoản người dùng & Phân quyền (RBAC), và Nhật ký hệ thống (Audit Logs).

### 1. Luồng sử dụng và giới hạn vai trò

MANAGER đăng nhập để theo dõi tình hình và báo cáo của phòng ban mình. ADMIN đăng nhập để xem dữ liệu toàn trường, quản trị tài khoản/quyền và tra soát nhật ký. Quản trị tài khoản thuộc riêng ADMIN tại FR-MNG-04; quyền MANAGER giám sát và phân công nhân sự trong phòng ban không bao gồm tạo tài khoản.

Dashboard phục vụ theo dõi tình hình hiện tại; báo cáo phục vụ phân tích kỳ dữ liệu đã chọn và xuất dữ liệu. Điểm hài lòng trong báo cáo lấy từ đánh giá đã có ở FR-STU-04, không phát sinh một chức năng đánh giá khác.

### 2. Danh mục Chức năng Cốt lõi

- **[FR-MNG-01]** Quản lý đăng nhập & Xác thực phân quyền.
- **[FR-MNG-02]** Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision).
- **[FR-MNG-03]** Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export).
- **[FR-MNG-04]** Quản trị người dùng & Phân quyền (User Management & RBAC).
- **[FR-MNG-05]** Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail).

---

### Giới hạn công sức và mã yêu cầu

Mã FR trong danh mục dưới đây giữ nguyên theo PRD đã chốt. Giờ M03 được đối chiếu theo các dòng Resource!22:27: **207 giờ cơ sở + 8 giờ dự phòng = 215 giờ kế hoạch**. Xem [bảng Resources](../../Phan_bo_Resources_Antigravity.md); số thứ tự dòng công sức không phải mã FR. Đăng nhập các cổng dùng chung R-ADM-01, không có estimate bổ sung. Những tên công việc nguồn chưa có đặc tả thống nhất không tự trở thành chức năng mới.

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-MNG-01] Quản lý đăng nhập & Xác thực phân quyền

#### 1. Mô tả & Phạm vi
Cho phép Trưởng phòng ban (Manager) và Quản trị hệ thống (Admin) đăng nhập vào Cổng Quản trị UniSupport, xác thực hai yếu tố (nếu bật) và phân luồng dữ liệu theo cấp quản lý.

**Luồng thao tác nghiệp vụ:**

1. MANAGER hoặc ADMIN dùng tài khoản đang hoạt động để đăng nhập vào cổng quản trị.
2. MANAGER vào màn hình dữ liệu phòng ban mình; ADMIN vào màn hình dữ liệu toàn trường.
3. Menu và dữ liệu được giới hạn theo vai trò tại mục 3. Tài khoản STUDENT/STAFF hoặc tài khoản bị vô hiệu hóa bị từ chối theo mục 6.

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
  - ADMIN đăng nhập thành công → Điều hướng về `/admin/dashboard`.
  - MANAGER đăng nhập thành công → Điều hướng về `/manager/dashboard` (Mặc định filter theo phòng ban cá nhân).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Quản lý truy cập `/admin/login`.
2. Kiểm tra Token: Nếu hợp lệ và có role `MANAGER`/`ADMIN` → Chuyển thẳng vào Dashboard.
3. Nhập Username/Email và Password, nhấn Đăng nhập.
4. Client validate form → Gửi request đăng nhập.
5. Server xác thực thông tin, cấp JWT Access Token chứa: `user_id`, `role`, `department_id`, `permissions_list`.
6. Client lưu Token an toàn, chuyển hướng dựa theo role.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Credential không đúng (401 Unauthorized):** Hiển thị Alert error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản Student/Staff cố truy cập (403 Forbidden):** Hiển thị Alert error: *"Bạn không có quyền truy cập vào Cổng Quản trị."*
- **Tài khoản bị khóa (403 Forbidden):** Hiển thị Alert error: *"Tài khoản quản trị đã bị vô hiệu hóa."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập đúng tài khoản `MANAGER` → Truy cập Dashboard chỉ hiển thị dữ liệu phòng ban phụ trách.
- **AC-02:** Đăng nhập đúng tài khoản `ADMIN` → Truy cập Dashboard hiển thị dữ liệu toàn trường và đầy đủ Menu Quản trị.
- **AC-03:** Đăng nhập từ tài khoản không phải Admin/Manager → Trả về lỗi 403, từ chối cấp token.

---

### [FR-MNG-02] Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision)

#### 1. Mô tả & Phạm vi
Cung cấp màn hình Tổng quan chỉ số hoạt động (KPIs), giám sát phân bổ công việc theo Nhân viên/Phòng ban và cảnh báo các Ticket vi phạm hoặc nguy cơ vi phạm thời gian cam kết xử lý (SLA).

**Luồng thao tác nghiệp vụ:**

1. Quản lý mở Dashboard, xem các thẻ tổng quan, bảng khối lượng công việc và danh sách cảnh báo SLA.
2. Chọn kỳ thời gian cần theo dõi; mọi chỉ số và danh sách vẫn nằm trong phạm vi dữ liệu của vai trò đăng nhập.
3. Mở thẻ quá hạn để xem các yêu cầu quá hạn cụ thể theo AC-02, hoặc làm mới dữ liệu theo cơ chế tại mục 4.
4. Kết quả là nhận biết số lượng, tiến độ và yêu cầu cần chú ý; không coi thao tác xem cảnh báo là đã xử lý hoặc hoàn tất Ticket.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** `MANAGER`, `ADMIN`.
- **Preconditions:** Đã đăng nhập thành công.

#### 3. Quy tắc Dữ liệu & Logic SLA (SLA Calculation Rules)
- **Quy định Khung giờ SLA (SLA Target):** Mặc định thời hạn xử lý Ticket là 24 giờ làm việc kể từ khi tạo Ticket theo BR-10 (không tính Thứ 7, Chủ nhật và ngày Lễ).
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
- **Chọn khoảng thời gian không hợp lệ (400 Bad Request):** Ví dụ Ngày bắt đầu > Ngày kết thúc → Hiển thị lỗi ngay trên Date Picker: *"Khoảng thời gian không hợp lệ."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Số liệu trên Thẻ chỉ số phản ánh chính xác trạng thái thực tế dưới Database.
- **AC-02:** Click vào thẻ `SLA Breached` → Chuyển hướng đến danh sách chi tiết các Ticket đã quá hạn.
- **AC-03:** Nhân viên A được gán 5 Ticket → Bảng phân bổ workload hiển thị đúng 5 Ticket dưới tên Nhân viên A.
- **AC-04:** Bấm nút Refresh → Dữ liệu cập nhật mới nhất trong dưới 1 giây.
- **AC-05:** MANAGER chọn kỳ thời gian và mở danh sách từ thẻ quá hạn → Thẻ, bảng khối lượng và danh sách chi tiết đều chỉ chứa dữ liệu phòng ban mình theo FR-MNG-01.

---

### [FR-MNG-03] Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export)

#### 1. Mô tả & Phạm vi
Cho phép Quản lý xem các biểu đồ phân tích chuyên sâu về xu hướng nhóm vấn đề, hiệu năng xử lý của phòng ban/nhân viên, phân bố điểm đánh giá mức độ hài lòng (CSAT) và xuất báo cáo ra file Excel/CSV.

**Luồng thao tác nghiệp vụ:**

1. Quản lý chọn báo cáo Xu hướng, Hiệu năng hoặc CSAT rồi chọn kỳ thời gian và các bộ lọc trong phạm vi được phép.
2. Xem biểu đồ và bảng số liệu; không có dữ liệu thì hiển thị trạng thái rỗng và không cho xuất theo mục 6.
3. Chọn xuất Excel hoặc CSV; file chứa dữ liệu theo cùng bộ lọc và phạm vi đang xem.
4. Vượt 10.000 bản ghi thì thu hẹp kỳ lọc theo thông báo đã có. Dữ liệu CSAT chỉ phản ánh đánh giá đã gửi thành công tại FR-STU-04.

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
- **Giới hạn số lượng (Export Limit):** Tối đa **10.000 bản ghi / 1 lần xuất**. Nếu vượt quá 10.000 bản ghi, hệ thống yêu cầu người dùng hẹp khoảng thời gian lọc.
- **Đặt tên File tự động:** `[Ma_Bao_Cao]_[Tu_Ngay]_[Den_Ngay].[xlsx]` (Ví dụ: `CSAT_Report_20261001_20261009.xlsx`).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Quản lý truy cập menu Báo cáo & Thống kê (`/admin/reports`).
2. Chọn Tab báo cáo cần xem (Xu hướng / Hiệu năng / CSAT).
3. Chọn Bộ lọc: Khoảng thời gian, Phòng ban, Nhóm vấn đề. Bấm **Xem báo cáo**.
4. Client gửi request fetch data → Server trả về data dạng JSON → Client render Biểu đồ và Bảng số liệu.
5. Quản lý bấm nút **Xuất Báo Cáo (Export)** → Chọn định dạng Excel hoặc CSV.
6. Client gọi API Export → Server sinh file async/stream → Trả về link download file.
7. Trình duyệt tự động tải file về máy người dùng.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Không có dữ liệu trong kỳ báo cáo (200 OK Data Empty):** Biểu đồ hiển thị trạng thái Empty State: *"Không có dữ liệu trong khoảng thời gian đã chọn"*. Nút Export bị vô hiệu hóa.
- **Xuất vượt quá 10.000 record (400 Bad Request):** Alert error: *"Dữ liệu xuất vượt quá 10.000 dòng. Vui lòng thu hẹp khoảng thời gian lọc."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Điểm CSAT trung bình và tỷ lệ % phân bố sao tính toán chính xác theo công thức quy định.
- **AC-02:** Xuất file Excel mở ra đầy đủ các cột dữ liệu, không bị lỗi font Tiếng Việt, định dạng ngày tháng chuẩn `YYYY-MM-DD HH:mm:ss`.
- **AC-03:** Lọc báo cáo theo Phòng Đào Tạo → Toàn bộ số liệu và danh sách phản hồi chỉ liên quan đến Phòng Đào Tạo.
- **AC-04:** MANAGER xuất báo cáo đã lọc → File chỉ chứa dữ liệu thuộc phòng ban mình và bộ lọc đang áp dụng, không có dữ liệu phòng ban khác; ADMIN xuất theo phạm vi được chọn trong quyền toàn trường.

---

### [FR-MNG-04] Quản trị người dùng & Phân quyền (User Management & RBAC)

#### 1. Mô tả & Phạm vi
Cung cấp công cụ quản lý toàn bộ tài khoản người dùng trong hệ thống (Tạo mới, Cập nhật thông tin, Khóa/Mở khóa tài khoản, Đổi mật khẩu) và phân quyền chi tiết theo vai trò. Đây là cổng duy nhất cấp tài khoản; sinh viên và nhân viên **không tự đăng ký tài khoản**.

**Luồng thao tác nghiệp vụ:**

1. ADMIN mở danh sách tài khoản, tìm/lọc người dùng theo các điều kiện đã có.
2. Khi cấp tài khoản, ADMIN nhập thông tin bắt buộc, chọn vai trò và gán phòng ban cho STAFF/MANAGER, rồi lưu theo mục 4–5.
3. Tài khoản được cấp được dùng để đăng nhập vào đúng cổng tại FR-STU-01, FR-STF-01 hoặc FR-MNG-01; sinh viên không tự đăng ký tài khoản.
4. Khi khóa tài khoản, ADMIN chọn đúng người dùng và xác nhận; người đó bị vô hiệu hóa phiên theo quy tắc đã có. Trùng thông tin hoặc tự khóa chính mình thì xử lý theo mục 6.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** CHỈ ADMIN (Quản trị viên hệ thống).
- **Preconditions:** Đăng nhập thành công với vai trò `ADMIN`.

#### 3. Ma trận Phân quyền Vai trò (RBAC Matrix)

| Chức năng / Quyền | STUDENT | STAFF | MANAGER | ADMIN |
| :--- | :---: | :---: | :---: | :---: |
| **Tạo Ticket cá nhân** | X | — | — | — |
| **Xem / Đánh giá Ticket cá nhân** | X | — | — | — |
| **Xem Queue & Claim Ticket** | — | X | X | X |
| **Chuyển phòng ban / Yêu cầu bổ sung** | — | X | X | X |
| **Ghi kết quả & Resolve Ticket** | — | X | X | X |
| **Phân công / Thu hồi Ticket** | — | — | X | X |
| **Xem Dashboard & Báo cáo Phòng ban** | — | — | X | X |
| **Xem Dashboard & Báo cáo Toàn trường** | — | — | — | X |
| **Tạo / Sửa / Khóa Tài khoản User** | — | — | — | X |
| **Xem Audit Log hệ thống** | — | — | — | X |

**Giới hạn nhập liệu đã có trong PRD gốc:** Mã định danh duy nhất, 6–20 ký tự, không chứa ký tự đặc biệt; họ tên 2–50 ký tự; email nhà trường đúng định dạng và duy nhất; mật khẩu khởi tạo tối thiểu 8 ký tự, có chữ hoa, chữ thường và chữ số. Tên trường kỹ thuật phía dưới được giữ theo bản hiện tại; không sửa API/CSDL.

#### 4. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Thông tin bắt buộc khi tạo tài khoản:**
  - **user_code:** Mã sinh viên / Mã nhân viên (Unique toàn hệ thống).
  - **full_name:** Họ và tên đầy đủ.
  - **email:** Email nhà trường (Unique toàn hệ thống). Tự động `trim()` và lowercase.
  - **role:** Bắt buộc chọn: `STUDENT`, `STAFF`, `MANAGER`, `ADMIN`.
  - **department_id:** Bắt buộc đối với `STAFF` và `MANAGER`. Để `NULL` đối với `STUDENT` và `ADMIN`.
- **Mật khẩu khởi tạo:** ADMIN nhập mật khẩu theo quy tắc PRD gốc: tối thiểu 8 ký tự, có chữ hoa, chữ thường và chữ số. Không bổ sung chức năng tự sinh/gửi mật khẩu tự động qua email trong lần sửa này.
- **Vô hiệu hóa phiên khi khóa tài khoản:** Khi `status = INACTIVE`, hệ thống ngay lập tức Revoke toàn bộ Active Sessions và Refresh Tokens của user đó trên Redis/Database (theo BR-15).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. ADMIN truy cập `/admin/users`.
2. Hệ thống hiển thị danh sách User kèm bộ lọc: `role`, `department`, `status` (`ACTIVE`/`INACTIVE`).
3. **Tạo tài khoản mới:**
   - ADMIN bấm **Tạo tài khoản mới**.
   - Nhập `user_code`, `full_name`, `email`, mật khẩu khởi tạo; chọn `role`, chọn `department_id` (nếu cần).
   - ADMIN bấm **Lưu tài khoản**.
   - Server kiểm tra trùng lặp `email` và `user_code`, tạo bản ghi User với `status = ACTIVE`.
   - Tài khoản đã tạo được dùng để đăng nhập tại đúng cổng tương ứng; không đặc tả thêm chức năng gửi email thông tin đăng nhập.
4. **Khóa tài khoản:**
   - ADMIN chọn User cần khóa, bấm **Khóa tài khoản**.
   - Server cập nhật `status = INACTIVE`, Revoke toàn bộ Sessions/Tokens của User đó.
   - User bị đẩy về màn hình Login ở thao tác API tiếp theo với lỗi `403 ACCOUNT_DISABLED`.
5. **Mở khóa tài khoản:**
   - ADMIN chọn User đang `INACTIVE`, bấm **Mở khóa tài khoản**.
   - Server cập nhật `status = ACTIVE`. User có thể đăng nhập lại bình thường.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Trùng email hoặc user_code (409 Conflict):** Alert error: *"Email hoặc Mã định danh đã tồn tại trên hệ thống."*
- **Admin tự khóa chính mình (400 Bad Request):** Alert error: *"Không thể vô hiệu hóa tài khoản đang đăng nhập hiện tại."*
- **Đổi role của STAFF/MANAGER không gán department:** Alert error: *"Vai trò STAFF/MANAGER bắt buộc phải được gán Phòng ban."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Tạo tài khoản Staff với đúng `department_id` → Nhân viên đăng nhập tại cổng Staff và chỉ thấy Queue của phòng ban được gán.
- **AC-02:** Khóa tài khoản → Người dùng bị đăng xuất ngay lập tức ở thao tác API tiếp theo với lỗi `403 ACCOUNT_DISABLED`.
- **AC-03:** Mở khóa tài khoản → Người dùng đăng nhập lại bình thường.
- **AC-04:** Admin thử tạo tài khoản với email đã tồn tại → Hệ thống báo lỗi và không tạo bản ghi trùng.

---

### [FR-MNG-05] Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail)

#### 1. Mô tả & Phạm vi
Kiểm soát an toàn dữ liệu và bảo mật tệp đính kèm thông qua Secured API Proxy, đồng thời ghi nhận nhật ký tra soát bất biến (Append-only Audit Trail) cho toàn bộ các hành động trọng yếu trong hệ thống.

**Luồng thao tác nghiệp vụ:**

1. Toàn bộ file đính kèm lưu ở thư mục Private, không truy cập được qua URL công khai.
2. API phục vụ xem file phải qua AuthMiddleware và DataScopeMiddleware; người không có quyền nhận `403 FORBIDDEN_ACCESS`.
3. Mọi hành động quan trọng (đổi trạng thái Ticket, chuyển phòng ban, khóa tài khoản) đều ghi 01 bản ghi Audit Log tự động.
4. ADMIN có thể tra soát Audit Log qua giao diện lọc/tìm kiếm; không có chức năng sửa/xóa nhật ký.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Toàn bộ người dùng (cho kiểm soát file), ADMIN (cho tra soát Audit Log).
- **Preconditions:** Mọi yêu cầu truy xuất dữ liệu/file đều có Token xác thực.

#### 3. Quy tắc Dữ liệu & Bảo mật (Data Contracts)
- **Kiểm soát quyền xem File:** Chỉ trả file stream khi người dùng là: Sinh viên sở hữu Ticket, Nhân viên thuộc phòng ban thụ lý, hoặc Admin/Manager. Người khác trả về `403 FORBIDDEN_ACCESS`.
- **Audit Log:** Bảng nhật ký **Append-Only** — nghiêm cấm UPDATE hoặc DELETE trên giao diện và API.
- **Nội dung bắt buộc mỗi bản ghi Audit Log:** `user_id`, `action`, `target_id`, `old_value`, `new_value`, `ip_address`, `timestamp` (UTC/ISO-8601).

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. **Kiểm soát truy cập File:** Request `GET /api/v1/attachments/{file_id}` → AuthMiddleware verify Token → DataScopeMiddleware kiểm tra quyền sở hữu → Stream file nếu hợp lệ, trả `403` nếu vi phạm.
2. **Ghi Audit Log tự động:** Tại mỗi action quan trọng trong Service Layer, hệ thống tự động INSERT 01 bản ghi vào `audit_logs` với đầy đủ thông tin.
3. **Tra soát Audit Log:** ADMIN truy cập `/admin/audit-logs` → Lọc theo `user_id`, `action`, khoảng thời gian → Hệ thống hiển thị danh sách phân trang, chỉ cho phép Read-only.

#### 5. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Người không liên quan mở link file đính kèm → Trả về mã lỗi `403 Forbidden`.
- **AC-02:** Mọi thay đổi trạng thái Ticket đều sinh dòng Audit Log chính xác.
- **AC-03:** Admin thử tìm nút xóa nhật ký trên giao diện Audit Log → Không tồn tại chức năng chỉnh sửa hay xóa; toàn bộ dữ liệu chỉ ở dạng xem (Read-only).

---

## III. BẢNG MÃ LỖI CHUẨN DÙNG CHUNG PHÂN HỆ MANAGEMENT (SYSTEM ERROR CODES)

| HTTP Status | Error Code | Message hiển thị người dùng | Kịch bản áp dụng |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | *"Dữ liệu nhập vào không hợp lệ. Vui lòng kiểm tra lại."* | Lỗi validation trường dữ liệu đầu vào. |
| **401** | `UNAUTHORIZED` | *"Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại."* | Token hết hạn hoặc không hợp lệ. |
| **403** | `FORBIDDEN_ACCESS` | *"Bạn không có quyền truy cập vào tài nguyên này."* | Vi phạm ma trận phân quyền RBAC. |
| **403** | `ACCOUNT_DISABLED` | *"Tài khoản của bạn đã bị vô hiệu hóa. Vui lòng liên hệ Admin."* | Tài khoản bị khóa, Token bị Revoke. |
| **409** | `DUPLICATE_USER` | *"Email hoặc Mã định danh đã tồn tại trên hệ thống."* | Tạo tài khoản trùng email/user_code. |
| **500** | `INTERNAL_SERVER_ERROR` | *"Hệ thống gặp sự cố kỹ thuật. Vui lòng thử lại sau."* | Lỗi Server/Database unhandled. |
