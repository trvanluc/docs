# PRD - M03 Management Dashboard

## 1. Scope summary

Management Dashboard phục vụ nhóm quản lý theo dõi tình hình Ticket, workload, xu hướng, thời gian xử lý, feedback sinh viên và quản trị account/permission theo phạm vi được cấp.

| Internal effort package | Effort | Scope status |
| :--- | :---: | :--- |
| Quản lý tài khoản, vai trò & RBAC | 64h | Baseline/Derived |
| Quản lý phòng ban & danh mục | 26h | Derived |
| Kiểm soát quyền truy cập & Audit Trail | 40h | Baseline/Derived |
| Quản lý thời hạn lưu trữ | 15h | Proposed/TBD |
| Dashboard & thống kê quản trị | 33h | Baseline |
| Báo cáo, mức độ hài lòng & xuất dữ liệu | 37h | Baseline/Proposed |
| **Tổng M3 - Management** | **215h** | Internal planning |

## 2. Functional requirements

### FR-MGT-01 - Login

- **Status**: Baseline
- **Actor**: Management
- **Description / Goal**: Management đăng nhập để truy cập dashboard, báo cáo và chức năng quản trị được cấp quyền.
- **Preconditions**: User có role `MANAGEMENT`.
- **Inputs**: Username/email và mật khẩu.
- **Main Flow**: User mở login, nhập thông tin, hệ thống xác thực và mở Management Dashboard.
- **Alternative/Error Flow**: User không có role/permission phù hợp bị từ chối.
- **Business Rules References**: BR-ACC-03.
- **Output/Postcondition**: Management thấy dữ liệu trong phạm vi được cấp.
- **Acceptance Criteria**: Login hợp lệ thành công; Student/Staff không có quyền không truy cập được.
- **Related Workflow**: N/A
- **Related Test Scenario**: TS-MGT-01-01, TS-MGT-01-02

### FR-MGT-02 - Dashboard Overview

- **Status**: Baseline
- **Actor**: Management
- **Description / Goal**: Management xem tổng quan số lượng Ticket mới, đang xử lý, sắp quá hạn/quá hạn.
- **Preconditions**: Management đã login.
- **Inputs**: Khoảng thời gian/phạm vi xem nếu có.
- **Main Flow**:
  1. Management mở Dashboard.
  2. Hệ thống hiển thị các chỉ số tổng quan theo phạm vi quyền.
  3. Management đổi filter thời gian/phòng ban nếu có.
- **Alternative/Error Flow**: Không có dữ liệu thì hiển thị empty state, không báo lỗi.
- **Business Rules References**: BR-ACC-03.
- **Output/Postcondition**: Management nắm tình trạng vận hành tổng quan.
- **Acceptance Criteria**: Dashboard không hiển thị dữ liệu ngoài phạm vi; số liệu đổi theo filter.
- **Related Workflow**: N/A
- **Related Test Scenario**: TS-MGT-02-01

### FR-MGT-03 - Workload Monitoring

- **Status**: Baseline
- **Actor**: Management
- **Description / Goal**: Management theo dõi workload theo phòng ban hoặc nhân viên.
- **Preconditions**: Có dữ liệu Ticket trong hệ thống.
- **Inputs**: Filter phòng ban/nhân viên/khoảng thời gian.
- **Main Flow**: Management chọn filter, hệ thống hiển thị số lượng Ticket theo phòng ban/nhân viên và trạng thái.
- **Alternative/Error Flow**: Phòng ban/nhân viên không có Ticket thì hiển thị 0.
- **Business Rules References**: BR-ACC-03.
- **Output/Postcondition**: Management nhận diện workload để điều phối.
- **Acceptance Criteria**: Workload tính theo Ticket thuộc phạm vi được chọn và tôn trọng quyền xem.
- **Related Workflow**: N/A
- **Related Test Scenario**: TS-MGT-03-01

### FR-MGT-04 - Reports & Statistics

- **Status**: Baseline; export Proposed
- **Actor**: Management
- **Description / Goal**: Management xem báo cáo xu hướng, thời gian xử lý trung bình và tổng hợp feedback sinh viên.
- **Preconditions**: Có dữ liệu Ticket/history/rating.
- **Inputs**: Loại báo cáo, khoảng thời gian, phòng ban/nhân viên/category nếu có.
- **Main Flow**:
  1. Management mở Reports.
  2. Management chọn loại báo cáo và filter.
  3. Hệ thống hiển thị bảng/biểu đồ.
- **Alternative/Error Flow**: Date range không hợp lệ thì báo lỗi validation.
- **Business Rules References**: BR-RAT-01, BR-HIS-01.
- **Output/Postcondition**: Management có dữ liệu phục vụ đánh giá chất lượng hỗ trợ.
- **Acceptance Criteria**: Báo cáo thời gian xử lý và feedback chỉ tính trên dữ liệu hợp lệ; filter hoạt động đúng.
- **Related Workflow**: N/A
- **Related Test Scenario**: TS-MGT-04-01, TS-MGT-04-02

### FR-MGT-05 - Account Management

- **Status**: Baseline
- **Actor**: Management có permission quản trị account
- **Description / Goal**: Tạo/chỉnh sửa account người dùng theo proposal.
- **Preconditions**: User đã login với role `MANAGEMENT` và permission phù hợp.
- **Inputs**: Thông tin account cần tạo/chỉnh sửa. Import từ Excel là TBD.
- **Main Flow**:
  1. Management mở User Management.
  2. Management tạo hoặc chỉnh sửa account.
  3. Hệ thống validate và lưu thay đổi.
  4. Hệ thống ghi history/audit.
- **Alternative/Error Flow**: Trùng định danh/email hoặc thiếu thông tin bắt buộc thì bị chặn.
- **Business Rules References**: BR-HIS-01.
- **Output/Postcondition**: Account được tạo/chỉnh sửa.
- **Acceptance Criteria**: Account hợp lệ được lưu; thao tác quản trị được ghi history.
- **Related Workflow**: N/A
- **Related Test Scenario**: TS-MGT-05-01, TS-MGT-05-02

### FR-MGT-06 - Role/Permission Management

- **Status**: Baseline
- **Actor**: Management có permission quản trị quyền
- **Description / Goal**: Gán quyền theo vai trò và phạm vi phù hợp.
- **Preconditions**: User có permission quản trị quyền.
- **Inputs**: User, role baseline (`STUDENT`, `STAFF`, `MANAGEMENT`) và phạm vi phòng ban nếu cần.
- **Main Flow**:
  1. Management chọn user.
  2. Management gán role/phạm vi.
  3. Hệ thống validate role model và lưu thay đổi.
  4. Hệ thống ghi history/audit.
- **Alternative/Error Flow**: Role/phạm vi không hợp lệ thì không lưu.
- **Business Rules References**: BR-ACC-01, BR-ACC-02, BR-ACC-03, BR-HIS-01.
- **Output/Postcondition**: User có quyền đúng vai trò/phạm vi.
- **Acceptance Criteria**: Role được lưu theo đúng model 3 role; quyền mới ảnh hưởng tới lần truy cập sau.
- **Related Workflow**: N/A
- **Related Test Scenario**: TS-MGT-06-01, TS-MGT-06-02

### FR-MGT-P01 - Department/Category Management

- **Status**: Derived/Proposed
- **Description / Goal**: Quản lý danh mục phòng ban/category để hỗ trợ phân loại Ticket.
- **Reason**: Cần cho vận hành thực tế nhưng proposal chưa mô tả chi tiết giao diện quản trị danh mục.

### FR-MGT-P02 - Export Data

- **Status**: Proposed/TBD
- **Description / Goal**: Xuất dữ liệu báo cáo ra file.
- **Reason**: Có thể hữu ích cho quản lý, nhưng proposal chỉ nêu xem báo cáo/tổng hợp.

### FR-MGT-P03 - Retention Management

- **Status**: Proposed/TBD
- **Description / Goal**: Cấu hình thời hạn lưu trữ Ticket/file/log.
- **Reason**: Có trong effort nội bộ, chưa có baseline từ proposal.
