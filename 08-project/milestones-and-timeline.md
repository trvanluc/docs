# [PRJ-03] Tiến độ & Cột mốc thực hiện (Milestones & Timeline)

Tài liệu chi tiết hóa lộ trình triển khai dự án **UniSupport** qua 6 giai đoạn trong 14 tuần làm việc phát triển theo phương pháp **Vertical Slice (Feature-driven Development)**, giúp tích hợp và kiểm thử End-to-End (E2E) ngay trên từng luồng chức năng.

---

## 📅 1. Kế hoạch thực hiện theo Giai đoạn (Phases Schedule)

| Giai đoạn | Thời gian | Nội dung công việc chính (Vertical Slice Approach) | Sản phẩm đầu ra |
| :--- | :---: | :--- | :--- |
| **Giai đoạn 1: Thu thập yêu cầu** | Tuần 1–2 | Thu thập & phân tích nghiệp vụ, làm rõ quy trình Ticket, xác định phạm vi E2E và tiêu chí nghiệm thu từng Vertical Slice. | Tài liệu PRD, Wireframe/SRS hoàn chỉnh |
| **Giai đoạn 2: Thiết kế Kiến trúc & Nền tảng** | Tuần 3–4 | Thiết kế UI/UX System, Kiến trúc hệ thống, Database Schema cốt lõi, RBAC Security Base & Dựng Khung ứng dụng (FE/BE Boilerplate). | UI/UX Prototype, Architecture Docs, Base Source Code (FE + BE) |
| **Giai đoạn 3: Phát triển theo Vertical Slice (Feature Slices)** | Tuần 5–9 | Phát triển trọn gói End-to-End (DB + BE API + FE UI + Auto/Manual Test) cho từng luồng nghiệp vụ: <br>• **Tuần 5–6 (Slice 1 - Luồng Sinh viên):** Đăng nhập RBAC, Tạo ticket, Theo dõi & Đánh giá trạng thái Ticket.<br>• **Tuần 7–8 (Slice 2 - Luồng Nhân viên):** Tiếp nhận ticket, Xử lý/Phân công, Phản hồi & Đóng ticket E2E.<br>• **Tuần 9 (Slice 3 - Luồng Quản lý):** Dashboard báo cáo, Thống kê SLA, Quản lý danh mục & Cấu hình hệ thống. | Source code các Feature Slices 1, 2, 3 hoàn chỉnh có thể chạy & demo E2E |
| **Giai đoạn 4: Tích hợp Cross-Slice & Testing Chuyên sâu** | Tuần 10–12 | Tích hợp liên luồng (Cross-Slice Integration), Hoàn thiện Notification Service, Kiểm thử bảo mật RBAC, Kiểm thử hiệu năng (Load Test) và Kiểm thử hồi quy toàn hệ thống (Regression Testing). | Hệ thống UniSupport hoàn chỉnh & Báo cáo kiểm thử nội bộ (Internal QA/QC) |
| **Giai đoạn 5: Hoàn thiện & Triển khai Staging** | Tuần 13 | Sửa lỗi nội bộ, tối ưu hóa truy vấn DB/API, đóng gói Docker/CI-CD và triển khai hệ thống lên môi trường Staging/Pre-production của Client. | Môi trường Staging hoàn thiện sẵn sàng cho UAT |
| **Giai đoạn 6: Bàn giao & Triển khai Production** | Tuần 14 | Triển khai chính thức lên môi trường Production của Client, bàn giao toàn bộ tài liệu hướng dẫn và mã nguồn để bắt đầu giai đoạn UAT. | Hệ thống running Production, Biên bản bàn giao |

---

## 🚩 2. Các Cột mốc quan trọng (Key Milestones)

* **Mốc 0 (Tuần 1):** Ký hợp đồng hợp tác và đặt cọc triển khai dự án.
* **Mốc 1 (Cuối Tuần 2):** Chốt tài liệu Phạm vi & Yêu cầu nghiệp vụ (PRD).
* **Mốc 2 (Cuối Tuần 4):** Phê duyệt Thiết kế giao diện (UI/UX Prototype), Kiến trúc hệ thống và dựng xong Nền tảng dự án (Boilerplate).
* **Mốc 3 (Cuối Tuần 9):** Hoàn thành phát triển 3 luồng nghiệp vụ cốt lõi (Vertical Slices) & Demo E2E nội bộ từng luồng.
* **Mốc 4 (Cuối Tuần 12):** Hoàn thành tích hợp Cross-slice và kết thúc đợt kiểm thử nội bộ (Internal QA/QC).
* **Mốc 5 (Cuối Tuần 14):** Bàn giao chính thức hệ thống Production, tài liệu và mã nguồn; bắt đầu thời gian 10 ngày kiểm thử UAT cùng Aurora University.

---

## 🏁 3. Quy trình Nghiệm thu & Bảo hành

### **3.1. Quy trình Nghiệm thu (10 ngày làm việc - Sau 14 tuần phát triển)**
1. **Bàn giao chính thức (Cuối Tuần 14):** Đơn vị phát triển bàn giao phần mềm đã triển khai trên hạ tầng Production của Client và đầy đủ bộ tài liệu.
2. **Thực hiện kiểm thử UAT (10 ngày làm việc / Tuần 15–16):** Aurora University tiến hành kiểm thử chấp nhận người dùng dựa trên kịch bản UAT E2E và chốt danh sách phản hồi. Đội ngũ phát triển phối hợp hỗ trợ và khắc phục các lỗi phát sinh trong thời gian này.
3. **Tiêu chí đạt nghiệm thu:**
   * Các luồng nghiệp vụ E2E (Sinh viên, Nhân viên, Quản lý) hoạt động chính xác theo kịch bản.
   * Phân quyền RBAC hoạt động chính xác theo vai trò trên từng chức năng.
   * Không còn lỗi nghiêm trọng (Blocker/Critical) gián đoạn chức năng chính.
   * Tài liệu bàn giao đầy đủ theo cam kết.

### **3.2. Chính sách Bảo hành (30 ngày)**
* **Thời hạn:** 30 ngày kể từ ngày ký biên bản nghiệm thu chính thức (sau khi hoàn tất 10 ngày UAT).
* **Phạm vi hỗ trợ:** Khắc phục miễn phí các lỗi kỹ thuật (Bugs) phát sinh do đội ngũ phát triển.
* **Lưu ý:** Không bao gồm việc thay đổi yêu cầu, thêm tính năng mới hoặc xử lý sự cố do hạ tầng máy chủ của Client gây ra.