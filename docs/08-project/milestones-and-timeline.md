# PRJ-04 - Tiến Độ Và Cột Mốc

**Bản nháp `v1.2-draft`, 25/11/2026 — Chờ PM rà soát; chưa được khách phê duyệt, chưa đồng bộ GitHub.** Đề xuất gửi 30/11/2026, mục tiêu xác nhận 04/12/2026, chỉ khởi động 07/12/2026 khi khách xác nhận Proposal/phạm vi, đầu mối và nguồn lực. Ngoài cuối tuần, loại 01/01/2027, 30/04 và 01/05/2027; 08–12/02, 16/04 và nghỉ bù 03/05/2027 là giả định đóng cửa trường phục vụ lập kế hoạch, chờ trường xác nhận (16/04 chưa xác minh lịch âm chính thức), không phải lịch nghỉ chính thức đã được duyệt. Thay đổi giả định phải tính lại trước baseline.

Bộ mốc dưới đây là bộ mốc đề xuất duy nhất của dự án, dùng chung cho [Proposal](Proposal.docx) mục 3, [master-schedule.xlsx](plans/master-schedule.xlsx) (sheet `Milestones`, `Master Schedule`) và GitHub Milestones (milestone trên GitHub chỉ chứa task dev; UAT, demo và feedback của client không đưa lên milestone). Nơi gốc của ngày, phần giao được và điều kiện nghiệm thu là sheet `Milestones`; trang này chỉ tóm tắt. Lý do chia mốc như vậy: xem [master-plan.md](master-plan.md).

## 1. Sáu Mốc Theo Luồng Ticket

Trước các mốc là **giai đoạn khởi động** 07/12–18/12/2026 (10 ngày làm việc; chốt phạm vi trước các phần prototype/thiết kế phụ thuộc, có đủ cửa sổ cho 27h UI/UX): chốt phạm vi và AC, prototype tương tác 3 vai trò (client duyệt bằng cách bấm qua theo WF-01…WF-07), thiết kế kỹ thuật. Giai đoạn này không phải milestone vì chưa giao phần mềm chạy được.

| Mã | Tên mốc | Bắt đầu | Kết thúc (hạn) | Client dùng thử được | Kiểm tra bằng (kịch bản trong `06-acceptance/test-scenarios.md`) |
| --- | --- | --- | --- | --- | --- |
| `MS-01` | Nền tảng hệ thống | 21/12/2026 | 14/01/2027 | Staging: đăng nhập 3 vai trò, quản lý tài khoản, phòng ban, Category, chặn truy cập sai quyền | TS-AUTH-01, TS-AUTH-02, TS-AUTH-03, TS-AUTH-04, TS-AUTH-05, TS-MGT-01, TS-MGT-07, TS-MGT-02, TS-MGT-08, TS-MGT-11 (phần nền tảng) |
| `MS-02` | Tiếp nhận Ticket | 15/01/2027 | 17/02/2027 | Sinh viên tra FAQ, tạo và theo dõi Ticket, nhận thông báo/lịch sử cho sự kiện tạo và tiếp nhận; Nhân viên xem hàng chờ, tiếp nhận, phân công | TS-STU-01, TS-STU-08, TS-STU-02, TS-STU-09, TS-STU-03, TS-STU-10, TS-STU-04, TS-STU-11, TS-STF-01, TS-STF-09, TS-STF-02, TS-STF-10 |
| `MS-03` | Xử lý Ticket | 18/02/2027 | 11/03/2027 | Priority và thời hạn, cập nhật tiến độ, yêu cầu/gửi bổ sung, Transfer, Escalation; bổ sung thông báo/lịch sử yêu cầu bổ sung và chuyển phòng | TS-STU-05, TS-STU-12, TS-STU-15, TS-STF-03, TS-STF-11, TS-STF-15, TS-STF-04, TS-STF-12, TS-STF-05, TS-STF-06, TS-STF-13 |
| `MS-04` | Trả kết quả & đóng Ticket | 12/03/2027 | 25/03/2027 | Vòng đời Ticket đầy đủ: ghi kết quả, chấp nhận/mở lại, tự đóng, CSAT; hoàn thiện thông báo/lịch sử kết quả, mở lại, đóng và regression toàn vòng đời | TS-STU-06, TS-STU-13, TS-STU-07, TS-STU-14, TS-STU-16, TS-STF-07, TS-STF-14, TS-STF-08, TS-STF-16 |
| `MS-05` | Quản trị & báo cáo | 26/03/2027 | 13/04/2027 | Tra soát, chính sách lưu trữ, Dashboard, báo cáo, xuất CSV | TS-MGT-03, TS-MGT-09, TS-MGT-04, TS-MGT-05, TS-MGT-06, TS-MGT-10 |
| `MS-06` | Tích hợp & bàn giao | 14/04/2027 | 18/05/2027 | Bản UAT trên staging, sau đó bản production, HDSD, mã nguồn, tài liệu | TS-NFR-01, TS-NFR-02, TS-NFR-03, TS-NFR-04, TS-NFR-05, TS-NFR-06; regression toàn bộ kịch bản MS-01…MS-05 |

Phương án v1.2 xếp các mốc tuần tự, không giữ chồng lấn 7 ngày của bản v1.1. Tổng từ khởi động đến bàn giao là **108 ngày làm việc / 163 ngày lịch**; giờ/nguồn lực theo task nằm trong các sheet `Lịch task-vai trò`, `Phân bổ WP`, `Tải ngày`, `Năng lực tuần`. BE/FE có thể song song trong mốc khi đủ đầu vào; QA/regression đợi đầu ra và hoàn tất trước giao.

**Điều kiện nghiệm thu chung của mọi mốc:** các kịch bản của mốc đạt trên staging, regression các mốc trước đạt, không còn lỗi mức Nghiêm trọng ([quality-plan.md](../09-quality/quality-plan.md)). PM demo cho client vào ngày cuối mốc; client gửi feedback trong 02 ngày làm việc qua GitHub Issue mẫu Feedback có ghi mã mốc (không gắn GitHub milestone) (giả định `A-16`). Client trong hồ sơ là `Mô phỏng`. Kiểm audit MS-01 qua TS-AUTH-05 bằng chứng kỹ thuật chỉ đọc có phân quyền, che dữ liệu nhạy cảm; không yêu cầu giao diện tra cứu audit trước MS-05.

**Kiểm lại quyền và cấu hình theo chức năng nguồn:** TS-MGT-01/07/08/11 và TS-AUTH-04/05 được chạy lại ở MS-02…MS-05 trên chức năng đã giao: MS-02 có Ticket/phân công, MS-03 có Priority/bổ sung/Transfer/Escalation, MS-04 có resolve/reopen/close, MS-05 có Audit UI/lưu trữ/xuất báo cáo. Không dùng dữ liệu Ticket giả ở MS-01 để tuyên bố đã kiểm phần xử lý Ticket tương lai. Các AC liên quan Ticket ở TS-MGT-01/07/08 được nghiệm thu tăng dần theo [bộ mẫu kiểm thử](../06-acceptance/test-scenarios.md#6-bộ-mẫu-quyền-phạm-vi-và-trạng-thái).

## 2. Sau Bàn Giao

Aurora University có **10 ngày làm việc** để nghiệm thu chính thức sau khi nhận bàn giao (theo tiêu chí Proposal mục 5.2). Sau nghiệm thu, hệ thống được bảo hành sửa lỗi kỹ thuật **30 ngày lịch**; giờ công bảo hành nằm ở hạng mục `Q-10` của [quotation.xlsx](quotation.xlsx).

Nếu nhận bàn giao ngày **18/05/2027**, 10 ngày làm việc tiếp theo (không tính ngày bàn giao) kết thúc **01/06/2027** theo lịch giả định. Đây là hạn phản hồi dự kiến, không phải bằng chứng nghiệm thu. Nếu nghiệm thu thực tế 01/06, cửa sổ bảo hành 30 ngày lịch **tính cả ngày nghiệm thu** là **01–30/06/2027**; nghiệm thu ngày khác phải tính lại. Ngày nghỉ không kéo dài cửa sổ 30 ngày lịch. 26h bảo hành được giữ chỗ theo vai trò, không cộng lại vào 885h.
