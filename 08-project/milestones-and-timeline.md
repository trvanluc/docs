# [PRJ-03] Tiến độ & Cột mốc thực hiện (Milestones & Timeline)

Tài liệu chi tiết hóa lộ trình triển khai dự án **UniSupport** qua 6 giai đoạn trong 14 tuần làm việc phát triển theo phương pháp **Vertical Slice (Feature-driven Development)**, với tổng công sức **618h cơ sở + 22h dự phòng = 640h kế hoạch**.

---

## 1. Kế hoạch thực hiện theo Giai đoạn (Phases Schedule)

| Giai đoạn | Thời gian | Nội dung công việc chính (Vertical Slice) | Sản phẩm đầu ra | Phân bổ Nhân sự |
| :--- | :---: | :--- | :--- | :--- |
| **Giai đoạn 1: Thu thập yêu cầu** | Tuần 1–2 | Phân tích nghiệp vụ, làm rõ quy trình Ticket, xác định phạm vi E2E và tiêu chí nghiệm thu. | PRD, SRS hoàn chỉnh, Baseline Resource Sheet | PM (15h), BA (30h), TL (5h) |
| **Giai đoạn 2: Thiết kế Kiến trúc & Nền tảng** | Tuần 3–4 | Thiết kế UI/UX Design System, Database Schema, RBAC Security Base & Dựng Boilerplate (FE/BE). | UI/UX Prototype, Architecture Docs, Base Boilerplate | BA (15h), UI/UX (27h), TL (10h), FE1/2 (20h), BE1/2 (20h), DevOps (10h) |
| **Giai đoạn 3: Phát triển theo Vertical Slice** | Tuần 5–9 | Phát triển End-to-End cho 3 Phân hệ:<br>• **Tuần 5–6 (Slice 1 - M1 Sinh viên):** FAQ, Tạo ticket, Theo dõi, Thông báo & Đánh giá (128h).<br>• **Tuần 7–8 (Slice 2 - M2 Nhân viên):** Hòm thư, Claim, SLA, Xử lý & Chuyển phòng ban (197h).<br>• **Tuần 9 (Slice 3 - M3 Quản lý/Admin):** RBAC, Danh mục, Audit Trail, Dashboard & Báo cáo (215h). | Source code 3 Feature Slices hoàn chỉnh chạy E2E | BA (18h), TL (12h), FE1 (36h), FE2 (41h), BE1 (65h), BE2 (40h), QA (45h) |
| **Giai đoạn 4: Tích hợp Cross-Slice & Testing** | Tuần 10–12 | Tích hợp liên luồng, Notification Service, kiểm thử bảo mật RBAC, Load Test và Regression Test. | Hệ thống UniSupport hoàn chỉnh & Báo cáo QA/QC | TL (4h), FE1/2 (20h), BE1/2 (22h), QA (45h), PM (20h) |
| **Giai đoạn 5: Hoàn thiện & Triển khai Staging** | Tuần 13 | Sửa lỗi nội bộ, tối ưu truy vấn DB/API, đóng gói Docker/CI-CD và triển khai lên Staging của Client. | Môi trường Staging hoàn thiện cho UAT | DevOps (10h), QA (8h), BE1/2 (10h) |
| **Giai đoạn 6: Bàn giao & Triển khai Production** | Tuần 14 | Triển khai chính thức lên Production của Aurora University, bàn giao tài liệu và mã nguồn. | Hệ thống running Production, Biên bản bàn giao | PM (15h), DevOps (10h) |

---

## 2. Các Cột mốc quan trọng (Key Milestones)

* **Mốc 0 (Tuần 1):** Ký hợp đồng hợp tác và tạm ứng kinh phí đợt 1.
* **Mốc 1 (Cuối Tuần 2):** Phê duyệt tài liệu Phạm vi & Yêu cầu nghiệp vụ (PRD) cùng Bảng phân bổ Resource (640h).
* **Mốc 2 (Cuối Tuần 4):** Phê duyệt Thiết kế giao diện (UI/UX Prototype), Kiến trúc hệ thống và dựng xong Nền tảng dự án (Boilerplate).
* **Mốc 3 (Cuối Tuần 9):** Hoàn thành phát triển 3 phân hệ nghiệp vụ cốt lõi (M1 Sinh viên, M2 Nhân viên, M3 Quản trị) & Demo E2E nội bộ từng luồng.
* **Mốc 4 (Cuối Tuần 12):** Hoàn thành tích hợp Cross-slice và kết thúc đợt kiểm thử nội bộ (Internal QA/QC).
* **Mốc 5 (Cuối Tuần 14):** Bàn giao chính thức hệ thống Production, tài liệu và mã nguồn; bắt đầu thời gian 10 ngày kiểm thử UAT cùng Aurora University.

---

## 3. Quy trình Nghiệm thu & Bảo hành

### 3.1 Quy trình Nghiệm thu (10 ngày làm việc - Sau 14 tuần phát triển)
1. **Bàn giao chính thức (Cuối Tuần 14):** Đơn vị phát triển bàn giao phần mềm đã triển khai trên hạ tầng Production của Client và đầy đủ bộ tài liệu.
2. **Thực hiện kiểm thử UAT (10 ngày làm việc / Tuần 15–16):** Aurora University tiến hành kiểm thử chấp nhận người dùng dựa trên kịch bản UAT E2E và chốt danh sách phản hồi. Đội ngũ phát triển phối hợp hỗ trợ và khắc phục các lỗi phát sinh trong thời gian này.
3. **Tiêu chí đạt nghiệm thu:**
   * Các luồng nghiệp vụ E2E (Sinh viên, Nhân viên, Quản lý) hoạt động chính xác theo kịch bản.
   * Phân quyền RBAC hoạt động chính xác theo vai trò trên từng chức năng.
   * Không còn lỗi nghiêm trọng (Blocker/Critical) gián đoạn chức năng chính.
   * Tài liệu bàn giao đầy đủ theo cam kết.

### 3.2 Chính sách Bảo hành (30 ngày)
* **Thời hạn:** 30 ngày kể từ ngày ký biên bản nghiệm thu chính thức (sau khi hoàn tất 10 ngày UAT).
* **Phạm vi hỗ trợ:** Khắc phục miễn phí các lỗi kỹ thuật (Bugs) phát sinh do đội ngũ phát triển.
* **Lưu ý:** Không bao gồm việc thay đổi yêu cầu, thêm tính năng mới hoặc xử lý sự cố do hạ tầng máy chủ của Client gây ra.