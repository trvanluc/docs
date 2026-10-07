# [PRJ-01] Các Giả định Dự án (Project Assumptions)

Tài liệu này xác định các giả định nền tảng về phạm vi, kỹ thuật, hạ tầng và vận hành đối với dự án **UniSupport** tại **Aurora University**. Các giả định này làm căn cứ để ước tính chi phí, phân bổ nguồn lực (618h cơ sở + 22h dự phòng = 640h kế hoạch), lập kế hoạch tiến độ 14 tuần và xác định tiêu chí nghiệm thu.

---

## 1. Giả định về Quy mô & Phạm vi Sử dụng (Scope & Scale)

* **Quy mô người dùng:** Hệ thống được thiết kế và tối ưu cho quy mô khoảng **3.000 sinh viên** cùng đội ngũ Nhân viên hỗ trợ và Quản lý các phòng ban.
* **Không tối ưu tải lớn:** Hệ thống không thiết kế cho kiến trúc chịu tải cực lớn (High Concurrency / Auto-scaling) hoặc tính năng giật ca/đăng ký tín chỉ đồng thời hàng loạt.
* **Loại ứng dụng:** Hệ thống là **Web Application** chạy trên trình duyệt web (hỗ trợ Responsive cho Máy tính và Thiết bị di động). Không phát triển Mobile App độc lập (iOS/Android).
* **Đa ngôn ngữ:** Giao diện người dùng hỗ trợ **Tiếng Việt** (mặc định) và **Tiếng Anh** ở mức cơ bản.

---

## 2. Giả định về Kỹ thuật & Tích hợp (Technical & Integration)

* **Không tích hợp hệ thống bên thứ ba:** Hệ thống vận hành độc lập, không yêu cầu tích hợp với các hệ thống bên thứ ba ngoài phạm vi đã thỏa thuận (như SSO/LDAP, LMS Canvas/Moodle, Core ERP hay Cổng thanh toán).
* **Xác thực người dùng:** Hệ thống tự quản lý tài khoản, mật khẩu và xác thực người dùng trực tiếp qua Cơ sở dữ liệu nội bộ của UniSupport.
* **Không hỗ trợ trao đổi thời gian thực:** Hệ thống không bao gồm các chức năng Chat trực tiếp (Live Chat), Gọi thoại/Video call nội bộ. Mọi tương tác diễn ra thông qua luồng trao đổi trên Ticket và Yêu cầu bổ sung hồ sơ.
* **Gửi thông báo:** Hệ thống tập trung vào thông báo nội bộ trong ứng dụng (In-app Notifications).

---

## 3. Giả định về Hạ tầng & Vận hành (Infrastructure & Operations)

* **Hạ tầng máy chủ:** Toàn bộ máy chủ (Server/Cloud), tên miền (Domain), chứng chỉ SSL và môi trường lưu trữ do **Aurora University cung cấp** đúng thời hạn.
* **Phụ thuộc hạ tầng:** Hiệu năng, độ tin cậy và tính ổn định của hệ thống phụ thuộc hoàn toàn vào chất lượng hạ tầng mạng và máy chủ của Client.
* **Bảo trì & Sao lưu:** Đơn vị phát triển không chịu trách nhiệm thiết lập sao lưu tự động (Auto-backup), theo dõi vận hành máy chủ lâu dài hay hỗ trợ hạ tầng sau khi kết thúc thời gian bảo hành.
* **Đánh giá an toàn thông tin:** Dự án không bao gồm yêu cầu đánh giá an ninh mạng chuyên sâu (Penetration Testing) hoặc các chứng nhận bảo mật quốc tế.

---

## 4. Giả định về Quản lý Dự án & Phối hợp (Project Management)

* **Thời gian chờ phê duyệt:** Tổng thời gian 14 tuần phát triển **chưa bao gồm** thời gian chờ phản hồi, rà soát hoặc phê duyệt tài liệu/giao diện từ phía Aurora University. Nếu có phát sinh chậm trễ phản hồi, tiến độ dự án sẽ được điều chỉnh tương ứng.
* **Tiêu chuẩn kiểm thử UAT:** Việc kiểm thử chấp nhận (UAT) kéo dài **10 ngày làm việc** được tính sau khi hoàn tất bàn giao chính thức. Các lỗi nhỏ không làm gián đoạn chức năng cốt lõi sẽ không được tính là điều kiện từ chối nghiệm thu.
* **Chính sách bảo hành:** Bảo hành sửa lỗi kỹ thuật miễn phí trong **30 ngày** kể từ ngày ký biên bản nghiệm thu. Không áp dụng cho việc thay đổi quy trình nghiệp vụ hoặc yêu cầu tính năng mới ngoài scope.