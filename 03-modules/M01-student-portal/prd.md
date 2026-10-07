# PRD - M01 Student Portal

## 1. Scope summary

Student Portal cho phép sinh viên đăng nhập, tạo yêu cầu hỗ trợ, theo dõi tiến độ, bổ sung thông tin khi được yêu cầu, nhận thông báo, xem kết quả và đánh giá mức độ hài lòng sau khi Ticket hoàn tất.

| Internal effort package | Effort | Scope status |
| :--- | :---: | :--- |
| Tra cứu hướng dẫn & FAQ | 14h | Proposed |
| Tạo & gửi yêu cầu hỗ trợ | 37h | Baseline |
| Xem & theo dõi yêu cầu | 33h | Baseline |
| Nhận thông báo trạng thái | 19h | Derived |
| Bổ sung thông tin & phản hồi | 25h | Baseline |
| **Tổng M1 - Student** | **128h** | Internal planning |

## 2. Functional requirements

### FR-STU-01 - Login

- **Status**: Baseline
- **Actor**: Student
- **Description / Goal**: Student đăng nhập để truy cập Ticket của mình.
- **Preconditions**: Student có account hợp lệ.
- **Inputs**: Username/email/mã sinh viên và mật khẩu.
- **Main Flow**:
  1. Student mở màn hình login.
  2. Student nhập thông tin đăng nhập.
  3. Hệ thống xác thực account.
  4. Hệ thống điều hướng Student vào Student Portal.
- **Alternative/Error Flow**: Sai thông tin đăng nhập hoặc account không hợp lệ thì không cho truy cập và hiển thị lỗi chung.
- **Business Rules References**: BR-ACC-01.
- **Output/Postcondition**: Student có phiên làm việc hợp lệ và chỉ xem được dữ liệu của mình.
- **Acceptance Criteria**:
  - AC1: Account hợp lệ đăng nhập thành công.
  - AC2: Sai thông tin đăng nhập không tạo phiên làm việc.
  - AC3: Student không truy cập được màn hình Staff/Management.
- **Related Workflow**: WF-01, WF-06
- **Related Test Scenario**: TS-STU-01-01, TS-STU-01-02

### FR-STU-02 - Create Support Ticket

- **Status**: Baseline
- **Actor**: Student
- **Description / Goal**: Student tạo yêu cầu hỗ trợ và nhận Ticket ID để theo dõi.
- **Preconditions**: Student đã login.
- **Inputs**: Category/nhóm vấn đề, description, attachment ảnh/PDF nếu có. Title là Derived/TBD nếu team cần để hiển thị danh sách.
- **Main Flow**:
  1. Student mở form tạo Ticket.
  2. Student chọn category/nhóm vấn đề.
  3. Student nhập mô tả yêu cầu.
  4. Student đính kèm ảnh/PDF nếu cần.
  5. Student gửi yêu cầu.
  6. Hệ thống validate dữ liệu.
  7. Hệ thống tạo Ticket, cấp Ticket ID và đặt trạng thái `NEW`.
  8. Hệ thống hiển thị Ticket ID cho Student.
- **Alternative/Error Flow**:
  - Thiếu category/description thì không tạo Ticket.
  - Attachment không hợp lệ theo rule đã xác nhận thì không nhận file.
  - Lỗi lưu dữ liệu thì không tạo Ticket dở dang.
- **Business Rules References**: BR-FILE-02, BR-HIS-01.
- **Output/Postcondition**: Ticket mới ở trạng thái `NEW`, gắn với Student owner.
- **Acceptance Criteria**:
  - AC1: Dữ liệu hợp lệ tạo được Ticket ID duy nhất.
  - AC2: Thiếu thông tin bắt buộc bị chặn.
  - AC3: Ticket vừa tạo xuất hiện trong danh sách Ticket của Student.
  - AC4: Attachment ảnh/PDF được gắn vào Ticket nếu hợp lệ.
- **Related Workflow**: WF-01
- **Related Test Scenario**: TS-STU-02-01, TS-STU-02-02, TS-STU-02-03

### FR-STU-03 - View & Track Ticket

- **Status**: Baseline
- **Actor**: Student
- **Description / Goal**: Student xem danh sách Ticket của mình, trạng thái hiện tại và lịch sử cập nhật.
- **Preconditions**: Student đã login.
- **Inputs**: Bộ lọc/từ khóa là Derived nếu triển khai.
- **Main Flow**:
  1. Student mở danh sách Ticket của tôi.
  2. Hệ thống hiển thị Ticket do Student tạo.
  3. Student mở chi tiết Ticket.
  4. Hệ thống hiển thị mô tả, status, department/assignee nếu có, attachment và history.
- **Alternative/Error Flow**: Student truy cập Ticket không thuộc mình thì bị từ chối.
- **Business Rules References**: BR-ACC-01, BR-FILE-01.
- **Output/Postcondition**: Student nắm trạng thái mới nhất của Ticket.
- **Acceptance Criteria**:
  - AC1: Danh sách chỉ hiển thị Ticket của Student đang đăng nhập.
  - AC2: Chi tiết Ticket hiển thị status và lịch sử cập nhật.
  - AC3: Truy cập Ticket của Student khác bị chặn.
- **Related Workflow**: WF-01, WF-03, WF-06
- **Related Test Scenario**: TS-STU-03-01, TS-STU-03-02

### FR-STU-04 - Supplement Information

- **Status**: Baseline
- **Actor**: Student
- **Description / Goal**: Student bổ sung thông tin/giấy tờ khi Staff yêu cầu.
- **Preconditions**: Ticket thuộc Student và đang ở `WAITING_STUDENT`.
- **Inputs**: Nội dung bổ sung và/hoặc attachment ảnh/PDF.
- **Main Flow**:
  1. Student mở Ticket đang chờ bổ sung.
  2. Student xem nội dung Staff yêu cầu.
  3. Student nhập phản hồi hoặc đính kèm tài liệu.
  4. Student gửi bổ sung.
  5. Hệ thống lưu bổ sung, ghi history và chuyển Ticket về `IN_PROGRESS`.
- **Alternative/Error Flow**:
  - Không nhập nội dung và không có attachment thì bị chặn.
  - Ticket không còn ở `WAITING_STUDENT` thì yêu cầu Student tải lại thông tin mới nhất.
- **Business Rules References**: BR-SUP-02, BR-FILE-02.
- **Output/Postcondition**: Staff có thể tiếp tục xử lý Ticket.
- **Acceptance Criteria**:
  - AC1: Bổ sung hợp lệ được lưu vào history.
  - AC2: Status chuyển từ `WAITING_STUDENT` về `IN_PROGRESS`.
  - AC3: Student khác không bổ sung được vào Ticket này.
- **Related Workflow**: WF-03
- **Related Test Scenario**: TS-STU-04-01, TS-STU-04-02

### FR-STU-05 - Receive Ticket Notifications

- **Status**: Derived
- **Actor**: Student
- **Description / Goal**: Student nhận thông báo trong hệ thống khi Ticket có cập nhật quan trọng.
- **Preconditions**: Student có Ticket liên quan.
- **Inputs**: Không có input trực tiếp từ Student.
- **Main Flow**:
  1. Một sự kiện liên quan đến Ticket xảy ra.
  2. Hệ thống tạo notification cho Student liên quan.
  3. Student xem notification và mở chi tiết Ticket.
- **Alternative/Error Flow**: Nếu Student không online, notification vẫn hiển thị khi Student đăng nhập lại.
- **Business Rules References**: BR-HIS-01.
- **Output/Postcondition**: Student biết Ticket đã được cập nhật.
- **Acceptance Criteria**:
  - AC1: Khi Staff yêu cầu bổ sung, Student nhận notification.
  - AC2: Khi Staff ghi nhận kết quả, Student nhận notification.
  - AC3: Notification dẫn tới đúng Ticket.
- **Related Workflow**: WF-03, WF-05, WF-06
- **Related Test Scenario**: TS-STU-05-01

### FR-STU-06 - View Result & Rate Satisfaction

- **Status**: Baseline, rating scale Proposed
- **Actor**: Student
- **Description / Goal**: Student xem kết quả xử lý và đánh giá hài lòng sau khi Ticket hoàn tất.
- **Preconditions**: Ticket thuộc Student và đã `CLOSED` hoặc đã có kết quả ở `RESOLVED` theo rule đóng Ticket được xác nhận.
- **Inputs**: Rating và comment tùy chọn. Thang 1-5 sao là Proposed.
- **Main Flow**:
  1. Student mở Ticket đã có kết quả.
  2. Student xem resolution và attachment kết quả nếu có.
  3. Student gửi đánh giá hài lòng nếu muốn.
  4. Hệ thống lưu đánh giá và đưa dữ liệu vào báo cáo.
- **Alternative/Error Flow**:
  - Student chưa chọn rating theo thang đã xác nhận thì bị yêu cầu chọn lại.
  - Student không sở hữu Ticket thì bị từ chối.
- **Business Rules References**: BR-RAT-01, BR-RAT-02, BR-RAT-03.
- **Output/Postcondition**: Ticket có kết quả hiển thị cho Student; rating được lưu nếu Student gửi.
- **Acceptance Criteria**:
  - AC1: Student xem được kết quả xử lý của Ticket của mình.
  - AC2: Student gửi rating hợp lệ thì hệ thống lưu thành công.
  - AC3: Rating chỉ khả dụng sau khi Ticket hoàn tất.
- **Related Workflow**: WF-06
- **Related Test Scenario**: TS-STU-06-01, TS-STU-06-02

### FR-STU-P01 - FAQ / Guidance

- **Status**: Proposed
- **Actor**: Student
- **Description / Goal**: Student tra cứu hướng dẫn hoặc FAQ trước khi tạo Ticket.
- **Reason**: Có trong effort nội bộ, chưa thấy proposal chốt trực tiếp.
- **Acceptance Criteria**: Chỉ triển khai nếu Product Owner xác nhận nằm trong scope bàn giao.
