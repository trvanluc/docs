# PRJ-01 - Giả Định Dự Án

Tài liệu này ghi nhận các giả định vận hành và triển khai được sử dụng trong kế hoạch dự án.

## 1. Phạm Vi Sử Dụng

- Quy mô khoảng **3.000 sinh viên**.
- UniSupport là **Web Application**, không phải mobile app độc lập.
- Giao diện hỗ trợ Tiếng Việt và Tiếng Anh ở mức cơ bản.
- Không tối ưu cho kiến trúc tải lớn vượt phạm vi dự án.

## 2. Tích Hợp Và Bảo Mật

- Không yêu cầu tích hợp bên thứ ba trong phạm vi hiện tại.
- Không bao gồm chat trực tiếp hoặc gọi thoại.
- Không yêu cầu chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

## 3. Hạ Tầng

- Hạ tầng máy chủ và tên miền do Aurora University cung cấp.
- Hiệu năng và độ ổn định phụ thuộc điều kiện hạ tầng Aurora University.
- Không bao gồm thiết lập sao lưu tự động, giám sát máy chủ và hỗ trợ hạ tầng lâu dài.

## 4. Phối Hợp

- Thời gian 14 tuần không bao gồm thời gian chờ phản hồi hoặc phê duyệt vượt quá kế hoạch phối hợp.
- Điều chỉnh phạm vi, chi phí hoặc tiến độ phải được hai bên xác nhận lại.

## 5. Dữ Liệu

- Môi trường phát triển, kiểm thử, UAT và trình diễn sử dụng **dữ liệu giả lập** có cấu trúc tương ứng dữ liệu của Aurora University: tài khoản, phòng ban, Nhóm vấn đề, FAQ, Ticket và file đính kèm.
- Không sử dụng dữ liệu cá nhân thật của sinh viên hoặc nhân viên.
- Bộ dữ liệu giả lập đáp ứng các kịch bản tại `06-acceptance/test-scenarios.md` và các chỉ tiêu tại `06-acceptance/success-metrics.md`.
