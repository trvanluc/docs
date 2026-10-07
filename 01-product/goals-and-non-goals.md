# Mục tiêu và ngoài phạm vi

## 1. Mục tiêu cốt lõi

| ID | Mục tiêu | Cách đánh giá | Trạng thái |
| :--- | :--- | :--- | :--- |
| **G-01** | Tập trung hóa các yêu cầu hỗ trợ trực tuyến của sinh viên vào UniSupport. | Sinh viên có thể tạo Ticket và nhận mã Ticket để theo dõi. | Baseline |
| **G-02** | Minh bạch hóa tiến độ xử lý. | Sinh viên xem được trạng thái mới nhất, lịch sử cập nhật và kết quả xử lý của Ticket của mình. | Baseline |
| **G-03** | Hỗ trợ quy trình vận hành phòng ban. | Staff xem được Ticket mới/được giao, phân loại, chuyển xử lý, yêu cầu bổ sung, cập nhật kết quả và đóng Ticket. | Baseline |
| **G-04** | Hỗ trợ giám sát quản lý. | Management xem được dashboard, workload, xu hướng vấn đề, thời gian xử lý trung bình và feedback sinh viên. | Baseline |
| **G-05** | Đảm bảo truy cập đúng phạm vi. | User phải login; role-based access được áp dụng; file chỉ người liên quan xem được; thao tác quan trọng được lưu lịch sử. | Baseline |

## 2. Ngoài phạm vi

| ID | Hạng mục ngoài phạm vi | Ghi chú |
| :--- | :--- | :--- |
| **NG-01** | Mobile app độc lập iOS/Android | Chỉ triển khai Web Application responsive. |
| **NG-02** | Tích hợp bên thứ ba ngoài phạm vi | Không tích hợp LMS/ERP/SSO/CRM nếu chưa có thỏa thuận mới. |
| **NG-03** | Live chat / VoIP | Trao đổi nằm trong Ticket và thông báo nội bộ. |
| **NG-04** | Advanced audit / advanced security certification | Không bao gồm audit nâng cao, pentest chuyên sâu hoặc chứng nhận bảo mật quốc tế. |
| **NG-05** | Kiến trúc chịu tải lớn vượt quy mô 3.000 sinh viên | Không thiết kế microservices/load balancing phức tạp cho quy mô lớn hơn scope. |
| **NG-06** | Long-term infrastructure support / auto backup nâng cao | Hạ tầng, backup dài hạn và vận hành server lâu dài thuộc trách nhiệm client nếu không có hợp đồng riêng. |

## 3. Nguyên tắc tránh mở rộng scope

- Không biến dòng effort nội bộ thành baseline nếu proposal không hỗ trợ trực tiếp.
- Không chốt con số kỹ thuật như SLA cụ thể, dung lượng file, số lượng file, retention hoặc response time nếu chưa có nguồn xác nhận.
- Chi tiết cần thiết để Dev triển khai baseline được ghi **Derived**.
- Hạng mục đề xuất nội bộ hoặc cần xác nhận thêm được ghi **Proposed** hoặc **TBD**.
