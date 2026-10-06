# Phân Hệ Nhân Viên (M02 - Staff Operations)

## 1. Tổng Quan Phân Hệ

Phân hệ **Nhân viên (Staff Operations)** là không gian làm việc chính dành cho cán bộ, chuyên viên thuộc các Phòng ban chức năng tại **Aurora University** (Phòng Đào tạo, Phòng CTHSSV, Phòng Tài chính - Kế toán, Trung tâm CNTT, Thư viện...). 

Phân hệ này cung cấp các công cụ vận hành giúp nhân viên tiếp nhận, phân loại, phân công, điều phối liên phòng ban, trao đổi với sinh viên và ghi nhận kết quả xử lý các phiếu hỗ trợ (Ticket) một cách chuyên nghiệp, tránh bỏ sót hoặc xử lý trùng lặp.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Hòm thư công việc tập trung (Centralized Inbox)**: Gom toàn bộ yêu cầu của sinh viên về một nơi, chia theo Phòng ban và Cá nhân phụ trách.
- **Phân công & Phối hợp rõ ràng**: Loại bỏ tình trạng đùn đẩy công việc nhờ cơ chế Tiếp nhận (Claim), Phân công (Assign) và Chuyển phòng ban (Transfer) minh bạch.
- **Kiểm soát tiến độ & SLA**: Theo dõi mức độ ưu tiên và thời hạn cam kết xử lý (SLA), hạn chế tối đa các yêu cầu bị trễ hạn.
- **Lưu vết toàn bộ quá trình**: Mọi ghi chú nội bộ, yêu cầu bổ sung thông tin hay cập nhật kết quả đều được ghi nhận vào nhật ký tra soát (Audit Trail).

---

## 3. Danh Mục Yêu Cầu Chức Năng (Functional Requirements)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ |
| :--- | :--- | :--- |
| **FR-STF-01** | Đăng nhập tài khoản Nhân viên | Đăng nhập bằng tài khoản nhân viên được gán quyền thuộc một hoặc nhiều Phòng ban. |
| **FR-STF-02** | Tiếp nhận (Claim) & Phân công (Assign) | Nhân viên tự nhận Ticket chưa có chủ (`Claim`) hoặc Trưởng phòng phân công (`Assign`) cho chuyên viên. |
| **FR-STF-03** | Phân loại (Triage) & Mức độ ưu tiên | Kiểm tra nội dung, chuẩn hóa nhóm vấn đề và gán mức độ ưu tiên (`Low`, `Medium`, `High`, `Urgent`). |
| **FR-STF-04** | Chuyển phòng ban chuyên trách | Điều chuyển Ticket sang Phòng ban khác khi sinh viên gửi nhầm địa chỉ, kèm lý do bắt buộc. |
| **FR-STF-05** | Yêu cầu sinh viên bổ sung thông tin | Yêu cầu sinh viên cung cấp thêm thông tin/giấy tờ, tạm dừng đếm thời gian SLA xử lý. |
| **FR-STF-06** | Cập nhật tiến độ & Đóng Ticket | Cập nhật ghi chú giải quyết, đính kèm file kết quả, chuyển trạng thái `RESOLVED` / `CLOSED`. |

---

## 4. Sơ Đồ Luồng Tương Tác Của Nhân Viên (Staff Workflow)
```
[Đăng nhập FR-STF-01] ──► [Hòm thư Phòng ban / Inbox]
                                 │
                                 ▼
                [Tiếp nhận / Phân công FR-STF-02]
                                 │
                                 ▼
                    [Phân loại & SLA FR-STF-03]
                                 │
┌────────────────────────────────┼────────────────────────────────┐
▼                                ▼                                ▼
[Chuyển phòng ban FR-STF-04] [Yêu cầu bổ sung FR-STF-05] [Xử lý nghiệp vụ]
│                                │                                │
▼                                ▼                                │
(Chờ PB mới Claim)      (Tạm dừng đếm SLA)                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┤
                                                                  ▼
                                                    [Cập nhật kết quả FR-STF-06]
                                                                  │
                                                                  ▼
                                                    [Chuyển trạng thái RESOLVED]
```

---

## 5. Quy Tắc Vận Hành & Giao Diện (Operational & UI Guidelines)

1. **Bộ lọc danh sách công việc (Inbox Filters)**:
   - **Ticket Mới (Department New)**: Các Ticket gửi đến phòng ban chưa có người tiếp nhận.
   - **Việc của tôi (My Assigned)**: Các Ticket do cá nhân nhân viên đang thụ lý.
   - **Chờ sinh viên bổ sung (Pending Student)**: Các Ticket đang chờ phản hồi từ sinh viên.
   - **Cảnh báo Quá hạn (Overdue / High Priority)**: Các Ticket sắp hoặc đã vượt thời gian SLA.
2. **Phân biệt Ghi chú Nội bộ vs Phản hồi Công khai**:
   - **Internal Note (Vàng)**: Trao đổi nội bộ giữa các nhân viên/quản lý, sinh viên **KHÔNG** nhìn thấy.
   - **Public Response (Trắng/Xanh)**: Phản hồi chính thức gửi tới sinh viên.
3. **An toàn bảo mật**: Nhân viên chỉ được xem file đính kèm của các Ticket thuộc Phòng ban mình phụ trách.