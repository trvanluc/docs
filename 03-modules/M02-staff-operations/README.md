# Phân Hệ Nhân Viên (M02 - Staff Operations)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md` (Sheet M2 – Staff)

## 1. Tổng Quan Phân Hệ

Phân hệ **Nhân viên (Staff Operations)** là không gian tác nghiệp chính dành cho cán bộ, chuyên viên thuộc các Phòng ban chức năng tại **Aurora University** (Phòng Đào tạo, Phòng CTHSSV, Phòng Tài chính - Kế toán, Trung tâm CNTT, Thư viện...). 

Phân hệ cung cấp các công cụ vận hành giúp nhân viên tiếp nhận, phân loại, phân công, điều phối liên phòng ban, xử lý trao đổi với sinh viên và ghi nhận kết quả xử lý Ticket một cách chuyên nghiệp, tránh bỏ sót hoặc xử lý trùng lặp.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Hòm thư công việc tập trung (Centralized Inbox)**: Gom toàn bộ yêu cầu của sinh viên về một nơi, chia theo Phòng ban và Cá nhân phụ trách.
- **Phân công & Phối hợp rõ ràng**: Loại bỏ tình trạng đùn đẩy công việc nhờ cơ chế Tiếp nhận (Claim), Phân công (Assign) và Chuyển phòng ban (Transfer/Escalation) minh bạch.
- **Kiểm soát tiến độ & SLA**: Theo dõi mức độ ưu tiên và thời hạn cam kết xử lý (SLA), cảnh báo khi sắp hoặc đã quá hạn.
- **Lưu vết toàn bộ quá trình**: Mọi ghi chú nội bộ, yêu cầu bổ sung thông tin hay cập nhật kết quả đều được ghi nhận vào nhật ký tra soát (Audit Trail).

---

## 3. Danh Mục Yêu Cầu Chức Năng & Phân Bổ Effort (Effort Breakdown)

*Tổng Effort Phân hệ M2: **187h cơ sở + 10h buffer = 197h kế hoạch***

| Mã Chức Năng | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Effort Cơ Sở (h) | Buffer (h) | Effort Kế Hoạch (h) | Phân Bổ Role (h) |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **FR-STF-01** | Tiếp nhận, tìm kiếm & lọc yêu cầu | Hòm thư công việc, bộ lọc đa chiều theo phòng ban/trạng thái/ưu tiên, tìm kiếm Ticket. | 33 | 0 | **33h** | BA: 3, UI/UX: 3, TL: 1, FE1: 4, FE2: 5, BE1: 8, BE2: 3, QA: 6 |
| **FR-STF-02** | Phân loại & phân công xử lý | Nhân viên tự nhận (`Claim`) hoặc Trưởng phòng phân công (`Assign`) chuyên viên phụ trách. | 37 | 1 | **38h** | BA: 4, UI/UX: 0, TL: 3, FE1: 4, FE2: 3, BE1: 9, BE2: 5, QA: 9 |
| **FR-STF-03** | Quản lý ưu tiên & thời hạn | Thiết lập độ ưu tiên (`Low`, `Medium`, `High`, `Urgent`), tính toán và theo dõi cam kết SLA. | 26 | 3 | **29h** | BA: 4, UI/UX: 0, TL: 4, FE1: 3, FE2: 3, BE1: 6, BE2: 3, QA: 3 |
| **FR-STF-04** | Xử lý & cập nhật yêu cầu | Ghi chú nội bộ, yêu cầu sinh viên bổ sung hồ sơ (tạm dừng SLA), cập nhật tiến trình. | 36 | 3 | **39h** | BA: 4, UI/UX: 1, TL: 1, FE1: 4, FE2: 4, BE1: 9, BE2: 4, QA: 9 |
| **FR-STF-05** | Chuyển xử lý, Escalation & hoàn tất | Chuyển tiếp phòng ban (Transfer), báo cáo vượt cấp (Escalation) và hoàn tất giải quyết (Resolve). | 29 | 3 | **32h** | BA: 3, UI/UX: 0, TL: 3, FE1: 3, FE2: 3, BE1: 8, BE2: 4, QA: 5 |
| **FR-STF-06** | Đóng & mở lại yêu cầu | Đóng Ticket tự động (sau 3 ngày) hoặc thủ công; xử lý mở lại Ticket (Reopen) khi có khiếu nại. | 26 | 0 | **26h** | BA: 3, UI/UX: 0, TL: 1, FE1: 3, FE2: 3, BE1: 8, BE2: 3, QA: 5 |
| **TỔNG M2** | **TỔNG PHÂN HỆ NHÂN VIÊN** | | **187h** | **10h** | **197h** | **BA: 21, UI/UX: 4, TL: 13, FE1: 21, FE2: 21, BE1: 48, BE2: 22, QA: 37** |

---

## 4. Sơ Đồ Luồng Tương Tác Của Nhân Viên (Staff Workflow)
```
[Tiếp nhận / Lọc Ticket FR-STF-01] ──► [Phân loại & Phân công FR-STF-02] ──► [Quản lý Ưu tiên & SLA FR-STF-03]
                                                                                              │
                                                                                              ▼
┌──────────────────────────────────────────────────────────────────────────────[Xử lý & Cập nhật FR-STF-04]
│                                                                                              │
├──► [Chuyển phòng ban / Escalation FR-STF-05] ──► (Phòng ban mới tiếp nhận)                  │
│                                                                                              │
├──► [Yêu cầu sinh viên bổ sung giấy tờ] ──► (Tạm dừng SLA) ──► (Sinh viên gửi bổ sung) ──────┤
│                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────▼
                                                                               [Cập nhật kết quả giải quyết FR-STF-05]
                                                                                              │
                                                                                              ▼
                                                                               [Đóng & Mở lại Ticket FR-STF-06]
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