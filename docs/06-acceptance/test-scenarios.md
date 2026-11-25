# Kịch Bản Test (UAT)

Mỗi kịch bản ghi mã AC (dạng `FR-XXX-nn/AC-nn`, nơi gốc là `prd.md` của module) hoặc mã NFR (`05-non-functional-requirements/`) mà nó kiểm. Một kịch bản gom các AC cùng một luồng; luồng lỗi và từ chối được tách thành kịch bản riêng. Tổng: 187 AC của 22 FR và 23 NFR, mỗi mã có ít nhất một kịch bản. Cột Mốc là milestone mà kịch bản được chạy lần đầu; các mốc sau chạy lại làm regression. Cách chạy, người chạy và nơi lưu kết quả: [quality-plan.md mục 3](../09-quality/quality-plan.md#3-kiểm-soát-chất-lượng-quality-control--check).


**Quy ước mốc:** mốc đầu là lần kiểm phần chức năng đã có, không phải hoàn tất mọi AC toàn vòng đời; phần phụ thuộc sự kiện sau có mốc riêng trong RTM và mục 6. Các báo cáo này là đặc tả kiểm thử, không phải kết quả test sản phẩm đã chạy.

## 1. Năng Lực Dùng Chung: Đăng Nhập Và Phân Quyền

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-AUTH-01 | Đăng nhập hợp lệ bằng tài khoản Sinh viên, Nhân viên, Quản lý | `FR-STU-00/AC-01`, `FR-STU-00/AC-07`, `FR-STF-00/AC-01`, `FR-STF-00/AC-06`, `FR-MGT-00/AC-01` | Mỗi vai trò vào đúng phân hệ của mình từ cùng một màn hình đăng nhập. | MS-01 |
| TS-AUTH-02 | Đăng nhập sai, tài khoản bị khóa, bỏ trống trường | `FR-STU-00/AC-02`, `FR-STU-00/AC-03`, `FR-STU-00/AC-04`, `FR-STF-00/AC-03`, `FR-MGT-00/AC-05`, `NFR-SEC-01` | Không tạo phiên; thông báo đúng từng trường hợp. | MS-01 |
| TS-AUTH-03 | Phiên hết hạn khi đang thao tác | `FR-STU-00/AC-06`, `FR-STF-00/AC-04`, `FR-MGT-00/AC-06` | Về màn hình đăng nhập kèm thông báo; dữ liệu chưa lưu không được ghi. | MS-01 |
| TS-AUTH-04 | Truy cập phân hệ, dữ liệu hoặc chức năng ngoài vai trò/phạm vi | `FR-STU-00/AC-05`, `FR-STF-00/AC-02`, `FR-STF-00/AC-05`, `FR-MGT-00/AC-02`, `FR-MGT-00/AC-03`, `FR-MGT-00/AC-04`, `FR-MGT-00/AC-07`, `NFR-SEC-02` | Trang "không có quyền truy cập"; không lộ dữ liệu. | MS-01 |
| TS-AUTH-05 | Nền tảng ghi audit qua bằng chứng kỹ thuật chỉ đọc, không qua UI | `FR-MGT-03/AC-01`, `FR-MGT-03/AC-03`, `NFR-OBS-02`, `NFR-OBS-03` | DevOps/TL cung cấp truy vấn/trích xuất được phân quyền; QA đối chiếu thao tác tài khoản/cấu hình đã có ở MS-01 với actor/thời điểm/trước–sau; không sửa/xóa qua ứng dụng, che mật khẩu/token/dữ liệu nhạy cảm. Lặp lại với sự kiện mới tại mốc giao; UI vẫn MS-05. | MS-01 |

## 2. M01 - Sinh Viên

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-STU-01 | Tra cứu FAQ theo nhóm vấn đề và từ khóa | `FR-STU-01/AC-01`, `FR-STU-01/AC-02`, `FR-STU-01/AC-03`, `FR-STU-01/AC-05` | Hiển thị FAQ phù hợp; chuyển được sang tạo Ticket; không tạo Ticket tự động. | MS-02 |
| TS-STU-08 | FAQ không tải được | `FR-STU-01/AC-04` | Thông báo thử lại; không tạo Ticket. | MS-02 |
| TS-STU-02 | Tạo Ticket với Category, nội dung và file hợp lệ | `FR-STU-02/AC-01`, `FR-STU-02/AC-02`, `FR-STU-02/AC-03`, `FR-STU-02/AC-08`, `FR-STU-02/AC-09`, `FR-MGT-02/AC-02`, `FR-MGT-02/AC-11` | Đúng một Ticket `NEW`, mã duy nhất, đúng phòng ban, `MEDIUM`, chưa có người phụ trách. | MS-02 |
| TS-STU-09 | Tạo Ticket với dữ liệu/file không hợp lệ, gửi lặp, Category vừa bị vô hiệu hóa | `FR-STU-02/AC-04`, `FR-STU-02/AC-05`, `FR-STU-02/AC-06`, `FR-STU-02/AC-07`, `NFR-USA-03` | Không tạo Ticket sai; thông báo tại đúng trường/file; gửi lặp chỉ tạo một Ticket. | MS-02 |
| TS-STU-03 | Xem danh sách và chi tiết Ticket của mình | `FR-STU-03/AC-01`, `FR-STU-03/AC-02`, `FR-STU-03/AC-04`, `FR-STU-03/AC-05`, `FR-STU-03/AC-07` | MS-02 chỉ kiểm tạo/tiếp nhận và thông tin đã có; không lộ ghi chú nội bộ/Escalation. Lịch sử bổ sung/Transfer ở TS-STU-15; đủ vòng đời ở TS-STU-16. | MS-02 |
| TS-STU-10 | Mở Ticket, file, thông báo của sinh viên khác | `FR-STU-03/AC-03`, `FR-STU-04/AC-04`, `NFR-SEC-03` | Trang "không có quyền"; không lộ dữ liệu. | MS-02 |
| TS-STU-04 | Nhận, mở và đánh dấu đã đọc thông báo | `FR-STU-04/AC-01`, `FR-STU-04/AC-02`, `FR-STU-04/AC-03`, `FR-STU-04/AC-06` | MS-02 chỉ sự kiện tạo/tiếp nhận; đúng người/Ticket/trạng thái đọc và chỉ in-app. Sự kiện MS-03/04 kiểm ở TS-STU-15/16. | MS-02 |
| TS-STU-11 | Mở thông báo trỏ tới Ticket không còn truy cập được | `FR-STU-04/AC-05` | "Nội dung không còn khả dụng"; không lộ dữ liệu. | MS-02 |
| TS-STU-05 | Bổ sung thông tin khi `WAITING_STUDENT` | `FR-STU-05/AC-01`, `FR-STU-05/AC-02`, `FR-STU-05/AC-04`, `FR-STF-04/AC-09` | Ticket về `IN_PROGRESS`; thời hạn tiếp tục từ phần còn lại. | MS-03 |
| TS-STU-12 | Bổ sung không hợp lệ hoặc khi Ticket đã đổi trạng thái | `FR-STU-05/AC-03`, `FR-STU-05/AC-05`, `FR-STU-05/AC-06` | Bị từ chối kèm thông báo; không lưu dữ liệu sai. | MS-03 |
| TS-STU-06 | Chấp nhận kết quả, mở lại hợp lệ, tự động đóng | `FR-STU-06/AC-01`, `FR-STU-06/AC-02`, `FR-STU-06/AC-03`, `FR-STU-06/AC-05`, `FR-STU-06/AC-08`, `FR-STF-06/AC-11` | Chấp nhận → `CLOSED`; mở lại → `IN_PROGRESS`; quá 03 ngày làm việc → tự `CLOSED`; mỗi lần có lịch sử. | MS-04 |
| TS-STU-13 | Mở lại không hợp lệ: thiếu lý do, đã đóng, hết hạn, Ticket của người khác | `FR-STU-06/AC-04`, `FR-STU-06/AC-06`, `FR-STU-06/AC-07` | Bị từ chối kèm thông báo; trạng thái không đổi. | MS-04 |
| TS-STU-07 | Đánh giá sau khi Ticket đóng | `FR-STU-07/AC-01`, `FR-STU-07/AC-02`, `FR-STU-07/AC-05`, `FR-STF-06/AC-10` | Nhận 1 đánh giá 1–5 sao trong 07 ngày theo lịch; trạng thái giữ `CLOSED`. | MS-04 |
| TS-STU-14 | Đánh giá không hợp lệ: thiếu sao, lần hai, quá hạn | `FR-STU-07/AC-03`, `FR-STU-07/AC-04`, `FR-STU-07/AC-06` | Bị từ chối kèm thông báo; không lưu đánh giá mới. | MS-04 |
| TS-STU-15 | Lịch sử và thông báo bổ sung/Transfer | `FR-STU-03/AC-02`, `FR-STU-03/AC-04`, `FR-STU-03/AC-06`, `FR-STU-03/AC-07`, `FR-STU-04/AC-01`, `FR-STU-04/AC-02`, `FR-STU-04/AC-03` | Yêu cầu/bổ sung, đổi trạng thái và Transfer hiển thị đúng lịch sử/người phụ trách và đúng một thông báo theo từng sự kiện bắt buộc; không công bố ghi chú nội bộ/Escalation. | MS-03 |
| TS-STU-16 | Lịch sử/thông báo toàn vòng đời và bảo toàn lần giải quyết trước | `FR-STU-03/AC-02`, `FR-STU-03/AC-04`, `FR-STU-03/AC-07`, `FR-STU-04/AC-01`, `FR-STU-04/AC-02`, `FR-STU-04/AC-03`, `FR-STU-06/AC-09` | Resolve/reopen/xác nhận/tự đóng hiển thị đúng lịch sử/thông báo; đối chiếu kết quả/file/thời điểm giải quyết cũ trước mở lại và sau kết quả vòng sau, không mất/ghi đè. Regression đầy đủ từ tạo đến đóng. | MS-04 |

## 3. M02 - Nhân Viên

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-STF-01 | Xem hàng chờ, tìm kiếm và lọc | `FR-STF-01/AC-01`, `FR-STF-01/AC-02`, `FR-STF-01/AC-04`, `FR-STF-01/AC-05`, `FR-STF-01/AC-06` | Chỉ Ticket trong phạm vi, đúng bộ lọc, phản ánh trạng thái/người phụ trách hiện tại. | MS-02 |
| TS-STF-09 | Tìm và mở Ticket ngoài phạm vi | `FR-STF-01/AC-03` | Không xuất hiện; mở trực tiếp nhận trang "không có quyền". | MS-02 |
| TS-STF-02 | Tiếp nhận và phân công Ticket | `FR-STF-02/AC-01`, `FR-STF-02/AC-03`, `FR-STF-02/AC-04`, `FR-STF-02/AC-07`, `FR-STF-02/AC-08` | Tối đa một người phụ trách; `NEW` → `IN_PROGRESS`; có lịch sử. | MS-02 |
| TS-STF-10 | Tiếp nhận đồng thời; Ticket bị Transfer giữa chừng (phần Transfer từ MS-03) | `FR-STF-02/AC-02`, `FR-STF-02/AC-06`, `NFR-REL-01` | Chỉ một người thành người phụ trách; thao tác muộn bị từ chối, thấy dữ liệu mới nhất. | MS-02 |
| TS-STF-03 | Điều chỉnh mức độ ưu tiên và theo dõi thời hạn | `FR-STF-03/AC-01`, `FR-STF-03/AC-02`, `FR-STF-03/AC-03`, `FR-STF-03/AC-04`, `FR-STF-03/AC-05` | Deadline tính lại theo Business Rules, không reset đồng hồ; đúng ngưỡng 80%/100%. | MS-03 |
| TS-STF-11 | Đổi Priority không có quyền, giá trị sai, Ticket đã chuyển phạm vi | `FR-STF-03/AC-06`, `FR-STF-03/AC-07`, `FR-STF-03/AC-08` | Bị từ chối; Priority và Deadline không đổi. | MS-03 |
| TS-STF-04 | Cập nhật tiến độ và yêu cầu sinh viên bổ sung | `FR-STF-04/AC-01`, `FR-STF-04/AC-02`, `FR-STF-04/AC-03`, `FR-STF-04/AC-04`, `FR-STF-04/AC-08` | `IN_PROGRESS → WAITING_STUDENT`; tạm dừng thời hạn; lịch sử giữ đủ các vòng. | MS-03 |
| TS-STF-12 | Yêu cầu bổ sung không hợp lệ hoặc không còn là người phụ trách | `FR-STF-04/AC-05`, `FR-STF-04/AC-06`, `FR-STF-04/AC-07` | Bị từ chối kèm thông báo; không ghi lịch sử. | MS-03 |
| TS-STF-05 | Transfer sang phòng ban khác | `FR-STF-05/AC-01`, `FR-STF-05/AC-02`, `FR-STF-05/AC-03`, `FR-STF-05/AC-06`, `FR-STF-05/AC-11`, `FR-STF-02/AC-05`, `FR-MGT-02/AC-05`, `NFR-REL-02` | Category và phòng ban đổi nhất quán, người phụ trách được gỡ, trạng thái giữ nguyên. | MS-03 |
| TS-STF-06 | Escalation tới Quản lý | `FR-STF-05/AC-04`, `FR-STF-05/AC-05` | Không đổi Category/phòng ban/người phụ trách/trạng thái; đúng người nhận thông báo. | MS-03 |
| TS-STF-13 | Transfer/Escalation không hợp lệ, không có quyền, Ticket đã đổi trạng thái | `FR-STF-05/AC-07`, `FR-STF-05/AC-08`, `FR-STF-05/AC-09`, `FR-STF-05/AC-10` | Bị từ chối kèm thông báo; không thay đổi nào được lưu. | MS-03 |
| TS-STF-07 | Ghi nhận kết quả | `FR-STF-06/AC-01`, `FR-STF-06/AC-02`, `FR-STF-06/AC-04` | `IN_PROGRESS → RESOLVED`; sinh viên xem được kết quả. | MS-04 |
| TS-STF-14 | Ghi kết quả không hợp lệ hoặc không có quyền | `FR-STF-06/AC-03`, `FR-STF-06/AC-08`, `FR-STF-06/AC-09` | Bị từ chối kèm thông báo; Ticket giữ `IN_PROGRESS`. | MS-04 |
| TS-STF-08 | Tiếp tục xử lý Ticket được mở lại | `FR-STF-06/AC-05`, `FR-STF-06/AC-06`, `FR-STF-06/AC-07`, `FR-STF-01/AC-04` | Giữ người phụ trách cũ nếu hợp lệ; nếu không thì về hàng chờ phòng ban. | MS-04 |
| TS-STF-15 | Biên lịch làm việc và đổi Priority hết thời gian | `FR-STF-03/AC-09`, `FR-STF-03/AC-10` | 01 ngày = 08 giờ, bỏ thứ Bảy/Chủ nhật/ngày nghỉ trường nạp sẵn; kiểm trước/sau ngày nghỉ, pause/resume. Remaining = 0 và < 0 đều quá hạn ngay khi lưu Priority kể cả WAITING_STUDENT; remaining > 0 giữ nguyên trong lúc pause, resume dùng lượng còn lại sau đổi Priority; không reset đồng hồ. | MS-03 |
| TS-STF-16 | Từ chối đổi Priority khi đã giải quyết/đóng | `FR-STF-03/AC-11`, `FR-STF-06/AC-09` | Có quyền nhưng RESOLVED/CLOSED vẫn bị từ chối qua API, Priority/Deadline/lịch sử không đổi; Management không resolve dù thử cấp cờ hoặc gọi trực tiếp. | MS-04 |

## 4. M03 - Quản Lý

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-MGT-01 | Tạo, cập nhật, khóa và mở khóa tài khoản | `FR-MGT-01/AC-01`, `FR-MGT-01/AC-04`, `FR-MGT-01/AC-07`, `FR-MGT-01/AC-10`, `FR-MGT-01/AC-12`, `NFR-SEC-04` | Đúng vai trò/phạm vi; khóa Nhân viên đưa Ticket về hàng chờ; có nhật ký. | MS-01 |
| TS-MGT-07 | Tài khoản không hợp lệ: trùng tên, thiếu phòng ban, tự khóa, Quản lý cuối cùng, vượt quyền, không có quyền | `FR-MGT-01/AC-02`, `FR-MGT-01/AC-03`, `FR-MGT-01/AC-05`, `FR-MGT-01/AC-06`, `FR-MGT-01/AC-08`, `FR-MGT-01/AC-09`, `FR-MGT-01/AC-11` | Bị từ chối kèm thông báo; tài khoản và quyền không đổi. | MS-01 |
| TS-MGT-02 | Quản lý phòng ban và Category | `FR-MGT-02/AC-01`, `FR-MGT-02/AC-03`, `FR-MGT-02/AC-06` | Category hoạt động có đúng một phòng ban; Ticket cũ không đổi; có nhật ký. | MS-01 |
| TS-MGT-08 | Cấu hình phòng ban/Category không hợp lệ | `FR-MGT-02/AC-04`, `FR-MGT-02/AC-07`, `FR-MGT-02/AC-08`, `FR-MGT-02/AC-09`, `FR-MGT-02/AC-10` | Bị từ chối kèm thông báo; cấu hình không đổi. | MS-01 |
| TS-MGT-03 | Xem và lọc nhật ký tra soát | `FR-MGT-03/AC-01`, `FR-MGT-03/AC-02`, `FR-MGT-03/AC-03`, `FR-MGT-03/AC-04`, `FR-MGT-03/AC-05`, `FR-MGT-03/AC-07`, `FR-MGT-03/AC-08`, `NFR-OBS-02`, `NFR-OBS-03` | Đúng phạm vi; bản ghi không sửa/xóa được qua ứng dụng. | MS-05 |
| TS-MGT-09 | Mở chức năng tra soát, lưu trữ, xuất báo cáo khi không có quyền | `FR-MGT-03/AC-06`, `FR-MGT-04/AC-06`, `FR-MGT-06/AC-06` | Không thấy chức năng; gọi trực tiếp bị từ chối. | MS-05 |
| TS-MGT-04 | Cấu hình thời hạn lưu trữ | `FR-MGT-04/AC-01`, `FR-MGT-04/AC-02`, `FR-MGT-04/AC-03`, `FR-MGT-04/AC-04`, `FR-MGT-04/AC-05`, `FR-MGT-04/AC-07` | Chỉ nhận 01–120 tháng; chỉ đánh dấu dữ liệu đến hạn; không tự động xóa/ẩn danh/di chuyển. | MS-05 |
| TS-MGT-05 | Dashboard | `FR-MGT-05/AC-01`, `FR-MGT-05/AC-02`, `FR-MGT-05/AC-03`, `FR-MGT-05/AC-04`, `FR-MGT-05/AC-05`, `FR-MGT-05/AC-06`, `FR-MGT-05/AC-07`, `FR-MGT-05/AC-08` | Số liệu trạng thái, gần quá hạn, quá hạn và workload đúng Business Rules và đúng phạm vi; Management hợp lệ không có cờ quản trị vẫn mở danh sách trong scope. Phiên hết hiệu lực/tài khoản bị khóa hoặc hạ khỏi MANAGEMENT bị từ chối cả API tổng hợp và danh sách, không có biến thể chỉ tổng hợp trong cùng scope. | MS-05 |
| TS-MGT-06 | Báo cáo, CSAT và xuất dữ liệu | `FR-MGT-06/AC-01`, `FR-MGT-06/AC-02`, `FR-MGT-06/AC-03`, `FR-MGT-06/AC-04`, `FR-MGT-06/AC-07`, `FR-MGT-06/AC-08`, `FR-MGT-06/AC-09`, `FR-MGT-06/AC-10`, `FR-MGT-06/AC-11` | Đúng công thức thời gian xử lý, CSAT, phạm vi quyền; CSV mở đúng trong Excel. | MS-05 |
| TS-MGT-10 | Chạy báo cáo với khoảng thời gian không hợp lệ | `FR-MGT-06/AC-05` | Không chạy báo cáo; thông báo tại trường ngày. | MS-05 |
| TS-MGT-11 | Mặc định, cấp/thu hồi cờ hữu hạn và chặn leo thang | `FR-MGT-01/AC-13`, `FR-MGT-01/AC-14`, `FR-MGT-01/AC-15`, `FR-MGT-01/AC-16`, `FR-MGT-01/AC-17`, `FR-MGT-01/AC-18` | Cùng nhóm/scope khác cờ; cấp rồi thu hồi có audit, phiên đang mở dùng quyền mới; mã lạ/sai nhóm/tự tăng quyền/vượt thẩm quyền hoặc scope/quản trị toàn trường cuối cùng đều bị từ chối nguyên tử. MS-01 thực thi trên tài khoản/cấu hình; kiểm cờ xử lý Ticket tại MS-02/03/04 và cờ AUDIT_READ/RETENTION_MANAGE/REPORT_EXPORT tại MS-05 theo chức năng nguồn, không yêu cầu chức năng tương lai. | MS-01 → MS-05 theo chức năng nguồn |

## 5. Yêu Cầu Phi Chức Năng

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-NFR-01 | Đo thời gian phản hồi và độ ổn định với dữ liệu UAT đại diện | `NFR-PERF-01`, `NFR-PERF-02`, `NFR-PERF-03`, `NFR-PERF-04` | Đạt ngưỡng ở `performance.md`; không treo. | MS-06 |
| TS-NFR-02 | Lỗi giữa chừng, tải lại trạng thái đã lưu và thông báo lỗi theo chức năng đã giao | `NFR-REL-01`, `NFR-REL-02`, `NFR-REL-03`, `NFR-REL-04` | Mỗi ca giữ snapshot trước lỗi, chèn lỗi tại bước ghi trước commit, gửi thao tác rồi tải lại bằng phiên mới: không có dữ liệu dở dang, thấy đúng trạng thái cuối đã lưu, lịch sử cũ còn nguyên và thông báo không lộ stack trace/mã lỗi kỹ thuật. Chạy theo bộ ca staged tại mục 7, không dùng concurrent claim để thay kiểm failure/reload/error. | MS-02 → MS-04 theo chức năng nguồn; MS-06 toàn hệ thống |
| TS-NFR-03 | Kiểm thử phân quyền toàn hệ thống và lưu trữ mật khẩu | `NFR-SEC-01`, `NFR-SEC-02`, `NFR-SEC-03`, `NFR-SEC-04`, `NFR-SEC-05` | 0 lần truy cập thành công ngoài phạm vi (SM-07); 0 mật khẩu đọc được. | MS-06 |
| TS-NFR-04 | Dùng luồng chính trên điện thoại và máy tính, chuyển Việt/Anh | `NFR-USA-01`, `NFR-USA-02`, `NFR-USA-03`, `NFR-USA-04` | Không mất nội dung, không cuộn ngang; đủ nhãn hai ngôn ngữ; lỗi chỉ rõ trường. | MS-06 |
| TS-NFR-05 | Đối chiếu thao tác đã làm với nhật ký tra soát và nhật ký kỹ thuật | `NFR-OBS-01`, `NFR-OBS-02`, `NFR-OBS-03` | Đủ bản ghi; nhật ký kỹ thuật không chứa mật khẩu. | MS-06 |
| TS-NFR-06 | Kiểm tra sau triển khai và đối chiếu danh mục bàn giao | `NFR-DEP-01`, `NFR-DEP-02`, `NFR-DEP-03` | Truy cập được trên môi trường bàn giao; đủ hạng mục bàn giao; luồng chính chạy được. | MS-06 |

## 6. Bộ Mẫu Quyền, Phạm Vi Và Trạng Thái

Chỉ dùng dữ liệu giả lập. Mỗi ca lưu user/group, tập cờ thực tế, scope/phòng ban, assignee, state, thời điểm/lịch nghỉ, yêu cầu trực tiếp và kết quả mong đợi/thực tế. Không chỉ kiểm ẩn nút.

- Cặp tài khoản cùng nhóm/cùng scope, một có cờ và một không; người phụ trách hợp lệ so với Staff không phụ trách; Student sở hữu/không sở hữu; Management phòng ban/toàn trường.
- Tài khoản không cờ mặc định, bị khóa, phiên đang mở trước cấp/thu hồi, mã quyền lạ/sai nhóm; người cấp thiếu cờ MANAGEMENT hoặc vượt scope; tự tăng quyền và quản trị toàn trường cuối cùng (kể cả hai yêu cầu đồng thời).
- Ticket mỗi state NEW/IN_PROGRESS/WAITING_STUDENT/RESOLVED/CLOSED, trong/ngoài scope; đổi assignee/phòng ban/state giữa lúc mở và lưu. Có cờ không vượt state/scope; Management không resolve, Staff không close/reopen.
- Mẫu lịch 8 giờ/ngày, thứ Sáu qua cuối tuần/ngày nghỉ trường, WAITING_STUDENT pause/resume; remaining dương/0/âm; bản kết quả/file/thời điểm/lịch sử trước và sau reopen và vòng giải quyết tiếp theo.
- MS-01 chỉ chạy chức năng tài khoản/cấu hình/auth/audit nền tảng đã có; mẫu Ticket thực thi quyền bổ sung ở MS-02/03/04 theo chức năng nguồn. AC khóa Staff có Ticket (FR-MGT-01/AC-04/10), vô hiệu hóa phòng ban còn Ticket (FR-MGT-02/AC-04) và cạnh tranh khi Transfer (TS-STF-10) được kiểm khi chức năng tương ứng đã có, không coi mẫu dữ liệu giả là bằng chứng tính năng đã xây. TS-MGT-01/07/08/11 lặp lại ở các mốc đó; MS-04 đủ vòng đời Ticket. MS-05 kiểm cấp/thu hồi và thực thi AUDIT_READ, RETENTION_MANAGE, REPORT_EXPORT khi có giao diện tra soát/lưu trữ/xuất báo cáo; dùng TS-MGT-03/04/06/09/11 và cặp tài khoản cùng scope khác cờ. MS-06 regression toàn hệ thống/SM-07.

**Đáp án biên thời gian (fixture, không phải cấu hình lịch nghỉ sản xuất):** dùng lịch giả lập 08:00–12:00/13:00–17:00, thứ Hai đến thứ Sáu; đánh dấu thứ Hai kế tiếp là ngày trường nghỉ. Ticket MEDIUM tạo thứ Sáu 09:00 có 24 giờ làm việc, không pause: còn 17 giờ sau thứ Sáu, 09 giờ sau thứ Ba, 01 giờ sau thứ Tư, deadline thứ Năm 09:00; cuối tuần và thứ Hai nghỉ không trừ giờ. Trong TS-STF-15, đã dùng 16 giờ rồi đổi HIGH (16 giờ) cho remaining = 0, đổi URGENT (08 giờ) cho remaining = −8: cả hai quá hạn ngay; đã dùng 15 giờ đổi HIGH còn 01 giờ. TS-STU-06 dùng cùng lịch để kiểm 03 ngày làm việc phản hồi/tự đóng qua cuối tuần/ngày nghỉ, không đóng sớm theo 72 giờ lịch; TS-STU-16 giữ ảnh chụp dữ liệu kết quả/thời điểm/lịch sử vòng trước để đối chiếu sau reopen và resolve lần tiếp.

## 7. Bộ Ca REL Theo Phần Chức Năng Đã Giao

TS-NFR-02 là một kịch bản có nhiều bộ ca, không phải chỉ chạy lần đầu ở MS-06. Chỉ dùng môi trường test và dữ liệu Mô phỏng; cách chèn lỗi do TL/QA xác nhận trong harness test, không thao tác phá môi trường vận hành. Với mỗi thao tác: lưu snapshot dữ liệu/trạng thái/lịch sử và kết quả thành công chuẩn; chèn lỗi ở bước ghi trước commit, gửi thao tác, kiểm phản hồi rồi tải lại bằng phiên mới. Kỳ vọng không còn dữ liệu dở dang, thấy trạng thái cuối đã lưu thành công, lịch sử trước lỗi không mất/sửa, thông báo dễ hiểu không có stack trace/mã lỗi kỹ thuật. Ca thành công đối chứng phải lưu đầy đủ đầu ra. Lưu kết quả mong đợi/thực tế và liên kết issue nguồn; mô tả dưới đây chưa phải bằng chứng test đã chạy.

| Bộ ca TS-NFR-02 | Khi chạy / task nguồn | Điểm kiểm cụ thể |
| --- | --- | --- |
| Phần MS-02 | Tạo Ticket và tiếp nhận/phân công: #132/#133/#136/#137 | Lỗi giữa ghi Ticket–Category/phòng ban/trạng thái hoặc giữa đổi assignee–state–lịch sử không để bản ghi một phần. Sau tải lại thấy dữ liệu trước thao tác lỗi hoặc kết quả đã commit đầy đủ, không tự gửi lặp; lịch sử đã có còn nguyên. TS-STF-10 kiểm cạnh tranh riêng, không thay bộ ca lỗi này. |
| Phần MS-03 | Bổ sung/Transfer và REL foundation: #145/#146/#148 | Lỗi giữa lưu bổ sung–state–lịch sử hoặc đổi Category–phòng ban–gỡ assignee không để trạng thái pha trộn. Tải lại đúng snapshot cuối thành công; kết quả/lịch sử cũ còn đủ; thông báo lỗi không lộ chi tiết kỹ thuật. Chạy lại phần MS-02. |
| Phần MS-04 | Resolve/reopen và REL hoàn thiện: #149/#152/#153/#148 | Chèn lỗi giữa lưu kết quả–RESOLVED hoặc mở lại–phân công–lịch sử; tải lại không có kết quả/trạng thái nửa chừng và vẫn giữ kết quả/file/thời điểm/lịch sử chu kỳ trước. Chạy lại các phần MS-02/MS-03. Parent REL #148 chỉ hoàn tất sau phần này. |
| Toàn hệ thống MS-06 | #165/#167, regression #168 | Chạy lại toàn bộ bộ ca trên bản tích hợp; gồm khóa tài khoản có Ticket và hành vi đưa Ticket về hàng chờ khi chức năng đó đã có. Đối chiếu đủ NFR-REL-01…04, gồm các màn hình UAT và thông báo lỗi, không lấy kết quả foundation thay toàn hệ thống. |

Các phần sớm nằm trong kiểm thử/DoD của task chức năng nguồn, không tạo parent/effort mới; #148 tổng hợp nền tảng MS-03 và hoàn thiện MS-04. BA/TL/QA phải xác nhận độ đủ của bộ ca trong effort đã ước lượng trước chốt baseline; thiếu effort phải đánh giá tác động, không tự gọi là đã đủ giờ.
