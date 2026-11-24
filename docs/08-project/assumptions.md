# PRJ-01 - Giả Định Dự Án

Tài liệu này ghi nhận các giả định vận hành và triển khai được sử dụng trong kế hoạch dự án. Mỗi giả định có mã `A-xx`; hạng mục báo giá bị ảnh hưởng được nối ở [quotation.xlsx](quotation.xlsx) sheet `Giả định`. Phần giả định gửi khách nằm ở [Proposal.docx](Proposal.docx) mục 2.4 "Assumptions (Giả định)".

## 1. Phạm Vi Sử Dụng

- `A-01` Quy mô khoảng **3.000 sinh viên**.
- `A-02` UniSupport là **Web Application**, không phải mobile app độc lập.
- `A-03` Giao diện hỗ trợ Tiếng Việt và Tiếng Anh ở mức cơ bản.
- `A-04` Không tối ưu cho kiến trúc tải lớn vượt phạm vi dự án.

## 2. Tích Hợp Và Bảo Mật

- `A-05` Không yêu cầu tích hợp bên thứ ba trong phạm vi hiện tại.
- `A-06` Không bao gồm chat trực tiếp hoặc gọi thoại.
- `A-07` Không yêu cầu chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

## 3. Hạ Tầng

- `A-08` Hạ tầng máy chủ và tên miền do Aurora University cung cấp.
- `A-09` Hiệu năng và độ ổn định phụ thuộc điều kiện hạ tầng Aurora University.
- `A-10` Không bao gồm thiết lập sao lưu tự động, giám sát máy chủ và hỗ trợ hạ tầng lâu dài.

## 4. Phối Hợp

- `A-11` Thời gian 14 tuần không bao gồm thời gian chờ phản hồi hoặc phê duyệt vượt quá kế hoạch phối hợp.
- `A-12` Điều chỉnh phạm vi, chi phí hoặc tiến độ phải được hai bên xác nhận lại.
- `A-16` Cuối mỗi mốc `MS-xx`, client dùng thử bản staging và gửi phản hồi trong **02 ngày làm việc** sau buổi demo.

## 5. Dữ Liệu

- `A-13` Môi trường phát triển, kiểm thử, UAT và trình diễn sử dụng **dữ liệu giả lập** có cấu trúc tương ứng dữ liệu của Aurora University: tài khoản, phòng ban, Nhóm vấn đề, FAQ, Ticket và file đính kèm.
- `A-14` Không sử dụng dữ liệu cá nhân thật của sinh viên hoặc nhân viên.
- `A-15` Bộ dữ liệu giả lập đáp ứng các kịch bản tại `06-acceptance/test-scenarios.md` và các chỉ tiêu tại `06-acceptance/success-metrics.md`.

## 6. Môn Học

- `A-17` Đây là dự án môn học. Đội thực thi 10 vai trò, Aurora University (client), Nhà tài trợ dự án, feedback, change request và số liệu báo cáo là `Mô phỏng`; 4 thành viên nhóm là ban quản lý dự án thật (xem [Team Charter](team-charter.md)).
