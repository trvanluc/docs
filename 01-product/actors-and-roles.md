# Các Vai Trò & Mô Hình Phân Quyền (Actors & Roles)

## 1. Danh Sách Các Vai Trò Trong Hệ Thống (Actors)

Hệ thống UniSupport xác định **3 vai trò chính (Actors)** tham gia vào quy trình nghiệp vụ:

```
┌──────────────────────────────────────────────┐
│                  UNISUPPORT                  │
└──────────────────────┬───────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌──────────────┐┌──────────────┐┌───────────────┐
│ 1. SINH VIÊN ││ 2. NHÂN VIÊN ││ 3. QUẢN LÝ    │
│   (Student)  ││ (Staff Agent)││(Manager/Admin)│
└──────────────┘└──────────────┘└───────────────┘
```

---

## 2. Chi Tiết Nhiệm Vụ & Phạm Vi Quyền Hạn

### 2.1 Sinh viên (Student)
- **Mô tả**: Là người dùng cuối có nhu cầu gửi các câu hỏi, thắc mắc hoặc yêu cầu giải quyết thủ tục hành chính/kỹ thuật.
- **Quyền hạn chính**:
  - Đăng nhập vào hệ thống bằng tài khoản cá nhân do nhà trường cấp.
  - Tạo mới Ticket hỗ trợ (chọn phân loại, nhập tiêu đề, mô tả, đính kèm file PDF/Ảnh).
  - Tra cứu danh sách và chi tiết các Ticket do chính mình đã tạo.
  - Theo dõi tiến độ xử lý và lịch sử phản hồi theo thời gian thực.
  - Bổ sung thông tin/giấy tờ khi nhân viên yêu cầu.
  - Xem kết quả giải quyết và thực hiện đánh giá mức độ hài lòng (1-5 sao + lời nhắn) sau khi Ticket hoàn tất.
- **Ràng buộc dữ liệu**: Sinh viên **chỉ nhìn thấy và thao tác** trên dữ liệu Ticket do chính tài khoản đó tạo ra.

### 2.2 Nhân viên (Staff / Support Agent)
- **Mô tả**: Là nhân viên/chuyên viên thuộc các phòng ban chức năng (Đào tạo, Công tác sinh viên, Tài chính - Kế toán, Trung tâm CNTT, Thư viện...).
- **Quyền hạn chính**:
  - Đăng nhập hệ thống bằng tài khoản nhân viên.
  - Xem danh sách Ticket thuộc phòng ban của mình hoặc các Ticket được giao cá nhân.
  - **Tiếp nhận (Claim)** Ticket mới hoặc **Phân công (Assign)** Ticket cho nhân viên khác trong cùng phòng ban.
  - **Phân loại (Triage)** nhóm vấn đề và cập nhật mức độ ưu tiên (Thấp, Trung bình, Cao, Khẩn cấp).
  - **Chuyển phòng ban (Transfer)** nếu Ticket gửi nhầm đơn vị xử lý.
  - **Gửi yêu cầu bổ sung thông tin (Request Supplement)** tới sinh viên.
  - Cập nhật tiến độ, ghi nhận kết quả xử lý và **Đóng Ticket (Resolve/Close)**.
- **Ràng buộc dữ liệu**: Nhân viên **chỉ nhìn thấy và xử lý** các Ticket thuộc Phòng ban mà mình được gán quyền, hoặc Ticket do chính mình phụ trách.

### 2.3 Quản lý / Quản trị viên (Manager / Admin)
- **Mô tả**: Ban Giám hiệu, Trưởng/Phó các Phòng ban hoặc Quản trị viên kỹ thuật của Aurora University.
- **Quyền hạn chính**:
  - Xem Dashboard tổng quan chỉ số vận hành toàn trường hoặc theo từng phòng ban.
  - Xem báo cáo chi tiết: Số lượng Ticket, tỷ lệ quá hạn, thời gian xử lý trung bình, chỉ số hài lòng (CSAT).
  - Quản lý tài khoản người dùng: Tạo mới, chỉnh sửa thông tin, khóa/mở khóa tài khoản.
  - Gán vai trò (Role) và phòng ban (Department) cho Nhân viên.
  - Tra soát nhật ký hệ thống cơ bản (Audit Log) khi cần thiết.
- **Ràng buộc dữ liệu**: Có quyền truy cập số liệu tổng hợp và quản trị toàn bộ hệ thống.

---

## 3. Ma Trận Phân Quyền Vận Hành (Permissions Matrix)

| Mức Độ Thao Tác | Chức Năng / Hành Động | Sinh Viên | Nhân Viên | Quản Lý |
| :--- | :--- | :---: | :---: | :---: |
| **Xác thực** | Đăng nhập / Đăng xuất hệ thống | ✅ | ✅ | ✅ |
| **Ticket (Khởi tạo)** | Tạo mới Ticket & Upload đính kèm | ✅ | ❌ | ❌ |
| **Ticket (Xem)** | Xem Ticket do mình tạo | ✅ | ✅ | ✅ |
| | Xem Ticket thuộc phòng ban mình | ❌ | ✅ | ✅ |
| | Xem toàn bộ Ticket toàn hệ thống | ❌ | ❌ | ✅ |
| **Ticket (Xử lý)** | Tiếp nhận (Claim) / Phân công (Assign) | ❌ | ✅ | ✅ |
| | Chuyển phòng ban (Transfer) | ❌ | ✅ | ✅ |
| | Yêu cầu bổ sung hồ sơ | ❌ | ✅ | ✅ |
| | Phản hồi & Bổ sung hồ sơ theo yêu cầu | ✅ | ❌ | ❌ |
| | Cập nhật kết quả & Đóng Ticket | ❌ | ✅ | ✅ |
| **Đánh giá** | Gửi đánh giá hài lòng (Rating/CSAT) | ✅ | ❌ | ❌ |
| **Báo cáo** | Xem Dashboard KPI & Báo cáo thống kê | ❌ | ❌ | ✅ |
| **Quản trị** | Quản lý tài khoản & Phân quyền RBAC | ❌ | ❌ | ✅ |
| | Xem Audit Log cơ bản | ❌ | ❌ | ✅ |

*Ghi chú: ✅ = Có quyền thao tác | ❌ = Không có quyền thao tác*