# Quy Tắc Nghiệp Vụ Bắt Buộc (Business Rules Specification)

## 1. Tổng Quan
Tài liệu này tập hợp toàn bộ các Quy tắc Nghiệp vụ Cốt lõi (Business Rules - BR) bắt buộc phải được cài đặt chặt chẽ ở cả 2 lớp: **Client-side Validation** (Giao diện người dùng) và **Server-side Validation & Database Constraints** (Logic dịch vụ Backend). Các vi phạm quy tắc phải lập tức kích hoạt mã lỗi chuẩn hệ thống.

---

## 2. Chi Tiết Danh Mục Quy Tắc Nghiệp Vụ

### GROUP 1: Quy Tắc Khởi Tạo Ticket & Chống Trùng Lặp

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-01** | Bắt buộc Thông tin Đầu vào | Khi Sinh viên tạo Ticket, các trường `category_id` (Dropdown), `title` (10 - 150 ký tự), và `description` (20 - 2000 ký tự) là BẮT BUỘC. | Nếu thiếu bất kỳ trường nào, Client chặn submit. Server trả mã lỗi `400 INVALID_INPUT`. |
| **BR-02** | Tính Hợp Lệ Nội Dung Chuỗi | Mọi trường văn bản đầu vào (`title`, `description`, `resolution_note`, `request_note`, `rating_comment`) bắt buộc phải qua hàm `trim()`. Chuỗi chỉ chứa ký tự trắng (space, tab, newline) bị coi là không hợp lệ. | Báo lỗi validation: *"Nội dung không được để trống hoặc chỉ chứa khoảng trắng."* (`400 INVALID_INPUT`). |
| **BR-03** | Chống Trùng Lặp Thao Tác (Idempotency) | Một hành động gửi của Sinh viên chỉ được tạo ra đúng 01 Ticket duy nhất, bất kể sinh viên click đúp, retry do mất mạng hoặc bị nghẽn request. | **Client:** Vô hiệu hóa Form & Nút Gửi ngay khi bấm.<br>**Server:** Sử dụng Header `Client-Request-ID` (UUID v4) + Redis Key lock trong 30 giây. Trả về `409 DUPLICATE_REQUEST` nếu trùng key. |
| **BR-04** | Ràng Buộc Quyền Sở Hữu (Ownership) | Ticket khi khởi tạo phải tự động liên kết cứng với `student_id` lấy từ JWT Token của phiên đăng nhập hiện tại. Tránh triệt để việc giả mạo ID người gửi trên Payload. | Backend bỏ qua mọi trường `student_id` gửi lên từ body payload; bắt buộc đọc từ `request.user.id` thu được sau khi verify Token. |

---

### GROUP 2: Quy Tắc Xử Lý, Chuyển Tiếp & Đóng Ticket

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-05** | Chống Tranh Chấp Tiếp Nhận (Claim Lock) | Hai Nhân viên cùng phòng ban bấm Tiếp nhận (Claim) 1 Ticket `NEW` tại 1 thời điểm: Chỉ người có request đến trước được tiếp nhận. | Server sử dụng Atomic Database Lock (`status IN ('NEW', 'TRANSFERRED')`). Người đến sau nhận lỗi `409 TICKET_ALREADY_CLAIMED`. |
| **BR-06** | Quy Tắc Chuyển Phòng Ban (Transfer) | - Nhân viên chỉ được chuyển phòng ban khi Ticket chưa ở trạng thái `CLOSED` / `REJECTED`.<br>- Bắt buộc nhập lý do chuyển tiếp (`transfer_reason`) từ 10 - 500 ký tự.<br>- Khi chuyển, `assignee_id` tự động đặt về `NULL`.<br>- Bắt buộc ghi 01 record vào Audit Log (`ticket_histories`). | Nếu thiếu lý do, trả mã lỗi `400 MISSING_TRANSFER_REASON`. |
| **BR-07** | Ràng Buộc Bổ Sung Hồ Sơ | Khi Ticket ở `NEED_MORE_INFO`, Sinh viên chỉ được gửi lời nhắn giải trình và upload file đính kèm bổ sung. KHÔNG ĐƯỢC phép chỉnh sửa `title`, `description` hay `category_id` ban đầu. | Trạng thái Ticket tự động chuyển từ `NEED_MORE_INFO` → `IN_PROGRESS` ngay khi Sinh viên submit bổ sung thành công. |
| **BR-08** | Bắt Buộc Kết Quả Khi Đóng Ticket | Nhân viên BẮT BUỘC phải nhập `resolution_note` (Độ dài từ 20 - 2000 ký tự) trước khi bấm Hoàn tất xử lý (`RESOLVED` / `CLOSED`). | Nếu để trống hoặc chỉ nhập khoảng trắng, Server từ chối đổi trạng thái và trả lỗi `400 INVALID_INPUT`. |
| **BR-09** | Quy Tắc Auto-Close Hệ Thống | Ticket ở trạng thái `RESOLVED` quá 3 ngày làm việc (72 giờ làm việc, loại trừ T7, CN, Lễ) mà Sinh viên không phản hồi, Cronjob sẽ tự động chuyển `status = CLOSED`. | Cronjob hệ thống chạy định kỳ 23:00 mỗi ngày. Ghi log `action = SYSTEM_AUTO_CLOSE`. |

---

### GROUP 3: Quy Tắc Cảnh Báo SLA (Service Level Agreement)

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-10** | Khung Thời Gian Cam Kết SLA | Mặc định thời hạn xử lý Ticket (`sla_target_at`) là 24 giờ làm việc kể từ khi tạo. Khung giờ làm việc tính từ 08:00 - 17:00 (từ Thứ 2 đến Thứ 6), không tính cuối tuần và ngày lễ. | Sinh tự động: `sla_target_at = created_at + 24 working hours`. |
| **BR-11** | Trạng Thái Cảnh Báo Quá Hạn SLA | Cảnh báo trạng thái SLA dựa trên thời gian còn lại đến mốc `sla_target_at`:<br>- `ON_TRACK`: Thời gian còn lại > 25% SLA (> 6 giờ làm việc).<br>- `WARNING`: Thời gian còn lại ≤ 25% SLA (≤ 6 giờ làm việc).<br>- `BREACHED`: Đã quá hạn nhưng Ticket chưa `RESOLVED`/`CLOSED`. | Dashboard Quản lý tự động nhóm và hiển thị cảnh báo đỏ với các Ticket ở trạng thái `BREACHED`. |

---

### GROUP 4: Quy Tắc Phân Quyền File, Tài Khoản & Đánh Giá CSAT

| Mã Quy Tắc | Tên Quy Tắc | Mô Tả Nghiệp Vụ & Rules Kỹ Thuật | Handling Specs & Error Code |
| :--- | :--- | :--- | :--- |
| **BR-12** | Phân Quyền Xem File Đính Kèm | File đính kèm lưu ở thư mục Private cách ly hoàn toàn với Web Root. Mọi API xem/tải file (`/api/v1/attachments/{file_id}`) bắt buộc verify Bearer Token và Context Ticket. | Chỉ trả file stream khi người dùng là: Sinh viên sở hữu Ticket, Nhân viên thuộc phòng ban thụ lý, hoặc Admin/Manager. Người khác trả về `403 FORBIDDEN_ACCESS`. |
| **BR-13** | Giới Hạn File Upload | - **Số lượng:** Tối đa 5 file/Ticket (đối với SV) và 3 file/Ticket (đối với kết quả xử lý của Staff).<br>- **Dung lượng:** Tối đa **5MB (5.242.880 Bytes)** / file.<br>- **Định dạng:** MIME Type thực tế (Magic Bytes) phải đúng `.pdf`, `.png`, `.jpg`, `.jpeg`. | Vi phạm dung lượng: Trả mã lỗi `400 FILE_EXCEEDS_LIMIT`. Vi phạm định dạng/magic bytes: Trả mã lỗi `400 FILE_TYPE_NOT_ALLOWED`. |
| **BR-14** | Đánh Giá Chất Lượng Dịch Vụ (CSAT) | Sinh viên chỉ được gửi Đánh giá hài lòng (`rating_score` từ 1 - 5 sao) đúng 01 lần duy nhất cho mỗi Ticket. Khi đã đánh giá, Component Đánh giá chuyển sang Read-only. | Nếu gửi lặp (Race condition): Backend kiểm tra `rating_score IS NOT NULL` và trả lỗi `409 ALREADY_RATED`. |
| **BR-15** | Vô Hiệu Hóa Phiên Khi Khóa Tài Khoản | Khi Admin chuyển trạng thái tài khoản User sang `INACTIVE`, hệ thống phải ngay lập tức vô hiệu hóa (Revoke) toàn bộ Active Sessions và Refresh Tokens của user đó trên Redis/Database. | User bị đẩy văng ra màn hình Login ngay ở thao tác API tiếp theo với mã lỗi `403 ACCOUNT_DISABLED`. |

---

## 3. Ma Trận Xử Lý Lỗi Tập Trung (Business Rules Error Matrix)

```plaintext
[Client Form Input] ────> Validation Layer (BR-01, BR-02, BR-13) ──── Lỗi ───> HTTP 400 INVALID_INPUT
                                  │
                                Hợp lệ
                                  ▼
[API Gateway] ──────────> Security & Token Check (BR-04, BR-12, BR-15) ─ Lỗi ───> HTTP 401 / 403 FORBIDDEN
                                  │
                                Hợp lệ
                                  ▼
[Service Engine] ───────> Business Rules & Concurrency Check (BR-03, BR-05, BR-14) ─ Lỗi ───> HTTP 409 CONFLICT
                                  │
                                Hợp lệ
                                  ▼
[Database Commit] ──────> State Machine & Audit Log (BR-06, BR-08, BR-09)
```

---

## 4. Bảng Mã Lỗi Business Rules Chuẩn (BR Error Code Reference)

| HTTP Status | Error Code | Quy Tắc BR Liên Quan | Mô Tả |
| :--- | :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | BR-01, BR-02, BR-08 | Validation dữ liệu thất bại (thiếu trường, chuỗi quá ngắn/dài, chỉ chứa khoảng trắng). |
| **400** | `FILE_EXCEEDS_LIMIT` | BR-13 | File upload vượt quá 5MB hoặc quá số lượng tối đa cho phép. |
| **400** | `FILE_TYPE_NOT_ALLOWED` | BR-13 | File sai định dạng MIME thực tế (Magic Bytes check thất bại). |
| **400** | `MISSING_TRANSFER_REASON` | BR-06 | Chuyển phòng ban nhưng không nhập lý do hoặc lý do quá ngắn. |
| **400** | `INVALID_TICKET_STATE` | BR-06, BR-07 | Thao tác sai luồng FSM (ví dụ: yêu cầu bổ sung khi Ticket đã CLOSED). |
| **403** | `FORBIDDEN_ACCESS` | BR-04, BR-12 | Vi phạm quyền sở hữu Ticket hoặc quyền xem file đính kèm. |
| **403** | `ACCOUNT_DISABLED` | BR-15 | Tài khoản bị khóa, Token bị đẩy vào Blacklist. |
| **409** | `DUPLICATE_REQUEST` | BR-03 | `Client-Request-ID` bị trùng trong Redis Key lock 30 giây. |
| **409** | `TICKET_ALREADY_CLAIMED` | BR-05 | Ticket đã bị Nhân viên khác Claim trước trong race condition. |
| **409** | `ALREADY_RATED` | BR-14 | Sinh viên cố gắng gửi đánh giá lần thứ 2 cho cùng 1 Ticket. |