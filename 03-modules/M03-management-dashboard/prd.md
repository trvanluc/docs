# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Quản Trị & Báo Cáo (PRD - M03 Admin & Management Dashboard)

## 1. Tổng Quan Phân Hệ

Phân hệ **Quản trị & Báo cáo (Admin & Management Dashboard)** là trung tâm điều hành và kiểm soát toàn diện dành cho Ban Giám hiệu, Trưởng/Phó các Phòng ban chức năng và Quản trị viên hệ thống (Admin) tại **Aurora University**. Phân hệ đảm nhiệm công tác quản trị tài khoản, phân quyền RBAC, quản lý danh mục phòng ban, kiểm soát an toàn dữ liệu, giám sát KPI thời gian thực và trích xuất báo cáo phân tích.

### Danh mục Chức năng & Phân bổ Công sức (Tổng: 215h)

| Mã Chức Năng | Tên Chức Năng | Phạm Vi Nghiệp Vụ | Effort Cơ Sở | Buffer | Effort Kế Hoạch |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **FR-ADM-01** | Quản lý tài khoản, vai trò & RBAC | Vòng đời tài khoản, xác thực mã hóa, phân quyền 4 vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`). | 60h | 4h | **64h** |
| **FR-ADM-02** | Quản lý phòng ban & danh mục | Cấu hình cơ cấu phòng ban, danh mục nhóm vấn đề và luồng tiếp nhận ban đầu. | 26h | 0h | **26h** |
| **FR-ADM-03** | Kiểm soát quyền truy cập & Audit Trail | Kiểm soát quyền truy cập tài nguyên/file qua API Proxy, lưu vết nhật ký bất biến. | 36h | 4h | **40h** |
| **FR-ADM-04** | Quản lý thời hạn lưu trữ | Thiết lập chính sách lưu trữ (Retention), dọn dẹp file tạm, archiving dữ liệu cũ. | 15h | 0h | **15h** |
| **FR-ADM-05** | Dashboard & thống kê quản trị | Thẻ chỉ số KPI thời gian thực, biểu đồ khối lượng công việc và cảnh báo quá hạn. | 33h | 0h | **33h** |
| **FR-ADM-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | Báo cáo thời gian xử lý SLA trung bình, xu hướng sự cố, tổng hợp CSAT, xuất Excel/CSV. | 37h | 0h | **37h** |
| **TỔNG CỘNG** | | | **207h** | **8h** | **215h** |

---

## 2. Đặc Tả Chi Tiết Chức Năng

### [FR-ADM-01] Quản lý tài khoản, vai trò & RBAC

**Mô tả**  
Quản lý toàn bộ vòng đời tài khoản người dùng trong hệ thống (tạo mới, cập nhật, khóa/mở khóa), xử lý xác thực đăng nhập an toàn và gán phân quyền theo vai trò (Role-Based Access Control).

**Actor**  
Quản trị viên hệ thống (Admin).

**Preconditions**  
Người dùng đăng nhập bằng tài khoản có vai trò `ADMIN`.

**Luồng chính**  
1. Admin truy cập mục **Quản lý tài khoản**.
2. Hệ thống hiển thị danh sách người dùng kèm vai trò và trạng thái hoạt động.
3. **Tạo tài khoản mới:** Admin nhập Họ tên, Email, Mã định danh (Mã SV / Mã NV), Mật khẩu khởi tạo, chọn Vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`) và chọn Phòng ban trực thuộc (đối với Staff).
4. **Khóa / Mở khóa tài khoản:** Admin chọn tài khoản cần thay đổi trạng thái, nhập lý do và bấm xác nhận.
5. Hệ thống mã hóa mật khẩu một chiều (Argon2/Bcrypt), lưu bản ghi và gửi thông tin xác thực cho người dùng.
6. Ghi nhận lịch sử thao tác vào Audit Log.

**Business Rules**  
- Email và Mã định danh là duy nhất trong toàn hệ thống.
- Khi tài khoản bị khóa (`INACTIVE`), hệ thống lập tức thu hồi phiên làm việc (Revoke Token) và ngăn chặn đăng nhập tiếp theo.
- Tài khoản có vai trò `STAFF` bắt buộc phải thuộc về ít nhất 01 Phòng ban chuyên trách.

**Alternative / Error Flows**  
- **Trùng Email hoặc Mã định danh**: Báo lỗi "Email hoặc Mã định danh đã tồn tại trên hệ thống".
- **Admin tự khóa chính mình**: Hệ thống chặn hành động và hiển thị cảnh báo không được phép.

**Acceptance Criteria**  
- **AC-01**: Tạo tài khoản mới thành công, đăng nhập kiểm tra đúng vai trò và phạm vi dữ liệu.
- **AC-02**: Khóa tài khoản -> Người dùng bị đăng xuất ngay lập tức ở thao tác tiếp theo.

**Ví dụ Edge Case**  
Admin đổi vai trò của một Nhân viên từ `STAFF` sang `MANAGER`.  
-> **Expected Result**: Nhân viên truy cập được thêm các báo cáo quản trị của phòng ban mà không cần tạo tài khoản mới.

---

### [FR-ADM-02] Quản lý phòng ban & danh mục

**Mô tả**  
Cho phép cấu hình danh sách các Phòng ban chuyên trách tại Aurora University và danh mục nhóm vấn đề / dịch vụ hỗ trợ trực thuộc.

**Actor**  
Quản trị viên hệ thống (Admin).

**Preconditions**  
Admin đã đăng nhập hệ thống.

**Luồng chính**  
1. Admin vào mục **Phòng ban & Danh mục**.
2. Hệ thống hiển thị cây phân cấp: Phòng ban -> Nhóm vấn đề (Category) -> Loại yêu cầu cụ thể (Subcategory).
3. Admin có thể thêm mới, sửa tên, đổi trưởng bộ phận hoặc ẩn/hiện một nhóm vấn đề.
4. Admin thiết lập thời hạn cam kết SLA mặc định cho từng loại yêu cầu (ví dụ: Cấp bảng điểm: 48h; Xác nhận sinh viên: 24h).
5. Nhấn **Lưu cấu hình**. Hệ thống áp dụng ngay cho các Ticket tạo mới từ thời điểm đó.

**Business Rules**  
- Không cho phép xóa cứng (Hard delete) phòng ban đã có Ticket phát sinh trong lịch sử; chỉ cho phép chuyển sang trạng thái ẩn (Inactive).

**Alternative / Error Flows**  
- **Tạo trùng tên phòng ban**: Báo lỗi tên phòng ban đã tồn tại.

**Acceptance Criteria**  
- **AC-01**: Thêm nhóm vấn đề mới -> Hiển thị ngay trên form gửi yêu cầu của sinh viên.
- **AC-02**: Ẩn phòng ban -> Sinh viên không còn chọn được phòng ban đó khi tạo Ticket mới.

**Ví dụ Edge Case**  
Admin cập nhật thời hạn SLA của dịch vụ "Xác nhận thực tập" từ 48h xuống 24h.  
-> **Expected Result**: Các Ticket mới tạo sẽ áp dụng mốc 24h; các Ticket đã tạo trước đó giữ nguyên hạn cũ.

---

### [FR-ADM-03] Kiểm soát quyền truy cập & Audit Trail

**Mô tả**  
Kiểm soát an toàn dữ liệu và bảo mật tệp đính kèm thông qua Secured API Proxy, đồng thời ghi nhận nhật ký tra soát bất biến (Append-only Audit Log) cho toàn bộ các hành động trọng yếu.

**Actor**  
Quản trị viên / Toàn bộ người dùng / Hệ thống.

**Preconditions**  
Mọi yêu cầu truy xuất dữ liệu/file đều có Token xác thực.

**Luồng chính**  
1. **Kiểm soát truy cập API & File:**
   - Khi có request tải file: `GET /api/v1/attachments/{id}/download`.
   - Backend xác minh Token và kiểm tra quyền sở hữu (Chỉ sinh viên tạo Ticket, nhân viên phòng ban thụ lý hoặc Admin mới được tải).
   - Nếu vi phạm -> Trả lỗi HTTP `403 Forbidden`.
2. **Ghi nhận Audit Log:**
   - Mỗi khi diễn ra hành động: Đổi trạng thái Ticket, Chuyển phòng ban, Phân công nhân viên, Khóa tài khoản.
   - Hệ thống tự động ghi bản ghi vào bảng `audit_logs`: `user_id`, `action`, `resource_id`, `old_value`, `new_value`, `ip_address`, `timestamp` (UTC).
3. **Tra soát nhật ký:** Admin mở màn hình Audit Log để xem và lọc lịch sử khi cần kiểm tra.

**Business Rules**  
- Bảng nhật ký `audit_logs` tuân thủ quy tắc `BR-AUD-01`: Chỉ ghi thêm (Append-only), không có chức năng sửa hoặc xóa trên giao diện hay API.
- Nghiêm cấm đặt thư mục upload file ở chế độ công khai tĩnh (Public static URL).

**Alternative / Error Flows**  
- **Truy cập file trái phép**: Chặn truy cập và ghi nhận cảnh báo an ninh.

**Acceptance Criteria**  
- **AC-01**: Người không liên quan mở link file đính kèm -> Trả về mã lỗi `403 Forbidden`.
- **AC-02**: Mọi thay đổi trạng thái Ticket đều sinh dòng Audit Log chính xác trong vòng 100ms.

**Ví dụ Edge Case**  
Admin thử tìm nút xóa nhật ký trên giao diện Audit Log.  
-> **Expected Result**: Không tồn tại chức năng chỉnh sửa hay xóa; toàn bộ dữ liệu chỉ ở dạng xem (Read-only).

---

### [FR-ADM-04] Quản lý thời hạn lưu trữ

**Mô tả**  
Thiết lập chính sách lưu trữ dữ liệu (Data Retention Policy), dọn dẹp các tệp tạm/tệp mồ côi (Orphan files) và lưu trữ định kỳ các Ticket đã đóng hoàn tất lâu ngày nhằm tối ưu dung lượng máy chủ.

**Actor**  
Quản trị viên hệ thống (Admin).

**Preconditions**  
Admin truy cập cấu hình hệ thống.

**Luồng chính**  
1. Admin vào mục **Chính sách lưu trữ dữ liệu**.
2. Cấu hình các tham số:
   - Thời gian lưu trữ Ticket hoạt động (ví dụ: 12 tháng).
   - Thời gian dọn dẹp file tạm upload dở dang (ví dụ: sau 24 giờ không gắn vào Ticket).
3. Admin có thể kích hoạt tác vụ quét và tối ưu dung lượng theo yêu cầu.
4. Hệ thống thực hiện dọn dẹp an toàn các tệp rác và nén lưu trữ dữ liệu cũ.

**Business Rules**  
- Chỉ dọn dẹp các file tạm mồ côi không gắn với bất kỳ Ticket hợp lệ nào.
- Tuyệt đối không xóa dữ liệu Ticket và Audit Log khi chưa có sự xác nhận chính thức từ nhà trường.

**Acceptance Criteria**  
- **AC-01**: Tác vụ dọn dẹp file tạm quét và xóa đúng các file mồ côi, thu hồi dung lượng đĩa.
- **AC-02**: Cấu hình thời hạn lưu trữ được ghi nhận và hoạt động đúng chu kỳ.

**Ví dụ Edge Case**  
Sinh viên upload ảnh nhưng sau đó hủy không gửi Ticket.  
-> **Expected Result**: File tạm mồ côi đó được hệ thống tự động dọn dẹp sau 24h để tránh rác dung lượng.

---

### [FR-ADM-05] Dashboard & thống kê quản trị

**Mô tả**  
Cung cấp màn hình Dashboard tổng quan hiển thị các thẻ chỉ số KPI vận hành và biểu đồ trực quan theo thời gian thực cho Ban Giám hiệu và Trưởng phòng ban.

**Actor**  
Quản lý phòng ban / Ban Giám hiệu / Admin.

**Preconditions**  
Người dùng đăng nhập tài khoản có vai trò `MANAGER` hoặc `ADMIN`.

**Luồng chính**  
1. Người dùng truy cập **Dashboard Tổng quan**.
2. Hệ thống tải và hiển thị các thẻ KPI cốt lõi:
   - **Tổng số yêu cầu tiếp nhận**: Phân bổ theo khoảng thời gian.
   - **Đang xử lý**: Số Ticket đang trong luồng vận hành.
   - **Quá hạn SLA**: Số Ticket chưa hoàn thành đã vượt mốc cam kết.
   - **Điểm CSAT trung bình**: Chỉ số hài lòng chung của toàn trường/phòng ban.
3. Hiển thị biểu đồ phân bổ trạng thái (Pie Chart) và biểu đồ khối lượng công việc theo phòng ban (Bar Chart).
4. Người dùng thay đổi bộ lọc thời gian ("Hôm nay", "Tuần này", "Tháng này", "Tùy chọn").
5. Toàn bộ số liệu và biểu đồ tự động cập nhật lại tương ứng.

**Business Rules**  
- Phân vùng dữ liệu: Trưởng phòng chỉ xem số liệu thuộc Phòng ban của mình; Ban Giám hiệu và Admin xem toàn trường.

**Acceptance Criteria**  
- **AC-01**: Thẻ chỉ số hiển thị chính xác số lượng Ticket thực tế theo thời gian thực.
- **AC-02**: Bấm vào thẻ "Quá hạn SLA" -> Điều hướng sang danh sách chi tiết các Ticket quá hạn.

**Ví dụ Edge Case**  
Một Ticket hết hạn lúc 14:00. Lúc 14:01 Quản lý xem Dashboard.  
-> **Expected Result**: Thẻ chỉ số Quá hạn SLA tự động tăng thêm 1 đơn vị.

---

### [FR-ADM-06] Báo cáo, mức độ hài lòng & xuất dữ liệu

**Mô tả**  
Cung cấp các báo cáo chuyên sâu về Thời gian giải quyết trung bình (SLA Performance), Xu hướng nhóm vấn đề phát sinh, Tổng hợp đánh giá và nhận xét CSAT, cùng tính năng Xuất báo cáo dạng file (Excel/CSV).

**Actor**  
Quản lý / Ban Giám hiệu / Admin.

**Preconditions**  
Người dùng có quyền xem báo cáo.

**Luồng chính**  
1. Người dùng truy cập mục **Báo cáo & Thống kê**.
2. Chọn loại báo cáo:
   - **Báo cáo Thời gian xử lý**: Thống kê thời gian giải quyết trung bình theo từng phòng ban/chuyên viên.
   - **Báo cáo Xu hướng sự cố**: Top 5 nhóm vấn đề sinh viên gặp phải nhiều nhất.
   - **Báo cáo Mức độ hài lòng CSAT**: Phổ điểm đánh giá sao (1-5 sao) và danh sách nhận xét chi tiết.
3. Chọn các tiêu chí lọc (Phòng ban, Khoảng ngày bắt đầu - kết thúc).
4. Nhấn nút **Xuất báo cáo** để tải file Excel/CSV về máy tính.

**Business Rules**  
- Thời gian xử lý thực tế của một Ticket được tính bằng thời gian từ lúc tạo đến lúc `RESOLVED`, đã loại trừ khoảng thời gian tạm dừng ở `WAITING_STUDENT`.
- Báo cáo CSAT chỉ tính toán trên các Ticket đã có đánh giá từ sinh viên.

**Alternative / Error Flows**  
- **Chọn khoảng ngày không hợp lệ (Ngày kết thúc trước Ngày bắt đầu)**: Hệ thống báo lỗi và yêu cầu chọn lại.

**Acceptance Criteria**  
- **AC-01**: Báo cáo tính đúng thời gian xử lý trung bình và tỷ lệ hài lòng CSAT.
- **AC-02**: Xuất file Excel/CSV chuẩn định dạng tiếng Việt UTF-8, đầy đủ cột dữ liệu.

**Ví dụ Edge Case**  
Trong tháng có 200 Ticket, trong đó 150 Ticket đánh giá 5 sao và 50 Ticket đánh giá 4 sao.  
-> **Expected Result**: Điểm CSAT trung bình hiển thị chính xác là `4.75 / 5.0 sao`.