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
| `R-01` | Phân quyền sai: người dùng xem/sửa được Ticket hoặc file ngoài phạm vi | 3 | 5 | 15 | TL | Kiểm tra quyền ở backend cho mọi API; test truy cập chéo từ MS-01 (TS-AUTH-04); kiểm ghi Audit từ MS-01 bằng TS-AUTH-05 qua bằng chứng kỹ thuật chỉ đọc có phân quyền, che dữ liệu nhạy cảm; giao diện tra cứu TS-MGT-03 ở MS-05, kiểm thử hệ thống TEST-02 ở MS-06 | Chặn bản phát hành, sửa ngay như lỗi Nghiêm trọng, regression toàn bộ kịch bản quyền | Test truy cập chéo thất bại; review PR thiếu kiểm tra quyền | Mở | `MS-01`, `MS-06`, FR-MGT-01, FR-MGT-03, `NFR-SEC-02` |
| `R-02` | Tính sai thời hạn xử lý (Priority, giờ làm việc, tạm dừng khi `WAITING_STUDENT`) làm Dashboard và báo cáo sai | 3 | 4 | 12 | BE2 | Viết test đơn vị cho `BR-DUE-01/02` với giá trị biên trước khi làm giao diện | Dùng buffer 10h của M02; sửa và chạy lại TS-STF-03, TS-STF-15 (lịch nghỉ, remaining ≤ 0), TS-STF-16 (từ chối đổi Priority sau giải quyết/đóng) và TS-MGT-05 | Ticket demo hiện sắp quá hạn/quá hạn khác tính tay | Mở | `MS-03`, `MS-05`, FR-STF-03, FR-MGT-05 |
| `R-03` | Trạng thái và lịch sử Ticket giữa Sinh viên và Nhân viên không đồng bộ khi hai người thao tác cùng lúc | 3 | 4 | 12 | BE1 | Thao tác nhiều bước chạy trong một transaction (task REL-01, `NFR-REL-01`); test tiếp nhận đồng thời | Khóa thao tác trùng, sửa dữ liệu lệch, bổ sung test | Lỗi "Ticket đã được tiếp nhận" xuất hiện sai; lịch sử thiếu sự kiện | Mở | `MS-02`…`MS-04`, FR-STF-02, FR-STU-03 |
| `R-04` | Tích hợp cuối dự án (MS-06) phát hiện nhiều lỗi giữa các phân hệ, không đủ 36h tích hợp | 3 | 4 | 12 | TL | Mỗi mốc từ MS-02 giao luồng xuyên phân hệ trên staging và chạy regression; tích hợp liên tục | Dùng giờ `Q-11`; ưu tiên sửa lỗi chặn luồng chính | Regression cuối mốc có lỗi giữa cổng Sinh viên và Nhân viên | Mở | `MS-06`, `Q-06`, `Q-11` |
| `R-05` | Client phản hồi chậm hoặc đổi yêu cầu sau demo mốc | 3 | 3 | 9 | PM | Demo cuối mỗi mốc; hạn phản hồi 02 ngày làm việc (A-16); đổi phạm vi đi qua CR | Ghi CR, đánh giá tác động, báo giá riêng; CR nhỏ (≤ 16h, vừa năng lực còn trống) làm trong mốc kế tiếp, CR lớn hơn mới dời mốc (master-plan.md); dời mốc nếu client chậm quá hạn (Proposal mục 6) | Quá 2 ngày không có feedback; feedback chứa yêu cầu mới | Mở | Mọi `MS-xx`, CR |
| `R-06` | Hạ tầng staging/production do Aurora University cấp chậm hoặc không đủ cấu hình | 2 | 4 | 8 | DevOps | Xin hạ tầng từ giai đoạn khởi động; dựng staging nội bộ dự phòng | Dùng staging nội bộ để demo; báo PM để thông báo client | Chưa có thông tin server khi bắt đầu MS-01 | Mở | `MS-01`, `MS-06`, A-08 |
| `R-07` | Thiếu người: một dev vắng dài ngày (≥ 3 ngày làm việc) | 2 | 3 | 6 | PM | Mỗi module có người thay thế theo Team Charter mục 3.1; PR review chéo để nhiều người hiểu code | Chuyển việc cho người thay thế; dùng `Q-11` | Thành viên báo bận dài ngày | Mở | Mọi `MS-xx` |
| `R-08` | Dữ liệu UAT không đại diện, không phát hiện được lỗi hiệu năng với 3.000 sinh viên | 2 | 3 | 6 | QA | Sinh dữ liệu giả lập theo quy mô A-01 trước MS-06 | Chạy lại kịch bản TS-NFR-01 (`NFR-PERF-01`, `NFR-PERF-02`) với dữ liệu bổ sung | Dữ liệu UAT ít hơn quy mô đã cam kết | Mở | `MS-06`, `NFR-PERF-01`, A-13 |
| `R-09` | Xuất CSV lỗi font tiếng Việt khi mở bằng Excel | 2 | 2 | 4 | BE1 | BE1 bảo đảm đầu ra UTF-8 có BOM; FE1 kiểm tra tải và mở file bằng Excel; QA xác minh trong TS-MGT-06 | BE1 sửa định dạng xuất, FE1 và QA kiểm tra lại dấu tiếng Việt | Thử mở file CSV trên Excel bị lỗi dấu | Mở | `MS-05`, FR-MGT-06, [RPT-02 #162](https://github.com/trvanluc/docs/issues/162) |

## Đối chiếu người theo dõi rủi ro với kế hoạch

Owner chịu trách nhiệm theo dõi và điều phối phòng ngừa, không nhất thiết là toàn bộ nhóm triển khai. Nơi gốc người làm chức năng là [Master Schedule](plans/master-schedule.xlsx), sheet `Master Schedule`; vai trò và quyền điều phối theo [Team Charter mục 3.1](team-charter.md#31-đội-thực-thi-mô-phỏng).

| Rủi ro | Đối chiếu / lý do giữ owner |
| --- | --- |
| R-01 | TL phụ trách kiến trúc/bảo mật, review chéo SEC-01/SEC-02 và ACC-02; người triển khai là BE/FE theo Gantt. Đây là owner giám sát xuyên module, không chuyển effort lập trình sang TL. |
| R-02 | BE2 làm SLA-01/SLA-02 ở MS-03; BE1/FE1 dùng kết quả SLA cho Dashboard MS-05. |
| R-03 | BE1 cùng BE2 làm REL-01 (#148); BE1 điều phối tính nhất quán giữa hai cổng, không thay người làm ASSIGN-01/02 phía nhân viên. |
| R-04 | TL điều phối tích hợp toàn hệ thống (INT-01/02); các dev tham gia theo Gantt MS-06. |
| R-05, R-07 | PM quản lý phản hồi, thay đổi và điều phối nguồn lực; không phải gói chức năng giao riêng cho dev. |
| R-06 | DevOps trực tiếp chuẩn bị môi trường và triển khai (ENV-01/02, DEP-01). |
| R-08 | QA phụ trách dữ liệu đại diện và kiểm thử hiệu năng (PERF-01); DevOps hỗ trợ hạ tầng. |
| R-09 | BE1 là owner đầu ra CSV, phối hợp FE1 theo Gantt hàng 31 và RPT-02 #162. Không giao việc CSV cho FE2 hoặc cộng giờ vào FE2 ở MS-05. |

Bản sửa R-09 trước đó được giữ nguyên (BE1 phối hợp FE1/QA, không chuyển sang FE2). Rà soát ngày 25/11/2026 phân biệt R-01 dùng TS-AUTH-04 cho truy cập chéo và TS-AUTH-05 cho bằng chứng ghi Audit ở MS-01; không dùng test giao diện Audit MS-05 hay system test MS-06 làm bằng chứng mốc đầu. R-02 dẫn thêm các test biên lịch và trạng thái; không đổi effort hoặc giá.
