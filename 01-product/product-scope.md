# Phạm Vi Sản Phẩm & Các Giả Định Dự Án (Product Scope & Assumptions)

## 1. Phạm Vi Chức Năng Sản Phẩm (Functional Scope)

Dự án UniSupport đóng gói trọn gói các chức năng trong **3 phân hệ chính** theo proposal và bảng chi phí nội bộ đã chốt. Thông báo nội bộ, bảo mật, phân quyền và audit log là các năng lực dùng chung được triển khai xuyên suốt trong 3 phân hệ này.

### 1.1 Module Sinh viên (Student Portal)
- **Đăng nhập**: Đăng nhập bằng tài khoản cá nhân.
- **Gửi yêu cầu hỗ trợ**:
  - Chọn Nhóm vấn đề / Phòng ban cần hỗ trợ.
  - Nhập Tiêu đề, Mô tả chi tiết vấn đề.
  - Đính kèm file minh chứng (Hỗ trợ định dạng PDF, JPG, PNG; tối đa 10MB/file).
  - Tự động sinh mã Ticket duy nhất ngay khi gửi thành công.
- **Theo dõi & Bổ sung**:
  - Tra cứu danh sách Ticket kèm trạng thái hiện tại.
  - Xem chi tiết nhật ký xử lý của nhân viên.
  - Upload bổ sung giấy tờ khi có yêu cầu từ nhân viên.
- **Kết quả & Đánh giá**:
  - Nhận thông báo và xem kết quả giải quyết chính thức.
  - Thực hiện đánh giá chất lượng phục vụ (Thang điểm 1-5 sao và nhận xét) sau khi Ticket hoàn thành.

### 1.2 Module Nhân viên (Staff Operations)
- **Danh sách công việc**: Xem danh sách Ticket Mới, Ticket Đang xử lý, Ticket Chờ sinh viên bổ sung, Ticket Quá hạn.
- **Tiếp nhận & Phân loại (Triage)**:
  - Tiếp nhận (Claim) Ticket về cá nhân hoặc Phân công (Assign) cho đồng nghiệp.
  - Điều chỉnh mức độ ưu tiên (Thấp, Trung bình, Cao, Khẩn cấp).
  - Chuyển tiếp Ticket sang Phòng ban khác kèm lý do chuyển.
- **Xử lý & Phản hồi**:
  - Gửi yêu cầu "Cần bổ sung thông tin" tới sinh viên.
  - Cập nhật trạng thái xử lý (In Progress, Resolved, Closed).
  - Soạn nội dung phản hồi kết quả giải quyết cho sinh viên.

### 1.3 Module Quản lý (Management Dashboard)
- **Dashboard tổng quan**:
  - Thống kê tổng số Ticket theo thời gian (Ngày/Tuần/Tháng).
  - Tỷ lệ Ticket đã đóng / đang xử lý / quá hạn SLA.
  - Biểu đồ khối lượng công việc theo từng Phòng ban.
- **Báo cáo & Phân tích**:
  - Thống kê top các nhóm vấn đề phát sinh nhiều nhất.
  - Thống kê Thời gian xử lý trung bình (Average Resolution Time).
  - Báo cáo chỉ số hài lòng trung bình (CSAT Score) và danh sách phản hồi.
- **Quản trị người dùng**:
  - Tạo mới, cập nhật, khóa tài khoản người dùng.
  - Gán Vai trò (Role) và Phòng ban (Department).

### 1.4 Năng lực dùng chung: Dịch vụ Thông báo (In-app Notification Service)
- Thông báo nội bộ trên giao diện web (In-app Bell Icon) khi:
  - Ticket tạo thành công.
  - Ticket thay đổi trạng thái (Đang xử lý -> Hoàn thành...).
  - Nhân viên yêu cầu bổ sung thông tin.
  - Có phản hồi mới từ sinh viên hoặc nhân viên.

### 1.5 Năng lực dùng chung: Bảo mật & Phân quyền (RBAC & Security)
- Phân quyền truy cập tài nguyên theo 3 vai trò (RBAC).
- Bảo mật đường dẫn file đính kèm (chỉ sinh viên tạo ticket và nhân viên phụ trách phòng ban mới có quyền tải/xem file).
- Ghi nhận Audit Log cho các hành động quan trọng (Đổi trạng thái, Phân công, Chuyển phòng ban, Xóa/Khóa tài khoản).

---

## 2. Giả Định Dự Án (Project Assumptions)

1. **Quy mô người dùng**: Hệ thống phục vụ khoảng **3.000 sinh viên** và khoảng **50 - 100 nhân viên/quản lý** tại Aurora University.
2. **Nền tảng vận hành**: Hệ thống là ứng dụng Web (Web Application), tối ưu hiển thị responsive cho trình duyệt PC và Thiết bị di động. Không yêu cầu xây dựng Mobile App cài đặt trên Android/iOS.
3. **Ngôn ngữ giao diện**: Giao diện người dùng hỗ trợ 2 ngôn ngữ **Tiếng Việt và Tiếng Anh** ở mức cơ bản (Static localization).
4. **Hạ tầng & Tên miền**:
   - Aurora University (Client) chịu trách nhiệm chuẩn bị và cung cấp hạ tầng máy chủ (Server/VPS), môi trường cài đặt (Node.js/Python/Database...), tên miền (Domain) và SSL.
   - Hiệu năng và độ ổn định truy cập phụ thuộc trực tiếp vào chất lượng hạ tầng do Client cung cấp.
5. **Dữ liệu ban đầu**: Client chịu trách nhiệm cung cấp danh sách phòng ban, danh sách nhân viên và dữ liệu sinh viên mẫu đúng định dạng để cấu hình ban đầu.
6. **Thời gian phê duyệt**: Lịch trình thực hiện dự án không bao gồm thời gian chờ phản hồi, góp ý hoặc phê duyệt hợp đồng/tài liệu từ phía Client. Các đợt chờ phản hồi kéo dài quá 03 ngày làm việc sẽ được cộng tương ứng vào tổng tiến độ.
7. **Tích hợp hệ thống**: Hệ thống hoạt động độc lập, không tích hợp với bất kỳ bên thứ ba nào ngoài các tính năng đã được thống nhất trong proposal.
8. **An toàn thông tin**: Dự án áp dụng các tiêu chuẩn bảo mật lập trình web cơ bản (OWASP Top 10 cơ bản, mã hóa mật khẩu, kiểm soát truy cập file). Không bao gồm chi phí chứng nhận bảo mật hoặc thuê dịch vụ Pentest độc lập.

---

## 3. Ràng Buộc Dự Án (Project Constraints)

- **Thời gian**: **14 tuần (70 ngày làm việc)** phát triển và kiểm thử nội bộ + **10 ngày làm việc** UAT chính thức của nhà trường.
- **Ngân sách**: **300.000.000 VNĐ** (Ba trăm triệu đồng chẵn).
- **Phạm vi thay đổi (Change Requests)**: Mọi yêu cầu thay đổi tính năng ngoài phạm vi đã thống nhất tại Mốc 1 (cuối Tuần 2) phải được đánh giá lại về chi phí và tiến độ bằng văn bản bổ sung.

---

## 4. Ví Dụ Chi Tiết Về Cấu Trúc Đặc Tả Yêu Cầu Chức Năng (Requirement Spec Pattern)

*Dưới đây là ví dụ minh họa chuẩn hóa theo cấu trúc đặc tả yêu cầu chức năng áp dụng cho các phân hệ của UniSupport:*

### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ

**Mô tả**  
Hệ thống cho phép sinh viên tạo một Ticket hỗ trợ bằng cách nhập thông tin mô tả vấn đề gặp phải, chọn phòng ban và đính kèm file minh chứng (nếu có), sau đó gửi yêu cầu đến bộ phận phụ trách.

**Actor**  
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**  
- Sinh viên đã đăng nhập thành công.
- Tài khoản sinh viên đang ở trạng thái hoạt động (Active) và có quyền tạo Ticket.

**Luồng chính**  
1. Sinh viên mở chức năng **Tạo Ticket**.
2. Hệ thống hiển thị form tạo Ticket.
3. Sinh viên chọn **Phòng ban / Nhóm vấn đề**, nhập **Tiêu đề** và **Mô tả chi tiết**.
4. Sinh viên đính kèm file minh chứng (nếu có, hỗ trợ PDF/PNG/JPG, tối đa 10MB).
5. Sinh viên nhấn nút **Gửi yêu cầu**.
6. Hệ thống kiểm tra tính hợp lệ của dữ liệu đầu vào.
7. Nếu dữ liệu hợp lệ, hệ thống tạo Ticket mới, sinh **Mã Ticket duy nhất** (ví dụ: `TK-20261004-001`).
8. Hệ thống lưu file đính kèm vào bộ nhớ bảo mật và liên kết với Ticket.
9. Hệ thống gửi thông báo nội bộ cho Phòng ban phụ trách.
10. Hệ thống hiển thị thông báo tạo Ticket thành công và cung cấp mã Ticket cho sinh viên.

**Business Rules**  
- Tiêu đề và Mô tả vấn đề là các trường thông tin bắt buộc.
- Nội dung chỉ chứa khoảng trắng được xem là không hợp lệ.
- Dung lượng file đính kèm không vượt quá 10MB/file; định dạng cho phép: `.pdf`, `.png`, `.jpg`, `.jpeg`.
- Một thao tác gửi của sinh viên chỉ được tạo tối đa **một Ticket**, kể cả khi nhấn nút gửi nhiều lần do double-click, gián đoạn mạng hoặc ấn retry.
- Ticket sau khi tạo phải được liên kết cố định với mã tài khoản của sinh viên gửi yêu cầu.

**Alternative / Error Flows**  
- **Thiếu thông tin bắt buộc**: Hệ thống không tạo Ticket, đánh dấu đỏ trường thiếu và hiển thị thông báo yêu cầu sinh viên bổ sung thông tin.
- **File đính kèm không hợp lệ (sai định dạng hoặc >10MB)**: Hệ thống hiển thị lỗi cụ thể bên dưới ô upload file và dừng quá trình gửi.
- **Tạo Ticket thất bại do lỗi hệ thống/database**: Hệ thống thông báo lỗi, hoàn tác transaction và không lưu Ticket ở trạng thái dữ liệu không hoàn chỉnh.
- **Gửi lại do sự cố mạng (Retry/Double click)**: Hệ thống chặn trùng lặp bằng cơ chế Idempotency/Debounce, không tạo thêm Ticket trùng.

**Acceptance Criteria**  
- **AC-01**: Sinh viên nhập đầy đủ thông tin hợp lệ và chọn **Gửi yêu cầu** -> Hệ thống tạo đúng 01 Ticket với mã định danh duy nhất và hiển thị thông báo thành công.
- **AC-02**: Sinh viên để trống trường Tiêu đề hoặc Mô tả -> Hệ thống không tạo Ticket và hiển thị lỗi validation tại trường tương ứng.
- **AC-03**: Sinh viên chọn file đính kèm dạng `.exe` hoặc dung lượng 15MB -> Hệ thống từ chối file và hiển thị cảnh báo định dạng/dung lượng.
- **AC-04**: Sinh viên nhấn nút **Gửi yêu cầu** nhiều lần liên tiếp trong thời gian ngắn -> Hệ thống chỉ tạo duy nhất 01 Ticket.
- **AC-05**: Ticket được tạo lưu đúng thông tin tài khoản sinh viên gửi, thời gian tạo và hiển thị đúng trong danh sách Ticket của sinh viên.

**Ví dụ Edge Case**  
*Sinh viên nhấn nút **Gửi yêu cầu** 5 lần liên tiếp trong khoảng thời gian 1 giây do mạng lag.*  
-> **Expected Result**: Hệ thống xử lý request đầu tiên, khóa nút bấm (Disable submit button), tạo duy nhất **01 Ticket** trong cơ sở dữ liệu và hiển thị thông báo thành công cho sinh viên.
