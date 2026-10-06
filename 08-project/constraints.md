# [PRJ-02] Ràng buộc Dự án (Project Constraints)

Tài liệu này xác định các giới hạn và ràng buộc cố định về thời gian, ngân sách, hạ tầng kỹ thuật và nhân lực đối với dự án **UniSupport**.

---

## ⏱️ 1. Ràng buộc về Thời gian (Time Constraints)

* **Tổng thời gian thực hiện:** **14 tuần** (tương đương khoảng **70 ngày làm việc**), tính từ ngày khởi động chính thức đến khi hoàn tất bàn giao.
* **Quy trình nghiệm thu:** Sau khi bàn giao, Aurora University có **10 ngày làm việc** để tiến hành kiểm thử UAT và nghiệm thu chính thức (không tính gộp vào 14 tuần phát triển).
* **Điều chỉnh tiến độ:** Thời gian chờ phản hồi, xác nhận hoặc cung cấp thông tin/hạ tầng từ phía Client vượt quá thỏa thuận sẽ được cộng tương ứng vào tiến độ chung của dự án.

---

## 💰 2. Ràng buộc về Chi phí & Ngân sách (Budget Constraints)

* **Tổng kinh phí cố định:** **300.000.000 VNĐ** (Ba trăm triệu đồng chẵn).
* **Phạm vi bảo hành:** Chi phí bảo hành miễn phí trong **30 ngày** kể từ ngày nghiệm thu chỉ áp dụng cho việc sửa lỗi kỹ thuật phát sinh từ đội ngũ phát triển.
* **Thay đổi phạm vi (Change Request):** Mọi yêu cầu phát sinh thêm tính năng hoặc thay đổi phạm vi ngoài thỏa thuận ban đầu sẽ được đánh giá tác động và chi phí bổ sung bằng văn bản riêng.

---

## 🛠️ 3. Ràng buộc Kỹ thuật & Hạ tầng (Technical Constraints)

* **Hạ tầng triển khai:** Hệ thống hoàn toàn phụ thuộc vào Server, tên miền và môi trường mạng do Aurora University cung cấp.
* **Quy mô hệ thống:** Tối ưu cho khoảng **3.000 sinh viên**; không thiết kế chịu tải lớn (Load balancing / Auto-scaling) hoặc kiến trúc phân tán phức tạp.
* **Loại ứng dụng:** Chỉ triển khai dưới dạng **Web Application** (Responsive UI cho máy tính và thiết bị di động), không phát triển Mobile App độc lập (iOS/Android).
* **Tích hợp:** Không tích hợp hệ thống bên thứ ba (SSO, CRM, LMS...) ngoài phạm vi đã xác định trong PRD.
* **Bảo mật:** Không bao gồm các yêu cầu chứng nhận bảo mật quốc tế (ISO, PCI-DSS) hoặc đánh giá an ninh mạng chuyên sâu (Penetration Testing).

---

## 👥 4. Ràng buộc về Nhân sự & Giao tiếp (Resource & Communication Constraints)

* **Đầu mối liên lạc:** Mỗi bên chỉ định 01 Quản lý dự án (PM) làm đầu mối chính để trao đổi và phê duyệt tài liệu/kết quả.
* **Hình thức phê duyệt:** Mọi điều chỉnh về phạm vi, ngân sách hoặc thời gian đều phải được xác nhận chính thức bằng văn bản hoặc email từ người có thẩm quyền.