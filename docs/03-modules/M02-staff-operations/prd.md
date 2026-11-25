# Phân Hệ Nhân Viên (M02 - Staff Operations)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Staff Operations** cung cấp không gian làm việc để nhân viên Aurora University tiếp nhận, phân loại, phân công, xử lý, chuyển xử lý và ghi nhận kết quả các Ticket hỗ trợ sinh viên.

- **Actor chính:** Nhân viên (Staff).
- **Phạm vi dữ liệu:** Nhân viên chỉ được truy cập Ticket thuộc phòng ban hoặc phạm vi trách nhiệm được cấp.
- **Người phụ trách:** Một Ticket có tối đa một người phụ trách chính tại một thời điểm. Ticket chưa được tiếp nhận/phân công hoặc vừa Transfer có thể chưa có người phụ trách chính.
- **Phân công:** Các thao tác phân công/phân công lại chỉ dành cho Staff hoặc Management có quyền tương ứng theo [Actors & Roles](../../01-product/actors-and-roles.md).
- **Phạm vi vòng đời:** Các thao tác xử lý chính của M02 kết thúc khi Ticket được ghi nhận `RESOLVED`. Nhân viên vẫn có thể xem Ticket `RESOLVED`/`CLOSED` trong phạm vi quyền; nếu Ticket được mở lại hợp lệ về `IN_PROGRESS`, M02 tiếp tục xử lý Ticket đó.

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

**Quyền hữu hạn:** áp dụng [Actors & Roles mục 4](../../01-product/actors-and-roles.md#4-danh-mục-quyền-chức-năng-hữu-hạn). Assignee Staff có quyền cơ sở xử lý Ticket mình phụ trách; thao tác thay assignee cần CATEGORY_OVERRIDE, PRIORITY_OVERRIDE, SUPPLEMENT_OVERRIDE hoặc RESOLVE_OVERRIDE tương ứng. Tiếp nhận cho Staff khác/phân công dùng TICKET_ASSIGN; Transfer dùng TICKET_TRANSFER; Escalation dùng ESCALATION_SEND và đích có ESCALATION_RECEIVE. Các cờ không vượt scope/state; Management không resolve. Thu hồi cờ chặn yêu cầu ủy quyền tiếp theo, không xóa lịch sử.

### [FR-STF-00] Đăng nhập và truy cập Staff Operations

**Priority:** Cao: nhân viên không làm được việc gì nếu không đăng nhập đúng phạm vi. **Mốc giao:** MS-01.

#### 1. Mô tả & Phạm vi
Cho phép nhân viên đăng nhập vào UniSupport và truy cập không gian làm việc phù hợp với phòng ban và quyền được cấp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên.
- **Preconditions:** Tài khoản tồn tại, đang hoạt động và được gắn với phạm vi phòng ban phù hợp.

#### 3. Quy tắc Dữ liệu & Validation
- **Tên đăng nhập:** bắt buộc, sử dụng tài khoản do nhà trường cấp.
- **Mật khẩu:** bắt buộc.
- Không chấp nhận dữ liệu chỉ chứa khoảng trắng.

#### 4. Luồng xử lý chi tiết
1. Nhân viên truy cập UniSupport.
2. Hệ thống yêu cầu đăng nhập nếu chưa có phiên hợp lệ.
3. Nhân viên nhập thông tin đăng nhập.
4. Hệ thống xác thực tài khoản, trạng thái hoạt động và phạm vi quyền.
5. Nếu hợp lệ, hệ thống cho phép truy cập Staff Operations và chỉ hiển thị dữ liệu thuộc phạm vi được cấp.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Thông tin đăng nhập không hợp lệ: từ chối truy cập.
- Tài khoản bị khóa hoặc vô hiệu hóa: không tạo phiên đăng nhập.
- Tài khoản chưa được gắn phạm vi phòng ban cần thiết: không cho phép truy cập dữ liệu Ticket của phòng ban.
- Phiên hết hạn: yêu cầu xác thực lại.

#### 6. Quy tắc nghiệp vụ
- Nhân viên không được truy cập Ticket ngoài phạm vi được cấp.
- Cơ chế xác thực và quản lý phiên được dùng chung với các phân hệ khác.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-00/AC-01:** Tài khoản Staff hợp lệ đăng nhập thành công và được đưa vào Staff Operations.
- **FR-STF-00/AC-02:** Nhân viên chỉ thấy Ticket thuộc phòng ban/phạm vi được cấp; mở Ticket ngoài phạm vi bằng đường dẫn nhận trang "không có quyền truy cập".
- **FR-STF-00/AC-03:** Sai thông tin đăng nhập: thông báo "thông tin đăng nhập không đúng"; tài khoản bị khóa: thông báo "tài khoản đã bị khóa"; cả hai trường hợp không tạo phiên.
- **FR-STF-00/AC-04:** Phiên hết hạn: thao tác tiếp theo đưa người dùng về màn hình đăng nhập kèm thông báo "phiên đã hết hạn"; dữ liệu chưa lưu không được ghi.
- **FR-STF-00/AC-05:** Tài khoản Staff chưa gắn phòng ban: đăng nhập được nhưng hàng chờ trống kèm thông báo liên hệ quản trị; không mở được Ticket nào.
- **FR-STF-00/AC-06:** Nhân viên đăng nhập trên màn hình đăng nhập dùng chung và được điều hướng tới Staff Operations theo vai trò.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Đã có phiên hợp lệ:** vào thẳng Staff Operations.
- **A2 — Nhân viên được đổi phòng ban khi đang đăng nhập:** ở lần tải dữ liệu tiếp theo, hàng chờ hiển thị theo phòng ban mới.

#### 9. Ví dụ Edge Case
- Tài khoản Staff chưa gắn phòng ban: đăng nhập được nhưng không thấy Ticket nào và có thông báo liên hệ quản trị.
- Tài khoản Student đăng nhập rồi mở URL Staff Operations: bị từ chối.
- Phiên hết hạn giữa lúc nhập kết quả xử lý: yêu cầu đăng nhập lại, dữ liệu chưa lưu không được ghi.

---

### [FR-STF-01] Xem hàng chờ, tìm kiếm và lọc Ticket

**Priority:** Cao: nhân viên chỉ làm việc được khi có hàng chờ (riêng tìm kiếm và lọc nâng cao ở mức Trung bình). **Mốc giao:** MS-02.

#### 1. Mô tả & Phạm vi
Cung cấp danh sách công việc để nhân viên xem Ticket mới, Ticket được giao và Ticket đang cần xử lý trong phạm vi của mình.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đã đăng nhập.
- **Preconditions:** Nhân viên có quyền truy cập ít nhất một phạm vi Ticket.

#### 3. Quy tắc Dữ liệu & Validation
- Tìm kiếm theo **Mã Ticket**.
- Bộ lọc hỗ trợ tối thiểu: **Trạng thái, Nhóm vấn đề, Mức độ ưu tiên, Người phụ trách**.
- Hàng chờ được hiểu là các nhóm Ticket phục vụ xử lý công việc, tối thiểu gồm:
  - **Ticket mới/chưa có người phụ trách:** Ticket thuộc phòng ban nhưng chưa được tiếp nhận hoặc phân công.
  - **Ticket của tôi:** Ticket mà nhân viên hiện là người phụ trách chính.
  - **Chờ sinh viên bổ sung:** Ticket trong phạm vi phòng ban đang ở `WAITING_STUDENT`.
  - **Sắp quá hạn / Quá hạn:** Ticket đạt ngưỡng cảnh báo hoặc đã vượt thời hạn xử lý theo Business Rules.
- Nhân viên chỉ nhận kết quả thuộc phạm vi dữ liệu được phép truy cập.
- Ticket được mở lại từ `RESOLVED` về `IN_PROGRESS` phải xuất hiện lại trong danh sách xử lý phù hợp.

#### 4. Luồng xử lý chi tiết
1. Nhân viên mở Staff Operations.
2. Hệ thống hiển thị hàng chờ Ticket thuộc phạm vi phòng ban/người dùng.
3. Nhân viên nhập Mã Ticket hoặc áp dụng một hay nhiều bộ lọc.
4. Hệ thống trả về danh sách Ticket phù hợp.
5. Nhân viên mở một Ticket để xem chi tiết trước khi tiếp nhận hoặc xử lý.
6. Hệ thống hiển thị thông tin Ticket, sinh viên gửi yêu cầu, Category, trạng thái, Priority, Deadline, người phụ trách, file được phép truy cập và lịch sử xử lý.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Không có Ticket phù hợp: hiển thị danh sách trống.
- Ticket ngoài phạm vi quyền: từ chối truy cập và không hiển thị dữ liệu.
- Mã Ticket không tồn tại: hiển thị trạng thái không tìm thấy.

#### 6. Quy tắc nghiệp vụ
- Kết quả tìm kiếm và lọc luôn phải tuân thủ phạm vi quyền của người dùng.
- Transfer hoặc phân công lại có thể làm Ticket không còn xuất hiện trong danh sách của người dùng cũ.
- Danh sách phải phản ánh trạng thái và người phụ trách hiện tại của Ticket.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-01/AC-01:** Tìm bằng mã Ticket hợp lệ trong phạm vi trả về đúng Ticket đó.
- **FR-STF-01/AC-02:** Bộ lọc trạng thái, Category, Priority, người phụ trách, dùng riêng hay kết hợp, chỉ trả về Ticket thỏa mọi điều kiện đã chọn.
- **FR-STF-01/AC-03:** Ticket ngoài phạm vi không xuất hiện trong danh sách hay kết quả tìm kiếm; mở trực tiếp bằng đường dẫn nhận trang "không có quyền truy cập".
- **FR-STF-01/AC-04:** Ticket được mở lại xuất hiện lại trong danh sách xử lý phù hợp ở trạng thái `IN_PROGRESS`.
- **FR-STF-01/AC-05:** Không có Ticket phù hợp: danh sách trống kèm thông báo "không có Ticket phù hợp"; mã Ticket không tồn tại: thông báo "không tìm thấy".
- **FR-STF-01/AC-06:** Sau Transfer hoặc phân công lại, ở lần tải tiếp theo Ticket rời danh sách của người/phòng ban cũ; danh sách luôn hiển thị trạng thái và người phụ trách hiện tại.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Chuyển giữa các hàng chờ** (Ticket mới, Ticket của tôi, Chờ sinh viên, Sắp quá hạn/Quá hạn) mà không cần nhập bộ lọc.
- **A2 — Kết hợp nhiều bộ lọc:** hệ thống trả các Ticket thỏa đồng thời mọi điều kiện.

#### 9. Ví dụ Edge Case
- Tìm mã Ticket thuộc phòng ban khác: không trả kết quả và không mở được chi tiết (FR-STF-01/AC-03).
- Ticket vừa được mở lại: xuất hiện lại trong "Ticket của tôi" của người phụ trách cũ nếu còn hợp lệ (FR-STF-01/AC-04).
- Ticket bị Transfer khi nhân viên đang xem danh sách: lần tải lại tiếp theo Ticket biến mất khỏi danh sách của nhân viên.

---

### [FR-STF-02] Phân loại, tiếp nhận và phân công Ticket

**Priority:** Cao: quyết định người chịu trách nhiệm xử lý; thiếu thì Ticket không ra khỏi `NEW`. **Mốc giao:** MS-02.

#### 1. Mô tả & Phạm vi
Cho phép nhân viên kiểm tra **Nhóm vấn đề (Category)** đã được sinh viên chọn từ danh mục có sẵn, điều chỉnh Category khi nội dung thực tế được phân loại khác, tiếp nhận Ticket chưa có người phụ trách và cho phép người dùng có quyền phân công hoặc phân công lại Ticket cho nhân viên phù hợp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đã đăng nhập.
- **Actor bổ sung:** Staff hoặc Management có quyền phân công theo ma trận quyền tại [Actors & Roles](../../01-product/actors-and-roles.md).
- **Preconditions:** Ticket thuộc phạm vi phòng ban được phép xử lý.

#### 3. Quy tắc Dữ liệu & Validation
- **Nhóm vấn đề (Category):**
  - Phải là một giá trị đang hoạt động trong danh mục Category có sẵn của hệ thống.
  - Nhân viên không được nhập tự do hoặc tạo Category mới trong màn hình xử lý Ticket.
  - Mỗi Category được cấu hình với một phòng ban tiếp nhận phù hợp.
  - Nếu nội dung thực tế không phù hợp với Category hiện tại, người có quyền xử lý có thể chọn lại một Category có sẵn.
  - Nếu Category mới thuộc phòng ban khác, thay đổi Category chỉ được xác nhận cùng với luồng **Transfer** sang phòng ban được cấu hình cho Category đó; hệ thống không được lưu Category mới nhưng vẫn giữ Ticket ở phòng ban cũ.
- **Người phụ trách:** phải là nhân viên đang hoạt động và thuộc phòng ban đang phụ trách Ticket.
- Một Ticket có **tối đa 01 người phụ trách chính tại một thời điểm**. Ticket chưa được tiếp nhận/phân công có thể chưa có người phụ trách chính.
- Danh sách nhân viên dùng cho thao tác Assign/Reassign chỉ hiển thị các nhân viên hợp lệ thuộc phòng ban hiện tại.

#### 4. Luồng xử lý chi tiết

**Luồng A — Tiếp nhận Ticket**
1. Nhân viên mở Ticket chưa có người phụ trách trong hàng chờ phòng ban.
2. Hệ thống hiển thị nội dung yêu cầu và Category hiện tại.
3. Nhân viên kiểm tra Category và điều chỉnh nếu cần.
4. Nhân viên chọn **Tiếp nhận**.
5. Hệ thống kiểm tra Ticket vẫn chưa có người phụ trách và còn thuộc phạm vi của nhân viên.
6. Hệ thống ghi nhận nhân viên là người phụ trách chính.
7. Nếu Ticket đang ở `NEW`, hệ thống chuyển Ticket sang `IN_PROGRESS`.
8. Hệ thống ghi nhận sự kiện tiếp nhận/phân công vào lịch sử Ticket.

**Luồng B — Phân công hoặc phân công lại**
1. Người dùng có quyền phân công mở Ticket.
2. Hệ thống hiển thị danh sách nhân viên hợp lệ thuộc phòng ban đang phụ trách Ticket.
3. Người dùng chọn một nhân viên.
4. Hệ thống kiểm tra quyền và phạm vi phòng ban.
5. Hệ thống cập nhật người phụ trách chính.
6. Nếu Ticket đang ở `NEW`, Ticket chuyển sang `IN_PROGRESS`.
7. Hệ thống ghi nhận người phụ trách trước, người phụ trách mới và người thực hiện thao tác vào lịch sử.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Hai nhân viên cùng tiếp nhận một Ticket: chỉ một người được trở thành người phụ trách chính; người còn lại nhận thông báo Ticket đã được tiếp nhận.
- Phân công cho người không thuộc phòng ban hiện tại: từ chối thao tác.
- Ticket đã được Transfer sang phòng ban khác trước khi thao tác hoàn tất: từ chối và hiển thị dữ liệu mới nhất.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-OWN-01`.
- Phân loại và phân công phải được ghi nhận trong lịch sử Ticket.
- Nhân viên không được tự tạo Category mới trong luồng xử lý Ticket.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-02/AC-01:** Tiếp nhận Ticket `NEW` chưa có người phụ trách gán đúng người tiếp nhận làm người phụ trách chính và chuyển Ticket sang `IN_PROGRESS`.
- **FR-STF-02/AC-02:** Hai nhân viên tiếp nhận cùng lúc: chỉ một người trở thành người phụ trách; người còn lại nhận thông báo "Ticket đã được tiếp nhận" và thấy dữ liệu mới nhất.
- **FR-STF-02/AC-03:** Danh sách phân công chỉ gồm nhân viên đang hoạt động của phòng ban hiện tại; phân công cho người ngoài phòng ban (gửi trực tiếp) bị từ chối với thông báo, người phụ trách không đổi.
- **FR-STF-02/AC-04:** Đổi Category sang Category cùng phòng ban được lưu và ghi lịch sử (Category trước/sau, người thực hiện).
- **FR-STF-02/AC-05:** Category thuộc phòng ban khác chỉ được lưu khi Transfer sang đúng phòng ban tương ứng thành công.
- **FR-STF-02/AC-06:** Ticket đã được Transfer trước khi tiếp nhận/phân công hoàn tất: thao tác bị từ chối với thông báo "Ticket đã chuyển phòng ban", màn hình tải lại dữ liệu mới nhất.
- **FR-STF-02/AC-07:** Mỗi lần tiếp nhận, phân công, phân công lại ghi lịch sử gồm người phụ trách trước/sau và người thực hiện.
- **FR-STF-02/AC-08:** Màn hình xử lý Ticket không có chức năng tạo Category mới; Category chỉ chọn từ danh mục đang hoạt động.

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (phân công/phân công lại) ở mục 4 là luồng thay thế của Luồng A (tự tiếp nhận).
- **A1 — Đổi Category sang Category cùng phòng ban:** lưu ngay, ghi lịch sử, không cần Transfer.
- **A2 — Đổi Category sang Category thuộc phòng ban khác:** hệ thống chuyển sang luồng Transfer của FR-STF-05.

#### 9. Ví dụ Edge Case
- Hai nhân viên bấm Tiếp nhận cùng lúc: chỉ một người thành người phụ trách (FR-STF-02/AC-02).
- Phân công lại cho chính người đang phụ trách: không tạo sự kiện lịch sử mới.
- Phân công cho nhân viên vừa bị khóa: bị từ chối.
- Ticket đang `WAITING_STUDENT` được phân công lại: giữ trạng thái `WAITING_STUDENT`.

---

### [FR-STF-03] Quản lý mức độ ưu tiên và thời hạn xử lý

**Priority:** Cao: thời hạn là căn cứ của Dashboard sắp quá hạn/quá hạn, mục tiêu giám sát của dự án. **Mốc giao:** MS-03.

#### 1. Mô tả & Phạm vi
Cho phép người dùng có quyền thiết lập mức độ ưu tiên của Ticket và theo dõi thời hạn xử lý tương ứng.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phụ trách Ticket hoặc Staff/Management có quyền điều chỉnh Priority theo [Actors & Roles](../../01-product/actors-and-roles.md).
- **Preconditions:** Ticket thuộc phạm vi xử lý của người dùng và đang ở một trong các trạng thái `NEW`, `IN_PROGRESS` hoặc `WAITING_STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation
- Priority chỉ nhận một trong bốn giá trị: `LOW`, `MEDIUM`, `HIGH`, `URGENT`.
- Ticket mới có Priority mặc định `MEDIUM`.
- Thời hạn mục tiêu:
  - `LOW`: 05 ngày làm việc.
  - `MEDIUM`: 03 ngày làm việc.
  - `HIGH`: 02 ngày làm việc.
  - `URGENT`: 01 ngày làm việc.
- Ticket được xem là **sắp quá hạn** khi tỷ lệ sử dụng thời hạn đạt từ 80% đến dưới 100%.
- Ticket được xem là **quá hạn** khi tỷ lệ sử dụng thời hạn đạt từ 100% trở lên và chưa ở `RESOLVED` hoặc `CLOSED`.

#### 4. Luồng xử lý chi tiết
1. Người dùng mở Ticket thuộc phạm vi xử lý.
2. Hệ thống hiển thị Priority và Deadline hiện tại.
3. Người dùng chọn Priority phù hợp.
4. Hệ thống kiểm tra quyền thực hiện.
5. Hệ thống lưu Priority mới và tính lại Deadline theo quy tắc dùng chung.
6. Hệ thống ghi nhận thay đổi Priority/Deadline vào lịch sử Ticket.
7. Danh sách công việc phản ánh trạng thái sắp quá hạn hoặc quá hạn tương ứng.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Người dùng không có quyền thay đổi Priority: từ chối thao tác.
- Ticket đã chuyển sang phạm vi khác trước khi lưu: từ chối và yêu cầu tải lại dữ liệu.
- Giá trị Priority không thuộc danh sách cho phép: không chấp nhận.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-DUE-01` và `BR-DUE-02`.
- Thời gian Ticket ở `WAITING_STUDENT` không tính vào thời gian xử lý.
- Khi Priority thay đổi, Deadline được tính lại theo công thức tại `BR-DUE-01` và `BR-DUE-02`; đồng hồ không được đặt lại từ đầu.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-03/AC-01:** Mỗi Priority cho Deadline đúng mục tiêu: `LOW` 05, `MEDIUM` 03, `HIGH` 02, `URGENT` 01 ngày làm việc.
- **FR-STF-03/AC-02:** Đổi Priority hợp lệ cập nhật Deadline bằng mục tiêu mới trừ thời gian hợp lệ đã dùng (không đặt lại đồng hồ) và ghi lịch sử Priority/Deadline trước–sau.
- **FR-STF-03/AC-03:** Ticket có tỷ lệ sử dụng thời hạn từ 80% đến dưới 100% được hiển thị là sắp quá hạn.
- **FR-STF-03/AC-04:** Ticket có tỷ lệ sử dụng thời hạn từ 100% trở lên và chưa `RESOLVED`/`CLOSED` được hiển thị là quá hạn.
- **FR-STF-03/AC-05:** Khoảng thời gian `WAITING_STUDENT` không làm tiêu hao thời gian xử lý còn lại.
- **FR-STF-03/AC-06:** Người không có quyền đổi Priority: người dùng không thấy thao tác này; nếu gửi trực tiếp tới hệ thống thì nhận thông báo "không có quyền thực hiện" và dữ liệu không đổi.
- **FR-STF-03/AC-07:** Ticket đã chuyển sang phạm vi khác trước khi lưu: thao tác bị từ chối với thông báo yêu cầu tải lại, Priority và Deadline không đổi.
- **FR-STF-03/AC-08:** Giá trị Priority ngoài `LOW`/`MEDIUM`/`HIGH`/`URGENT` gửi trực tiếp tới hệ thống bị từ chối, dữ liệu không đổi.
- **FR-STF-03/AC-09:** Deadline và thời gian SLA dùng lịch trường theo múi giờ Việt Nam, 01 ngày = 08 giờ làm việc; không tiêu hao thời gian vào thứ Bảy, Chủ nhật, ngày nghỉ lễ/nghỉ trường nạp sẵn hoặc khi WAITING_STUDENT; không bổ sung giao diện cấu hình lịch nghỉ.
- **FR-STF-03/AC-10:** Đổi Priority khi thời gian mục tiêu mới trừ thời gian hợp lệ đã dùng bằng 0 hoặc âm: Ticket chưa RESOLVED/CLOSED được đánh dấu quá hạn ngay khi lưu, không đặt lại đồng hồ và ghi lịch sử trước/sau.
- **FR-STF-03/AC-11:** Ticket RESOLVED hoặc CLOSED không cho đổi Priority dù có quyền; ẩn thao tác, yêu cầu trực tiếp bị từ chối kèm lý do trạng thái, Priority/Deadline và lịch sử cũ không đổi.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Giảm Priority** (ví dụ `HIGH` → `LOW`): Deadline tính lại bằng mục tiêu mới trừ thời gian hợp lệ đã dùng (`BR-DUE-01`), đồng hồ không đặt lại.
- **A2 — Đổi Priority khi Ticket đang `WAITING_STUDENT`:** lưu Priority và tính lại thời gian còn lại/Deadline ngay theo `BR-DUE-01`, ghi lịch sử trước–sau; nếu remaining ≤ 0 thì đánh dấu quá hạn ngay khi lưu. Đồng hồ vẫn tạm dừng, không tiêu hao thêm trong thời gian chờ. Khi quay về `IN_PROGRESS`, xác định Deadline từ lượng thời gian còn lại đã cập nhật theo `BR-DUE-02`, không đặt lại mục tiêu hoặc cộng thời gian chờ vào thời gian đã dùng.

#### 9. Ví dụ Edge Case
- Tỷ lệ sử dụng 79,9%: chưa sắp quá hạn; đúng 80%: sắp quá hạn; đúng 100%: quá hạn (FR-STF-03/AC-03, FR-STF-03/AC-04).
- Ticket tạo 16:30 thứ Sáu với `URGENT`: thời hạn chỉ tính giờ làm việc, không tính cuối tuần.
- Đặt lại cùng Priority đang có: không ghi lịch sử, không tính lại Deadline.
- Ticket đã quá hạn được nâng lên `URGENT`: vẫn ở trạng thái quá hạn, không "hết quá hạn" nhờ đổi Priority.

---

### [FR-STF-04] Xử lý Ticket và yêu cầu sinh viên bổ sung

**Priority:** Cao: thiếu thì nhân viên không xin được thông tin còn thiếu và thời hạn bị tính sai. **Mốc giao:** MS-03.

#### 1. Mô tả & Phạm vi
Cho phép nhân viên xử lý Ticket đang phụ trách, ghi nhận tiến độ và yêu cầu sinh viên bổ sung thông tin hoặc tài liệu khi dữ liệu hiện có chưa đủ để tiếp tục xử lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phụ trách Ticket; Staff có SUPPLEMENT_OVERRIDE chỉ được yêu cầu bổ sung thay người phụ trách.
- **Preconditions:** Ticket đang ở `IN_PROGRESS` và thuộc phạm vi của nhân viên.

#### 3. Quy tắc Dữ liệu & Validation
- **Nội dung cập nhật tiến độ:** nếu được ghi nhận, phải từ **10 đến 1.000 ký tự** và không được chỉ chứa khoảng trắng.
- Cập nhật tiến độ được ghi vào lịch sử xử lý nội bộ của Ticket; Student Portal chỉ hiển thị các sự kiện được phép công khai theo quy tắc của M01.
- **Yêu cầu bổ sung:** bắt buộc có nội dung mô tả rõ thông tin hoặc tài liệu cần cung cấp, từ **10 đến 1.000 ký tự**.
- Nhân viên chỉ được yêu cầu bổ sung khi Ticket đang ở `IN_PROGRESS`.

#### 4. Luồng xử lý chi tiết

**Luồng A — Cập nhật tiến độ**
1. Nhân viên mở Ticket đang phụ trách.
2. Nhân viên ghi nhận nội dung tiến độ xử lý khi cần.
3. Hệ thống lưu cập nhật vào lịch sử Ticket.
4. Ticket tiếp tục ở `IN_PROGRESS`.

**Luồng B — Yêu cầu bổ sung**
1. Nhân viên mở Ticket đang phụ trách.
2. Nhân viên chọn **Yêu cầu bổ sung**.
3. Nhân viên nhập nội dung cần sinh viên cung cấp.
4. Hệ thống kiểm tra dữ liệu và trạng thái hiện tại.
5. Hệ thống lưu yêu cầu bổ sung vào lịch sử.
6. Ticket chuyển từ `IN_PROGRESS` sang `WAITING_STUDENT`.
7. Thời gian xử lý được tạm dừng.
8. Hệ thống tạo thông báo trong hệ thống cho sinh viên.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Nội dung yêu cầu bổ sung không hợp lệ: không gửi yêu cầu.
- Ticket không còn ở `IN_PROGRESS`: từ chối thao tác.
- Không còn là người phụ trách: từ chối cập nhật tiến độ nội bộ; yêu cầu bổ sung chỉ được làm thay khi có SUPPLEMENT_OVERRIDE hợp lệ. Không còn quyền/phạm vi xử lý: từ chối.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-SUP-01` và `BR-DUE-02`.
- Yêu cầu bổ sung và phản hồi sau đó của sinh viên phải được bảo toàn trong lịch sử Ticket.
- Khi sinh viên bổ sung hợp lệ, Ticket quay về `IN_PROGRESS`.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-04/AC-01:** Cập nhật tiến độ hợp lệ (10–1.000 ký tự) được lưu vào lịch sử nội bộ của đúng Ticket; Ticket giữ `IN_PROGRESS`.
- **FR-STF-04/AC-02:** Yêu cầu bổ sung hợp lệ chuyển Ticket sang `WAITING_STUDENT`.
- **FR-STF-04/AC-03:** Sinh viên nhận thông báo trong hệ thống và xem được nội dung cần bổ sung.
- **FR-STF-04/AC-04:** Thời gian xử lý tạm dừng trong `WAITING_STUDENT` và tiếp tục khi Ticket quay về `IN_PROGRESS`.
- **FR-STF-04/AC-05:** Ticket ngoài `IN_PROGRESS`: không có thao tác yêu cầu bổ sung; yêu cầu gửi trực tiếp bị từ chối với thông báo trạng thái hiện tại, trạng thái không đổi.
- **FR-STF-04/AC-06:** Nội dung cập nhật tiến độ hoặc yêu cầu bổ sung rỗng, chỉ có khoảng trắng, dưới 10 hoặc trên 1.000 ký tự: thông báo tại trường nội dung, không lưu, trạng thái không đổi.
- **FR-STF-04/AC-07:** Nhân viên không còn là người phụ trách (và không có SUPPLEMENT_OVERRIDE hợp lệ cho thao tác yêu cầu bổ sung) hoặc đã mất quyền xử lý: cập nhật hoặc yêu cầu bổ sung bị từ chối với thông báo, không ghi lịch sử.
- **FR-STF-04/AC-08:** Yêu cầu bổ sung và phản hồi của sinh viên được giữ nguyên trong lịch sử, kể cả sau nhiều vòng bổ sung.
- **FR-STF-04/AC-09:** Sau khi sinh viên bổ sung hợp lệ (FR-STU-05/AC-01), Ticket quay về `IN_PROGRESS` và xuất hiện lại trong "Ticket của tôi" của người phụ trách.

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (yêu cầu bổ sung) ở mục 4 là luồng thay thế của Luồng A (cập nhật tiến độ).
- **A1 — Yêu cầu bổ sung lần hai** sau khi sinh viên đã bổ sung lần một: được phép, mỗi lần đều lưu trong lịch sử.

#### 9. Ví dụ Edge Case
- Nội dung 9 ký tự: từ chối; 10: chấp nhận; 1.000: chấp nhận; 1.001: từ chối.
- Yêu cầu bổ sung khi Ticket đang `WAITING_STUDENT`: bị từ chối (FR-STF-04/AC-05).
- Nhân viên vừa bị phân công lại cho người khác rồi gửi cập nhật: bị từ chối.

---

### [FR-STF-05] Chuyển xử lý và Escalation

**Priority:** Cao: Transfer tránh Ticket sai phòng ban bị kẹt. Riêng Escalation ở mức Trung bình, có thể dời qua CR nếu thiếu thời gian. **Mốc giao:** MS-03.

#### 1. Mô tả & Phạm vi
Cho phép chuyển Ticket sang **phòng ban khác** khi cần thay đổi đơn vị chịu trách nhiệm, hoặc thực hiện Escalation khi Ticket cần hỗ trợ/chuyển cấp xử lý. Việc đổi người phụ trách trong cùng phòng ban được thực hiện bằng luồng phân công lại tại FR-STF-02.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Staff có quyền Transfer/Escalation hoặc Management có quyền Transfer theo [Actors & Roles](../../01-product/actors-and-roles.md).
- **Preconditions:** Ticket thuộc phạm vi xử lý hiện tại và đang ở một trong các trạng thái `NEW`, `IN_PROGRESS` hoặc `WAITING_STUDENT`.

#### 3. Quy tắc Dữ liệu & Validation
- **Transfer sang phòng ban khác:**
  - Người dùng phải chọn **Category đích** từ danh mục Category đang hoạt động.
  - Hệ thống hiển thị phòng ban được cấu hình cho từng Category và tự xác định **phòng ban đích** từ Category đã chọn.
  - Category đích phải ánh xạ tới phòng ban khác phòng ban hiện tại.
  - Lý do Transfer bắt buộc, từ **10 đến 1.000 ký tự**.
  - Category mới và phòng ban mới chỉ được lưu khi toàn bộ thao tác Transfer thành công.
- **Escalation:**
  - Đích Escalation là **tài khoản Management có quyền tiếp nhận escalation trong phạm vi quản lý liên quan**.
  - Hệ thống chỉ hiển thị các tài khoản Management hợp lệ cho Ticket hiện tại.
  - Lý do Escalation bắt buộc, từ **10 đến 1.000 ký tự**.
  - Escalation không thay đổi Category, phòng ban, người phụ trách chính hoặc trạng thái Ticket.
- Transfer và Escalation không tạo trạng thái Ticket mới.

#### 4. Luồng xử lý chi tiết

**Luồng A — Chuyển xử lý (Transfer)**
1. Nhân viên mở Ticket.
2. Nhân viên chọn **Chuyển xử lý**.
3. Hệ thống hiển thị danh mục Category đang hoạt động kèm phòng ban được cấu hình cho từng Category.
4. Nhân viên chọn Category đích phù hợp và nhập lý do Transfer.
5. Hệ thống xác định phòng ban đích từ Category đã chọn và kiểm tra quyền, trạng thái, Category/phòng ban hợp lệ.
6. Khi toàn bộ kiểm tra hợp lệ, hệ thống cập nhật **Category và phòng ban** trong cùng một thao tác.
7. Người phụ trách hiện tại được gỡ khỏi Ticket vì Ticket đã chuyển sang phòng ban khác.
8. Ticket giữ trạng thái nghiệp vụ hiện tại phù hợp và xuất hiện trong hàng chờ của phòng ban mới.
9. Hệ thống ghi nhận Category trước/sau, phòng ban trước/sau, lý do và người thực hiện vào lịch sử.
10. Hệ thống tạo thông báo trong hệ thống cho sinh viên và phạm vi phòng ban mới.

**Luồng B — Chuyển cấp xử lý (Escalation)**
1. Nhân viên xác định Ticket vượt thẩm quyền hiện tại, cần hỗ trợ hoặc có nguy cơ quá hạn.
2. Nhân viên chọn **Escalation**.
3. Hệ thống hiển thị các tài khoản Management hợp lệ có quyền tiếp nhận escalation trong phạm vi quản lý liên quan.
4. Nhân viên chọn người nhận escalation và nhập lý do.
5. Hệ thống kiểm tra quyền, trạng thái và dữ liệu.
6. Hệ thống ghi nhận người gửi, người nhận, lý do và thời điểm Escalation vào lịch sử Ticket.
7. Category, phòng ban, người phụ trách chính và trạng thái Ticket được giữ nguyên.
8. Người phụ trách hiện tại tiếp tục chịu trách nhiệm xử lý Ticket.
9. Hệ thống gửi thông báo trong hệ thống cho người nhận Management và người phụ trách hiện tại. Sinh viên không nhận thông báo chỉ vì sự kiện Escalation nội bộ.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Transfer không có Category đích hợp lệ, Category đích vẫn thuộc phòng ban hiện tại hoặc lý do không hợp lệ: từ chối.
- Escalation không có người nhận Management hợp lệ hoặc lý do không hợp lệ: từ chối.
- Người dùng không đủ quyền: từ chối thao tác.
- Ticket đã thay đổi phạm vi/trạng thái không còn phù hợp trước khi xác nhận: từ chối và hiển thị dữ liệu mới nhất.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-OWN-02` và `BR-OWN-03`.
- Transfer/Escalation phải giữ nguyên mã Ticket, nội dung, file và lịch sử đã có.
- Transfer không tạo trạng thái mới; Category và phòng ban chịu trách nhiệm phải được cập nhật nhất quán trong cùng một thao tác.
- Transfer thành công phải gửi thông báo trong hệ thống cho sinh viên và phạm vi phòng ban mới.
- Escalation không tạo trạng thái mới, không đổi Category/phòng ban/người phụ trách và không thay thế Transfer.
- Escalation thành công phải thông báo trong hệ thống cho Management nhận escalation và người phụ trách hiện tại.
- Transfer/Escalation không tự động chuyển Ticket sang `RESOLVED` hoặc `CLOSED`.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-05/AC-01:** Transfer hợp lệ cập nhật Category và phòng ban trong cùng một thao tác theo cấu hình; mã Ticket, trạng thái, nội dung và file giữ nguyên.
- **FR-STF-05/AC-02:** Transfer sang phòng ban khác luôn gỡ người phụ trách hiện tại; Ticket xuất hiện ở hàng chờ chưa có người phụ trách của phòng ban mới.
- **FR-STF-05/AC-03:** Lịch sử Transfer ghi Category trước/sau, phòng ban trước/sau, lý do và người thực hiện; sinh viên và phòng ban mới nhận thông báo trong hệ thống.
- **FR-STF-05/AC-04:** Escalation hợp lệ được gửi tới đúng Management được chọn, giữ nguyên Category/phòng ban/người phụ trách/trạng thái và được ghi trong lịch sử.
- **FR-STF-05/AC-05:** Management nhận escalation và người phụ trách hiện tại nhận thông báo; sinh viên không nhận thông báo chỉ vì escalation.
- **FR-STF-05/AC-06:** Lịch sử có trước Transfer/Escalation được giữ nguyên.
- **FR-STF-05/AC-07:** Transfer thiếu Category đích, Category đích không hoạt động (kể cả bị vô hiệu hóa sau khi chọn nhưng trước khi xác nhận), Category đích cùng phòng ban hiện tại, hoặc lý do dưới 10/trên 1.000 ký tự: hệ thống kiểm tra lại khi xử lý yêu cầu, kể cả yêu cầu gửi trực tiếp, và từ chối với thông báo nêu trường cần sửa; Category, phòng ban, người phụ trách và trạng thái Ticket không đổi, không ghi sự kiện Transfer hoặc gửi thông báo Transfer.
- **FR-STF-05/AC-08:** Escalation không chọn người nhận Management hợp lệ hoặc lý do không hợp lệ: bị từ chối với thông báo nêu trường cần sửa; không gửi thông báo, không ghi lịch sử.
- **FR-STF-05/AC-09:** Người không có quyền Transfer/Escalation: người dùng không thấy thao tác này; nếu gửi trực tiếp tới hệ thống thì nhận thông báo "không có quyền thực hiện" và dữ liệu không đổi.
- **FR-STF-05/AC-10:** Ticket đã đổi phạm vi hoặc trạng thái (ví dụ đã `RESOLVED`) trước khi xác nhận: thao tác bị từ chối, màn hình hiển thị dữ liệu mới nhất, không thay đổi nào được lưu.
- **FR-STF-05/AC-11:** Transfer và Escalation không tạo trạng thái mới và không làm Ticket chuyển sang `RESOLVED` hoặc `CLOSED`.

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (Escalation) ở mục 4 là luồng thay thế của Luồng A (Transfer).
- **A1 — Management thực hiện Transfer** thay cho Staff: luồng giống Luồng A, người thực hiện là Management.
- **A2 — Transfer khi Ticket đang `WAITING_STUDENT`:** trạng thái giữ nguyên, thời hạn vẫn tạm dừng.

#### 9. Ví dụ Edge Case
- Chọn Category đích thuộc chính phòng ban hiện tại: bị từ chối; hướng dẫn dùng đổi Category của FR-STF-02.
- Transfer hai lần liên tiếp A → B → A: lịch sử ghi đủ hai sự kiện, mã Ticket không đổi.
- Chỉ có một tài khoản Management hợp lệ và tài khoản đó vừa bị khóa: danh sách người nhận Escalation trống, thao tác bị từ chối.
- Lý do 9 ký tự: từ chối; 10 ký tự: chấp nhận.

---

### [FR-STF-06] Ghi nhận kết quả và hoàn tất phần xử lý

**Priority:** Cao: kết quả xử lý là đầu ra chính sinh viên cần; thiếu thì Ticket không đến `RESOLVED`. **Mốc giao:** MS-04.

#### 1. Mô tả & Phạm vi
Cho phép nhân viên ghi nhận kết quả xử lý chính thức của Ticket và chuyển Ticket sang `RESOLVED` để sinh viên xem và phản hồi.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phụ trách Ticket hoặc Staff có `RESOLVE_OVERRIDE` để ghi nhận kết quả theo [Actors & Roles](../../01-product/actors-and-roles.md).
- **Preconditions:** Ticket đang ở `IN_PROGRESS` và đã đáp ứng điều kiện nghiệp vụ để có thể ghi nhận kết quả.

#### 3. Quy tắc Dữ liệu & Validation
- **Nội dung kết quả xử lý:** bắt buộc, từ **20 đến 2.000 ký tự**, không chấp nhận nội dung chỉ chứa khoảng trắng.
- **Tài liệu kết quả:** không bắt buộc; tối đa 03 file/lần, mỗi file tối đa 10 MB, định dạng PDF/PNG/JPG/JPEG.
- Chỉ Ticket ở `IN_PROGRESS` mới được chuyển sang `RESOLVED` theo luồng này.

#### 4. Luồng xử lý chi tiết

**Luồng A — Ghi nhận kết quả**
1. Nhân viên mở Ticket đang xử lý.
2. Nhân viên chọn **Ghi nhận kết quả**.
3. Nhân viên nhập nội dung kết quả và đính kèm tài liệu nếu có.
4. Hệ thống kiểm tra quyền, trạng thái và dữ liệu.
5. Hệ thống lưu kết quả xử lý.
6. Ticket chuyển từ `IN_PROGRESS` sang `RESOLVED`.
7. Hệ thống ghi nhận thời điểm giải quyết.
8. Kết quả và sự kiện thay đổi trạng thái được ghi vào lịch sử Ticket.
9. Hệ thống gửi thông báo trong hệ thống cho sinh viên.

**Luồng B — Tiếp tục xử lý Ticket được mở lại**
1. Sinh viên yêu cầu mở lại hợp lệ theo M01; Ticket chuyển từ `RESOLVED` về `IN_PROGRESS`.
2. Hệ thống kiểm tra người phụ trách của vòng xử lý trước.
3. Nếu người phụ trách đó vẫn đang hoạt động và còn thuộc phòng ban phụ trách Ticket, Ticket tiếp tục được giao cho người đó.
4. Nếu người phụ trách cũ không còn hợp lệ, hệ thống gỡ người phụ trách và đưa Ticket về hàng chờ chưa có người phụ trách của phòng ban hiện tại.
5. Ticket xuất hiện lại trong danh sách xử lý phù hợp tại Staff Operations.
6. Nếu Ticket có người phụ trách hợp lệ, hệ thống gửi thông báo trong hệ thống cho người phụ trách đó.
7. Nhân viên tiếp tục xử lý Ticket theo các luồng nghiệp vụ hiện có của M02.
8. Khi có kết quả mới, nhân viên thực hiện lại Luồng A để ghi nhận kết quả và đưa Ticket về `RESOLVED`.
9. Toàn bộ kết quả và lịch sử của vòng xử lý trước được giữ nguyên.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Thiếu nội dung kết quả hoặc nội dung không hợp lệ: không cho phép hoàn tất.
- File kết quả không đáp ứng quy tắc file: từ chối file không hợp lệ.
- Ticket không còn ở `IN_PROGRESS`: từ chối thao tác.
- Người dùng không có quyền hoàn tất Ticket: từ chối.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-LIFE-01`, `BR-FILE-01` và `BR-FILE-02`.
- `RESOLVED` chưa phải trạng thái kết thúc vòng đời.
- Sinh viên có 03 ngày làm việc để chấp nhận kết quả hoặc yêu cầu mở lại.
- M02 không mở chức năng CSAT tại `RESOLVED`; CSAT chỉ áp dụng khi Ticket đã `CLOSED`.
- Khi Ticket được mở lại hợp lệ, Ticket quay về `IN_PROGRESS`.
- Nếu người phụ trách trước đó vẫn đang hoạt động và còn thuộc phòng ban phụ trách Ticket, Ticket tiếp tục được giao cho người đó; nếu không, Ticket quay về hàng chờ chưa có người phụ trách của phòng ban hiện tại để được tiếp nhận/phân công lại.

#### 7. Tiêu chí nghiệm thu
- **FR-STF-06/AC-01:** Kết quả hợp lệ (20–2.000 ký tự, file tùy chọn) chuyển Ticket từ `IN_PROGRESS` sang `RESOLVED` và ghi thời điểm giải quyết.
- **FR-STF-06/AC-02:** Sinh viên nhận thông báo và xem được nội dung/tài liệu kết quả thuộc Ticket của mình.
- **FR-STF-06/AC-03:** Thiếu nội dung kết quả, hoặc nội dung dưới 20/trên 2.000 ký tự: thông báo tại trường kết quả, Ticket giữ `IN_PROGRESS`.
- **FR-STF-06/AC-04:** Ghi nhận kết quả không làm mất lịch sử xử lý trước đó.
- **FR-STF-06/AC-05:** Ticket được mở lại hợp lệ quay về `IN_PROGRESS`; hệ thống giữ người phụ trách cũ nếu vẫn hợp lệ, nếu không Ticket quay về hàng chờ chưa có người phụ trách của phòng ban hiện tại.
- **FR-STF-06/AC-06:** Ticket mở lại có người phụ trách cũ còn hợp lệ xuất hiện lại trong danh sách xử lý của người đó và người phụ trách nhận thông báo trong hệ thống.
- **FR-STF-06/AC-07:** Ticket mở lại không còn người phụ trách hợp lệ xuất hiện trong hàng chờ chưa có người phụ trách của phòng ban hiện tại để được tiếp nhận hoặc phân công lại.
- **FR-STF-06/AC-08:** File kết quả sai định dạng, trên 10 MB hoặc vượt 03 file: file đó bị loại kèm thông báo nêu lý do, file hợp lệ được giữ.
- **FR-STF-06/AC-09:** Ticket không còn ở `IN_PROGRESS`, hoặc người dùng không có quyền ghi kết quả (bao gồm mọi tài khoản Management): thao tác bị từ chối với thông báo, trạng thái không đổi.
- **FR-STF-06/AC-10:** Khi Ticket `RESOLVED`, Staff Operations không có chức năng CSAT; sinh viên chỉ thấy form đánh giá sau khi Ticket `CLOSED` (FR-STU-07).
- **FR-STF-06/AC-11:** Ticket `RESOLVED` chưa kết thúc vòng đời: sinh viên vẫn chấp nhận hoặc mở lại được trong 03 ngày làm việc (FR-STU-06/AC-02, FR-STU-06/AC-03, FR-STU-06/AC-05).

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (tiếp tục xử lý Ticket mở lại) ở mục 4 là luồng thay thế sau khi sinh viên mở lại.
- **A1 — Staff được ủy quyền ghi kết quả** thay cho Staff đang vắng, nếu có `RESOLVE_OVERRIDE` và đúng phạm vi. Management không được ghi kết quả/chuyển `RESOLVED`.

#### 9. Ví dụ Edge Case
- Nội dung kết quả 19 ký tự: từ chối; 20: chấp nhận.
- Người phụ trách cũ bị khóa trước khi sinh viên mở lại: Ticket về hàng chờ chưa có người phụ trách (FR-STF-06/AC-07).
- Ghi kết quả đúng lúc sinh viên gửi bổ sung: chỉ một thao tác thành công; thao tác kia thấy trạng thái mới nhất.

---

## III. QUY TẮC THAM CHIẾU

Các Functional Requirements của M02 phải tuân thủ thống nhất với:

- [Ticket Lifecycle](../../02-domain/ticket-lifecycle.md)
- [State Transition](../../02-domain/state-transition.md)
- [Business Rules](../../02-domain/business-rules.md)
