# 📚 Tài liệu Dự án UniSupport (UniSupport Documentation)

Chào mừng bạn đến với kho tài liệu chính thức của hệ thống **UniSupport** – Nền tảng chuẩn hóa và tập trung hóa quy trình tiếp nhận, xử lý và theo dõi các yêu cầu hỗ trợ sinh viên tại **Aurora University**.

---

## 📌 Cấu trúc Cây Tài liệu (Documentation Structure)

```text
docs/
├── README.md                          # [Tài liệu này] Tổng quan toàn bộ hệ thống tài liệu
├── 01-product/                        # Tổng quan sản phẩm, mục tiêu & phạm vi dự án
│   ├── product-overview.md            # Tổng quan dự án UniSupport
│   ├── problem-statement.md           # Hiện trạng & Khó khăn kênh rời rạc
│   ├── goals-and-non-goals.md         # Mục tiêu cốt lõi & Scope/Out of Scope
│   ├── actors-and-roles.md            # Vai trò (Sinh viên, Nhân viên, Quản lý)
│   └── product-scope.md               # Phạm vi sản phẩm & Các giả định (3.000 sinh viên)
├── 02-domain/                         # Nghiệp vụ hỗ trợ sinh viên Aurora University
│   ├── domain-overview.md             # Tổng quan nghiệp vụ
│   ├── terminology.md                 # Thuật ngữ nghiệp vụ (Ticket, SLA, Department...)
│   ├── ticket-model.md                # Mô hình dữ liệu Ticket
│   ├── ticket-lifecycle.md            # Vòng đời phiếu hỗ trợ
│   ├── state-transition.md            # Ma trận chuyển đổi trạng thái Ticket
│   └── business-rules.md              # Quy tắc nghiệp vụ (Quyền truy cập, chuyển phòng ban)
├── 03-modules/                        # Mô tả yêu cầu chi tiết 5 Phân hệ
│   ├── M01-student-portal/            # PRD Phân hệ Sinh viên
│   ├── M02-staff-operations/          # PRD Phân hệ Nhân viên
│   ├── M03-management-dashboard/      # PRD Phân hệ Quản lý
│   ├── M04-notification-service/      # PRD Dịch vụ Thông báo
│   └── M05-rbac-security/             # PRD Phân quyền & Bảo mật Audit log
├── 04-workflows/                      # Quy trình thao tác nghiệp vụ (Workflows)
│   ├── WF-01-submit-support-request.md # QTTN 01: Gửi yêu cầu & nhận mã Ticket
│   ├── WF-02-claim-and-triage.md      # QTTN 02: Tiếp nhận & Phân loại
│   ├── WF-03-request-supplement.md    # QTTN 03: Yêu cầu bổ sung thông tin
│   ├── WF-04-transfer-department.md   # QTTN 04: Chuyển tiếp phòng ban
│   ├── WF-05-complete-and-resolve.md  # QTTN 05: Cập nhật kết quả & Đóng yêu cầu
│   └── WF-06-close-and-rate.md        # QTTN 06: Đánh giá mức độ hài lòng
├── 05-non-functional-requirements/    # Yêu cầu phi chức năng (NFR)
│   ├── performance.md                 # Hiệu năng (Quy mô 3.000 sinh viên)
│   ├── security.md                    # Bảo mật (Xác thực, phân quyền file)
│   ├── reliability.md                 # Độ ổn định & Tin cậy
│   ├── usability.md                   # Tính dễ sử dụng (Responsive, Đa ngôn ngữ VI/EN)
│   ├── observability.md               # Theo dõi trạng thái & Log hoạt động
│   └── deployment.md                  # Yêu cầu triển khai trên Server Client
├── 06-acceptance/                     # Tiêu chí Chấp nhận & Kiểm thử
│   ├── traceability-matrix.md         # Ma trận truy xuất yêu cầu (RTM)
│   └── test-scenarios.md              # Kịch bản kiểm thử UAT (10 ngày nghiệm thu)
├── 07-architecture/                   # Thiết kế Kiến trúc Hệ thống
│   ├── system-context.md              # Sơ đồ ngữ cảnh C4 Context
│   ├── architecture-overview.md       # Kiến trúc Frontend, Backend & Storage
│   ├── data-model.md                  # ERD & Schema CSDL
│   ├── api-design.md                  # Thiết kế RESTful API
│   ├── security-design.md             # Thiết kế Bảo mật & RBAC
│   └── technical-decisions/           # Các quyết định kiến trúc (ADR-001, ADR-002, ADR-003)
└── 08-project/                        # Quản lý Dự án & Kế hoạch
    ├── assumptions.md                 # Các giả định dự án
    ├── constraints.md                 # Ràng buộc dự án (14 tuần, 300 triệu VNĐ)
    ├── milestones-and-timeline.md     # Tiến độ 6 giai đoạn, mốc nghiệm thu & bảo hành 30 ngày
    ├── open-questions.md              # Vấn đề chờ thảo luận / phê duyệt
    └── glossary.md                    # Thuật ngữ & Khái niệm dự án