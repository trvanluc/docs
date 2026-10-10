# WF-06 - Phản Hồi Kết Quả, Mở Lại, Đóng Và Đánh Giá

## 1. Mục Đích Và Phạm Vi

Mô tả toàn bộ hành vi sau khi Ticket ở `RESOLVED`: sinh viên chấp nhận kết quả hoặc yêu cầu mở lại; hệ thống tự đóng khi hết thời hạn; sau khi `CLOSED`, sinh viên có thể đánh giá mức độ hài lòng.

## 2. Sơ Đồ Nghiệp Vụ

```mermaid
flowchart TD
    A[Ticket RESOLVED] --> B[Sinh viên xem kết quả]
    B --> C{Sinh viên phản hồi trong 03 ngày làm việc?}

    C -->|Chấp nhận kết quả| D[Chuyển sang CLOSED]
    C -->|Yêu cầu mở lại| E[Nhập lý do mở lại]
    C -->|Không phản hồi đến hết hạn| F[Hệ thống tự động chuyển CLOSED]

    E --> G{Lý do và thời hạn hợp lệ?}
    G -->|Không| H[Từ chối mở lại]
    G -->|Có| I[Chuyển RESOLVED thành IN_PROGRESS]
    I --> J{Người phụ trách cũ còn hợp lệ?}
    J -->|Có| K[Giữ người phụ trách cũ và gửi thông báo]
    J -->|Không| L[Đưa về hàng chờ chưa có người phụ trách]
    K --> M[Nhân viên tiếp tục xử lý]
    L --> M
    M --> N[Thực hiện lại WF-05]

    D --> O[Ticket CLOSED]
    F --> O
    O --> P{Còn trong 07 ngày đánh giá?}
    P -->|Không| Q[Kết thúc]
    P -->|Có| R{Ticket đã được đánh giá?}
    R -->|Có| Q
    R -->|Chưa| S[Sinh viên chọn 1-5 sao và nhận xét nếu muốn]
    S --> T[Lưu đánh giá]
    T --> Q
```

## 3. Ghi Chú Nghiệp Vụ

- Reopen chỉ thực hiện từ `RESOLVED → IN_PROGRESS`.
- Staff không có thao tác đóng hoặc mở lại độc lập.
- `CLOSED` là trạng thái kết thúc vòng đời.
- Mỗi Ticket chỉ có tối đa một đánh giá.
- CSAT chỉ nhận trong 07 ngày theo lịch kể từ lúc Ticket `CLOSED`.
- Lịch sử/kết quả của các vòng xử lý trước phải được giữ nguyên.

## 4. Tài Liệu Tham Chiếu

- M01: `FR-STU-06`, `FR-STU-07`.
- M02: `FR-STF-01`, `FR-STF-06`.
- Domain: `BR-LIFE-02`, `BR-LIFE-03`, `BR-CSAT-01`.
