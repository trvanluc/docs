# Đặc Tả Thông Báo Nội Bộ (Notification Service dùng chung)

## 1. Tổng Quan

**Notification Service** là năng lực dùng chung cho 3 phân hệ chính M01 Sinh viên, M02 Nhân viên và M03 Quản lý theo proposal đã chốt. Service chịu trách nhiệm tự động phát sinh, quản lý và hiển thị các thông báo nội bộ hệ thống (In-app Notification) tới đúng đối tượng người dùng mỗi khi có sự kiện quan trọng phát sinh trên Ticket hỗ trợ.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Cập nhật tức thì (Real-time Engagement)**: Giúp sinh viên nắm bắt ngay tiến độ giải quyết yêu cầu, nhận thông báo kết quả hoặc yêu cầu bổ sung hồ sơ từ nhà trường mà không cần liên tục f5/tải lại trang.
- **Giảm thiểu độ trễ vận hành**: Cảnh báo nhân viên chuyên trách ngay khi có Ticket mới gửi đến phòng ban, được phân công công việc hoặc khi có phản hồi mới từ sinh viên.
- **Cảnh báo vi phạm SLA**: Tự động nhắc nhở nhân viên và quản lý khi Ticket sắp hoặc đã quá hạn cam kết xử lý, giúp nâng cao chỉ số hoàn thành công việc đúng hạn.
- **Tập trung hóa trải nghiệm**: Quản lý toàn bộ thông báo tại Trung tâm thông báo (Notification Center) với biểu tượng quả chuông trực quan trên giao diện Web Application.

---

## 3. Danh Mục Yêu Cầu Chức Năng (Functional Requirements)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ |
| :--- | :--- | :--- |
| **FR-NTF-01** | Khởi tạo & Phát thông báo tự động | Tự động sinh thông báo In-app khi có các sự kiện trên Ticket (Tạo mới, Đổi trạng thái, Yêu cầu bổ sung, Cập nhật kết quả...). |
| **FR-NTF-02** | Trung tâm thông báo (Notification Center) | Biểu tượng quả chuông (Bell Icon) hiển thị số thông báo chưa đọc, danh sách thông báo và chi tiết nội dung. |
| **FR-NTF-03** | Đánh dấu Đã đọc / Chưa đọc | Cho phép người dùng đánh dấu từng thông báo hoặc "Đánh dấu tất cả là đã đọc". |
| **FR-NTF-04** | Cảnh báo quá hạn SLA (SLA Overdue Alert) | Tự động phát thông báo cảnh báo tới Nhân viên phụ trách và Trưởng phòng khi Ticket sắp hoặc đã vượt thời hạn SLA. |

---

## 4. Sơ Đồ Luồng Tự Động Phát Thông Báo (Notification Flow)

[Sự kiện nghiệp vụ phát sinh]
(Tạo Ticket / Chuyển trạng thái / Yêu cầu bổ sung / Phân công / Quá hạn SLA)
        │
        ▼
    [Khởi tạo Thông báo - FR-NTF-01]

Bắt sự kiện (Event Listener)

Xác định danh sách Người nhận (Recipients) theo Vai trò

Biên dịch Nội dung theo mẫu (Notification Template)
        │
        ▼
    [Lưu vào Database & Đẩy về Client]
        │
        ▼
    [Trung tâm thông báo Client - FR-NTF-02 / FR-NTF-03]

Cập nhật Badge số lượng chưa đọc trên quả chuông

Hiển thị Toast thông báo nổi trên màn hình

Đánh dấu Đã đọc khi người dùng nhấn xem


---

## 5. Bảng Ma Trận Sự Kiện & Người Nhận Thông Báo (Event-Recipient Matrix)

| Mã Sự Kiện | Sự Kiện Kích Hoạt | Sinh Viên (Student) | Nhân Viên (Staff Agent) | Quản Lý (Manager) |
| :---: | :--- | :---: | :---: | :---: |
| **EVT-01** | Sinh viên gửi thành công Ticket mới |  (Xác nhận) |  (Hòm thư PB) | ❌ |
| **EVT-02** | Ticket được Claim / Assign cho Nhân viên | ❌ |  (Người nhận) | ❌ |
| **EVT-03** | Chuyển trạng thái sang `WAITING_STUDENT` |  (Cần bổ sung) | ❌ | ❌ |
| **EVT-04** | Sinh viên cập nhật hồ sơ bổ sung | ❌ |  (Người thụ lý) | ❌ |
| **EVT-05** | Chuyển Phòng ban chuyên trách | ❌ |  (PB mới) | ❌ |
| **EVT-06** | Ticket hoàn thành (`RESOLVED` / `CLOSED`) |  (Nhận kết quả) | ❌ | ❌ |
| **EVT-07** | Ticket sắp quá hạn hoặc đã quá hạn SLA | ❌ |  (Nhắc nhở) |  (Cảnh báo) |

*Ghi chú:  = Có nhận thông báo | ❌ = Không nhận thông báo*
