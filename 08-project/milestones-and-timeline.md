# [PRJ-03] Tiến độ & Cột mốc thực hiện (Milestones & Timeline)

Tài liệu chi tiết hóa lộ trình triển khai dự án **UniSupport** qua 6 giai đoạn trong 14 tuần làm việc và các cột mốc bàn giao/nghiệm thu quan trọng.

---

## 📅 1. Kế hoạch thực hiện theo Giai đoạn (Phases Schedule)

| Giai đoạn | Thời gian | Nội dung công việc chính | Sản phẩm đầu ra |
| :--- | :---: | :--- | :--- |
| **Giai đoạn 1: Thu thập yêu cầu** | Tuần 1–2 | Thu thập & phân tích nghiệp vụ, làm rõ quy trình Ticket, xác định phạm vi và tiêu chí nghiệm thu. | Tài liệu PRD, Wireframe/SRS hoàn chỉnh |
| **Giai đoạn 2: Thiết kế** | Tuần 3–4 | Thiết kế UI/UX, Prototype, kiến trúc hệ thống, Database Schema (ERD), RESTful API và RBAC. | UI Prototype, Design System, Architecture Docs |
| **Giai đoạn 3: Phát triển chính** | Tuần 5–9 | Lập trình các phân hệ chính: <br>• **Tuần 5–6:** Module Sinh viên (M01)<br>• **Tuần 7–8:** Module Nhân viên (M02)<br>• **Tuần 9:** Module Quản lý (M03) | Source code các Module M01, M02, M03 |
| **Giai đoạn 4: Tích hợp hệ thống** | Tuần 10–11 | Tích hợp Frontend & Backend, xây dựng Dashboard báo cáo, Notification Service và đóng gói RBAC Security. | Hệ thống UniSupport chạy tích hợp nội bộ |
| **Giai đoạn 5: Kiểm thử & UAT** | Tuần 12–13 | Kiểm thử chức năng, kiểm thử tích hợp, kiểm thử hồi quy, phối hợp Client thực hiện UAT và sửa lỗi. | Báo cáo test case, biên bản UAT thành công |
| **Giai đoạn 6: Hoàn thiện & Bàn giao** | Tuần 14 | Sửa lỗi cuối cùng, đóng gói source code, triển khai lên Server Client, bàn giao tài liệu và hướng dẫn. | Hệ thống chạy Production, Tài liệu bàn giao |

---

## 🚩 2. Các Cột mốc quan trọng (Key Milestones)

* **Mốc 0 (Tuần 1):** Ký hợp đồng hợp tác và đặt cọc triển khai dự án.
* **Mốc 1 (Cuối Tuần 2):** Chốt tài liệu Phạm vi & Yêu cầu nghiệp vụ (PRD).
* **Mốc 2 (Cuối Tuần 4):** Phê duyệt Thiết kế giao diện (UI/UX Prototype) & Kiến trúc hệ thống.
* **Mốc 3 (Cuối Tuần 9):** Hoàn thành phát triển 3 phân hệ cốt lõi & Demo nội bộ.
* **Mốc 4 (Tuần 13):** Hoàn thành đợt kiểm thử UAT với Aurora University và chốt danh sách phản hồi.
* **Mốc 5 (Tuần 14):** Khắc phục toàn bộ lỗi UAT, triển khai chính thức và bàn giao toàn bộ tài liệu/mã nguồn.

---

## 🏁 3. Quy trình Nghiệm thu & Bảo hành

### **3.1. Quy trình Nghiệm thu (10 ngày làm việc)**
1. **Bàn giao chính thức:** Đơn vị phát triển bàn giao phần mềm đã triển khai trên hạ tầng Client và đầy đủ bộ tài liệu.
2. **Thực hiện kiểm thử:** Aurora University có **10 ngày làm việc** để kiểm thử hệ thống dựa trên kịch bản UAT.
3. **Tiêu chí đạt nghiệm thu:**
   * Các luồng chính của 3 phân hệ hoạt động đúng mô tả.
   * Phân quyền RBAC hoạt động chính xác theo vai trò.
   * Không còn lỗi nghiêm trọng (Blocker/Critical) gián đoạn chức năng chính.
   * Tài liệu bàn giao đầy đủ theo cam kết.

### **3.2. Chính sách Bảo hành (30 ngày)**
* **Thời hạn:** 30 ngày kể từ ngày ký biên bản nghiệm thu chính thức.
* **Phạm vi hỗ trợ:** Khắc phục miễn phí các lỗi kỹ thuật (Bugs) phát sinh do đội ngũ phát triển.
* **Lưu ý:** Không bao gồm việc thay đổi yêu cầu, thêm tính năng mới hoặc xử lý sự cố do hạ tầng máy chủ của Client gây ra.