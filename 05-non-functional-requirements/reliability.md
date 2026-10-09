# [NFR-REL] Yêu cầu về Độ ổn định & Tin cậy (Reliability Requirements)

### 1. Tổng quan
Tài liệu định nghĩa các chỉ số và quy tắc nhằm đảm bảo hệ thống UniSupport duy trì trạng thái hoạt động ổn định và nhất quán trên hạ tầng do Aurora University cung cấp.

### 2. Chỉ số sẵn sàng & Tin cậy

| Chỉ số | Yêu cầu | Ghi chú |
| :--- | :--- | :--- |
| **Mức độ sẵn sàng (Availability)** | $\ge 98.5\%$ | Trong thời gian hoạt động hành chính của nhà trường |
| **Toàn vẹn dữ liệu (Data Integrity)** | 100% | Không xảy ra mất mát dữ liệu Ticket trong điều kiện vận hành bình thường |
| **Xử lý sự cố lỗi (Graceful Degradation)** | Hiển thị thông báo lỗi thân thiện | Không để lộ lỗi hệ thống (Stack trace/Code error) cho người dùng cuối |

### 3. Toàn vẹn giao dịch & Khôi phục
- **Đảm bảo giao dịch (Database Transaction):** Thao tác gửi Ticket bao gồm thông tin văn bản và lưu tệp đính kèm phải tuân thủ nguyên tắc All-or-Nothing (ACID). Nếu lưu tệp thất bại, thông tin Ticket sẽ không được tạo để tránh dữ liệu mống/rác.
- **Hạ tầng & Sao lưu:** Tính ổn định, tên miền, chứng chỉ SSL và sao lưu dữ liệu máy chủ hoàn toàn phụ thuộc vào hạ tầng do Aurora University cung cấp (nằm ngoài phạm vi bảo trì dài hạn của nhà phát triển).

### 4. Tiêu chí Kiểm thử & Nghiệm thu
- **NFR-REL-01:** Khi xảy ra lỗi kết nối mạng trong quá trình gửi Ticket, hệ thống hủy giao dịch và không lưu Ticket ở trạng thái dở dang (dữ liệu không hoàn chỉnh).
- **NFR-REL-02:** Giao diện người dùng hiển thị thông điệp lỗi rõ ràng (ví dụ: "Có lỗi xảy ra, vui lòng thử lại sau") thay vì lộ mã lỗi lập trình (Stack trace).