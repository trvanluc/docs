# 05 - Yêu Cầu Phi Chức Năng

Thư mục này xác định các thuộc tính chất lượng áp dụng chung cho UniSupport trong phạm vi ba phân hệ nghiệp vụ và quy mô khoảng 3.000 sinh viên.

## 1. Danh Sách Tài Liệu

| Tài liệu | Phạm vi |
| :--- | :--- |
| [performance.md](./performance.md) | Hiệu năng phù hợp quy mô sử dụng dự kiến. |
| [reliability.md](./reliability.md) | Tính ổn định và toàn vẹn dữ liệu nghiệp vụ. |
| [security.md](./security.md) | Xác thực, phân quyền, bảo vệ file và tra soát. |
| [usability.md](./usability.md) | Giao diện Web responsive và hỗ trợ Việt/Anh ở mức cơ bản. |
| [deployment.md](./deployment.md) | Điều kiện triển khai và bàn giao trên hạ tầng Aurora University. |
| [observability.md](./observability.md) | Nhật ký kỹ thuật và nhật ký tra soát nghiệp vụ. |

## 2. Nguyên Tắc Áp Dụng

- Các NFR áp dụng xuyên suốt M01, M02 và M03.
- Giới hạn file, trạng thái Ticket, quyền truy cập và Audit phải nhất quán với Domain và PRD.
- Các chỉ số tải lớn, chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu không thuộc phạm vi dự án hiện tại.
- Công nghệ triển khai cụ thể được mô tả tại `07-architecture`.
