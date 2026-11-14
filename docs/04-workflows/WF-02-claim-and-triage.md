# WF-02 - Tiếp Nhận, Phân Loại Và Phân Công

## 1. Mục Đích Và Phạm Vi

Mô tả cách Ticket mới trong hàng chờ phòng ban được kiểm tra Nhóm vấn đề, tiếp nhận hoặc phân công cho một nhân viên và bắt đầu quá trình xử lý.

## 2. Sơ Đồ Nghiệp Vụ

```mermaid
flowchart TD
    A[Ticket NEW trong hàng chờ phòng ban] --> B[Nhân viên mở Ticket]
    B --> C[Kiểm tra nội dung, file và Nhóm vấn đề]
    C --> D{Nhóm vấn đề đúng?}

    D -->|Có| H{Tiếp nhận hay phân công?}
    D -->|Không| E[Chọn Nhóm vấn đề mới]
    E --> F{Nhóm vấn đề mới thuộc phòng ban hiện tại?}
    F -->|Không| G[Chuyển sang WF-04 Transfer]
    F -->|Có| S[Cập nhật Nhóm vấn đề và ghi lịch sử]
    S --> H

    H -->|Tiếp nhận| I[Nhân viên nhận Ticket cho mình]
    H -->|Phân công| J[Chọn nhân viên hợp lệ trong phòng ban]

    I --> K{Ticket còn chưa có người phụ trách?}
    J --> L{Nhân viên và quyền hợp lệ?}

    K -->|Không| M[Tải lại dữ liệu mới nhất]
    K -->|Có| N[Gán người phụ trách]
    L -->|Không| O[Từ chối thao tác]
    L -->|Có| N

    N --> P[Chuyển NEW thành IN_PROGRESS]
    P --> Q{Cần điều chỉnh mức ưu tiên?}
    Q -->|Không| R[Ghi lịch sử phân loại/phân công]
    Q -->|Có và có quyền| T[Điều chỉnh mức ưu tiên]
    T --> U[Tính lại thời hạn theo Business Rules]
    U --> R
    R --> V[Ticket xuất hiện trong danh sách xử lý]
```

## 3. Ghi Chú Nghiệp Vụ

- Một Ticket có tối đa một người phụ trách chính tại một thời điểm.
- Nhân viên được phân công phải đang hoạt động và thuộc phòng ban hiện tại.
- Nếu Nhóm vấn đề mới vẫn thuộc phòng ban hiện tại, thay đổi phải được lưu và ghi nhận lịch sử trước khi tiếp tục tiếp nhận/phân công.
- Nếu Nhóm vấn đề mới thuộc phòng ban khác, phải dùng WF-04; không lưu Nhóm vấn đề mới riêng lẻ.
- Mức độ ưu tiên chỉ được điều chỉnh bởi người có quyền; thời hạn phải được tính lại theo `BR-DUE-01` và `BR-DUE-02`, không đặt lại đồng hồ từ đầu.

## 4. Tài Liệu Tham Chiếu

- M02: `FR-STF-01`, `FR-STF-02`, `FR-STF-03`.
- Domain: `BR-OWN-01`, `BR-DUE-01`, `BR-DUE-02`.
