# Sổ rủi ro

Nơi gốc duy nhất của rủi ro dự án (không còn lưu trên Google Drive). PM chịu trách nhiệm sổ. Người theo dõi (owner) cập nhật từng dòng tại buổi họp tuần ([kế hoạch quản trị, mục 3.2](../11-governance/ke-hoach-quan-tri-giam-sat.md#32-giám-sát-rủi-ro)). Owner là vai trò trong đội thực thi giả định (`Mô phỏng`, xem [Team Charter](team-charter.md)).

**Cách chấm:**

- **Khả năng (K)** và **Tác động (T)** chấm theo thang 1–5.
- **Mức = K × T:**
  - ≥ 15: **Cao**. Báo trong báo cáo tháng; nếu xảy ra thì xử lý như mức Đỏ.
  - 8–14: **Trung bình**.
  - ≤ 7: **Thấp**.
- Rủi ro đã xảy ra thì chuyển trạng thái `Đã xảy ra`, mở GitHub Issue nhãn `issue-log` và có thể dùng giờ dự phòng `Q-11` (PM duyệt).

| Mã | Mô tả | K | T | Mức | Owner | Phòng ngừa | Ứng phó khi xảy ra | Dấu hiệu báo trước | Trạng thái | Liên quan |
| --- | --- | :-: | :-: | :-: | --- | --- | --- | --- | --- | --- |
| `R-01` | Phân quyền sai: người dùng xem/sửa được Ticket hoặc file ngoài phạm vi | 3 | 5 | 15 | TL | Kiểm tra quyền ở backend cho mọi API; test truy cập chéo từ MS-01 (TS-MGT-03, TEST-02) | Chặn bản phát hành, sửa ngay như lỗi Nghiêm trọng, regression toàn bộ kịch bản quyền | Test truy cập chéo thất bại; review PR thiếu kiểm tra quyền | Mở | `MS-01`, `MS-06`, FR-MGT-01, FR-MGT-03, `NFR-SEC-02` |
| `R-02` | Tính sai thời hạn xử lý (Priority, giờ làm việc, tạm dừng khi `WAITING_STUDENT`) làm Dashboard và báo cáo sai | 3 | 4 | 12 | BE2 | Viết test đơn vị cho `BR-DUE-01/02` với giá trị biên trước khi làm giao diện | Dùng buffer 10h của M02; sửa và chạy lại TS-STF-03, TS-MGT-05 | Ticket demo hiện sắp quá hạn/quá hạn khác tính tay | Mở | `MS-03`, `MS-05`, FR-STF-03, FR-MGT-05 |
| `R-03` | Trạng thái và lịch sử Ticket giữa Sinh viên và Nhân viên không đồng bộ khi hai người thao tác cùng lúc | 3 | 4 | 12 | BE1 | Thao tác nhiều bước chạy trong một transaction (task REL-01, `NFR-REL-01`); test tiếp nhận đồng thời | Khóa thao tác trùng, sửa dữ liệu lệch, bổ sung test | Lỗi "Ticket đã được tiếp nhận" xuất hiện sai; lịch sử thiếu sự kiện | Mở | `MS-02`…`MS-04`, FR-STF-02, FR-STU-03 |
| `R-04` | Tích hợp cuối dự án (MS-06) phát hiện nhiều lỗi giữa các phân hệ, không đủ 36h tích hợp | 3 | 4 | 12 | TL | Mỗi mốc từ MS-02 giao luồng xuyên phân hệ trên staging và chạy regression; tích hợp liên tục | Dùng giờ `Q-11`; ưu tiên sửa lỗi chặn luồng chính | Regression cuối mốc có lỗi giữa cổng Sinh viên và Nhân viên | Mở | `MS-06`, `Q-06`, `Q-11` |
| `R-05` | Client phản hồi chậm hoặc đổi yêu cầu sau demo mốc | 3 | 3 | 9 | PM | Demo cuối mỗi mốc; hạn phản hồi 02 ngày làm việc (A-16); đổi phạm vi đi qua CR | Ghi CR, đánh giá tác động, báo giá riêng; CR nhỏ (≤ 16h, vừa năng lực còn trống) làm trong mốc kế tiếp, CR lớn hơn mới dời mốc (master-plan.md); dời mốc nếu client chậm quá hạn (Proposal mục 6) | Quá 2 ngày không có feedback; feedback chứa yêu cầu mới | Mở | Mọi `MS-xx`, CR |
| `R-06` | Hạ tầng staging/production do Aurora University cấp chậm hoặc không đủ cấu hình | 2 | 4 | 8 | DevOps | Xin hạ tầng từ giai đoạn khởi động; dựng staging nội bộ dự phòng | Dùng staging nội bộ để demo; báo PM để thông báo client | Chưa có thông tin server khi bắt đầu MS-01 | Mở | `MS-01`, `MS-06`, A-08 |
| `R-07` | Thiếu người: một dev vắng dài ngày (≥ 3 ngày làm việc) | 2 | 3 | 6 | PM | Mỗi module có người thay thế theo Team Charter mục 3.1; PR review chéo để nhiều người hiểu code | Chuyển việc cho người thay thế; dùng `Q-11` | Thành viên báo bận dài ngày | Mở | Mọi `MS-xx` |
| `R-08` | Dữ liệu UAT không đại diện, không phát hiện được lỗi hiệu năng với 3.000 sinh viên | 2 | 3 | 6 | QA | Sinh dữ liệu giả lập theo quy mô A-01 trước MS-06 | Chạy lại kịch bản TS-NFR-01 (`NFR-PERF-01`, `NFR-PERF-02`) với dữ liệu bổ sung | Dữ liệu UAT ít hơn quy mô đã cam kết | Mở | `MS-06`, `NFR-PERF-01`, A-13 |
| `R-09` | Xuất CSV lỗi font tiếng Việt khi mở bằng Excel | 2 | 2 | 4 | FE2 | Dùng UTF-8 có BOM; thêm vào kịch bản TS-MGT-06 | Sửa định dạng xuất | Thử mở file CSV trên Excel bị lỗi dấu | Mở | `MS-05`, FR-MGT-06 |
