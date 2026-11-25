# PRJ-01 - Giả Định Dự Án

Tài liệu này là **nơi gốc nội bộ** của các giả định vận hành và triển khai. Mỗi giả định có mã `A-xx`. Bộ hồ sơ gửi khách gồm [Proposal.docx](Proposal.docx), phần Assumptions, và [quotation.xlsx](quotation.xlsx), sheet `Giả định`, chứa bản sao đầy đủ cùng mã, nội dung, hạng mục bị ảnh hưởng và hệ quả khi giả định sai; khách không cần truy cập repo. Khi đổi giả định ảnh hưởng giá, người phụ trách đồng bộ cả hai bản gửi khách và ghi chung lịch sử ở sheet `Phiên bản` của báo giá trước khi gửi. Phần giả định gửi khách nằm ở [Proposal.docx](Proposal.docx) mục 2.4 "Assumptions (Giả định)".

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

- `A-11` Thời lượng dự thảo 108 ngày làm việc (07/12/2026–18/05/2027; 163 ngày lịch), gồm khởi động 10 ngày làm việc và 6 mốc không chồng nhau. Lịch task/vai trò giữ tối đa 4h/ngày, 20h/tuần/người; 885h = 823h cơ sở (gồm 26h bảo hành) + 22h dự phòng kỹ thuật + 40h dự phòng rủi ro được giữ năng lực, chưa sử dụng. Giả định nghỉ 01/01, 08–12/02, 16/04, 30/04, 01/05 và nghỉ bù 03/05/2027; lịch nghỉ trường chưa được xác nhận. Bàn giao dự kiến 18/05/2027; nghiệm thu mục tiêu 01/06/2027 sau 10 ngày làm việc; bảo hành 01/06/2027–30/06/2027 (30 ngày lịch gồm ngày xác nhận). Gửi đề xuất mục tiêu 30/11/2026, xác nhận mục tiêu 04/12, kickoff 07/12 có điều kiện. Chờ PM/TL và khách rà soát; đây không phải baseline, actual hoặc approval. Nếu lịch nghỉ/đầu vào/phạm vi thay đổi hoặc chờ phản hồi vượt kế hoạch phải tính lại, không tự cộng giờ ngoài báo giá.
- `A-12` Điều chỉnh phạm vi, chi phí hoặc tiến độ phải được hai bên xác nhận lại.
- `A-16` Cuối mỗi mốc `MS-xx`, client dùng thử bản staging và gửi phản hồi trong **02 ngày làm việc** sau buổi demo.

## 5. Dữ Liệu

- `A-13` Môi trường phát triển, kiểm thử, UAT và trình diễn sử dụng **dữ liệu giả lập** có cấu trúc tương ứng dữ liệu của Aurora University: tài khoản, phòng ban, Nhóm vấn đề, FAQ, Ticket và file đính kèm.
- `A-14` Không sử dụng dữ liệu cá nhân thật của sinh viên hoặc nhân viên.
- `A-15` Bộ dữ liệu giả lập đáp ứng các kịch bản tại `06-acceptance/test-scenarios.md` và các chỉ tiêu tại `06-acceptance/success-metrics.md`.

## 6. Tính Chất Mô Phỏng

- `A-17` Đội thực thi 10 vai trò, Aurora University (client), Nhà tài trợ dự án, feedback, change request và số liệu báo cáo là `Mô phỏng`; 4 thành viên nhóm là ban quản lý dự án thật (xem [Team Charter](team-charter.md)).
