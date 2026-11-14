# Kịch Bản Test (UAT)

Mỗi kịch bản ghi mã AC (dạng `FR-XXX-nn/AC-nn`, nơi gốc là `prd.md` của module) hoặc mã NFR (`05-non-functional-requirements/`) mà nó kiểm. Một kịch bản gom các AC cùng một luồng; luồng lỗi và từ chối được tách thành kịch bản riêng. Tổng: 177 AC của 22 FR và 23 NFR, mỗi mã có ít nhất một kịch bản. Cột Mốc là milestone mà kịch bản được chạy lần đầu; các mốc sau chạy lại làm regression. Cách chạy, người chạy và nơi lưu kết quả: [quality-plan.md mục 3](../09-quality/quality-plan.md#3-kiểm-soát-chất-lượng-quality-control--check).


## 1. Năng Lực Dùng Chung: Đăng Nhập Và Phân Quyền

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-AUTH-01 | Đăng nhập hợp lệ bằng tài khoản Sinh viên, Nhân viên, Quản lý | `FR-STU-00/AC-01`, `FR-STU-00/AC-07`, `FR-STF-00/AC-01`, `FR-STF-00/AC-06`, `FR-MGT-00/AC-01` | Mỗi vai trò vào đúng phân hệ của mình từ cùng một màn hình đăng nhập. | MS-01 |
| TS-AUTH-02 | Đăng nhập sai, tài khoản bị khóa, bỏ trống trường | `FR-STU-00/AC-02`, `FR-STU-00/AC-03`, `FR-STU-00/AC-04`, `FR-STF-00/AC-03`, `FR-MGT-00/AC-05`, `NFR-SEC-01` | Không tạo phiên; thông báo đúng từng trường hợp. | MS-01 |
| TS-AUTH-03 | Phiên hết hạn khi đang thao tác | `FR-STU-00/AC-06`, `FR-STF-00/AC-04`, `FR-MGT-00/AC-06` | Về màn hình đăng nhập kèm thông báo; dữ liệu chưa lưu không được ghi. | MS-01 |
| TS-AUTH-04 | Truy cập phân hệ, dữ liệu hoặc chức năng ngoài vai trò/phạm vi | `FR-STU-00/AC-05`, `FR-STF-00/AC-02`, `FR-STF-00/AC-05`, `FR-MGT-00/AC-02`, `FR-MGT-00/AC-03`, `FR-MGT-00/AC-04`, `FR-MGT-00/AC-07`, `NFR-SEC-02` | Trang "không có quyền truy cập"; không lộ dữ liệu. | MS-01 |

## 2. M01 - Sinh Viên

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-STU-01 | Tra cứu FAQ theo nhóm vấn đề và từ khóa | `FR-STU-01/AC-01`, `FR-STU-01/AC-02`, `FR-STU-01/AC-03`, `FR-STU-01/AC-05` | Hiển thị FAQ phù hợp; chuyển được sang tạo Ticket; không tạo Ticket tự động. | MS-02 |
| TS-STU-08 | FAQ không tải được | `FR-STU-01/AC-04` | Thông báo thử lại; không tạo Ticket. | MS-02 |
| TS-STU-02 | Tạo Ticket với Category, nội dung và file hợp lệ | `FR-STU-02/AC-01`, `FR-STU-02/AC-02`, `FR-STU-02/AC-03`, `FR-STU-02/AC-08`, `FR-STU-02/AC-09`, `FR-MGT-02/AC-02`, `FR-MGT-02/AC-11` | Đúng một Ticket `NEW`, mã duy nhất, đúng phòng ban, `MEDIUM`, chưa có người phụ trách. | MS-02 |
| TS-STU-09 | Tạo Ticket với dữ liệu/file không hợp lệ, gửi lặp, Category vừa bị vô hiệu hóa | `FR-STU-02/AC-04`, `FR-STU-02/AC-05`, `FR-STU-02/AC-06`, `FR-STU-02/AC-07`, `NFR-USA-03` | Không tạo Ticket sai; thông báo tại đúng trường/file; gửi lặp chỉ tạo một Ticket. | MS-02 |
| TS-STU-03 | Xem danh sách và chi tiết Ticket của mình | `FR-STU-03/AC-01`, `FR-STU-03/AC-02`, `FR-STU-03/AC-04`, `FR-STU-03/AC-05`, `FR-STU-03/AC-06`, `FR-STU-03/AC-07` | Chỉ Ticket của sinh viên; lịch sử đủ sự kiện, không có Escalation. | MS-02 |
| TS-STU-10 | Mở Ticket, file, thông báo của sinh viên khác | `FR-STU-03/AC-03`, `FR-STU-04/AC-04`, `NFR-SEC-03` | Trang "không có quyền"; không lộ dữ liệu. | MS-02 |
| TS-STU-04 | Nhận, mở và đánh dấu đã đọc thông báo | `FR-STU-04/AC-01`, `FR-STU-04/AC-02`, `FR-STU-04/AC-03`, `FR-STU-04/AC-06` | Thông báo đúng người, đúng Ticket, đúng trạng thái đọc; chỉ in-app. | MS-02 |
| TS-STU-11 | Mở thông báo trỏ tới Ticket không còn truy cập được | `FR-STU-04/AC-05` | "Nội dung không còn khả dụng"; không lộ dữ liệu. | MS-02 |
| TS-STU-05 | Bổ sung thông tin khi `WAITING_STUDENT` | `FR-STU-05/AC-01`, `FR-STU-05/AC-02`, `FR-STU-05/AC-04`, `FR-STF-04/AC-09` | Ticket về `IN_PROGRESS`; thời hạn tiếp tục từ phần còn lại. | MS-03 |
| TS-STU-12 | Bổ sung không hợp lệ hoặc khi Ticket đã đổi trạng thái | `FR-STU-05/AC-03`, `FR-STU-05/AC-05`, `FR-STU-05/AC-06` | Bị từ chối kèm thông báo; không lưu dữ liệu sai. | MS-03 |
| TS-STU-06 | Chấp nhận kết quả, mở lại hợp lệ, tự động đóng | `FR-STU-06/AC-01`, `FR-STU-06/AC-02`, `FR-STU-06/AC-03`, `FR-STU-06/AC-05`, `FR-STU-06/AC-08`, `FR-STF-06/AC-11` | Chấp nhận → `CLOSED`; mở lại → `IN_PROGRESS`; quá 03 ngày làm việc → tự `CLOSED`; mỗi lần có lịch sử. | MS-04 |
| TS-STU-13 | Mở lại không hợp lệ: thiếu lý do, đã đóng, hết hạn, Ticket của người khác | `FR-STU-06/AC-04`, `FR-STU-06/AC-06`, `FR-STU-06/AC-07` | Bị từ chối kèm thông báo; trạng thái không đổi. | MS-04 |
| TS-STU-07 | Đánh giá sau khi Ticket đóng | `FR-STU-07/AC-01`, `FR-STU-07/AC-02`, `FR-STU-07/AC-05`, `FR-STF-06/AC-10` | Nhận 1 đánh giá 1–5 sao trong 07 ngày theo lịch; trạng thái giữ `CLOSED`. | MS-04 |
| TS-STU-14 | Đánh giá không hợp lệ: thiếu sao, lần hai, quá hạn | `FR-STU-07/AC-03`, `FR-STU-07/AC-04`, `FR-STU-07/AC-06` | Bị từ chối kèm thông báo; không lưu đánh giá mới. | MS-04 |

## 3. M02 - Nhân Viên

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-STF-01 | Xem hàng chờ, tìm kiếm và lọc | `FR-STF-01/AC-01`, `FR-STF-01/AC-02`, `FR-STF-01/AC-04`, `FR-STF-01/AC-05`, `FR-STF-01/AC-06` | Chỉ Ticket trong phạm vi, đúng bộ lọc, phản ánh trạng thái/người phụ trách hiện tại. | MS-02 |
| TS-STF-09 | Tìm và mở Ticket ngoài phạm vi | `FR-STF-01/AC-03` | Không xuất hiện; mở trực tiếp nhận trang "không có quyền". | MS-02 |
| TS-STF-02 | Tiếp nhận và phân công Ticket | `FR-STF-02/AC-01`, `FR-STF-02/AC-03`, `FR-STF-02/AC-04`, `FR-STF-02/AC-07`, `FR-STF-02/AC-08` | Tối đa một người phụ trách; `NEW` → `IN_PROGRESS`; có lịch sử. | MS-02 |
| TS-STF-10 | Tiếp nhận đồng thời; Ticket bị Transfer giữa chừng | `FR-STF-02/AC-02`, `FR-STF-02/AC-06`, `NFR-REL-01` | Chỉ một người thành người phụ trách; thao tác muộn bị từ chối, thấy dữ liệu mới nhất. | MS-02 |
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
| TS-MGT-05 | Dashboard | `FR-MGT-05/AC-01`, `FR-MGT-05/AC-02`, `FR-MGT-05/AC-03`, `FR-MGT-05/AC-04`, `FR-MGT-05/AC-05`, `FR-MGT-05/AC-06`, `FR-MGT-05/AC-07`, `FR-MGT-05/AC-08` | Số liệu trạng thái, gần quá hạn, quá hạn và workload đúng Business Rules và đúng phạm vi. | MS-05 |
| TS-MGT-06 | Báo cáo, CSAT và xuất dữ liệu | `FR-MGT-06/AC-01`, `FR-MGT-06/AC-02`, `FR-MGT-06/AC-03`, `FR-MGT-06/AC-04`, `FR-MGT-06/AC-07`, `FR-MGT-06/AC-08`, `FR-MGT-06/AC-09`, `FR-MGT-06/AC-10`, `FR-MGT-06/AC-11` | Đúng công thức thời gian xử lý, CSAT, phạm vi quyền; CSV mở đúng trong Excel. | MS-05 |
| TS-MGT-10 | Chạy báo cáo với khoảng thời gian không hợp lệ | `FR-MGT-06/AC-05` | Không chạy báo cáo; thông báo tại trường ngày. | MS-05 |

## 5. Yêu Cầu Phi Chức Năng

| Mã | Kịch bản | Kiểm các mã | Kết quả chính | Mốc |
| :--- | :--- | :--- | :--- | :--- |
| TS-NFR-01 | Đo thời gian phản hồi và độ ổn định với dữ liệu UAT đại diện | `NFR-PERF-01`, `NFR-PERF-02`, `NFR-PERF-03`, `NFR-PERF-04` | Đạt ngưỡng ở `performance.md`; không treo. | MS-06 |
| TS-NFR-02 | Mô phỏng lỗi giữa chừng ở tạo Ticket, Transfer, bổ sung, ghi kết quả, khóa tài khoản | `NFR-REL-01`, `NFR-REL-02`, `NFR-REL-03`, `NFR-REL-04` | Không có dữ liệu dở dang; tải lại thấy trạng thái cuối đã lưu; không hiện lỗi kỹ thuật. | MS-06 |
| TS-NFR-03 | Kiểm thử phân quyền toàn hệ thống và lưu trữ mật khẩu | `NFR-SEC-01`, `NFR-SEC-02`, `NFR-SEC-03`, `NFR-SEC-04`, `NFR-SEC-05` | 0 lần truy cập thành công ngoài phạm vi (SM-07); 0 mật khẩu đọc được. | MS-06 |
| TS-NFR-04 | Dùng luồng chính trên điện thoại và máy tính, chuyển Việt/Anh | `NFR-USA-01`, `NFR-USA-02`, `NFR-USA-03`, `NFR-USA-04` | Không mất nội dung, không cuộn ngang; đủ nhãn hai ngôn ngữ; lỗi chỉ rõ trường. | MS-06 |
| TS-NFR-05 | Đối chiếu thao tác đã làm với nhật ký tra soát và nhật ký kỹ thuật | `NFR-OBS-01`, `NFR-OBS-02`, `NFR-OBS-03` | Đủ bản ghi; nhật ký kỹ thuật không chứa mật khẩu. | MS-06 |
| TS-NFR-06 | Kiểm tra sau triển khai và đối chiếu danh mục bàn giao | `NFR-DEP-01`, `NFR-DEP-02`, `NFR-DEP-03` | Truy cập được trên môi trường bàn giao; đủ hạng mục bàn giao; luồng chính chạy được. | MS-06 |
