# PRJ-04 - Tiến Độ Và Cột Mốc

Bộ mốc dưới đây là bộ mốc duy nhất của dự án, dùng chung cho [Proposal](Proposal.docx) mục 3, [master-schedule.xlsx](plans/master-schedule.xlsx) (sheet `Milestones`, `Master Schedule`) và GitHub Milestones (milestone trên GitHub chỉ chứa task dev; UAT, demo và feedback của client không đưa lên milestone). Nơi gốc của ngày, phần giao được và điều kiện nghiệm thu là sheet `Milestones`; trang này chỉ tóm tắt. Lý do chia mốc như vậy: xem [master-plan.md](master-plan.md).

## 1. Sáu Mốc Theo Luồng Ticket

Trước các mốc là **giai đoạn khởi động** 05/10–14/10/2026: chốt phạm vi và AC, prototype tương tác 3 vai trò (client duyệt bằng cách bấm qua theo WF-01…WF-07), thiết kế kỹ thuật. Giai đoạn này không phải milestone vì chưa giao phần mềm chạy được.

| Mã | Tên mốc | Bắt đầu | Kết thúc (hạn) | Client dùng thử được | Kiểm tra bằng |
| --- | --- | --- | --- | --- | --- |
| `MS-01` | Nền tảng hệ thống | 15/10/2026 | 27/10/2026 | Staging: đăng nhập 3 vai trò, quản lý tài khoản, phòng ban, Category, chặn truy cập sai quyền | AC-00 của FR-STU-00/FR-STF-00/FR-MGT-00; TS-MGT-01, TS-MGT-02 |
| `MS-02` | Tiếp nhận Ticket | 28/10/2026 | 12/11/2026 | Sinh viên tra FAQ, tạo và theo dõi Ticket, nhận thông báo; Nhân viên xem hàng chờ, tiếp nhận, phân công | TS-STU-01…04, TS-STF-01, TS-STF-02 |
| `MS-03` | Xử lý Ticket | 04/11/2026 | 19/11/2026 | Priority và thời hạn, cập nhật tiến độ, yêu cầu/gửi bổ sung, Transfer, Escalation | TS-STF-03…06, TS-STU-05 |
| `MS-04` | Trả kết quả & đóng Ticket | 20/11/2026 | 08/12/2026 | Vòng đời Ticket đầy đủ: ghi kết quả, chấp nhận/mở lại, tự đóng, CSAT | TS-STF-07, TS-STF-08, TS-STU-06, TS-STU-07 |
| `MS-05` | Quản trị & báo cáo | 09/12/2026 | 18/12/2026 | Tra soát, chính sách lưu trữ, Dashboard, báo cáo, xuất CSV | TS-MGT-03…06 |
| `MS-06` | Tích hợp & bàn giao | 21/12/2026 | 08/01/2027 | Bản UAT trên staging, sau đó bản production, HDSD, mã nguồn, tài liệu | Toàn bộ TS và NFR |

`MS-02` và `MS-03` chồng nhau từ 04/11 đến 12/11/2026: phần Nhân viên của MS-03 bắt đầu khi hàng chờ và phân công của MS-02 đã xong.

**Điều kiện nghiệm thu chung của mọi mốc:** các kịch bản của mốc đạt trên staging, regression các mốc trước đạt, không còn lỗi mức Nghiêm trọng ([quality-plan.md](../09-quality/quality-plan.md)). PM demo cho client vào ngày cuối mốc; client gửi feedback trong 02 ngày làm việc qua GitHub Issue mẫu Feedback có ghi mã mốc (không gắn GitHub milestone) (giả định `A-16`). Client trong dự án môn học là `Mô phỏng`.

## 2. Sau Bàn Giao

Aurora University có **10 ngày làm việc** để nghiệm thu chính thức sau khi nhận bàn giao (theo tiêu chí Proposal mục 5.2). Sau nghiệm thu, hệ thống được bảo hành sửa lỗi kỹ thuật **30 ngày**; giờ công bảo hành nằm ở hạng mục `Q-10` của [quotation.xlsx](quotation.xlsx).
