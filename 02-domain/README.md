# 02 - Domain

Thư mục `02-domain` định nghĩa miền nghiệp vụ của **UniSupport**, bao gồm các khái niệm cốt lõi, mô hình Ticket, vòng đời xử lý, chuyển đổi trạng thái và các quy tắc nghiệp vụ dùng chung.

Các nội dung trong phần này là cơ sở để đặc tả Functional Requirements, Workflows, Acceptance Criteria và thiết kế hệ thống ở các phần tiếp theo.

## Phạm Vi Tài Liệu

Phần Domain bao gồm:

- Các thực thể và khái niệm nghiệp vụ cốt lõi.
- Thuật ngữ sử dụng thống nhất trong toàn hệ thống.
- Mô hình thông tin nghiệp vụ của Ticket và các dữ liệu liên quan.
- Vòng đời Ticket và các trạng thái xử lý.
- Quy tắc chuyển đổi trạng thái hợp lệ.
- Các quy tắc nghiệp vụ áp dụng xuyên suốt các phân hệ.

## Cấu Trúc Tài Liệu

| Tài liệu | Nội dung |
| :--- | :--- |
| [Domain Overview](./domain-overview.md) | Tổng quan miền nghiệp vụ, các khái niệm cốt lõi và luồng xử lý Ticket ở mức tổng quan. |
| [Terminology](./terminology.md) | Định nghĩa các thuật ngữ nghiệp vụ được sử dụng thống nhất trong toàn hệ thống. |
| [Ticket Model](./ticket-model.md) | Mô tả các thông tin nghiệp vụ chính của Ticket và các dữ liệu liên quan. |
| [Ticket Lifecycle](./ticket-lifecycle.md) | Mô tả các giai đoạn của Ticket từ khi được tạo đến khi hoàn tất xử lý. |
| [State Transition](./state-transition.md) | Quy định các trạng thái của Ticket và các chuyển đổi trạng thái hợp lệ. |
| [Business Rules](./business-rules.md) | Tổng hợp các quy tắc nghiệp vụ dùng chung như file đính kèm, phân công/chuyển xử lý, bổ sung thông tin, thời hạn xử lý, CSAT và Audit. |

## Quan Hệ Giữa Các Tài Liệu

`Domain Overview` xác lập bối cảnh và các khái niệm nghiệp vụ chung. `Terminology` chuẩn hóa thuật ngữ sử dụng trong toàn bộ tài liệu. `Ticket Model`, `Ticket Lifecycle` và `State Transition` đặc tả cấu trúc và quá trình xử lý Ticket. `Business Rules` tập hợp các quy tắc nghiệp vụ áp dụng xuyên suốt các phân hệ.

Các yêu cầu chức năng chi tiết của từng phân hệ được đặc tả tại [03-modules](../03-modules/).
