# Đặc Tả Phân Quyền & Bảo Mật Dùng Chung (RBAC & Security)

## 1. Tổng Quan

**RBAC & Security** là năng lực dùng chung cho 3 phân hệ chính M01 Sinh viên, M02 Nhân viên và M03 Quản lý theo proposal đã chốt. Năng lực này duy trì tính toàn vẹn, an toàn dữ liệu và kiểm soát truy cập cho toàn bộ hệ thống **UniSupport** tại **Aurora University**.

Năng lực này chịu trách nhiệm xác thực danh tính người dùng (Authentication), phân quyền thao tác theo vai trò (Role-Based Access Control - RBAC) đối với các vai trò chính (Sinh viên, Nhân viên, Quản lý), bảo vệ an toàn cho các tệp đính kèm (PDF, Ảnh) và lưu vết nhật ký hoạt động (Audit Log) cho các giao dịch nghiệp vụ quan trọng.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Bảo mật danh tính & Xác thực an toàn**: Đảm bảo 100% người dùng truy cập hệ thống đều được định danh bằng tài khoản cá nhân với mật khẩu được mã hóa chuẩn an toàn.
- **Phân định ranh giới dữ liệu (Data Isolation)**: Người dùng thuộc vai trò nào chỉ được thấy và thao tác đúng phạm vi dữ liệu được cấp phép (Sinh viên chỉ thấy Ticket của mình; Nhân viên chỉ xử lý Ticket thuộc Phòng ban của mình).
- **Bảo vệ tài liệu nhạy cảm**: Chặn đứng nguy cơ rò rỉ file đính kèm (bảng điểm, giấy xác nhận, đơn từ...) bằng cơ chế đường dẫn bảo mật qua Secured API Proxy (không lộ đường dẫn lưu trữ tĩnh).
- **Tính minh bạch & Khả năng tra soát (Auditability)**: Ghi lại đầy đủ lịch sử các thao tác quan trọng để phục vụ công tác kiểm tra, đối soát khi có thắc mắc hoặc khiếu nại.

---

## 3. Danh Mục Yêu Cầu Chức Năng (Functional Requirements)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ |
| :--- | :--- | :--- |
| **FR-SEC-01** | Xác thực & Quản lý phiên làm việc | Đăng nhập mã hóa, cấp Token xác thực (JWT/Session), tự động hết hạn phiên và cơ chế đăng xuất an toàn. |
| **FR-SEC-02** | Phân quyền theo vai trò (RBAC) | Kiểm soát quyền truy cập API và giao diện dựa trên 3 vai trò chính (`STUDENT`, `STAFF`, `MANAGER`). |
| **FR-SEC-03** | Bảo mật tệp đính kèm | Kiểm soát quyền tải/xem file đính kèm (PDF/Ảnh) thông qua Secured API Proxy, ngăn chặn truy cập trực tiếp URL. |
| **FR-SEC-04** | Ghi nhận Nhật ký tra soát (Audit Log) | Tự động ghi vết các sự kiện hệ thống quan trọng (Đổi trạng thái, Phân công, Chuyển phòng ban, Khóa tài khoản) dưới dạng immutable log. |

---

## 4. Sơ Đồ Kiến Trúc Phân Quyền & Bảo Mật (Security Architecture)
```
[Client Web Request]
        │
        ▼
┌─────────────────────────┐
│   API Gateway / Router  │
└────────────┬────────────┘
             │
             ▼
┌────────────────────────────────────┐
│ 1. AUTHENTICATION MIDDLEWARE       │
│    - Kiểm tra JWT Token / Session  │
│    - Xác minh danh tính người dùng │
└──────────────────┬─────────────────┘
                   │ (Hợp lệ)
                   ▼
┌────────────────────────────────────┐
│ 2. RBAC AUTHORIZATION MIDDLEWARE   │
│    - Kiểm tra Role (STUDENT/STAFF/ │
│      MANAGER)                │
│    - Kiểm tra Resource Ownership & │
│      Department Scope              │
└──────────────────┬─────────────────┘
                   │ (Hợp lệ)
          ┌────────┴────────┐
          ▼                 ▼
┌──────────────────────┐  ┌──────────────────────┐
│   Business Logic     │  │ Secured File Proxy   │
│   (Process Ticket)   │  │ (Verify Attachment  │
└──────────┬───────────┘  │  Ownership)         │
           │              └──────────┬───────────┘
           ▼                         ▼
┌──────────────────────┐  ┌──────────────────────┐
│ 3. AUDIT LOG MODULE  │  │ Return Encrypted     │
│    - Append Activity │  │ File Stream          │
└──────────────────────┘  └──────────────────────┘
```
---

## 5. Ma Trận Phân Quyền Dữ Liệu Chi Tiết (Data Access Control Matrix)

| Phạm Vi Dữ Liệu (Resource Scope) | Sinh Viên (`STUDENT`) | Nhân Viên (`STAFF`) | Quản Lý (`MANAGER`) |
| :--- | :---: | :---: | :---: | :---: |
| **Ticket do mình tạo** | Full (Xem, Tạo, Bổ sung, Đánh giá) | N/A | N/A | N/A |
| **Ticket thuộc Phòng ban mình phụ trách** | ❌ Không có quyền | Full (Xem, Claim, Transfer, Resolve) | Xem & Phân công trong Phòng ban | Xem & Quản trị |
| **Ticket thuộc Phòng ban khác** | ❌ Không có quyền | ❌ Không có quyền | ❌ Không có quyền | Xem tra soát |
| **Tệp đính kèm của Ticket** |  (Chỉ file thuộc Ticket của mình) |  (Chỉ file thuộc Ticket của PB mình) |  (Chỉ file thuộc Ticket của PB mình) |  (Tải tra soát) |
| **Báo cáo & Thống kê KPI** | ❌ Không có quyền | ❌ Không có quyền |  (Dữ liệu PB phụ trách) |  (Dữ liệu Toàn trường) |
| **Quản lý Tài khoản & Audit Log** | ❌ Không có quyền | ❌ Không có quyền | ❌ Không có quyền |  (Toàn bộ hệ thống) |

*Ghi chú:  = Có quyền truy cập | ❌ = Cấm truy cập*
