# PRJ-04 - Tiến Độ Và Cột Mốc

Bộ mốc dưới đây là bộ mốc duy nhất của dự án, dùng chung cho [Proposal](Proposal.docx) mục 3, [master-schedule.xlsx](plans/master-schedule.xlsx) (sheet `Milestones`, `Master Schedule`) và GitHub Milestones (milestone trên GitHub chỉ chứa task dev; UAT, demo và feedback của client không đưa lên milestone). Nơi gốc của ngày, phần giao được và điều kiện nghiệm thu là sheet `Milestones`; trang này chỉ tóm tắt. Lý do chia mốc như vậy: xem [master-plan.md](master-plan.md).

## 1. Sáu Mốc Theo Luồng Ticket

Trước các mốc là **giai đoạn khởi động** 05/10–14/10/2026: chốt phạm vi và AC, prototype tương tác 3 vai trò (client duyệt bằng cách bấm qua theo WF-01…WF-07), thiết kế kỹ thuật. Giai đoạn này không phải milestone vì chưa giao phần mềm chạy được.

| Mã | Tên mốc | Bắt đầu | Kết thúc (hạn) | Client dùng thử được | Kiểm tra bằng (kịch bản trong `06-acceptance/test-scenarios.md`) |
| --- | --- | --- | --- | --- | --- |
| `MS-01` | Nền tảng hệ thống | 15/10/2026 | 27/10/2026 | Staging: đăng nhập 3 vai trò, quản lý tài khoản, phòng ban, Category, chặn truy cập sai quyền | TS-AUTH-01, TS-AUTH-02, TS-AUTH-03, TS-AUTH-04, TS-MGT-01, TS-MGT-07, TS-MGT-02, TS-MGT-08 |
| `MS-02` | Tiếp nhận Ticket | 28/10/2026 | 12/11/2026 | Sinh viên tra FAQ, tạo và theo dõi Ticket, nhận thông báo; Nhân viên xem hàng chờ, tiếp nhận, phân công | TS-STU-01, TS-STU-08, TS-STU-02, TS-STU-09, TS-STU-03, TS-STU-10, TS-STU-04, TS-STU-11, TS-STF-01, TS-STF-09, TS-STF-02, TS-STF-10 |
| `MS-03` | Xử lý Ticket | 04/11/2026 | 19/11/2026 | Priority và thời hạn, cập nhật tiến độ, yêu cầu/gửi bổ sung, Transfer, Escalation | TS-STU-05, TS-STU-12, TS-STF-03, TS-STF-11, TS-STF-04, TS-STF-12, TS-STF-05, TS-STF-06, TS-STF-13 |
| `MS-04` | Trả kết quả & đóng Ticket | 20/11/2026 | 08/12/2026 | Vòng đời Ticket đầy đủ: ghi kết quả, chấp nhận/mở lại, tự đóng, CSAT | TS-STU-06, TS-STU-13, TS-STU-07, TS-STU-14, TS-STF-07, TS-STF-14, TS-STF-08 |
| `MS-05` | Quản trị & báo cáo | 09/12/2026 | 18/12/2026 | Tra soát, chính sách lưu trữ, Dashboard, báo cáo, xuất CSV | TS-MGT-03, TS-MGT-09, TS-MGT-04, TS-MGT-05, TS-MGT-06, TS-MGT-10 |
| `MS-06` | Tích hợp & bàn giao | 21/12/2026 | 08/01/2027 | Bản UAT trên staging, sau đó bản production, HDSD, mã nguồn, tài liệu | TS-NFR-01, TS-NFR-02, TS-NFR-03, TS-NFR-04, TS-NFR-05, TS-NFR-06; regression toàn bộ kịch bản MS-01…MS-05 |

`MS-02` và `MS-03` chồng nhau từ 04/11 đến 12/11/2026: phần Nhân viên của MS-03 bắt đầu khi hàng chờ và phân công của MS-02 đã xong.

**Điều kiện nghiệm thu chung của mọi mốc:** các kịch bản của mốc đạt trên staging, regression các mốc trước đạt, không còn lỗi mức Nghiêm trọng ([quality-plan.md](../09-quality/quality-plan.md)). PM demo cho client vào ngày cuối mốc; client gửi feedback trong 02 ngày làm việc qua GitHub Issue mẫu Feedback có ghi mã mốc (không gắn GitHub milestone) (giả định `A-16`). Client trong dự án môn học là `Mô phỏng`.

## 2. Sau Bàn Giao

Aurora University có **10 ngày làm việc** để nghiệm thu chính thức sau khi nhận bàn giao (theo tiêu chí Proposal mục 5.2). Sau nghiệm thu, hệ thống được bảo hành sửa lỗi kỹ thuật **30 ngày**; giờ công bảo hành nằm ở hạng mục `Q-10` của [quotation.xlsx](quotation.xlsx).
