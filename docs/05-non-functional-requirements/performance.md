# NFR-PERF - Hiệu Năng

## Mã yêu cầu

Nơi gốc của mã và ngưỡng. Kịch bản test (`06-acceptance/test-scenarios.md`) và các tài liệu khác chỉ dẫn mã.

| Mã | Yêu cầu | Ngưỡng / cách đo | Loại |
| --- | --- | --- | --- |
| `NFR-PERF-01` | Hệ thống chạy với dữ liệu đại diện quy mô dự án | Bộ dữ liệu UAT giả lập có 3.000 tài khoản sinh viên (giả định `A-01`); các luồng chính của M01, M02, M03 chạy hết mà không lỗi. | Cam kết với khách |
| `NFR-PERF-02` | Thời gian phản hồi của thao tác chính: đăng nhập, tạo Ticket, xem danh sách Ticket, xem Dashboard | Đo trên môi trường kiểm thử với dữ liệu của NFR-PERF-01: ít nhất 95% lượt đo phản hồi trong 3 giây. | Mục tiêu nội bộ, không phải tiêu chí nghiệm thu, vì tốc độ thực tế phụ thuộc hạ tầng do khách cấp (`A-09`) |
| `NFR-PERF-03` | Không treo chức năng | 0 lần thao tác chính bị treo hoặc lỗi làm gián đoạn luồng trong UAT bình thường. | Cam kết với khách |
| `NFR-PERF-04` | Dung lượng file đính kèm | Tối đa 10 MB/file (`BR-FILE-02`); file 10 MB tải lên và mở được. | Cam kết với khách |

## 1. Mục Tiêu

UniSupport phải đáp ứng ổn định các chức năng chính cho quy mô sử dụng khoảng **3.000 sinh viên** và không đặt mục tiêu cho kiến trúc tải lớn vượt phạm vi dự án.

## 2. Yêu Cầu

- Các thao tác chính như đăng nhập, tạo/xem Ticket, cập nhật xử lý, xem Dashboard và báo cáo được đo theo `NFR-PERF-02`.
- Danh sách Ticket và báo cáo phải hỗ trợ lọc/tìm kiếm mà không làm thay đổi hoặc mất dữ liệu nghiệp vụ.
- File đính kèm tối đa **10 MB/file** theo Business Rules.
- Ngưỡng thời gian phản hồi là `NFR-PERF-02` (mục tiêu nội bộ). Không cam kết với khách ngưỡng về số người dùng đồng thời hay thời gian phản hồi vì tốc độ thực tế phụ thuộc hạ tầng do Aurora University cung cấp (`A-09`).

## 3. Nghiệm Thu

- Các luồng chính của M01, M02, M03 hoạt động ổn định với bộ dữ liệu UAT đại diện cho phạm vi dự án.
- Không xuất hiện tình trạng treo chức năng hoặc lỗi làm gián đoạn luồng chính trong điều kiện UAT bình thường.
- Nếu hiệu năng phụ thuộc vào hạ tầng Aurora University, kết quả phải được đánh giá cùng điều kiện môi trường thực tế.
