# NFR-OBS - Ghi Log Và Tra Soát

## 1. Phạm Vi

Tách biệt hai mục đích:
- **Nhật ký kỹ thuật:** hỗ trợ đội phát triển chẩn đoán lỗi trong quá trình triển khai/bảo hành.
- **Nhật ký tra soát nghiệp vụ:** ghi các hành động quan trọng theo M03 và `BR-AUD`.

## 2. Yêu Cầu

### 2.1 Nhật ký kỹ thuật
- Ghi đủ thông tin để xác định thời điểm, mức độ lỗi và khu vực chức năng liên quan.
- Không ghi mật khẩu hoặc nội dung bí mật ở dạng có thể đọc trực tiếp.
- Cách lưu, định dạng và thời hạn log kỹ thuật là quyết định triển khai, không phải cam kết nghiệp vụ.

### 2.2 Nhật ký tra soát nghiệp vụ
Tối thiểu bao gồm các sự kiện được quy định trong PRD:
- thay đổi trạng thái Ticket;
- phân công/phân công lại;
- thay đổi mức độ ưu tiên/thời hạn;
- Transfer và Escalation;
- ghi nhận kết quả, mở lại và đóng Ticket;
- tạo/thay đổi/khóa tài khoản và quyền;
- thay đổi phòng ban, Category và chính sách lưu trữ.

## 3. Nghiệm Thu

- Các sự kiện Audit bắt buộc có bản ghi tương ứng.
- Management chỉ xem nhật ký trong phạm vi quyền.
- Nhật ký Audit không thể sửa/xóa bằng chức năng thông thường của ứng dụng.
