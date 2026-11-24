# 06 - Nghiệm Thu Và Truy Xuất Yêu Cầu

Thư mục này quản lý tiêu chí nghiệm thu, kịch bản UAT và khả năng truy xuất giữa gói công việc, yêu cầu chức năng và workflow của UniSupport.

## 1. Tài Liệu

| Tài liệu | Mục đích |
| :--- | :--- |
| [traceability-matrix.md](./traceability-matrix.md) | Liên kết gói công việc → FR/Flow → Workflow → UAT. |
| [test-scenarios.md](./test-scenarios.md) | Các kịch bản UAT đại diện cho ba phân hệ và năng lực dùng chung. |
| [success-metrics.md](./success-metrics.md) | Chỉ tiêu thành công, ngưỡng đạt và phương pháp kiểm chứng. |

## 2. Nguyên Tắc Nghiệm Thu

- Aurora University có **10 ngày làm việc sau bàn giao chính thức** để thực hiện nghiệm thu.
- Các luồng chính của M01, M02 và M03 phải hoạt động đúng yêu cầu.
- Phân quyền phải đúng theo vai trò và phạm vi dữ liệu.
- Không còn lỗi làm gián đoạn chức năng chính.
- Tài liệu bàn giao phải đầy đủ theo phạm vi dự án.
- Lỗi kỹ thuật không ảnh hưởng chức năng chính được ghi nhận và theo dõi khắc phục theo quy trình quản lý lỗi.

## 3. Nguyên Tắc Truy Xuất

- Effort kế hoạch được quản lý theo từng gói công việc.
- Một gói công việc có thể ánh xạ tới nhiều FR hoặc Flow.
- Xác thực là năng lực dùng chung; effort không được nhân đôi chỉ vì nhiều phân hệ cùng sử dụng.
- Kế hoạch nguồn lực dùng cùng mã `M01` (Student Portal), `M02` (Staff Operations), `M03` (Management Dashboard) với PRD.
- Nơi gốc mã gói và giờ là [wbs.xlsx](../08-project/plans/wbs.xlsx), sheet `WBS`; sheet `Đối chiếu mã` nối từng parent task với WBS, hàng Gantt, WP và hàng `Resource`. Sheet `Đối chiếu effort` giải thích các gói có ranh giới khác nhau, không cộng giờ của cùng một gói nhiều lần.
