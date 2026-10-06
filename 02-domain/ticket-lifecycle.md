# Vòng Đời Phiếu Hỗ Trợ (Ticket Lifecycle)

Vòng đời của một Ticket trong hệ thống UniSupport đại diện cho toàn bộ quá trình biến chuyển từ khi Sinh viên khởi tạo yêu cầu cho đến khi được giải quyết dứt điểm và ghi nhận phản hồi.

---

## 1. Sơ Đồ Tổng Quan Các Giai Đoạn Vòng Đời
```
┌──────────────┐      Nhân viên Claim/Assign      ┌──────────────┐
│   1. NEW     │ ───────────────────────────────► │2. IN_PROGRESS│ ◄──────────┐
└──────┬───────┘                                  └──────┬───────┘            │
│                                                 │                           │
│ Tự hủy /                                        │ Yêu cầu                   │ SV đã bổ sung
│ Sinh viên hủy                                   │ bổ sung hồ sơ             │ hồ sơ/thông tin
▼                                                 ▼                           │
┌──────────────┐                                  ┌──────────────┐            │
│  CANCELLED   │                                  │3. WAITING_   │ ───────────┘
└──────────────┘                                  │   STUDENT    │
                                                  └──────────────┘
                                                  │
                                                  │                                                  
                                                  │Nhân viên cập nhật      
                                                  │kết quả thành công      
                                                  ▼
┌──────────────┐       Sinh viên Đánh giá /       ┌──────────────┐
│  5. CLOSED   │ ◄─────────────────────────────── │ 4. RESOLVED  │
└──────────────┘       Tự động đóng sau 3 ngày    └──────────────┘

```
---

## 2. Chi Tiết Các Giai Đoạn (Lifecycle Stages)

### Giai đoạn 1: Khởi tạo (NEW)
- **Hành động kích hoạt**: Sinh viên điền form và nhấn **Gửi yêu cầu**.
- **Trạng thái hệ thống**: `NEW`.
- **Đặc điểm**:
  - Hệ thống tự động cấp **Mã Ticket duy nhất**.
  - Ticket chưa có người thụ lý cá nhân (`assigned_staff_id = NULL`).
  - Ticket xuất hiện trong Hòm thư chung (Inbox) của Phòng ban chức năng tương ứng.

### Giai đoạn 2: Phân loại & Đang xử lý (IN_PROGRESS)
- **Hành động kích hoạt**: Nhân viên nhấn **Tiếp nhận (Claim)** hoặc Trưởng phòng **Phân công (Assign)** cho nhân viên cụ thể.
- **Trạng thái hệ thống**: `IN_PROGRESS`.
- **Đặc điểm**:
  - Ticket gắn cố định với 01 nhân viên phụ trách.
  - Nhân viên tiến hành kiểm tra hồ sơ, xử lý nghiệp vụ hoặc chuyển phòng ban nếu gửi sai địa chỉ.

### Giai đoạn 3: Chờ sinh viên bổ sung thông tin (WAITING_STUDENT)
- **Hành động kích hoạt**: Nhân viên kiểm tra hồ sơ thấy thiếu giấy tờ/thông tin và nhấn nút **Yêu cầu bổ sung**.
- **Trạng thái hệ thống**: `WAITING_STUDENT`.
- **Đặc điểm**:
  - Tạm dừng đếm thời gian SLA xử lý của nhân viên.
  - Hệ thống phát thông báo yêu cầu Sinh viên cập nhật.
  - Khi Sinh viên phản hồi/upload thêm file, trạng thái tự động chuyển lại về `IN_PROGRESS`.

### Giai đoạn 4: Đã giải quyết (RESOLVED)
- **Hành động kích hoạt**: Nhân viên hoàn tất xử lý, nhập nội dung kết quả/đính kèm file trả lời và nhấn **Hoàn thành**.
- **Trạng thái hệ thống**: `RESOLVED`.
- **Đặc điểm**:
  - Ghi nhận mốc thời gian hoàn thành `resolved_at`.
  - Sinh viên nhận thông báo kết quả và có quyền xem nội dung giải quyết.

### Giai đoạn 5: Đóng hoàn tất & Đánh giá (CLOSED)
- **Hành động kích hoạt**: Sinh viên xác nhận hài lòng & gửi đánh giá CSAT, HOẶC hệ thống tự động đóng sau **03 ngày làm việc** kể từ khi ở trạng thái `RESOLVED` nếu sinh viên không có khiếu nại thêm.
- **Trạng thái hệ thống**: `CLOSED`.
- **Đặc điểm**:
  - Ticket đóng hoàn toàn, không thể chỉnh sửa hoặc thêm bình luận mới.
  - Lưu trữ dữ liệu phục vụ báo cáo và thống kê KPI.