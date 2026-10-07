# PRD - M02 Staff Operations

## 1. Scope summary

Staff Operations hỗ trợ nhân viên/phòng ban xem Ticket mới hoặc được giao, phân loại, xem xét ưu tiên, chuyển xử lý, cập nhật trạng thái, yêu cầu bổ sung, ghi nhận kết quả và đóng Ticket.

| Internal effort package | Effort | Scope status |
| :--- | :---: | :--- |
| Tiếp nhận, tìm kiếm & lọc yêu cầu | 33h | Baseline/Derived |
| Phân loại & phân công xử lý | 38h | Baseline/Derived |
| Quản lý ưu tiên & thời hạn | 29h | Baseline/TBD |
| Xử lý & cập nhật yêu cầu | 39h | Baseline |
| Chuyển xử lý, Escalation & hoàn tất | 32h | Baseline/Proposed |
| Đóng & mở lại yêu cầu | 26h | Baseline/Proposed |
| **Tổng M2 - Staff** | **197h** | Internal planning |

## 2. Functional requirements

### FR-STA-01 - Login

- **Status**: Baseline
- **Actor**: Staff
- **Description / Goal**: Staff đăng nhập để xem và xử lý Ticket trong phạm vi được phân quyền.
- **Preconditions**: Staff có account hợp lệ.
- **Inputs**: Username/email/mã nhân viên và mật khẩu.
- **Main Flow**: Staff mở login, nhập thông tin, hệ thống xác thực và mở Staff Operations.
- **Alternative/Error Flow**: Sai thông tin hoặc không có role `STAFF`/permission phù hợp thì bị từ chối.
- **Business Rules References**: BR-ACC-02.
- **Output/Postcondition**: Staff thấy queue theo phạm vi được giao.
- **Acceptance Criteria**: Đăng nhập hợp lệ thành công; user không có quyền Staff không truy cập được Staff Operations.
- **Related Workflow**: WF-02, WF-03, WF-04, WF-05
- **Related Test Scenario**: TS-STA-01-01, TS-STA-01-02

### FR-STA-02 - View/Search/Filter Ticket Queue

- **Status**: View queue Baseline; search/filter Derived
- **Actor**: Staff
- **Description / Goal**: Staff xem Ticket mới/Ticket được giao và tìm nhanh Ticket cần xử lý.
- **Preconditions**: Staff đã login.
- **Inputs**: Queue type, status filter, category/department/assignee filter, keyword nếu triển khai.
- **Main Flow**:
  1. Staff mở queue.
  2. Hệ thống hiển thị Ticket thuộc phạm vi Staff.
  3. Staff lọc/tìm kiếm nếu cần.
  4. Staff mở chi tiết Ticket.
- **Alternative/Error Flow**: Không có Ticket thì hiển thị empty state.
- **Business Rules References**: BR-ACC-02.
- **Output/Postcondition**: Staff chọn được Ticket cần xử lý.
- **Acceptance Criteria**: Queue không hiển thị Ticket ngoài phạm vi; filter không làm mất quyền truy cập.
- **Related Workflow**: WF-02
- **Related Test Scenario**: TS-STA-02-01, TS-STA-02-02

### FR-STA-03 - Classify Ticket

- **Status**: Baseline
- **Actor**: Staff
- **Description / Goal**: Staff kiểm tra nội dung và phân loại Ticket theo nhóm vấn đề phù hợp.
- **Preconditions**: Ticket thuộc phạm vi Staff.
- **Inputs**: Category/sub-category nếu có.
- **Main Flow**: Staff mở Ticket, xem mô tả/attachment, cập nhật classification và lưu.
- **Alternative/Error Flow**: Staff không có quyền hoặc Ticket đã đóng thì không cho sửa classification.
- **Business Rules References**: BR-HIS-01.
- **Output/Postcondition**: Ticket có classification phục vụ xử lý/báo cáo.
- **Acceptance Criteria**: Classification được lưu và hiển thị lại trong Ticket/history.
- **Related Workflow**: WF-02
- **Related Test Scenario**: TS-STA-03-01

### FR-STA-04 - Assign / Transfer Ticket

- **Status**: Baseline
- **Actor**: Staff có permission phù hợp
- **Description / Goal**: Staff tự nhận, phân công hoặc chuyển Ticket sang phòng ban/người phụ trách khác khi cần.
- **Preconditions**: Ticket ở `NEW` hoặc `IN_PROGRESS`, thuộc phạm vi Staff.
- **Inputs**: Assignee hoặc department/person đích; lý do chuyển là TBD.
- **Main Flow - Claim/Assign**:
  1. Staff chọn Ticket trong queue.
  2. Staff claim hoặc assign cho Staff phù hợp.
  3. Hệ thống gán assignee và chuyển Ticket sang `IN_PROGRESS`.
- **Main Flow - Transfer**:
  1. Staff chọn transfer.
  2. Staff chọn đơn vị/người phụ trách mới.
  3. Hệ thống cập nhật phạm vi xử lý, clear assignee, chuyển Ticket về `NEW` và lưu history.
- **Alternative/Error Flow**:
  - Hai Staff claim cùng lúc: chỉ một thao tác thành công.
  - Chọn phòng ban/người phụ trách không hợp lệ thì bị chặn.
- **Business Rules References**: BR-XFR-01, BR-XFR-02, BR-XFR-03.
- **Output/Postcondition**: Ticket có assignee hoặc quay lại queue mới sau transfer.
- **Acceptance Criteria**: Claim/assign đúng phạm vi; transfer clear assignee và Ticket xuất hiện ở queue mới.
- **Related Workflow**: WF-02, WF-04
- **Related Test Scenario**: TS-STA-04-01, TS-STA-04-02

### FR-STA-05 - Manage Priority & Deadline

- **Status**: Baseline/TBD
- **Actor**: Staff
- **Description / Goal**: Staff xem xét mức độ ưu tiên và theo dõi Ticket sắp/quá hạn.
- **Preconditions**: Ticket thuộc phạm vi Staff.
- **Inputs**: Priority/deadline rule theo cấu hình đã xác nhận.
- **Main Flow**: Staff xem hoặc cập nhật priority; hệ thống hiển thị deadline/overdue nếu rule đã cấu hình.
- **Alternative/Error Flow**: Nếu chưa có SLA config, hệ thống không tự tính deadline và hiển thị trạng thái TBD/config missing cho quản trị.
- **Business Rules References**: SLA/priority là TBD trong terminology và BR-SUP-03.
- **Output/Postcondition**: Ticket có thông tin ưu tiên/hạn xử lý nếu đã chốt rule.
- **Acceptance Criteria**: Khi SLA config tồn tại, Ticket sắp/quá hạn được hiển thị đúng; khi chưa config, không tự bịa deadline.
- **Related Workflow**: WF-02, WF-05
- **Related Test Scenario**: TS-STA-05-01

### FR-STA-06 - Process & Update Ticket Status

- **Status**: Baseline
- **Actor**: Staff
- **Description / Goal**: Staff cập nhật tiến độ xử lý trong Ticket để Student/Management theo dõi.
- **Preconditions**: Ticket đang `IN_PROGRESS` và thuộc phạm vi Staff.
- **Inputs**: Nội dung cập nhật trạng thái/ghi chú xử lý.
- **Main Flow**: Staff nhập cập nhật, hệ thống lưu history và hiển thị cho các bên liên quan theo quyền.
- **Alternative/Error Flow**: Nội dung rỗng hoặc Staff không có quyền thì bị chặn.
- **Business Rules References**: BR-HIS-01.
- **Output/Postcondition**: Ticket history có cập nhật mới.
- **Acceptance Criteria**: Cập nhật hợp lệ được lưu; Student thấy cập nhật công khai liên quan.
- **Related Workflow**: WF-05
- **Related Test Scenario**: TS-STA-06-01

### FR-STA-07 - Request Additional Information

- **Status**: Baseline
- **Actor**: Staff
- **Description / Goal**: Staff yêu cầu Student bổ sung thông tin/giấy tờ.
- **Preconditions**: Ticket đang `IN_PROGRESS`.
- **Inputs**: Nội dung yêu cầu bổ sung.
- **Main Flow**:
  1. Staff nhập yêu cầu bổ sung.
  2. Hệ thống lưu yêu cầu vào history.
  3. Hệ thống chuyển Ticket sang `WAITING_STUDENT`.
  4. Hệ thống tạo notification cho Student.
- **Alternative/Error Flow**: Nội dung yêu cầu rỗng thì không gửi.
- **Business Rules References**: BR-SUP-01.
- **Output/Postcondition**: Ticket chờ Student bổ sung.
- **Acceptance Criteria**: Status chuyển đúng; Student nhận thấy yêu cầu bổ sung.
- **Related Workflow**: WF-03
- **Related Test Scenario**: TS-STA-07-01, TS-STA-07-02

### FR-STA-08 - Record Resolution

- **Status**: Baseline
- **Actor**: Staff
- **Description / Goal**: Staff ghi nhận kết quả xử lý Ticket.
- **Preconditions**: Ticket đang `IN_PROGRESS` và đã có đủ thông tin xử lý.
- **Inputs**: Resolution note, attachment kết quả nếu có.
- **Main Flow**: Staff nhập kết quả, hệ thống lưu resolution, chuyển Ticket sang `RESOLVED`, ghi history và thông báo Student.
- **Alternative/Error Flow**: Resolution note rỗng thì không chuyển trạng thái.
- **Business Rules References**: BR-RES-01, BR-HIS-01.
- **Output/Postcondition**: Ticket có resolution và ở `RESOLVED`.
- **Acceptance Criteria**: Resolution hợp lệ được lưu; Student xem được kết quả theo quyền.
- **Related Workflow**: WF-05
- **Related Test Scenario**: TS-STA-08-01, TS-STA-08-02

### FR-STA-09 - Close Ticket

- **Status**: Baseline; auto-close/reopen Proposed/TBD
- **Actor**: Staff hoặc System rule đã xác nhận
- **Description / Goal**: Đóng Ticket sau khi đã có kết quả xử lý.
- **Preconditions**: Ticket đang `RESOLVED`.
- **Inputs**: Xác nhận đóng Ticket hoặc rule đóng được xác nhận.
- **Main Flow**: Staff/System đóng Ticket, hệ thống chuyển status sang `CLOSED`, lưu history và cho Student xem kết quả/rating.
- **Alternative/Error Flow**: Ticket chưa có resolution thì không được đóng.
- **Business Rules References**: BR-CLS-01, BR-RAT-01.
- **Output/Postcondition**: Ticket ở `CLOSED`.
- **Acceptance Criteria**: Chỉ Ticket `RESOLVED` được đóng; Ticket `CLOSED` không còn xử lý theo baseline.
- **Related Workflow**: WF-05, WF-06
- **Related Test Scenario**: TS-STA-09-01, TS-STA-09-02

### FR-STA-P01 - Reopen / Advanced Escalation

- **Status**: Proposed/TBD
- **Reason**: Có trong effort nội bộ ở dạng mở lại/escalation nhưng proposal chưa mô tả chi tiết.
- **Decision needed**: Product Owner/Client xác nhận có triển khai trong MVP hay không.
