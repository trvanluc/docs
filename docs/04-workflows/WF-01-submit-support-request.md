# WF-01 - Gửi Yêu Cầu Hỗ Trợ

## 1. Mục Đích Và Phạm Vi

Mô tả luồng từ khi sinh viên tạo yêu cầu đến khi hệ thống tạo Ticket thành công, xác định phòng ban tiếp nhận và trả mã Ticket cho sinh viên.

## 2. Sơ Đồ Nghiệp Vụ

```mermaid
flowchart TD
    A[Sinh viên đăng nhập] --> B[Mở Tạo yêu cầu]
    B --> C[Chọn Nhóm vấn đề]
    C --> D[Nhập nội dung yêu cầu]
    D --> E{Có file minh chứng?}
    E -->|Có| F[Đính kèm file]
    E -->|Không| G[Xác nhận gửi]
    F --> G
    G --> H{Dữ liệu hợp lệ?}
    H -->|Không| I[Hiển thị lỗi và yêu cầu chỉnh sửa]
    I --> C
    H -->|Có| J[Xác định phòng ban từ Nhóm vấn đề]
    J --> K[Tạo Ticket]
    K --> L[Trạng thái NEW]
    L --> M[Mức ưu tiên mặc định MEDIUM]
    M --> N[Tính thời hạn xử lý]
    N --> O[Ghi lịch sử tạo Ticket]
    O --> P[Hiển thị mã Ticket và thông báo thành công]
```

## 3. Ghi Chú Nghiệp Vụ

- Sinh viên chỉ chọn Nhóm vấn đề đang hoạt động; không tự tạo hoặc nhập tự do.
- Nội dung yêu cầu từ 20 đến 2.000 ký tự.
- Tối đa 03 file/lần, 10 MB/file, PDF/PNG/JPG/JPEG.
- Một lần xác nhận gửi chỉ tạo tối đa một Ticket.
- Phòng ban tiếp nhận được xác định từ Nhóm vấn đề.

## 4. Tài Liệu Tham Chiếu

- M01: `FR-STU-02`, `FR-STU-04`.
- Domain: `BR-FILE-01`, `BR-FILE-02`, `BR-DUE-01`.
