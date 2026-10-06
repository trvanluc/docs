# [PRJ-01] Các Giả định Dự án (Project Assumptions)

Tài liệu này xác định các giả định nền tảng về phạm vi, kỹ thuật, hạ tầng và vận hành đối với dự án **UniSupport** tại **Aurora University**. Các giả định này làm căn cứ để ước tính chi phí, lập kế hoạch tiến độ 14 tuần và xác định tiêu chí nghiệm thu.

---

## 🎯 1. Giả định về Quy mô & Phạm vi Sử dụng (Scope & Scale Assumptions)

* **Quy mô người dùng:** Hệ thống được thiết kế và tối ưu cho quy mô khoảng **3.000 sinh viên** cùng đội ngũ Nhân viên hỗ trợ và Quản lý các phòng ban[cite: 1].
* **Không tối ưu tải lớn:** Hệ thống không thiết kế cho kiến trúc chịu tải cực lớn (High Concurrency / Auto-scaling) hoặc tính năng giật ca/đăng ký tín chỉ đồng thời hàng loạt[cite: 1].
* **Loại ứng dụng:** Hệ thống là **Web Application** chạy trên trình duyệt web (hỗ trợ Responsive cho Máy tính và Thiết bị di động)[cite: 1]. Không phát triển Mobile App độc lập (iOS/Android)[cite: 1].
* **Đa ngôn ngữ:** Giao diện người dùng hỗ trợ **Tiếng Việt** (mặc định) và **Tiếng Anh** ở mức cơ bản[cite: 1].

---

## ⚙️ 2. Giả định về Kỹ thuật & Tích hợp (Technical & Integration Assumptions)

* **Không tích hợp hệ thống bên thứ ba:** Hệ thống vận hành độc lập, không yêu cầu tích hợp với các hệ thống bên thứ ba ngoài phạm vi đã thỏa thuận (như SSO/LDAP, LMS Canvas/Moodle, Core ERP hay Cổng thanh toán)[cite: 1].
* **Xác thực người dùng:** Hệ thống tự quản lý tài khoản, mật khẩu và xác thực người dùng trực tiếp qua Cơ sở dữ liệu nội bộ của UniSupport[cite: 1].
* **Không hỗ trợ trao đổi thời gian thực:** Hệ thống không bao gồm các chức năng Chat trực tiếp (Live Chat), Gọi thoại/Video call nội bộ[cite: 1]. Mọi tương tác diễn ra thông qua luồng trao đổi trên Ticket và Yêu cầu bổ sung hồ sơ[cite: 1].
* **Gửi thông báo:** Hệ thống tập trung vào thông báo nội bộ trong ứng dụng (In-app Notifications)[cite: 1].

---

## 🏗️ 3. Giả định về Hạ tầng & Vận hành (Infrastructure & Operations Assumptions)

* **Hạ tầng máy chủ:** Toàn bộ máy chủ (Server/Cloud), tên miền (Domain), chứng chỉ SSL và môi trường lưu trữ do **Aurora University cung cấp** đúng thời hạn[cite: 1].
* **Phụ thuộc hạ tầng:** Hiệu năng, độ tin cậy và tính ổn định của hệ thống phụ thuộc hoàn toàn vào chất lượng hạ tầng mạng và máy chủ của Client[cite: 1].
* **Bảo trì & Sao lưu:** Đơn vị phát triển không chịu trách nhiệm thiết lập sao lưu tự động (Auto-backup), theo dõi vận hành máy chủ lâu dài hay hỗ trợ hạ tầng sau khi kết thúc thời gian bảo hành[cite: 1].
* **Đánh giá an toàn thông tin:** Dự án không bao gồm yêu cầu đánh giá an ninh mạng chuyên sâu (Penetration Testing) hoặc các chứng nhận bảo mật quốc tế[cite: 1].

---

## 👥 4. Giả định về Quản lý Dự án & Phối hợp (Project Management Assumptions)

* **Thời gian chờ phê duyệt:** Tổng thời gian 14 tuần phát triển **chưa bao gồm** thời gian chờ phản hồi, rà soát hoặc phê duyệt tài liệu/giao diện từ phía Aurora University[cite: 1]. Nếu có phát sinh chậm trễ phản hồi, tiến độ dự án sẽ được điều chỉnh tương ứng[cite: 1].
* **Tiêu chuẩn kiểm thử UAT:** Việc kiểm thử chấp nhận (UAT) kéo dài **10 ngày làm việc** được tính sau khi hoàn tất bàn giao chính thức[cite: 1]. Các lỗi nhỏ không làm gián đoạn chức năng cốt lõi sẽ không được tính là điều kiện từ chối nghiệm thu[cite: 1].
* **Chính sách bảo hành:** Bảo hành sửa lỗi kỹ thuật miễn phí trong **30 ngày** kể từ ngày ký biên bản nghiệm thu[cite: 1]. Không áp dụng cho việc thay đổi quy trình nghiệp vụ hoặc yêu cầu tính năng mới ngoài scope[cite: 1].