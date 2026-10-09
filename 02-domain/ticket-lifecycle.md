# Vòng Đời Phiếu Hỗ Trợ (Ticket Lifecycle)

Vòng đời của một Ticket trong hệ thống UniSupport đại diện cho toàn bộ quá trình biến chuyển từ khi Sinh viên khởi tạo yêu cầu cho đến khi được giải quyết dứt điểm và ghi nhận phản hồi.

---

## 1. Sơ Đồ Tổng Quan Các Giai Đoạn Vòng Đời

```
                            ┌──────────────┐
                            │   1. NEW     │ ──── REJECTED (Terminal)
                            └──────┬───────┘
                                   │
                    Claim / Assign  │       Transfer
                                   ▼
           ┌────────────────────────────────────────────────┐
           │              2. IN_PROGRESS                    │
           │  (assignee_id != NULL, đang xử lý nghiệp vụ) │
           └──────┬──────────────────────────────────────┬──┘
                  │                                      │
          Yêu cầu│                               Chuyển │ phòng
          bổ sung│                               ban     ▼
                  ▼                         ┌────────────────────┐
         ┌────────────────┐                 │   3. TRANSFERRED   │ ──── REJECTED (Terminal)
         │ 4. NEED_MORE_  │                 │  (Queue PB mới,    │
         │    INFO        │                 │   assignee = NULL) │
         └────────┬───────┘                 └─────────┬──────────┘
                  │                                   │
         SV bổ   │                             Claim  │ (PB mới)
         sung    │                                   │
                  ▼                                   ▼
                  └────────────────────────────────────┘
                                   │
                              Resolve
                                   ▼
                         ┌──────────────┐
                         │ 5. RESOLVED  │
                         └──────┬───────┘
                                │
                  SV Đánh giá / Cronjob 3 ngày
                                │
                                ▼
                         ┌──────────────┐
                         │  6. CLOSED   │  (Terminal State)
                         └──────────────┘
```

---

## 2. Chi Tiết Các Giai Đoạn (Lifecycle Stages)

### Giai đoạn 1: Khởi tạo (NEW)
- **Hành động kích hoạt**: Sinh viên điền form và nhấn **Gửi yêu cầu**.
- **Trạng thái hệ thống**: `NEW`.
- **Đặc điểm**:
  - Hệ thống tự động cấp **Mã Ticket duy nhất** dạng `TK-YYYYMMDD-XXXX`.
  - Ticket chưa có người thụ lý cá nhân (`assignee_id = NULL`).
  - Ticket xuất hiện trong Queue chung của Phòng ban chức năng tương ứng với `category_id` đã chọn.
  - `sla_target_at` được tính tự động = `created_at + 24 giờ làm việc`.

### Giai đoạn 2: Đang xử lý (IN_PROGRESS)
- **Hành động kích hoạt**: Nhân viên nhấn **Tiếp nhận (Claim)** hoặc Trưởng phòng **Phân công (Assign)** cho nhân viên cụ thể.
- **Trạng thái hệ thống**: `IN_PROGRESS`.
- **Đặc điểm**:
  - Ticket gắn cố định với 01 nhân viên phụ trách (`assignee_id = staff_id`).
  - Nhân viên tiến hành kiểm tra hồ sơ, xử lý nghiệp vụ, có thể yêu cầu bổ sung hoặc chuyển phòng ban.
  - Cơ chế Atomic Locking ngăn chặn 2 nhân viên Claim cùng 1 Ticket.

### Giai đoạn 3: Đã chuyển giao (TRANSFERRED)
- **Hành động kích hoạt**: Nhân viên phát hiện Ticket không đúng thẩm quyền, bấm **Chuyển phòng ban** kèm lý do.
- **Trạng thái hệ thống**: `TRANSFERRED`.
- **Đặc điểm**:
  - `department_id` cập nhật sang Phòng ban mới.
  - `assignee_id` đặt về `NULL` — Ticket nằm trong Queue chờ của Phòng ban mới.
  - Lịch sử chuyển tiếp được ghi vào Audit Log.
  - Nhân viên Phòng ban mới tiếp nhận tương tự `NEW`.

### Giai đoạn 4: Cần bổ sung thông tin (NEED_MORE_INFO)
- **Hành động kích hoạt**: Nhân viên kiểm tra hồ sơ thấy thiếu giấy tờ/thông tin và nhấn nút **Yêu cầu bổ sung**.
- **Trạng thái hệ thống**: `NEED_MORE_INFO`.
- **Đặc điểm**:
  - Hệ thống phát thông báo yêu cầu Sinh viên cập nhật.
  - Sinh viên chỉ được upload file và nhắn tin bổ sung — **KHÔNG** được chỉnh sửa `title`, `description`, `category_id` ban đầu.
  - Khi Sinh viên gửi bổ sung thành công → Trạng thái **tự động** chuyển lại về `IN_PROGRESS` (không cần nhân viên xác nhận thủ công).

### Giai đoạn 5: Đã giải quyết (RESOLVED)
- **Hành động kích hoạt**: Nhân viên hoàn tất xử lý, nhập nội dung kết quả (`resolution_note` ≥ 20 ký tự) và nhấn **Hoàn thành**.
- **Trạng thái hệ thống**: `RESOLVED`.
- **Đặc điểm**:
  - Ghi nhận mốc thời gian hoàn thành `resolved_at`.
  - Sinh viên nhận thông báo kết quả và có quyền xem nội dung giải quyết.
  - Kích hoạt bộ đếm Auto-Close: Nếu 3 ngày làm việc không có đánh giá → Cronjob tự đóng Ticket.

### Giai đoạn 6: Đóng hoàn tất (CLOSED)
- **Hành động kích hoạt**: Sinh viên xác nhận hài lòng & gửi đánh giá CSAT, HOẶC hệ thống tự động đóng sau **03 ngày làm việc** kể từ khi ở trạng thái `RESOLVED`.
- **Trạng thái hệ thống**: `CLOSED`.
- **Đặc điểm**:
  - **Terminal State**: Ticket đóng hoàn toàn, không thể chỉnh sửa hoặc thay đổi trạng thái.
  - Lưu trữ dữ liệu đầy đủ phục vụ báo cáo và thống kê KPI.

### Trạng thái Terminal Khác: Từ chối (REJECTED)
- **Hành động kích hoạt**: Nhân viên phát hiện Ticket vi phạm, spam hoặc không đúng quy định, bấm **Từ chối** kèm lý do.
- **Trạng thái hệ thống**: `REJECTED`.
- **Đặc điểm**:
  - **Terminal State**: Không thể chuyển sang trạng thái khác.
  - Sinh viên nhận thông báo kèm lý do từ chối.
  - `closed_at` được ghi nhận tại thời điểm từ chối.

---

## 3. Quy Tắc Đặc Biệt

| Quy tắc | Mô tả |
| :--- | :--- |
| **Chống mở lại Ticket CLOSED** | Không hỗ trợ Reopen. Nếu có vấn đề mới, sinh viên tạo Ticket mới. |
| **Không tự đăng ký tài khoản** | Sinh viên và Nhân viên không tự tạo tài khoản — chỉ ADMIN mới có quyền cấp. |
| **Idempotency khi tạo Ticket** | Một form gửi = tối đa 01 Ticket dù người dùng nhấn nhiều lần (Redis Key lock 30s). |
| **Auto-Close Cronjob** | Chạy lúc 23:00 mỗi ngày, tự đóng Ticket `RESOLVED` quá 3 ngày làm việc. |