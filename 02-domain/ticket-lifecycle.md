# 1. Tổng Quan Vòng Đời Phiếu Hỗ Trợ (Ticket Lifecycle)

Vòng đời của một Ticket trong UniSupport phản ánh chính xác quy trình nghiệp vụ từng bước giữa Sinh viên (Student), Nhân viên (Staff) và Quản lý (Manager/Admin). Trạng thái Ticket được quản lý dưới dạng Máy trạng thái hữu hạn (Finite State Machine - FSM) nhằm đảm bảo dữ liệu không bị chuyển trạng thái sai quy tắc.

Plaintext

       [ Khởi Tạo ] (Student)
            │
            ▼
        (  NEW  ) ───────────────┬───────────────┐
            │                    │               │
      Claim │              Reject│       Transfer│
            ▼                    ▼               ▼
    ( IN_PROGRESS )       ( REJECTED )   ( TRANSFERRED )
       │        ▲                │               │
Request│        │Upload          └───────┬───────┘
       ▼        │                        │ Claim
(NEED_MORE_INFO)                         ▼
       │                          ( IN_PROGRESS )
       │ Resolve                         │
       └─────────────────────────────────┤ Resolve
                                         ▼
                                   ( RESOLVED )
                                         │
                                   Rate  │ (or Auto-close)
                                         ▼
                                   (  CLOSED  )

# 2. Chi Tiết Các Giai Đoạn Trong Vòng Đời

## Giai đoạn 1: Khởi Tạo (Created)
- **Tác nhân:** Sinh viên.
- **Thao tác:** Nhập tiêu đề, mô tả, chọn nhóm vấn đề (`category_id`), đính kèm file (nếu có).
- **Trạng thái hệ thống:** Khởi tạo ở trạng thái `NEW`.
- **Hành vi hệ thống:**
  - Kiểm tra `client_request_id` (Idempotency Key) để tránh trùng lặp.
  - Tự động gán `department_id` mặc định dựa trên `category_id`.
  - Tự động tính toán mốc thời hạn giải quyết `sla_target_at` (= Thời điểm tạo + 24 giờ làm việc).
  - Khởi tạo `sla_status` = `ON_TRACK`.

## Giai đoạn 2: Tiếp Nhận & Phân Loại (Claim, Triage & Transfer)
- **Tác nhân:** Nhân viên phòng ban (`department_id`).
- **Thao tác:**
  - **Trường hợp 1 (Tiếp nhận):** Nhân viên bấm Tiếp nhận xử lý, điều chỉnh priority (`LOW`, `MEDIUM`, `HIGH`, `URGENT`) nếu cần. Trạng thái chuyển sang `IN_PROGRESS`, gán `assignee_id` = `staff_id`.
  - **Trường hợp 2 (Từ chối):** Yêu cầu sai quy định, vi phạm chính sách hoặc spam. Nhân viên nhập lý do từ chối (bắt buộc) và chuyển trạng thái sang `REJECTED`.
  - **Trường hợp 3 (Chuyển phòng ban):** Yêu cầu không thuộc thẩm quyền phòng ban hiện tại. Nhân viên chọn phòng ban mới, nhập lý do chuyển tiếp (bắt buộc, min 10 ký tự). Trạng thái chuyển sang `TRANSFERRED`, gán `assignee_id` = `NULL`.

## Giai đoạn 3: Xử Lý & Bổ Sung Hồ Sơ (Processing & Supplementation)
- **Tác nhân:** Nhân viên phụ trách & Sinh viên.
- **Thao tác:**
  - **Xử lý bình thường:** Nhân viên thực hiện các nghiệp vụ nội bộ để giải quyết yêu cầu. Ticket giữ nguyên `IN_PROGRESS`.
  - **Yêu cầu bổ sung (Staff):** Thiếu hồ sơ/giấy tờ. Nhân viên nhập tin nhắn yêu cầu bổ sung. Trạng thái đổi sang `NEED_MORE_INFO`.
  - **Gửi bổ sung (Student):** Sinh viên tải lên các file/mô tả còn thiếu. Ngay khi bấm Gửi bổ sung, trạng thái tự động chuyển ngược lại về `IN_PROGRESS` và phát thông báo cho Nhân viên.

## Giai đoạn 4: Giải Quyết & Đóng Ticket (Resolution & Closure)
- **Tác nhân:** Nhân viên phụ trách & Hệ thống (Auto-task).
- **Thao tác:**
  - **Nhân viên xử lý xong:** Nhập `resolution_note` (min 20 ký tự), đính kèm file kết quả (nếu có) và bấm Hoàn tất xử lý.
  - Trạng thái Ticket chuyển sang `RESOLVED`, ghi nhận `resolved_at` = `CURRENT_TIMESTAMP`.
  - **Đóng Ticket (Closure):**
    - Sinh viên gửi đánh giá hài lòng -> Ticket tự động chuyển sang `CLOSED`.
    - Sau 03 ngày làm việc kể từ khi ở `RESOLVED`, nếu sinh viên không có khiếu nại hoặc không đánh giá, Job tự động của Server (Cron job) sẽ chuyển trạng thái Ticket sang `CLOSED` và lưu `closed_at`.

## Giai đoạn 5: Đánh Giá Chất Lượng Phục Vụ (Feedback & CSAT)
- **Tác nhân:** Sinh viên.
- **Thao tác:** Mở Ticket ở trạng thái `RESOLVED` hoặc `CLOSED` để chọn số sao (1–5) và nhập nhận xét.
- **Ràng buộc:**
  - Chỉ cho phép đánh giá 01 lần duy nhất.
  - Khi đã đánh giá, giao diện đánh giá chuyển sang dạng Read-only.