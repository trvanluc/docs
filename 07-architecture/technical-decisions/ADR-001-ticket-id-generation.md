# ADR-001: Quy Tắc Sinh Mã Ticket Duy Nhất (Ticket ID Generation Strategy)

- **Trạng thái (Status):** Accepted (Đã chấp thuận)
- **Ngày quyết định:** 2026-09-15 (Giai đoạn Thiết kế Kiến trúc)
- **Đối tượng áp dụng:** Backend Engineering Team, Database Administrator (DBA)

## 1. Bối Cảnh (Context)
Trong hệ thống UniSupport, mỗi yêu cầu hỗ trợ do sinh viên tạo ra cần một mã định danh duy nhất (`ticket_id`) để phục vụ tra cứu, giao tiếp giữa Sinh viên - Nhân viên - Quản lý, và theo dõi lịch sử trên toàn bộ các kênh (Web App, Email, In-app Notification).

Yêu cầu kỹ thuật bắt buộc:
1. **Dễ đọc & Dễ giao tiếp (Human-readable):** Sinh viên và Nhân viên có thể đọc, chép hoặc tìm kiếm thủ công nhanh chóng.
2. **Duy nhất tuyệt đối (Uniqueness):** Không bị trùng lặp dưới mọi điều kiện vận hành.
3. **Chống tranh chấp đồng thời (Concurrency-safe):** Đảm bảo tính nhất quán (Atomic Increment) khi có hàng trăm sinh viên bấm tạo Ticket cùng một thời điểm.
4. **Idempotency Support:** Kết hợp được với cơ chế Idempotency Key để ngăn tạo mã lặp khi đúp click hoặc mạng gián đoạn.

## 2. Các Phương Án Cân Nhắc (Options Considered)
- **Phương án A: UUID v4** (ví dụ: `c9bf9e57-1685-4c89-bafb-ff5af830be8a`)
  - *Ưu điểm:* Duy nhất tuyệt đối, sinh độc lập ở bất kỳ Node/Service nào mà không cần Lock CSDL.
  - *Nhược điểm:* Quá dài ($36\text{ ký tự}$), sinh viên không thể nhớ hoặc đọc qua điện thoại; làm phình to B-Tree Index trên Database khi lưu dưới dạng String.
- **Phương án B: Auto-increment ID CSDL** (ví dụ: `1`, `2`, `10523`)
  - *Ưu điểm:* Ngắn gọn, hiệu năng Index cực cao.
  - *Nhược điểm:* Lộ số lượng giao dịch thực tế của nhà trường; không chứa thông tin ngày tạo; dễ bị thu thập dữ liệu (Enumeration Attack) nếu lộ API endpoint.
- **Phương án C: Formatted Business Key TK-YYYYMMDD-XXXX** (Được chọn)
  - *Ưu điểm:* Dễ nhớ, chuyên nghiệp, phản ánh trực tiếp ngày tạo yêu cầu, tối ưu B-Tree Index khi sắp xếp theo chuỗi thời gian.
  - *Nhược điểm:* Cần cơ chế cấp phát số thứ tự tăng dần (Sequence) theo ngày an toàn và hiệu năng cao.

## 3. Quy Định Kỹ Thuật Chi Tiết (Detailed Specifications)

### 3.1. Cấu Trúc Mã Ticket (`TK-YYYYMMDD-XXXX`)
Mã Ticket bao gồm 3 thành phần nối với nhau bằng dấu gạch ngang (`-`):

| Thành phần | Định dạng | Ví dụ | Quy tắc Validation & Specs |
| :--- | :--- | :--- | :--- |
| **Prefix** | Chuỗi cố định | `TK` | Viết hoa, đại diện cho Ticket UniSupport. |
| **Date String** | `YYYYMMDD` | `20261009` | Lấy theo múi giờ hệ thống `Asia/Ho_Chi_Minh` (UTC+7) tại thời điểm khởi tạo. |
| **Sequence** | `XXXX` | `0001` | Số thứ tự tăng dần trong ngày, định dạng cố định 4 chữ số (Padded with zeros). |

- **Độ dài cố định:** Đúng $15\text{ ký tự}$ (Ví dụ: `TK-20261009-0001`).
- **Ví dụ mã hợp lệ:** `TK-20261009-0001`, `TK-20261009-0150`, `TK-20261009-9999`.

### 3.2. Cơ Chế Sinh Mã Đảm Bảo Concurrency & Atomic Increment
Để đảm bảo tốc độ sinh mã $< 5\text{ms}$ và không bị trùng lặp khi chạy đa tiến trình (Multi-thread/Multi-node):
- **Sử dụng Atomic Counter trên Redis:**
  - Tạo Redis Key theo ngày: `ticket:sequence:YYYYMMDD` (Ví dụ: `ticket:sequence:20261009`).
  - Sử dụng lệnh Atomic `INCR` của Redis để lấy số thứ tự tiếp theo.
  - Set thời gian hết hạn (TTL) cho Key là $48\text{ giờ}$ kể từ khi khởi tạo Key mới trong ngày (để tự động giải phóng bộ nhớ Redis).

- **Thuật toán xử lý phía Backend (Logic Flow):**
  - **Bước 1:** Lấy ngày hiện tại `YYYYMMDD` theo múi giờ UTC+7.
  - **Bước 2:** Gọi Redis `INCR ticket:sequence:YYYYMMDD` $\rightarrow$ Nhận về giá trị số nguyên $N$.
  - **Bước 3:** Nếu $N == 1$ (Key mới trong ngày), gọi Redis `EXPIRE ticket:sequence:YYYYMMDD 172800` ($48\text{ giờ}$).
  - **Bước 4:** Định dạng $N$ thành chuỗi 4 chữ số: `XXXX = String.format("%04d", N)`.
  - **Bước 5:** Ghép thành `ticket_id = "TK-" + YYYYMMDD + "-" + XXXX`.

- **Phương án Dự phòng (Fallback Mechanism):**
  - Nếu Redis ngắt kết nối/sự cố, Backend tự động chuyển sang query Database Sequence hoặc Atomic Database Transaction:
    `SELECT COALESCE(MAX(SUBSTRING(ticket_id, 13, 4)::INT), 0) + 1 FROM tickets WHERE created_at::date = CURRENT_DATE FOR UPDATE;`

## 4. Hệ Quả & Đánh Giá Kỹ Thuật (Consequences)

### Tích cực (Positive)
- **Trải nghiệm người dùng:** Sinh viên và Nhân viên chỉ cần nhớ 4 số cuối trong ngày để trao đổi nhanh (Ví dụ: *"Kiểm tra Ticket 0001 hôm nay"*).
- **Hiệu năng Indexing:** Do mã chứa ngày `YYYYMMDD` ở đầu, các bản ghi mới luôn được chèn vào cuối B-Tree Index của CSDL, hạn chế tối đa việc phân mảnh Index (Index Fragmentation).
- **An toàn Concurrency:** Lệnh `INCR` của Redis xử lý đơn luồng (Single-threaded) đạt hiệu năng đến hàng chục nghìn request/giây mà không lo tranh chấp dữ liệu.

### Ràng buộc & Giới hạn (Constraints & Limits)
- **Giới hạn $9.999\text{ Ticket/ngày}$:**
  - Khung 4 chữ số (`0001` - `9999`) đáp ứng tối đa $9.999\text{ Ticket}$ tạo mới trong một ngày.
  - Đánh giá quy mô: Dự án phục vụ 3.000 sinh viên, tải đỉnh điểm ước tính $< 500\text{ Ticket/ngày}$. Giới hạn $9.999$ hoàn toàn an toàn.
  - **Kế hoạch mở rộng (Scale-up Plan):** Nếu số Ticket vượt quá $9.999$, hệ thống tự động mở rộng chuỗi `XXXX` thành 5 chữ số (`00001` - `99999`) mà không ảnh hưởng tới logic tra cứu cũ.

## 5. Ràng Buộc Validation & Mã Lỗi Hệ Thống (Error Codes)

| Ràng buộc Kỹ thuật | Xử lý vi phạm | Mã lỗi HTTP & Error Code | Message hiển thị cho Sinh viên |
| :--- | :--- | :--- | :--- |
| **Định dạng Mã Ticket** | Kiểm tra Regex: `^TK-\d{8}-\d{4,5}$` | `400 Bad Request`<br><br>`INVALID_TICKET_ID_FORMAT` | "Mã Ticket không đúng định dạng chuẩn (VD: TK-20261009-0001)." |
| **Quá giới hạn trong ngày** | Khi Counter $> 99.999$ | `500 Internal Server Error`<br><br>`SEQUENCE_LIMIT_EXCEEDED` | "Hệ thống vượt quá số lượng tạo yêu cầu trong ngày. Vui lòng liên hệ Admin." |
| **Trùng lặp Key (Edge case)** | Vi phạm `UNIQUE(ticket_id)` ở CSDL | `409 Conflict`<br><br>`DUPLICATE_TICKET_ID` | "Mã Ticket bị trùng lặp. Hệ thống đang tự động thử lại." (Backend tự retry sinh mã mới). |