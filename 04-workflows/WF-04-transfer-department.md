# WF-04 - Chuyển Xử Lý Sang Phòng Ban Khác

## 1. Mục Đích Và Phạm Vi

Mô tả cách Ticket được chuyển sang phòng ban khác khi nội dung thực tế thuộc phạm vi xử lý khác. Đổi người phụ trách trong cùng phòng ban không dùng Workflow này.

## 2. Sơ Đồ Nghiệp Vụ

```mermaid
flowchart TD
    A[Ticket NEW / IN_PROGRESS / WAITING_STUDENT] --> B[Người có quyền chọn Chuyển xử lý]
    B --> C[Chọn Nhóm vấn đề đích]
    C --> D[Nhập lý do chuyển]
    D --> E[Hệ thống xác định phòng ban đích từ Nhóm vấn đề]
    E --> F{Nhóm vấn đề và phòng ban hợp lệ?}
    F -->|Không| G[Từ chối thao tác]
    F -->|Có| H[Cập nhật Nhóm vấn đề và phòng ban cùng lúc]
    H --> I[Gỡ người phụ trách hiện tại]
    I --> J[Giữ nguyên trạng thái nghiệp vụ hiện tại]
    J --> K[Ghi lịch sử trước/sau và lý do]
    K --> L[Ticket vào hàng chờ phòng ban mới]
    L --> M[Thông báo sinh viên và phạm vi phòng ban mới]
    M --> N[Phòng ban mới tiếp nhận hoặc phân công theo trạng thái hiện tại]
```

## 3. Ghi Chú Nghiệp Vụ

- Transfer chỉ dùng khi chuyển sang **phòng ban khác**.
- Category đích phải đang hoạt động và ánh xạ tới phòng ban khác phòng ban hiện tại.
- Lý do chuyển từ 10 đến 1.000 ký tự.
- Transfer không tạo trạng thái mới và không tự đưa Ticket về `NEW`.
- Nội dung, file và toàn bộ lịch sử được giữ nguyên.

## 4. Tài Liệu Tham Chiếu

- M02: `FR-STF-05`.
- Domain: `BR-OWN-02`.
