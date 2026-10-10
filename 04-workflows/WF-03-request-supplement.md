# WF-03 - Yêu Cầu Và Tiếp Nhận Bổ Sung

## 1. Mục Đích Và Phạm Vi

Mô tả luồng nhân viên yêu cầu sinh viên bổ sung thông tin/tài liệu và cách Ticket quay lại quá trình xử lý sau khi sinh viên phản hồi hợp lệ.

## 2. Sơ Đồ Nghiệp Vụ

```mermaid
flowchart TD
    A[Ticket IN_PROGRESS] --> B[Nhân viên chọn Yêu cầu bổ sung]
    B --> C[Nhập nội dung cần bổ sung]
    C --> D{Nội dung hợp lệ?}
    D -->|Không| E[Hiển thị lỗi]
    E --> C
    D -->|Có| F[Ghi yêu cầu vào lịch sử]
    F --> G[Chuyển sang WAITING_STUDENT]
    G --> H[Tạm dừng đồng hồ thời hạn]
    H --> I[Thông báo cho sinh viên]

    I --> J[Sinh viên mở Ticket]
    J --> K[Nhập nội dung và/hoặc đính kèm file]
    K --> L{Có ít nhất nội dung hoặc file hợp lệ?}
    L -->|Không| M[Hiển thị lỗi]
    M --> K
    L -->|Có| N[Lưu bổ sung và ghi lịch sử]
    N --> O[Chuyển về IN_PROGRESS]
    O --> P[Tiếp tục đồng hồ từ thời gian còn lại]
    P --> Q[Ticket trở lại danh sách xử lý phù hợp]
    Q --> R[Nhân viên tiếp tục xử lý]
```

## 3. Ghi Chú Nghiệp Vụ

- Yêu cầu bổ sung chỉ thực hiện khi Ticket ở `IN_PROGRESS`.
- Thời gian ở `WAITING_STUDENT` không tính vào thời gian xử lý.
- Sinh viên phải cung cấp ít nhất nội dung hoặc file.
- File bổ sung tuân thủ quy tắc file dùng chung.

## 4. Tài Liệu Tham Chiếu

- M01: `FR-STU-04`, `FR-STU-05`.
- M02: `FR-STF-04`.
- Domain: `BR-SUP-01`, `BR-FILE-02`, `BR-DUE-02`.
