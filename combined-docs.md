# UniSupport — Bộ tài liệu hiện tại sau đối chiếu PRD

Nguồn yêu cầu: 14 FR M01–M03. Nguồn giờ: Resource, 618 + 22 = 640 giờ. Phần kỹ thuật được giữ nguyên và có ghi nhận sai lệch; không tự mở rộng chức năng. Bản này tổng hợp từ các file hiện tại, không nhập bản combined cũ hoặc thư mục extracted.



---

## Tài liệu nguồn: README.md

# Tài liệu Dự án UniSupport (UniSupport Documentation)

Chào mừng bạn đến với kho tài liệu chính thức của hệ thống **UniSupport** – Nền tảng chuẩn hóa và tập trung hóa quy trình tiếp nhận, xử lý và theo dõi các yêu cầu hỗ trợ sinh viên tại **Aurora University**.

> Số giờ công sức lấy đúng từ workbook Phân bổ Resources.xlsx, sheet Resource; xem [bảng đối chiếu giờ](Phan_bo_Resources_Antigravity.md). Tài liệu đối chiếu không tính lại chi phí hoặc phê duyệt phạm vi mới.

---

## Phạm vi của bản hiệu chỉnh này

1. **Nguồn yêu cầu sản phẩm:** 14 FR trong [M01 PRD](03-modules/M01-student-portal/prd.md), [M02 PRD](03-modules/M02-staff-operations/prd.md), [M03 PRD](03-modules/M03-management-dashboard/prd.md), đối chiếu với bản PRD đã sửa theo review video.
2. **Nguồn số giờ:** workbook Phân bổ Resources.xlsx, sheet Resource. 17 dòng công sức dùng mã R độc lập; tổng 618 giờ cơ sở + 22 dự phòng = 640 giờ, không tự chia lại hoặc cộng effort theo giai đoạn.
3. **Phạm vi nghiệp vụ:** [product-scope.md](01-product/product-scope.md). FAQ, mở lại xử lý, báo cáo vượt cấp nhiều cấp và UI lưu trữ chưa có đặc tả thống nhất; không tự coi là chức năng mới đã duyệt.
4. **Tài liệu kỹ thuật:** giữ nguyên nội dung M04/M05, NFR, Architecture/ADR và các bảng kỹ thuật hiện có. Các mã tham khảo kỹ thuật không được dùng thay mã FR nghiệp vụ. Sai lệch còn tồn tại được ghi ở [prd-review-notes.md](08-project/prd-review-notes.md), không phải quyết định thay phương án triển khai.
5. **Nghiệm thu:** [RTM](06-acceptance/traceability-matrix.md) và [kịch bản](06-acceptance/test-scenarios.md) bám 14 FR, chưa ghi là đã Pass khi chưa chạy.

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


---

## Tài liệu nguồn: 01-product/actors-and-roles.md

# Vai trò và phạm vi quyền UniSupport

## Bốn vai trò đã có trong PRD

- **STUDENT:** Sinh viên được nhà trường/ADMIN cấp tài khoản; tạo, theo dõi, bổ sung theo yêu cầu và đánh giá chính Ticket của mình. Không tự đăng ký tài khoản.
- **STAFF:** Nhân viên được ADMIN cấp tài khoản và gán phòng ban; xem hàng đợi của phòng ban và thực hiện các thao tác theo quyền trên Ticket/người phụ trách.
- **MANAGER:** Quản lý phòng ban; giám sát, báo cáo và phân công trong phòng ban mình. Không quản trị tài khoản toàn hệ thống hoặc xem dữ liệu phòng ban khác.
- **ADMIN:** Quản trị viên; cấp tài khoản, gán vai trò/phòng ban, khóa/mở khóa, quản lý danh mục, tra soát và xem báo cáo toàn trường theo quyền gốc.

Đây là phân biệt bốn vai trò đã có trong FR-MNG-01/04, không tạo thêm cấp phân quyền. Các cổng nghiệp vụ vẫn gồm Student, Staff và Management.

## Ma trận quyền nghiệp vụ

| Thao tác | STUDENT | STAFF | MANAGER | ADMIN |
| --- | --- | --- | --- | --- |
| Đăng nhập | Có | Có | Có | Có |
| Tạo Ticket cá nhân | Có | Không | Không | Không |
| Xem/bổ sung/đánh giá Ticket cá nhân | Chỉ Ticket của mình | Không | Không | Không |
| Xem Queue và tiếp nhận Ticket | Không | Trong phòng ban | Trong phòng ban | Toàn trường theo quyền đã có |
| Chuyển phòng, yêu cầu bổ sung, ghi kết quả | Không | Theo quyền Ticket/người phụ trách | Trong phòng ban theo quyền đã có | Theo quyền đã có |
| Phân công/thu hồi/phân công lại | Không | Không | Trong phòng ban | Theo quyền đã có |
| Dashboard/báo cáo | Không | Không | Phòng ban phụ trách | Toàn trường |
| Tạo/sửa/khóa/mở khóa tài khoản và gán quyền | Không | Không | Không | Có |
| Quản lý danh mục nhóm vấn đề | Không | Không | Không | Quyền đã có trong tài liệu gốc |
| Xem Audit Log hệ thống | Không | Không | Không | Có; chỉ đọc |

## Các điểm không được nhầm

- STAFF tự nhận Ticket (Claim); MANAGER/ADMIN phân công cho người khác (Assign/Reassign). Chuyển phòng ban là thao tác khác, đặc tả tại FR-STF-03.
- Không coi chức danh “Ban Giám hiệu” là tự động có ADMIN: phạm vi dữ liệu phụ thuộc vai trò đã được cấp.
- Sau chuyển phòng ban, quyền xử lý thuộc đơn vị tiếp nhận theo PRD; không cấp thêm quyền xem/sửa ngoài phòng ban cho STAFF cũ.
- Danh mục nhóm vấn đề gắn phòng ban mặc định. Quyền ADMIN đã có không đồng nghĩa lần sửa này mở thêm FR hoặc màn hình quản trị mới.


---

## Tài liệu nguồn: 01-product/goals-and-non-goals.md

# Mục Tiêu Dự Án & Các Mục Nằm Ngoài Phạm Vi (Goals & Non-Goals)

## 1. Mục Tiêu Cốt Lõi (Core Goals)

### G-01: Tập trung hóa đầu mối tiếp nhận
- **Mục tiêu**: Tập trung 100% các yêu cầu hỗ trợ trực tuyến của sinh viên Aurora University vào hệ thống UniSupport.
- **Tiêu chí đo lường**: 100% yêu cầu khởi tạo trên hệ thống đều được cấp mã Ticket định danh duy nhất (ví dụ: `TK-20261004-0001`).

### G-02: Minh bạch hóa tiến độ xử lý
- **Mục tiêu**: Giúp sinh viên dễ dàng tra cứu trạng thái xử lý và đơn vị/nhân viên đang thụ lý yêu cầu.
- **Tiêu chí đo lường**: Sinh viên xem được tiến độ theo thời gian thực (Real-time status) ngay trên trang cá nhân mà không cần gọi điện hay gửi email truy vấn.

### G-03: Tối ưu quy trình vận hành phòng ban
- **Mục tiêu**: Chuẩn hóa luồng làm việc của nhân viên từ khâu tiếp nhận, phân loại, chuyển phòng ban đến cập nhật kết quả.
- **Tiêu chí đo lường**: Giảm tỷ lệ bỏ sót yêu cầu xuống **0%**; giảm thời gian chuyển tiếp công việc giữa các phòng ban.

### G-04: Cung cấp năng lực giám sát cho Ban quản lý
- **Mục tiêu**: Cung cấp Dashboard tổng quan và Báo cáo chi tiết về khối lượng công việc, tỷ lệ hoàn thành, thời gian xử lý trung bình và chỉ số hài lòng.
- **Tiêu chí đo lường**: Xuất được báo cáo trực quan theo khoảng thời gian và theo từng phòng ban.

### G-05: Bảo mật và Phân quyền truy cập
- **Mục tiêu**: Đảm bảo đúng người đúng việc, file đính kèm chỉ người có thẩm quyền mới được truy cập.
- **Tiêu chí đo lường**: Áp dụng mô hình RBAC cho 4 vai trò đã có (STUDENT, STAFF, MANAGER, ADMIN), tra soát log thao tác cho các hành động quan trọng.

---

## 2. Các Mục Nằm Ngoài Phạm Vi Hiện Tại (Out of Scope / Non-Goals)

Để đảm bảo dự án hoàn thành đúng tiến độ **14 tuần** và ngân sách **300 triệu VNĐ**, các hạng mục sau **KHÔNG** thuộc phạm vi triển khai của hợp đồng này:

| STT | Hạng Mục Nằm Ngoài Phạm Vi | Lý Do / Giải Thích |
| :---: | :--- | :--- |
| **NG-01** | **Mobile App độc lập (iOS / Android)** | Hệ thống chỉ phát triển dạng **Web Application** (Responsive giao diện trên di động). Không phát triển app native trên App Store / Google Play. |
| **NG-02** | **Tích hợp hệ thống bên thứ ba nâng cao** | Không tích hợp với hệ thống quản lý đào tạo (ERP), phần mềm kế toán, hay hệ thống SSO phức tạp ngoài phạm vi thống nhất. |
| **NG-03** | **Quản trị hạ tầng máy chủ & Backup tự động** | Đơn vị phát triển bàn giao script/tài liệu cài đặt. Việc thiết lập tự động sao lưu, giám sát hạ tầng máy chủ lâu dài do Aurora University tự đảm nhận. |
| **NG-04** | **Phân quyền nhiều cấp & Audit Log nâng cao** | Chỉ hỗ trợ mô hình phân quyền 4 vai trò đã có (STUDENT, STAFF, MANAGER, ADMIN) và lưu log thao tác cơ bản. Không hỗ trợ phân quyền ma trận đa cấp độ hoặc ghi log chi tiết mức dữ liệu sâu. |
| **NG-05** | **Chat trực tiếp (Livechat) / Gọi thoại (VoIP)** | Không tích hợp khung chat real-time hoặc gọi điện trực tiếp trong hệ thống. Mọi trao đổi diễn ra qua tính năng nhắn/gửi yêu cầu bổ sung thông tin trên Ticket. |
| **NG-06** | **Tối ưu chịu tải lớn (> 3.000 sinh viên)** | Hệ thống được thiết kế tối ưu cho quy mô 3.000 sinh viên của Aurora University, không chịu trách nhiệm tối ưu kiến trúc Microservices/Load Balancing phức tạp cho hàng trăm nghìn truy cập đồng thời. |
| **NG-07** | **Kiểm thử thâm nhập (Pentest) & Chứng nhận bảo mật** | Không bao gồm chi phí thuê bên thứ ba đánh giá an toàn thông tin chuyên sâu hoặc cấp chứng chỉ bảo mật quốc tế (ISO/IEC 27001, SOC2...). |


---

## Tài liệu nguồn: 01-product/problem-statement.md

# Hiện Trạng & Bài Toán Nghiệp Vụ (Problem Statement)

## 1. Hiện Trạng Tiếp Nhận Yêu Cầu Tại Aurora University

Hiện tại, công tác tiếp nhận và phản hồi yêu cầu hỗ trợ sinh viên tại Aurora University đang phân tán qua nhiều kênh không chuẩn hóa:
1. **Email cá nhân / Email phòng ban**: Sinh viên gửi email đến giảng viên, chuyên viên hoặc hòm thư chung phòng Đào tạo/CTHSSV.
2. **Google Forms / Biểu mẫu trực tuyến lẻ tẻ**: Mỗi phòng ban tự tạo form riêng, dữ liệu không đồng bộ.
3. **Tin nhắn mạng xã hội / Ứng dụng chat**: Zalo, Fanpage, Messenger.
4. **Tiếp nhận trực tiếp**: Sinh viên đến nộp hồ sơ giấy tại văn phòng một cửa.

---

## 2. Các Điểm Nghẽn & Khó Khăn Chính (Key Pain Points)

### 2.1 Thiếu đầu mối tập trung và mất mát dữ liệu
- Yêu cầu của sinh viên bị rải rác ở nhiều nơi, không có cơ sở dữ liệu tập trung để tra cứu lại lịch sử hỗ trợ.
- Nguy cơ thất lạc thông tin hoặc trôi email trong các đợt cao điểm (đầu khóa học, đăng ký môn học, xét tốt nghiệp).

### 2.2 Phản hồi chậm và nguy cơ bỏ sót yêu cầu
- Thiếu hệ thống mã định danh (Ticket ID), khiến việc tra cứu trạng thái gặp khó khăn.
- Không có cơ chế cảnh báo yêu cầu quá hạn hoặc phân công trách nhiệm rõ ràng, dẫn đến tình trạng "đùn đẩy" công việc giữa các bộ phận.

### 2.3 Xử lý trùng lặp và phản hồi không thống nhất
- Nhiều nhân viên cùng phản hồi một email hoặc xử lý trùng một hồ sơ gây lãng phí nguồn lực.
- Thông tin hướng dẫn sinh viên giữa các nhân viên trong cùng phòng ban đôi khi không nhất quán.

### 2.4 Sinh viên thiếu thông tin tiến độ
- Sinh viên không biết yêu cầu của mình đang ở bước nào, ai đang thụ lý, khi nào có kết quả.
- Dẫn đến việc sinh viên phải gửi lại yêu cầu nhiều lần hoặc đến trực tiếp văn phòng để hỏi, gây quá tải bộ phận một cửa.

### 2.5 Ban quản lý thiếu công cụ giám sát và số liệu báo cáo
- Trưởng phòng ban và Ban giám hiệu không có số liệu thực tế về:
  - Tổng số yêu cầu tiếp nhận / đã giải quyết / còn tồn đọng.
  - Thời gian xử lý trung bình của từng phòng ban/nhân viên.
  - Các nhóm vấn đề phát sinh phổ biến nhất để cải tiến quy trình đào tạo/vận hành.
  - Mức độ hài lòng của sinh viên đối với dịch vụ hỗ trợ.

---

## 3. Tác Động Tiêu Cực (Impact Analysis)
[Kênh tiếp nhận rời rạc]
│
├──► Thất lạc / Bỏ sót yêu cầu ───────► Sinh viên bức xúc, giảm uy tín nhà trường
├──► Xử lý trùng lặp / Chậm trễ ──────► Lãng phí thời gian & nhân lực vận hành
└──► Thiếu báo cáo số liệu ───────────► Quản lý không thể điều phối & cải tiến quy trình

---

## 4. Giải Pháp Mong Muốn Từ UniSupport

Hệ thống UniSupport giải quyết các vấn đề trên thông qua:
1. **Chuẩn hóa đầu mối**: Mọi yêu cầu hỗ trợ phải đi qua duy nhất một Web Portal. Mỗi yêu cầu sinh ra một Mã Ticket duy nhất.
2. **Minh bạch tiến độ**: Sinh viên xem được nhật ký chuyển trạng thái và đơn vị đang thụ lý theo thời gian thực.
3. **Quy trình hóa vận hành**: Quy định rõ luồng Tiếp nhận/phân loại -> Bổ sung hoặc chuyển phòng khi cần -> Cập nhật kết quả -> Sinh viên xem/đánh giá -> Đóng theo vòng đời hiện có.
4. **Dashboard báo cáo trực quan**: Ban quản lý nắm bắt ngay các chỉ số KPI, ticket quá hạn và đánh giá mức độ hài lòng của sinh viên.


---

## Tài liệu nguồn: 01-product/product-overview.md

# Tổng Quan Sản Phẩm - UniSupport (Product Overview)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`

## 1. Tóm Tắt Dự Án (Executive Summary)
**UniSupport** là hệ thống Web Application quản lý và hỗ trợ sinh viên tập trung được phát triển dành riêng cho **Aurora University**. Hệ thống ra đời nhằm chuẩn hóa toàn bộ quy trình tiếp nhận, phân loại, điều phối và xử lý các yêu cầu hỗ trợ từ sinh viên, thay thế cho các kênh truyền thống rời rạc (email cá nhân/phòng ban, form trực tuyến, tin nhắn rải rác).

Hệ thống phục vụ quy mô khoảng **3.000 sinh viên** cùng đội ngũ nhân viên vận hành và ban quản lý nhà trường, hướng tới mục tiêu tối ưu hóa thời gian xử lý yêu cầu, nâng cao tính minh bạch và nâng cao mức độ hài lòng của sinh viên.

---

## 2. Bối Cảnh & Tầm Nhìn Dự Án (Context & Vision)

### 2.1 Bối cảnh
Tại Aurora University, công tác hỗ trợ sinh viên (thủ tục hành chính, xác nhận học tập, miễn giảm học phí, tư vấn đào tạo, hỗ trợ kỹ thuật...) đang được thực hiện qua nhiều kênh thủ công. Điều này dẫn đến tình trạng trôi thông tin, xử lý trùng lặp, thiếu công cụ theo dõi tiến độ và gây khó khăn cho Ban giám hiệu trong việc đánh giá hiệu suất vận hành của các phòng ban.

### 2.2 Tầm nhìn sản phẩm
Trở thành **đầu mối giao tiếp số duy nhất** giữa Sinh viên và Các phòng ban chức năng tại Aurora University. Tất cả yêu cầu hỗ trợ đều được định danh bằng mã Ticket duy nhất, luồng xử lý được chuẩn hóa minh bạch, số liệu báo cáo được cập nhật theo thời gian thực.

---

## 3. Các Phân Hệ & Phân Bổ Công Sức (Modules & Effort Allocation)

Hệ thống có 3 cổng nghiệp vụ với 14 FR chi tiết. Resources phân bổ 17 dòng công việc theo Student/Staff/Admin và PM/DevOps; số dòng công sức không phải số FR.

| Nhóm | Phạm vi PRD hiện có | Cơ sở | Dự phòng | Kế hoạch |
| --- | --- | --- | --- | --- |
| M01 Student | Đăng nhập, gửi yêu cầu, theo dõi/bổ sung, xem kết quả/CSAT | 124 | 4 | 128 |
| M02 Staff | Đăng nhập, tiếp nhận/phân loại, chuyển phòng, yêu cầu bổ sung, hoàn tất | 187 | 10 | 197 |
| M03 Management | Đăng nhập/quyền, dashboard/SLA, báo cáo/xuất, tài khoản, tra soát | 207 | 8 | 215 |
| PM/DevOps | Giữ đúng hoạt động cấp dự án nguồn | 100 | 0 | 100 |
| Tổng | Mỗi dòng nguồn tính một lần | 618 | 22 | 640 |

Xem [đối chiếu Resources](Phan_bo_Resources_Antigravity.md) và [phạm vi sản phẩm](01-product/product-scope.md). M04/M05 là tài liệu kỹ thuật dùng chung, được giữ nguyên; không bổ sung effort hoặc mở rộng chức năng từ mô tả kỹ thuật đó.

---

## 4. Hình Thức Triển Khai & Hạ Tầng
- **Loại hình ứng dụng**: Web Application (Responsive trên Máy tính desktop và Thiết bị di động).
- **Hạ tầng triển khai**: Triển khai trực tiếp trên hạ tầng máy chủ và tên miền do Aurora University cung cấp.
- **Hỗ trợ ngôn ngữ**: Tiếng Việt và Tiếng Anh (mức cơ bản).

---

## 5. Tóm Tắt Thông Số Dự Án (Project Snapshot)
- **Tổng kinh phí hợp đồng**: 300.000.000 VNĐ.
- **Chi phí nhân sự nội bộ cơ sở (618h)**: 186.557.727 VNĐ (Lương gross: 153.545.455 đ + BH 21.5%: 33.012.273 đ).
- **Chi phí dự phòng rủi ro ước tính (22h)**: 6.641.214 VNĐ.
- **Tổng chi phí nhân sự kế hoạch (640h)**: 193.198.941 VNĐ.
- **Quy mô đội ngũ**: 10 vị trí chuyên môn (PM, BA, UI/UX, TL, FE1, FE2, BE1, BE2, QA, DevOps).
- **Thời gian thực hiện**: 14 tuần phát triển (tương đương 70 ngày làm việc).
- **Thời gian nghiệm thu**: 10 ngày làm việc UAT sau bàn giao.
- **Thời gian bảo hành kỹ thuật**: 30 ngày kể từ ngày nghiệm thu chính thức.


---

## Tài liệu nguồn: 01-product/product-scope.md

# Phạm vi sản phẩm và giới hạn Resources

## Yêu cầu sản phẩm đã chốt

Phạm vi PRD gồm **14 mã FR**: 4 Student, 5 Staff và 5 Management. Bảng Resources gồm **17 dòng công việc**, không phải 17 FR. Bản hiệu chỉnh giữ các mã và ý nghĩa hiện có; không đổi FR-STU-01 từ đăng nhập thành FAQ hoặc FR-STU-04 từ xem kết quả/đánh giá thành thông báo.

| Mã FR | Yêu cầu sản phẩm | Tài liệu chi tiết |
| --- | --- | --- |
| FR-STU-01 | Đăng nhập tài khoản sinh viên | [M01 PRD](03-modules/M01-student-portal/prd.md) |
| FR-STU-02 | Gửi yêu cầu hỗ trợ (Tạo Ticket) | [M01 PRD](03-modules/M01-student-portal/prd.md) |
| FR-STU-03 | Theo dõi tiến độ & Bổ sung thông tin/giấy tờ | [M01 PRD](03-modules/M01-student-portal/prd.md) |
| FR-STU-04 | Xem kết quả giải quyết & Đánh giá mức độ hài lòng | [M01 PRD](03-modules/M01-student-portal/prd.md) |
| FR-STF-01 | Nhân viên đăng nhập hệ thống | [M02 PRD](03-modules/M02-staff-operations/prd.md) |
| FR-STF-02 | Tiếp nhận và phân loại yêu cầu (Claim & Triage) | [M02 PRD](03-modules/M02-staff-operations/prd.md) |
| FR-STF-03 | Chuyển yêu cầu sang đúng phòng ban | [M02 PRD](03-modules/M02-staff-operations/prd.md) |
| FR-STF-04 | Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement) | [M02 PRD](03-modules/M02-staff-operations/prd.md) |
| FR-STF-05 | Ghi kết quả và hoàn tất xử lý yêu cầu | [M02 PRD](03-modules/M02-staff-operations/prd.md) |
| FR-MNG-01 | Quản lý đăng nhập & Xác thực phân quyền | [M03 PRD](03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-02 | Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision) | [M03 PRD](03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-03 | Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export) | [M03 PRD](03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-04 | Quản trị người dùng & Phân quyền (User Management & RBAC) | [M03 PRD](03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-05 | Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail) | [M03 PRD](03-modules/M03-management-dashboard/prd.md) |

## Giới hạn nghiệp vụ

Tài khoản do ADMIN cấp; Student chỉ thao tác Ticket của mình; Staff xử lý theo phòng ban; Manager giám sát/phân công phòng ban; Admin quản trị toàn trường theo quyền gốc. Nhóm vấn đề lấy từ danh mục hệ thống và gắn phòng ban mặc định.

Theo PRD: tiêu đề 10–150 ký tự, nội dung 20–2000 ký tự; tối đa 5 tệp sinh viên và 3 tệp kết quả nhân viên, mỗi tệp 5MB, PDF/PNG/JPG/JPEG. Cần bổ sung dùng NEED_MORE_INFO; sau bổ sung quay lại IN_PROGRESS. Hoàn tất xử lý hiển thị RESOLVED; đóng hiển thị CLOSED. CSAT 1–5 sao, nhận xét tùy chọn tối đa 500 ký tự, một lần/Ticket.

## Giới hạn phạm vi và giờ nguồn

- 14 mã FR trong M01–M03 là mã yêu cầu sản phẩm. 17 dòng Excel dùng mã R-STU/R-STF/R-ADM để đối chiếu công sức; không đổi các dòng đó thành FR mới.
- Một dòng công sức có thể liên quan nhiều FR. Chỉ tính dòng đó một lần; không tự tách hoặc chia lại giờ cho FR, vai trò hay tuần.
- FAQ có 14 giờ ở dòng nguồn nhưng chưa có đặc tả FR được chốt. Giữ giờ; không tự thêm màn hình, tìm kiếm FAQ hay đổi FR-STU-01 từ đăng nhập thành FAQ.
- Dòng “Đóng & mở lại yêu cầu” giữ 26 giờ; bản PRD/vòng đời hiện có không hỗ trợ mở lại quá trình xử lý Ticket đã CLOSED. Mở lại trang chi tiết là thao tác xem lại.
- Phản hồi/CSAT đã có tại FR-STU-04. Ghép với R-STU-05 chỉ là đối chiếu; chưa xác nhận chia effort riêng và không cộng thêm giờ.
- Dòng danh mục và lưu trữ được giữ nguyên giờ. Quyền cấu hình danh mục đã có trong tài liệu; không tự tạo FR, UI dọn dẹp/archiving hoặc chính sách lưu trữ mới.
- Tên “Escalation” trong dòng nguồn không đủ để chốt thêm luồng báo cáo vượt cấp. Bản sửa giữ luồng chuyển phòng ban/hoàn tất đã có.
- M04/M05 là tài liệu hỗ trợ kỹ thuật hiện tại, không phải hai phân hệ nghiệp vụ có effort bổ sung. Các mã FR-NTF/FR-SEC trong đó không được cộng vào 14 FR sản phẩm.

## Giới hạn công sức

Nguồn: [bảng đối chiếu Resources](Phan_bo_Resources_Antigravity.md). Student 128 giờ; Staff 197 giờ; Admin/Management 215 giờ; PM 70 giờ; DevOps 30 giờ. Tổng **618 giờ cơ sở + 22 giờ dự phòng = 640 giờ**. Giữ nguyên mỗi giờ theo dòng/role, không phân lại theo FR hoặc giai đoạn.

## Các ràng buộc dự án giữ theo hồ sơ hiện có

Ứng dụng Web responsive cho khoảng 3.000 sinh viên; không phát triển Mobile App độc lập, không mở rộng tích hợp ngoài phạm vi. Lịch 14 tuần phát triển và 10 ngày làm việc UAT sau bàn giao, bảo hành 30 ngày giữ như tài liệu hiện tại. Bản sửa không thay giá hợp đồng, đơn giá nhân sự hoặc phương án triển khai.


---

## Tài liệu nguồn: 02-domain/business-rules.md

# Quy Tắc Nghiệp Vụ Bắt Buộc (Business Rules Specification)

## 1. Tổng Quan
Tài liệu này tập hợp toàn bộ các Quy tắc Nghiệp vụ Cốt lõi (Business Rules - BR) bắt buộc phải được cài đặt chặt chẽ ở cả 2 lớp: **Client-side Validation** (Giao diện người dùng) và **Server-side Validation & Database Constraints** (Logic dịch vụ Backend). Các vi phạm quy tắc phải lập tức kích hoạt mã lỗi chuẩn hệ thống.

---

## 2. Chi Tiết Danh Mục Quy Tắc Nghiệp Vụ

### GROUP 1: Quy Tắc Khởi Tạo Ticket & Chống Trùng Lặp

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-01** | Bắt buộc Thông tin Đầu vào | Khi Sinh viên tạo Ticket, các trường `category_id` (Dropdown), `title` (10 - 150 ký tự), và `description` (20 - 2000 ký tự) là BẮT BUỘC. | Nếu thiếu bất kỳ trường nào, Client chặn submit. Server trả mã lỗi `400 INVALID_INPUT`. |
| **BR-02** | Tính Hợp Lệ Nội Dung Chuỗi | Mọi trường văn bản đầu vào (`title`, `description`, `resolution_note`, `request_note`, `rating_comment`) bắt buộc phải qua hàm `trim()`. Chuỗi chỉ chứa ký tự trắng (space, tab, newline) bị coi là không hợp lệ. | Báo lỗi validation: *"Nội dung không được để trống hoặc chỉ chứa khoảng trắng."* (`400 INVALID_INPUT`). |
| **BR-03** | Chống Trùng Lặp Thao Tác (Idempotency) | Một hành động gửi của Sinh viên chỉ được tạo ra đúng 01 Ticket duy nhất, bất kể sinh viên click đúp, retry do mất mạng hoặc bị nghẽn request. | **Client:** Vô hiệu hóa Form & Nút Gửi ngay khi bấm.<br>**Server:** Sử dụng Header `Client-Request-ID` (UUID v4) + Redis Key lock trong 30 giây. Trả về `409 DUPLICATE_REQUEST` nếu trùng key. |
| **BR-04** | Ràng Buộc Quyền Sở Hữu (Ownership) | Ticket khi khởi tạo phải tự động liên kết cứng với `student_id` lấy từ JWT Token của phiên đăng nhập hiện tại. Tránh triệt để việc giả mạo ID người gửi trên Payload. | Backend bỏ qua mọi trường `student_id` gửi lên từ body payload; bắt buộc đọc từ `request.user.id` thu được sau khi verify Token. |

---

### GROUP 2: Quy Tắc Xử Lý, Chuyển Tiếp & Đóng Ticket

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-05** | Chống Tranh Chấp Tiếp Nhận (Claim Lock) | Hai Nhân viên cùng phòng ban bấm Tiếp nhận (Claim) 1 Ticket `NEW` tại 1 thời điểm: Chỉ người có request đến trước được tiếp nhận. | Server sử dụng Atomic Database Lock (`status IN ('NEW', 'TRANSFERRED')`). Người đến sau nhận lỗi `409 TICKET_ALREADY_CLAIMED`. |
| **BR-06** | Quy Tắc Chuyển Phòng Ban (Transfer) | - Nhân viên chỉ được chuyển phòng ban khi Ticket chưa ở trạng thái `CLOSED` / `REJECTED`.<br>- Bắt buộc nhập lý do chuyển tiếp (`transfer_reason`) từ 10 - 500 ký tự.<br>- Khi chuyển, `assignee_id` tự động đặt về `NULL`.<br>- Bắt buộc ghi 01 record vào Audit Log (`ticket_histories`). | Nếu thiếu lý do, trả mã lỗi `400 MISSING_TRANSFER_REASON`. |
| **BR-07** | Ràng Buộc Bổ Sung Hồ Sơ | Khi Ticket ở `NEED_MORE_INFO`, Sinh viên chỉ được gửi lời nhắn giải trình và upload file đính kèm bổ sung. KHÔNG ĐƯỢC phép chỉnh sửa `title`, `description` hay `category_id` ban đầu. | Trạng thái Ticket tự động chuyển từ `NEED_MORE_INFO` → `IN_PROGRESS` ngay khi Sinh viên submit bổ sung thành công. |
| **BR-08** | Bắt Buộc Kết Quả Khi Đóng Ticket | Nhân viên BẮT BUỘC phải nhập `resolution_note` (Độ dài từ 20 - 2000 ký tự) trước khi bấm Hoàn tất xử lý (`RESOLVED` / `CLOSED`). | Nếu để trống hoặc chỉ nhập khoảng trắng, Server từ chối đổi trạng thái và trả lỗi `400 INVALID_INPUT`. |
| **BR-09** | Quy Tắc Auto-Close Hệ Thống | Ticket ở trạng thái `RESOLVED` quá 3 ngày làm việc (72 giờ làm việc, loại trừ T7, CN, Lễ) mà Sinh viên không phản hồi, Cronjob sẽ tự động chuyển `status = CLOSED`. | Cronjob hệ thống chạy định kỳ 23:00 mỗi ngày. Ghi log `action = SYSTEM_AUTO_CLOSE`. |

---

### GROUP 3: Quy Tắc Cảnh Báo SLA (Service Level Agreement)

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-10** | Khung Thời Gian Cam Kết SLA | Mặc định thời hạn xử lý Ticket (`sla_target_at`) là 24 giờ làm việc kể từ khi tạo. Khung giờ làm việc tính từ 08:00 - 17:00 (từ Thứ 2 đến Thứ 6), không tính cuối tuần và ngày lễ. | Sinh tự động: `sla_target_at = created_at + 24 working hours`. |
| **BR-11** | Trạng Thái Cảnh Báo Quá Hạn SLA | Cảnh báo trạng thái SLA dựa trên thời gian còn lại đến mốc `sla_target_at`:<br>- `ON_TRACK`: Thời gian còn lại > 25% SLA (> 6 giờ làm việc).<br>- `WARNING`: Thời gian còn lại ≤ 25% SLA (≤ 6 giờ làm việc).<br>- `BREACHED`: Đã quá hạn nhưng Ticket chưa `RESOLVED`/`CLOSED`. | Dashboard Quản lý tự động nhóm và hiển thị cảnh báo đỏ với các Ticket ở trạng thái `BREACHED`. |

---

### GROUP 4: Quy Tắc Phân Quyền File, Tài Khoản & Đánh Giá CSAT

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-12** | Phân Quyền Xem File Đính Kèm | File đính kèm lưu ở thư mục Private cách ly hoàn toàn với Web Root. Mọi API xem/tải file (`/api/v1/attachments/{file_id}`) bắt buộc verify Bearer Token và Context Ticket. | Chỉ trả file stream khi người dùng là: Sinh viên sở hữu Ticket, Nhân viên thuộc phòng ban thụ lý, hoặc Admin/Manager. Người khác trả về `403 FORBIDDEN_ACCESS`. |
| **BR-13** | Giới Hạn File Upload | - **Số lượng:** Tối đa 5 file/Ticket (đối với SV) và 3 file/Ticket (đối với kết quả xử lý của Staff).<br>- **Dung lượng:** Tối đa **5MB (5.242.880 Bytes)** / file.<br>- **Định dạng:** MIME Type thực tế (Magic Bytes) phải đúng `.pdf`, `.png`, `.jpg`, `.jpeg`. | Vi phạm dung lượng: Trả mã lỗi `400 FILE_EXCEEDS_LIMIT`. Vi phạm định dạng/magic bytes: Trả mã lỗi `400 FILE_TYPE_NOT_ALLOWED`. |
| **BR-14** | Đánh Giá Chất Lượng Dịch Vụ (CSAT) | Sinh viên chỉ được gửi Đánh giá hài lòng (`rating_score` từ 1 - 5 sao) đúng 01 lần duy nhất cho mỗi Ticket. Khi đã đánh giá, Component Đánh giá chuyển sang Read-only. | Nếu gửi lặp (Race condition): Backend kiểm tra `rating_score IS NOT NULL` và trả lỗi `409 ALREADY_RATED`. |
| **BR-15** | Vô Hiệu Hóa Phiên Khi Khóa Tài Khoản | Khi Admin chuyển trạng thái tài khoản User sang `INACTIVE`, hệ thống phải ngay lập tức vô hiệu hóa (Revoke) toàn bộ Active Sessions và Refresh Tokens của user đó trên Redis/Database. | User bị đẩy văng ra màn hình Login ngay ở thao tác API tiếp theo với mã lỗi `403 ACCOUNT_DISABLED`. |

---

## 3. Ma Trận Xử Lý Lỗi Tập Trung (Business Rules Error Matrix)

```plaintext
[Client Form Input] ────> Validation Layer (BR-01, BR-02, BR-13) ──── Lỗi ───> HTTP 400 INVALID_INPUT
                                  │
                                Hợp lệ
                                  ▼
[API Gateway] ──────────> Security & Token Check (BR-04, BR-12, BR-15) ─ Lỗi ───> HTTP 401 / 403 FORBIDDEN
                                  │
                                Hợp lệ
                                  ▼
[Service Engine] ───────> Business Rules & Concurrency Check (BR-03, BR-05, BR-14) ─ Lỗi ───> HTTP 409 CONFLICT
                                  │
                                Hợp lệ
                                  ▼
[Database Commit] ──────> State Machine & Audit Log (BR-06, BR-08, BR-09)
```

---

## 4. Bảng Mã Lỗi Business Rules Chuẩn (BR Error Code Reference)

| HTTP Status | Error Code | Quy Tắc BR Liên Quan | Mô Tả |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | BR-01, BR-02, BR-08 | Validation dữ liệu thất bại (thiếu trường, chuỗi quá ngắn/dài, chỉ chứa khoảng trắng). |
| **400** | `FILE_EXCEEDS_LIMIT` | BR-13 | File upload vượt quá 5MB hoặc quá số lượng tối đa cho phép. |
| **400** | `FILE_TYPE_NOT_ALLOWED` | BR-13 | File sai định dạng MIME thực tế (Magic Bytes check thất bại). |
| **400** | `MISSING_TRANSFER_REASON` | BR-06 | Chuyển phòng ban nhưng không nhập lý do hoặc lý do quá ngắn. |
| **400** | `INVALID_TICKET_STATE` | BR-06, BR-07 | Thao tác sai luồng FSM (ví dụ: yêu cầu bổ sung khi Ticket đã CLOSED). |
| **403** | `FORBIDDEN_ACCESS` | BR-04, BR-12 | Vi phạm quyền sở hữu Ticket hoặc quyền xem file đính kèm. |
| **403** | `ACCOUNT_DISABLED` | BR-15 | Tài khoản bị khóa, Token bị đẩy vào Blacklist. |
| **409** | `DUPLICATE_REQUEST` | BR-03 | `Client-Request-ID` bị trùng trong Redis Key lock 30 giây. |
| **409** | `TICKET_ALREADY_CLAIMED` | BR-05 | Ticket đã bị Nhân viên khác Claim trước trong race condition. |
| **409** | `ALREADY_RATED` | BR-14 | Sinh viên cố gắng gửi đánh giá lần thứ 2 cho cùng 1 Ticket. |


---

## Tài liệu nguồn: 02-domain/domain-overview.md

# Tổng Quan Nghiệp Vụ Hỗ Trợ Sinh Viên (Domain Overview)

## 1. Bối Cảnh Nghiệp Vụ Tại Aurora University
Tại **Aurora University**, dịch vụ hỗ trợ sinh viên đóng vai trò cầu nối quan trọng giữa Sinh viên và các Đơn vị/Phòng ban chuyên trách trong toàn trường. Các nhóm nghiệp vụ hỗ trợ phổ biến bao gồm:

- **Phòng Đào tạo**: Giải quyết các vấn đề đăng ký tín chỉ, miễn giảm học phần, cấp bảng điểm, xác nhận điểm, đăng ký tốt nghiệp, hoãn thi.
- **Phòng Công tác Học sinh Sinh viên (CTHSSV)**: Xác nhận sinh viên, giải quyết chế độ chính sách, học bổng, khen thưởng, kỷ luật, thẻ sinh viên, ký túc xá.
- **Phòng Tài chính - Kế toán**: Giải đáp thắc mắc về học phí, hóa đơn, hoàn phí, gia hạn nộp học phí.
- **Trung tâm Công nghệ Thông tin**: Cấp lại mật khẩu tài khoản portal, lỗi kết nối Wi-Fi, hỗ trợ phần mềm học tập, email sinh viên.
- **Thư viện & Bộ phận Khác**: Mượn trả giáo trình, cấp tài khoản thư viện số, xác nhận nghĩa vụ thư viện.

---

## 2. Mục Tiêu Chuẩn Hóa Miền Nghiệp Vụ (Domain Objectives)

Trước khi triển khai UniSupport, quy trình trao đổi mang tính thủ công, thiếu tính nhất quán và không lưu vết. Việc chuẩn hóa miền nghiệp vụ hướng tới 4 nguyên tắc cốt lõi:
```
┌────────────────────────────────────────────────────────────────────────┐
│                        4 NGUYÊN TẮC CỐT LÕI                            │
├───────────────────┬───────────────────┬────────────────┬───────────────┤
│ 1. ĐỊNH DANH      │ 2. PHÂN ĐỊNH      │ 3. LƯU VẾT     │ 4. RÕ RÀNG    │
│    DUY NHẤT       │    TRÁCH NHIỆM    │    MINH BẠCH   │    TRẠNG THÁI │
│ (Ticket ID)       │ (Department/Agent)│ (Audit Trail)  │ (Lifecycle)   │
└───────────────────┴───────────────────┴────────────────┴───────────────┘
```

1. **Định danh duy nhất (Single Identifier)**: Mọi yêu cầu từ sinh viên được đóng gói thành một đơn vị nghiệp vụ gọi là **Ticket** với một mã định danh duy nhất (Ticket ID).
2. **Phân định trách nhiệm (Ownership Assignment)**: Mỗi Ticket luôn thuộc về **01 Phòng ban phụ trách**. Sau khi trải qua bước Tiếp nhận (Claim) hoặc Phân công (Assign), Ticket mới được gắn với **01 Nhân viên thụ lý (Assignee)** chính. Ở giai đoạn khởi tạo (`NEW`) hoặc khi đang chuyển phòng ban, trường Nhân viên thụ lý có thể để trống (`NULL`).
3. **Lưu vết minh bạch (Complete Auditability)**: Tất cả hành động (chuyển trạng thái, nhắn phản hồi, chuyển phòng ban, đăng tải file) đều được ghi nhật ký và không thể sửa/xóa.
4. **Vòng đời trạng thái rõ ràng (Strict Lifecycle)**: Ticket chuyển đổi trạng thái dựa trên các quy tắc nghiệp vụ chặt chẽ, tránh trạng thái mập mờ hoặc treo không thời hạn.

---

## 3. Bản Đồ Tổng Quan Các Luồng Nghiệp Vụ (Business Process Map)
```
[Sinh viên tạo Ticket]
        │
        ▼
[Hệ thống cấp Mã Ticket & Gửi về Phòng ban]
        │
        ▼
[Nhân viên tiếp nhận (Claim) / Quản lý phân công (Assign)]
        │
        ├───► [Cần bổ sung hồ sơ] ───► [Sinh viên cập nhật file/thông tin]
        │                                        │
        │                                        │
        ├───► [Gửi nhầm phòng ban] ──► [Chuyển phòng ban chuyên trách]
        │                                        │
        ▼                                        ▼
[Xử lý & Cập nhật kết quả giải quyết] ◄──────────┘
        │
        ▼
[Sinh viên xem/đánh giá kết quả & Đóng theo vòng đời hiện có]
```


---

## Tài liệu nguồn: 02-domain/state-transition.md

# Ma Trận Chuyển Đổi Trạng Thái Ticket (State Transition Matrix)

## 1. Danh Sách Mã Trạng Thái (State Definitions)

| Mã trạng thái (`status`) | Tên hiển thị (VI) | Mô tả chi tiết & Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- |
| `NEW` | Mới tạo | Ticket vừa tạo thành công, đang nằm trong Queue chung của Phòng ban, chưa có cá nhân Nhân viên tiếp nhận. |
| `IN_PROGRESS` | Đang xử lý | Ticket đã có Nhân viên phụ trách (`assignee_id != NULL`) và đang trong tiến trình giải quyết nghiệp vụ. |
| `NEED_MORE_INFO` | Cần bổ sung | Nhân viên tạm dừng xử lý để chờ Sinh viên cung cấp thêm thông tin hoặc giấy tờ còn thiếu. |
| `TRANSFERRED` | Đã chuyển giao | Ticket đã được điều chuyển sang Phòng ban khác. Đang nằm trong Queue chờ của Phòng ban mới (`assignee_id = NULL`). |
| `REJECTED` | Từ chối xử lý | Ticket bị từ chối do nội dung vi phạm, spam hoặc không đúng quy định nhà trường. Đây là trạng thái kết thúc (Terminal State). |
| `RESOLVED` | Đã giải quyết | Nhân viên đã xử lý xong nghiệp vụ và gửi kết quả cho Sinh viên. Chờ Sinh viên nghiệm thu/đánh giá. |
| `CLOSED` | Đã đóng hoàn tất | Ticket đã kết thúc toàn bộ vòng đời (Đã được đánh giá hoặc tự động đóng sau 3 ngày). Không thể chỉnh sửa hay thay đổi trạng thái. |

---

## 2. Bảng Ma Trận Chuyển Đổi Trạng Thái (State Transition Table)

Các đường chuyển trạng thái **KHÔNG NẰM TRONG BẢNG DƯỚI ĐÂY** đều bị hệ thống cấm (trả về mã lỗi `400 INVALID_TICKET_STATE`).

| Trạng thái hiện tại | Trạng thái chuyển tới | Vai trò thực hiện | Điều kiện kích hoạt & Validation Rules | Hành động phụ kèm theo (Side Effects) |
| :--- | :--- | :--- | :--- | :--- |
| `NEW` | `IN_PROGRESS` | STAFF, MANAGER | Nhân viên bấm Tiếp nhận xử lý. Áp dụng Optimistic Locking chống tranh chấp. | - Gán `assignee_id = current_user_id`<br>- Cập nhật `priority` (nếu có chỉnh sửa). |
| `NEW` | `TRANSFERRED` | STAFF, MANAGER | Bắt buộc nhập lý do chuyển tiếp (10 - 500 ký tự). Chọn phòng ban mới khác phòng ban hiện tại. | - Đổi `department_id = target_department_id`<br>- Gán `assignee_id = NULL`<br>- Ghi vết Audit Log. |
| `NEW` | `REJECTED` | STAFF, MANAGER | Bắt buộc nhập lý do từ chối (10 - 500 ký tự). | - Gửi thông báo từ chối kèm lý do cho Sinh viên.<br>- Cập nhật `closed_at = CURRENT_TIMESTAMP`. |
| `IN_PROGRESS` | `NEED_MORE_INFO` | STAFF (Assignee) | Bắt buộc nhập nội dung yêu cầu bổ sung (10 - 1000 ký tự). | - Lưu tin nhắn vào Conversation log.<br>- Gửi Notification cho Sinh viên. |
| `IN_PROGRESS` | `TRANSFERRED` | STAFF (Assignee) | Bắt buộc nhập lý do chuyển tiếp (10 - 500 ký tự). | - Đổi `department_id = target_department_id`<br>- Gán `assignee_id = NULL`<br>- Ghi vết Audit Log. |
| `IN_PROGRESS` | `RESOLVED` | STAFF (Assignee) | Bắt buộc nhập `resolution_note` (20 - 2000 ký tự). | - Cập nhật `resolved_at = CURRENT_TIMESTAMP`<br>- Gửi thông báo kết quả cho Sinh viên. |
| `NEED_MORE_INFO` | `IN_PROGRESS` | STUDENT (Owner) | Sinh viên gửi đính kèm/lời nhắn bổ sung thành công. | - Lưu file/tin nhắn vào Conversation log.<br>- Phát thông báo cho Nhân viên phụ trách. |
| `TRANSFERRED` | `IN_PROGRESS` | STAFF (PB mới) | Nhân viên phòng ban mới bấm Tiếp nhận xử lý. | - Gán `assignee_id = current_user_id`. |
| `TRANSFERRED` | `REJECTED` | STAFF (PB mới) | Nhân viên phòng ban mới kiểm tra và từ chối. Bắt buộc nhập lý do từ chối. | - Cập nhật `closed_at = CURRENT_TIMESTAMP`. |
| `RESOLVED` | `CLOSED` | STUDENT (Owner) | Sinh viên gửi Đánh giá hài lòng (Rating 1-5 sao). | - Lưu `rating_score`, `rating_comment`, `rated_at`.<br>- Cập nhật `closed_at = CURRENT_TIMESTAMP`. |
| `RESOLVED` | `CLOSED` | SYSTEM (Cronjob) | Ticket ở trạng thái `RESOLVED` quá 03 ngày làm việc không có tương tác mới. | - Cập nhật `closed_at = CURRENT_TIMESTAMP`. |

---

## 3. Quy Tắc Bảo Mật & Phân Quyền Theo Trạng Thái (State-based Security Matrix)

| Trạng thái Ticket | Quyền của Sinh viên (Owner) | Quyền của Nhân viên (Assignee) | Quyền của Quản lý / Admin |
| :--- | :--- | :--- | :--- |
| `NEW` | Xem chi tiết. KHÔNG được chỉnh sửa nội dung. | Xem chi tiết, Claim, Transfer, Reject. | Xem chi tiết, Phân công trực tiếp cho Staff. |
| `IN_PROGRESS` | Xem tiến độ, xem tên Nhân viên phụ trách. | Xem chi tiết, Yêu cầu bổ sung, Transfer, Complete. | Xem chi tiết, Thu hồi Ticket cấp lại cho Staff khác. |
| `NEED_MORE_INFO` | Xem yêu cầu bổ sung, Được upload file / nhắn tin bổ sung. | Xem tiến độ, Chờ sinh viên phản hồi. | Xem chi tiết. |
| `TRANSFERRED` | Xem lịch sử chuyển phòng ban. | **Staff cũ:** Read-only.<br>**Staff phòng ban mới:** Xem & Claim. | Xem chi tiết. |
| `REJECTED` | Xem lý do bị từ chối (Read-only). | Read-only. | Read-only. |
| `RESOLVED` | Xem kết quả giải quyết, Được thực hiện Đánh giá (Rating). | Read-only. | Read-only. |
| `CLOSED` | Xem lại toàn bộ lịch sử & đánh giá đã gửi (Read-only). | Read-only. | Read-only. |

---

## 4. Quy Tắc Chặn Chuyển Trạng Thái Bất Hợp Lệ (Invalid Transition Rules)

1. **Không cho phép chuyển từ `NEW` thẳng sang `RESOLVED` hoặc `CLOSED`**: Bắt buộc phải qua bước tiếp nhận (`IN_PROGRESS`) để đảm bảo đúng quy trình phân công trách nhiệm.
2. **Không thể chỉnh sửa Ticket khi ở trạng thái `CLOSED`, `REJECTED`**: Đây là các Terminal State. Mọi thao tác thay đổi trạng thái đều bị vô hiệu hóa.
3. **Sinh viên không được tự chuyển trạng thái sang `RESOLVED`**: Chỉ có Nhân viên phụ trách mới có quyền ghi nhận kết quả xử lý.
4. **Không hỗ trợ mở lại Ticket đã `CLOSED`**: Nếu có vấn đề phát sinh sau khi đóng, sinh viên tạo Ticket mới.
5. **Mọi chuyển đổi trạng thái không hợp lệ đều trả về**: `400 Bad Request` với Error Code `INVALID_TICKET_STATE`.


---

## Tài liệu nguồn: 02-domain/terminology.md

# Thuật Ngữ Nghiệp Vụ (Domain Terminology)

Tài liệu này định nghĩa toàn bộ các thuật ngữ, khái niệm và từ viết tắt được sử dụng nhất quán trong tài liệu thiết kế, mã nguồn và quy trình vận hành của hệ thống **UniSupport**.

## 1. Danh Mục Thuật Ngữ Cốt Lõi

| Thuật Ngữ (English) | Thuật Ngữ (Tiếng Việt) | Định Nghĩa & Giải Thích Chi Tiết |
| :--- | :--- | :--- |
| **Ticket** | Phiếu hỗ trợ / Yêu cầu | Đơn vị dữ liệu trung tâm đại diện cho 01 yêu cầu, thắc mắc hoặc đề nghị giải quyết thủ tục của sinh viên gửi tới nhà trường. |
| **Ticket ID** | Mã phiếu hỗ trợ | Chuỗi ký tự định danh duy nhất được hệ thống tự động sinh ra khi sinh viên gửi yêu cầu thành công (Ví dụ: `TK-20261004-0001`). |
| **Category** | Nhóm vấn đề | Danh mục phân loại nội dung yêu cầu do ADMIN quản lý, ví dụ Học phí, Đăng ký môn học, Giấy xác nhận. Mỗi nhóm gắn mặc định với một phòng ban. Không đặc tả thêm phân loại nhiều cấp. |
| **Department** | Phòng ban chuyên trách | Đơn vị hành chính trong Aurora University có thẩm quyền xử lý Ticket (Ví dụ: Phòng Đào tạo, Phòng CTHSSV...). |
| **Student** | Sinh viên | Người dùng khởi tạo Ticket và là người thụ hưởng kết quả xử lý. |
| **Agent / Staff** | Nhân viên xử lý | Chuyên viên thuộc Phòng ban chức năng có nhiệm vụ tiếp nhận, xử lý và phản hồi Ticket. |
| **Manager** | Quản lý phòng ban | Giám sát, báo cáo và phân công trong phòng ban mình; không quản trị tài khoản toàn trường. |
| **Admin** | Quản trị viên | Quản trị tài khoản, vai trò, danh mục, tra soát và báo cáo toàn trường theo quyền đã có. |
| **Triage** | Phân loại & Điều phối | Quá trình kiểm tra nội dung Ticket mới để xác định đúng nhóm vấn đề, độ ưu tiên và gán cho nhân viên/phòng ban phù hợp. |
| **Claim** | Tiếp nhận | Hành động nhân viên tự nhận một Ticket chưa có người phụ trách về cho chính mình xử lý. |
| **Assign** | Phân công | Hành động gán trách nhiệm xử lý Ticket cho một nhân viên cụ thể trong cùng phòng ban. |
| **Transfer** | Chuyển phòng ban | Hành động điều chuyển Ticket từ phòng ban hiện tại sang một phòng ban khác do gửi nhầm hoặc cần phối hợp. |
| **Supplement Request** | Yêu cầu bổ sung | Yêu cầu từ nhân viên đề nghị sinh viên cung cấp thêm thông tin hoặc upload thêm giấy tờ minh chứng. |
| **SLA (Service Level Agreement)** | Cam kết thời gian xử lý | Khung thời gian tiêu chuẩn quy định hạn chót nhân viên phải phản hồi hoặc xử lý xong Ticket. |
| **Priority** | Mức độ ưu tiên | Tầm quan trọng/mức độ khẩn cấp của Ticket (Bao gồm 4 mức: *Thấp, Trung bình, Cao, Khẩn cấp*). |
| **Resolution** | Kết quả giải quyết | Nội dung trả lời, quyết định hoặc tài liệu đính kèm do nhân viên cung cấp để hoàn thành yêu cầu của sinh viên. |
| **CSAT (Customer Satisfaction)** | Mức độ hài lòng | Chỉ số đánh giá chất lượng dịch vụ do sinh viên chấm điểm (từ 1 đến 5 sao) khi Ticket đã RESOLVED hoặc CLOSED và chưa có đánh giá, theo FR-STU-04. |
| **Audit Log / Activity Log** | Nhật ký tra soát | Bản ghi lịch sử ghi nhận lại từng hành động làm thay đổi dữ liệu hoặc trạng thái của Ticket. |
| **UAT (User Acceptance Testing)** | Kiểm thử chấp nhận người dùng | Giai đoạn người dùng thực tế (sinh viên, nhân viên Aurora University) kiểm thử hệ thống trước khi vận hành chính thức. |


---

## Tài liệu nguồn: 02-domain/ticket-lifecycle.md

# Vòng Đời Phiếu Hỗ Trợ (Ticket Lifecycle)

Vòng đời của một Ticket trong hệ thống UniSupport đại diện cho toàn bộ quá trình biến chuyển từ khi Sinh viên khởi tạo yêu cầu cho đến khi được giải quyết dứt điểm và ghi nhận phản hồi.

---

## 1. Sơ Đồ Tổng Quan Các Giai Đoạn Vòng Đời

```
                            ┌──────────────┐
                            │   1. NEW     │ ──── REJECTED (Terminal)
                            └──────┬───────┘
                                   │
                    Claim / Assign  │       Transfer
                                   ▼
           ┌────────────────────────────────────────────────┐
           │              2. IN_PROGRESS                    │
           │  (assignee_id != NULL, đang xử lý nghiệp vụ) │
           └──────┬──────────────────────────────────────┬──┘
                  │                                      │
          Yêu cầu│                               Chuyển │ phòng
          bổ sung│                               ban     ▼
                  ▼                         ┌────────────────────┐
         ┌────────────────┐                 │   3. TRANSFERRED   │ ──── REJECTED (Terminal)
         │ 4. NEED_MORE_  │                 │  (Queue PB mới,    │
         │    INFO        │                 │   assignee = NULL) │
         └────────┬───────┘                 └─────────┬──────────┘
                  │                                   │
         SV bổ   │                             Claim  │ (PB mới)
         sung    │                                   │
                  ▼                                   ▼
                  └────────────────────────────────────┘
                                   │
                              Resolve
                                   ▼
                         ┌──────────────┐
                         │ 5. RESOLVED  │
                         └──────┬───────┘
                                │
                  SV Đánh giá / Cronjob 3 ngày
                                │
                                ▼
                         ┌──────────────┐
                         │  6. CLOSED   │  (Terminal State)
                         └──────────────┘
```

---

## 2. Chi Tiết Các Giai Đoạn (Lifecycle Stages)

### Giai đoạn 1: Khởi tạo (NEW)
- **Hành động kích hoạt**: Sinh viên điền form và nhấn **Gửi yêu cầu**.
- **Trạng thái hệ thống**: `NEW`.
- **Đặc điểm**:
  - Hệ thống tự động cấp **Mã Ticket duy nhất** dạng `TK-YYYYMMDD-XXXX`.
  - Ticket chưa có người thụ lý cá nhân (`assignee_id = NULL`).
  - Ticket xuất hiện trong Queue chung của Phòng ban chức năng tương ứng với `category_id` đã chọn.
  - `sla_target_at` được tính tự động = `created_at + 24 giờ làm việc`.

### Giai đoạn 2: Đang xử lý (IN_PROGRESS)
- **Hành động kích hoạt**: Nhân viên nhấn **Tiếp nhận (Claim)** hoặc Trưởng phòng **Phân công (Assign)** cho nhân viên cụ thể.
- **Trạng thái hệ thống**: `IN_PROGRESS`.
- **Đặc điểm**:
  - Ticket gắn cố định với 01 nhân viên phụ trách (`assignee_id = staff_id`).
  - Nhân viên tiến hành kiểm tra hồ sơ, xử lý nghiệp vụ, có thể yêu cầu bổ sung hoặc chuyển phòng ban.
  - Cơ chế Atomic Locking ngăn chặn 2 nhân viên Claim cùng 1 Ticket.

### Giai đoạn 3: Đã chuyển giao (TRANSFERRED)
- **Hành động kích hoạt**: Nhân viên phát hiện Ticket không đúng thẩm quyền, bấm **Chuyển phòng ban** kèm lý do.
- **Trạng thái hệ thống**: `TRANSFERRED`.
- **Đặc điểm**:
  - `department_id` cập nhật sang Phòng ban mới.
  - `assignee_id` đặt về `NULL` — Ticket nằm trong Queue chờ của Phòng ban mới.
  - Lịch sử chuyển tiếp được ghi vào Audit Log.
  - Nhân viên Phòng ban mới tiếp nhận tương tự `NEW`.

### Giai đoạn 4: Cần bổ sung thông tin (NEED_MORE_INFO)
- **Hành động kích hoạt**: Nhân viên kiểm tra hồ sơ thấy thiếu giấy tờ/thông tin và nhấn nút **Yêu cầu bổ sung**.
- **Trạng thái hệ thống**: `NEED_MORE_INFO`.
- **Đặc điểm**:
  - Hệ thống phát thông báo yêu cầu Sinh viên cập nhật.
  - Sinh viên chỉ được upload file và nhắn tin bổ sung — **KHÔNG** được chỉnh sửa `title`, `description`, `category_id` ban đầu.
  - Khi Sinh viên gửi bổ sung thành công → Trạng thái **tự động** chuyển lại về `IN_PROGRESS` (không cần nhân viên xác nhận thủ công).

### Giai đoạn 5: Đã giải quyết (RESOLVED)
- **Hành động kích hoạt**: Nhân viên hoàn tất xử lý, nhập nội dung kết quả (`resolution_note` ≥ 20 ký tự) và nhấn **Hoàn thành**.
- **Trạng thái hệ thống**: `RESOLVED`.
- **Đặc điểm**:
  - Ghi nhận mốc thời gian hoàn thành `resolved_at`.
  - Sinh viên nhận thông báo kết quả và có quyền xem nội dung giải quyết.
  - Kích hoạt bộ đếm Auto-Close: Nếu 3 ngày làm việc không có đánh giá → Cronjob tự đóng Ticket.

### Giai đoạn 6: Đóng hoàn tất (CLOSED)
- **Hành động kích hoạt**: Sinh viên xác nhận hài lòng & gửi đánh giá CSAT, HOẶC hệ thống tự động đóng sau **03 ngày làm việc** kể từ khi ở trạng thái `RESOLVED`.
- **Trạng thái hệ thống**: `CLOSED`.
- **Đặc điểm**:
  - **Terminal State**: Ticket đóng hoàn toàn, không thể chỉnh sửa hoặc thay đổi trạng thái.
  - Lưu trữ dữ liệu đầy đủ phục vụ báo cáo và thống kê KPI.

### Trạng thái Terminal Khác: Từ chối (REJECTED)
- **Hành động kích hoạt**: Nhân viên phát hiện Ticket vi phạm, spam hoặc không đúng quy định, bấm **Từ chối** kèm lý do.
- **Trạng thái hệ thống**: `REJECTED`.
- **Đặc điểm**:
  - **Terminal State**: Không thể chuyển sang trạng thái khác.
  - Sinh viên nhận thông báo kèm lý do từ chối.
  - `closed_at` được ghi nhận tại thời điểm từ chối.

---

## 3. Quy Tắc Đặc Biệt

| Quy tắc | Mô tả |
| :--- | :--- |
| **Chống mở lại Ticket CLOSED** | Không hỗ trợ Reopen. Nếu có vấn đề mới, sinh viên tạo Ticket mới. |
| **Không tự đăng ký tài khoản** | Sinh viên và Nhân viên không tự tạo tài khoản — chỉ ADMIN mới có quyền cấp. |
| **Idempotency khi tạo Ticket** | Một form gửi = tối đa 01 Ticket dù người dùng nhấn nhiều lần (Redis Key lock 30s). |
| **Auto-Close Cronjob** | Chạy lúc 23:00 mỗi ngày, tự đóng Ticket `RESOLVED` quá 3 ngày làm việc. |


---

## Tài liệu nguồn: 02-domain/ticket-model.md

# Mô Hình Dữ Liệu Ticket (Ticket Data Model)

## Phạm vi đọc tài liệu

Các bảng kiểu dữ liệu/tên trường bên dưới là mô hình kỹ thuật của bản hiện tại, được giữ nguyên trong lần sửa PRD. Chúng còn có chỗ lệch PRD (WAITING_STUDENT/CANCELLED, 10MB, giới hạn tiêu đề 255). Giới hạn **người dùng nhập liệu** lấy theo FR-STU-02/03: tiêu đề 10–150, tệp 5MB và trạng thái cần bổ sung NEED_MORE_INFO. Bảng này không được dùng để tự mở rộng giới hạn hoặc thêm trạng thái/chức năng; xem [ghi nhận sai lệch](08-project/prd-review-notes.md).

## 1. Thực Thể Cốt Lõi: Ticket (Ticket Entity)

Ticket là thực thể chính trong hệ thống UniSupport. Dưới đây là cấu trúc thuộc tính chi tiết của thực thể Ticket:

| Tên Thuộc Tính (Field) | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả & Quy Tắc Dữ Liệu |
| :--- | :--- | :---: | :--- |
| `id` | BigInt / UUID | Có | Khóa chính tự tăng hoặc chuỗi UUID định danh đằng sau database. |
| `ticket_code` | String(20) | Có | Mã Ticket hiển thị cho người dùng (Format: `TK-YYYYMMDD-XXXX`). Mã này là DUY NHẤT. |
| `title` | String(255) | Có | Tiêu đề tóm tắt yêu cầu do sinh viên nhập (Tối đa 255 ký tự). |
| `description` | Text | Có | Nội dung mô tả chi tiết vấn đề do sinh viên cung cấp. |
| `category_id` | Integer | Có | Khóa ngoại trỏ tới Bảng Nhóm vấn đề (Category). |
| `department_id` | Integer | Có | Khóa ngoại trỏ tới Bảng Phòng ban đang thụ lý. |
| `created_by_student_id` | BigInt | Có | Khóa ngoại trỏ tới Bảng Sinh viên (người tạo). |
| `assigned_staff_id` | BigInt | Không | Khóa ngoại trỏ tới Bảng Nhân viên đang thụ lý (`NULL` nếu chưa có người Claim/Assign). |
| `status` | Enum | Có | Trạng thái hiện tại: `NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`, `CANCELLED`. |
| `priority` | Enum | Có | Mức độ ưu tiên: `LOW`, `MEDIUM`, `HIGH`, `URGENT` (Mặc định: `MEDIUM`). |
| `resolution_note` | Text | Không | Nội dung ghi nhận kết quả giải quyết do Nhân viên nhập khi hoàn thành. |
| `created_at` | Timestamp | Có | Thời điểm khởi tạo Ticket. |
| `updated_at` | Timestamp | Có | Thời điểm cập nhật dữ liệu gần nhất. |
| `first_responded_at` | Timestamp | Không | Thời điểm nhân viên phản hồi đầu tiên. |
| `resolved_at` | Timestamp | Không | Thời điểm nhân viên đánh dấu Hoàn thành (`RESOLVED`). |
| `closed_at` | Timestamp | Không | Thời điểm Ticket chuyển sang Đóng hoàn toàn (`CLOSED`). |
| `sla_due_at` | Timestamp | Không | Thời hạn cam kết xử lý dựa trên độ ưu tiên và quy định phòng ban. |

---

## 2. Thực Thể Liên Quan 1: File Đính Kèm (Ticket Attachment Entity)

Lưu trữ thông tin các tệp tin đính kèm (Hình ảnh, tài liệu PDF) do Sinh viên hoặc Nhân viên tải lên.

| Tên Thuộc Tính | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :---: | :--- |
| `id` | BigInt | Có | Khóa chính tệp đính kèm. |
| `ticket_id` | BigInt | Có | Khóa ngoại liên kết với Ticket. |
| `file_name` | String(255) | Có | Tên gốc của file do người dùng tải lên (Ví dụ: `BangDiem_Ky1.pdf`). |
| `file_path` | String(500) | Có | Đường dẫn lưu trữ file trên hệ thống/bộ nhớ bảo mật. |
| `file_size` | Integer | Có | Dung lượng file (tính bằng Bytes, tối đa 10MB = 10,485,760 Bytes). |
| `mime_type` | String(100) | Có | Định dạng file (`application/pdf`, `image/jpeg`, `image/png`). |
| `uploaded_by_user_id` | BigInt | Có | ID người dùng thực hiện upload file. |
| `created_at` | Timestamp | Có | Thời điểm upload. |

---

## 3. Thực Thể Liên Quan 2: Nhật Ký Trao Đổi / Tra Soát (Ticket Comment & Activity Log)

Lưu vết toàn bộ tiến trình trao đổi giữa Sinh viên và Nhân viên, cũng như các sự kiện hệ thống.

| Tên Thuộc Tính | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :---: | :--- |
| `id` | BigInt | Có | Khóa chính dòng log. |
| `ticket_id` | BigInt | Có | Khóa ngoại trỏ tới Ticket. |
| `sender_type` | Enum | Có | Loại người gửi: `STUDENT`, `STAFF`, `SYSTEM`. |
| `sender_id` | BigInt | Có | ID tài khoản thực hiện thao tác. |
| `content` | Text | Có | Nội dung tin nhắn, yêu cầu bổ sung hoặc mô tả thay đổi trạng thái tự động. |
| `is_internal_note` | Boolean | Có | `TRUE`: Ghi chú nội bộ (chỉ nhân viên thấy); `FALSE`: Phản hồi công khai (sinh viên nhìn thấy). |
| `created_at` | Timestamp | Có | Thời điểm ghi nhận log. |

---

## 4. Thực Thể Liên Quan 3: Đánh Giá Hài Lòng (Ticket Rating Entity)

Lưu trữ đánh giá của sinh viên sau khi Ticket được xử lý xong.

| Tên Thuộc Tính | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :---: | :--- |
| `id` | BigInt | Có | Khóa chính bản ghi đánh giá. |
| `ticket_id` | BigInt | Có | Khóa ngoại trỏ tới Ticket (Mỗi Ticket chỉ có tối đa 01 Rating). |
| `score` | Integer | Có | Điểm số đánh giá từ `1` đến `5` sao. |
| `comment` | Text | Không | Phản hồi/góp ý chi tiết của sinh viên. |
| `created_at` | Timestamp | Có | Thời điểm sinh viên thực hiện đánh giá. |


---

## Tài liệu nguồn: 03-modules/M01-student-portal/README.md

# M01 — Chỉ mục PRD và đối chiếu Resources

## Danh mục yêu cầu đã chốt

Nguồn mô tả chi tiết: [prd.md](03-modules/M01-student-portal/prd.md). Danh mục dưới đây dùng mã FR của PRD, không lấy số thứ tự công việc Resources làm mã FR.

| Mã FR | Tên yêu cầu |
| --- | --- |
| FR-STU-01 | Đăng nhập tài khoản sinh viên |
| FR-STU-02 | Gửi yêu cầu hỗ trợ (Tạo Ticket) |
| FR-STU-03 | Theo dõi tiến độ & Bổ sung thông tin/giấy tờ |
| FR-STU-04 | Xem kết quả giải quyết & Đánh giá mức độ hài lòng |

## Luồng người dùng

ADMIN cấp tài khoản → Sinh viên đăng nhập (FR-STU-01) → Gửi yêu cầu (FR-STU-02) → Theo dõi/bổ sung khi cần (FR-STU-03) → Xem kết quả và đánh giá (FR-STU-04).

Nhóm vấn đề là danh mục nội dung yêu cầu do ADMIN quản lý và gắn phòng ban mặc định. Tệp sinh viên tối đa 5 tệp, 5MB/tệp; tệp kết quả nhân viên tối đa 3 tệp, 5MB/tệp; định dạng PDF, PNG, JPG, JPEG theo PRD. “Cần bổ sung” dùng mã NEED_MORE_INFO; “Đã giải quyết” dùng RESOLVED, “Đã đóng” dùng CLOSED. Xem lại trang Ticket không phải mở lại xử lý.

## Đối chiếu giờ Resources

Nguồn là sheet **Resource** của workbook, không có sheet riêng mang tên M1/M2/M3. Tổng nhóm 124 giờ cơ sở + 4 giờ dự phòng = **128 giờ kế hoạch**. Một dòng giờ có thể được nhiều FR dùng chung; không cộng lại hay tự chia giờ giữa các FR.

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-STU-01 | 3 | Tra cứu hướng dẫn & FAQ | 3 | 3 | 0 | 4 | 0 | 0 | 0 | 4 | 14 | 0 | 14 | Chưa có FR FAQ được chốt; giữ dòng nguồn, không thay mã đăng nhập |
| R-STU-02 | 4 | Tạo & gửi yêu cầu hỗ trợ | 5 | 5 | 1 | 10 | 1 | 6 | 1 | 5 | 34 | 3 | 37 | FR-STU-02 |
| R-STU-03 | 5 | Xem & theo dõi yêu cầu | 4 | 3 | 1 | 8 | 3 | 5 | 3 | 5 | 32 | 1 | 33 | FR-STU-03 |
| R-STU-04 | 6 | Nhận thông báo trạng thái | 3 | 1 | 0 | 4 | 0 | 4 | 4 | 3 | 19 | 0 | 19 | FR-STU-03; thông báo trạng thái đã có |
| R-STU-05 | 7 | Bổ sung thông tin & phản hồi | 3 | 1 | 0 | 5 | 3 | 5 | 3 | 5 | 25 | 0 | 25 | FR-STU-03; FR-STU-04 (đối chiếu phần phản hồi/đánh giá; chưa có phân bổ riêng) |
| Tổng | — | Mỗi dòng tính một lần | 18 | 13 | 2 | 31 | 7 | 20 | 11 | 22 | 124 | 4 | 128 | Không cộng lại khi nhiều FR dùng chung |

Xem [giới hạn và những tên công việc chưa có đặc tả thống nhất](Phan_bo_Resources_Antigravity.md). Không tự bổ sung FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ hoặc UI dọn dẹp chỉ vì tên công việc có trong bảng nguồn.


---

## Tài liệu nguồn: 03-modules/M01-student-portal/prd.md

# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Sinh Viên (PRD - M01 Student Portal)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Sinh viên (Student Portal)** là cổng giao tiếp số tập trung dành cho khoảng 3.000 sinh viên tại **Aurora University**. Phân hệ cho phép sinh viên đăng nhập bằng tài khoản do ADMIN cấp, tạo phiếu hỗ trợ (Ticket), theo dõi tiến độ giải quyết, bổ sung giấy tờ khi được yêu cầu, nhận thông báo cập nhật và đánh giá chất lượng dịch vụ.

### Luồng sử dụng và trách nhiệm

Sinh viên đăng nhập bằng tài khoản ADMIN cấp tại cổng sinh viên. Sinh viên tạo yêu cầu hỗ trợ và theo dõi tiến độ tại đây. Khi nhân viên yêu cầu bổ sung, sinh viên nộp tại FR-STU-03. Khi yêu cầu được giải quyết, sinh viên xem kết quả và đánh giá tại FR-STU-04.

Hệ thống không hỗ trợ tự đăng ký tài khoản. Sinh viên không được chỉnh sửa nội dung Ticket (`title`, `category_id`, `description`) sau khi đã gửi, kể cả khi Ticket đang ở `NEED_MORE_INFO`.

### Danh mục Chức năng Cốt lõi

- **[FR-STU-01]** Đăng nhập tài khoản sinh viên.
- **[FR-STU-02]** Gửi yêu cầu hỗ trợ (Tạo Ticket kèm file đính kèm ảnh/PDF).
- **[FR-STU-03]** Theo dõi tiến độ, xem lịch sử xử lý & bổ sung thông tin/giấy tờ theo yêu cầu.
- **[FR-STU-04]** Xem kết quả giải quyết & Đánh giá mức độ hài lòng.

---

### Nhóm vấn đề và phòng ban tiếp nhận

| Nội dung | Quy tắc đã có trong PRD gốc |
| --- | --- |
| Ý nghĩa nhóm vấn đề | Phân loại nội dung yêu cầu, ví dụ Học phí, Đăng ký môn học, Giấy xác nhận; đây là ví dụ, không phải danh mục mới cố định. |
| Nguồn và chủ sở hữu | Danh mục hệ thống do ADMIN quản lý; sinh viên chọn từ danh sách có sẵn, không tự tạo danh mục tại form gửi yêu cầu. |
| Phòng ban | Mỗi nhóm vấn đề gắn mặc định với một phòng ban nhận yêu cầu. Sinh viên chọn nhóm vấn đề; không nhầm tên phòng ban với tên nhóm vấn đề. |
| Nhân viên | Phân loại lại bằng danh mục phòng ban tại FR-STF-02; chuyển phòng ban tại FR-STF-03 khi cần. |

### Giới hạn công sức và mã yêu cầu

Mã FR trong danh mục dưới đây giữ nguyên theo PRD đã chốt. Giờ M01 được đối chiếu theo các dòng Resource!3:7: **124 giờ cơ sở + 4 giờ dự phòng = 128 giờ kế hoạch**. Xem [bảng Resources](Phan_bo_Resources_Antigravity.md); số thứ tự dòng công sức không phải mã FR. Đăng nhập các cổng dùng chung R-ADM-01, không có estimate bổ sung. Những tên công việc nguồn chưa có đặc tả thống nhất không tự trở thành chức năng mới.

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STU-01] Đăng nhập tài khoản sinh viên

#### 1. Mô tả & Phạm vi
Cho phép Sinh viên đăng nhập vào Cổng Sinh viên UniSupport bằng tài khoản cá nhân (Mã sinh viên / Email trường) do Quản trị viên hệ thống (ADMIN) khởi tạo và cấp sẵn.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên dùng tài khoản đã được ADMIN cấp để đăng nhập vào cổng sinh viên.
2. Đăng nhập thành công thì vào trang danh sách yêu cầu cá nhân.
3. Sai thông tin hoặc tài khoản bị khóa thì hiển thị thông báo tương ứng; không tạo phiên làm việc.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên Aurora University.
- **Preconditions:** Tài khoản đã được ADMIN khởi tạo theo FR-MNG-04, ở trạng thái `ACTIVE`, có `role = STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Trường dữ liệu đầu vào:**
  - **Username / Email:** Bắt buộc, tự động `trim()` khoảng trắng hai đầu.
  - **Password:** Bắt buộc, độ dài 6 - 50 ký tự.
- **Scope & Session Context:** Sau khi xác thực thành công, Token phải chứa: `user_id`, `role = STUDENT`, `department_id = NULL`, `permissions_list`.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Trạng thái Nút Đăng nhập:** Disable khi thông tin trống. Chuyển Loading (kèm spinner) và khóa toàn bộ Form khi request đang xử lý.
- **Redirect Rule:** Đăng nhập thành công → Tự động điều hướng về `/student/tickets`.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập `/student/login`.
2. Kiểm tra phiên làm việc: Nếu Token hợp lệ → Chuyển hướng sang `/student/tickets`.
3. Nhập Username/Email và Password, nhấn Đăng nhập (hoặc phím Enter).
4. Client validate form → Gửi request đăng nhập.
5. Server xác thực thông tin, kiểm tra vai trò `STUDENT`:
   - Trả về Token xác thực (JWT) + Profile (`student_id`, `full_name`).
6. Client lưu Token an toàn, chuyển hướng sang `/student/tickets`.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Credential không đúng (401 Unauthorized):** Hiển thị Alert error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản không phải STUDENT (403 Forbidden):** Hiển thị Alert error: *"Tài khoản của bạn không có quyền truy cập cổng Sinh viên."*
- **Tài khoản bị khóa (403 Forbidden / INACTIVE):** Hiển thị Alert error: *"Tài khoản đã bị vô hiệu hóa. Vui lòng liên hệ Quản trị viên."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập đúng tài khoản Student → Chuyển sang trang danh sách Ticket cá nhân trong dưới 1.5s.
- **AC-02:** Tài khoản Staff/Manager cố gắng đăng nhập tại cổng Student → Báo lỗi 403 từ chối truy cập.
- **AC-03:** Click Đăng nhập liên tiếp → Chỉ phát sinh 01 request duy nhất.

---

### [FR-STU-02] Gửi yêu cầu hỗ trợ (Tạo Ticket)

#### 1. Mô tả & Phạm vi
Cho phép sinh viên khởi tạo một yêu cầu hỗ trợ mới bằng cách chọn nhóm vấn đề (Category), nhập tiêu đề, nội dung chi tiết và đính kèm tài liệu minh chứng. Hệ thống tự động sinh mã Ticket duy nhất và phân tuyến đến đúng phòng ban phụ trách theo danh mục đã chọn.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên bấm tạo yêu cầu mới, chọn nhóm vấn đề từ danh mục phòng ban cung cấp, nhập tiêu đề và nội dung, đính kèm file nếu cần.
2. Bấm Gửi; nút vô hiệu hóa ngay để chống bấm đúp. Thành công thì hiển thị mã Ticket và thông báo.
3. Ticket vào hàng đợi đúng phòng ban theo danh mục đã chọn; sinh viên theo dõi tiến độ tại FR-STU-03.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Tài khoản `ACTIVE`, có `role = STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Nhóm vấn đề (`category_id`):** Bắt buộc chọn từ Dropdown danh mục được cấu hình bởi ADMIN.
- **Tiêu đề (`title`):** Bắt buộc, 10 - 150 ký tự. Tự động `trim()`.
- **Nội dung mô tả (`description`):** Bắt buộc, 20 - 2000 ký tự. Tự động `trim()`.
- **File đính kèm (`attachments`):** Không bắt buộc. Tối đa **5 file/Ticket**. Mỗi file ≤ **5MB (5.242.880 Bytes)**. Định dạng MIME thực tế (Magic Bytes): `.pdf`, `.png`, `.jpg`, `.jpeg`.
- **Chống trùng lặp (Idempotency):** Client sinh `Client-Request-ID` (UUID v4) khi mở form, gửi kèm trong Header. Server khóa Redis Key trong 30 giây.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Nút Gửi:** Vô hiệu hóa ngay khi bấm lần đầu, chuyển trạng thái Loading để chống đúp click.
- **Thành công:** Hiển thị Toast: *"Yêu cầu [Mã_Ticket] đã được gửi thành công!"* và điều hướng sang trang chi tiết Ticket.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập `/student/tickets/new`.
2. Client sinh `Client-Request-ID` (UUID v4) và gắn vào state form.
3. Sinh viên chọn `category_id`, nhập `title` và `description`, đính kèm file (nếu có).
4. Sinh viên nhấn **Gửi yêu cầu**. Client vô hiệu hóa nút và chuyển Loading.
5. Client validate client-side (độ dài, file type, file size).
6. Client gửi request `POST /api/v1/student/tickets` kèm Header `X-Client-Request-ID`.
7. Server xử lý:
   - Kiểm tra `Client-Request-ID` trong Redis → Nếu trùng, trả về `409 DUPLICATE_REQUEST`.
   - Đọc `student_id` từ JWT (bỏ qua mọi `student_id` gửi từ body).
   - Sinh mã Ticket `TK-YYYYMMDD-XXXX` qua Redis Atomic Counter.
   - Lưu Ticket, upload file lên Private Storage, ghi Audit Log.
   - Phát Notification tới Queue phòng ban tương ứng.
8. Server trả về `HTTP 201 Created` kèm `ticket_id`, `status = NEW`, `sla_target_at`.
9. Client hiển thị Toast thành công và điều hướng sang `/student/tickets/{ticket_id}`.

#### 6. Luồng ngoại lệ & Mã lỗi (Exception & Error Flows)

| Tình huống ngoại lệ | Mã lỗi HTTP & Error Code | Message hiển thị cho Sinh viên | Hành động xử lý của Client |
| :--- | :--- | :--- | :--- |
| **Thiếu thông tin bắt buộc / Nhập toàn space** | `400 Bad Request`<br><br>`INVALID_INPUT` | "Vui lòng chọn nhóm vấn đề, nhập tiêu đề từ 10 đến 150 ký tự và mô tả từ 20 đến 2000 ký tự." | Hiển thị lỗi dưới input field tương ứng, kích hoạt lại nút Gửi. |
| **File quá dung lượng (> 5MB)** | `400 Bad Request`<br><br>`FILE_EXCEEDS_LIMIT` | "File [Tên_File] vượt quá dung lượng cho phép (tối đa 5MB)." | Đánh dấu đỏ file lỗi trong danh sách upload, từ chối gửi request. |
| **File sai định dạng / Giả mạo đuôi file** | `400 Bad Request`<br><br>`FILE_TYPE_NOT_ALLOWED` | "Chỉ chấp nhận file định dạng PDF hoặc hình ảnh (PNG, JPG, JPEG)." | Loại bỏ file không hợp lệ khỏi danh sách đính kèm. |
| **Mạng lag / Bấm gửi nhiều lần liên tiếp** | `409 Conflict`<br><br>`DUPLICATE_REQUEST` | "Yêu cầu của bạn đang được xử lý. Vui lòng không bấm liên tục." | Client giữ nguyên giao diện Loading, chặn gửi request trùng thứ hai. |
| **Lỗi Server / Storage ngắt kết nối** | `500 Internal Server Error`<br><br>`INTERNAL_SERVER_ERROR` | "Không thể tạo yêu cầu do sự cố hệ thống. Vui lòng thử lại sau." | Báo Toast error, giữ nguyên dữ liệu đã nhập trên Form để bấm thử lại. |

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Nhập đúng và đủ thông tin → Tạo đúng 01 Ticket với mã duy nhất `TK-YYYYMMDD-XXXX`, trạng thái `NEW`.
- **AC-02:** Click Gửi liên tục nhiều lần → Hệ thống chỉ tạo 01 Ticket duy nhất (kiểm tra cả Client-side disable lẫn Server-side idempotency).
- **AC-03:** File đính kèm lưu an toàn ở Private Storage và hiển thị đúng trong chi tiết Ticket.
- **AC-04:** Upload file 12MB → Client chặn ngay với thông báo *"Dung lượng tệp vượt quá 5MB cho phép"*.
- **AC-05:** Upload file `.mp4` → Client/Server từ chối với thông báo định dạng không hợp lệ.

---

### [FR-STU-03] Theo dõi tiến độ & Bổ sung thông tin/giấy tờ

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem danh sách Ticket cá nhân, theo dõi trạng thái xử lý theo thời gian thực và thực hiện bổ sung thông tin/file đính kèm khi Ticket ở trạng thái `NEED_MORE_INFO`.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên mở danh sách yêu cầu, lọc hoặc tìm theo mã, mở chi tiết để đọc lịch sử cập nhật và thông tin người phụ trách.
2. Khi nhận thông báo cần bổ sung, sinh viên mở yêu cầu đang ở `NEED_MORE_INFO`, đọc nội dung nhân viên yêu cầu, tải file và/hoặc nhập lời nhắn bổ sung rồi gửi.
3. Gửi thành công thì trạng thái tự động đổi về `IN_PROGRESS` và nhân viên nhận thông báo; sinh viên tiếp tục theo dõi.
4. Trong suốt quá trình bổ sung, sinh viên không được chỉnh sửa `title`, `category_id` hay `description` ban đầu.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions (xem danh sách):** Tài khoản `ACTIVE`, có `role = STUDENT`.
- **Preconditions (bổ sung):** Ticket đang ở trạng thái `NEED_MORE_INFO` và `student_id == current_user.id`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Phân quyền dữ liệu:** Sinh viên chỉ xem và thao tác trên Ticket do chính mình tạo (`WHERE student_id == current_user_id`).
- **Nội dung bổ sung (`supplement_note`):** Không bắt buộc, tối đa 1.000 ký tự. Tự động `trim()`.
- **File bổ sung:** Tối đa **5 file** mỗi lần gửi. Mỗi file ≤ **5MB**. Định dạng MIME: `.pdf`, `.png`, `.jpg`, `.jpeg`.
- **Ràng buộc:** Phải có ít nhất 01 file đính kèm hoặc 01 lời nhắn bổ sung (không được gửi trống hoàn toàn).
- **Không cho chỉnh sửa nội dung gốc:** `title`, `description`, `category_id` ở trạng thái Read-Only trong mọi trường hợp.

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên truy cập `/student/tickets` → Xem danh sách Ticket sắp xếp theo `created_at DESC`.
2. Sinh viên lọc theo trạng thái (`NEW`, `IN_PROGRESS`, `NEED_MORE_INFO`, `TRANSFERRED`, `RESOLVED`, `CLOSED`, `REJECTED`) hoặc tìm theo mã Ticket.
3. Sinh viên nhấn vào một Ticket để mở trang Chi tiết `/student/tickets/{ticket_id}`.
4. Trang chi tiết hiển thị: Tiêu đề, mô tả, trạng thái, nhân viên phụ trách (nếu có), Timeline lịch sử, file đính kèm gốc.
5. **Nếu Ticket ở `NEED_MORE_INFO`:**
   - Hệ thống tự động mở Khung Bổ sung thông tin kèm nội dung yêu cầu từ Nhân viên.
   - Các trường `title`, `category_id` hiển thị Read-Only.
   - Sinh viên nhập `supplement_note` (tùy chọn) và/hoặc đính kèm file bổ sung.
   - Sinh viên nhấn **Xác nhận gửi bổ sung**.
   - Client validate, gửi `POST /api/v1/student/tickets/{ticket_id}/supplement`.
   - Server kiểm tra `status == NEED_MORE_INFO`, cập nhật `status = IN_PROGRESS`, lưu Conversation log, phát Notification cho Nhân viên.
   - Client hiển thị Toast: *"Đã gửi hồ sơ bổ sung thành công!"*, đóng Khung bổ sung và cập nhật Badge trạng thái.

#### 5. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Truy cập Ticket của người khác:** Server trả `403 FORBIDDEN_ACCESS`. Message: *"Không tìm thấy yêu cầu hoặc bạn không có quyền truy cập."*
- **Gửi bổ sung mà không có file và note:** Báo lỗi validation: *"Vui lòng tải lên ít nhất 01 file đính kèm hoặc nhập lời nhắn bổ sung."*
- **Upload file bổ sung sai định dạng/quá 5MB:** Sai định dạng hiển thị lỗi `400 FILE_TYPE_NOT_ALLOWED`; quá 5MB hiển thị lỗi `400 FILE_EXCEEDS_LIMIT`, theo bảng mã lỗi đã có. Đánh dấu đỏ file lỗi, ngăn submit.
- **Ticket không còn ở `NEED_MORE_INFO` khi submit:** `400 INVALID_TICKET_STATE`. Reload lại dữ liệu Ticket để cập nhật UI.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Danh sách Ticket chỉ hiển thị đúng Ticket của sinh viên đang đăng nhập.
- **AC-02:** Timeline hiển thị đúng trình tự thời gian các bước chuyển trạng thái và lịch sử trao đổi.
- **AC-03:** Sinh viên sao chép URL Ticket của bạn học và mở → Hệ thống trả về lỗi `403 Forbidden`.
- **AC-04:** Gửi bổ sung thành công → Trạng thái Ticket tự động đổi sang `IN_PROGRESS`, nhân viên nhận được thông báo.
- **AC-05:** Nhân viên gửi yêu cầu bổ sung theo FR-STF-04 → Sinh viên thấy đúng nội dung cần bổ sung tại cùng mã Ticket; gửi bổ sung thành công → Nhân viên xem được phần bổ sung trong lịch sử của Ticket đó.

---

### [FR-STU-04] Xem kết quả giải quyết & Đánh giá mức độ hài lòng

#### 1. Mô tả & Phạm vi
Cho phép sinh viên xem nội dung phản hồi kết quả xử lý cuối cùng từ nhà trường và thực hiện đánh giá chất lượng dịch vụ cho Ticket đã hoàn tất.

**Luồng thao tác nghiệp vụ:**

1. Sinh viên mở yêu cầu đã giải quyết/đã đóng của mình và đọc câu trả lời, tệp kết quả nếu có và thời gian hoàn thành.
2. Nếu chưa đánh giá, sinh viên chọn 1–5 sao, nhập nhận xét nếu muốn rồi gửi; nếu đã đánh giá thì chỉ xem lại đánh giá đã lưu.
3. Gửi thành công thì hiển thị lời cảm ơn và đánh giá ở chế độ chỉ đọc. Khi lỗi mạng, giữ số sao và nhận xét để thử lại theo AC-04.
4. Mở lại trang chi tiết để xem hoặc đánh giá không có nghĩa mở lại quá trình xử lý Ticket.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Sinh viên đã đăng nhập.
- **Preconditions:** Ticket của sinh viên đã được Nhân viên/Quản lý xử lý xong và chuyển sang trạng thái `RESOLVED` hoặc `CLOSED`.

#### 3. Quy tắc Dữ liệu & Đánh giá (Business & Validation Rules)
- **Trường thông tin Đánh giá:**
  - **Rating (`rating_score`):** Bắt buộc, số nguyên từ 1 đến 5 (tương ứng từ 1 sao đến 5 sao).
  - **Feedback / Comment (`rating_comment`):** Không bắt buộc, tối đa 500 ký tự. Tự động `trim()`.
- **Ràng buộc số lần đánh giá:** Mỗi Ticket chỉ được đánh giá duy nhất **01 lần**.
- **Khóa biểu mẫu:** Khi Ticket đã có dữ liệu đánh giá, hệ thống chuyển Form đánh giá sang trạng thái Read-Only (Hiển thị số sao và nhận xét đã gửi, không cho thao tác bấm gửi lại).

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Sinh viên mở chi tiết Ticket đã xử lý xong tại `/student/tickets/{ticket_id}`.
2. Hệ thống hiển thị rõ ràng phần Kết quả giải quyết (Gồm câu trả lời, file đính kèm kết quả từ nhân viên nếu có, thời gian hoàn thành).
3. Kiểm tra trạng thái đánh giá của Ticket:
   - Chưa đánh giá: Hiển thị Component Đánh giá (5 ngôi sao tương tác + Textarea nhập nhận xét + Nút Gửi đánh giá).
   - Đã đánh giá: Hiển thị kết quả đánh giá cũ dạng Read-only.
4. Sinh viên chọn số sao, nhập nhận xét và bấm **Gửi đánh giá**.
5. Client gửi request `POST /api/v1/student/tickets/{ticket_id}/rate`.
6. Server ghi nhận thông tin đánh giá, chuyển trạng thái Ticket từ `RESOLVED` sang `CLOSED` (nếu đang ở `RESOLVED`), lưu timestamp `rated_at`.
7. Client hiển thị Toast thông báo: *"Cảm ơn bạn đã đánh giá dịch vụ!"*, đồng thời chuyển Component đánh giá sang dạng Read-only.

#### 5. Luồng ngoại lệ & Race Condition Handling
- **Lỗi mạng khi gửi đánh giá:** Hiển thị *"Chưa gửi được đánh giá. Vui lòng thử lại."* và giữ nguyên số sao, nhận xét đã nhập theo AC-04.
- **Đánh giá đồng thời nhiều tab (Race Condition):** Nếu sinh viên mở 2 tab cùng 1 Ticket và bấm gửi ở tab A trước:
  - **Tab A:** Gửi thành công.
  - **Tab B:** Khi bấm gửi, Server trả về mã lỗi `409 ALREADY_RATED` với message: *"Ticket này đã được đánh giá trước đó."*
  - **Client tại Tab B nhận lỗi:** Tự động ẩn form nhập và fetch lại dữ liệu đánh giá đã lưu để hiển thị dạng Read-only.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đánh giá 5 sao + nhận xét hợp lệ → Lưu chính xác dữ liệu vào hệ thống, hiển thị đúng trạng thái đã đánh giá.
- **AC-02:** Không chọn số sao mà bấm Gửi → Báo lỗi validation: *"Vui lòng chọn mức độ hài lòng (từ 1 đến 5 sao)"*.
- **AC-03:** Sau khi gửi đánh giá thành công, F5 lại trang hoặc mở lại trang chi tiết Ticket → Form đánh giá ở trạng thái Read-only, không thể chỉnh sửa hay gửi lại.
- **AC-04:** Lỗi mạng khi gửi đánh giá → Thông báo lỗi, giữ nguyên số sao và nhận xét sinh viên đã nhập trên giao diện để sinh viên bấm thử lại.

---

## III. BẢNG MÃ LỖI CHUẨN DÙNG CHUNG CHO DEV (SYSTEM ERROR CODES)

Để Frontend và Backend đồng bộ xử lý không cần trao đổi thêm, phân hệ áp dụng chuẩn response lỗi như sau:

| HTTP Status | Error Code | Message hiển thị người dùng | Kịch bản áp dụng |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | *"Dữ liệu nhập vào không hợp lệ. Vui lòng kiểm tra lại."* | Lỗi validation trường dữ liệu đầu vào. |
| **400** | `FILE_EXCEEDS_LIMIT` | *"File đính kèm vượt quá dung lượng 5MB."* | Upload file > 5MB. |
| **400** | `FILE_TYPE_NOT_ALLOWED` | *"Chỉ chấp nhận file .pdf, .png, .jpg, .jpeg."* | Upload sai định dạng file. |
| **401** | `UNAUTHORIZED` | *"Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại."* | Token hết hạn hoặc không hợp lệ. |
| **403** | `FORBIDDEN_ACCESS` | *"Bạn không có quyền truy cập vào tài nguyên này."* | Sinh viên xem Ticket của người khác. |
| **404** | `TICKET_NOT_FOUND` | *"Không tìm thấy dữ liệu Ticket yêu cầu."* | Ticket ID không tồn tại. |
| **409** | `ALREADY_RATED` | *"Ticket này đã được đánh giá trước đó."* | Gửi đánh giá 2 lần cho 1 Ticket. |
| **409** | `DUPLICATE_REQUEST` | *"Yêu cầu đang được xử lý, vui lòng không thao tác lặp lại."* | Trùng Client-Request-ID. |
| **500** | `INTERNAL_SERVER_ERROR` | *"Hệ thống gặp sự cố kỹ thuật. Vui lòng thử lại sau."* | Lỗi Server/Database unhandled. |


---

## Tài liệu nguồn: 03-modules/M02-staff-operations/README.md

# M02 — Chỉ mục PRD và đối chiếu Resources

## Danh mục yêu cầu đã chốt

Nguồn mô tả chi tiết: [prd.md](03-modules/M02-staff-operations/prd.md). Danh mục dưới đây dùng mã FR của PRD, không lấy số thứ tự công việc Resources làm mã FR.

| Mã FR | Tên yêu cầu |
| --- | --- |
| FR-STF-01 | Nhân viên đăng nhập hệ thống |
| FR-STF-02 | Tiếp nhận và phân loại yêu cầu (Claim & Triage) |
| FR-STF-03 | Chuyển yêu cầu sang đúng phòng ban |
| FR-STF-04 | Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement) |
| FR-STF-05 | Ghi kết quả và hoàn tất xử lý yêu cầu |

## Luồng người dùng

Nhân viên đăng nhập (FR-STF-01) → Tiếp nhận/phân loại (FR-STF-02) → Chuyển phòng nếu cần (FR-STF-03), hoặc yêu cầu bổ sung (FR-STF-04) → Ghi kết quả/hoàn tất (FR-STF-05).

Nhóm vấn đề là danh mục nội dung yêu cầu do ADMIN quản lý và gắn phòng ban mặc định. Tệp sinh viên tối đa 5 tệp, 5MB/tệp; tệp kết quả nhân viên tối đa 3 tệp, 5MB/tệp; định dạng PDF, PNG, JPG, JPEG theo PRD. “Cần bổ sung” dùng mã NEED_MORE_INFO; “Đã giải quyết” dùng RESOLVED, “Đã đóng” dùng CLOSED. Xem lại trang Ticket không phải mở lại xử lý.

## Đối chiếu giờ Resources

Nguồn là sheet **Resource** của workbook, không có sheet riêng mang tên M1/M2/M3. Tổng nhóm 187 giờ cơ sở + 10 giờ dự phòng = **197 giờ kế hoạch**. Một dòng giờ có thể được nhiều FR dùng chung; không cộng lại hay tự chia giờ giữa các FR.

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-STF-01 | 12 | Tiếp nhận, tìm kiếm & lọc yêu cầu | 3 | 3 | 1 | 4 | 5 | 8 | 3 | 6 | 33 | 0 | 33 | FR-STF-02; Queue phòng ban đã có |
| R-STF-02 | 13 | Phân loại & phân công xử lý | 4 | 0 | 3 | 4 | 3 | 9 | 5 | 9 | 37 | 1 | 38 | FR-STF-02; quyền phân công MANAGER/ADMIN đã có |
| R-STF-03 | 14 | Quản lý ưu tiên & thời hạn | 4 | 0 | 4 | 3 | 3 | 6 | 3 | 3 | 26 | 3 | 29 | FR-STF-02; FR-MNG-02 |
| R-STF-04 | 15 | Xử lý & cập nhật yêu cầu | 4 | 1 | 1 | 4 | 4 | 9 | 4 | 9 | 36 | 3 | 39 | FR-STF-04 |
| R-STF-05 | 16 | Chuyển xử lý, Escalation & hoàn tất | 3 | 0 | 3 | 3 | 3 | 8 | 4 | 5 | 29 | 3 | 32 | FR-STF-03; FR-STF-05 |
| R-STF-06 | 17 | Đóng & mở lại yêu cầu | 3 | 0 | 1 | 3 | 3 | 8 | 3 | 5 | 26 | 0 | 26 | FR-STF-05; FR-STU-04; không chốt phần mở lại xử lý |
| Tổng | — | Mỗi dòng tính một lần | 21 | 4 | 13 | 21 | 21 | 48 | 22 | 37 | 187 | 10 | 197 | Không cộng lại khi nhiều FR dùng chung |

Xem [giới hạn và những tên công việc chưa có đặc tả thống nhất](Phan_bo_Resources_Antigravity.md). Không tự bổ sung FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ hoặc UI dọn dẹp chỉ vì tên công việc có trong bảng nguồn.


---

## Tài liệu nguồn: 03-modules/M02-staff-operations/prd.md

# Đặc Tả Yêu Cầu Sản Phẩm - Phân Hệ Nhân Viên (PRD - M02 Staff Operations)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Nhân viên (Staff Operations)** cung cấp không gian làm việc chuyên môn cho Cán bộ / Nhân viên các phòng ban tại Aurora University. Phân hệ bao gồm các nhóm chức năng chính: Quản lý Queue Ticket phòng ban, Tiếp nhận & Phân loại, Chuyển tiếp liên phòng ban, Yêu cầu bổ sung hồ sơ, Cập nhật tiến độ xử lý, Ghi nhận kết quả và Đóng Ticket.

### 1. Luồng sử dụng và trách nhiệm

Nhân viên đăng nhập bằng tài khoản do ADMIN cấp và gán phòng ban. Nhân viên xem hàng đợi phòng ban, tiếp nhận yêu cầu chưa có người xử lý, kiểm tra nội dung, yêu cầu bổ sung nếu thiếu, chuyển phòng ban nếu cần hoặc ghi kết quả khi đã xử lý xong. Sinh viên theo dõi và bổ sung tại M01; kết quả được xem và đánh giá tại FR-STU-04.

Tiếp nhận là nhận yêu cầu về xử lý cá nhân. Chuyển phòng ban là bàn giao yêu cầu vào hàng đợi của đơn vị khác. Phân công/thu hồi/phân công lại trong cùng phòng là quyền MANAGER/ADMIN đã có trong Actors & Roles; không đồng nhất với hai thao tác trên.

### 2. Danh mục Chức năng Cốt lõi

- **[FR-STF-01]** Đăng nhập tài khoản nhân viên.
- **[FR-STF-02]** Tiếp nhận, phân loại nhóm vấn đề & gán độ ưu tiên cho Ticket.
- **[FR-STF-03]** Chuyển tiếp Ticket sang phòng ban khác; phân công lại trong phòng là quyền MANAGER/ADMIN đã có.
- **[FR-STF-04]** Cập nhật tiến độ & Yêu cầu sinh viên bổ sung thông tin/giấy tờ.
- **[FR-STF-05]** Ghi nhận kết quả và hoàn tất xử lý; đóng sau theo vòng đời đã có.

---

### Giới hạn công sức và mã yêu cầu

Mã FR trong danh mục dưới đây giữ nguyên theo PRD đã chốt. Giờ M02 được đối chiếu theo các dòng Resource!12:17: **187 giờ cơ sở + 10 giờ dự phòng = 197 giờ kế hoạch**. Xem [bảng Resources](Phan_bo_Resources_Antigravity.md); số thứ tự dòng công sức không phải mã FR. Đăng nhập các cổng dùng chung R-ADM-01, không có estimate bổ sung. Những tên công việc nguồn chưa có đặc tả thống nhất không tự trở thành chức năng mới.

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STF-01] Nhân viên đăng nhập hệ thống

#### 1. Mô tả & Phạm vi
Cho phép Nhân viên đăng nhập bằng tài khoản công vụ (Email/Username) do nhà trường cấp. Hệ thống xác thực, trả về Token và cấp quyền truy cập vào Workspace của Phòng ban tương ứng.

**Luồng thao tác nghiệp vụ:**

1. Nhân viên dùng tài khoản đã được ADMIN cấp và gán đúng phòng ban để đăng nhập.
2. Đăng nhập thành công thì vào không gian làm việc và hàng đợi của phòng ban được gán.
3. Sai thông tin, sai vai trò hoặc tài khoản khóa thì hiển thị thông báo tại mục 6; không cấp quyền làm việc tại phòng ban khác.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phòng ban (Staff).
- **Preconditions:** Tài khoản đã được Quản trị viên hệ thống (ADMIN) khởi tạo theo FR-MNG-04, được gán đúng `Department_ID` và ở trạng thái `ACTIVE`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Trường dữ liệu đầu vào:**
  - **Username / Email:** Bắt buộc, tự động `trim()` khoảng trắng hai đầu.
  - **Password:** Bắt buộc, độ dài 6 - 50 ký tự.
- **Scope & Session Context:** Sau khi xác thực thành công, Token phải chứa các thông báo context: `user_id`, `role = STAFF`, `department_id`, `permissions_list`.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Trạng thái Nút Đăng nhập:** Disable khi thông tin trống. Chuyển Loading (kèm spinner) và khóa toàn bộ Form khi request đang được xử lý.
- **Redirect Rule:** Đăng nhập thành công → Tự động điều hướng về `/staff/dashboard` (Hiển thị Queue Ticket của phòng ban).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Nhân viên truy cập `/staff/login`.
2. Kiểm tra phiên làm việc: Nếu Token hợp lệ → Chuyển hướng sang `/staff/dashboard`.
3. Nhập Username/Email và Password, nhấn Đăng nhập (hoặc phím Enter).
4. Client validate form → Gửi request đăng nhập.
5. Server xác thực thông tin, kiểm tra vai trò `STAFF`:
   - Trả về Token xác thực (JWT) + Profile (`staff_id`, `full_name`, `department_id`).
6. Client lưu Token an toàn, chuyển hướng sang `/staff/dashboard`.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Credential không đúng (401 Unauthorized):** Hiển thị Alert error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản không phải STAFF (403 Forbidden):** Hiển thị Alert error: *"Tài khoản của bạn không có quyền truy cập cổng Nhân viên."*
- **Tài khoản bị khóa (403 Forbidden / INACTIVE):** Hiển thị Alert error: *"Tài khoản nhân viên đã bị vô hiệu hóa. Vui lòng liên hệ Quản trị viên."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập đúng tài khoản Staff → Chuyển sang Dashboard hiển thị danh sách Ticket của đúng phòng ban đó trong dưới 1.5s.
- **AC-02:** Tài khoản sinh viên cố gắng đăng nhập tại cổng Staff → Báo lỗi 403 từ chối truy cập.
- **AC-03:** Click Đăng nhập liên tiếp → Chỉ phát sinh 01 request duy nhất.

---

### [FR-STF-02] Tiếp nhận và phân loại yêu cầu (Claim & Triage)

#### 1. Mô tả & Phạm vi
Cung cấp giao diện Queue công việc chung của Phòng ban. Cho phép nhân viên duyệt qua các Ticket mới (`NEW`) hoặc được chuyển đến (`TRANSFERRED`), đánh giá nội dung, điều chỉnh Mức độ ưu tiên (Priority) và Phân loại lại nhóm vấn đề (Category) nếu cần, sau đó Tiếp nhận (Claim) Ticket về danh sách cá nhân xử lý.

**Luồng thao tác nghiệp vụ:**

1. Nhân viên mở hàng đợi phòng ban, chọn yêu cầu chưa tiếp nhận và đọc nội dung, minh chứng.
2. Nhân viên điều chỉnh độ ưu tiên hoặc nhóm vấn đề nếu cần, sử dụng danh mục của phòng ban theo mục 3.
3. Bấm Tiếp nhận xử lý; thành công thì yêu cầu vào danh sách cá nhân, thể hiện người phụ trách và trạng thái đang xử lý.
4. Nếu người khác đã tiếp nhận trước, hiển thị thông báo và cập nhật lại thông tin theo mục 6; không coi thao tác của người gửi sau là thành công.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phòng ban.
- **Preconditions:** Ticket đang ở trạng thái `NEW` hoặc `TRANSFERRED`, thuộc `Department_ID` của nhân viên.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Mức độ ưu tiên (Priority):** Enum bắt buộc: `LOW` (Thấp), `MEDIUM` (Trung bình - Mặc định), `HIGH` (Cao), `URGENT` (Khẩn cấp).
- **Phân loại vấn đề (Category):** Dropdown lấy danh sách Category thuộc phòng ban hiện tại.
- **Trạng thái đích:** Chuyển từ `NEW` / `TRANSFERRED` → `IN_PROGRESS`.
- **Gán phụ trách:** Ghi nhận `assignee_id = current_staff_id`.

#### 4. Cơ chế chống tranh chấp tiếp nhận (Concurrency Control / Optimistic Locking)
- **Bài toán:** Hai nhân viên A và B cùng mở 1 Ticket `NEW` và cùng bấm nút Tiếp nhận xử lý tại 1 thời điểm.
- **Cơ chế xử lý:**
  - Server sử dụng DB Locking / Version check (hoặc `UPDATE tickets SET status='IN_PROGRESS', assignee_id=? WHERE id=? AND status IN ('NEW', 'TRANSFERRED')`).
  - Người gửi request thành công trước sẽ chiếm quyền phụ trách.
  - Người gửi request sau 1 millisecond sẽ nhận phản hồi lỗi `409 Conflict`.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Nhân viên truy cập Tab "Ticket chưa tiếp nhận" (`/staff/queue`).
2. Chọn một Ticket để mở trang Chi tiết (`/staff/tickets/{ticket_id}`).
3. Nhân viên xem mô tả, đính kèm. Chọn/điều chỉnh Priority và Category nếu sinh viên chọn chưa đúng.
4. Nhấn nút **Tiếp nhận xử lý**.
5. Client gửi request claim kèm theo Ticket ID và thông tin Priority/Category đã điều chỉnh.
6. Server kiểm tra điều kiện lock:
   - Nếu Ticket vẫn ở trạng thái `NEW` / `TRANSFERRED` → Cập nhật `status = IN_PROGRESS`, `assignee_id = current_staff_id`, lưu log thao tác. Trả về HTTP 200 OK.
   - Nếu Ticket đã bị người khác claim → Trả về HTTP 409 Conflict.
7. Client nhận 200 OK: Cập nhật UI, hiển thị Toast *"Đã tiếp nhận Ticket thành công"*, chuyển Ticket sang Tab "Ticket của tôi".

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Ticket đã bị gán cho người khác (409 Conflict):** Hiển thị Alert error: *"Ticket này đã được tiếp nhận bởi nhân viên [Tên_Nhân_Viên] trước đó ít giây."* Tự động reload lại trang để khóa nút Tiếp nhận.

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Tiếp nhận Ticket thành công → Trạng thái đổi sang `IN_PROGRESS`, trường người phụ trách hiển thị tên nhân viên hiện tại.
- **AC-02:** Hai nhân viên bấm Tiếp nhận cùng lúc → Đúng 01 người nhận thành công, người còn lại nhận thông báo lỗi rõ ràng và UI tự cập nhật.
- **AC-03:** Thay đổi Priority từ `MEDIUM` sang `URGENT` trong lúc Claim → Dữ liệu lưu đúng Priority mới vào CSDL.
- **AC-04:** Tiếp nhận một Ticket được chuyển đến (`TRANSFERRED`) thuộc phòng ban hiện tại → Ticket vào danh sách cá nhân ở trạng thái `IN_PROGRESS` và ghi đúng người phụ trách, như với Ticket `NEW`.

---

### [FR-STF-03] Chuyển yêu cầu sang đúng phòng ban (Transfer Ticket)

#### 1. Mô tả & Phạm vi
Cho phép nhân viên chuyển tiếp Ticket sang một phòng ban khác nếu yêu cầu gửi nhầm đơn vị hoặc vượt quá thẩm quyền giải quyết. Chức năng này đặc tả chuyển phòng ban; phân công lại nhân viên trong cùng phòng thuộc quyền MANAGER/ADMIN tại Actors & Roles, không thuộc biểu mẫu chuyển phòng ban dưới đây.

**Luồng thao tác nghiệp vụ:**

1. Nhân viên có quyền trên yêu cầu mở thao tác Chuyển phòng ban, chọn đơn vị khác và nhập lý do.
2. Xác nhận chuyển; thành công thì yêu cầu vào hàng đợi chờ tiếp nhận của phòng ban mới và không còn người phụ trách cũ.
3. Nhân viên phòng ban mới tiếp nhận theo FR-STF-02. Lịch sử giữ lại phòng ban cũ, phòng ban mới, người chuyển và lý do.
4. Nếu thiếu lý do hoặc chọn chính phòng ban hiện tại thì không thực hiện chuyển; xử lý theo mục 6.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đang phụ trách Ticket (`assignee_id == current_staff_id`) hoặc Nhân viên thuộc phòng ban đang giữ Ticket.
- **Preconditions:** Ticket có trạng thái `NEW`, `IN_PROGRESS`, `NEED_MORE_INFO` (Chưa ở trạng thái `CLOSED`).

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Phòng ban đích (Target Department):** Dropdown bắt buộc chọn, khác với phòng ban hiện tại.
- **Lý do chuyển tiếp (Transfer Note):** Bắt buộc nhập, chuỗi từ **10 đến 500 ký tự**. Tự động `trim()`. Không chấp nhận chuỗi chỉ chứa khoảng trắng.
- **Chuyển đổi trạng thái & Cập nhật trường:**
  - `status = TRANSFERRED`
  - `department_id = target_department_id`
  - `assignee_id = NULL` (Xóa người phụ trách cũ, đẩy vào Queue chờ của phòng ban mới).

#### 4. Ghi vết lịch sử chuyển tiếp (Audit Log Spec)
- Mỗi lần chuyển phòng ban, hệ thống BẮT BUỘC lưu 01 record vào bảng Audit Log / Ticket History gồm các trường: `ticket_id`, `action = TRANSFER`, `from_department_id`, `to_department_id`, `performed_by_staff_id`, `reason_note`, `created_at`.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Trong màn hình chi tiết Ticket, nhân viên bấm **Chuyển phòng ban**.
2. Modal Chuyển phòng ban hiển thị:
   - Dropdown chọn Target Department.
   - Textarea nhập Reason Note.
3. Nhập dữ liệu và bấm **Xác nhận chuyển**.
4. Client validate dữ liệu (Bắt buộc chọn phòng ban và nhập lý do >= 10 ký tự).
5. Client gửi request transfer.
6. Server cập nhật `department_id`, `status = TRANSFERRED`, `assignee_id = NULL`, ghi nhận Audit Log. Gửi thông báo (Notification) đến Queue của Phòng ban mới.
7. Client đóng Modal, hiển thị Toast thành công và điều hướng nhân viên về danh sách công việc chung.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Bỏ trống lý do / Lý do quá ngắn (400 Bad Request):** Hiển thị lỗi validation ngay dưới Textarea: *"Lý do chuyển tiếp phải từ 10 đến 500 ký tự."*
- **Chọn trùng phòng ban hiện tại (400 Bad Request):** Disable phòng ban hiện tại trong dropdown list.

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Chuyển phòng ban thành công → Ticket biến mất khỏi Tab "Cá nhân xử lý", xuất hiện trong Queue "Chờ tiếp nhận" của Phòng ban mới.
- **AC-02:** Nhập lý do chỉ gồm khoảng trắng → Nút Xác nhận bị khóa hoặc báo lỗi validation.
- **AC-03:** Mở Lịch sử Ticket (Timeline) → Hiển thị đúng nội dung lịch sử: *"Nhân viên A đã chuyển Ticket từ Phòng Đào tạo sang Phòng Tài chính. Lý do: [Nội dung lý do]"*.

---

### [FR-STF-04] Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement)

#### 1. Mô tả & Phạm vi
Cho phép Nhân viên gửi yêu cầu trực tiếp đến Sinh viên để yêu cầu giải thích thêm hoặc upload bổ sung các file/giấy tờ minh chứng còn thiếu trước khi có thể xử lý tiếp.

**Luồng thao tác nghiệp vụ:**

1. Nhân viên đang phụ trách đọc hồ sơ và xác định thông tin/giấy tờ còn thiếu trước khi xử lý tiếp.
2. Nhân viên nhập rõ nội dung cần sinh viên cung cấp rồi gửi yêu cầu bổ sung.
3. Gửi thành công thì yêu cầu chuyển sang `NEED_MORE_INFO`; sinh viên nhận thông báo và đọc nội dung trên cổng Sinh viên.
4. Sinh viên gửi phần bổ sung tại FR-STU-03; nhân viên đọc phần bổ sung trên cùng yêu cầu để tiếp tục xử lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đang phụ trách Ticket (`assignee_id == current_staff_id`).
- **Preconditions:** Ticket ở trạng thái `IN_PROGRESS`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Nội dung yêu cầu bổ sung (Request Note):** Bắt buộc nhập, chuỗi từ **10 đến 1000 ký tự**. Không chứa toàn khoảng trắng. Tự động `trim()`.
- **Danh mục giấy tờ cần bổ sung (Requested Documents Checkbox/Text):** Chọn từ danh sách mẫu hoặc nhập tự do để sinh viên dễ hình dung.
- **Thay đổi trạng thái:** Chuyển từ `IN_PROGRESS` → `NEED_MORE_INFO`.

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Trong màn chi tiết Ticket, nhân viên chọn nút **Yêu cầu bổ sung hồ sơ**.
2. Hiển thị Form nhập nội dung yêu cầu.
3. Nhân viên nhập chi tiết các giấy tờ/thông tin sinh viên cần cung cấp thêm, nhấn **Gửi yêu cầu**.
4. Client thực hiện validate client-side.
5. Client gửi request cập nhật.
6. Server cập nhật `status = NEED_MORE_INFO`, lưu tin nhắn vào Conversation log, phát Notification (In-app / Email) cho Sinh viên.
7. Client hiển thị Toast success: *"Đã gửi yêu cầu bổ sung thông tin tới sinh viên"*, cập nhật Badge trạng thái trên UI thành `NEED_MORE_INFO`.

#### 5. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Ticket bị thay đổi trạng thái bởi thao tác khác (400 Bad Request):** Nếu Ticket không còn ở `IN_PROGRESS` (ví dụ bị Quản lý can thiệp đóng), báo lỗi: *"Ticket không ở trạng thái cho phép yêu cầu bổ sung."*

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Gửi yêu cầu thành công → Trạng thái Ticket đổi sang `NEED_MORE_INFO`, sinh viên thấy nội dung yêu cầu này trên Cổng Sinh viên.
- **AC-02:** Không cho phép gửi tin nhắn rỗng hoặc chỉ chứa khoảng trắng.
- **AC-03:** Gửi nội dung yêu cầu bổ sung hợp lệ → Nội dung sinh viên đọc được tại FR-STU-03 trùng với nội dung nhân viên đã gửi, trên đúng mã Ticket; lịch sử phản hồi cũ vẫn được giữ.

---

### [FR-STF-05] Ghi kết quả và hoàn tất xử lý yêu cầu (Complete & Resolve Ticket)

#### 1. Mô tả & Phạm vi
Cho phép nhân viên nhập kết quả giải quyết chi tiết, đính kèm tệp kết quả nếu có và xác nhận hoàn tất xử lý để sinh viên xem kết quả. "Đã giải quyết" và "Đã đóng" là hai trạng thái khác nhau; giao diện phải thể hiện đúng trạng thái thực tế của Ticket theo quy tắc hiện có.

**Luồng thao tác nghiệp vụ:**

1. Nhân viên đang phụ trách mở thao tác Hoàn tất xử lý, nhập câu trả lời/kết quả và chọn tệp kết quả nếu cần.
2. Nhân viên xác nhận hoàn tất; chỉ thông báo thành công sau khi kết quả đã được ghi nhận.
3. Sinh viên nhận thông báo và xem câu trả lời, tệp kết quả, thời gian hoàn thành tại FR-STU-04.
4. Hiển thị "Đã giải quyết" khi Ticket ở RESOLVED, "Đã đóng" khi ở CLOSED. Việc đóng sau đánh giá theo FR-STU-04/WF-06 được giữ theo tài liệu gốc; không bổ sung thao tác mở lại xử lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đang phụ trách Ticket.
- **Preconditions:** Ticket đang ở trạng thái `IN_PROGRESS`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Nội dung kết quả giải quyết (Resolution Detail):** Bắt buộc nhập, chuỗi từ **20 đến 2000 ký tự**. Tự động `trim()`. Không chấp nhận chuỗi chỉ chứa khoảng trắng.
- **File đính kèm kết quả (Resolution Attachments):** Optional. Tối đa **3 file**, mỗi file ≤ 5MB, định dạng `.pdf`, `.png`, `.jpg`, `.jpeg`.
- **Chuyển đổi trạng thái:**
  - Chuyển `status` từ `IN_PROGRESS` → `RESOLVED`.
  - Cập nhật timestamp `resolved_at = CURRENT_TIMESTAMP`.

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Nhân viên chọn nút **Hoàn tất xử lý**.
2. Hiển thị Form Ghi nhận kết quả giải quyết:
   - Textarea nhập Resolution Detail.
   - Khu vực Upload file đính kèm kết quả.
3. Nhân viên nhập kết quả, đính kèm file (nếu có) và nhấn **Xác nhận hoàn tất**.
4. Client kiểm tra validation dữ liệu.
5. Client gửi request hoàn tất.
6. Server lưu thông tin kết quả giải quyết, file đính kèm kết quả, cập nhật `status = RESOLVED`, lưu `resolved_at`, phát Notification báo kết quả cho Sinh viên.
7. Client cập nhật UI: Hiển thị **Đã giải quyết** nếu trạng thái là `RESOLVED`, **Đã đóng** nếu trạng thái là `CLOSED`; ẩn các button thao tác xử lý.

#### 5. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Để trống kết quả hoặc chỉ nhập khoảng trắng (400 Bad Request):** Hiển thị lỗi ngay tại Client: *"Nội dung kết quả giải quyết không được để trống (tối thiểu 20 ký tự)."*
- **Upload file kết quả lỗi (400 Bad Request / 500):** Ngắt tiến trình hoàn tất xử lý Ticket, giữ nguyên dữ liệu đã nhập trên Form, hiển thị thông báo lỗi upload file.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Nhập kết quả >= 20 ký tự + bấm Xác nhận hoàn tất → Ticket đổi sang trạng thái `RESOLVED`, thời gian hoàn thành ghi nhận chính xác. Sinh viên xem được đầy đủ câu trả lời này.
- **AC-02:** Nhập dưới 20 ký tự hoặc cố tình spam spacebar → Báo lỗi validation, không cho gửi request.
- **AC-03:** Ticket đã đóng → Khóa toàn bộ các nút thao tác (Tiếp nhận, Chuyển phòng, Yêu cầu bổ sung).
- **AC-04:** Sau khi hoàn tất, trạng thái thực tế là `RESOLVED` → Nhãn hiển thị **Đã giải quyết**; là `CLOSED` → Nhãn hiển thị **Đã đóng**. Cả hai trường hợp sinh viên xem được kết quả đã lưu theo FR-STU-04.

---

## III. BẢNG MÃ LỖI CHUẨN DÙNG CHUNG PHÂN HỆ STAFF (SYSTEM ERROR CODES)

| HTTP Status | Error Code | Message hiển thị người dùng | Kịch bản áp dụng |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | *"Dữ liệu nhập vào không hợp lệ. Vui lòng kiểm tra lại."* | Lỗi validation trường dữ liệu đầu vào. |
| **400** | `INVALID_TICKET_STATE` | *"Trạng thái Ticket hiện tại không cho phép thực hiện thao tác này."* | Thao tác sai luồng trạng thái (VD: Yêu cầu bổ sung khi Ticket đã đóng). |
| **400** | `MISSING_TRANSFER_REASON` | *"Vui lòng nhập lý do chuyển phòng ban (tối thiểu 10 ký tự)."* | Không nhập lý do khi chuyển tiếp. |
| **401** | `UNAUTHORIZED` | *"Phiên đăng nhập hết hạn. Vui lòng đăng nhập lại."* | Token Staff hết hạn. |
| **403** | `FORBIDDEN_STAFF_ACCESS` | *"Bạn không có quyền thao tác trên Ticket của phòng ban khác."* | Staff cố truy cập/chỉnh sửa Ticket không thuộc thẩm quyền. |
| **409** | `TICKET_ALREADY_CLAIMED` | *"Ticket này đã được tiếp nhận bởi nhân viên [Tên_Staff] trước đó."* | Xảy ra tranh chấp khi 2 Staff bấm Claim cùng lúc. |
| **500** | `INTERNAL_SERVER_ERROR` | *"Hệ thống gặp sự cố kỹ thuật. Vui lòng thử lại sau."* | Lỗi Server/Database unhandled. |


---

## Tài liệu nguồn: 03-modules/M03-management-dashboard/README.md

# M03 — Chỉ mục PRD và đối chiếu Resources

## Danh mục yêu cầu đã chốt

Nguồn mô tả chi tiết: [prd.md](03-modules/M03-management-dashboard/prd.md). Danh mục dưới đây dùng mã FR của PRD, không lấy số thứ tự công việc Resources làm mã FR.

| Mã FR | Tên yêu cầu |
| --- | --- |
| FR-MNG-01 | Quản lý đăng nhập & Xác thực phân quyền |
| FR-MNG-02 | Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision) |
| FR-MNG-03 | Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export) |
| FR-MNG-04 | Quản trị người dùng & Phân quyền (User Management & RBAC) |
| FR-MNG-05 | Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail) |

## Luồng người dùng

MANAGER/ADMIN đăng nhập (FR-MNG-01) → Xem tình hình và SLA (FR-MNG-02), phân tích/xuất báo cáo (FR-MNG-03). Riêng ADMIN quản trị tài khoản (FR-MNG-04) và xem nhật ký/quyền dữ liệu (FR-MNG-05).

Nhóm vấn đề là danh mục nội dung yêu cầu do ADMIN quản lý và gắn phòng ban mặc định. Tệp sinh viên tối đa 5 tệp, 5MB/tệp; tệp kết quả nhân viên tối đa 3 tệp, 5MB/tệp; định dạng PDF, PNG, JPG, JPEG theo PRD. “Cần bổ sung” dùng mã NEED_MORE_INFO; “Đã giải quyết” dùng RESOLVED, “Đã đóng” dùng CLOSED. Xem lại trang Ticket không phải mở lại xử lý.

## Đối chiếu giờ Resources

Nguồn là sheet **Resource** của workbook, không có sheet riêng mang tên M1/M2/M3. Tổng nhóm 207 giờ cơ sở + 8 giờ dự phòng = **215 giờ kế hoạch**. Một dòng giờ có thể được nhiều FR dùng chung; không cộng lại hay tự chia giờ giữa các FR.

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-ADM-01 | 22 | Quản lý tài khoản, vai trò & RBAC | 5 | 3 | 6 | 3 | 8 | 13 | 9 | 13 | 60 | 4 | 64 | FR-MNG-04; FR-STU-01, FR-STF-01, FR-MNG-01 dùng chung |
| R-ADM-02 | 23 | Quản lý phòng ban & danh mục | 4 | 1 | 3 | 0 | 4 | 5 | 5 | 4 | 26 | 0 | 26 | Danh mục ADMIN quản lý tại Actors & Roles / Terminology; không thêm FR |
| R-ADM-03 | 24 | Kiểm soát quyền truy cập & Audit Trail | 4 | 0 | 4 | 1 | 4 | 9 | 5 | 9 | 36 | 4 | 40 | FR-MNG-04; FR-MNG-05; quyền dữ liệu đã có |
| R-ADM-04 | 25 | Quản lý thời hạn lưu trữ | 3 | 0 | 1 | 0 | 0 | 4 | 4 | 3 | 15 | 0 | 15 | Giữ giờ nguồn; chưa có FR nghiệp vụ riêng về cấu hình/dọn dẹp lưu trữ |
| R-ADM-05 | 26 | Dashboard & thống kê quản trị | 4 | 3 | 1 | 0 | 9 | 3 | 9 | 4 | 33 | 0 | 33 | FR-MNG-02 |
| R-ADM-06 | 27 | Báo cáo, mức độ hài lòng & xuất dữ liệu | 4 | 3 | 1 | 0 | 8 | 5 | 10 | 6 | 37 | 0 | 37 | FR-MNG-03; sử dụng dữ liệu FR-STU-04 |
| Tổng | — | Mỗi dòng tính một lần | 24 | 10 | 16 | 4 | 33 | 39 | 42 | 39 | 207 | 8 | 215 | Không cộng lại khi nhiều FR dùng chung |

Xem [giới hạn và những tên công việc chưa có đặc tả thống nhất](Phan_bo_Resources_Antigravity.md). Không tự bổ sung FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ hoặc UI dọn dẹp chỉ vì tên công việc có trong bảng nguồn.


---

## Tài liệu nguồn: 03-modules/M03-management-dashboard/prd.md

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

Mã FR trong danh mục dưới đây giữ nguyên theo PRD đã chốt. Giờ M03 được đối chiếu theo các dòng Resource!22:27: **207 giờ cơ sở + 8 giờ dự phòng = 215 giờ kế hoạch**. Xem [bảng Resources](Phan_bo_Resources_Antigravity.md); số thứ tự dòng công sức không phải mã FR. Đăng nhập các cổng dùng chung R-ADM-01, không có estimate bổ sung. Những tên công việc nguồn chưa có đặc tả thống nhất không tự trở thành chức năng mới.

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


---

## Tài liệu nguồn: 03-modules/M04-notification-service/README.md

# Dịch Vụ Thông Báo (M04 - Notification Service)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`  
> Phân hệ kỹ thuật này hiện thực hóa trực tiếp chức năng **FR-STU-04: Nhận thông báo trạng thái (19h kế hoạch)** thuộc M1 – Student và tầng hạ tầng thông báo phục vụ các luồng nghiệp vụ liên phân hệ.

## 1. Tổng Quan Phân Hệ Kỹ Thuật

Phân hệ **Dịch vụ Thông báo (Notification Service)** đóng vai trò là kênh truyền tải thông tin trung gian theo thời gian thực trong hệ thống **UniSupport**. Phân hệ chịu trách nhiệm tự động phát sinh, quản lý và hiển thị các thông báo nội bộ hệ thống (In-app Notification) tới đúng đối tượng người dùng (Sinh viên, Nhân viên, Quản lý) mỗi khi có sự kiện quan trọng phát sinh trên Ticket hỗ trợ.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Cập nhật tức thì (Real-time Engagement)**: Giúp sinh viên nắm bắt ngay tiến độ giải quyết yêu cầu, nhận thông báo kết quả hoặc yêu cầu bổ sung hồ sơ từ nhà trường mà không cần liên tục f5/tải lại trang.
- **Giảm thiểu độ trễ vận hành**: Cảnh báo nhân viên chuyên trách ngay khi có Ticket mới gửi đến phòng ban, được phân công công việc hoặc khi có phản hồi mới từ sinh viên.
- **Cảnh báo vi phạm SLA**: Tự động nhắc nhở nhân viên và quản lý khi Ticket sắp hoặc đã quá hạn cam kết xử lý, giúp nâng cao chỉ số hoàn thành công việc đúng hạn.
- **Tập trung hóa trải nghiệm**: Quản lý toàn bộ thông báo tại Trung tâm thông báo (Notification Center) với biểu tượng quả chuông trực quan trên giao diện Web Application.

---

## 3. Danh Mục Yêu Cầu Chức Năng Kỹ Thuật (Technical Feature Specifications)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Mapping Resource Baseline |
| :--- | :--- | :--- | :--- |
| **FR-NTF-01** | Khởi tạo & Phát thông báo tự động | Tự động sinh thông báo In-app khi có các sự kiện trên Ticket (Tạo mới, Đổi trạng thái, Yêu cầu bổ sung, Cập nhật kết quả...). | Nằm trong phạm vi FR-STU-04 (M1) & Backend Services |
| **FR-NTF-02** | Trung tâm thông báo (Notification Center) | Biểu tượng quả chuông (Bell Icon) hiển thị số thông báo chưa đọc, danh sách thông báo và chi tiết nội dung. | Nằm trong phạm vi FR-STU-04 (M1) (FE1: 4h, BA: 3h) |
| **FR-NTF-03** | Đánh dấu Đã đọc / Chưa đọc | Cho phép người dùng đánh dấu từng thông báo hoặc "Đánh dấu tất cả là đã đọc". | Nằm trong phạm vi FR-STU-04 (M1) |
| **FR-NTF-04** | Cảnh báo quá hạn SLA (SLA Overdue Alert) | Tự động phát thông báo cảnh báo tới Nhân viên phụ trách và Trưởng phòng khi Ticket sắp hoặc đã vượt thời hạn SLA. | Nằm trong phạm vi FR-STF-03 (M2: 29h) |

---

## 4. Sơ Đồ Luồng Tự Động Phát Thông Báo (Notification Flow)
```
[Sự kiện nghiệp vụ phát sinh]
(Tạo Ticket / Chuyển trạng thái / Yêu cầu bổ sung / Phân công / Quá hạn SLA)
        │
        ▼
    [Khởi tạo Thông báo - FR-NTF-01]
    - Bắt sự kiện (Event Listener)
    - Xác định danh sách Người nhận (Recipients) theo Vai trò
    - Biên dịch Nội dung theo mẫu (Notification Template)
        │
        ▼
    [Lưu vào Database & Đẩy về Client qua Socket/API]
        │
        ▼
    [Trung tâm thông báo Client - FR-NTF-02 / FR-NTF-03]
    - Cập nhật Badge số lượng chưa đọc trên quả chuông
    - Hiển thị Toast thông báo nổi trên màn hình
    - Đánh dấu Đã đọc khi người dùng nhấn xem
```

---

## 5. Bảng Ma Trận Sự Kiện & Người Nhận Thông Báo (Event-Recipient Matrix)

| Mã Sự Kiện | Sự Kiện Kích Hoạt | Sinh Viên (Student) | Nhân Viên (Staff Agent) | Quản Lý (Manager) |
| :---: | :--- | :---: | :---: | :---: |
| **EVT-01** | Sinh viên gửi thành công Ticket mới |  (Xác nhận) |  (Hòm thư PB) | ❌ |
| **EVT-02** | Ticket được Claim / Assign cho Nhân viên | ❌ |  (Người nhận) | ❌ |
| **EVT-03** | Chuyển trạng thái sang `WAITING_STUDENT` |  (Cần bổ sung) | ❌ | ❌ |
| **EVT-04** | Sinh viên cập nhật hồ sơ bổ sung | ❌ |  (Người thụ lý) | ❌ |
| **EVT-05** | Chuyển Phòng ban chuyên trách | ❌ |  (PB mới) | ❌ |
| **EVT-06** | Ticket hoàn thành (`RESOLVED` / `CLOSED`) |  (Nhận kết quả) | ❌ | ❌ |
| **EVT-07** | Ticket sắp quá hạn hoặc đã quá hạn SLA | ❌ |  (Nhắc nhở) |  (Cảnh báo) |

*Ghi chú:  = Có nhận thông báo | ❌ = Không nhận thông báo*


---

## Tài liệu nguồn: 03-modules/M04-notification-service/prd.md

# Tài Liệu Đặc Tả Yêu Cầu Sản Phẩm - Dịch Vụ Thông Báo (PRD - M04 Notification Service)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`  
> Phân hệ kỹ thuật này hiện thực hóa trực tiếp chức năng **FR-STU-04: Nhận thông báo trạng thái (19h kế hoạch: BA 3h, UI/UX 1h, FE1 4h, BE1 4h, BE2 4h, QA 3h)** và hạ tầng thông báo phục vụ cảnh báo SLA trong **FR-STF-03 (M2)**.

---

### [FR-NTF-01] Khởi tạo & Phát thông báo nội bộ hệ thống tự động

**Mô tả**  
Hệ thống tự động lắng nghe các sự kiện nghiệp vụ phát sinh trên Ticket, sau đó khởi tạo và gửi thông báo nội bộ (In-app Notification) tới đúng đối tượng người dùng liên quan.

**Actor**  
Hệ thống (System Event Engine).

**Preconditions**  
- Xảy ra một sự kiện nghiệp vụ hợp lệ trên Ticket (Tạo mới, Phân công, Chuyển trạng thái, Bổ sung thông tin, Cập nhật kết quả, Cảnh báo SLA).

**Luồng chính**  
1. Sự kiện nghiệp vụ phát sinh trên hệ thống (Ví dụ: Nhân viên A nhấn nút "Hoàn thành" một Ticket).
2. Dịch vụ Thông báo tiếp nhận thông tin sự kiện.
3. Hệ thống xác định danh sách Người nhận thông báo (Recipients) dựa trên Mã ma trận sự kiện (`EVT-01` đến `EVT-07`).
4. Hệ thống điền các biến dữ liệu (Mã Ticket, Tiêu đề, Tên người thao tác...) vào **Mẫu thông báo (Template)** tương ứng.
5. Hệ thống lưu bản ghi thông báo vào cơ sở dữ liệu.
6. Hệ thống đẩy thông báo tới giao diện người dùng (Client Web) của người nhận theo thời gian thực.

**Business Rules**  
- Mọi thông báo In-app đều chứa liên kết trực tiếp (Deep-link) trỏ về đúng màn hình Chi tiết của Ticket liên quan.
- Nội dung thông báo ngắn gọn, rõ ràng, không quá 150 ký tự.
- Không gửi thông báo cho chính người thực hiện thao tác (Ví dụ: Nhân viên tự Claim ticket thì không nhận thông báo "Bạn vừa claim ticket").

**Alternative / Error Flows**  
- **Người nhận đang Offline**: Thông báo vẫn được lưu vào cơ sở dữ liệu và hiển thị ngay khi người nhận đăng nhập lại hệ thống.

**Acceptance Criteria**  
- **AC-01**: Sinh viên tạo Ticket thành công -> Hệ thống gửi thông báo xác nhận cho Sinh viên và thông báo cho Nhân viên thuộc Phòng ban tiếp nhận.
- **AC-02**: Nhân viên yêu cầu bổ sung thông tin -> Sinh viên nhận ngay thông báo kèm đường dẫn tới form bổ sung hồ sơ.
- **AC-03**: Nhấn vào thông báo -> Hệ thống tự động điều hướng chính xác tới trang chi tiết Ticket tương ứng.

**Ví dụ Edge Case**  
Nhân viên A chuyển Ticket `TK-20261004-001` sang Phòng Tài chính - Kế toán.  
-> **Expected Result**: Toàn bộ nhân viên thuộc Phòng Tài chính - Kế toán nhận được thông báo "Có 01 Ticket mới được chuyển tới phòng ban của bạn". Chuyên viên A (người bấm chuyển) không nhận thông báo này.

---

### [FR-NTF-02] Trung tâm thông báo (Notification Center) & Hiển thị quả chuông

**Mô tả**  
Cung cấp giao diện Trung tâm thông báo dạng biểu tượng quả chuông (Bell Icon) trên thanh điều hướng góc trên màn hình Web Application, cho phép người dùng xem danh sách các thông báo mới nhất.

**Actor**  
Tất cả người dùng đã đăng nhập (Sinh viên, Nhân viên, Quản lý).

**Preconditions**  
- Người dùng đã đăng nhập thành công vào hệ thống.

**Luồng chính**  
1. Người dùng quan sát thanh điều hướng (Header) của ứng dụng.
2. Biểu tượng **Quả chuông** hiển thị một thẻ số đỏ (Badge) phản ánh số lượng thông báo **chưa đọc**.
3. Người dùng nhấn vào biểu tượng Quả chuông.
4. Hệ thống mở bảng danh sách Trung tâm thông báo (Notification Dropdown Menu).
5. Bảng hiển thị danh sách 10 thông báo mới nhất, mỗi thông báo gồm:
   - Tiêu đề tóm tắt.
   - Nội dung ngắn.
   - Mốc thời gian tương đối (Ví dụ: "5 phút trước", "2 giờ trước").
   - Trạng thái Đã đọc / Chưa đọc (Phân biệt bằng màu nền).
6. Người dùng nhấn vào một thông báo cụ thể.
7. Hệ thống tự động đánh dấu thông báo đó là "Đã đọc", giảm số lượng trên Badge và điều hướng người dùng tới trang Chi tiết Ticket tương ứng.

**Business Rules**  
- Số hiển thị trên Badge tối đa là `99+` nếu số thông báo chưa đọc vượt quá 99.
- Danh sách thông báo xếp theo thứ tự thời gian giảm dần (Mới nhất nằm ở trên cùng).

**Alternative / Error Flows**  
- **Người dùng không có thông báo nào**: Hiển thị trạng thái trống (Empty state) với biểu tượng quả chuông xám và dòng chữ "Bạn không có thông báo nào".

**Acceptance Criteria**  
- **AC-01**: Khi có thông báo mới -> Badge trên quả chuông tự động tăng số lượng và phát tiếng/hiệu ứng nổi (Toast notification).
- **AC-02**: Nhấn vào danh sách thông báo -> Hiển thị đúng 10 thông báo gần nhất kèm thời gian tương đối.
- **AC-03**: Bấm nút "Xem tất cả" -> Điều hướng tới trang Quản lý toàn bộ thông báo.

**Ví dụ Edge Case**  
Người dùng có 105 thông báo chưa đọc.  
-> **Expected Result**: Badge trên biểu tượng quả chuông hiển thị chuỗi `99+`.

---

### [FR-NTF-03] Đánh dấu Đã đọc / Chưa đọc (Notification Read Status)

**Mô tả**  
Cho phép người dùng quản lý trạng thái của các thông báo trong Trung tâm thông báo, bao gồm đánh dấu lẻ từng thông báo hoặc đánh dấu tất cả là đã đọc.

**Actor**  
Tất cả người dùng đã đăng nhập.

**Preconditions**  
- Người dùng đang mở Trung tâm thông báo.

**Luồng chính**  
1. Người dùng mở Trung tâm thông báo.
2. **Thao tác 1 (Đọc từng thông báo)**: Người dùng nhấn trực tiếp vào dòng thông báo cần xem.
3. **Thao tác 2 (Đánh dấu tất cả đã đọc)**: Người dùng nhấn nút **"Đánh dấu tất cả là đã đọc"** (Mark all as read) ở góc trên bảng thông báo.
4. Hệ thống cập nhật trạng thái các thông báo thành `READ` trong cơ sở dữ liệu.
5. Số lượng Badge trên biểu tượng Quả chuông tự động giảm về `0`.
6. Màu nền của các dòng thông báo chuyển từ màu nổi (Chưa đọc) sang màu nhạt (Đã đọc).

**Business Rules**  
- Việc đánh dấu "Đã đọc" là thao tác một chiều (không hỗ trợ chuyển ngược lại thành Chưa đọc).
- Cập nhật trạng thái "Đã đọc" diễn ra tức thì trên giao diện mà không cần làm mới toàn bộ trang.

**Alternative / Error Flows**  
- **Mất kết nối mạng khi bấm Đánh dấu tất cả đã đọc**: Hệ thống hiển thị thông báo lỗi "Không thể cập nhật trạng thái thông báo. Vui lòng thử lại" và giữ nguyên số Badge.

**Acceptance Criteria**  
- **AC-01**: Bấm nút "Đánh dấu tất cả là đã đọc" -> Badge hiển thị về 0, tất cả thông báo chuyển sang trạng thái đã đọc.
- **AC-02**: Nhấn vào 01 thông báo chưa đọc -> Chỉ riêng thông báo đó chuyển sang đã đọc và Badge giảm đi 1 đơn vị.

---

### [FR-NTF-04] Thông báo cảnh báo trễ hạn / Cảnh báo thời gian SLA (SLA Warning Alert)

**Mô tả**  
Hệ thống tự động quét và phát thông báo cảnh báo tới Nhân viên phụ trách và Trưởng phòng ban khi một Ticket sắp chạm mốc thời gian cam kết xử lý (SLA Warning) hoặc đã vượt quá thời hạn xử lý (SLA Overdue).

**Actor**  
Hệ thống tự động (SLA Monitor Daemon).

**Preconditions**  
- Ticket đang ở trạng thái `IN_PROGRESS` hoặc `NEW`.
- Mốc thời gian cam kết xử lý (`sla_due_at`) đã được thiết lập.

**Luồng chính**  
1. Hệ thống định kỳ quét các Ticket chưa hoàn thành.
2. **Mức 1 (Cảnh báo sắp quá hạn)**: Khi thời gian còn lại đến hạn `sla_due_at` nhỏ hơn hoặc bằng **2 giờ làm việc**:
   - Hệ thống khởi tạo thông báo "CẢNH BÁO SLA: Ticket [Mã Ticket] sắp đến hạn xử lý".
   - Gửi thông báo tới Nhân viên phụ trách.
3. **Mức 2 (Cảnh báo đã quá hạn)**: Khi thời điểm hiện tại vượt quá mốc `sla_due_at`:
   - Hệ thống khởi tạo thông báo "SỰ CỐ SLA: Ticket [Mã Ticket] ĐÃ QUÁ HẠN XỬ LÝ".
   - Gửi thông báo cảnh báo tới Nhân viên phụ trách VÀ Trưởng phòng ban.
4. Hệ thống hiển thị biểu tượng cảnh báo màu đỏ đối với Ticket quá hạn trong Hòm thư công việc.

**Business Rules**  
- Cảnh báo Mức 1 (Sắp quá hạn) chỉ gửi **01 lần duy nhất** cho mỗi Ticket.
- Cảnh báo Mức 2 (Đã quá hạn) gửi cho cả Nhân viên thụ lý và Trưởng phòng ban để hỗ trợ điều phối kịp thời.
- Thời gian tính toán SLA tự động loại trừ khoảng thời gian Ticket nằm ở trạng thái `WAITING_STUDENT` theo quy tắc `BR-SUP-01`.

**Alternative / Error Flows**  
- **Ticket được chuyển sang `RESOLVED` trước khi hết hạn**: Hệ thống hủy các lịch trình cảnh báo trễ hạn còn lại của Ticket đó.

**Acceptance Criteria**  
- **AC-01**: Ticket còn 1.5 giờ là hết hạn SLA -> Nhân viên phụ trách nhận được thông báo cảnh báo sắp quá hạn.
- **AC-02**: Ticket vượt quá hạn SLA 1 phút -> Cả Nhân viên thụ lý và Trưởng phòng ban nhận được thông báo cảnh báo quá hạn.
- **AC-03**: Ticket đang ở trạng thái `WAITING_STUDENT` -> Không phát thông báo cảnh báo SLA.


---

## Tài liệu nguồn: 03-modules/M05-rbac-security/README.md

# Phân Hệ Phân Quyền & Bảo Mật (M05 - RBAC & Security)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`  
> Phân hệ kỹ thuật này hiện thực hóa các chức năng bảo mật cốt lõi thuộc M3 – Admin:
> - **FR-ADM-01: Quản lý tài khoản, vai trò & RBAC (64h kế hoạch)**
> - **FR-ADM-03: Kiểm soát quyền truy cập & Audit Trail (40h kế hoạch)**
> - **FR-ADM-04: Quản lý thời hạn lưu trữ (15h kế hoạch)**

## 1. Tổng Quan Phân Hệ Kỹ Thuật

Phân hệ **Phân Quyền & Bảo Mật (RBAC & Security)** là nền tảng hạ tầng bảo mật cốt lõi duy trì tính toàn vẹn, an toàn dữ liệu và kiểm soát truy cập cho toàn bộ hệ thống **UniSupport** tại **Aurora University**.

Phân hệ chịu trách nhiệm xác thực danh tính người dùng (Authentication), phân quyền thao tác theo vai trò (Role-Based Access Control - RBAC) đối với 4 vai trò chính (Sinh viên, Nhân viên, Quản lý, Quản trị viên), bảo vệ an toàn cho các tệp đính kèm (PDF, Ảnh) và lưu vết nhật ký hoạt động (Audit Log) cho các giao dịch nghiệp vụ quan trọng.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Bảo mật danh tính & Xác thực an toàn**: Đảm bảo 100% người dùng truy cập hệ thống đều được định danh bằng tài khoản cá nhân với mật khẩu được mã hóa chuẩn an toàn (Argon2/BCrypt).
- **Phân định ranh giới dữ liệu (Data Isolation)**: Người dùng thuộc vai trò nào chỉ được thấy và thao tác đúng phạm vi dữ liệu được cấp phép (Sinh viên chỉ thấy Ticket của mình; Nhân viên chỉ xử lý Ticket thuộc Phòng ban của mình).
- **Bảo vệ tài liệu nhạy cảm**: Chặn đứng nguy cơ rò rỉ file đính kèm (bảng điểm, giấy xác nhận, đơn từ...) bằng cơ chế đường dẫn bảo mật qua Secured API Proxy (không lộ đường dẫn lưu trữ tĩnh).
- **Tính minh bạch & Khả năng tra soát (Auditability)**: Ghi lại đầy đủ lịch sử các thao tác quan trọng để phục vụ công tác kiểm tra, đối soát khi có thắc mắc hoặc khiếu nại.

---

## 3. Danh Mục Yêu Cầu Chức Năng Kỹ Thuật (Technical Feature Specifications)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Mapping Resource Baseline (M3) |
| :--- | :--- | :--- | :--- |
| **FR-SEC-01** | Xác thực & Quản lý phiên làm việc | Đăng nhập mã hóa, cấp Token xác thực (JWT/Session), tự động hết hạn phiên và cơ chế đăng xuất an toàn. | FR-ADM-01 (M3: 64h) |
| **FR-SEC-02** | Phân quyền theo vai trò (RBAC) | Kiểm soát quyền truy cập API và giao diện dựa trên 4 vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`). | FR-ADM-01 (M3: 64h) |
| **FR-SEC-03** | Bảo mật tệp đính kèm & Lưu trữ | Kiểm soát quyền tải/xem file đính kèm qua Secured API Proxy, quản lý thời hạn lưu trữ dữ liệu. | FR-ADM-03 & FR-ADM-04 (M3: 55h) |
| **FR-SEC-04** | Ghi nhận Nhật ký tra soát (Audit Log) | Tự động ghi vết các sự kiện hệ thống quan trọng (Đổi trạng thái, Phân công, Chuyển phòng ban, Khóa tài khoản) dưới dạng immutable log. | FR-ADM-03 (M3: 40h) |

---

## 4. Sơ Đồ Kiến Trúc Phân Quyền & Bảo Mật (Security Architecture)
```
[Client Web Request]
        │
        ▼
┌─────────────────────────┐
│   API Gateway / Router  │
└────────────┬────────────┘
             │
             ▼
┌────────────────────────────────────┐
│ 1. AUTHENTICATION MIDDLEWARE       │
│    - Kiểm tra JWT Token / Session  │
│    - Xác minh danh tính người dùng │
└──────────────────┬─────────────────┘
                   │ (Hợp lệ)
                   ▼
┌────────────────────────────────────┐
│ 2. RBAC AUTHORIZATION MIDDLEWARE   │
│    - Kiểm tra Role (STUDENT/STAFF/ │
│      MANAGER/ADMIN)                │
│    - Kiểm tra Resource Ownership & │
│      Department Scope              │
└──────────────────┬─────────────────┘
                   │ (Hợp lệ)
          ┌────────┴────────┐
          ▼                 ▼
┌──────────────────────┐  ┌──────────────────────┐
│   Business Logic     │  │ Secured File Proxy   │
│   (Process Ticket)   │  │ (Verify Attachment  │
└──────────┬───────────┘  │  Ownership)         │
           │              └──────────┬───────────┘
           ▼                         ▼
┌──────────────────────┐  ┌──────────────────────┐
│ 3. AUDIT LOG MODULE  │  │ Return Encrypted     │
│    - Append Activity │  │ File Stream          │
└──────────────────────┘  └──────────────────────┘
```

---

## 5. Ma Trận Phân Quyền Dữ Liệu Chi Tiết (Data Access Control Matrix)

| Phạm Vi Dữ Liệu (Resource Scope) | Sinh Viên (`STUDENT`) | Nhân Viên (`STAFF`) | Quản Lý (`MANAGER`) | Quản Trị Viên (`ADMIN`) |
| :--- | :---: | :---: | :---: | :---: |
| **Ticket do mình tạo** | Full (Xem, Tạo, Bổ sung, Đánh giá) | N/A | N/A | N/A |
| **Ticket thuộc Phòng ban mình phụ trách** | ❌ Không có quyền | Full (Xem, Claim, Transfer, Resolve) | Xem & Phân công trong Phòng ban | Xem & Quản trị |
| **Ticket thuộc Phòng ban khác** | ❌ Không có quyền | ❌ Không có quyền | ❌ Không có quyền | Xem tra soát |
| **Tệp đính kèm của Ticket** |  (Chỉ file thuộc Ticket của mình) |  (Chỉ file thuộc Ticket của PB mình) |  (Chỉ file thuộc Ticket của PB mình) |  (Tải tra soát) |
| **Báo cáo & Thống kê KPI** | ❌ Không có quyền | ❌ Không có quyền |  (Dữ liệu PB phụ trách) |  (Dữ liệu Toàn trường) |
| **Quản lý Tài khoản & Audit Log** | ❌ Không có quyền | ❌ Không có quyền | ❌ Không có quyền |  (Toàn bộ hệ thống) |

*Ghi chú:  = Có quyền truy cập | ❌ = Cấm truy cập*


---

## Tài liệu nguồn: 03-modules/M05-rbac-security/prd.md

# Tài Liệu Đặc Tả Yêu Cầu Sản Phẩm - Phân Quyền & Bảo Mật (PRD - M05 RBAC & Security)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`  
> Phân hệ kỹ thuật này hiện thực hóa các chức năng bảo mật cốt lõi thuộc M3 – Admin:
> - **FR-ADM-01: Quản lý tài khoản, vai trò & RBAC (64h kế hoạch: BA 5h, UI/UX 3h, TL 6h, FE1 3h, FE2 8h, BE1 13h, BE2 9h, QA 13h)**
> - **FR-ADM-03: Kiểm soát quyền truy cập & Audit Trail (40h kế hoạch: BA 4h, TL 4h, FE1 1h, FE2 4h, BE1 9h, BE2 5h, QA 9h)**
> - **FR-ADM-04: Quản lý thời hạn lưu trữ (15h kế hoạch: BA 3h, TL 1h, BE1 4h, BE2 4h, QA 3h)**

---

### [FR-SEC-01] Xác thực tài khoản & Quản lý phiên làm việc (Authentication & Session Management)

**Mô tả**  
Hệ thống xử lý quá trình đăng nhập, mã hóa thông tin xác thực, khởi tạo Token phiên làm việc an toàn và quản lý đăng xuất đối với tất cả các nhóm người dùng.

**Actor**  
Tất cả người dùng hệ thống (Sinh viên, Nhân viên, Quản lý, Admin).

**Preconditions**  
- Người dùng truy cập trang Đăng nhập hệ thống UniSupport.

**Luồng chính**  
1. Người dùng nhập tên đăng nhập (Mã SV/Mã NV/Email) và mật khẩu.
2. Hệ thống mã hóa mật khẩu đầu vào (chuẩn Argon2 hoặc BCrypt) và so sánh với giá trị lưu trong cơ sở dữ liệu.
3. Nếu thông tin chính xác, hệ thống kiểm tra trạng thái tài khoản (`status = ACTIVE`).
4. Hệ thống khởi tạo chuỗi xác thực Token (JWT/Session Token) chứa thông tin: `user_id`, `role`, `department_id`, `exp_time`.
5. Hệ thống trả Token về Client và lưu trữ an toàn (HttpOnly Secure Cookie hoặc Secure Storage).
6. Khi người dùng bấm **Đăng xuất**, hệ thống thu hồi (Revoke/Invalidate) Token hiện tại và xóa phiên làm việc ở Client.

**Business Rules**  
- Mật khẩu lưu trong cơ sở dữ liệu **bắt buộc** phải mã hóa một chiều (Salted Hash), tuyệt đối không lưu dạng plain-text.
- Thời gian hết hạn của Token phiên làm việc tối đa là **24 giờ**.
- Nếu tài khoản chuyển trạng thái `INACTIVE` (bị khóa), toàn bộ các Token đang hoạt động của tài khoản đó phải lập tức bị vô hiệu hóa.

**Alternative / Error Flows**  
- **Mật khẩu không chính xác**: Hệ thống hiển thị thông báo lỗi chung "Tên đăng nhập hoặc mật khẩu không đúng".
- **Tài khoản đang bị khóa (`INACTIVE`)**: Hệ thống hiển thị lỗi "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ Admin".
- **Token hết hạn (Expired Token)**: Khi người dùng thao tác, hệ thống trả về mã lỗi HTTP `401 Unauthorized` và điều hướng người dùng về màn hình Đăng nhập.

**Acceptance Criteria**  
- **AC-01**: Đăng nhập với tài khoản hợp lệ -> Khởi tạo Token an toàn, cho phép truy cập các API được phân quyền.
- **AC-02**: Đăng xuất thành công -> Token cũ bị vô hiệu hóa, nhấn nút Back trên trình duyệt không thể xem lại trang nội bộ.
- **AC-03**: Nhập sai mật khẩu -> Dừng đăng nhập, không cấp Token.

**Ví dụ Edge Case**  
Người dùng đổi mật khẩu ở thiết bị A.  
-> **Expected Result**: Phiên làm việc trên thiết bị B tự động bị vô hiệu hóa ở thao tác tiếp theo do Token cũ không còn hợp lệ.

---

### [FR-SEC-02] Phân quyền truy cập theo vai trò (Role-Based Access Control - RBAC)

**Mô tả**  
Hệ thống tự động kiểm tra Vai trò (`Role`) và Phạm vi Phòng ban (`Department Scope`) của người dùng trên từng API Request để cho phép hoặc chặn quyền truy cập tài nguyên.

**Actor**  
Hệ thống (RBAC Middleware).

**Preconditions**  
- Người dùng đã đăng nhập thành công và gửi request đính kèm Token xác thực.

**Luồng chính**  
1. Client gửi request tới API Endpoint (Ví dụ: `GET /api/v1/tickets/{id}`).
2. Middleware kiểm tra và giải mã Token xác thực.
3. Middleware kiểm tra **Vai trò (Role)** của người dùng với yêu cầu của Endpoint:
   - Nếu Endpoint yêu cầu quyền `MANAGER` mà người dùng là `STUDENT` -> Từ chối.
4. Middleware kiểm tra **Phạm vi dữ liệu (Data Scope / Ownership)**:
   - Nếu là `STUDENT`: Ticket `{id}` bắt buộc phải có `created_by_student_id` = ID người dùng.
   - Nếu là `STAFF`: Ticket `{id}` bắt buộc phải có `department_id` = ID Phòng ban của Nhân viên.
5. Nếu tất cả điều kiện hợp lệ, Request được chuyển tiếp cho Business Logic xử lý.
6. Nếu vi phạm, hệ thống chặn lại và trả về mã lỗi HTTP `403 Forbidden`.

**Business Rules**  
- Kiểm tra phân quyền phải diễn ra tại lớp Backend (Server-side Enforcement), không tin tưởng hoàn toàn vào việc ẩn/hiện nút bấm trên giao diện Frontend.
- Nhân viên thuộc Phòng A tuyệt đối không thể xem, chuyển trạng thái hoặc can thiệp Ticket thuộc Phòng B trừ khi Ticket đó được chuyển phòng ban sang Phòng A.

**Alternative / Error Flows**  
- **Truy cập tài nguyên không thuộc quyền quản lý**: Hệ thống trả về lỗi `403 Forbidden` kèm thông báo "Bạn không có quyền thực hiện thao tác này".

**Acceptance Criteria**  
- **AC-01**: Sinh viên A gửi request xem Ticket của Sinh viên B -> Hệ thống trả về lỗi `403 Forbidden`.
- **AC-02**: Nhân viên Phòng Đào tạo thực hiện Claim Ticket của Phòng CTHSSV -> Hệ thống từ chối thao tác và báo lỗi không đúng phòng ban.
- **AC-03**: Admin gửi request -> Hệ thống cho phép truy cập theo đúng thẩm quyền quản trị.

**Ví dụ Edge Case**  
Sinh viên cố tình thay đổi tham số ID trên URL từ `/tickets/101` thành `/tickets/102` (mã ticket của người khác).  
-> **Expected Result**: Backend phát hiện người tạo Ticket 102 khác với ID người dùng trong Token, lập tức trả về `403 Forbidden`.

---

### [FR-SEC-03] Bảo mật & Kiểm soát truy cập tệp đính kèm (Secure File Access Control)

**Mô tả**  
Đảm bảo các file đính kèm (PDF, Ảnh minh chứng, Giấy xác nhận) lưu trên hệ thống được bảo vệ an toàn, không thể truy cập qua đường dẫn tĩnh công khai (Public URL).

**Actor**  
Tất cả người dùng có nhu cầu Tải/Xem file đính kèm.

**Preconditions**  
- File đính kèm đã được tải lên và lưu trữ trong thư mục bảo mật của hệ thống.
- Người dùng đã đăng nhập.

**Luồng chính**  
1. Người dùng nhấn vào liên kết Xem/Tải file đính kèm trên giao diện Ticket.
2. Client gửi request tới Secured File API Proxy: `GET /api/v1/attachments/{file_id}/download`.
3. Backend tiếp nhận request và giải mã Token người dùng.
4. Backend truy vấn cơ sở dữ liệu để tìm Ticket chứa `file_id` tương ứng.
5. Backend kiểm tra quyền truy cập của người dùng đối với Ticket đó theo quy tắc `BR-FILE-01`:
   - Người dùng là Sinh viên tạo Ticket.
   - HOẶC Người dùng là Nhân viên/Quản lý thuộc Phòng ban thụ lý Ticket.
   - HOẶC Người dùng là Quản trị viên (Admin).
6. Nếu hợp lệ, Backend đọc luồng dữ liệu file (Stream) từ thư mục lưu trữ bảo mật và trả về cho Client.
7. Nếu không hợp lệ, Backend chặn truy cập và từ chối tải file.

**Business Rules**  
- Đường dẫn lưu file trên máy chủ (`file_path`) không được hiển thị trực tiếp ra phía Client.
- Nghiêm cấm cấu hình thư mục chứa file ở chế độ Static Public Web Access (Ví dụ: `http://domain.com/uploads/file.pdf` bị cấm hoàn toàn).
- Mọi yêu cầu tải file bắt buộc phải đi qua API Proxy có xác thực Token.

**Alternative / Error Flows**  
- **Thử truy cập trực tiếp URL file tĩnh (nếu có)**: Hệ thống trả về lỗi `404 Not Found` hoặc `403 Forbidden`.
- **Người dùng không liên quan bấm tải file**: Hệ thống chặn và báo lỗi "Bạn không có quyền truy cập tệp đính kèm này".

**Acceptance Criteria**  
- **AC-01**: Sinh viên chủ sở hữu nhấn xem file đính kèm -> File tải/hiển thị thành công.
- **AC-02**: Sinh viên khác copy link download file đính kèm đó và paste sang trình duyệt -> Hệ thống chặn và trả lỗi `403 Forbidden`.
- **AC-03**: Nhân viên thuộc phòng ban phụ trách nhấn tải file -> File tải thành công.

**Ví dụ Edge Case**  
Người dùng chưa đăng nhập paste trực tiếp đường dẫn API download file `https://unisupport.aurora.edu.vn/api/v1/attachments/88/download` vào trình duyệt.  
-> **Expected Result**: Hệ thống từ chối do thiếu Token xác thực, trả lỗi `401 Unauthorized` và không tải bất kỳ dữ liệu file nào.

---

### [FR-SEC-04] Ghi nhận nhật ký tra soát hệ thống cơ bản (Basic Audit Logging)

**Mô tả**  
Hệ thống tự động ghi lại toàn bộ nhật ký lịch sử cho các sự kiện biến động dữ liệu hoặc thay đổi trạng thái quan trọng nhằm phục vụ tra soát độc lập.

**Actor**  
Hệ thống (Audit Log Engine).

**Preconditions**  
- Xảy ra một hành động quan trọng trên hệ thống (Ví dụ: Thay đổi trạng thái Ticket, Chuyển phòng ban, Phân công nhân viên, Tạo/Khóa tài khoản).

**Luồng chính**  
1. Một hành động nghiệp vụ được thực hiện thành công trong hệ thống.
2. Module Audit Log được kích hoạt tự động.
3. Module trích xuất thông tin bối cảnh giao dịch:
   - `user_id`: ID người thực hiện.
   - `action`: Mã hành động (Ví dụ: `TICKET_STATUS_UPDATED`, `DEPARTMENT_TRANSFERRED`).
   - `resource_type`: Loại tài nguyên (`TICKET`, `USER`, `ATTACHMENT`).
   - `resource_id`: ID tài nguyên bị tác động.
   - `old_value` / `new_value`: Dữ liệu trước và sau khi thay đổi (dạng JSON).
   - `ip_address`: Địa chỉ IP của Client.
   - `timestamp`: Thời gian thực hiện (UTC).
4. Module ghi bản ghi log vào cơ sở dữ liệu nhật ký (`audit_logs` table).

**Business Rules**  
- Bảng nhật ký `audit_logs` được thiết lập theo quy tắc `BR-AUD-01`: Chỉ cho phép chèn dữ liệu mới (Append-only).
- Tuyệt đối không cung cấp API hoặc chức năng trên giao diện cho phép SỬA (UPDATE) hoặc XÓA (DELETE) bản ghi nhật ký.
- Thời gian lưu vết bắt buộc theo định dạng chuẩn UTC/ISO-8601.

**Alternative / Error Flows**  
- **Ghi log thất bại**: Nếu quá trình ghi log gặp sự cố, giao dịch chính vẫn đảm bảo tính nhất quán (Rollback nếu quy định bắt buộc) hoặc cảnh báo lỗi hệ thống log.

**Acceptance Criteria**  
- **AC-01**: Nhân viên thực hiện chuyển trạng thái Ticket từ `IN_PROGRESS` sang `RESOLVED` -> Một dòng log được tạo tự động lưu rõ ID nhân viên, giá trị cũ `IN_PROGRESS`, giá trị mới `RESOLVED` và thời điểm thực hiện.
- **AC-02**: Nhật ký chỉ ở dạng truy vấn xem (Read-only), không có bất kỳ lệnh sửa/xóa nào trên hệ thống.

**Ví dụ Edge Case**  
Tài khoản Admin thử gửi lệnh xóa dữ liệu bảng `audit_logs` qua giao diện.  
-> **Expected Result**: Hệ thống không cung cấp chức năng xóa, mọi truy cập trực tiếp bị chặn ở mức phân quyền database.


---

## Tài liệu nguồn: 03-modules/README.md

# Chỉ mục yêu cầu sản phẩm và tài liệu hỗ trợ

| Thư mục | Vai trò của tài liệu | Mã yêu cầu |
| --- | --- | --- |
| [M01](03-modules/M01-student-portal/prd.md) | PRD cổng Student | FR-STU-01..04 |
| [M02](03-modules/M02-staff-operations/prd.md) | PRD cổng Staff | FR-STF-01..05 |
| [M03](03-modules/M03-management-dashboard/prd.md) | PRD cổng Management/Admin | FR-MNG-01..05 |
| [M04](03-modules/M04-notification-service/prd.md) | Tài liệu hỗ trợ kỹ thuật thông báo, giữ nguyên nội dung | Không có FR sản phẩm mới; đối chiếu R-STU-04 và luồng hiện có |
| [M05](03-modules/M05-rbac-security/prd.md) | Tài liệu hỗ trợ kỹ thuật quyền/bảo mật, giữ nguyên nội dung | Không có FR sản phẩm mới; đối chiếu R-ADM-01/03/04 |

14 FR sản phẩm được nghiệm thu theo 3 PRD và RTM. M04/M05 hiện dùng các mã nội bộ FR-NTF/FR-SEC và một số ánh xạ cũ; các mã đó không thay thế hoặc cộng thêm FR nghiệp vụ. Không cộng 19/64/40/15 giờ một lần nữa cho dịch vụ kỹ thuật: đây là những dòng dùng chung đã nằm trong 640 giờ.

Xem [bảng giờ nguồn](Phan_bo_Resources_Antigravity.md) và [các sai lệch kỹ thuật chưa chỉnh](08-project/prd-review-notes.md). Bản sửa không phê duyệt thêm trung tâm quản lý toàn bộ thông báo, đánh dấu tất cả đã đọc, tiếng báo, ngưỡng SLA mới, timeout phiên mới hoặc cơ chế dọn dẹp lưu trữ chỉ vì chúng có trong tài liệu hỗ trợ hiện tại.


---

## Tài liệu nguồn: 04-workflows/README.md

# 04-workflows: Quy trình Nghiệp vụ UniSupport

Thư mục này chứa toàn bộ tài liệu mô tả chi tiết các **Quy trình Nghiệp vụ (Workflows)** của hệ thống UniSupport tại Aurora University. Các quy trình được chuẩn hóa nhằm đảm bảo tính minh bạch, đúng phân quyền và theo sát vòng đời của một Ticket hỗ trợ.

---

## Danh sách Quy trình Nghiệp vụ

| Mã Workflow | Tên Quy trình | Vai trò chính | Mô tả ngắn gọn |
| :--- | :--- | :--- | :--- |
| **[WF-01](04-workflows/WF-01-submit-support-request.md)** | Gửi yêu cầu hỗ trợ | Sinh viên | Sinh viên tạo Ticket, chọn nhóm vấn đề, đính kèm file (ảnh/PDF) và nhận mã Ticket. |
| **[WF-02](04-workflows/WF-02-claim-and-triage.md)** | Tiếp nhận & Phân loại | Nhân viên | Nhân viên tiếp nhận (claim) Ticket, cập nhật độ ưu tiên và kiểm tra nhóm vấn đề. |
| **[WF-03](04-workflows/WF-03-request-supplement.md)** | Yêu cầu bổ sung hồ sơ | Nhân viên & Sinh viên | Nhân viên yêu cầu bổ sung giấy tờ; sinh viên phản hồi và đính kèm file bổ sung. |
| **[WF-04](04-workflows/WF-04-transfer-department.md)** | Chuyển tiếp phòng ban | Nhân viên | Chuyển Ticket sang phòng ban khác kèm lý do chuyển minh bạch. |
| **[WF-05](04-workflows/WF-05-complete-and-resolve.md)** | Cập nhật kết quả & Hoàn tất xử lý | Nhân viên | Ghi kết quả, tệp kết quả nếu có và chuyển RESOLVED; đóng theo WF-06/vòng đời hiện có. |
| **[WF-06](04-workflows/WF-06-close-and-rate.md)** | Nhận kết quả & Đánh giá | Sinh viên | Sinh viên xem kết quả xử lý và đánh giá độ hài lòng (1–5 sao). |

---

## Quy chuẩn Cấu trúc tài liệu Workflow

Mỗi file quy trình nghiệp vụ trong thư mục này tuân thủ thống nhất các phần nội dung sau:
1. **Mô tả (Description):** Tóm tắt mục đích nghiệp vụ.
2. **Actor:** Các vai trò tham gia thực hiện.
3. **Preconditions:** Điều kiện tiên quyết để kích hoạt quy trình.
4. **Luồng chính (Main Flow):** Các bước thực hiện theo thứ tự chuẩn.
5. **Business Rules:** Quy tắc nghiệp vụ bắt buộc tuân thủ.
6. **Alternative / Error Flows:** Khả năng xử lý các trường hợp ngoại lệ/lỗi.
7. **Acceptance Criteria (AC):** Tiêu chí nghiệm thu rõ ràng.
8. **Ví dụ Edge Case:** Minh họa tình huống biên cụ thể và kết quả mong đợi.


---

## Tài liệu nguồn: 04-workflows/WF-01-submit-support-request.md

# [WF-01] Sinh viên gửi yêu cầu hỗ trợ (Submit Support Request)

### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ

**Mô tả**
Hệ thống cho phép sinh viên tạo một Ticket hỗ trợ bằng cách chọn nhóm vấn đề, nhập nội dung mô tả tình huống, đính kèm tệp tài liệu (ảnh hoặc PDF nếu cần) và gửi yêu cầu đến bộ phận phụ trách của Aurora University.

**Actor**
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**
- Sinh viên đã đăng nhập thành công vào hệ thống UniSupport.
- Sinh viên có quyền tạo Ticket hỗ trợ.

**Luồng chính**
1. Sinh viên mở chức năng **Tạo Ticket**.
2. Hệ thống hiển thị form tạo Ticket.
3. Sinh viên chọn **Nhóm vấn đề** (Category) từ danh mục ADMIN quản lý; mỗi nhóm gắn phòng ban mặc định.
4. Sinh viên nhập các thông tin bắt buộc, bao gồm tiêu đề và **Mô tả vấn đề**.
5. Sinh viên đính kèm tệp tài liệu (ảnh JPG/JPEG/PNG hoặc tệp PDF) nếu cần.
6. Sinh viên chọn **Gửi yêu cầu**.
7. Hệ thống kiểm tra tính hợp lệ của dữ liệu đầu vào và tệp đính kèm.
8. Nếu dữ liệu hợp lệ, hệ thống khởi tạo Ticket mới, tự động sinh mã Ticket duy nhất và gán trạng thái ban đầu là `NEW` (Mới tạo).
9. Hệ thống hiển thị thông báo tạo Ticket thành công, cung cấp mã Ticket cho sinh viên và gửi thông báo nội bộ hệ thống.

**Business Rules**
- Nhóm vấn đề, tiêu đề (10–150 ký tự) và mô tả (20–2000 ký tự) là các thông tin bắt buộc theo FR-STU-02.
- Nội dung mô tả chỉ chứa khoảng trắng được xem là không hợp lệ.
- Tệp đính kèm hỗ trợ PDF, PNG, JPG, JPEG; tối đa 5 tệp, 5MB/tệp theo FR-STU-02.
- Một thao tác gửi của sinh viên chỉ được tạo tối đa **một Ticket**, kể cả khi yêu cầu bị gửi nhiều lần do double-click, retry hoặc vấn đề mạng.
- Ticket sau khi được tạo phải được liên kết chính xác với tài khoản sinh viên đã gửi yêu cầu.

**Alternative / Error Flows**
- **Thiếu thông tin bắt buộc:** Hệ thống không tạo Ticket, hiển thị thông báo lỗi validation chi tiết tại từng trường thông tin.
- **Tệp đính kèm không hợp lệ (sai định dạng hoặc vượt dung lượng):** Hệ thống chặn gửi, báo lỗi tệp không hợp lệ và yêu cầu chọn lại.
- **Lỗi hệ thống trong quá trình tạo:** Hệ thống thông báo lỗi và không tạo Ticket ở trạng thái dữ liệu không hoàn chỉnh (rollback).
- **Trùng lặp request do kết nối:** Nếu cùng một request được gửi lại do retry/network retry, hệ thống không tạo thêm Ticket trùng lặp.

**Acceptance Criteria**
- **AC-01:** Sinh viên chọn nhóm vấn đề, nhập đầy đủ thông tin hợp lệ và chọn **Gửi yêu cầu** -> Hệ thống tạo đúng một Ticket, sinh mã Ticket duy nhất và hiển thị thông báo thành công.
- **AC-02:** Sinh viên để trống trường mô tả hoặc nhóm vấn đề -> Hệ thống không tạo Ticket và hiển thị lỗi validation.
- **AC-03:** Sinh viên nhập nội dung chỉ gồm khoảng trắng -> Hệ thống không tạo Ticket.
- **AC-04:** Sinh viên tải lên tệp đính kèm đúng chuẩn (.pdf, .jpg, .jpeg, .png) -> Hệ thống lưu trữ tệp và gắn liên kết vào Ticket.
- **AC-05:** Sinh viên tải lên tệp sai định dạng (ví dụ .docx, .zip) -> Hệ thống từ chối tệp và báo lỗi.
- **AC-06:** Sinh viên nhấn nút **Gửi yêu cầu** nhiều lần liên tiếp -> Hệ thống chỉ tạo một Ticket duy nhất.
- **AC-07:** Ticket được tạo phải lưu đúng thông tin sinh viên gửi yêu cầu và gửi thông báo xác nhận.

**Ví dụ Edge Case**
Sinh viên nhấn nút **Gửi yêu cầu** 5 lần liên tiếp trong thời gian ngắn do mạng giật lag.

**Expected Result:** Hệ thống chỉ ghi nhận **một Ticket duy nhất** cho thao tác gửi đó, loại bỏ 4 request trùng lặp còn lại.


---

## Tài liệu nguồn: 04-workflows/WF-02-claim-and-triage.md

# [WF-02] Tiếp nhận & Phân loại yêu cầu (Claim and Triage)

### [FR-STF-02] Nhân viên tiếp nhận, phân loại và quản lý ưu tiên yêu cầu

**Mô tả**
Hệ thống cho phép nhân viên phụ trách xem danh sách yêu cầu mới gửi đến, tiếp nhận yêu cầu (claim), phân loại theo từng nhóm vấn đề và đánh giá mức độ ưu tiên để chuẩn bị cho quá trình xử lý.

**Actor**
Nhân viên phòng ban (Staff) đã đăng nhập vào hệ thống.

**Preconditions**
- Nhân viên đã đăng nhập thành công.
- Nhân viên có quyền truy cập và xử lý các Ticket thuộc phòng ban của mình.
- Tồn tại các Ticket ở trạng thái `NEW` hoặc `TRANSFERRED`, chưa được tiếp nhận theo FR-STF-02.

**Luồng chính**
1. Nhân viên truy cập danh sách **Tiếp nhận yêu cầu**.
2. Hệ thống hiển thị danh sách các Ticket mới chưa có người tiếp nhận hoặc đang chờ phân loại.
3. Nhân viên chọn xem chi tiết một Ticket.
4. Nhân viên xem xét nội dung, tệp đính kèm và thực hiện thao tác **Tiếp nhận** (Claim) về cho bản thân. Phân công cho đồng nghiệp chỉ do MANAGER/ADMIN theo quyền đã có.
5. Nhân viên cập nhật **Mức độ ưu tiên** (Priority: Thấp, Trung bình, Cao, Khẩn cấp) và điều chỉnh **Nhóm vấn đề** (nếu sinh viên chọn chưa chính xác).
6. Nhân viên xác nhận lưu thông tin phân loại.
7. Hệ thống cập nhật trạng thái Ticket sang `IN_PROGRESS` (Đang xử lý), ghi nhận người phụ trách (Assignee) và lưu lịch sử thao tác.
8. Hệ thống gửi thông báo nội bộ cho sinh viên về việc Ticket đã được tiếp nhận.

**Business Rules**
- Một Ticket tại một thời điểm chỉ có tối đa **một nhân viên** chịu trách nhiệm chính (Assignee).
- Khi nhân viên bấm **Tiếp nhận**, hệ thống phải khóa trạng thái tiếp nhận đối với các nhân viên khác để tránh tranh chấp (race condition).
- Việc thay đổi mức độ ưu tiên và nhóm vấn đề phải được ghi lại trong lịch sử tra soát (Audit log).

**Alternative / Error Flows**
- **Xảy ra tranh chấp tiếp nhận (Race condition):** Nếu hai nhân viên cùng bấm tiếp nhận một Ticket gần như đồng thời, hệ thống duyệt cho người nhấn trước; người nhấn sau sẽ nhận được thông báo "Ticket đã được tiếp nhận bởi nhân viên khác" và danh sách tự động cập nhật lại.
- **Thao tác thất bại do mất kết nối:** Hệ thống hiển thị thông báo lỗi và giữ nguyên trạng thái cũ của Ticket.

**Acceptance Criteria**
- **AC-01:** Nhân viên chọn **Tiếp nhận** một Ticket mới -> Hệ thống gán tài khoản nhân viên đó làm người phụ trách và chuyển trạng thái sang `Đang xử lý`.
- **AC-02:** Nhân viên cập nhật mức độ ưu tiên cho Ticket -> Hệ thống lưu giá trị ưu tiên mới và cập nhật danh sách hiển thị.
- **AC-03:** Sinh viên nhận được thông báo trong hệ thống ngay khi Ticket chuyển sang trạng thái `Đang xử lý` kèm tên nhân viên/phòng ban phụ trách.
- **AC-04:** Hai nhân viên tiếp nhận cùng 1 Ticket đồng thời -> Hệ thống chỉ ghi nhận cho 1 người và báo lỗi hợp lệ cho người còn lại.

**Ví dụ Edge Case**
Nhân viên A và Nhân viên B cùng mở chi tiết Ticket #TK-1002 và nhấn nút **Tiếp nhận** cách nhau 0.2 giây.

**Expected Result:** Hệ thống phân công Ticket #TK-1002 cho Nhân viên A. Nhân viên B nhận thông báo "Ticket này đã được Nhân viên A tiếp nhận trước đó" và giao diện hiển thị thông tin cập nhật mới nhất.


---

## Tài liệu nguồn: 04-workflows/WF-03-request-supplement.md

# [WF-03] Yêu cầu bổ sung thông tin/giấy tờ (Request Supplement)

### [FR-STF-04 / FR-STU-03] Nhân viên yêu cầu bổ sung hồ sơ & Sinh viên phản hồi

**Mô tả**
Trong quá trình xử lý, nếu thông tin hoặc tài liệu sinh viên cung cấp bị thiếu hoặc chưa đủ cơ sở giải quyết, nhân viên có thể gửi yêu cầu sinh viên bổ sung thêm thông tin hoặc giấy tờ.

**Actor**
- Nhân viên phụ trách xử lý Ticket (Staff).
- Sinh viên gửi Ticket (Student).

**Preconditions**
- Ticket đang ở trạng thái `IN_PROGRESS` (Đang xử lý).
- Nhân viên thực hiện là người đang phụ trách Ticket đó.

**Luồng chính**
1. Nhân viên mở chi tiết Ticket đang xử lý và chọn chức năng **Yêu cầu bổ sung thông tin**.
2. Hệ thống hiển thị form nhập nội dung cần bổ sung.
3. Nhân viên nhập mô tả chi tiết các giấy tờ/thông tin sinh viên cần cung cấp thêm và nhấn **Gửi yêu cầu**.
4. Hệ thống chuyển trạng thái Ticket sang `NEED_MORE_INFO` (Cần bổ sung) và gửi thông báo nội bộ tới sinh viên.
5. Sinh viên nhận được thông báo, truy cập vào Ticket xem yêu cầu bổ sung.
6. Sinh viên nhập nội dung phản hồi và/hoặc tải lên tệp đính kèm bổ sung (ảnh/PDF).
7. Sinh viên nhấn **Xác nhận bổ sung**.
8. Hệ thống kiểm tra dữ liệu, cập nhật thông tin bổ sung vào Ticket, tự động chuyển trạng thái Ticket trở lại `IN_PROGRESS` (Đang xử lý) và thông báo cho nhân viên phụ trách.

**Business Rules**
- Ticket ở NEED_MORE_INFO để chờ sinh viên bổ sung. Không tự chốt thêm cơ chế dừng/tính lại SLA trong quy trình này; thời hạn giữ theo FR-MNG-02/BR-10 đã có.
- Chỉ có sinh viên chủ sở hữu Ticket mới có quyền tải tệp bổ sung hoặc gửi phản hồi.
- Tệp đính kèm bổ sung phải tuân thủ đúng định dạng hợp lệ (.pdf, .jpg, .jpeg, .png), tối đa 5 tệp, 5MB/tệp theo FR-STU-03.

**Alternative / Error Flows**
- **Sinh viên gửi phản hồi rỗng:** Hệ thống từ chối cập nhật và yêu cầu sinh viên phải nhập thông tin hoặc đính kèm tệp trước khi gửi.
- **Sinh viên gửi tệp đính kèm không đúng định dạng:** Hệ thống chặn và báo lỗi tệp không hợp lệ.

**Acceptance Criteria**
- **AC-01:** Nhân viên gửi yêu cầu bổ sung -> Ticket chuyển trạng thái thành `NEED_MORE_INFO`, sinh viên nhận được thông báo.
- **AC-02:** Sinh viên nhập nội dung phản hồi và đính kèm file hợp lệ -> Ticket chuyển lại trạng thái `Đang xử lý`, nhân viên nhận được thông báo.
- **AC-03:** Sinh viên bấm gửi phản hồi nhưng không nhập nội dung và không đính kèm file -> Hệ thống báo lỗi validation.
- **AC-04:** Sinh viên khác (không phải người tạo Ticket) tìm cách truy cập và nộp file bổ sung -> Hệ thống từ chối quyền truy cập (HTTP 403 Forbidden).

**Ví dụ Edge Case**
Sinh viên đính kèm file hình ảnh bị hỏng hoặc chọn nhầm file đuôi `.exe` khi phản hồi yêu cầu bổ sung của nhân viên.

**Expected Result:** Hệ thống kiểm tra định dạng tệp, từ chối tải lên file `.exe`, hiển thị thông báo lỗi "Chỉ chấp nhận định dạng PDF, JPG, JPEG, PNG" và giữ nguyên trạng thái Ticket là `NEED_MORE_INFO`.


---

## Tài liệu nguồn: 04-workflows/WF-04-transfer-department.md

# [WF-04] Chuyển tiếp yêu cầu sang phòng ban khác (Transfer Department)

### [FR-STF-03] Chuyển tiếp Ticket giữa các phòng ban (Transfer Department)

**Mô tả**
Hệ thống cho phép nhân viên chuyển tiếp Ticket sang đúng phòng ban khác nếu nội dung yêu cầu thuộc phạm vi giải quyết của đơn vị đó.

**Actor**
Nhân viên đang phụ trách Ticket (Staff).

**Preconditions**
- Ticket đang ở trạng thái NEW, IN_PROGRESS hoặc NEED_MORE_INFO theo FR-STF-03.
- Nhân viên thực hiện có quyền xử lý Ticket hiện tại.

**Luồng chính**
1. Nhân viên mở chi tiết Ticket và chọn chức năng **Chuyển phòng ban**.
2. Hệ thống hiển thị danh sách các phòng ban chuyên trách tại Aurora University (VD: Phòng Đào tạo, Phòng Công tác sinh viên, Phòng Tài chính - Kế toán,...).
3. Nhân viên chọn **Phòng ban đích** và nhập **Lý do chuyển tiếp** (bắt buộc).
4. Nhân viên chọn **Xác nhận chuyển**.
5. Hệ thống cập nhật phòng ban phụ trách mới cho Ticket, hủy bỏ gán cá nhân phụ trách cũ, và chuyển trạng thái Ticket thành `TRANSFERRED` (Đã chuyển giao), chờ phòng ban mới tiếp nhận.
6. Hệ thống lưu lại lịch sử chuyển tiếp (phòng ban cũ, phòng ban mới, lý do, người chuyển, thời gian).
7. Hệ thống gửi thông báo nội bộ đến nhân viên/quản lý của phòng ban mới.

**Business Rules**
- Lý do chuyển tiếp bắt buộc, 10–500 ký tự, không chấp nhận chỉ khoảng trắng theo FR-STF-03.
- Không cho phép chuyển tiếp Ticket về chính phòng ban hiện tại.
- Mọi tài liệu đính kèm, lịch sử trao đổi trước đó của Ticket phải được giữ nguyên vẹn khi chuyển sang phòng ban mới.
- Nhân viên phòng ban cũ không còn quyền cập nhật Ticket sau chuyển; quyền xem tuân theo phạm vi phòng ban/vai trò hiện có, không tự cấp quyền xem ngoài phòng ban.

**Alternative / Error Flows**
- **Không nhập lý do chuyển:** Hệ thống chặn thao tác và báo lỗi "Lý do chuyển tiếp không được để trống".
- **Chọn phòng ban đích trùng với phòng ban hiện tại:** Hệ thống hiển thị cảnh báo và không cho phép thực hiện.

**Acceptance Criteria**
- **AC-01:** Nhân viên chọn phòng ban mới và nhập lý do chuyển đầy đủ -> Hệ thống cập nhật đơn vị phụ trách mới thành công, ghi log lịch sử.
- **AC-02:** Nhân viên không nhập lý do chuyển -> Hệ thống hiển thị báo lỗi validation và dừng thao tác.
- **AC-03:** Ticket sau khi chuyển xuất hiện trong danh sách tiếp nhận của phòng ban mới.
- **AC-04:** Nhân viên phòng ban cũ không thể chỉnh sửa hay cập nhật trạng thái của Ticket sau khi đã chuyển thành công.

**Ví dụ Edge Case**
Nhân viên chọn phòng ban đích là "Phòng Tài chính" nhưng để trống ô "Lý do chuyển tiếp" rồi nhấn nút **Xác nhận chuyển**.

**Expected Result:** Hệ thống không thực hiện chuyển phòng ban, hiển thị thông báo lỗi màu đỏ ngay dưới trường Lý do chuyển: "Vui lòng nhập lý do chuyển tiếp yêu cầu" và giữ nguyên đơn vị xử lý hiện tại.


---

## Tài liệu nguồn: 04-workflows/WF-05-complete-and-resolve.md

# [WF-05] Cập nhật kết quả & Hoàn tất xử lý (Complete and Resolve)

### [FR-STF-05] Nhân viên cập nhật kết quả giải quyết và hoàn thành Ticket

**Mô tả**
Hệ thống cho phép nhân viên phụ trách ghi nhận kết quả xử lý, tải lên các tài liệu/kết quả giải quyết (nếu có) và xác nhận hoàn tất xử lý để sinh viên xem kết quả; việc đóng theo vòng đời hiện có.

**Actor**
Nhân viên phụ trách Ticket (Staff).

**Preconditions**
- Ticket đang ở trạng thái `Đang xử lý` (In Progress).
- Nhân viên thực hiện là người đang trực tiếp phụ trách Ticket đó.

**Luồng chính**
1. Nhân viên truy cập chi tiết Ticket cần hoàn thành.
2. Nhân viên chọn chức năng **Hoàn thành / Giải quyết**.
3. Nhân viên nhập nội dung **Kết quả giải quyết** (bắt buộc) và đính kèm file kết quả (nếu có).
4. Nhân viên bấm chọn **Xác nhận hoàn thành**.
5. Hệ thống ghi nhận nội dung giải quyết, cập nhật trạng thái Ticket sang `RESOLVED` (Đã giải quyết).
6. Hệ thống lưu mốc thời gian hoàn thành, tính toán thời gian xử lý thực tế phục vụ báo cáo SLA.
7. Hệ thống tự động gửi thông báo nội bộ cho sinh viên về việc Ticket đã được xử lý xong kèm kết quả giải quyết.

**Business Rules**
- Nội dung kết quả giải quyết bắt buộc 20–2000 ký tự, không chỉ khoảng trắng; tệp kết quả tùy chọn tối đa 3 tệp, 5MB/tệp, PDF/PNG/JPG/JPEG theo FR-STF-05.
- Sau hoàn tất, kết quả và lịch sử giữ theo chế độ chỉ đọc đã có; không mở thêm ngoại lệ sửa kết quả cho MANAGER/ADMIN.
- Lịch sử cập nhật và tệp kết quả được lưu trữ nguyên vẹn để tra soát.

**Alternative / Error Flows**
- **Để trống nội dung kết quả:** Hệ thống chặn thao tác, hiển thị thông báo "Vui lòng nhập nội dung kết quả giải quyết trước khi hoàn thành Ticket".
- **Lỗi lưu dữ liệu:** Hệ thống thông báo lỗi, giữ nguyên trạng thái `Đang xử lý` của Ticket.

**Acceptance Criteria**
- **AC-01:** Nhân viên nhập đầy đủ nội dung kết quả và xác nhận -> Hệ thống chuyển trạng thái Ticket thành `Hoàn thành`, ghi nhận mốc thời gian và gửi thông báo cho sinh viên.
- **AC-02:** Nhân viên để trống ô kết quả giải quyết -> Hệ thống hiển thị lỗi validation và dừng thao tác.
- **AC-03:** Sinh viên nhận được thông báo nội bộ ngay sau khi nhân viên bấm hoàn thành Ticket.
- **AC-04:** Nhân viên không phụ trách Ticket này tìm cách hoàn thành Ticket -> Hệ thống chặn truy cập (HTTP 403).

**Ví dụ Edge Case**
Nhân viên nhấn **Xác nhận hoàn thành** khi ô nội dung giải quyết chỉ chứa các dấu khoảng trắng "   ".

**Expected Result:** Hệ thống coi đây là nội dung không hợp lệ, không chuyển trạng thái Ticket và hiển thị lỗi validation: "Nội dung kết quả giải quyết không được để trống".


---

## Tài liệu nguồn: 04-workflows/WF-06-close-and-rate.md

# [WF-06] Sinh viên nhận kết quả & Đánh giá mức độ hài lòng (Close and Rate)

### [FR-STU-04] Sinh viên xem kết quả, đánh giá chất lượng dịch vụ (CSAT) & Đóng Ticket

**Mô tả**
Hệ thống cho phép sinh viên xem chi tiết kết quả xử lý của Ticket và gửi đánh giá mức độ hài lòng (số sao và góp ý) sau khi yêu cầu đã hoàn thành.

**Actor**
Sinh viên sở hữu Ticket (Student).

**Preconditions**
- Ticket đang ở trạng thái RESOLVED hoặc CLOSED của chính sinh viên; gửi đánh giá chỉ khi chưa có đánh giá theo FR-STU-04.
- Sinh viên đã đăng nhập vào hệ thống.

**Luồng chính**
1. Sinh viên nhận thông báo hoặc truy cập danh sách Ticket cá nhân, chọn Ticket đã hoàn thành.
2. Sinh viên xem nội dung kết quả giải quyết và các tệp đính kèm (nếu có) từ nhân viên.
3. Sinh viên chọn mức **Đánh giá hài lòng** (thang điểm từ 1 đến 5 sao).
4. Sinh viên nhập **Nhận xét / Góp ý** (không bắt buộc).
5. Sinh viên nhấn nút **Gửi đánh giá**.
6. Hệ thống lưu số sao, nhận xét, trạng thái đánh giá. Ticket đang RESOLVED được chuyển CLOSED theo FR-STU-04; Ticket đã CLOSED không mở lại xử lý.
7. Hệ thống hiển thị thông báo cảm ơn sinh viên và khóa form đánh giá cho Ticket này.

**Business Rules**
- Mỗi Ticket chỉ được phép gửi đánh giá **duy nhất 1 lần**.
- Việc đánh giá là tự nguyện, sinh viên có thể xem kết quả mà không bắt buộc phải đánh giá ngay.
- Kết quả đánh giá được tổng hợp tự động vào Dashboard báo cáo cho Ban quản lý.

**Alternative / Error Flows**
- **Sinh viên gửi đánh giá lại cho Ticket đã đánh giá:** Hệ thống ẩn form đánh giá và chỉ hiển thị kết quả đánh giá đã gửi trước đó.
- **Mất kết nối khi gửi đánh giá:** Hiển thị thông báo thử lại; giữ số sao và nhận xét đã nhập theo AC-04 của FR-STU-04, không báo thành công khi chưa có kết quả lưu.

**Acceptance Criteria**
- **AC-01:** Sinh viên chọn số sao (1–5 sao), nhập nhận xét và bấm **Gửi đánh giá** -> Hệ thống lưu đánh giá thành công và hiển thị thông báo ghi nhận.
- **AC-02:** Sinh viên chọn số sao và để trống nhận xét -> Hệ thống vẫn chấp nhận và lưu đánh giá thành công.
- **AC-03:** Sau khi đã gửi đánh giá, giao diện Ticket hiển thị đánh giá cũ và không cho phép chỉnh sửa/gửi lại.
- **AC-04:** Sinh viên khác không sở hữu Ticket không thể thực hiện đánh giá (HTTP 403).

**Ví dụ Edge Case**
Sinh viên mở hai tab trình duyệt cùng lúc cho Ticket đã hoàn thành và bấm **Gửi đánh giá** trên cả hai tab.

**Expected Result:** Tab gửi đầu tiên ghi nhận đánh giá thành công. Tab thứ hai gửi sau sẽ nhận thông báo "Ticket này đã được đánh giá trước đó" và tự động làm mới lại giao diện hiển thị đánh giá cũ.


---

## Tài liệu nguồn: 05-non-functional-requirements/README.md

# 05-non-functional-requirements: Yêu cầu Phi chức năng UniSupport

Thư mục này tập hợp toàn bộ các tài liệu chuẩn hóa về **Yêu cầu Phi chức năng (Non-Functional Requirements - NFR)** của hệ thống UniSupport tại Aurora University. Các yêu cầu này đóng vai trò làm khung tiêu chuẩn cho thiết kế kiến trúc, phát triển phần mềm và làm tiêu chí nghiệm thu kỹ thuật.

---

## Danh sách Yêu cầu Phi chức năng

| Mã Tài liệu | Tên Yêu cầu | Phạm vi chính |
| :--- | :--- | :--- |
| **[performance.md](05-non-functional-requirements/performance.md)** | Yêu cầu Hiệu năng | Tối ưu cho quy mô 3.000 sinh viên, thời gian phản hồi API $\le 500$ms, dung lượng tệp tối đa 10 MB. |
| **[security.md](05-non-functional-requirements/security.md)** | Yêu cầu Bảo mật | Phân quyền RBAC 3 vai trò, mã hóa mật khẩu, bảo mật đường dẫn tệp đính kèm và Audit log. |
| **[reliability.md](05-non-functional-requirements/reliability.md)** | Yêu cầu Độ ổn định | Độ sẵn sàng $\ge 98.5\%$, đảm bảo toàn vẹn giao dịch (ACID), xử lý lỗi thân thiện. |
| **[usability.md](05-non-functional-requirements/usability.md)** | Yêu cầu Tính dễ dùng | Giao diện Responsive (PC/Mobile), hỗ trợ 2 ngôn ngữ (Việt/Anh), màu sắc trạng thái trực quan. |
| **[observability.md](05-non-functional-requirements/observability.md)** | Yêu cầu Giám sát & Log | Cấu trúc log JSON (`INFO`/`WARN`/`ERROR`), log tra soát thao tác và API Health check. |
| **[deployment.md](05-non-functional-requirements/deployment.md)** | Yêu cầu Triển khai | Đóng gói Docker, triển khai trên tên miền và máy chủ do Aurora University cung cấp. |

---

## Nguyên tắc áp dụng & Giới hạn phạm vi
- **Bám sát Scope & Assumptions:** Các chỉ số NFR được thiết kế vừa đặn cho quy mô 3.000 sinh viên của Aurora University, không phình to kiến trúc vô lý.
- **Cơ sở Kiểm thử UAT:** Các mục tiêu NFR đi kèm tiêu chí nghiệm thu rõ ràng (`NFR-xxx-01`), làm căn cứ đánh giá chất lượng trong giai đoạn kiểm thử 10 ngày nghiệm thu của nhà trường.


---

## Tài liệu nguồn: 05-non-functional-requirements/deployment.md

# [NFR-DEP] Yêu cầu về Triển khai & Hạ tầng (Deployment Requirements)

### 1. Tổng quan
Tài liệu quy định các điều kiện hạ tầng, môi trường chạy và quy trình triển khai ứng dụng Web UniSupport lên hệ thống của Aurora University theo thỏa thuận cam kết.

### 2. Điều kiện Hạ tầng do Client (Aurora University) Cung cấp
Phù hợp với các Giả định dự án (Assumptions), hạ tầng máy chủ và tên miền hoàn toàn do nhà trường bàn giao:
- **Máy chủ Web/Database:** Máy chủ ảo (VPS) hoặc máy chủ vật lý chạy OS Linux (Ubuntu Server 20.04/22.04 LTS) hoặc Windows Server.
- **Cấu hình tối thiểu đề xuất:** 
  - CPU: 2 Core vCPU.
  - RAM: 4 GB.
  - Dung lượng đĩa cứng: Tối thiểu 50 GB SSD khả dụng (phục vụ lưu trữ dữ liệu và tệp đính kèm).
- **Mạng & Tên miền:**
  - Tên miền/Tên miền phụ chính thức (VD: `unisupport.aurora.edu.vn`).
  - Cấu hình địa chỉ IP Public và chứng chỉ bảo mật SSL/TLS (HTTPS).

### 3. Phương án Triển khai (Deployment Strategy)
- **Đóng gói ứng dụng:** Hệ thống được đóng gói chuẩn hóa bằng Docker / Docker Compose (bao gồm Frontend, Backend API, Database) giúp việc cài đặt lên hạ tầng của nhà trường diễn ra nhanh chóng, độc lập với môi trường.
- **Môi trường:**
  - **Staging/UAT Environment:** Phục vụ kiểm thử nghiệm thu 10 ngày với nhà trường.
  - **Production Environment:** Môi trường vận hành chính thức sau khi ký nghiệm thu.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-DEP-01:** Hệ thống triển khai thành công trên hạ tầng của Aurora University và truy cập ổn định thông qua tên miền/HTTPS do nhà trường cung cấp.
- **NFR-DEP-02:** Đội ngũ phát triển bàn giao đầy đủ Tài liệu hướng dẫn Cài đặt & Vận hành (Deployment Guide) giúp cán bộ IT nhà trường có thể chủ động khởi động lại service khi cần.


---

## Tài liệu nguồn: 05-non-functional-requirements/observability.md

# [NFR-OBS] Yêu cầu về Giám sát & Ghi log (Observability & Logging Requirements)

### 1. Tổng quan
Tài liệu định nghĩa các yêu cầu về khả năng quan sát, theo dõi trạng thái hoạt động và lưu trữ nhật ký hệ thống (System Logs) nhằm hỗ trợ quản trị viên Aurora University dễ dàng tra soát, phát hiện và chẩn đoán sự cố khi vận hành hệ thống Web Application UniSupport.

### 2. Cấu trúc và Quy định Ghi Log (Logging Standards)
Hệ thống triển khai 2 nhóm log chính:

#### 2.1 System & Application Log (Log hệ thống & Ứng dụng)
- **Cấp độ Log (Log Levels):** `INFO`, `WARN`, `ERROR`.
- **Định dạng chuẩn:** JSON/Plain text bao gồm các trường bắt buộc:
  - `timestamp`: Thời gian phát sinh sự cố (định dạng ISO 8601).
  - `level`: Cấp độ nghiêm trọng.
  - `module`: Phân hệ phát sinh log (VD: `M01-student-portal`, `M05-rbac`).
  - `message`: Nội dung mô tả chi tiết.
  - `stack_trace`: Lỗi kỹ thuật chi tiết (chỉ áp dụng đối với cấp độ `ERROR`).

#### 2.2 Audit Log (Log tra soát nghiệp vụ)
- Tự động ghi lại các thao tác ghi/sửa/xóa dữ liệu quan trọng của người dùng.
- Thông tin lưu trữ: `User_ID`, `Role`, `Action_Type`, `Resource_Target` (Ticket ID, Account ID), `IP_Address`, `Timestamp`.

### 3. Giám sát Trạng thái (System Monitoring)
- **Health Check Endpoint:** Cung cấp API `/api/v1/health` công khai ở mức cơ bản để hạ tầng của nhà trường kiểm tra trạng thái hoạt động của Service (Database Connection, File System Storage).
- **Lưu trữ Log:** Nhật ký ứng dụng được ghi ra file log theo ngày và giữ tối thiểu 30 ngày trên máy chủ triển khai.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-OBS-01:** Khi phát sinh lỗi kết nối cơ sở dữ liệu hoặc lỗi ứng dụng (5xx), hệ thống phải ghi vết bản ghi `ERROR` kèm chi tiết lỗi vào file log.
- **NFR-OBS-02:** Truy cập API `/api/v1/health` trả về HTTP status `200 OK` kèm trạng thái hoạt động của cơ sở dữ liệu.
- **NFR-OBS-03:** Thao tác đổi vai trò tài khoản hoặc đổi trạng thái Ticket đều sinh bản ghi Audit Log tra soát chính xác.


---

## Tài liệu nguồn: 05-non-functional-requirements/performance.md

# [NFR-PERF] Yêu cầu về Hiệu năng (Performance Requirements)

### 1. Tổng quan
Tài liệu này xác định các chỉ số hiệu năng mục tiêu cho hệ thống UniSupport. Hệ thống được thiết kế tối ưu cho quy mô **3.000 sinh viên** tại Aurora University và không bao gồm yêu cầu tối ưu cho kiến trúc chịu tải lớn vượt quá phạm vi này.

### 2. Chỉ số hiệu năng chính (KPIs)

| Chỉ số | Mục tiêu | Điều kiện thử nghiệm |
| :--- | :--- | :--- |
| **Thời gian phản hồi trang (Page Load Time)** | $\le 2.0$ giây | Tải trang trên kết nối mạng tiêu chuẩn ($\ge 10$ Mbps) |
| **Thời gian xử lý API (API Response Time)** | $\le 500$ ms | Cho 95% các tác vụ CRUD thông thường (Read/Write Ticket) |
| **Tải concurrent (Concurrent Users)** | 100 - 150 người dùng đồng thời | Tương ứng đỉnh điểm giờ cao điểm của trường |
| **Dung lượng tệp đính kèm (File Attachment)** | Tối đa 10 MB / tệp | Định dạng cho phép: `.pdf`, `.jpg`, `.png` |
| **Thời gian tải lên tệp (Upload Speed)** | $\le 5.0$ giây | Đối với tệp dung lượng tối đa 10 MB |

### 3. Quy định về Giới hạn Tải (Load & Capacity Limits)
- **Quy mô người dùng:** Hệ thống đảm bảo hoạt động mượt mà với cơ sở dữ liệu lên đến 3.000 tài khoản sinh viên và khoảng 50-100 tài khoản cán bộ/quản lý.
- **Giới hạn chịu tải:** Hệ thống không cam kết duy trì hiệu năng nếu lượng truy cập đồng thời vượt quá 300 người dùng cùng thời điểm.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-PERF-01:** Khi 100 người dùng thực hiện thao tác gửi/xem Ticket cùng lúc, thời gian phản hồi trung bình của API không vượt quá 1.0 giây.
- **NFR-PERF-02:** Thao tác tải lên tệp đính kèm PDF dung lượng 5 MB hoàn tất trong thời gian dưới 3 giây.


---

## Tài liệu nguồn: 05-non-functional-requirements/reliability.md

# [NFR-REL] Yêu cầu về Độ ổn định & Tin cậy (Reliability Requirements)

### 1. Tổng quan
Tài liệu định nghĩa các chỉ số và quy tắc nhằm đảm bảo hệ thống UniSupport duy trì trạng thái hoạt động ổn định và nhất quán trên hạ tầng do Aurora University cung cấp.

### 2. Chỉ số sẵn sàng & Tin cậy

| Chỉ số | Yêu cầu | Ghi chú |
| :--- | :--- | :--- |
| **Mức độ sẵn sàng (Availability)** | $\ge 98.5\%$ | Trong thời gian hoạt động hành chính của nhà trường |
| **Toàn vẹn dữ liệu (Data Integrity)** | 100% | Không xảy ra mất mát dữ liệu Ticket trong điều kiện vận hành bình thường |
| **Xử lý sự cố lỗi (Graceful Degradation)** | Hiển thị thông báo lỗi thân thiện | Không để lộ lỗi hệ thống (Stack trace/Code error) cho người dùng cuối |

### 3. Toàn vẹn giao dịch & Khôi phục
- **Đảm bảo giao dịch (Database Transaction):** Thao tác gửi Ticket bao gồm thông tin văn bản và lưu tệp đính kèm phải tuân thủ nguyên tắc All-or-Nothing (ACID). Nếu lưu tệp thất bại, thông tin Ticket sẽ không được tạo để tránh dữ liệu mống/rác.
- **Hạ tầng & Sao lưu:** Tính ổn định, tên miền, chứng chỉ SSL và sao lưu dữ liệu máy chủ hoàn toàn phụ thuộc vào hạ tầng do Aurora University cung cấp (nằm ngoài phạm vi bảo trì dài hạn của nhà phát triển).

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-REL-01:** Khi xảy ra lỗi kết nối mạng trong quá trình gửi Ticket, hệ thống hủy giao dịch và không lưu Ticket ở trạng thái dở dang (dữ liệu không hoàn chỉnh).
- **NFR-REL-02:** Giao diện người dùng hiển thị thông điệp lỗi rõ ràng (ví dụ: "Có lỗi xảy ra, vui lòng thử lại sau") thay vì lộ mã lỗi lập trình (Stack trace).


---

## Tài liệu nguồn: 05-non-functional-requirements/security.md

# [NFR-SEC] Yêu cầu về Bảo mật (Security Requirements)

### 1. Tổng quan
Tài liệu quy định các nguyên tắc bảo mật thông tin, phân quyền truy cập và an toàn dữ liệu áp dụng cho hệ thống UniSupport. Theo giả định dự án, hệ thống tuân thủ các quy chuẩn bảo mật cơ bản, không bao gồm kiểm thử bảo mật chuyên sâu hay chứng nhận bảo mật quốc tế.

### 2. Xác thực và Phân quyền (Authentication & Authorization)
- **Đăng nhập:** Người dùng đăng nhập bằng tài khoản và mật khẩu riêng. Mật khẩu phải được mã hóa dạng hash (ví dụ: Bcrypt/Argon2) trước khi lưu vào CSDL.
- **Mô hình RBAC (Role-Based Access Control):**
  - **Sinh viên (Student):** Chỉ được xem, tạo và tương tác với các Ticket do chính tài khoản đó tạo ra.
  - **Nhân viên (Staff):** Xem và xử lý các Ticket thuộc phòng ban được gán thẩm quyền.
  - **Quản lý (Manager):** Xem báo cáo tổng quan, quản lý tài khoản và phân quyền hệ thống.
- **Bảo mật tệp đính kèm:** Đường dẫn tệp đính kèm (PDF/Ảnh) phải được bảo vệ. Hệ thống xác thực quyền truy cập trước khi cho phép tải xuống/xem tệp; không công khai đường dẫn trực tiếp (Direct URL).

### 3. Tra soát và Nhật ký hoạt động (Audit Logging)
- Hệ thống tự động ghi lại lịch sử đối với các thao tác quan trọng:
  - Đăng nhập / Đăng xuất / Thay đổi mật khẩu.
  - Thay đổi trạng thái Ticket, chuyển tiếp phòng ban.
  - Cập nhật kết quả giải quyết và tạo/sửa tài khoản.
- Nhật ký tra soát (Audit Log) bao gồm các thông tin: `User_ID`, `Action`, `Timestamp`, `IP_Address`, `Target_ID`.

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-SEC-01:** Sinh viên A nhập đường dẫn URL tệp đính kèm của Sinh viên B -> Hệ thống chặn truy cập và trả về lỗi `403 Forbidden`.
- **NFR-SEC-02:** Tất cả mật khẩu trong cơ sở dữ liệu phải được lưu dưới dạng chuỗi mã hóa hash, không hiển thị plain-text.
- **NFR-SEC-03:** Mọi thao tác đổi trạng thái Ticket đều sinh bản ghi trong bảng Audit Log.


---

## Tài liệu nguồn: 05-non-functional-requirements/usability.md

# [NFR-USA] Yêu cầu về Tính dễ sử dụng (Usability Requirements)

### 1. Tổng quan
Tài liệu quy định các tiêu chuẩn về thiết kế giao diện (UI) và trải nghiệm người dùng (UX) đối với hệ thống Web Application UniSupport, đảm bảo sự thân thiện và thuận tiện cho cả 3 nhóm vai trò.

### 2. Tiêu chuẩn Giao diện & Trải nghiệm

| Tiêu chí | Mô tả chi tiết |
| :--- | :--- |
| **Thiết kế Responsive** | Tối ưu hiển thị linh hoạt trên cả trình duyệt máy tính (Desktop) và thiết bị di động (Mobile Web / Tablet). |
| **Đa ngôn ngữ (Multilingual)** | Hỗ trợ 2 ngôn ngữ giao diện ở mức cơ bản: **Tiếng Việt** và **Tiếng Anh**. Người dùng có thể chuyển đổi ngôn ngữ nhanh trên thanh điều hướng. |
| **Tính nhất quán (Consistency)** | Thống nhất về màu sắc nhận diện, font chữ, kích thước nút bấm và quy chuẩn bảng biểu trên toàn bộ các trang. |
| **Trạng thái thao tác** | Luôn hiển thị phản hồi tức thì cho người dùng khi thực hiện tác vụ (VD: hiệu ứng Loading khi gửi biểu mẫu, Toast notification khi thành công/thất bại). |

### 3. Quy chuẩn Đồ họa & Điều hướng
- **Đơn giản hóa form nhập:** Form tạo Ticket cho sinh viên không quá 5 trường thông tin bắt buộc nhằm tối ưu thời gian thao tác.
- **Phân loại rõ ràng:** Sử dụng màu sắc mã hóa cho các trạng thái Ticket (VD: `Mới` - Xanh dương, `Đang xử lý` - Cam, `Hoàn thành` - Xanh lá, `Quá hạn` - Đỏ).

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-USA-01:** Giao diện phân hệ Sinh viên hiển thị đầy đủ, không bị đè chữ hay tràn khung hình khi truy cập trên trình duyệt điện thoại di động (Mobile Web).
- **NFR-USA-02:** Khi chuyển đổi ngôn ngữ giao diện sang Tiếng Anh, toàn bộ các nhãn nút bấm, tiêu đề trang và thông báo chính chuyển sang Tiếng Anh tương ứng.
- **NFR-USA-03:** Sinh viên hoàn thành việc gửi một Ticket hỗ trợ trong vòng dưới 3 phút mà không cần hướng dẫn trực tiếp.


---

## Tài liệu nguồn: 06-acceptance/README.md

# 06-acceptance: Tiêu chí & Kịch bản Nghiệm thu UniSupport

Thư mục này đóng vai trò làm bộ tài liệu căn cứ phục vụ cho quá trình kiểm thử nội bộ và **giai đoạn Nghiệm thu UAT 10 ngày làm việc** của Aurora University (được quy định tại Mục 5.2 của Project Proposal).

---

## Danh mục Tài liệu

| Tên File | Nội dung chính |
| :--- | :--- |
| **[traceability-matrix.md](06-acceptance/traceability-matrix.md)** | Ma trận truy xuất yêu cầu (RTM) liên kết giữa Yêu cầu nghiệp vụ, Quy trình, Phân hệ và Test Scenario. |
| **[test-scenarios.md](06-acceptance/test-scenarios.md)** | Chi tiết các kịch bản kiểm thử UAT cho 3 phân hệ (Sinh viên, Nhân viên, Quản lý) và Bảo mật. |

---

## Phạm vi truy xuất

RTM và kịch bản bám 14 FR đã chốt. 17 dòng Resources là công sức được đối chiếu riêng; không dùng chúng đổi mã yêu cầu hoặc cộng thêm 17 chức năng. Các ca hiện là dự kiến, chưa có bằng chứng chạy để xác nhận Pass. QA/UAT dùng giờ trong bảng nguồn, không tự tạo một ngân sách giờ khác.

## Quy trình & Tiêu chí Nghiệm thu (Acceptance Process)

### 1. Thời gian Nghiệm thu
- Quý trường (Aurora University) có **10 ngày làm việc** kể từ ngày bàn giao chính thức để tiến hành kiểm thử UAT trên môi trường Staging/Production.

### 2. Tiêu chí Đạt Nghiệm thu (Pass Criteria)
- Các luồng chính của 3 phân hệ (Sinh viên, Nhân viên, Quản lý) hoạt động đúng kịch bản và ổn định.
- Phân quyền RBAC hoạt động chính xác theo từng vai trò; bảo mật tệp đính kèm được đảm bảo.
- Không còn lỗi làm gián đoạn chức năng chính (Blocking/Critical bugs).
- Bàn giao đầy đủ tài liệu hướng dẫn sử dụng, tài liệu cài đặt, ERD và mã nguồn theo cam kết.

### 3. Quy định xử lý lỗi phát sinh
- Các lỗi kỹ thuật nhỏ phát sinh do phía đơn vị phát triển (nếu có) được ghi nhận và có kế hoạch khắc phục cụ thể, không tính là điều kiện từ chối nghiệm thu nếu không ảnh hưởng trực tiếp đến chức năng chính của hệ thống.


---

## Tài liệu nguồn: 06-acceptance/test-scenarios.md

# Kịch bản nghiệm thu theo PRD đã chốt

Phạm vi: 14 FR trong M01–M03; 17 dòng Resources là công sức, không phải 17 FR. Các ca dưới đây là kịch bản dự kiến, **chưa phải kết quả chạy thử hoặc chứng nhận Pass**. Chi tiết giới hạn, lỗi và hiệu năng vẫn lấy từ Acceptance Criteria của từng FR. Không cộng estimate QA/UAT ngoài Resources.

## [TS-STU-01] FR-STU-01 — Đăng nhập tài khoản sinh viên

- **Điều kiện:** ADMIN đã cấp tài khoản Student hoạt động.
- **Thao tác:** Đăng nhập bằng tài khoản hợp lệ; thử sai mật khẩu hoặc tài khoản khóa.
- **Kết quả mong đợi:** Vào danh sách Ticket cá nhân khi hợp lệ; bị từ chối với thông báo khi không hợp lệ.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STU-02] FR-STU-02 — Gửi yêu cầu hỗ trợ (Tạo Ticket)

- **Điều kiện:** Student đã đăng nhập, danh mục nhóm vấn đề đã có.
- **Thao tác:** Chọn một nhóm vấn đề, tiêu đề 10–150 và mô tả 20–2000; chọn PDF/PNG/JPG/JPEG ≤5MB; gửi.
- **Kết quả mong đợi:** Tạo đúng một Ticket NEW ở phòng ban mặc định, hiển thị mã duy nhất. Thiếu trường, tệp >5MB, sai loại hoặc quá 5 tệp bị từ chối; bấm nhiều lần không tạo trùng.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STU-03] FR-STU-03 — Theo dõi tiến độ & Bổ sung thông tin/giấy tờ

- **Điều kiện:** Có Ticket của Student; khi bổ sung phải NEED_MORE_INFO.
- **Thao tác:** Xem danh sách/chi tiết; đọc yêu cầu bổ sung từ Staff rồi gửi tệp/lời nhắn đúng giới hạn.
- **Kết quả mong đợi:** Chỉ xem Ticket của mình; bổ sung trên cùng mã Ticket và quay lại IN_PROGRESS. Không sửa nội dung gốc; không được gửi bổ sung sai trạng thái.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STU-04] FR-STU-04 — Xem kết quả giải quyết & Đánh giá mức độ hài lòng

- **Điều kiện:** Ticket của Student ở RESOLVED/CLOSED.
- **Thao tác:** Xem kết quả; chọn 1–5 sao và nhận xét tối đa 500 ký tự nếu muốn; gửi.
- **Kết quả mong đợi:** Kết quả, tệp và thời gian hoàn thành đúng; lưu đánh giá một lần, dạng chỉ đọc sau gửi. RESOLVED sang CLOSED; không mở lại xử lý. Lỗi mạng giữ nội dung để thử lại.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-01] FR-STF-01 — Nhân viên đăng nhập hệ thống

- **Điều kiện:** ADMIN đã cấp tài khoản STAFF và gán phòng ban.
- **Thao tác:** Đăng nhập hợp lệ; thử tài khoản Student ở cổng Staff.
- **Kết quả mong đợi:** Staff vào đúng Queue phòng ban; sai vai trò bị từ chối. Không cấp thêm quyền tạo tài khoản hoặc Assign đồng nghiệp cho Staff.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-02] FR-STF-02 — Tiếp nhận và phân loại yêu cầu (Claim & Triage)

- **Điều kiện:** Ticket NEW/TRANSFERRED thuộc phòng ban Staff.
- **Thao tác:** Đọc nội dung; chọn nhóm vấn đề và mức ưu tiên nếu cần; tiếp nhận; thử hai Staff cùng tiếp nhận.
- **Kết quả mong đợi:** Một người được giao phụ trách, Ticket IN_PROGRESS; người đến sau nhận thông báo và dữ liệu cập nhật. Không nghiệm thu tự đổi thời hạn SLA chỉ do đổi priority.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-03] FR-STF-03 — Chuyển yêu cầu sang đúng phòng ban

- **Điều kiện:** Ticket thuộc quyền thao tác và trạng thái theo FR-STF-03.
- **Thao tác:** Chọn phòng ban khác, lý do 10–500 ký tự, xác nhận chuyển.
- **Kết quả mong đợi:** Ticket TRANSFERRED trong Queue phòng ban mới, bỏ phụ trách cũ và giữ lịch sử/tệp. Lý do trống/toàn khoảng trắng hoặc cùng phòng ban bị từ chối.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-04] FR-STF-04 — Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement)

- **Điều kiện:** Nhân viên đang phụ trách Ticket IN_PROGRESS.
- **Thao tác:** Nhập yêu cầu bổ sung 10–1000 ký tự rồi gửi; Student mở cùng Ticket.
- **Kết quả mong đợi:** Ticket NEED_MORE_INFO; Student thấy đúng nội dung và nhận thông báo theo phạm vi có sẵn. Không có phép đo nghiệm thu mới về tạm dừng SLA.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-STF-05] FR-STF-05 — Ghi kết quả và hoàn tất xử lý yêu cầu

- **Điều kiện:** Nhân viên phụ trách Ticket IN_PROGRESS.
- **Thao tác:** Nhập kết quả 20–2000 ký tự; tệp tùy chọn tối đa 3 tệp, 5MB/tệp; xác nhận hoàn tất.
- **Kết quả mong đợi:** Ticket RESOLVED, ghi thời gian và sinh viên xem được kết quả. Kết quả trống/quá ngắn bị từ chối; lỗi upload giữ form. Nhãn giải quyết/đóng khớp trạng thái thật.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-01] FR-MNG-01 — Quản lý đăng nhập & Xác thực phân quyền

- **Điều kiện:** Tài khoản MANAGER/ADMIN hoạt động.
- **Thao tác:** Đăng nhập từng vai trò; thử Student/Staff vào cổng quản trị.
- **Kết quả mong đợi:** MANAGER chỉ dữ liệu phòng ban; ADMIN dữ liệu toàn trường; vai trò không phù hợp bị từ chối.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-02] FR-MNG-02 — Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision)

- **Điều kiện:** Có dữ liệu Ticket trong kỳ và phạm vi được phép.
- **Thao tác:** Xem các thẻ, workload, cảnh báo; đổi kỳ và mở thẻ quá hạn.
- **Kết quả mong đợi:** Số liệu/danh sách đúng trạng thái và phạm vi, theo SLA hiện có; làm mới theo AC gốc. Không nghiệm thu luồng Escalation hoặc deadline mới.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-03] FR-MNG-03 — Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export)

- **Điều kiện:** Có dữ liệu báo cáo/đánh giá và vai trò phù hợp.
- **Thao tác:** Chọn Xu hướng/Hiệu năng/CSAT, bộ lọc; xuất Excel/CSV; thử không có dữ liệu hoặc >10.000 dòng.
- **Kết quả mong đợi:** Báo cáo và file đúng bộ lọc/quyền; CSAT dùng đánh giá đã gửi. Không dữ liệu vô hiệu hóa xuất; vượt giới hạn báo thu hẹp kỳ. Font/ngày tháng theo AC gốc.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-04] FR-MNG-04 — Quản trị người dùng & Phân quyền (User Management & RBAC)

- **Điều kiện:** ADMIN đã đăng nhập.
- **Thao tác:** Cấp tài khoản Student/Staff, gán vai trò/phòng ban theo yêu cầu; khóa/mở khóa; thử trùng email hoặc tự khóa.
- **Kết quả mong đợi:** Đăng nhập đúng cổng và scope; khóa/mở theo phiên hiện có. Trùng thông tin/tự khóa bị từ chối; MANAGER không được quản trị tài khoản. Không yêu cầu import Excel hay gửi mật khẩu tự động.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## [TS-MNG-05] FR-MNG-05 — Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail)

- **Điều kiện:** Có thao tác quản trị và Ticket/tệp thuộc người khác.
- **Thao tác:** ADMIN xem nhật ký; người không có quyền thử mở tệp; kiểm tra giao diện log.
- **Kết quả mong đợi:** Nhật ký ghi đúng các thao tác hiện có, chỉ đọc; truy cập tệp ngoài quyền bị từ chối. Không thử UI dọn dẹp/archiving chưa được chốt.
- **Trạng thái kiểm chứng:** Chưa chạy; cần ghi kết quả thực tế khi nghiệm thu.

## Các dòng công sức chưa đủ đặc tả để coi là ca nghiệm thu mới

FAQ, mở lại xử lý, Escalation nhiều cấp và màn hình quản lý lưu trữ chưa có FR nghiệp vụ được chốt. Giữ giờ nguồn nhưng không đặt ca kiểm thử mới chứng minh đã có những chức năng này. Thông báo và phân quyền được kiểm tra trong luồng FR hiện có; không cộng mã FR-NTF/FR-SEC hoặc cộng giờ lần thứ hai.


---

## Tài liệu nguồn: 06-acceptance/traceability-matrix.md

# Ma trận truy xuất PRD đã chốt

14 FR có cùng mã/ý nghĩa với 3 PRD chi tiết. Mã R là dòng công sức trong [bảng Resources](Phan_bo_Resources_Antigravity.md), không phải FR. Những mã FR-ADM-01..06, FR-STU-05, FR-STF-06 từng dùng thay cho dòng công sức đã được chuyển thành R-ADM/R-STU/R-STF trong bảng đối chiếu; không có chức năng mới từ việc đổi mã.

| FR | Tên yêu cầu | PRD | Luồng | Kịch bản | Dòng công sức đối chiếu | Kiểm chứng |
| --- | --- | --- | --- | --- | --- | --- |
| FR-STU-01 | Đăng nhập tài khoản sinh viên | [M01](03-modules/M01-student-portal/prd.md) | — | TS-STU-01 | R-ADM-01 | Chưa chạy |
| FR-STU-02 | Gửi yêu cầu hỗ trợ (Tạo Ticket) | [M01](03-modules/M01-student-portal/prd.md) | WF-01 | TS-STU-02 | R-STU-02 | Chưa chạy |
| FR-STU-03 | Theo dõi tiến độ & Bổ sung thông tin/giấy tờ | [M01](03-modules/M01-student-portal/prd.md) | WF-01, WF-03 | TS-STU-03 | R-STU-03, R-STU-04, R-STU-05 | Chưa chạy |
| FR-STU-04 | Xem kết quả giải quyết & Đánh giá mức độ hài lòng | [M01](03-modules/M01-student-portal/prd.md) | WF-06 | TS-STU-04 | R-STU-05, R-STF-06, R-ADM-06 | Chưa chạy |
| FR-STF-01 | Nhân viên đăng nhập hệ thống | [M02](03-modules/M02-staff-operations/prd.md) | — | TS-STF-01 | R-ADM-01 | Chưa chạy |
| FR-STF-02 | Tiếp nhận và phân loại yêu cầu (Claim & Triage) | [M02](03-modules/M02-staff-operations/prd.md) | WF-02 | TS-STF-02 | R-STF-01, R-STF-02, R-STF-03 | Chưa chạy |
| FR-STF-03 | Chuyển yêu cầu sang đúng phòng ban | [M02](03-modules/M02-staff-operations/prd.md) | WF-04 | TS-STF-03 | R-STF-05 | Chưa chạy |
| FR-STF-04 | Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement) | [M02](03-modules/M02-staff-operations/prd.md) | WF-03 | TS-STF-04 | R-STF-04 | Chưa chạy |
| FR-STF-05 | Ghi kết quả và hoàn tất xử lý yêu cầu | [M02](03-modules/M02-staff-operations/prd.md) | WF-05 | TS-STF-05 | R-STF-05, R-STF-06 | Chưa chạy |
| FR-MNG-01 | Quản lý đăng nhập & Xác thực phân quyền | [M03](03-modules/M03-management-dashboard/prd.md) | — | TS-MNG-01 | R-ADM-01 | Chưa chạy |
| FR-MNG-02 | Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision) | [M03](03-modules/M03-management-dashboard/prd.md) | Giám sát đầu ra WF-02/WF-05 | TS-MNG-02 | R-STF-03, R-ADM-05 | Chưa chạy |
| FR-MNG-03 | Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export) | [M03](03-modules/M03-management-dashboard/prd.md) | Báo cáo đầu ra WF-06 | TS-MNG-03 | R-ADM-06 | Chưa chạy |
| FR-MNG-04 | Quản trị người dùng & Phân quyền (User Management & RBAC) | [M03](03-modules/M03-management-dashboard/prd.md) | Cấp tài khoản liên cổng | TS-MNG-04 | R-ADM-01, R-ADM-03 | Chưa chạy |
| FR-MNG-05 | Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail) | [M03](03-modules/M03-management-dashboard/prd.md) | Tra soát đầu ra các luồng | TS-MNG-05 | R-ADM-03 | Chưa chạy |

Không cộng tổng giờ theo các hàng FR này: nhiều FR dùng chung một dòng công sức. Tổng giờ chỉ tính theo 17 dòng Resource cộng PM/DevOps, bằng 640. Ánh xạ CSAT với R-STU-05 là đối chiếu chưa tách effort riêng; không xác nhận một chức năng FAQ/mở lại/lưu trữ đã hoàn tất khi chưa có đặc tả.


---

## Tài liệu nguồn: 07-architecture/README.md

# 07 - Kiến trúc Hệ thống UniSupport (System Architecture)

Thư mục này chứa toàn bộ các tài liệu thiết kế kiến trúc kỹ thuật của hệ thống **UniSupport** (Aurora University Student Support System). Tài liệu đóng vai trò làm kim chỉ nam kỹ thuật cho đội ngũ phát triển, kiểm thử, cũng như hỗ trợ việc bàn giao và vận hành hệ thống.

---

## 1. Danh mục tài liệu

| STT | Tên File | Mô tả nội dung |
| :---: | :--- | :--- |
| **01** | [`system-context.md`](07-architecture/system-context.md) | Sơ đồ ngữ cảnh hệ thống (System Context Diagram - C4 Model Level 1), định nghĩa ranh giới hệ thống, các Actor tương tác và các tương tác ngoại vi. |
| **02** | [`architecture-overview.md`](07-architecture/architecture-overview.md) | Kiến trúc tổng quan hệ thống Web Application (Frontend & Backend), mô hình Layered Architecture, giao tiếp API và lưu trữ dữ liệu. |
| **03** | [`data-model.md`](07-architecture/data-model.md) | Mô hình cơ sở dữ liệu quan hệ (Relational Database Schema) và sơ đồ ERD chi tiết cho toàn bộ thực thể. |
| **04** | [`api-design.md`](07-architecture/api-design.md) | Quy chuẩn thiết kế RESTful API cho 3 phân hệ (Sinh viên, Nhân viên, Quản lý) và dịch vụ hệ thống. |
| **05** | [`security-design.md`](07-architecture/security-design.md) | Thiết kế bảo mật, xác thực tài khoản (Authentication), phân quyền 3 vai trò (RBAC) và bảo mật file đính kèm. |
| **06** | [`technical-decisions/`](07-architecture/technical-decisions/README.md) | Thư mục lưu trữ các quyết định kiến trúc quan trọng (Architectural Decision Records - ADR). |

---

## 2. Nguyên tắc thiết kế cốt lõi (Architecture Principles)

1. **Đơn giản & Tập trung (KISS Principle):**
   * Hệ thống được thiết kế tối ưu cho quy mô **3.000 sinh viên**, tập trung vào tính đúng đắn và ổn định của quy trình xử lý Ticket thay vì áp dụng các kiến trúc phân tán phức tạp không cần thiết (như Microservices/Event-driven).
2. **Bảo mật theo lớp (Defense in Depth):**
   * Áp dụng mô hình **RBAC (Role-Based Access Control)** nghiêm ngặt cho 3 vai trò: Sinh viên, Nhân viên, Quản lý.
   * Kiểm soát quyền truy cập chi tiết đến từng đối tượng Ticket và tệp đính kèm (PDF, PNG/JPG).
3. **Mô-đun hóa cao (Modular Monolith):**
   * Cấu trúc Backend phân tách rõ ràng giữa các Module nghiệp vụ (Student, Staff, Management, Notification, RBAC) giúp dễ dàng bảo trì, mở rộng và bàn giao source code.
4. **Phù hợp hạ tầng Client:**
   * Tối ưu hóa việc đóng gói và triển khai (Docker Containerized / Node.js Runtime) nhằm đáp ứng linh hoạt trên hạ tầng máy chủ nội bộ hoặc Cloud do Aurora University cung cấp.

---

## 3. Vai trò sử dụng tài liệu

* **Software Architect / Lead Dev:** Tham chiếu để định hướng phát triển và kiểm soát tuân thủ kiến trúc.
* **Backend / Frontend Developers:** Căn cứ triển khai chi tiết các chức năng, API và cấu trúc dữ liệu.
* **QA / QC Team:** Tham chiếu để xây dựng kịch bản kiểm thử hiệu năng, bảo mật và luồng dữ liệu.


---

## Tài liệu nguồn: 07-architecture/api-design.md

# [ARC-04] Thiết kế RESTful API (API Design Standard)

Tài liệu này chuẩn hóa quy cách thiết kế RESTful API cho toàn bộ các phân hệ trong hệ thống **UniSupport**, bao gồm chuẩn HTTP Status Codes, định dạng Request/Response và danh sách Endpoints chính.

---

## 1. Quy chuẩn API Tổng quan

* **Giao thức:** HTTPS
* **Đường dẫn cơ sở (Base URL):** `https://unisupport.aurora.edu.vn/api/v1`
* **Định dạng dữ liệu:** `application/json`
* **Mã hóa:** UTF-8

### 1.1 Cấu trúc Response Chuẩn (Standard Response Format)

#### Response Thành công (`200 OK`, `201 Created`):
```json
{
  "success": true,
  "code": 200,
  "message": "Thao tác thành công",
  "data": { ... }
}
```

#### Response Phân trang (Pagination Response):
```json
{
  "success": true,
  "code": 200,
  "data": [ ... ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total_items": 45,
    "total_pages": 5
  }
}
```

#### Response Lỗi (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `500 Internal Error`):
```json
{
  "success": false,
  "code": 400,
  "error_code": "INVALID_INPUT",
  "message": "Nội dung mô tả là bắt buộc.",
  "errors": [
    {
      "field": "description",
      "message": "Mô tả không được để trống"
    }
  ]
}
```

---

## 2. Danh sách API Endpoints Chính

### 2.1 Authentication & System (`/auth`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| :--- | :--- | :--- | :--- |
| **POST** | `/auth/login` | Public | Đăng nhập hệ thống & lấy JWT Token |
| **GET** | `/auth/me` | Authenticated | Lấy thông tin tài khoản đang đăng nhập |
| **POST** | `/auth/logout` | Authenticated | Đăng xuất |

### 2.2 Phân hệ Sinh viên (`/student`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| :--- | :--- | :--- | :--- |
| **POST** | `/student/tickets` | Student | Tạo mới Ticket hỗ trợ (kèm upload file) |
| **GET** | `/student/tickets` | Student | Xem danh sách Ticket cá nhân đã gửi |
| **GET** | `/student/tickets/{ticket_code}` | Student | Xem chi tiết tiến độ Ticket & lịch sử phản hồi |
| **POST** | `/student/tickets/{id}/supplement` | Student | Bổ sung thông tin/giấy tờ theo yêu cầu Nhân viên |
| **POST** | `/student/tickets/{id}/rating` | Student | Đánh giá mức độ hài lòng (1-5 sao) khi hoàn tất |

### 2.3 Phân hệ Nhân viên (`/staff`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| :--- | :--- | :--- | :--- |
| **GET** | `/staff/tickets` | Staff, Management | Lấy danh sách Ticket thuộc phòng ban phụ trách |
| **POST** | `/staff/tickets/{id}/claim` | Staff | Nhận phụ trách (Claim) Ticket |
| **PATCH** | `/staff/tickets/{id}/triage` | Staff | Phân loại & cập nhật độ ưu tiên Ticket |
| **POST** | `/staff/tickets/{id}/transfer` | Staff | Chuyển Ticket sang phòng ban khác |
| **POST** | `/staff/tickets/{id}/request-supplement` | Staff | Yêu cầu Sinh viên bổ sung giấy tờ/thông tin |
| **POST** | `/staff/tickets/{id}/resolve` | Staff | Cập nhật kết quả giải quyết & Đóng Ticket |

### 2.4 Phân hệ Quản lý & Admin (`/management`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| :--- | :--- | :--- | :--- |
| **GET** | `/management/dashboard/overview` | Management | Số liệu tổng quan (Ticket mới, đang xử lý, quá hạn) |
| **GET** | `/management/dashboard/metrics` | Management | Báo cáo SLA, thời gian xử lý trung bình, điểm đánh giá |
| **GET** | `/management/users` | Management | Danh sách tài khoản hệ thống |
| **POST** | `/management/users` | Management | Tạo tài khoản mới & phân quyền vai trò |
| **PATCH** | `/management/users/{id}` | Management | Cập nhật thông tin/trạng thái tài khoản |


---

## Tài liệu nguồn: 07-architecture/architecture-overview.md

# [ARC-02] Kiến trúc tổng quan Hệ thống (Architecture Overview)

> Nguồn chuẩn hóa nhân sự & phân bổ công sức: `Phan_bo_Resources_Antigravity.md`

Tài liệu này chi tiết hóa kiến trúc tổng thể phần mềm của ứng dụng Web Application **UniSupport**, bao gồm mô hình phân lớp, kiến trúc Frontend, Backend, chiến lược quản lý dữ liệu và luồng giao tiếp dữ liệu giữa các thành phần.

---

## 1. Mô hình Kiến trúc Tổng quan (High-Level Architecture)

UniSupport được xây dựng theo mô hình **Layered Monolithic Architecture (Kiến trúc đơn khối phân lớp)** nhằm đảm bảo tính đơn giản, dễ bảo trì, tối ưu thời gian phát triển trong **14 tuần (640h kế hoạch)** và hoạt động mượt mà trên hạ tầng phục vụ **3.000 sinh viên**.

```
+-----------------------------------------------------------------------------------+
|                                 CLIENT LAYER                                      |
|   Web Browser (PC Desktop & Mobile Browsers - Responsive Web UI / VI-EN)           |
+-----------------------------------------------------------------------------------+
                              |
                              | HTTPS / REST API (JSON)
                              v
+-----------------------------------------------------------------------------------+
|                                PRESENTATION LAYER                                 |
|   - Student UI Module     - Staff UI Module      - Management Dashboard UI        |
+-----------------------------------------------------------------------------------+
                              |
                              | Internal API Calls
                              v
+-----------------------------------------------------------------------------------+
|                               APPLICATION / SERVICE LAYER                         |
|   +-------------------+  +-------------------+  +------------------------------+  |
|   | Student Service   |  | Staff Service     |  | Management & Admin Service   |  |
|   +-------------------+  +-------------------+  +------------------------------+  |
|   | Notification Svc  |  | RBAC & Auth Svc   |  | Ticket Lifecycle Engine      |  |
|   +-------------------+  +-------------------+  +------------------------------+  |
+-----------------------------------------------------------------------------------+
                              |
                              | ORM / Data Access Layer
                              v
+-----------------------------------------------------------------------------------+
|                                  DATA LAYER                                       |
|   +---------------------------------------+  +---------------------------------+  |
|   | Relational DB (PostgreSQL / MySQL)    |  | Local File Storage / Storage    |  |
|   | (Ticket, Users, Audit Log, Metrics)   |  | (Attachments: PDF, PNG, JPG)    |  |
|   +---------------------------------------+  +---------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Kiến trúc Frontend (Presentation Layer)

### 2.1 Công nghệ & Đặc điểm
* **Kiến trúc:** Single Page Application (SPA) hoặc Server-Side Rendering (SSR) tùy chọn tối ưu UI.
* **Giao diện:** Responsive Design (tương thích máy tính để bàn và thiết bị di động).
* **Đa ngôn ngữ:** Hỗ trợ Tiếng Việt (Default) và Tiếng Anh ở mức cơ bản.

### 2.2 Phân chia Phân hệ UI
1. **Student Portal (Phân hệ Sinh viên - M1):**
   * Tra cứu hướng dẫn & FAQ.
   * Form gửi Ticket đơn giản, hỗ trợ upload đính kèm (Image/PDF).
   * Màn hình tra cứu tiến độ chi tiết và khung bổ sung hồ sơ.
   * Giao diện đánh giá độ hài lòng (Rating CSAT & Feedback) sau khi hoàn thành.
2. **Staff Operations (Phân hệ Nhân viên - M2):**
   * Hòm thư Ticket theo phân loại và phòng ban.
   * Tool điều phối, tiếp nhận (Claim), chuyển phòng ban, cập nhật trạng thái và yêu cầu bổ sung thông tin.
3. **Management Dashboard (Phân hệ Quản trị & Báo cáo - M3):**
   * Báo cáo thống kê trực quan (Biểu đồ số lượng Ticket, tỷ lệ quá hạn, thời gian xử lý trung bình).
   * Giao diện quản trị tài khoản, phân quyền vai trò (RBAC) và kiểm tra Audit Log.

---

## 3. Kiến trúc Backend (Application Service Layer)

Backend của UniSupport được phân rã theo 3 phân hệ nghiệp vụ cốt lõi (17 Functions) và 2 dịch vụ kỹ thuật phụ trợ:

### 3.1 Phân hệ M01 - Student Portal Module (M1: 128h kế hoạch)
* Xử lý tra cứu FAQ/Knowledge base.
* Tạo mới Ticket, tự động sinh Mã Ticket duy nhất (theo quy tắc ADR-001).
* Quản lý thông tin hồ sơ Ticket của sinh viên.
* Cho phép đính kèm tệp và cập nhật thông tin bổ sung khi Nhân viên yêu cầu.

### 3.2 Phân hệ M02 - Staff Operations Module (M2: 197h kế hoạch)
* Cung cấp logic tiếp nhận (Claim), phân loại (Triage) và thiết lập độ ưu tiên & thời hạn SLA.
* Xử lý luồng chuyển giao phòng ban (Transfer Department) và yêu cầu bổ sung hồ sơ (tạm dừng SLA).
* Quản lý việc cập nhật trạng thái xử lý và ghi nhận kết quả cuối cùng.

### 3.3 Phân hệ M03 - Management Dashboard Module (M3: 215h kế hoạch)
* Tính toán các chỉ số đo lường hiệu năng xử lý (SLA, thời gian giải quyết trung bình).
* Tổng hợp dữ liệu thống kê theo nhóm vấn đề và báo cáo đánh giá CSAT.
* Cung cấp các API quản trị tài khoản người dùng, sơ đồ phòng ban và chính sách lưu trữ.

### 3.4 Dịch vụ kỹ thuật phụ trợ: Notification Service (M04)
* Quản lý và phát thông báo nội bộ hệ thống (In-app Notifications) cho Sinh viên và Nhân viên khi Ticket có sự thay đổi trạng thái hoặc nhận phản hồi mới (hiện thực hóa FR-STU-04).

### 3.5 Dịch vụ kỹ thuật phụ trợ: RBAC & Security Module (M05)
* Quản lý xác thực JWT / Session Token.
* Kiểm soát quyền truy cập theo vai trò (Role-Based Access Control).
* Kiểm soát an toàn tệp đính kèm: Chỉ cho phép tài khoản liên quan (Sinh viên sở hữu Ticket, Nhân viên phòng ban xử lý, Quản lý) được tải hoặc xem file.
* Ghi chép nhật ký thao tác quan trọng (Audit Logging bất biến).

---

## 4. Kiến trúc Lưu trữ & Dữ liệu (Data Layer)

### 4.1 Cơ sở dữ liệu quan hệ (Relational Database)
* Sử dụng RDBMS (PostgreSQL/MySQL) để đảm bảo tính toàn vẹn dữ liệu (ACID).
* Quản lý các thông tin: Người dùng, Phòng ban, Ticket, Lịch sử chuyển trạng thái, Đánh giá hài lòng, Audit Log.

### 4.2 Lưu trữ Tệp đính kèm (Attachment Storage)
* Tệp đính kèm (PDF, PNG, JPG) được lưu trữ tại cấu trúc thư mục bảo mật trên Server.
* Tên file được mã hóa/đổi tên ngẫu nhiên (UUID) để tránh dò quét trực tiếp.
* Không công khai URL trực tiếp (Public Storage); mọi yêu cầu xem/tải file phải đi qua API kiểm tra quyền ở Phân hệ M05.

---

## 5. Tương tác Kỹ thuật & Bảo mật cơ bản

1. **Giao tiếp API:** Tất cả truy xuất dữ liệu giữa Frontend và Backend sử dụng giao thức HTTPS với dữ liệu định dạng JSON.
2. **Bảo vệ thao tác trùng lặp:** Áp dụng cơ chế kiểm tra Request Token / Idempotency tại Backend để tránh tình trạng trùng lặp Ticket khi người dùng click liên tục hoặc gặp lỗi mạng (Retry).
3. **Mã hóa mật khẩu:** Mật khẩu người dùng được mã hóa bằng thuật toán hashing an toàn (như Bcrypt/Argon2) trước khi lưu trữ.


---

## Tài liệu nguồn: 07-architecture/data-model.md

# [ARC-03] Mô hình Dữ liệu & Cơ sở Dữ liệu (Data Model & Schema)

Tài liệu này mô tả chi tiết mô hình dữ liệu quan hệ (Relational Database Schema) cho hệ thống **UniSupport**, bao gồm sơ đồ ERD, định nghĩa các bảng (Tables), quan hệ giữa các thực thể và chiến lược đánh chỉ mục (Indexing).

---

## 1. Sơ đồ Quan hệ Thực thể (Entity Relationship Diagram - ERD)

```text
+-------------------+       1:N       +-------------------+       1:N       +-------------------+
|    departments    |----------------<|       users       |----------------<|      tickets      |
+-------------------+                 +-------------------+                 +-------------------+
| id (PK)           |                 | id (PK)           |                 | id (PK)           |
| code              |                 | department_id(FK) |                 | ticket_code (UQ)  |
| name              |                 | email (UQ)        |                 | student_id (FK)   |
| description       |                 | password_hash     |                 | department_id(FK) |
| created_at        |                 | full_name         |                 | assigned_staff(FK)|
+-------------------+                 | role (ENUM)       |                 | category_id (FK)  |
                                      | status            |                 | priority (ENUM)   |
                                      +-------------------+                 | status (ENUM)     |
                                                |                           | title             |
                                                | 1:N                       | description       |
                                                |                           | created_at        |
                                                v                           +-------------------+
                                      +-------------------+                   |     |     |
                                      |    audit_logs     |                   |     |     |
                                      +-------------------+                   |     |     |
                                      | id (PK)           |                   |     |     |
                                      | user_id (FK)      |                   |     |     |
                                      | action            |                   |     |     |
                                      | details (JSONB)   |                   |     |     |
                                      | created_at        |                   |     |     |
                                      +-------------------+                   |     |     |
                                                                              |     |     |
           +------------------------------------------------------------------+     |     +-----------------------------------+
           | 1:N                                                                    | 1:N                                     | 1:1
           v                                                                        v                                         v
+-------------------+                                                     +-------------------+                     +-------------------+
|ticket_attachments |                                                     |ticket_histories   |                     |  ticket_ratings   |
+-------------------+                                                     +-------------------+                     +-------------------+
| id (PK)           |                                                     | id (PK)           |                     | id (PK)           |
| ticket_id (FK)    |                                                     | ticket_id (FK)    |                     | ticket_id (FK, UQ)|
| file_name         |                                                     | actor_id (FK)     |                     | student_id (FK)   |
| file_path         |                                                     | action_type       |                     | rating_score      |
| file_type         |                                                     | old_status        |                     | comment           |
| file_size         |                                                     | new_status        |                     | created_at        |
| created_at        |                                                     | note              |                     +-------------------+
+-------------------+                                                     | created_at        |
                                                                          +-------------------+
```

---

## 2. Chi tiết Cấu trúc các Bảng (Table Schemas)

### 2.1 Bảng `departments` (Phòng ban)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key, Auto-increment | Mã định danh phòng ban |
| **code** | VARCHAR(20) | Unique, Not Null | Mã ngắn phòng ban (VD: DT, CTSV, HC) |
| **name** | VARCHAR(100) | Not Null | Tên phòng ban |
| **description** | TEXT | Nullable | Mô tả chức năng nhiệm vụ |
| **created_at** | TIMESTAMP | Default NOW() | Thời gian tạo |

---

### 2.2 Bảng `users` (Người dùng)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key, Auto-increment | Mã người dùng |
| **department_id** | UUID / BIGINT | Foreign Key (`departments.id`), Nullable | Phòng ban công tác (Null đối với Sinh viên) |
| **email** | VARCHAR(100) | Unique, Not Null | Email cá nhân/trường |
| **password_hash** | VARCHAR(255) | Not Null | Mật khẩu mã hóa (Bcrypt) |
| **full_name** | VARCHAR(100) | Not Null | Họ và tên |
| **role** | ENUM | Not Null | Vai trò: `'STUDENT'`, `'STAFF'`, `'MANAGEMENT'` |
| **status** | VARCHAR(20) | Default `'ACTIVE'` | Trạng thái tài khoản (ACTIVE, INACTIVE) |
| **created_at** | TIMESTAMP | Default NOW() | Thời gian khởi tạo |

---

### 2.3 Bảng `tickets` (Phiếu hỗ trợ)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key, Auto-increment | ID kỹ thuật |
| **ticket_code** | VARCHAR(30) | Unique, Not Null | Mã Ticket hiển thị (VD: TK-20261005-001) |
| **student_id** | UUID / BIGINT | Foreign Key (`users.id`), Not Null | Người tạo Ticket |
| **department_id** | UUID / BIGINT | Foreign Key (`departments.id`), Nullable | Phòng ban tiếp nhận xử lý |
| **assigned_staff_id**| UUID / BIGINT | Foreign Key (`users.id`), Nullable | Nhân viên trực tiếp phụ trách |
| **priority** | ENUM | Default `'MEDIUM'` | Mức độ ưu tiên: `'LOW'`, `'MEDIUM'`, `'HIGH'`, `'URGENT'` |
| **status** | ENUM | Default `'NEW'` | Trạng thái: `'NEW'`, `'IN_PROGRESS'`, `'WAITING_STUDENT'`, `'RESOLVED'`, `'CLOSED'` |
| **title** | VARCHAR(255) | Not Null | Tiêu đề yêu cầu |
| **description** | TEXT | Not Null | Nội dung chi tiết |
| **created_at** | TIMESTAMP | Default NOW() | Thời điểm gửi Ticket |
| **updated_at** | TIMESTAMP | Default NOW() | Thời điểm cập nhật cuối |

---

### 2.4 Bảng `ticket_attachments` (Tệp đính kèm)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key | ID tệp đính kèm |
| **ticket_id** | UUID / BIGINT | Foreign Key (`tickets.id`), Not Null | Tệp thuộc Ticket nào |
| **file_name** | VARCHAR(255) | Not Null | Tên file gốc người dùng tải lên |
| **file_path** | VARCHAR(255) | Not Null | Đường dẫn lưu trữ hệ thống (UUID-renamed) |
| **file_type** | VARCHAR(50) | Not Null | Định dạng MIME (image/png, application/pdf) |
| **file_size** | INTEGER | Not Null | Dung lượng file tính bằng Bytes |
| **created_at** | TIMESTAMP | Default NOW() | Thời gian tải lên |

---

### 2.5 Bảng `ticket_histories` (Lịch sử xử lý Ticket)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key | ID nhật ký |
| **ticket_id** | UUID / BIGINT | Foreign Key (`tickets.id`), Not Null | Ticket liên quan |
| **actor_id** | UUID / BIGINT | Foreign Key (`users.id`), Not Null | Người thực hiện thao tác |
| **action_type** | VARCHAR(50) | Not Null | Loại thao tác (CREATE, ASSIGN, TRANSFER, RESOLVE...) |
| **old_status** | VARCHAR(20) | Nullable | Trạng thái trước thao tác |
| **new_status** | VARCHAR(20) | Nullable | Trạng thái sau thao tác |
| **note** | TEXT | Nullable | Ghi chú/Nội dung phản hồi |
| **created_at** | TIMESTAMP | Default NOW() | Thời điểm thực hiện |

---

### 2.6 Bảng `ticket_ratings` (Đánh giá mức độ hài lòng)

| Tên trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| **id** | UUID / BIGINT | Primary Key | ID đánh giá |
| **ticket_id** | UUID / BIGINT | Foreign Key (`tickets.id`), Unique, Not Null | Ticket được đánh giá (1:1) |
| **student_id** | UUID / BIGINT | Foreign Key (`users.id`), Not Null | Sinh viên đánh giá |
| **rating_score** | SMALLINT | Not Null, Check (1 <= rating_score <= 5) | Điểm số đánh giá (1 đến 5 sao) |
| **comment** | TEXT | Nullable | Ý kiến đóng góp |
| **created_at** | TIMESTAMP | Default NOW() | Thời điểm gửi đánh giá |

---

## 3. Chỉ mục (Indexes) & Tối ưu hóa truy vấn

Nhằm đảm bảo tốc độ truy xuất mượt mà trên quy mô 3.000 sinh viên, hệ thống thiết lập các Index cơ bản:

- **`idx_tickets_student_id`**: Tối ưu danh sách Ticket cá nhân của Sinh viên (`tickets.student_id`).
- **`idx_tickets_department_status`**: Tối ưu lọc Ticket theo phòng ban & trạng thái cho Nhân viên (`tickets.department_id`, `tickets.status`).
- **`idx_tickets_code`**: Truy vấn nhanh bằng Mã Ticket (`tickets.ticket_code`).
- **`idx_histories_ticket_id`**: Lấy mượt mà tiến độ/lịch sử thay đổi (`ticket_histories.ticket_id`).


---

## Tài liệu nguồn: 07-architecture/security-design.md

# [ARC-05] Thiết kế Bảo mật & Phân quyền (Security & RBAC Design)

Tài liệu này chi tiết hóa kiến trúc bảo mật của hệ thống **UniSupport**, mô hình phân quyền dựa trên vai trò (Role-Based Access Control - RBAC), cơ chế mã hóa và phương án bảo vệ tài nguyên tệp đính kèm.

---

## 1. Cơ chế Xác thực & Quản lý Phiên (Authentication & Session)

1. **Phương thức xác thực:**
   * Hệ thống áp dụng cơ chế xác thực **JSON Web Token (JWT)** Stateless hoặc **Session Token**.
   * Khi đăng nhập thành công qua `/api/v1/auth/login`, Backend trả về `AccessToken` kèm thời gian hết hạn (Expiration Time).
2. **Quản lý Token:**
   * Token được gửi kèm trong HTTP Header của mỗi request dưới dạng: `Authorization: Bearer <JWT_TOKEN>`.
   * Mật khẩu lưu trữ trong Cơ sở dữ liệu bắt buộc phải mã hóa bằng thuật toán băm an toàn **Bcrypt** (với Salt Factor >= 10).

---

## 2. Ma trận Phân quyền Vai trò (RBAC Matrix)

Hệ thống UniSupport định nghĩa **3 Vai trò chính (Roles)** với phạm vi quyền thao tác rõ ràng:

| Phân hệ / Chức năng | Sinh viên (`STUDENT`) | Nhân viên (`STAFF`) | Quản lý (`MANAGEMENT`) |
| :--- | :---: | :---: | :---: |
| **Đăng nhập hệ thống** | ✅ | ✅ | ✅ |
| **Gửi Ticket & Up file** | ✅ (Chỉ của mình) | ❌ | ❌ |
| **Xem danh sách Ticket** | ✅ (Chỉ của mình) | ✅ (Thuộc Phòng ban) | ✅ (Toàn trường) |
| **Tiếp nhận / Phân loại** | ❌ | ✅ | ✅ |
| **Chuyển phòng ban** | ❌ | ✅ | ✅ |
| **Yêu cầu bổ sung hồ sơ** | ❌ | ✅ | ❌ |
| **Cập nhật kết quả / Đóng** | ❌ | ✅ | ❌ |
| **Đánh giá hài lòng** | ✅ (Ticket của mình) | ❌ | ❌ |
| **Xem Dashboard Báo cáo** | ❌ | ❌ | ✅ |
| **Quản trị Tài khoản/Quyền** | ❌ | ❌ | ✅ |

---

## 3. Bảo mật Tệp đính kèm (File Attachment Security)

Tệp đính kèm (Ảnh/PDF) do sinh viên gửi chứa các thông tin cá nhân và giấy tờ quan trọng. Hệ thống thực hiện phương án bảo mật 3 lớp:

1. **Lưu trữ An toàn (Static Storage Isolation):**
   * Tệp đính kèm không lưu trong thư mục Web công khai (`public/`).
   * Tên tệp được mã hóa ngẫu nhiên bằng **UUIDv4** khi ghi vào đĩa để tránh dò tìm tệp (Directory Traversal attack).
2. **Kiểm tra Quyền xem tệp (Access Control Middleware):**
   * Mọi yêu cầu xem/tải tệp đính kèm phải thông qua API Proxy: `GET /api/v1/attachments/{file_id}`.
   * Middleware sẽ verify JWT Token và kiểm tra người dùng có quyền truy cập:
     * **Sinh viên:** Chỉ xem được tệp thuộc Ticket do chính mình tạo.
     * **Nhân viên:** Chỉ xem được tệp thuộc Ticket gán cho phòng ban của mình.
     * **Quản lý:** Có quyền xem tra soát toàn bộ.
3. **Validate Định dạng & Dung lượng (Input Sanitization):**
   * Chỉ chấp nhận các định dạng MIME allowed: `image/png`, `image/jpeg`, `application/pdf`.
   * Chặn hoàn toàn các file thực thi (`.exe`, `.php`, `.js`, `.sh`...).
   * Giới hạn dung lượng tối đa 10MB/file.

---

## 4. Nhật ký Tra soát (Audit Logging)

Để phục vụ công tác tra soát khi có khiếu nại hoặc sự cố bảo mật, hệ thống ghi chép **Audit Log** cơ bản đối với các thao tác quan trọng vào bảng `audit_logs`:
* **Các sự kiện được Log:** Đăng nhập thất bại/thành công, Chuyển tiếp phòng ban, Xóa/Khóa tài khoản, Thay đổi quyền hạn.
* **Thông tin ghi nhận:** `User_ID`, `IP_Address`, `Action_Type`, `Timestamp`, `Old_Value`, `New_Value`.


---

## Tài liệu nguồn: 07-architecture/system-context.md

# [ARC-01] Sơ đồ ngữ cảnh hệ thống UniSupport (System Context)

Tài liệu này mô tả sơ đồ ngữ cảnh (System Context Diagram - C4 Model Level 1) của hệ thống **UniSupport**, xác định ranh giới giữa hệ thống Web Application UniSupport với các đối tượng người dùng (Actors) và môi trường hạ tầng của **Aurora University**.

---

## 1. Tổng quan phạm vi hệ thống (System Scope)

UniSupport là hệ thống **Web Application** đóng vai trò là đầu mối tập trung toàn bộ quy trình tiếp nhận, phân loại, xử lý, theo dõi và đánh giá chất lượng yêu cầu hỗ trợ sinh viên tại Aurora University.

* **Phạm vi phục vụ:** Khối lượng người dùng khoảng **3.000 sinh viên** cùng đội ngũ Nhân viên hỗ trợ và Quản lý các phòng ban.
* **Loại ứng dụng:** Web Application (Responsive Web hỗ trợ trình duyệt Máy tính và Thiết bị di động).
* **Ranh giới tích hợp:** Độc lập, không kết nối/tích hợp với các hệ thống bên thứ ba ngoài phạm vi đã thỏa thuận.

---

## 2. Các Tác nhân tương tác (Actors)

### 2.1 Sinh viên (Student)
* **Mô tả:** Người dùng gửi các yêu cầu cần giải đáp hoặc hỗ trợ hành chính/đào tạo/mạng/cơ sở vật chất.
* **Tương tác:**
  * Đăng nhập tài khoản cá nhân.
  * Tạo phiếu hỗ trợ (Ticket), đính kèm minh chứng (ảnh/PDF).
  * Theo dõi tiến độ xử lý và lịch sử cập nhật.
  * Bổ sung thông tin/giấy tờ theo yêu cầu của nhân viên.
  * Nhận kết quả và thực hiện đánh giá mức độ hài lòng (1-5 sao).

### 2.2 Nhân viên hỗ trợ (Staff)
* **Mô tả:** Nhân viên các phòng ban nghiệp vụ thuộc Aurora University chịu trách nhiệm giải quyết yêu cầu của sinh viên.
* **Tương tác:**
  * Đăng nhập hệ thống theo phòng ban.
  * Tiếp nhận, phân loại nhóm vấn đề và gán mức độ ưu tiên cho Ticket.
  * Chuyển tiếp Ticket sang phòng ban khác nếu sai thẩm quyền.
  * Yêu cầu sinh viên bổ sung giấy tờ/thông tin.
  * Cập nhật tiến độ, ghi nhận kết quả giải quyết và đóng Ticket.

### 2.3 Quản lý / Quản trị viên (Management & Admin)
* **Mô tả:** Ban quản lý đơn vị/trường và Quản trị viên hệ thống.
* **Tương tác:**
  * Xem Dashboard báo cáo tổng quan về khối lượng công việc, tỷ lệ Ticket đúng/quá hạn SLA.
  * Phân tích xu hướng các nhóm vấn đề sinh viên thường gặp.
  * Quản trị tài khoản, phân quyền vai trò (Student, Staff, Management) và quản lý danh mục phòng ban.
  * Tra soát nhật ký hoạt động (Audit log) cơ bản của hệ thống.

---

## 3. Sơ đồ ngữ cảnh C4 (System Context Diagram)

```
                    +-----------------------------------+
                    |        Aurora University          |
                    +-----------------------------------+
                                      |
      +-------------------------------+-------------------------------+
      |                               |                               |
      v                               v                               v
+------------------+           +-------------------+           +-------------------+
|  Sinh viên       |           |  Nhân viên        |           |  Quản lý / Admin  |
|  (Student)       |           |  (Staff)          |           |  (Management)     |
+------------------+           +-------------------+           +-------------------+
        |                               |                               |
        | HTTP / HTTPS                  | HTTP / HTTPS                  | HTTP / HTTPS
        | (Web Browser PC/Mobile)       | (Web Browser PC/Mobile)       | (Web Browser PC)
        v                               v                               v
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                              HỆ THỐNG UNISUPPORT                                  |
|                            (Web Application Platform)                             |
|                                                                                   |
|  - Student Portal: Tạo ticket, theo dõi tiến độ, bổ sung hồ sơ, đánh giá         |
|  - Staff Operations: Phân loại, điều phối, xử lý, cập nhật trạng thái             |
|  - Management Dashboard: Báo cáo thống kê, xu hướng, quản trị tài khoản           |
|  - Notification Service: Thông báo cập nhật trạng thái nội bộ                     |
|  - Security & Storage: Phân quyền RBAC, lưu trữ file đính kèm (PDF/Image)          |
|                                                                                   |
+-----------------------------------------------------------------------------------+
                                      |
                                      | Lưu trữ dữ liệu & File
                                      v
                    +-----------------------------------+
                    | Hạ tầng Server & Storage          |
                    | (Do Aurora University cung cấp)   |
                    +-----------------------------------+
```

---

## 4. Các Giả định & Ràng buộc ngữ cảnh (Contextual Assumptions & Constraints)

* **Hạ tầng triển khai:** Hệ thống được vận hành hoàn toàn trên hạ tầng Server và tên miền nội bộ/Cloud do Aurora University cấp.
* **Không kết nối SSO/Third-party:** Xác thực được thực hiện trực tiếp thông qua Cơ sở dữ liệu của UniSupport (không tích hợp LDAP/OAuth ngoài phạm vi).
* **Truy cập tệp đính kèm:** Tệp đính kèm (Ảnh/PDF) được lưu trữ trên Server local/cloud và được kiểm soát quyền truy cập trực tiếp bởi phân hệ `M05-rbac-security`.


---

## Tài liệu nguồn: 07-architecture/technical-decisions/ADR-001-ticket-id-generation.md

# [ADR-001] Quy tắc sinh mã Ticket duy nhất (Ticket ID Generation Strategy)

* **Trạng thái:** Đã phê duyệt (Accepted)
* **Ngày quyết định:** 2026-10-05
* **Người quyết định:** Tech Lead / System Architect
* **Phân hệ liên quan:** `02-domain`, `M01-student-portal`, `M02-staff-operations`

---

## 1. Bối cảnh (Context)
Hệ thống UniSupport yêu cầu mỗi phiếu hỗ trợ (Ticket) phải có một định danh duy nhất để sinh viên dễ dàng tra cứu, nhân viên tiện trao đổi và hệ thống dễ truy vấn.
- Mã định danh trong CSDL sử dụng khóa chính dạng tự tăng (Auto-increment ID) hoặc UUID để tối ưu index.
- Tuy nhiên, giao diện người dùng cần một mã Ticket ngắn gọn, dễ đọc, dễ giao tiếp qua điện thoại/email nhưng vẫn đảm bảo tính duy nhất và không thể đoán trước quá dễ dàng.

## 2. Các phương án xem xét (Options Considered)
1. **Phương án 1: Dùng ID tự tăng của CSDL (Ví dụ: `1`, `2`, `1024`)**
   - *Ưu điểm:* Đơn giản, ngắn gọn.
   - *Nhược điểm:* Dễ lộ thông tin kinh doanh (số lượng Ticket của nhà trường), lộ quy luật số đếm.
2. **Phương án 2: Dùng UUID v4 (Ví dụ: `c9bf9e57-1685-4c89-bafb-ff5af830be8a`)**
   - *Ưu điểm:* Đảm bảo tính duy nhất tuyệt đối.
   - *Nhược điểm:* Quá dài, khó nhớ, không thân thiện khi đọc hoặc tìm kiếm nhanh.
3. **Phương án 3: Sinh mã định dạng Prefix + Timestamp/Random + Sequence (Ví dụ: `TK-202610-A89F`)**
   - *Ưu điểm:* Thân thiện, dễ phân biệt theo thời gian, độ dài vừa phải, chuyên nghiệp.
   - *Nhược điểm:* Cần xử lý logic sinh mã trùng lặp ở tầng ứng dụng hoặc DB constraint.

## 3. Quyết định (Decision)
Lựa chọn **Phương án 3**. Cấu trúc mã Ticket hiển thị cho người dùng sẽ bao gồm:
$$\text{Ticket Code} = \text{TK} + \text{[YYYYMM]} + \text{[4 Ký tự ngẫu nhiên AlphaNumeric/Sequence]}$$
*(Ví dụ: `TK-202610-8F3A`)*

- Khóa chính CSDL (Primary Key) vẫn lưu bằng `UUID` hoặc `BigInt` để đảm bảo hiệu năng liên kết bảng.
- Trường `ticket_code` lưu chuỗi trên, được gắn chỉ mục `UNIQUE INDEX` trong CSDL.

## 4. Hệ quả (Consequences)
* **Tích cực:** Mã Ticket thân thiện với người dùng, hỗ trợ nhận diện thời gian tạo, chuyên nghiệp và an toàn.
* **Tiêu cực:** Cần thêm bước validate hoặc hàm sinh mã bảo đảm không trùng lặp (retry mechanism nếu va chạm chuỗi ngẫu nhiên).


---

## Tài liệu nguồn: 07-architecture/technical-decisions/ADR-002-role-based-access-control.md

# [ADR-002] Giải pháp phân quyền 3 vai trò (RBAC Strategy)

* **Trạng thái:** Đã phê duyệt (Accepted)
* **Ngày quyết định:** 2026-10-05
* **Người quyết định:** Security Architect / Tech Lead
* **Phân hệ liên quan:** `M05-rbac-security`, `05-non-functional-requirements/security.md`

---

## 1. Bối cảnh (Context)
UniSupport phục vụ 3 nhóm đối tượng chính tại Aurora University với thẩm quyền khác nhau:
1. **Sinh viên (Student):** Chỉ truy cập và tương tác với các Ticket của chính mình.
2. **Nhân viên (Staff):** Truy cập, phân loại, chuyển tiếp và xử lý Ticket thuộc phòng ban được gán.
3. **Quản lý (Manager):** Xem báo cáo tổng quan, quản lý danh mục và tài khoản hệ thống.

Cần một mô hình phân quyền vừa đảm bảo an toàn dữ liệu, vừa linh hoạt, đơn giản để triển khai trong quy mô dự án 14 tuần.

## 2. Các phương án xem xét (Options Considered)
1. **Phương án 1: Hardcode phân quyền trực tiếp trong code theo Role Name (Simple RBAC)**
   - *Ưu điểm:* Phát triển nhanh, logic đơn giản.
   - *Nhược điểm:* Cứng nhắc, khó mở rộng nếu sau này nhà trường chia thêm vai trò nhỏ (VD: Trưởng phòng vs Nhân viên).
2. **Phương án 2: Mô hình RBAC dựa trên Quyền (Permission-based / ABAC)**
   - *Ưu điểm:* Rất linh hoạt, phân quyền tới từng nút bấm/API.
   - *Nhược điểm:* Phức tạp, tốn thời gian thiết kế cơ sở dữ liệu và middleware kiểm tra quyền.

## 3. Quyết định (Decision)
Lựa chọn **Phương án 1 kết hợp Scoping theo Context**:
- Định nghĩa 3 Role cố định: `ROLE_STUDENT`, `ROLE_STAFF`, `ROLE_MANAGER`.
- **JWT (JSON Web Token)** chứa thông tin `user_id`, `role`, và `department_id` (đối với Staff).
- Sử dụng **Middleware / Interceptor** tại Backend API để kiểm tra:
  - **Role Level:** Quyền truy cập API (VD: API xem Dashboard chỉ cho `ROLE_MANAGER`).
  - **Data Level (Data Scoping):**
    - `ROLE_STUDENT`: Query ép điều kiện `WHERE student_id = current_user_id`.
    - `ROLE_STAFF`: Query ép điều kiện `WHERE department_id = current_staff_department_id`.

## 4. Hệ quả (Consequences)
* **Tích cực:** Tối ưu thời gian phát triển, đáp ứng hoàn hảo phạm vi dự án, bảo mật dữ liệu ở cả 2 cấp độ (Route & Data).
* **Tiêu cực:** Nếu nhà trường muốn tùy chỉnh phân quyền chi tiết cho từng cá nhân trong tương lai sẽ cần nâng cấp mô hình DB.


---

## Tài liệu nguồn: 07-architecture/technical-decisions/ADR-003-file-attachment-storage.md

# [ADR-003] Phương án lưu trữ & Phân quyền xem file đính kèm (File Attachment Storage Strategy)

* **Trạng thái:** Đã phê duyệt (Accepted)
* **Ngày quyết định:** 2026-10-05
* **Người quyết định:** Infrastructure Lead / Backend Lead
* **Phân hệ liên quan:** `M01-student-portal`, `M02-staff-operations`, `05-non-functional-requirements/security.md`

---

## 1. Bối cảnh (Context)
Sinh viên và Nhân viên có nhu cầu tải lên tệp đính kèm (định dạng PDF, PNG, JPG) chứa giấy tờ cá nhân hoặc kết quả xử lý.
- Giả định hệ thống triển khai trên hạ tầng máy chủ của Client (Aurora University).
- Tệp đính kèm chứa thông tin nhạy cảm của sinh viên, **tuyệt đối không được công khai (Public URL)** để tránh truy cập trái phép.

## 2. Các phương án xem xét (Options Considered)
1. **Phương án 1: Lưu file vào thư mục `public/` của Web Server**
   - *Ưu điểm:* Dễ triển khai, trả về URL tĩnh cho Frontend dùng ngay.
   - *Nhược điểm:* Mất an toàn thông tin, ai có link cũng tải được file (Lỗ hổng Direct Access).
2. **Phương án 2: Lưu tệp trong Local Storage/NAS của Server + Truy xuất qua Proxy Stream API**
   - *Ưu điểm:* Chi phí hạ tầng $0$ (dùng trực tiếp ổ cứng máy chủ), kiểm soát phân quyền 100% qua API Backend.
   - *Nhược điểm:* Tốn băng thông Backend khi phải stream file.
3. **Phương án 3: Dùng Object Storage (S3 / MinIO) + Presigned URL**
   - *Ưu điểm:* Hiệu năng cao, bảo mật tốt, chuẩn enterprise.
   - *Nhược điểm:* Yêu cầu Client phải trang bị thêm hạ tầng S3 hoặc cài đặt MinIO, vượt ngoài giả định hạ tầng cơ bản.

## 3. Quyết định (Decision)
Lựa chọn **Phương án 2**:
- Tệp đính kèm được lưu trong thư mục riêng biệt của Server (nằm ngoài thư mục Web Public).
- Tên tệp trên đĩa được đổi thành chuỗi ngẫu nhiên (UUID) để tránh trùng tên và dò đoán file.
- **Cơ chế truy cập:**
  1. Client gọi API `GET /api/v1/attachments/{file_id}`.
  2. Backend kiểm tra quyền (User có phải chủ Ticket hoặc Nhân viên phòng ban xử lý hay không).
  3. Nếu hợp lệ, Backend đọc file và stream trực tiếp về Client (hoặc trả về chuỗi Base64 / File Blob).
  4. Nếu không có quyền, trả về lỗi `403 Forbidden`.

## 4. Hệ quả (Consequences)
* **Tích cực:** Đảm bảo an toàn tuyệt đối cho hồ sơ sinh viên, tuân thủ tiêu chí NFR-SEC-01, tương thích tốt với hạ tầng VPS/Server của nhà trường.
* **Tiêu cực:** Tăng nhẹ tải CPU/RAM của Backend Service khi đọc/ghi file.


---

## Tài liệu nguồn: 07-architecture/technical-decisions/README.md

# 07-architecture/technical-decisions: Quyết định Kiến trúc Kỹ thuật (ADR)

Thư mục này lưu trữ các **Bản ghi Quyết định Kiến trúc (Architecture Decision Records - ADR)** cho hệ thống UniSupport. Mỗi ADR ghi lại một quyết định kỹ thuật quan trọng, bối cảnh lựa chọn, các phương án cân nhắc và hệ quả đi kèm.

---

## Danh sách các Báo cáo ADR

| Mã ADR | Tiêu đề Quyết định | Trạng thái | Tóm tắt Giải pháp |
| :--- | :--- | :--- | :--- |
| **[ADR-001](07-architecture/technical-decisions/ADR-001-ticket-id-generation.md)** | Quy tắc sinh mã Ticket duy nhất | Accepted | Sinh mã hiển thị ngắn gọn `TK-YYYYMM-XXXX` cho người dùng; dùng UUID/BigInt cho Primary Key CSDL. |
| **[ADR-002](07-architecture/technical-decisions/ADR-002-role-based-access-control.md)** | Giải pháp phân quyền 3 vai trò (RBAC) | Accepted | Sử dụng RBAC dựa trên JWT với 3 Role chính kết hợp lọc dữ liệu ở cấp độ context (`student_id`, `department_id`). |
| **[ADR-003](07-architecture/technical-decisions/ADR-003-file-attachment-storage.md)** | Phương án lưu trữ & Phân quyền xem file | Accepted | Lưu tệp trong thư mục bảo mật trên máy chủ local, đổi tên file dạng UUID và kiểm soát truy cập qua API Stream Proxy (trả về 403 nếu sai quyền). |

---

## Quy chuẩn Cấu trúc một Báo cáo ADR
Mỗi file ADR tuân thủ thống nhất 4 phần chính:
1. **Bối cảnh (Context):** Vấn đề kỹ thuật hoặc nghiệp vụ cần giải quyết.
2. **Các phương án xem xét (Options Considered):** So sánh ưu/nhược điểm của từng lựa chọn.
3. **Quyết định (Decision):** Giải pháp được thống nhất lựa chọn.
4. **Hệ quả (Consequences):** Các tác động tích cực và hạn chế cần lưu ý khi triển khai.


---

## Tài liệu nguồn: 08-project/assumptions.md

# [PRJ-01] Các Giả định Dự án (Project Assumptions)

Tài liệu này xác định các giả định nền tảng về phạm vi, kỹ thuật, hạ tầng và vận hành đối với dự án **UniSupport** tại **Aurora University**. Các giả định này làm căn cứ để ước tính chi phí, phân bổ nguồn lực (618h cơ sở + 22h dự phòng = 640h kế hoạch), lập kế hoạch tiến độ 14 tuần và xác định tiêu chí nghiệm thu.

---

## 1. Giả định về Quy mô & Phạm vi Sử dụng (Scope & Scale)

* **Quy mô người dùng:** Hệ thống được thiết kế và tối ưu cho quy mô khoảng **3.000 sinh viên** cùng đội ngũ Nhân viên hỗ trợ và Quản lý các phòng ban.
* **Không tối ưu tải lớn:** Hệ thống không thiết kế cho kiến trúc chịu tải cực lớn (High Concurrency / Auto-scaling) hoặc tính năng giật ca/đăng ký tín chỉ đồng thời hàng loạt.
* **Loại ứng dụng:** Hệ thống là **Web Application** chạy trên trình duyệt web (hỗ trợ Responsive cho Máy tính và Thiết bị di động). Không phát triển Mobile App độc lập (iOS/Android).
* **Đa ngôn ngữ:** Giao diện người dùng hỗ trợ **Tiếng Việt** (mặc định) và **Tiếng Anh** ở mức cơ bản.

---

## 2. Giả định về Kỹ thuật & Tích hợp (Technical & Integration)

* **Không tích hợp hệ thống bên thứ ba:** Hệ thống vận hành độc lập, không yêu cầu tích hợp với các hệ thống bên thứ ba ngoài phạm vi đã thỏa thuận (như SSO/LDAP, LMS Canvas/Moodle, Core ERP hay Cổng thanh toán).
* **Xác thực người dùng:** Hệ thống tự quản lý tài khoản, mật khẩu và xác thực người dùng trực tiếp qua Cơ sở dữ liệu nội bộ của UniSupport.
* **Không hỗ trợ trao đổi thời gian thực:** Hệ thống không bao gồm các chức năng Chat trực tiếp (Live Chat), Gọi thoại/Video call nội bộ. Mọi tương tác diễn ra thông qua luồng trao đổi trên Ticket và Yêu cầu bổ sung hồ sơ.
* **Gửi thông báo:** Hệ thống tập trung vào thông báo nội bộ trong ứng dụng (In-app Notifications).

---

## 3. Giả định về Hạ tầng & Vận hành (Infrastructure & Operations)

* **Hạ tầng máy chủ:** Toàn bộ máy chủ (Server/Cloud), tên miền (Domain), chứng chỉ SSL và môi trường lưu trữ do **Aurora University cung cấp** đúng thời hạn.
* **Phụ thuộc hạ tầng:** Hiệu năng, độ tin cậy và tính ổn định của hệ thống phụ thuộc hoàn toàn vào chất lượng hạ tầng mạng và máy chủ của Client.
* **Bảo trì & Sao lưu:** Đơn vị phát triển không chịu trách nhiệm thiết lập sao lưu tự động (Auto-backup), theo dõi vận hành máy chủ lâu dài hay hỗ trợ hạ tầng sau khi kết thúc thời gian bảo hành.
* **Đánh giá an toàn thông tin:** Dự án không bao gồm yêu cầu đánh giá an ninh mạng chuyên sâu (Penetration Testing) hoặc các chứng nhận bảo mật quốc tế.

---

## 4. Giả định về Quản lý Dự án & Phối hợp (Project Management)

* **Thời gian chờ phê duyệt:** Tổng thời gian 14 tuần phát triển **chưa bao gồm** thời gian chờ phản hồi, rà soát hoặc phê duyệt tài liệu/giao diện từ phía Aurora University. Nếu có phát sinh chậm trễ phản hồi, tiến độ dự án sẽ được điều chỉnh tương ứng.
* **Tiêu chuẩn kiểm thử UAT:** Việc kiểm thử chấp nhận (UAT) kéo dài **10 ngày làm việc** được tính sau khi hoàn tất bàn giao chính thức. Các lỗi nhỏ không làm gián đoạn chức năng cốt lõi sẽ không được tính là điều kiện từ chối nghiệm thu.
* **Chính sách bảo hành:** Bảo hành sửa lỗi kỹ thuật miễn phí trong **30 ngày** kể từ ngày ký biên bản nghiệm thu. Không áp dụng cho việc thay đổi quy trình nghiệp vụ hoặc yêu cầu tính năng mới ngoài scope.


---

## Tài liệu nguồn: 08-project/constraints.md

# [PRJ-02] Ràng buộc Dự án (Project Constraints)

Tài liệu này xác định các giới hạn và ràng buộc cố định về thời gian, ngân sách, phân bổ nguồn lực và hạ tầng kỹ thuật đối với dự án **UniSupport** tại **Aurora University**.

---

## 1. Ràng buộc về Thời gian & Tiến độ (Time Constraints)

* **Tổng thời gian phát triển:** **14 tuần** (tương đương khoảng **70 ngày làm việc**), tính từ ngày khởi động chính thức đến khi hoàn tất triển khai bàn giao.
* **Quy trình nghiệm thu:** Sau khi bàn giao, Aurora University có **10 ngày làm việc** (Tuần 15–16) để tiến hành kiểm thử UAT và nghiệm thu chính thức (không tính gộp vào 14 tuần phát triển).
* **Thời gian bảo hành:** **30 ngày** hỗ trợ kỹ thuật miễn phí kể từ ngày ký biên bản nghiệm thu.
* **Điều chỉnh tiến độ:** Thời gian chờ phản hồi, xác nhận hoặc cung cấp thông tin/hạ tầng từ phía Client vượt quá thỏa thuận (quá 03 ngày làm việc) sẽ được cộng tương ứng vào tiến độ chung của dự án.

---

## 2. Ràng buộc về Chi phí & Ngân sách (Budget & Cost Breakdown)

### 2.1 Tổng ngân sách hợp đồng
* **Tổng kinh phí cố định:** **300.000.000 VNĐ** (Ba trăm triệu đồng chẵn).

### 2.2 Cơ cấu Chi phí Nhân sự Nội bộ (Internal Resource Cost Baseline)

| STT | Vị trí Nhân sự | Đơn giá / Giờ (VNĐ) | Thời gian làm việc (h) | Lương Gross phân bổ (VNĐ) | Bảo hiểm 21,5% (VNĐ) | Chi phí Nhân sự Nội bộ (VNĐ) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Project Manager (PM) | 409.091 | 70 | 28.636.364 | 6.156.818 | 34.793.182 |
| 2 | Business Analyst (BA) | 236.364 | 63 | 14.890.909 | 3.201.545 | 18.092.455 |
| 3 | UI/UX Designer | 218.182 | 27 | 5.890.909 | 1.266.545 | 7.157.455 |
| 4 | Technical Lead (TL) | 454.545 | 31 | 14.090.909 | 3.029.545 | 17.120.455 |
| 5 | Frontend Developer 1 | 254.545 | 56 | 14.254.545 | 3.064.727 | 17.319.273 |
| 6 | Frontend Developer 2 | 181.818 | 61 | 11.090.909 | 2.384.545 | 13.475.455 |
| 7 | Backend Developer 1 | 254.545 | 107 | 27.236.364 | 5.855.818 | 33.092.182 |
| 8 | Backend Developer 2 | 181.818 | 75 | 13.636.364 | 2.931.818 | 16.568.182 |
| 9 | QA/QC Engineer | 181.818 | 98 | 17.818.182 | 3.830.909 | 21.649.091 |
| 10 | DevOps / Deployment Engineer | 200.000 | 30 | 6.000.000 | 1.290.000 | 7.290.000 |
| | **TỔNG CƠ SỞ** | | **618h** | **153.545.455** | **33.012.273** | **186.557.727** |

### 2.3 Tổng hợp Chi phí Kế hoạch & Dự phòng
* **Tổng công sức cơ sở của Business Functions:** 518h
* **Hoạt động cấp dự án (PM & DevOps):** 100h
* **Tổng công sức cơ sở toàn dự án:** **618h**
* **Chi phí nhân sự nội bộ cơ sở:** **186.557.727 VNĐ**
* **Dự phòng rủi ro công sức (Risk Reserve / Buffer):** **22h**
* **Chi phí dự phòng rủi ro ước tính:** **6.641.214 VNĐ**
* **Tổng công sức kế hoạch:** **640h**
* **Tổng chi phí nhân sự kế hoạch (sử dụng toàn bộ dự phòng):** **193.198.941 VNĐ**
* **Phần ngân sách còn lại (Quản lý dự án, chi phí hạ tầng hỗ trợ & lợi nhuận định mức):** **106.801.059 VNĐ** (Tổng ngân sách: 300.000.000 VNĐ).

---

## 3. Ràng buộc về Nguồn lực & Phân bổ Công sức (Resource Allocation Breakdown)

* **M1 – Student (Phân hệ Sinh viên):** 124h cơ sở + 4h buffer = **128h kế hoạch** (5 dòng công sức, 4 FR Student trong PRD).
* **M2 – Staff (Phân hệ Nhân viên):** 187h cơ sở + 10h buffer = **197h kế hoạch** (6 dòng công sức, 5 FR Staff trong PRD).
* **M3 – Admin (Phân hệ Quản trị & Báo cáo):** 207h cơ sở + 8h buffer = **215h kế hoạch** (6 dòng công sức, 5 FR Management trong PRD).
* **Hoạt động cấp dự án (PM + DevOps):** 100h cơ sở + 0h buffer = **100h kế hoạch**.
* **Tổng toàn bộ chức năng & hoạt động:** **618h cơ sở + 22h buffer = 640h kế hoạch**.

---

## 4. Ràng buộc Kỹ thuật & Hạ tầng (Technical Constraints)

* **Hạ tầng triển khai:** Hệ thống hoàn toàn phụ thuộc vào Server, tên miền và môi trường mạng do Aurora University cung cấp.
* **Quy mô hệ thống:** Tối ưu cho khoảng **3.000 sinh viên**; không thiết kế chịu tải lớn (Load balancing / Auto-scaling) hoặc kiến trúc phân tán phức tạp.
* **Loại ứng dụng:** Chỉ triển khai dưới dạng **Web Application** (Responsive UI cho máy tính và thiết bị di động), không phát triển Mobile App độc lập (iOS/Android).
* **Tích hợp:** Không tích hợp hệ thống bên thứ ba (SSO, CRM, LMS...) ngoài phạm vi đã xác định trong PRD.
* **Bảo mật:** Không bao gồm các yêu cầu chứng nhận bảo mật quốc tế (ISO, PCI-DSS) hoặc đánh giá an ninh mạng chuyên sâu (Penetration Testing).

---

## 5. Ràng buộc về Giao tiếp & Quản lý Thay đổi (Change Management Constraints)

* **Đầu mối liên lạc:** Mỗi bên chỉ định 01 Quản lý dự án (PM) làm đầu mối chính để trao đổi và phê duyệt tài liệu/kết quả.
* **Yêu cầu thay đổi (Change Request):** Mọi yêu cầu phát sinh thêm tính năng hoặc thay đổi phạm vi ngoài thỏa thuận ban đầu sẽ được đánh giá tác động về tiến độ và chi phí bổ sung bằng văn bản riêng.


---

## Tài liệu nguồn: 08-project/glossary.md

# [PRJ-05] Thuật ngữ & Giải thích Khái niệm (Glossary)

Tài liệu này định nghĩa các thuật ngữ kỹ thuật, nghiệp vụ và các từ viết tắt được sử dụng xuyên suốt trong toàn bộ hệ thống tài liệu dự án **UniSupport**.

---

## 1. Bảng Thuật ngữ Dự án

| Thuật ngữ / Từ viết tắt | Tên tiếng Anh đầy đủ | Giải thích nghĩa |
| :--- | :--- | :--- |
| **Ticket (Phiếu hỗ trợ)** | Support Ticket | Đơn vị dữ liệu cốt lõi đại diện cho một yêu cầu hỗ trợ do sinh viên gửi lên hệ thống, chứa mã ID, mô tả, tệp đính kèm và lịch sử xử lý. |
| **SLA** | Service Level Agreement | Cam kết mức độ dịch vụ; thời hạn quy định mà Nhân viên phải hoàn tất xử lý một Ticket (ví dụ: trong vòng 24h - 48h). |
| **RBAC** | Role-Based Access Control | Mô hình phân quyền dựa trên vai trò. Người dùng được gán vai trò (STUDENT, STAFF, MANAGER, ADMIN) và vai trò quyết định quyền thao tác trên hệ thống. |
| **PRD** | Product Requirements Document | Tài liệu Yêu cầu Sản phẩm, chi tiết hóa các tính năng, luồng nghiệp vụ và tiêu chí chấp nhận của phần mềm. |
| **UAT** | User Acceptance Testing | Kiểm thử chấp nhận sản phẩm do phía Khách hàng (Aurora University) thực hiện trước khi ký nghiệm thu bàn giao. |
| **RTM** | Requirements Traceability Matrix | Ma trận truy xuất yêu cầu, giúp đối chiếu từ Yêu cầu nghiệp vụ đến kịch bản kiểm thử (Test Cases). |
| **C4 Model** | Context, Containers, Components, Code | Mô hình chuẩn hóa dùng để vẽ và mô tả kiến trúc phần mềm theo các cấp độ từ tổng quan đến chi tiết. |
| **Audit Log** | Audit Logging | Nhật ký ghi lại toàn bộ các thao tác quan trọng (đăng nhập, đổi trạng thái Ticket, phân quyền) phục vụ tra soát bảo mật. |
| **Responsive UI** | Responsive User Interface | Giao diện phần mềm tự động điều chỉnh bố cục hiển thị phù hợp với kích thước màn hình Máy tính (Desktop) và Điện thoại (Mobile). |
| **ADR** | Architectural Decision Record | Tài liệu ghi nhận các quyết định kiến trúc kỹ thuật quan trọng và lý do lựa chọn phương án đó trong quá trình phát triển. |


---

## Tài liệu nguồn: 08-project/milestones-and-timeline.md

# [PRJ-03] Tiến độ & Cột mốc thực hiện (Milestones & Timeline)

Tài liệu chi tiết hóa lộ trình triển khai dự án **UniSupport** qua 6 giai đoạn trong 14 tuần làm việc phát triển theo phương pháp **Vertical Slice (Feature-driven Development)**, với tổng công sức **618h cơ sở + 22h dự phòng = 640h kế hoạch**.

---

## 1. Kế hoạch thực hiện theo Giai đoạn (Phases Schedule)

| Giai đoạn | Thời gian giữ theo bản hiện tại | Đầu ra review | Giới hạn công sức |
| --- | --- | --- | --- |
| 1. Làm rõ yêu cầu | Tuần 1–2 | 14 FR, quyền vai trò, danh mục và các sai lệch nguồn được đối chiếu | Dùng BA/PM/TL trong giờ nguồn, chưa tự chia giờ theo tuần |
| 2. Chuẩn bị thiết kế | Tuần 3–4 | Đầu ra thiết kế theo hồ sơ hiện có; không chọn phương án kỹ thuật mới | Dùng giờ UI/UX/TL và các vai trò của đúng dòng nguồn |
| 3. Hoàn thiện các luồng nghiệp vụ | Tuần 5–9 | Demo: cấp tài khoản/quyền → Student gửi/Staff thấy → tiếp nhận/chuyển/bổ sung → kết quả/đánh giá → dashboard/báo cáo/xuất | M01 128; M02 197; M03 215 là giờ cho toàn bộ công việc nhóm, không riêng giờ phát triển ở giai đoạn này |
| 4. Đối chiếu liên vai trò và kiểm thử nội bộ | Tuần 10–12 | Kết quả kiểm tra các luồng và phạm vi quyền theo 14 FR | QA 98 giờ đã nằm trong dòng chức năng, không cộng thêm một đợt QA |
| 5. Hoàn thiện hồ sơ và chuẩn bị bàn giao | Tuần 13 | Các lỗi thuộc phạm vi đã có được xử lý và ghi nhận | Dùng giờ còn lại/dự phòng đúng dòng; không tự tạo estimate mới |
| 6. Bàn giao | Tuần 14 | Tài liệu/kết quả bàn giao theo hồ sơ hiện có | PM tổng 70; DevOps tổng 30 cho toàn dự án, không cộng lại theo giai đoạn |

**Cách đọc lịch:** các tuần giữ như tài liệu hiện tại; đây không phải cam kết công suất từng người đã được kiểm chứng. Workbook nguồn chưa phân giờ theo tuần, vì vậy bỏ các con số giai đoạn tự chia. 618 giờ cơ sở + 22 dự phòng là trần toàn dự án; các giai đoạn, UAT và hỗ trợ không tự sinh effort ngoài bảng. Phân công thực tế chỉ dùng đúng giờ/role/dòng nguồn và không coi mỗi role làm mọi chức năng.

---

## 2. Các Cột mốc quan trọng (Key Milestones)

* **Mốc 0 (Tuần 1):** Ký hợp đồng hợp tác và tạm ứng kinh phí đợt 1.
* **Mốc 1 (Cuối Tuần 2):** Phê duyệt tài liệu Phạm vi & Yêu cầu nghiệp vụ (PRD) cùng Bảng phân bổ Resource (640h).
* **Mốc 2 (Cuối Tuần 4):** Phê duyệt Thiết kế giao diện (UI/UX Prototype), Kiến trúc hệ thống và dựng xong Nền tảng dự án (Boilerplate).
* **Mốc 3 (Cuối Tuần 9):** Hoàn thành phát triển 3 phân hệ nghiệp vụ cốt lõi (M1 Sinh viên, M2 Nhân viên, M3 Quản trị) & Demo E2E nội bộ từng luồng.
* **Mốc 4 (Cuối Tuần 12):** Hoàn thành tích hợp Cross-slice và kết thúc đợt kiểm thử nội bộ (Internal QA/QC).
* **Mốc 5 (Cuối Tuần 14):** Bàn giao chính thức hệ thống Production, tài liệu và mã nguồn; bắt đầu thời gian 10 ngày kiểm thử UAT cùng Aurora University.

---

## 3. Quy trình Nghiệm thu & Bảo hành

### 3.1 Quy trình Nghiệm thu (10 ngày làm việc - Sau 14 tuần phát triển)
1. **Bàn giao chính thức (Cuối Tuần 14):** Đơn vị phát triển bàn giao phần mềm đã triển khai trên hạ tầng Production của Client và đầy đủ bộ tài liệu.
2. **Thực hiện kiểm thử UAT (10 ngày làm việc / Tuần 15–16):** Aurora University tiến hành kiểm thử chấp nhận người dùng dựa trên kịch bản UAT E2E và chốt danh sách phản hồi. Đội ngũ phát triển phối hợp hỗ trợ và khắc phục các lỗi phát sinh trong thời gian này.
3. **Tiêu chí đạt nghiệm thu:**
   * Các luồng nghiệp vụ E2E (Sinh viên, Nhân viên, Quản lý) hoạt động chính xác theo kịch bản.
   * Phân quyền RBAC hoạt động chính xác theo vai trò trên từng chức năng.
   * Không còn lỗi nghiêm trọng (Blocker/Critical) gián đoạn chức năng chính.
   * Tài liệu bàn giao đầy đủ theo cam kết.

### 3.2 Chính sách Bảo hành (30 ngày)
* **Thời hạn:** 30 ngày kể từ ngày ký biên bản nghiệm thu chính thức (sau khi hoàn tất 10 ngày UAT).
* **Phạm vi hỗ trợ:** Khắc phục miễn phí các lỗi kỹ thuật (Bugs) phát sinh do đội ngũ phát triển.
* **Lưu ý:** Không bao gồm việc thay đổi yêu cầu, thêm tính năng mới hoặc xử lý sự cố do hạ tầng máy chủ của Client gây ra.


---

## Tài liệu nguồn: 08-project/open-questions.md

# Các đầu vào và sai lệch cần theo dõi

## Đầu vào từ hồ sơ hiện có

| Mục | Cần theo dõi | Trạng thái trong tài liệu |
| --- | --- | --- |
| Hạ tầng nhà trường | Thông tin Server, tên miền, môi trường được cung cấp theo hồ sơ triển khai hiện có | Chưa có bằng chứng cung cấp trong bộ file này; không đổi giải pháp |
| Dữ liệu tài khoản ban đầu | Danh sách người dùng, vai trò và phòng ban để ADMIN cấp tài khoản theo FR-MNG-04 | Không tự thêm import Excel hoặc tự đăng ký |
| Danh mục đầu vào | Danh sách nhóm vấn đề và phòng ban mặc định do ADMIN quản lý | Quyền đã có; chưa tự đặt thêm danh mục hoặc màn hình |
| Lý do chuyển phòng | FR-STF-03 đã quy định bắt buộc 10–500 ký tự, không toàn khoảng trắng | Đã có trong PRD; không còn là câu hỏi tùy chọn/không bắt buộc |
| Phạm vi dòng FAQ/mở lại/lưu trữ | Xem [giới hạn Resources](Phan_bo_Resources_Antigravity.md) | Giữ giờ, không tự tạo FR hay ca nghiệm thu mới |
| Sai lệch tài liệu kỹ thuật | Xem [prd-review-notes.md](08-project/prd-review-notes.md) | Ghi nhận để đối chiếu, không tự sửa triển khai |

## Nguyên tắc cập nhật

Ghi quyết định dựa trên bằng chứng nguồn thực tế, không coi dòng công sức hoặc nội dung do công cụ tạo là phê duyệt thêm chức năng. Giữ 14 FR và 640 giờ; không yêu cầu xác nhận lại những quy tắc đã được PRD quy định rõ.


---

## Tài liệu nguồn: 08-project/prd-review-notes.md

# Ghi nhận đối chiếu PRD và tài liệu hiện tại

## Các sửa đổi nghiệp vụ đã thực hiện

- Đồng bộ 14 mã FR giữa PRD, README, Product Scope, Workflows, RTM và kịch bản nghiệm thu; 17 dòng Resources dùng mã R độc lập.
- Giữ đúng 187 giá trị giờ của 17 dòng công việc (8 vai trò, cơ sở, dự phòng, kế hoạch), cùng PM 70 và DevOps 30; tổng 640.
- Tách MANAGER/ADMIN, Staff Claim và Manager/Admin Assign; danh mục nhóm vấn đề do ADMIN quản lý và gắn phòng ban mặc định.
- Làm rõ 5MB/tệp, tối đa 5 tệp sinh viên / 3 tệp kết quả, PDF/PNG/JPG/JPEG; sửa message thiếu trường và phân biệt sai định dạng/quá dung lượng.
- Nối luồng bổ sung trên cùng Ticket, phân biệt NEED_MORE_INFO/IN_PROGRESS/TRANSFERRED/RESOLVED/CLOSED; phân biệt hoàn tất xử lý với đóng.
- Nghiệm thu theo các giới hạn đã có, không yêu cầu FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ, tự sinh/gửi mật khẩu hoặc UI dọn dẹp mới.
- Bỏ phân giờ giai đoạn không có trong nguồn; giữ lịch hiện tại nhưng không khẳng định đã kiểm chứng công suất từng người/tuần.
- Tạo tài liệu đối chiếu Resources đang thiếu và tạo lại bản tổng hợp từ file hiện tại.

## Những sai lệch thuộc nội dung kỹ thuật được giữ nguyên theo yêu cầu người dùng

Các mục dưới đây là **quan sát trực tiếp trong file**, không phải bug ứng dụng đã tái hiện. Bản sửa không thay API, schema, enum, thuật toán, kiến trúc hoặc nội dung triển khai của các tài liệu này. Chúng không được dùng để mở rộng PRD nghiệp vụ đã chốt.

| Tài liệu/vị trí | Sai lệch hiện tại | Cách đọc trong bản sửa |
| --- | --- | --- |
| 02-domain/ticket-model.md; 07-architecture/data-model.md | WAITING_STUDENT/CANCELLED, tên trường sinh viên/phụ trách và 10MB/255 ký tự khác PRD | Giữ bảng kỹ thuật; đầu vào nghiệp vụ theo FR-STU-02/03. Không tự thêm trạng thái hoặc đổi schema. |
| 05-non-functional-requirements/performance.md; 07-architecture/security-design.md | Còn ghi 10MB và một số định dạng thiếu JPEG | Nghiệp vụ/AC theo 5MB và bốn định dạng của PRD. Không chỉnh NFR hoặc phương án file. |
| 05-non-functional-requirements/security.md; 07-architecture/security-design.md; ADR-002 | Gộp 3 vai trò/MANAGEMENT và quyền quản trị toàn trường, khác MANAGER/ADMIN trong PRD | Quyền nghiệp vụ theo Actors & Roles/FR-MNG-01/04. Nội dung kỹ thuật giữ nguyên, chưa xác nhận đã đồng bộ triển khai. |
| M04 prd.md/README.md | FR-STU-04 bị gọi là thông báo; FR-STF-03 bị gọi là SLA; WAITING_STUDENT; cảnh báo 2 giờ thay vì ngưỡng PRD; thêm mark-all-read/âm thanh/xem tất cả | Tài liệu hỗ trợ hiện tại, không phải FR nghiệp vụ mới. Giữ giờ R-STU-04 19 và giờ nguồn liên quan; không chốt các mở rộng đó. |
| M05 prd.md/README.md | Dùng FR-ADM-01/03/04 theo dòng công sức, mã FR-SEC trùng cách gọi NFR, timeout 24 giờ, hành vi đổi mật khẩu liên thiết bị | Đối chiếu bằng R-ADM; không cộng FR hoặc effort mới, không chốt cơ chế phiên mới. |
| 07-architecture/api-design.md | Cổng Management gộp quyền; đường dẫn rating khác PRD rate; mô tả Resolve/Close còn gộp | Giữ API hiện tại. Không thay endpoint hoặc coi mô tả này là quyền mới cho Manager. |
| ADR-001 và README ADR | Mã Ticket dùng YYYYMM/random, khác ví dụ YYYYMMDD-XXXX trong PRD | Giữ quyết định kỹ thuật gốc hiện tại; bản sửa nghiệp vụ chỉ dùng ví dụ của PRD, không chọn bộ sinh mã thay thế. |
| 02-domain/state-transition.md | Chưa liệt kê NEED_MORE_INFO → TRANSFERRED trong khi FR-STF-03 cho phép chuyển trong trạng thái đó; quyền Staff cũ xem sau chuyển còn chưa thống nhất | Workflow dẫn về điều kiện FR-STF-03 đã có; không tự thêm hàng vào FSM hoặc quyền dữ liệu trong triển khai. |
| BR-09 / vòng đời | Cách ghi 3 ngày làm việc và 72 giờ làm việc chưa cùng cách tính | Giữ quy tắc Auto-close hiện có, không chọn thuật toán hoặc deadline mới. |
| 05-deployment và timeline | Môi trường Production trước/sau nghiệm thu còn mô tả khác nhau | Giữ nội dung triển khai; lịch không được dùng làm estimate giờ mới. |

## Nguồn video và giới hạn bằng chứng

Các điểm sửa về tài khoản, nhóm vấn đề và độ rõ PRD đối chiếu review V1 00:55–01:15, 02:20–05:06, 05:17–06:26; mã FR/giờ và luồng đối chiếu V2 00:42–05:57, 07:42–10:50. Mốc là khoảng tìm đoạn review tài liệu, không phải thời điểm một bug app. Ý lời nói dùng bản nhận dạng đã nêu giới hạn ở báo cáo video trước, không trích nguyên văn hay coi là phê duyệt thêm chức năng.

## Quy tắc giữ phạm vi

Nguồn FR là 3 PRD nghiệp vụ, nguồn giờ là workbook Resource. Tài liệu tổng hợp cũ và thư mục unisupport-prd-extracted là bản tham chiếu, không trộn vào bản hiện tại. Không xác nhận QA/UAT đã Pass khi chưa có kết quả chạy. Không tính lại chi phí nhân sự trong lần sửa PRD này.


---

## Tài liệu nguồn: Phan_bo_Resources_Antigravity.md

# Đối chiếu giờ Resources UniSupport

Nguồn số giờ: **Phân bổ Resources.xlsx**, sheet **Resource**, do người dùng cung cấp tại `C:/Users/ACER/Downloads/Phân bổ Resources.xlsx`. Tài liệu này sao lại giờ và tên công việc để tra cứu; không thay thế workbook nguồn, không phải bảng estimate mới và không xác nhận thêm chức năng.

## Bảng giờ theo dòng và vai trò

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-STU-01 | 3 | Tra cứu hướng dẫn & FAQ | 3 | 3 | 0 | 4 | 0 | 0 | 0 | 4 | 14 | 0 | 14 | Chưa có FR FAQ được chốt; giữ dòng nguồn, không thay mã đăng nhập |
| R-STU-02 | 4 | Tạo & gửi yêu cầu hỗ trợ | 5 | 5 | 1 | 10 | 1 | 6 | 1 | 5 | 34 | 3 | 37 | FR-STU-02 |
| R-STU-03 | 5 | Xem & theo dõi yêu cầu | 4 | 3 | 1 | 8 | 3 | 5 | 3 | 5 | 32 | 1 | 33 | FR-STU-03 |
| R-STU-04 | 6 | Nhận thông báo trạng thái | 3 | 1 | 0 | 4 | 0 | 4 | 4 | 3 | 19 | 0 | 19 | FR-STU-03; thông báo trạng thái đã có |
| R-STU-05 | 7 | Bổ sung thông tin & phản hồi | 3 | 1 | 0 | 5 | 3 | 5 | 3 | 5 | 25 | 0 | 25 | FR-STU-03; FR-STU-04 (đối chiếu phần phản hồi/đánh giá; chưa có phân bổ riêng) |
| R-STF-01 | 12 | Tiếp nhận, tìm kiếm & lọc yêu cầu | 3 | 3 | 1 | 4 | 5 | 8 | 3 | 6 | 33 | 0 | 33 | FR-STF-02; Queue phòng ban đã có |
| R-STF-02 | 13 | Phân loại & phân công xử lý | 4 | 0 | 3 | 4 | 3 | 9 | 5 | 9 | 37 | 1 | 38 | FR-STF-02; quyền phân công MANAGER/ADMIN đã có |
| R-STF-03 | 14 | Quản lý ưu tiên & thời hạn | 4 | 0 | 4 | 3 | 3 | 6 | 3 | 3 | 26 | 3 | 29 | FR-STF-02; FR-MNG-02 |
| R-STF-04 | 15 | Xử lý & cập nhật yêu cầu | 4 | 1 | 1 | 4 | 4 | 9 | 4 | 9 | 36 | 3 | 39 | FR-STF-04 |
| R-STF-05 | 16 | Chuyển xử lý, Escalation & hoàn tất | 3 | 0 | 3 | 3 | 3 | 8 | 4 | 5 | 29 | 3 | 32 | FR-STF-03; FR-STF-05 |
| R-STF-06 | 17 | Đóng & mở lại yêu cầu | 3 | 0 | 1 | 3 | 3 | 8 | 3 | 5 | 26 | 0 | 26 | FR-STF-05; FR-STU-04; không chốt phần mở lại xử lý |
| R-ADM-01 | 22 | Quản lý tài khoản, vai trò & RBAC | 5 | 3 | 6 | 3 | 8 | 13 | 9 | 13 | 60 | 4 | 64 | FR-MNG-04; FR-STU-01, FR-STF-01, FR-MNG-01 dùng chung |
| R-ADM-02 | 23 | Quản lý phòng ban & danh mục | 4 | 1 | 3 | 0 | 4 | 5 | 5 | 4 | 26 | 0 | 26 | Danh mục ADMIN quản lý tại Actors & Roles / Terminology; không thêm FR |
| R-ADM-03 | 24 | Kiểm soát quyền truy cập & Audit Trail | 4 | 0 | 4 | 1 | 4 | 9 | 5 | 9 | 36 | 4 | 40 | FR-MNG-04; FR-MNG-05; quyền dữ liệu đã có |
| R-ADM-04 | 25 | Quản lý thời hạn lưu trữ | 3 | 0 | 1 | 0 | 0 | 4 | 4 | 3 | 15 | 0 | 15 | Giữ giờ nguồn; chưa có FR nghiệp vụ riêng về cấu hình/dọn dẹp lưu trữ |
| R-ADM-05 | 26 | Dashboard & thống kê quản trị | 4 | 3 | 1 | 0 | 9 | 3 | 9 | 4 | 33 | 0 | 33 | FR-MNG-02 |
| R-ADM-06 | 27 | Báo cáo, mức độ hài lòng & xuất dữ liệu | 4 | 3 | 1 | 0 | 8 | 5 | 10 | 6 | 37 | 0 | 37 | FR-MNG-03; sử dụng dữ liệu FR-STU-04 |
| Tổng | — | Mỗi dòng tính một lần | 63 | 27 | 31 | 56 | 61 | 107 | 75 | 98 | 518 | 22 | 540 | Không cộng lại khi nhiều FR dùng chung |

## Tổng công sức

| Nhóm | Cơ sở | Dự phòng | Kế hoạch |
| --- | ---: | ---: | ---: |
| Student (Resource!3:7) | 124 | 4 | 128 |
| Staff (Resource!12:17) | 187 | 10 | 197 |
| Admin/Management (Resource!22:27) | 207 | 8 | 215 |
| Chức năng | 518 | 22 | 540 |
| PM (Resource!35) | 70 | 0 | 70 |
| DevOps (Resource!36) | 30 | 0 | 30 |
| Toàn dự án | 618 | 22 | 640 |

Giờ vai trò toàn dự án: PM 70; BA 63; UI/UX 27; TL 31; FE1 56; FE2 61; BE1 107; BE2 75; QA 98; DevOps 30. Dự phòng 22 giờ giữ theo dòng nguồn và chưa tự gán cho người. Ô giờ BE2 ở sheet chi phí đang trống; giờ BE2 lấy từ Resource là 75, không coi ô trống là 0.

Giờ bao gồm các công việc thuộc dự án trong bảng nguồn. Không cộng thêm giờ triển khai, tích hợp, QA/UAT hoặc bảo hành ngoài tổng 640 khi tài liệu nguồn chưa phân bổ; lịch có giai đoạn nào không có nghĩa được thêm giờ cho giai đoạn đó. Bản sửa không tính lại đơn giá, lương, bảo hiểm hoặc lợi nhuận.

## Giới hạn phạm vi và giờ nguồn

- 14 mã FR trong M01–M03 là mã yêu cầu sản phẩm. 17 dòng Excel dùng mã R-STU/R-STF/R-ADM để đối chiếu công sức; không đổi các dòng đó thành FR mới.
- Một dòng công sức có thể liên quan nhiều FR. Chỉ tính dòng đó một lần; không tự tách hoặc chia lại giờ cho FR, vai trò hay tuần.
- FAQ có 14 giờ ở dòng nguồn nhưng chưa có đặc tả FR được chốt. Giữ giờ; không tự thêm màn hình, tìm kiếm FAQ hay đổi FR-STU-01 từ đăng nhập thành FAQ.
- Dòng “Đóng & mở lại yêu cầu” giữ 26 giờ; bản PRD/vòng đời hiện có không hỗ trợ mở lại quá trình xử lý Ticket đã CLOSED. Mở lại trang chi tiết là thao tác xem lại.
- Phản hồi/CSAT đã có tại FR-STU-04. Ghép với R-STU-05 chỉ là đối chiếu; chưa xác nhận chia effort riêng và không cộng thêm giờ.
- Dòng danh mục và lưu trữ được giữ nguyên giờ. Quyền cấu hình danh mục đã có trong tài liệu; không tự tạo FR, UI dọn dẹp/archiving hoặc chính sách lưu trữ mới.
- Tên “Escalation” trong dòng nguồn không đủ để chốt thêm luồng báo cáo vượt cấp. Bản sửa giữ luồng chuyển phòng ban/hoàn tất đã có.
- M04/M05 là tài liệu hỗ trợ kỹ thuật hiện tại, không phải hai phân hệ nghiệp vụ có effort bổ sung. Các mã FR-NTF/FR-SEC trong đó không được cộng vào 14 FR sản phẩm.
