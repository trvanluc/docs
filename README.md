# UniSupport - Tài Liệu Dự Án (Documentation Center)

Chào mừng bạn đến với kho tài liệu kỹ thuật và quản lý dự án chính thức của **UniSupport** – Nền tảng tiếp nhận, xử lý và quản lý yêu cầu hỗ trợ sinh viên tại **Aurora University**.

---

## 📌 Tổng Quan Dự Án

* **Tên dự án:** Hệ thống Quản lý Yêu cầu Hỗ trợ Sinh viên (UniSupport)
* **Khách hàng:** Aurora University
* **Mục tiêu:** Chuẩn hóa và tập trung hóa toàn bộ quy trình gửi, tiếp nhận, điều phối, xử lý và đánh giá yêu cầu hỗ trợ của sinh viên; loại bỏ sự phụ thuộc vào các kênh rời rạc như email, form online hay tin nhắn tự phát.
* **Quy mô phục vụ:** Tối ưu cho quy mô khoảng **3.000 sinh viên**.
* **Nền tảng triển khai:** Web Application (Responsive trên máy tính và thiết bị di động).
* **Thời gian thực hiện:** **14 tuần** (70 ngày làm việc), bao gồm 6 giai đoạn từ thu thập yêu cầu đến bàn giao.
* **Tổng ngân sách:** **300 Triệu VNĐ**.

---

## 📐 Cấu Trúc Thư Mục Tài Liệu

Bộ tài liệu này được cấu trúc chi tiết thành 8 phần chính nhằm đảm bảo tính đồng bộ thông tin giữa đội ngũ phát triển, kiểm thử, quản lý dự án và đại diện Aurora University:

```text
docs/
├── README.md                           # Tổng quan tài liệu & Hướng dẫn tra cứu
├── 01-product/                         # Tổng quan sản phẩm & Phạm vi dự án
│   ├── product-overview.md             # Định hướng & Giải pháp cốt lõi
│   ├── problem-statement.md            # Khó khăn hiện tại & Động lực dự án
│   ├── goals-and-non-goals.md          # Mục tiêu dự án & Phạm vi Out of Scope
│   ├── actors-and-roles.md             # Định nghĩa 3 vai trò (Sinh viên, Nhân viên, Quản lý)
│   └── product-scope.md                # Phạm vi chi tiết & Giả định kỹ thuật
├── 02-domain/                          # Nghiệp vụ & Quy tắc hệ thống
│   ├── domain-overview.md             # Nghiệp vụ hỗ trợ tại Aurora University
│   ├── terminology.md                  # Thuật ngữ chuyên ngành (Ticket, SLA, UAT,...)
│   ├── ticket-model.md                 # Cấu trúc & Trường dữ liệu Ticket
│   ├── ticket-lifecycle.md             # Vòng đời chuyển dịch của Ticket
│   ├── state-transition.md             # Ma trận chuyển đổi trạng thái
│   └── business-rules.md               # Các quy tắc nghiệp vụ bắt buộc
├── 03-modules/                         # Phân hệ chức năng & PRD Chi tiết
│   ├── M01-student-portal.md       # Phân hệ Sinh viên
│   ├── M02-staff-operations.md     # Phân hệ Nhân viên
│   └── M03-management-dashboard.md # Phân hệ Quản lý
├── 04-workflows/                       # Quy trình nghiệp vụ tiêu chuẩn (Workflows)
│   ├── WF-01-submit-support-request.md # Sinh viên tạo Ticket mới
│   ├── WF-02-claim-and-triage.md       # Nhân viên tiếp nhận & Phân loại
│   ├── WF-03-request-supplement.md     # Yêu cầu bổ sung thông tin/giấy tờ
│   ├── WF-04-transfer-department.md    # Chuyển tiếp yêu cầu liên phòng ban
│   ├── WF-05-complete-and-resolve.md   # Xử lý hoàn tất & Đóng Ticket
│   └── WF-06-close-and-rate.md         # Sinh viên nhận kết quả & Đánh giá
├── 05-non-functional-requirements/    # Yêu cầu phi chức năng
│   ├── performance.md                  # Hiệu năng (Đáp ứng 3.000 SV)
│   ├── security.md                     # Bảo mật & Phân quyền xem File
│   ├── reliability.md                  # Độ ổn định & Hạ tầng triển khai
│   ├── usability.md                    # Giao diện Responsive & Đa ngôn ngữ (VI/EN)
│   ├── observability.md                # Ghi nhận thông tin & Audit Log
│   └── deployment.md                   # Hạ tầng Server & Tên miền Client
├── 06-acceptance/                      # Kiểm thử & Nghiệm thu
│   ├── traceability-matrix.md          # Ma trận truy xuất yêu cầu (RTM)
│   └── test-scenarios.md               # Kịch bản kiểm thử UAT (10 ngày nghiệm thu)
├── 07-architecture/                    # Thiết kế Kiến trúc & Kỹ thuật
│   ├── system-context.md               # Sơ đồ ngữ cảnh hệ thống
│   ├── architecture-overview.md        # Kiến trúc Frontend & Backend
│   ├── data-model.md                   # Sơ đồ ERD & Mô hình CSDL
│   ├── api-design.md                   # Thiết kế chuẩn RESTful API
│   ├── security-design.md              # Cơ chế xác thực & Phân quyền
│   └── technical-decisions/            # Các quyết định kỹ thuật quan trọng (ADR)
│       ├── ADR-001-ticket-id-generation.md
│       ├── ADR-002-role-based-access-control.md
│       └── ADR-003-file-attachment-storage.md
└── 08-project/                         # Quản lý Dự án & Tiến độ
    ├── assumptions.md                  # Giả định triển khai
    ├── constraints.md                  # Ràng buộc dự án (14 tuần, 300 tr)
    ├── milestones-and-timeline.md      # Lịch trình 6 giai đoạn & Lịch nghiệm thu/Bảo hành
    ├── open-questions.md               # Danh mục trao đổi cần phê duyệt
    └── glossary.md                     # Thuật ngữ dự án