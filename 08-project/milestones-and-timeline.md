# [PRJ-03] Tiến độ & Cột mốc thực hiện (Milestones & Timeline)

Tài liệu chi tiết hóa lộ trình triển khai dự án **UniSupport** qua 6 giai đoạn trong 14 tuần làm việc phát triển theo phương pháp **Vertical Slice (Feature-driven Development)**, với tổng công sức **618h cơ sở + 22h dự phòng = 640h kế hoạch**.

---

## 1. Kế hoạch thực hiện theo Giai đoạn (Phases Schedule)

| Giai đoạn | Thời gian giữ theo bản hiện tại | Đầu ra review | Giới hạn công sức |
| --- | --- | --- | --- |
| 1. Làm rõ yêu cầu | Tuần 1–2 | 14 FR, quyền vai trò, danh mục và các sai lệch nguồn được đối chiếu | Dùng BA/PM/TL trong giờ nguồn, chưa tự chia giờ theo tuần |
| 2. Chuẩn bị thiết kế | Tuần 3–4 | Đầu ra thiết kế theo hồ sơ hiện có; không chọn phương án kỹ thuật mới | Dùng giờ UI/UX/TL và các vai trò của đúng dòng nguồn |
| 3. Hoàn thiện các luồng nghiệp vụ | Tuần 5–9 | Demo: cấp tài khoản/quyền → Student gửi/Staff thấy → tiếp nhận/chuyển/bổ sung → kết quả/đánh giá → dashboard/báo cáo/xuất | M01 128; M02 197; M03 215 là giờ cho toàn bộ công việc nhóm, không riêng giờ phát triển ở giai đoạn này |
| 4. Đối chiếu liên vai trò và kiểm thử nội bộ | Tuần 10–12 | Kết quả kiểm tra các luồng và phạm vi quyền theo 14 FR | QA 98 giờ đã nằm trong dòng chức năng, không cộng thêm một đợt QA |
| 5. Hoàn thiện hồ sơ và chuẩn bị bàn giao | Tuần 13 | Các lỗi thuộc phạm vi đã có được xử lý và ghi nhận | Dùng giờ còn lại/dự phòng đúng dòng; không tự tạo estimate mới |
| 6. Bàn giao | Tuần 14 | Tài liệu/kết quả bàn giao theo hồ sơ hiện có | PM tổng 70; DevOps tổng 30 cho toàn dự án, không cộng lại theo giai đoạn |

**Cách đọc lịch:** các tuần giữ như tài liệu hiện tại; đây không phải cam kết công suất từng người đã được kiểm chứng. Workbook nguồn chưa phân giờ theo tuần, vì vậy bỏ các con số giai đoạn tự chia. 618 giờ cơ sở + 22 dự phòng là trần toàn dự án; các giai đoạn, UAT và hỗ trợ không tự sinh effort ngoài bảng. Phân công thực tế chỉ dùng đúng giờ/role/dòng nguồn và không coi mỗi role làm mọi chức năng.

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
