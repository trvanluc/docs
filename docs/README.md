# Tài Liệu Dự Án UniSupport

Kho tài liệu này mô tả phạm vi, nghiệp vụ, yêu cầu chức năng, workflow, yêu cầu phi chức năng, nghiệm thu, kiến trúc và các ràng buộc dự án của **UniSupport – Student Support Management System** tại Aurora University.

Tài liệu được tổ chức theo chuỗi: **Phạm vi dự án → Sản phẩm → Nghiệp vụ → PRD → Workflow → Yêu cầu phi chức năng → Nghiệm thu/RTM → Kiến trúc → Quản lý dự án**.

## Cấu Trúc Tài Liệu

```text
docs/
├── README.md
├── 01-product/
│   ├── README.md
│   ├── product-overview.md
│   ├── problem-statement.md
│   ├── goals-and-non-goals.md
│   ├── actors-and-roles.md
│   └── product-scope.md
├── 02-domain/
│   ├── README.md
│   ├── domain-overview.md
│   ├── terminology.md
│   ├── ticket-model.md
│   ├── ticket-lifecycle.md
│   ├── state-transition.md
│   └── business-rules.md
├── 03-modules/
│   ├── README.md
│   ├── M01-student-portal/
│   ├── M02-staff-operations/
│   └── M03-management-dashboard/
├── 04-workflows/
│   ├── README.md
│   ├── WF-01-submit-support-request.md
│   ├── WF-02-claim-and-triage.md
│   ├── WF-03-request-supplement.md
│   ├── WF-04-transfer-department.md
│   ├── WF-05-complete-and-resolve.md
│   ├── WF-06-close-and-rate.md
│   └── WF-07-escalation.md
├── 05-non-functional-requirements/
│   ├── README.md
│   ├── performance.md
│   ├── reliability.md
│   ├── security.md
│   ├── usability.md
│   ├── deployment.md
│   └── observability.md
├── 06-acceptance/
│   ├── README.md
│   ├── traceability-matrix.md
│   ├── test-scenarios.md
│   └── success-metrics.md
├── 07-architecture/
│   ├── README.md
│   ├── system-context.md
│   ├── architecture-overview.md
│   ├── data-model.md
│   ├── api-design.md
│   ├── security-design.md
│   └── technical-decisions/
├── 08-project/
│   ├── README.md
│   ├── Proposal.docx
│   ├── quotation.xlsx
│   ├── master-plan.md
│   ├── risk-register.md
│   ├── decision-log.md
│   ├── team-charter.md
│   ├── assumptions.md
│   ├── constraints.md
│   ├── milestones-and-timeline.md
│   ├── open-questions.md
│   ├── glossary.md
│   ├── sent/
│   └── plans/
│       ├── README.md
│       ├── wbs.xlsx
│       ├── ngan-sach-noi-bo.xlsx
│       ├── master-schedule.xlsx
│       └── images/
├── 09-quality/
│   └── quality-plan.md
├── 10-product-management/
│   └── ke-hoach-quan-ly-san-pham.md
└── 11-governance/
    └── ke-hoach-quan-tri-giam-sat.md
```

## Thứ tự đọc

1. Bài toán và phạm vi: [Proposal](08-project/Proposal.docx), [Tổng quan sản phẩm](01-product/README.md)
2. Yêu cầu: [Danh sách module](03-modules/README.md) → PRD từng module ([M01](03-modules/M01-student-portal/prd.md), [M02](03-modules/M02-staff-operations/prd.md), [M03](03-modules/M03-management-dashboard/prd.md)) → [NFR](05-non-functional-requirements/README.md)
3. Nghiệm thu: [Kịch bản test](06-acceptance/test-scenarios.md), [Ma trận truy vết](06-acceptance/traceability-matrix.md)
4. Giá và kế hoạch: [Báo giá](08-project/quotation.xlsx), [Master Plan](08-project/master-plan.md) + [master-schedule.xlsx](08-project/plans/master-schedule.xlsx), [Bộ mốc MS-01…MS-06](08-project/milestones-and-timeline.md), [Rủi ro](08-project/risk-register.md)
5. Cách làm việc: [Team Charter](08-project/team-charter.md), [Quality](09-quality/quality-plan.md), [Decision Log](08-project/decision-log.md), mẫu issue/PR trong [.github](../.github/)
6. Product: [Quy trình feedback](10-product-management/ke-hoach-quan-ly-san-pham.md#42-đo-lường-và-thu-thập-phản-hồi), [Roadmap](10-product-management/ke-hoach-quan-ly-san-pham.md#5-định-hướng-phát-triển-sản-phẩm), [Chỉ số giá trị](10-product-management/ke-hoach-quan-ly-san-pham.md#3-chỉ-số-đánh-giá-sản-phẩm)
7. Quản trị: [Báo cáo](11-governance/ke-hoach-quan-tri-giam-sat.md#2-quy-trình-báo-cáo), [Giám sát](11-governance/ke-hoach-quan-tri-giam-sat.md#3-chỉ-số-giám-sát-và-ngưỡng-cảnh-báo), [Change request](11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi)
8. Tài liệu hỗ trợ (bằng chứng): [Domain](02-domain/README.md), [Workflows](04-workflows/README.md), [Kiến trúc](07-architecture/README.md), [Bản proposal đã gửi](08-project/sent/)

## Tra nhanh vị trí

| Nội dung | Ở đâu |
| --- | --- |
| Scope (làm và không làm) | [Proposal.docx](08-project/Proposal.docx) mục 2 "Phạm Vi Chức Năng" và mục "Các hạng mục ngoài phạm vi hiện tại (Out of Scope)"; [goals-and-non-goals.md](01-product/goals-and-non-goals.md) |
| Nguồn lực | [ngan-sach-noi-bo.xlsx](08-project/plans/ngan-sach-noi-bo.xlsx) sheet `Resource` (theo vai trò); [master-schedule.xlsx](08-project/plans/master-schedule.xlsx) sheet `Resources` (theo mốc); đội thực thi `Mô phỏng`: [Team Charter mục 3](08-project/team-charter.md#3-vai-trò-và-trách-nhiệm) |
| Giá và hạng mục báo giá | [quotation.xlsx](08-project/quotation.xlsx) sheet `Hạng mục` |
| Milestones, Gantt, Change log | [master-schedule.xlsx](08-project/plans/master-schedule.xlsx) sheet `Milestones`, `Master Schedule`, `Change log`; giải thích: [master-plan.md](08-project/master-plan.md) |
| Priority FR | [03-modules/README.md](03-modules/README.md#mức-ưu-tiên-fr) |
| Rủi ro | [risk-register.md](08-project/risk-register.md) |
| Change request | Quy trình: [ke-hoach-quan-tri-giam-sat.md, mục 5](11-governance/ke-hoach-quan-tri-giam-sat.md#5-kiểm-soát-thay-đổi); CR thực tế: GitHub Issues nhãn `change-request` (mẫu [4-change-request.md](../.github/ISSUE_TEMPLATE/4-change-request.md)) |
| Nhãn GitHub | [ke-hoach-quan-tri-giam-sat.md, mục 6.1a](11-governance/ke-hoach-quan-tri-giam-sat.md#61a-nhãn-github) |
| Definition of Done | [quality-plan.md, mục 5](09-quality/quality-plan.md#5-definition-of-done-dod--tiêu-chuẩn-hoàn-thành) |
| Giả định, ràng buộc, câu hỏi mở | [assumptions.md](08-project/assumptions.md), [constraints.md](08-project/constraints.md), [open-questions.md](08-project/open-questions.md) |
| Quy trình báo cáo | [ke-hoach-quan-tri-giam-sat.md, mục 2](11-governance/ke-hoach-quan-tri-giam-sat.md#2-quy-trình-báo-cáo) |

## Quy ước mã

Liên kết chỉ ghi ở **một phía**: phía ghi là cột "Liên kết phải ghi". Ví dụ kịch bản test ghi mã AC mà nó kiểm; PRD không ghi ngược lại mã test.

Bộ khung không yêu cầu phần mềm chạy thật: nhóm làm tài liệu, kế hoạch và quy trình cho toàn dự án.

| Đối tượng | Dạng | Nơi gốc | Liên kết phải ghi |
| --- | --- | --- | --- |
| Module | `M01` | `03-modules/` | |
| Yêu cầu chức năng | `FR-XXX-01` | prd.md của module | |
| Tiêu chí nghiệm thu | `FR-XXX-01/AC-01` | prd.md của module | |
| Yêu cầu phi chức năng | `NFR-PERF-01` | `05-non-functional-requirements/` | |
| Kịch bản test | `TS-01` | `06-acceptance/test-scenarios.md` | Mã AC hoặc NFR được test |
| Hạng mục báo giá | `Q-01` | `08-project/quotation.xlsx` (sheet Hạng mục) | Module hoặc FR thuộc hạng mục |
| Milestone | `MS-01` | `08-project/plans/master-schedule.xlsx`; GitHub Milestones chỉ có `MS-01`…`MS-06` (task dev) | Phần giao được, điều kiện nghiệm thu |
| Parent task | `#12` | GitHub Issue | Mã FR, `MS-xx`, owner, hạn, điều kiện hoàn thành |
| Rủi ro | `R-01` | `08-project/risk-register.md` | Owner, phương án xử lý |
| Change request | `CR-01` | GitHub Issue | Tài liệu và task đã cập nhật |
| Giả định | `A-01` | `08-project/assumptions.md` | |

`M01` là module, `MS-01` là milestone; không dùng lẫn. Dạng mã trong chuẩn là ví dụ; nhóm đặt dạng khác vẫn được nếu mỗi mã là duy nhất và lần được. Cách đặt phần XXX của mã FR và mã giả định `A-01` là gợi ý của bộ khung.

## Dữ liệu mô phỏng

Đây là dự án môn học: phần mềm không chạy thật. Những phần dưới đây là `Mô phỏng` và được ghi chữ `Mô phỏng` ngay tại chỗ dùng (giả định `A-17` trong [assumptions.md](08-project/assumptions.md)).

| Phần | Mô phỏng? | Ghi chú |
| --- | --- | --- |
| Client (Aurora University), Nhà tài trợ dự án | Có | Khách hàng giả định của đề bài |
| Đội thực thi 10 vai trò (PM, BA, UI/UX, TL, FE1, FE2, BE1, BE2, QA, DevOps) | Có | Giờ công, đơn giá, owner task và rủi ro tính theo vai trò; 4 thành viên nhóm là ban quản lý thật ([Team Charter mục 3](08-project/team-charter.md#3-vai-trò-và-trách-nhiệm)) |
| Feedback | Có | GitHub Issues nhãn `feedback` |
| Change request | Có | GitHub Issues nhãn `change-request`, mã `CR-xx` |
| Báo cáo, giờ thực tế, số liệu kiểm thử | Có | Ví dụ trong [kế hoạch quản trị mục 6.2](11-governance/ke-hoach-quan-tri-giam-sat.md#62-mẫu-và-ví-dụ-báo-cáo-tuần) |

## Người chịu trách nhiệm tài liệu

Mỗi tài liệu (kể cả file Word/Excel) có một thành viên phụ trách chính, ghi ở [Team Charter mục 3.2](08-project/team-charter.md#32-ban-quản-lý-dự-án-phụ-trách-tài-liệu).

## Phạm Vi Nghiệp Vụ Chính

UniSupport có đúng **03 phân hệ nghiệp vụ**:

| Mã | Phân hệ | Người dùng chính |
| :--- | :--- | :--- |
| **M01** | Student Portal | Sinh viên |
| **M02** | Staff Operations | Nhân viên |
| **M03** | Management Dashboard | Quản lý |

Thông báo, xác thực, phân quyền, bảo mật file và Audit được triển khai như **các năng lực dùng chung** xuyên suốt ba phân hệ nghiệp vụ.

## Quy Ước Tài Liệu

- **Product, Domain và PRD** mô tả hành vi nghiệp vụ và không phụ thuộc vào công nghệ triển khai.
- **Workflows** thể hiện luồng phối hợp giữa các chức năng và phân hệ bằng Mermaid.
- **Yêu cầu phi chức năng** xác định các thuộc tính chất lượng áp dụng toàn hệ thống.
- **Kiến trúc** mô tả giải pháp kỹ thuật phục vụ các yêu cầu đã xác định và không làm thay đổi quy tắc nghiệp vụ.
- **Nghiệm thu và RTM** duy trì truy xuất giữa yêu cầu, workflow và kịch bản UAT.
- **Tài liệu dự án** quản lý các giả định, ràng buộc, tiến độ và quyết định cấp dự án.
