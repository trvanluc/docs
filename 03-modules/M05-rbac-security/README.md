# Phân Hệ Phân Quyền & Bảo Mật (M05 - RBAC & Security)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md`  
> Phân hệ kỹ thuật này hiện thực hóa các chức năng bảo mật cốt lõi thuộc M3 – Admin:
> - **FR-ADM-01: Quản lý tài khoản, vai trò & RBAC (64h kế hoạch)**
> - **FR-ADM-03: Kiểm soát quyền truy cập & Audit Trail (40h kế hoạch)**
> - **FR-ADM-04: Quản lý thời hạn lưu trữ (15h kế hoạch)**

## 1. Tổng Quan Phân Hệ Kỹ Thuật

Phân hệ **Phân Quyền & Bảo Mật (RBAC & Security)** là nền tảng hạ tầng bảo mật cốt lõi duy trì tính toàn vẹn, an toàn dữ liệu và kiểm soát truy cập cho toàn bộ hệ thống **UniSupport** tại **Aurora University**.

Phân hệ chịu trách nhiệm xác thực danh tính người dùng (Authentication), phân quyền thao tác theo vai trò (Role-Based Access Control - RBAC) đối với 4 vai trò chính (Sinh viên, Nhân viên, Quản lý, Quản trị viên), bảo vệ an toàn cho các tệp đính kèm (PDF, Ảnh) và lưu vết nhật ký hoạt động (Audit Log) cho các giao dịch nghiệp vụ quan trọng.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Bảo mật danh tính & Xác thực an toàn**: Đảm bảo 100% người dùng truy cập hệ thống đều được định danh bằng tài khoản cá nhân với mật khẩu được mã hóa chuẩn an toàn (Argon2/BCrypt).
- **Phân định ranh giới dữ liệu (Data Isolation)**: Người dùng thuộc vai trò nào chỉ được thấy và thao tác đúng phạm vi dữ liệu được cấp phép (Sinh viên chỉ thấy Ticket của mình; Nhân viên chỉ xử lý Ticket thuộc Phòng ban của mình).
- **Bảo vệ tài liệu nhạy cảm**: Chặn đứng nguy cơ rò rỉ file đính kèm (bảng điểm, giấy xác nhận, đơn từ...) bằng cơ chế đường dẫn bảo mật qua Secured API Proxy (không lộ đường dẫn lưu trữ tĩnh).
- **Tính minh bạch & Khả năng tra soát (Auditability)**: Ghi lại đầy đủ lịch sử các thao tác quan trọng để phục vụ công tác kiểm tra, đối soát khi có thắc mắc hoặc khiếu nại.

---

## 3. Danh Mục Yêu Cầu Chức Năng Kỹ Thuật (Technical Feature Specifications)

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Mapping Resource Baseline (M3) |
| :--- | :--- | :--- | :--- |
| **FR-SEC-01** | Xác thực & Quản lý phiên làm việc | Đăng nhập mã hóa, cấp Token xác thực (JWT/Session), tự động hết hạn phiên và cơ chế đăng xuất an toàn. | FR-ADM-01 (M3: 64h) |
| **FR-SEC-02** | Phân quyền theo vai trò (RBAC) | Kiểm soát quyền truy cập API và giao diện dựa trên 4 vai trò (`STUDENT`, `STAFF`, `MANAGER`, `ADMIN`). | FR-ADM-01 (M3: 64h) |
| **FR-SEC-03** | Bảo mật tệp đính kèm & Lưu trữ | Kiểm soát quyền tải/xem file đính kèm qua Secured API Proxy, quản lý thời hạn lưu trữ dữ liệu. | FR-ADM-03 & FR-ADM-04 (M3: 55h) |
| **FR-SEC-04** | Ghi nhận Nhật ký tra soát (Audit Log) | Tự động ghi vết các sự kiện hệ thống quan trọng (Đổi trạng thái, Phân công, Chuyển phòng ban, Khóa tài khoản) dưới dạng immutable log. | FR-ADM-03 (M3: 40h) |

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
│      MANAGER/ADMIN)                │
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

| Phạm Vi Dữ Liệu (Resource Scope) | Sinh Viên (`STUDENT`) | Nhân Viên (`STAFF`) | Quản Lý (`MANAGER`) | Quản Trị Viên (`ADMIN`) |
| :--- | :---: | :---: | :---: | :---: |
| **Ticket do mình tạo** | Full (Xem, Tạo, Bổ sung, Đánh giá) | N/A | N/A | N/A |
| **Ticket thuộc Phòng ban mình phụ trách** | ❌ Không có quyền | Full (Xem, Claim, Transfer, Resolve) | Xem & Phân công trong Phòng ban | Xem & Quản trị |
| **Ticket thuộc Phòng ban khác** | ❌ Không có quyền | ❌ Không có quyền | ❌ Không có quyền | Xem tra soát |
| **Tệp đính kèm của Ticket** |  (Chỉ file thuộc Ticket của mình) |  (Chỉ file thuộc Ticket của PB mình) |  (Chỉ file thuộc Ticket của PB mình) |  (Tải tra soát) |
| **Báo cáo & Thống kê KPI** | ❌ Không có quyền | ❌ Không có quyền |  (Dữ liệu PB phụ trách) |  (Dữ liệu Toàn trường) |
| **Quản lý Tài khoản & Audit Log** | ❌ Không có quyền | ❌ Không có quyền | ❌ Không có quyền |  (Toàn bộ hệ thống) |

*Ghi chú:  = Có quyền truy cập | ❌ = Cấm truy cập*