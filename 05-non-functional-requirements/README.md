# 05-non-functional-requirements: Yêu cầu Phi chức năng UniSupport

Thư mục này tập hợp toàn bộ các tài liệu chuẩn hóa về **Yêu cầu Phi chức năng (Non-Functional Requirements - NFR)** của hệ thống UniSupport tại Aurora University. Các yêu cầu này đóng vai trò làm khung tiêu chuẩn cho thiết kế kiến trúc, phát triển phần mềm và làm tiêu chí nghiệm thu kỹ thuật.

---

## Danh sách Yêu cầu Phi chức năng

| Mã Tài liệu | Tên Yêu cầu | Phạm vi chính |
| :--- | :--- | :--- |
| **[performance.md](./performance.md)** | Yêu cầu Hiệu năng | Tối ưu cho quy mô 3.000 sinh viên, thời gian phản hồi API $\le 500$ms, dung lượng tệp tối đa 10 MB. |
| **[security.md](./security.md)** | Yêu cầu Bảo mật | Phân quyền RBAC 3 vai trò, mã hóa mật khẩu, bảo mật đường dẫn tệp đính kèm và Audit log. |
| **[reliability.md](./reliability.md)** | Yêu cầu Độ ổn định | Độ sẵn sàng $\ge 98.5\%$, đảm bảo toàn vẹn giao dịch (ACID), xử lý lỗi thân thiện. |
| **[usability.md](./usability.md)** | Yêu cầu Tính dễ dùng | Giao diện Responsive (PC/Mobile), hỗ trợ 2 ngôn ngữ (Việt/Anh), màu sắc trạng thái trực quan. |
| **[observability.md](./observability.md)** | Yêu cầu Giám sát & Log | Cấu trúc log JSON (`INFO`/`WARN`/`ERROR`), log tra soát thao tác và API Health check. |
| **[deployment.md](./deployment.md)** | Yêu cầu Triển khai | Đóng gói Docker, triển khai trên tên miền và máy chủ do Aurora University cung cấp. |

---

## Nguyên tắc áp dụng & Giới hạn phạm vi
- **Bám sát Scope & Assumptions:** Các chỉ số NFR được thiết kế vừa đặn cho quy mô 3.000 sinh viên của Aurora University, không phình to kiến trúc vô lý.
- **Cơ sở Kiểm thử UAT:** Các mục tiêu NFR đi kèm tiêu chí nghiệm thu rõ ràng (`NFR-xxx-01`), làm căn cứ đánh giá chất lượng trong giai đoạn kiểm thử 10 ngày nghiệm thu của nhà trường.