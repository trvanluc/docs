# Phân Hệ Quản Trị & Quản Lý (M03 - Admin / Management Dashboard)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md` (Sheet M3 – Admin)

## 1. Tổng Quan Phân Hệ

Phân hệ **Quản trị & Quản lý (Admin / Management Dashboard)** là trung tâm điều hành và kiểm soát dữ liệu dành cho Ban Giám hiệu, Trưởng/Phó các Phòng ban chức năng và Quản trị viên hệ thống (Admin) tại **Aurora University**.

Phân hệ bao gồm 6 khối chức năng cốt lõi: Quản lý tài khoản & phân quyền vai trò (RBAC), Quản lý phòng ban & danh mục yêu cầu, Kiểm soát quyền truy cập & nhật ký tra soát (Audit Trail), Quản lý thời hạn lưu trữ dữ liệu, Dashboard thống kê KPI thời gian thực, và Hệ thống Báo cáo chuyên sâu / Đo lường hài lòng (CSAT) / Xuất dữ liệu báo cáo.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Giám sát thời gian thực (Real-time Monitoring)**: Theo dõi các chỉ số KPI vận hành cốt lõi (Tổng số Ticket, Quá hạn SLA, Thời gian xử lý trung bình, Chỉ số hài lòng CSAT).
- **Cơ sở điều phối nhân sự**: Giúp nhà trường nhận diện ngay phòng ban nào đang quá tải hoặc nhóm vấn đề nào phát sinh đột biến để kịp thời điều chỉnh quy trình/nhân sự.
- **Đánh giá chất lượng dịch vụ khách quan**: Tổng hợp phản hồi, điểm đánh giá sao và nhận xét của sinh viên sau khi yêu cầu được hoàn thành; hỗ trợ xuất báo cáo Excel/CSV.
- **An toàn & Quản trị tập trung**: Quản lý vòng đời tài khoản người dùng, gán đúng vai trò/phòng ban, kiểm soát an toàn dữ liệu và đảm bảo tính minh bạch nhờ nhật ký tra soát (Audit Log).

---

## 3. Danh Mục Yêu Cầu Chức Năng & Phân Bổ Effort (Effort Breakdown)

*Tổng Effort Phân hệ M3: **207h cơ sở + 8h buffer = 215h kế hoạch***

| Mã Chức Năng | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Effort Cơ Sở (h) | Buffer (h) | Effort Kế Hoạch (h) | Phân Bổ Role (h) |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **FR-ADM-01** | Quản lý tài khoản, vai trò & RBAC | Tạo mới, khóa/mở khóa tài khoản, xác thực mã hóa, phân quyền 4 vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`). | 60 | 4 | **64h** | BA: 5, UI/UX: 3, TL: 6, FE1: 3, FE2: 8, BE1: 13, BE2: 9, QA: 13 |
| **FR-ADM-02** | Quản lý phòng ban & danh mục | Cấu hình cơ cấu Phòng ban, quản lý danh mục nhóm vấn đề và phân luồng tiếp nhận ban đầu. | 26 | 0 | **26h** | BA: 4, UI/UX: 1, TL: 3, FE2: 4, BE1: 5, BE2: 5, QA: 4 |
| **FR-ADM-03** | Kiểm soát quyền truy cập & Audit Trail | Kiểm soát quyền truy cập tài nguyên/file đính kèm qua Secured API Proxy, lưu vết nhật ký bất biến. | 36 | 4 | **40h** | BA: 4, UI/UX: 0, TL: 4, FE1: 1, FE2: 4, BE1: 9, BE2: 5, QA: 9 |
| **FR-ADM-04** | Quản lý thời hạn lưu trữ | Thiết lập chính sách lưu trữ (Retention Policy), thu dọn file tạm và lưu trữ định kỳ dữ liệu Ticket cũ. | 15 | 0 | **15h** | BA: 3, UI/UX: 0, TL: 1, BE1: 4, BE2: 4, QA: 3 |
| **FR-ADM-05** | Dashboard & thống kê quản trị | Xem các thẻ chỉ số (KPI Cards) và biểu đồ trực quan về khối lượng công việc, tình trạng quá hạn theo phòng ban. | 33 | 0 | **33h** | BA: 4, UI/UX: 3, TL: 1, FE2: 9, BE1: 3, BE2: 9, QA: 4 |
| **FR-ADM-06** | Báo cáo, mức độ hài lòng & xuất dữ liệu | Báo cáo thời gian xử lý SLA trung bình, xu hướng nhóm sự cố, tổng hợp điểm CSAT và xuất file báo cáo (Excel/CSV). | 37 | 0 | **37h** | BA: 4, UI/UX: 3, TL: 1, FE2: 8, BE1: 5, BE2: 10, QA: 6 |
| **TỔNG M3** | **TỔNG PHÂN HỆ QUẢN TRỊ & BÁO CÁO** | | **207h** | **8h** | **215h** | **BA: 24, UI/UX: 10, TL: 16, FE1: 4, FE2: 33, BE1: 39, BE2: 42, QA: 39** |

---

## 4. Sơ Đồ Luồng Tương Tác Của Quản Lý & Quản Trị Viên (Management Workflow)
```
[Đăng nhập Xác thực FR-ADM-01]
│
├───────────────────────────────┬───────────────────────────────┬───────────────────────────────┐
▼                               ▼                               ▼                               ▼
[Dashboard KPI FR-ADM-05]     [Báo cáo & CSAT FR-ADM-06]      [Quản trị Cơ sở & Quyền hạn]    [Quản trị Hệ thống & Dữ liệu]
(Tổng Ticket, Quá hạn SLA,      (Thời gian xử lý trung bình,    ├──► [Tài khoản & RBAC FR-ADM-01]├──► [Kiểm soát quyền & Audit FR-ADM-03]
Phân bổ tải phòng ban)          Top xu hướng, Xuất Excel/CSV)   └──► [Phòng ban & DM FR-ADM-02]  └──► [Thời hạn lưu trữ FR-ADM-04]
```

---

## 5. Quy Tắc Vận Hành & Thiết Kế Giao Diện (UI/UX Guidelines)

1. **Giao diện Trực quan (Data Visualization)**: Sử dụng các biểu đồ tròn (Pie chart) biểu diễn tỷ lệ trạng thái Ticket, biểu đồ cột (Bar chart) so sánh khối lượng công việc giữa các phòng ban, và biểu đồ đường (Line chart) thể hiện xu hướng theo thời gian.
2. **Bộ lọc Báo cáo linh hoạt (Filter Options)**: Cho phép lọc dữ liệu theo:
   - Khoảng thời gian (Hôm nay, Tuần này, Tháng này, Tùy chọn ngày).
   - Phòng ban chuyên trách.
   - Nhóm vấn đề (Category).
3. **Phân vùng dữ liệu xem (Data Scope)**:
   - **Trưởng phòng ban**: Chỉ xem được Báo cáo & KPI thuộc Phòng ban của mình phụ trách.
   - **Ban Giám hiệu / Admin**: Xem được Báo cáo & KPI toàn trường của tất cả phòng ban.