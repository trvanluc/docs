# Phân Hệ Nhân Viên (M02 - Staff Operations)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ Nhân viên cung cấp không gian làm việc chuyên môn cho Cán bộ / Nhân viên các phòng ban tại Aurora University. Phân hệ bao gồm các nhóm chức năng chính: Quản lý Queue Ticket phòng ban, Tiếp nhận & Phân loại, Chuyển tiếp liên phòng ban, Yêu cầu bổ sung hồ sơ, Cập nhật tiến độ xử lý, Ghi nhận kết quả và Đóng Ticket.

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-STF-01] Nhân viên đăng nhập hệ thống

#### 1. Mô tả & Phạm vi
Cho phép Nhân viên đăng nhập bằng tài khoản công vụ (Email/Username) do nhà trường cấp. Hệ thống xác thực, trả về Token và cấp quyền truy cập vào Workspace của Phòng ban tương ứng.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phòng ban (Staff).
- **Preconditions:** Tài khoản đã được Quản trị viên/Quản lý khởi tạo, được gán đúng `Department_ID` và ở trạng thái `ACTIVE`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Trường dữ liệu đầu vào:**
  - **Username / Email:** Bắt buộc, tự động `trim()` khoảng trắng hai đầu.
  - **Password:** Bắt buộc, độ dài 6 - 50 ký tự.
- **Scope & Session Context:** Sau khi xác thực thành công, Token phải chứa các thông báo context: `user_id`, `role = STAFF`, `department_id`, `permissions_list`.

#### 4. Giao diện & Hành vi UI/UX (UI States)
- **Trạng thái Nút Đăng nhập:** Disable khi thông tin trống. Chuyển Loading (kèm spinner) và khóa toàn bộ Form khi request đang được xử lý.
- **Redirect Rule:** Đăng nhập thành công -> Tự động điều hướng về `/staff/dashboard` (Hiển thị Queue Ticket của phòng ban).

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Nhân viên truy cập `/staff/login`.
2. Kiểm tra phiên làm việc: Nếu Token hợp lệ -> Chuyển hướng sang `/staff/dashboard`.
3. Nhập Username/Email và Password, nhấn Đăng nhập (hoặc phím Enter).
4. Client validate form -> Gửi request đăng nhập.
5. Server xác thực thông tin, kiểm tra vai trò `STAFF`:
   - Trả về Token xác thực (JWT) + Profile (`staff_id`, `full_name`, `department_id`).
6. Client lưu Token an toàn, chuyển hướng sang `/staff/dashboard`.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Credential không đúng (401 Unauthorized):** Hiển thị Alert error: *"Tài khoản hoặc mật khẩu không chính xác."*
- **Tài khoản không phải STAFF (403 Forbidden):** Hiển thị Alert error: *"Tài khoản của bạn không có quyền truy cập cổng Nhân viên."*
- **Tài khoản bị khóa (403 Forbidden / INACTIVE):** Hiển thị Alert error: *"Tài khoản nhân viên đã bị vô hiệu hóa. Vui lòng liên hệ Quản trị viên."*

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Đăng nhập đúng tài khoản Staff -> Chuyển sang Dashboard hiển thị danh sách Ticket của đúng phòng ban đó trong dưới 1.5s.
- **AC-02:** Tài khoản sinh viên cố gắng đăng nhập tại cổng Staff -> Báo lỗi 403 từ chối truy cập.
- **AC-03:** Click Đăng nhập liên tiếp -> Chỉ phát sinh 01 request duy nhất.

---

### [FR-STF-02] Tiếp nhận và phân loại yêu cầu (Claim & Triage)

#### 1. Mô tả & Phạm vi
Cung cấp giao diện Queue công việc chung của Phòng ban. Cho phép nhân viên duyệt qua các Ticket mới (`NEW`), đánh giá nội dung, điều chỉnh Mức độ ưu tiên (Priority) và Phân loại lại nhóm vấn đề (Category) nếu cần, sau đó Tiếp nhận (Claim) Ticket về danh sách cá nhân xử lý.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên phòng ban.
- **Preconditions:** Ticket đang ở trạng thái `NEW` hoặc `TRANSFERRED`, thuộc `Department_ID` của nhân viên.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Mức độ ưu tiên (Priority):** Enum bắt buộc: `LOW` (Thấp), `MEDIUM` (Trung bình - Mặc định), `HIGH` (Cao), `URGENT` (Khẩn cấp).
- **Phân loại vấn đề (Category):** Dropdown lấy danh sách Category thuộc phòng ban hiện tại.
- **Trạng thái đích:** Chuyển từ `NEW` / `TRANSFERRED` -> `IN_PROGRESS`.
- **Gán phụ trách:** Ghi nhận `assignee_id = current_staff_id`.

#### 4. Cơ chế chống tranh chấp tiếp nhận (Concurrency Control / Optimistic Locking)
- **Bài toán:** Hai nhân viên A và B cùng mở 1 Ticket `NEW` và cùng bấm nút Tiếp nhận xử lý tại 1 thời điểm.
- **Cơ chế xử lý:**
  - Server sử dụng DB Locking / Version check (hoặc `UPDATE tickets SET status='IN_PROGRESS', assignee_id=? WHERE id=? AND status IN ('NEW', 'TRANSFERRED')`).
  - Người gửi request thành công trước sẽ chiếm quyền phụ trách.
  - Người gửi request sau 1 millisecond sẽ nhận phản hồi lỗi 409 Conflict.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Nhân viên truy cập Tab "Ticket chưa tiếp nhận" (`/staff/queue`).
2. Chọn một Ticket để mở trang Chi tiết (`/staff/tickets/{ticket_id}`).
3. Nhân viên xem mô tả, đính kèm. Chọn/điều chỉnh Priority và Category nếu sinh viên chọn chưa đúng.
4. Nhấn nút Tiếp nhận xử lý.
5. Client gửi request claim kèm theo Ticket ID và thông tin Priority/Category đã điều chỉnh.
6. Server kiểm tra điều kiện lock:
   - Nếu Ticket vẫn ở trạng thái `NEW` / `TRANSFERRED` -> Cập nhật `status = IN_PROGRESS`, `assignee_id = current_staff_id`, lưu log thao tác. Trả về HTTP 200 OK.
   - Nếu Ticket đã bị người khác claim -> Trả về HTTP 409 Conflict.
7. Client nhận 200 OK: Cập nhật UI, hiển thị Toast *"Đã tiếp nhận Ticket thành công"*, chuyển Ticket sang Tab "Ticket của tôi".

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Ticket đã bị gán cho người khác (409 Conflict):** Hiển thị Alert error: *"Ticket này đã được tiếp nhận bởi nhân viên [Tên_Nhân_Viên] trước đó ít giây."* Tự động reload lại trang để khóa nút Tiếp nhận.

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Tiếp nhận Ticket thành công -> Trạng thái đổi sang `IN_PROGRESS`, trường người phụ trách hiển thị tên nhân viên hiện tại.
- **AC-02:** Hai nhân viên bấm Tiếp nhận cùng lúc -> Đúng 01 người nhận thành công, người còn lại nhận thông báo lỗi rõ ràng và UI tự cập nhật.
- **AC-03:** Thay đổi Priority từ `MEDIUM` sang `URGENT` trong lúc Claim -> Dữ liệu lưu đúng Priority mới vào CSDL.

---

### [FR-STF-03] Chuyển sang đúng phòng ban hoặc người phụ trách (Transfer Ticket)

#### 1. Mô tả & Phạm vi
Cho phép nhân viên chuyển tiếp Ticket sang một Phòng ban khác (hoặc điều chuyển nội bộ sang Nhân viên khác cùng phòng) nếu yêu cầu gửi nhầm đơn vị hoặc vượt quá thẩm quyền giải quyết.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đang phụ trách Ticket (`assignee_id == current_staff_id`) hoặc Nhân viên thuộc phòng ban đang giữ Ticket.
- **Preconditions:** Ticket có trạng thái `NEW`, `IN_PROGRESS`, `NEED_MORE_INFO` (Chưa ở trạng thái `CLOSED`).

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Phòng ban đích (Target Department):** Dropdown bắt buộc chọn, khác với phòng ban hiện tại.
- **Lý do chuyển tiếp (Transfer Note):** Bắt buộc nhập, chuỗi từ 10 đến 500 ký tự. Tự động `trim()`. Không chấp nhận chuỗi chỉ chứa khoảng trắng.
- **Chuyển đổi trạng thái & Cập nhật trường:**
  - `status = TRANSFERRED`
  - `department_id = target_department_id`
  - `assignee_id = NULL` (Xóa người phụ trách cũ, đẩy vào Queue chờ của phòng ban mới).

#### 4. Ghi vết lịch sử chuyển tiếp (Audit Log Spec)
- Mỗi lần chuyển phòng ban, hệ thống BẮT BUỘC lưu 01 record vào bảng Audit Log / Ticket History gồm các trường: `ticket_id`, `action = TRANSFER`, `from_department_id`, `to_department_id`, `performed_by_staff_id`, `reason_note`, `created_at`.

#### 5. Luồng xử lý chi tiết (Flow of Events)
1. Trong màn hình chi tiết Ticket, nhân viên bấm Chuyển phòng ban.
2. Modal Chuyển phòng ban hiển thị:
   - Dropdown chọn Target Department.
   - Textarea nhập Reason Note.
3. Nhập dữ liệu và bấm Xác nhận chuyển.
4. Client validate dữ liệu (Bắt buộc chọn phòng ban và nhập lý do >= 10 ký tự).
5. Client gửi request transfer.
6. Server cập nhật `department_id`, `status = TRANSFERRED`, `assignee_id = NULL`, ghi nhận Audit Log. Gửi thông báo (Notification) đến Queue của Phòng ban mới.
7. Client đóng Modal, hiển thị Toast thành công và điều hướng nhân viên về danh sách công việc chung.

#### 6. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Bỏ trống lý do / Lý do quá ngắn (400 Bad Request):** Hiển thị lỗi validation ngay dưới Textarea: *"Lý do chuyển tiếp phải từ 10 đến 500 ký tự."*
- **Chọn trùng phòng ban hiện tại (400 Bad Request):** Disable phòng ban hiện tại trong dropdown list.

#### 7. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Chuyển phòng ban thành công -> Ticket biến mất khỏi Tab "Cá nhân xử lý", xuất hiện trong Queue "Chờ tiếp nhận" của Phòng ban mới.
- **AC-02:** Nhập lý do chỉ gồm khoảng trắng -> Nút Xác nhận bị khóa hoặc báo lỗi validation.
- **AC-03:** Mở Lịch sử Ticket (Timeline) -> Hiển thị chínhეც log: *"Nhân viên A đã chuyển Ticket từ Phòng Đào tạo sang Phòng Tài chính. Lý do: [Nội dung lý do]"*.

---

### [FR-STF-04] Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement)

#### 1. Mô tả & Phạm vi
Cho phép Nhân viên gửi yêu cầu trực tiếp đến Sinh viên để yêu cầu giải thích thêm hoặc upload bổ sung các file/giấy tờ minh chứng còn thiếu trước khi có thể xử lý tiếp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đang phụ trách Ticket (`assignee_id == current_staff_id`).
- **Preconditions:** Ticket ở trạng thái `IN_PROGRESS`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Nội dung yêu cầu bổ sung (Request Note):** Bắt buộc nhập, chuỗi từ 10 đến 1000 ký tự. Không chứa toàn khoảng trắng. Tự động `trim()`.
- **Danh mục giấy tờ cần bổ sung (Requested Documents Checkbox/Text):** Chọn từ danh sách mẫu hoặc nhập tự do để sinh viên dễ hình dung.
- **Thay đổi trạng thái:** Chuyển từ `IN_PROGRESS` -> `NEED_MORE_INFO`.

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Trong màn chi tiết Ticket, nhân viên chọn nút Yêu cầu bổ sung hồ sơ.
2. Hiển thị Form nhập nội dung yêu cầu.
3. Nhân viên nhập chi tiết các giấy tờ/thông tin sinh viên cần cung cấp thêm, nhấn Gửi yêu cầu.
4. Client thực hiện validate client-side.
5. Client gửi request cập nhật.
6. Server cập nhật `status = NEED_MORE_INFO`, lưu tin nhắn vào Conversation log, phát Notification (In-app / Email) cho Sinh viên.
7. Client hiển thị Toast success: *"Đã gửi yêu cầu bổ sung thông tin tới sinh viên"*, cập nhật Badge trạng thái trên UI thành `NEED_MORE_INFO`.

#### 5. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Ticket bị thay đổi trạng thái bởi thao tác khác (400 Bad Request):** Nếu Ticket không còn ở `IN_PROGRESS` (ví dụ bị Quản lý can thiệp đóng), báo lỗi: *"Ticket không ở trạng thái cho phép yêu cầu bổ sung."*

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Gửi yêu cầu thành công -> Trạng thái Ticket đổi sang `NEED_MORE_INFO`, sinh viên thấy nội dung yêu cầu này trên Cổng Sinh viên.
- **AC-02:** Không cho phép gửi tin nhắn rỗng hoặc chỉ chứa khoảng trắng.

---

### [FR-STF-05] Ghi lại kết quả và đóng yêu cầu (Complete & Resolve Ticket)

#### 1. Mô tả & Phạm vi
Cho phép Nhân viên nhập kết quả giải quyết chi tiết, đính kèm file kết quả (nếu có) và đóng Ticket sau khi đã hoàn thành công tác xử lý nghiệp vụ.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Nhân viên đang phụ trách Ticket.
- **Preconditions:** Ticket đang ở trạng thái `IN_PROGRESS`.

#### 3. Quy tắc Dữ liệu & Validation (Data Contracts)
- **Nội dung kết quả giải quyết (Resolution Detail):** Bắt buộc nhập, chuỗi từ 20 đến 2000 ký tự. Tự động `trim()`. Không chấp nhận chuỗi chỉ chứa khoảng trắng.
- **File đính kèm kết quả (Resolution Attachments):** Optional. Tối đa 3 file, mỗi file <= 5MB, định dạng `.pdf`, `.png`, `.jpg`, `.jpeg`.
- **Chuyển đổi trạng thái:**
  - Chuyển `status` từ `IN_PROGRESS` -> `RESOLVED` (Hoặc `CLOSED` tùy cấu hình luồng tự động đóng).
  - Cập nhật timestamp `resolved_at = CURRENT_TIMESTAMP`.

#### 4. Luồng xử lý chi tiết (Flow of Events)
1. Nhân viên chọn nút Hoàn tất & Đóng Ticket.
2. Hiển thị Form Ghi nhận kết quả giải quyết:
   - Textarea nhập Resolution Detail.
   - Khu vực Upload file đính kèm kết quả.
3. Nhân viên nhập kết quả, đính kèm file (nếu có) và nhấn Đóng yêu cầu.
4. Client kiểm tra validation dữ liệu.
5. Client gửi request hoàn tất.
6. Server lưu thông tin kết quả giải quyết, file đính kèm kết quả, cập nhật `status = RESOLVED` (hoặc `CLOSED`), lưu `resolved_at`, phát Notification báo kết quả cho Sinh viên.
7. Client cập nhật UI: Chuyển Ticket sang trạng thái Đã đóng, ẩn các button thao tác xử lý.

#### 5. Luồng ngoại lệ & Mã lỗi (Alternative & Error Flows)
- **Để trống kết quả hoặc chỉ nhập khoảng trắng (400 Bad Request):** Hiển thị lỗi ngay tại Client: *"Nội dung kết quả giải quyết không được let trống (tối thiểu 20 ký tự)."*
- **Upload file kết quả lỗi (400 Bad Request / 500):** Ngắt tiến trình đóng Ticket, giữ nguyên dữ liệu đã nhập trên Form, hiển thị thông báo lỗi upload file.

#### 6. Tiêu chí nghiệm thu (Acceptance Criteria)
- **AC-01:** Nhập kết quả >= 20 ký tự + bấm Đóng -> Ticket đổi sang trạng thái `RESOLVED`/`CLOSED`, thời gian hoàn thành ghi nhận chính xác. Sinh viên xem được đầy đủ câu trả lời này.
- **AC-02:** Nhập dưới 20 ký tự hoặc cố tình spam spacebar -> Báo lỗi validation, không cho gửi request.
- **AC-03:** Ticket đã đóng -> Khóa toàn bộ các nút thao tác (Tiếp nhận, Chuyển phòng, Yêu cầu bổ sung).

---

## III. BẢNG MÃ LỖI CHUẨN DÙNG CHUNG PHÂN HỆ STAFF (SYSTEM ERROR CODES)

| HTTP Status | Error Code | Message hiển thị người dùng | Kịch bản áp dụng |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | *"Dữ liệu nhập vào không hợp lệ. Vui lòng kiểm tra lại."* | Lỗi validation trường dữ liệu đầu vào. |
| **400** | `INVALID_TICKET_STATE` | *"Trạng thái Ticket hiện tại không cho phép thực hiện thao tác này."* | Thao tác sai luồng trạng thái (VD: Yêu cầu bổ sung khi Ticket đã đóng). |
| **400** | `MISSING_TRANSFER_REASON` | *"Vui lòng nhập lý do chuyển phòng ban (tối thiểu 10 ký tự)."* | Không nhập lý do khi chuyển tiếp. |
| **401** | `UNAUTHORIZED` | *"Phiên đăng nhập hết hạn. Vui lòng đăng nhập lại."* | Token Staff hết hạn. |
| **403** | `FORBIDDEN_STAFF_ACCESS` | *"Bạn không có quyền thao tác trên Ticket của phòng ban khác."* | Staff cố truy cập/chỉnh sửa Ticket không thuộc thẩm quyền. |
| **409** | `TICKET_ALREADY_CLAIMED` | *"Ticket này đã được tiếp nhận bởi nhân viên [Tên_Staff] trước đó."* | Xảy ra tranh chấp khi 2 Staff bấm Claim cùng lúc. |
| **500** | `INTERNAL_SERVER_ERROR` | *"Hệ thống gặp sự cố kỹ thuật. Vui lòng thử lại sau."* | Lỗi Server/Database unhandled. |