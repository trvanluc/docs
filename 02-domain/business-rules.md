# Quy Tắc Nghiệp Vụ Cốt Lõi (Business Rules)

Tài liệu này quy định các Business Rules dùng chung cho **UniSupport**. Các quy tắc trong phần này được áp dụng nhất quán giữa Student Portal, Staff Operations và Management Dashboard, đồng thời là cơ sở để xây dựng Functional Requirements và Acceptance Criteria.

## 1. File Đính Kèm (`BR-FILE`)

### `BR-FILE-01` — Quyền truy cập file đính kèm

- File đính kèm của Ticket chỉ được truy cập bởi người dùng có liên quan và có quyền phù hợp.
- Sinh viên chỉ được xem file thuộc Ticket của chính mình.
- Nhân viên chỉ được xem file của Ticket thuộc phạm vi xử lý được phân quyền.
- Người dùng Management chỉ được truy cập file khi quyền được cấp cho phép phục vụ quản lý hoặc tra soát.
- Việc chuyển Ticket sang người/phòng ban khác không làm mất các file đã được ghi nhận trước đó.

### `BR-FILE-02` — Định dạng, dung lượng và số lượng file

- Định dạng được chấp nhận: **PDF, PNG, JPG/JPEG**.
- Dung lượng tối đa: **10 MB cho mỗi file**.
- Tối đa **03 file** cho mỗi lần tạo Ticket, mỗi lần bổ sung thông tin hoặc mỗi lần ghi nhận tài liệu kết quả.
- File không đáp ứng định dạng hoặc dung lượng cho phép phải bị từ chối trước khi được gắn vào Ticket.

---

## 2. Phân Công, Chuyển Xử Lý và Escalation (`BR-OWN`)

### `BR-OWN-01` — Phân công người phụ trách

- Ticket phải xác định được phòng ban phụ trách trong quá trình xử lý.
- Một Ticket có **tối đa 01 người phụ trách chính tại một thời điểm**.
- Ticket có thể chưa có người phụ trách cụ thể khi vừa được tạo, khi chưa được tiếp nhận/phân công hoặc sau khi được chuyển sang phòng ban khác.
- Mọi thay đổi người phụ trách phải được ghi nhận trong lịch sử Ticket.

### `BR-OWN-02` — Chuyển xử lý

- Transfer được sử dụng khi Ticket cần chuyển sang **phòng ban khác** chịu trách nhiệm xử lý.
- Mỗi Category được cấu hình với một phòng ban tiếp nhận mặc định. Khi Transfer sang phòng ban khác, người thực hiện phải chọn **Category đích** phù hợp; hệ thống xác định phòng ban đích từ cấu hình của Category đó.
- Category đích phải đang hoạt động và phải ánh xạ tới phòng ban khác phòng ban hiện tại.
- Category mới và phòng ban mới chỉ được cập nhật khi toàn bộ thao tác Transfer thành công; không được lưu trạng thái Category/phòng ban không nhất quán.
- Người thực hiện chuyển phải nhập **lý do từ 10 đến 1.000 ký tự**.
- Khi Transfer thành công, người phụ trách hiện tại được gỡ khỏi Ticket và phòng ban mới thực hiện tiếp nhận/phân công lại.
- Lịch sử Transfer phải ghi nhận tối thiểu: Category trước/sau, phòng ban trước/sau, lý do và người thực hiện.
- Transfer không làm mất nội dung, file đính kèm, kết quả trung gian hoặc lịch sử trước đó.
- Transfer không tạo trạng thái vòng đời mới; Ticket giữ trạng thái nghiệp vụ hiện tại phù hợp.

### `BR-OWN-03` — Escalation

- Escalation được sử dụng khi Ticket vượt quá thẩm quyền xử lý hiện tại, cần hỗ trợ từ cấp quản lý hoặc có nguy cơ không đáp ứng thời hạn xử lý.
- Đích Escalation là **tài khoản Management có quyền tiếp nhận escalation trong phạm vi quản lý liên quan**. Hệ thống chỉ hiển thị các đích Management hợp lệ cho Ticket hiện tại.
- Người thực hiện phải chọn đích Escalation và nhập **lý do từ 10 đến 1.000 ký tự**.
- Escalation **không thay đổi Category, phòng ban phụ trách, người phụ trách chính hoặc trạng thái Ticket**.
- Người phụ trách hiện tại tiếp tục chịu trách nhiệm xử lý Ticket cho đến khi có một thao tác Transfer hoặc phân công lại riêng biệt.
- Escalation phải giữ nguyên toàn bộ lịch sử và được ghi nhận như một sự kiện riêng, bao gồm người gửi escalation, người nhận escalation, lý do và thời điểm.
- Khi Escalation thành công, thông báo trong hệ thống được gửi cho người nhận Management và người phụ trách hiện tại. Sinh viên không nhận thông báo chỉ vì sự kiện Escalation nội bộ.

---

## 3. Mức Độ Ưu Tiên và Thời Hạn Xử Lý (`BR-DUE`)

### `BR-DUE-01` — Mức độ ưu tiên và thời hạn mục tiêu

UniSupport sử dụng bốn mức độ ưu tiên:

| Mức độ | Thời hạn xử lý mục tiêu |
| :--- | :--- |
| **Thấp (LOW)** | 05 ngày làm việc |
| **Trung bình (MEDIUM)** | 03 ngày làm việc |
| **Cao (HIGH)** | 02 ngày làm việc |
| **Khẩn cấp (URGENT)** | 01 ngày làm việc |

- Ticket mới được áp dụng mức **Trung bình (MEDIUM)** mặc định.
- Đồng hồ thời hạn bắt đầu từ **thời điểm Ticket được tạo thành công**, không phải từ thời điểm nhân viên tiếp nhận.
- Thời gian xử lý mục tiêu hiện tại được xác định theo Priority hiện tại của Ticket.
- Khi Priority thay đổi, hệ thống **không đặt lại đồng hồ về 0**. Hệ thống giữ nguyên tổng thời gian xử lý hợp lệ đã sử dụng và tính lại thời gian còn lại theo công thức:

  **Thời gian còn lại = Thời gian mục tiêu của Priority mới − Thời gian xử lý hợp lệ đã sử dụng**

- Nếu thời gian còn lại lớn hơn 0, Deadline mới được xác định bằng cách cộng phần thời gian còn lại vào lịch làm việc kể từ thời điểm thay đổi Priority.
- Nếu thời gian còn lại nhỏ hơn hoặc bằng 0, Ticket được xem là **quá hạn ngay tại thời điểm thay đổi Priority**.
- Ví dụ: Ticket `MEDIUM` có mục tiêu 03 ngày làm việc và đã sử dụng 01 ngày làm việc hợp lệ. Khi đổi sang `HIGH` có mục tiêu 02 ngày, Ticket còn **01 ngày làm việc** để xử lý.
- Việc thay đổi Priority phải có quyền phù hợp và được ghi nhận trong lịch sử Ticket.

### `BR-DUE-02` — Cách tính ngày làm việc và tình trạng thời hạn

- UniSupport sử dụng lịch làm việc của Aurora University theo múi giờ Việt Nam.
- **Ngày làm việc** là thứ Hai đến thứ Sáu, không bao gồm ngày nghỉ lễ hoặc ngày nghỉ chính thức của Aurora University.
- Một ngày làm việc được quy đổi thành **08 giờ làm việc** để tính thời lượng SLA.
- **Thời gian xử lý hợp lệ đã sử dụng** là tổng thời gian làm việc từ lúc Ticket được tạo đến thời điểm hiện tại, sau khi loại trừ toàn bộ khoảng thời gian Ticket ở `WAITING_STUDENT` và các khoảng thời gian ngoài lịch làm việc.
- Khi Ticket chuyển sang `WAITING_STUDENT`, đồng hồ thời hạn tạm dừng tại thời điểm chuyển trạng thái.
- Khi sinh viên bổ sung hợp lệ và Ticket quay lại `IN_PROGRESS`, đồng hồ tiếp tục từ đúng lượng thời gian còn lại trước khi tạm dừng; thời gian chờ sinh viên không được cộng vào thời gian đã sử dụng.
- Tỷ lệ sử dụng thời hạn được tính theo công thức:

  **Tỷ lệ sử dụng = Thời gian xử lý hợp lệ đã sử dụng / Thời gian mục tiêu hiện tại**

- Ticket được xem là **sắp quá hạn** khi tỷ lệ sử dụng đạt từ **80% đến dưới 100%**.
- Ticket được xem là **quá hạn** khi tỷ lệ sử dụng đạt từ **100% trở lên** và Ticket chưa chuyển sang `RESOLVED` hoặc `CLOSED`.
- Các phép tính Deadline, sắp quá hạn và quá hạn phải sử dụng cùng một lịch làm việc và cùng cách loại trừ thời gian `WAITING_STUDENT`.
- Khi tính **thời gian xử lý phục vụ báo cáo hiệu quả**, chỉ cộng các khoảng thời gian Ticket thực sự nằm trong quá trình xử lý hợp lệ. Đồng hồ dừng khi Ticket chuyển sang `RESOLVED`; nếu Ticket được mở lại về `IN_PROGRESS`, đồng hồ tiếp tục tính cho vòng xử lý mới. Khoảng thời gian Ticket ở `RESOLVED` để chờ sinh viên phản hồi không được tính vào thời gian xử lý của nhân viên.

---

## 4. Yêu Cầu Bổ Sung Thông Tin (`BR-SUP`)

### `BR-SUP-01` — Chờ sinh viên bổ sung

- Nhân viên chỉ được yêu cầu bổ sung khi Ticket đang trong quá trình xử lý và thông tin hiện có chưa đủ để tiếp tục.
- Nội dung yêu cầu bổ sung phải nêu rõ thông tin hoặc tài liệu cần cung cấp.
- Sau khi yêu cầu bổ sung được gửi, Ticket chuyển sang `WAITING_STUDENT`.
- Trong thời gian `WAITING_STUDENT`, thời hạn xử lý được tạm dừng theo `BR-DUE-02`.
- Khi sinh viên bổ sung thông tin hoặc tài liệu hợp lệ, Ticket quay lại `IN_PROGRESS`.
- Yêu cầu bổ sung và phản hồi của sinh viên phải được ghi nhận trong lịch sử Ticket.

---

## 5. Hoàn Tất, Phản Hồi và Mở Lại Ticket (`BR-LIFE`)

### `BR-LIFE-01` — Chuyển sang RESOLVED

- Ticket chỉ được chuyển từ `IN_PROGRESS` sang `RESOLVED` khi đã có kết quả xử lý.
- Nội dung kết quả xử lý là thông tin bắt buộc trước khi Ticket được đánh dấu `RESOLVED`.
- Khi Ticket chuyển sang `RESOLVED`, sinh viên phải nhận được thông báo và có quyền xem kết quả.

### `BR-LIFE-02` — Thời hạn phản hồi và tự động đóng

- Sinh viên có **03 ngày làm việc** kể từ thời điểm Ticket chuyển sang `RESOLVED` để phản hồi kết quả.
- Nếu sinh viên chấp nhận kết quả, Ticket được chuyển sang `CLOSED`.
- Nếu hết **03 ngày làm việc** mà không có phản hồi yêu cầu xử lý tiếp, hệ thống chuyển Ticket sang `CLOSED`.
- Thời điểm đóng phải được ghi nhận trong lịch sử Ticket.

### `BR-LIFE-03` — Mở lại Ticket

- Mở lại chỉ được thực hiện khi Ticket đang ở trạng thái `RESOLVED` và còn trong thời hạn phản hồi.
- Sinh viên phải cung cấp lý do cho biết vấn đề chưa được giải quyết.
- Ticket hợp lệ được mở lại sẽ chuyển từ `RESOLVED` về `IN_PROGRESS`.
- Việc mở lại không xóa kết quả, thời điểm giải quyết hoặc lịch sử của vòng xử lý trước.
- Ticket đã chuyển sang `CLOSED` không được mở lại; nếu phát sinh nhu cầu hỗ trợ mới, sinh viên tạo Ticket mới.

---

## 6. Đánh Giá Mức Độ Hài Lòng (`BR-CSAT`)

### `BR-CSAT-01` — Điều kiện và thời hạn đánh giá

- Sinh viên được đánh giá khi Ticket đã ở trạng thái `CLOSED`.
- Mỗi Ticket chỉ được gửi **01 đánh giá**.
- Điểm đánh giá sử dụng thang **1 đến 5 sao**.
- Nội dung nhận xét bổ sung là không bắt buộc.
- Sinh viên có **07 ngày theo lịch** kể từ thời điểm Ticket chuyển sang `CLOSED` để gửi đánh giá.
- Sau thời hạn trên, Ticket vẫn được lưu phục vụ tra cứu nhưng không còn nhận đánh giá mới.
- **CSAT trung bình theo kỳ báo cáo** được tính từ các đánh giá hợp lệ có thời điểm gửi đánh giá nằm trong khoảng báo cáo.
- **Tỷ lệ phản hồi CSAT theo kỳ báo cáo** được tính trên các Ticket có thời điểm chuyển sang `CLOSED` nằm trong khoảng báo cáo và đã hết đủ 07 ngày theo lịch để đánh giá. Ticket chưa hết thời hạn đánh giá không được đưa vào mẫu số.

---

## 7. Lịch Sử Xử Lý và Tra Soát (`BR-AUD`)

### `BR-AUD-01` — Ghi nhận lịch sử Ticket

Các sự kiện quan trọng phải được ghi nhận trong lịch sử Ticket, tối thiểu gồm:

- Tạo Ticket.
- Phân loại và phân công.
- Thay đổi trạng thái.
- Thay đổi mức độ ưu tiên hoặc thời hạn xử lý.
- Yêu cầu và tiếp nhận thông tin bổ sung.
- Chuyển người/phòng ban xử lý.
- Escalation.
- Ghi nhận kết quả xử lý.
- Mở lại Ticket.
- Đóng Ticket.

Mỗi sự kiện phải xác định được nội dung thay đổi, người hoặc hệ thống thực hiện và thời điểm phát sinh.

### `BR-AUD-02` — Tính toàn vẹn của nhật ký tra soát

- Các bản ghi lịch sử/tra soát không được chỉnh sửa hoặc xóa thông qua chức năng thông thường của ứng dụng, kể cả bởi tài khoản Management.
- Việc xử lý dữ liệu tra soát đã hết thời hạn lưu trữ chỉ được thực hiện theo chính sách lưu trữ được phê duyệt và không được làm mất dấu vết trái với chính sách đó.
- Lịch sử Ticket phải được bảo toàn khi Ticket được phân công lại, chuyển xử lý, escalation, mở lại hoặc đóng.
