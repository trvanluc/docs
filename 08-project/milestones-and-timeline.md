# [PRJ-03] Tiến độ & Cột mốc thực hiện (Milestones & Timeline)

Tài liệu chi tiết hóa lộ trình triển khai dự án **UniSupport** qua 6 giai đoạn trong 14 tuần làm việc phát triển theo phương pháp **Vertical Slice (Feature-driven Development)**, giúp tích hợp và kiểm thử End-to-End (E2E) ngay trên từng luồng chức năng.

---

## 📅 1. Kế hoạch thực hiện theo Giai đoạn (Phases Schedule)

| Giai đoạn | Thời gian | Nội dung công việc chính (Vertical Slice Approach) | Sản phẩm đầu ra |
| :--- | :---: | :--- | :--- |
| **Giai đoạn 1: Thu thập yêu cầu** | Tuần 1–2 | Thu thập & phân tích nghiệp vụ, làm rõ quy trình Ticket, xác định phạm vi E2E và tiêu chí nghiệm thu từng Vertical Slice. | Tài liệu PRD, Wireframe/SRS hoàn chỉnh |
| **Giai đoạn 2: Thiết kế Kiến trúc & Nền tảng** | Tuần 3–4 | Thiết kế UI/UX System, Kiến trúc hệ thống, Database Schema cốt lõi, RBAC Security Base & Dựng Khung ứng dụng (FE/BE Boilerplate). | UI/UX Prototype, Architecture Docs, Base Source Code (FE + BE) |
| **Giai đoạn 3: Phát triển chính** | Tuần 5–9 | Phát triển 3 phân hệ đã chốt trong proposal: <br>• **Tuần 5–6 - Module Sinh viên:** Đăng nhập, gửi yêu cầu hỗ trợ, theo dõi trạng thái, nhận kết quả và đánh giá.<br>• **Tuần 7–8 - Module Nhân viên:** Tiếp nhận, phân loại, phân công, xử lý yêu cầu và cập nhật tiến độ.<br>• **Tuần 9 - Module Quản lý/Admin:** Thống kê, báo cáo, quản trị tài khoản và phân quyền. | Source code 3 phân hệ chính hoàn chỉnh có thể chạy & demo nội bộ |
| **Giai đoạn 4: Tích hợp hệ thống** | Tuần 10–11 | Tích hợp giao diện và backend, xây dựng dashboard/báo cáo, hoàn thiện thông báo nội bộ và kiểm tra phân quyền truy cập. | Hệ thống UniSupport tích hợp đầy đủ trên môi trường kiểm thử |
| **Giai đoạn 5: Kiểm thử & Nghiệm thu** | Tuần 12–13 | Kiểm thử chức năng, kiểm thử tích hợp, kiểm thử hồi quy, UAT với client và sửa lỗi thuộc phạm vi. | Báo cáo kiểm thử/UAT, danh sách lỗi và kết quả khắc phục |
| **Giai đoạn 6: Hoàn thiện & Bàn giao** | Tuần 14 | Sửa lỗi cuối, triển khai hệ thống, hoàn thiện tài liệu, mã nguồn và bàn giao chính thức. | Hệ thống triển khai, tài liệu bàn giao, biên bản bàn giao |

---

## 🚩 2. Các Cột mốc quan trọng (Key Milestones)

* **Mốc 0 (Tuần 1):** Ký hợp đồng hợp tác và đặt cọc triển khai dự án.
* **Mốc 1 (Cuối Tuần 2):** Chốt tài liệu Phạm vi & Yêu cầu nghiệp vụ (PRD).
* **Mốc 2 (Cuối Tuần 4):** Phê duyệt Thiết kế giao diện (UI/UX Prototype), Kiến trúc hệ thống và dựng xong Nền tảng dự án (Boilerplate).
* **Mốc 3 (Cuối Tuần 9):** Hoàn thành phát triển 3 phân hệ chính và demo nội bộ.
* **Mốc 4 (Tuần 13):** Hoàn thành UAT và tổng hợp kết quả phản hồi từ client.
* **Mốc 5 (Tuần 14):** Hoàn tất xử lý lỗi thuộc phạm vi, triển khai và bàn giao chính thức.

---

## 🏁 3. Quy trình Nghiệm thu & Bảo hành

### **3.1. Quy trình Nghiệm thu (10 ngày làm việc - Sau bàn giao chính thức)**
1. **Bàn giao chính thức (Cuối Tuần 14):** Đơn vị phát triển bàn giao phần mềm đã triển khai trên hạ tầng Production của Client và đầy đủ bộ tài liệu.
2. **Thực hiện nghiệm thu chính thức (10 ngày làm việc sau bàn giao):** Aurora University tiến hành kiểm thử chấp nhận người dùng theo kịch bản UAT đã thống nhất và chốt danh sách phản hồi. Thời gian này được tính sau thời điểm bàn giao, đúng theo proposal.
3. **Tiêu chí đạt nghiệm thu:**
   * Các luồng nghiệp vụ E2E (Sinh viên, Nhân viên, Quản lý) hoạt động chính xác theo kịch bản.
   * Phân quyền RBAC hoạt động chính xác theo vai trò trên từng chức năng.
   * Không còn lỗi nghiêm trọng (Blocker/Critical) gián đoạn chức năng chính.
   * Tài liệu bàn giao đầy đủ theo cam kết.

### **3.2. Chính sách Bảo hành (30 ngày)**
* **Thời hạn:** 30 ngày kể từ ngày ký biên bản nghiệm thu chính thức (sau khi hoàn tất 10 ngày UAT).
* **Phạm vi hỗ trợ:** Khắc phục miễn phí các lỗi kỹ thuật (Bugs) phát sinh do đội ngũ phát triển.
* **Lưu ý:** Không bao gồm việc thay đổi yêu cầu, thêm tính năng mới hoặc xử lý sự cố do hạ tầng máy chủ của Client gây ra.
