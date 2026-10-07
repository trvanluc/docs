# Specification - RBAC & Security dùng chung

RBAC & Security là năng lực dùng chung cho 3 business module. Tài liệu này mô tả yêu cầu sản phẩm/an toàn dữ liệu; chi tiết JWT/session, middleware, database constraint, encryption, secured file endpoint nằm trong `07-architecture`.

## FR-SEC-01 - Role-Based Access Enforcement

- **Status**: Baseline
- **Actor**: System
- **Description / Goal**: Kiểm tra role/phạm vi dữ liệu trước khi cho người dùng xem hoặc thao tác tài nguyên.
- **Role model**: `STUDENT`, `STAFF`, `MANAGEMENT`.
- **Business Rules References**: BR-ACC-01, BR-ACC-02, BR-ACC-03.
- **Acceptance Criteria**:
  - AC1: Student không xem được Ticket của Student khác.
  - AC2: Staff không xử lý Ticket ngoài phạm vi được giao.
  - AC3: Management chỉ xem/quản trị theo permission được cấp.
- **Related Test Scenario**: TS-SEC-01-01, TS-SEC-01-02

## FR-SEC-02 - Attachment Access Protection

- **Status**: Baseline
- **Actor**: System
- **Description / Goal**: File đính kèm chỉ người liên quan được xem/tải.
- **Business Rules References**: BR-FILE-01.
- **Acceptance Criteria**:
  - AC1: Student owner xem được file của Ticket mình.
  - AC2: Student khác bị từ chối.
  - AC3: Staff ngoài phạm vi bị từ chối.
- **Related Test Scenario**: TS-SEC-02-01, TS-SEC-02-02

## FR-SEC-03 - Important Action History

- **Status**: Baseline
- **Actor**: System
- **Description / Goal**: Lưu lịch sử các thao tác quan trọng để tra soát.
- **Important actions**: create Ticket, claim/assign, transfer, request supplement, supplement, record resolution, close Ticket, create/edit account, assign role/permission.
- **Business Rules References**: BR-HIS-01.
- **Acceptance Criteria**:
  - AC1: Mỗi thao tác quan trọng tạo một history/audit entry đủ để tra soát.
  - AC2: Management có permission phù hợp xem được lịch sử theo phạm vi.
- **Related Test Scenario**: TS-SEC-03-01

## FR-SEC-P01 - Authentication Implementation Details

- **Status**: Derived/Architecture
- **Description / Goal**: Chọn JWT hay server-side session, token expiry, password hashing, cookie/header storage.
- **Reason**: Đây là implementation decision, không phải business scope từ proposal.
