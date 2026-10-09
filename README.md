# Tài liệu Dự án UniSupport (UniSupport Documentation)

Chào mừng bạn đến với kho tài liệu chính thức của hệ thống **UniSupport** – Nền tảng chuẩn hóa và tập trung hóa quy trình tiếp nhận, xử lý và theo dõi các yêu cầu hỗ trợ sinh viên tại **Aurora University**.

> Số giờ công sức lấy đúng từ workbook Phân bổ Resources.xlsx, sheet Resource; xem [bảng đối chiếu giờ](./Phan_bo_Resources_Antigravity.md). Tài liệu đối chiếu không tính lại chi phí hoặc phê duyệt phạm vi mới.

---

## Phạm vi của bản hiệu chỉnh này

1. **Nguồn yêu cầu sản phẩm:** 14 FR trong [M01 PRD](./03-modules/M01-student-portal/prd.md), [M02 PRD](./03-modules/M02-staff-operations/prd.md), [M03 PRD](./03-modules/M03-management-dashboard/prd.md), đối chiếu với bản PRD đã sửa theo review video.
2. **Nguồn số giờ:** workbook Phân bổ Resources.xlsx, sheet Resource. 17 dòng công sức dùng mã R độc lập; tổng 618 giờ cơ sở + 22 dự phòng = 640 giờ, không tự chia lại hoặc cộng effort theo giai đoạn.
3. **Phạm vi nghiệp vụ:** [product-scope.md](./01-product/product-scope.md). FAQ, mở lại xử lý, báo cáo vượt cấp nhiều cấp và UI lưu trữ chưa có đặc tả thống nhất; không tự coi là chức năng mới đã duyệt.
4. **Tài liệu kỹ thuật:** giữ nguyên nội dung M04/M05, NFR, Architecture/ADR và các bảng kỹ thuật hiện có. Các mã tham khảo kỹ thuật không được dùng thay mã FR nghiệp vụ. Sai lệch còn tồn tại được ghi ở [prd-review-notes.md](./08-project/prd-review-notes.md), không phải quyết định thay phương án triển khai.
5. **Nghiệm thu:** [RTM](./06-acceptance/traceability-matrix.md) và [kịch bản](./06-acceptance/test-scenarios.md) bám 14 FR, chưa ghi là đã Pass khi chưa chạy.

`combined-docs.md` được tạo lại từ các file hiện tại để đọc một lần. Thư mục `unisupport-prd-extracted/` là bản tham chiếu đã nhập trước, không phải bộ PRD hiện hành và không được trộn vào bản tổng hợp mới.

---

## 1. Tóm Tắt Thông Số Dự Án (Project Snapshot)

| Thông Số / Chỉ Số | Giá Trị Chuẩn Hóa | Ghi Chú |
| :--- | :---: | :--- |
| **Tổng ngân sách hợp đồng** | **300.000.000 VNĐ** | Ba trăm triệu đồng chẵn |
| **Tổng công sức cơ sở (Base Effort)** | **618h** | 518h Business Functions + 100h Project Activities |
| **Dự phòng rủi ro công sức (Buffer)** | **22h** | Phân bổ cho các chức năng rủi ro cao |
| **Tổng công sức kế hoạch (Planned Effort)**| **640h** | 618h cơ sở + 22h dự phòng |
| **Chi phí nhân sự nội bộ cơ sở** | **186.557.727 VNĐ** | Lương Gross: 153.545.455 đ + BH 21.5%: 33.012.273 đ |
| **Chi phí dự phòng rủi ro ước tính** | **6.641.214 VNĐ** | Dự phòng 22h |
| **Tổng chi phí nhân sự kế hoạch** | **193.198.941 VNĐ** | Nếu sử dụng toàn bộ 22h dự phòng |
| **Thời gian phát triển** | **14 tuần (70 ngày làm việc)** | Triển khai theo phương pháp Vertical Slice (6 giai đoạn) |
| **Thời gian kiểm thử UAT** | **10 ngày làm việc** | Tuần 15–16 sau khi bàn giao |
| **Thời gian bảo hành kỹ thuật** | **30 ngày** | Sau khi ký biên bản nghiệm thu chính thức |
| **Quy mô đội ngũ** | **10 vị trí chuyên môn** | PM (70h), BA (63h), UI/UX (27h), TL (31h), FE1 (56h), FE2 (61h), BE1 (107h), BE2 (75h), QA (98h), DevOps (30h) |

---

## 2. Cấu trúc Cây Tài liệu (Documentation Structure)

```text
docs/
├── Phan_bo_Resources_Antigravity.md   # Giờ nguồn từ Excel và ánh xạ R → FR; không tạo estimate mới
├── README.md                          # [Tài liệu này] Tổng quan toàn bộ hệ thống tài liệu
├── 01-product/                        # Tổng quan sản phẩm, mục tiêu & phạm vi dự án
│   ├── product-overview.md            # Tổng quan dự án UniSupport & Snapshot
│   ├── problem-statement.md           # Hiện trạng & Khó khăn kênh tiếp nhận rời rạc
│   ├── goals-and-non-goals.md         # Mục tiêu cốt lõi & Scope / Non-goals
│   ├── actors-and-roles.md            # Vai trò (Sinh viên, Nhân viên, Quản lý, Admin)
│   └── product-scope.md               # Phạm vi 14 FR & Đối chiếu 17 dòng công sức
├── 02-domain/                         # Nghiệp vụ hỗ trợ sinh viên Aurora University
│   ├── domain-overview.md             # Tổng quan nghiệp vụ (4 nguyên tắc cốt lõi)
│   ├── terminology.md                 # Thuật ngữ nghiệp vụ (Ticket, SLA, Department...)
│   ├── ticket-model.md                # Mô hình dữ liệu Ticket
│   ├── ticket-lifecycle.md            # Vòng đời phiếu hỗ trợ
│   ├── state-transition.md            # Ma trận chuyển đổi trạng thái Ticket
│   └── business-rules.md              # Quy tắc nghiệp vụ (Quyền truy cập, chuyển phòng ban)
├── 03-modules/                        # Đặc tả yêu cầu chi tiết các Phân hệ
│   ├── M01-student-portal/            # PRD Phân hệ Sinh viên (4 FR Student; 5 dòng công sức, 128h)
│   ├── M02-staff-operations/          # PRD Phân hệ Nhân viên (5 FR Staff; 6 dòng công sức, 197h)
│   ├── M03-management-dashboard/      # PRD Phân hệ Quản trị & Báo cáo (5 FR Management; 6 dòng công sức, 215h)
│   ├── M04-notification-service/      # PRD Dịch vụ Thông báo (Hạ tầng kỹ thuật In-app & SLA)
│   └── M05-rbac-security/             # PRD Phân quyền RBAC & Bảo mật Audit log
├── 04-workflows/                      # Quy trình thao tác nghiệp vụ (Workflows)
│   ├── WF-01-submit-support-request.md # QTTN 01: Gửi yêu cầu & nhận mã Ticket
│   ├── WF-02-claim-and-triage.md      # QTTN 02: Tiếp nhận & Phân loại
│   ├── WF-03-request-supplement.md    # QTTN 03: Yêu cầu bổ sung thông tin
│   ├── WF-04-transfer-department.md   # QTTN 04: Chuyển tiếp phòng ban
│   ├── WF-05-complete-and-resolve.md  # QTTN 05: Cập nhật kết quả & Hoàn tất
│   └── WF-06-close-and-rate.md        # QTTN 06: Đóng Ticket & Đánh giá CSAT
├── 05-non-functional-requirements/    # Yêu cầu phi chức năng (NFR)
│   ├── performance.md                 # Hiệu năng (Quy mô 3.000 sinh viên)
│   ├── security.md                    # Bảo mật (Xác thực, phân quyền file)
│   ├── reliability.md                 # Độ ổn định & Tin cậy
│   ├── usability.md                   # Tính dễ sử dụng (Responsive, Đa ngôn ngữ VI/EN)
│   ├── observability.md               # Theo dõi trạng thái & Log hoạt động
│   └── deployment.md                  # Yêu cầu triển khai trên Server Client
├── 06-acceptance/                     # Tiêu chí Chấp nhận & Kiểm thử
│   ├── traceability-matrix.md         # Ma trận truy xuất 14 FR đã chốt (RTM)
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
    ├── constraints.md                 # Ràng buộc dự án & Cơ cấu chi phí chi tiết
    ├── milestones-and-timeline.md     # Tiến độ 6 giai đoạn & Phân bổ nhân sự 14 tuần
    ├── open-questions.md              # Vấn đề chờ thảo luận / phê duyệt
    └── glossary.md                    # Thuật ngữ & Khái niệm dự án
```
