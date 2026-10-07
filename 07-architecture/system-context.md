# Sơ Đồ Ngữ Cảnh Hệ Thống (System Context)

## 1. Tổng Quan Ngữ Cảnh
Hệ thống **UniSupport** đóng vai trò là Web Application tập trung duy nhất tiếp nhận, điều phối và xử lý toàn bộ các yêu cầu hỗ trợ từ sinh viên Aurora University. Hệ thống vận hành độc lập trên hạ tầng máy chủ của nhà trường và tương tác trực tiếp với 3 nhóm người dùng chính.

---

## 2. Sơ Đồ Ngữ Cảnh (C4 Context Diagram)

```text
                               ┌─────────────────────────┐
                               │   Sinh Viên (Student)   │
                               │     (3.000 sinh viên)   │
                               └────────────┬────────────┘
                                            │
                                  Gửi Ticket, Tra cứu,
                                  Bổ sung hồ sơ, Đánh giá
                                            │
                                            ▼
 ┌────────────────────────┐    ┌─────────────────────────┐    ┌────────────────────────┐
 │ Nhân Viên (Staff)      │───►│    Hệ Thống Web App    │◄───│  Quản Lý (Manager)     │
 │ (Phòng Đào tạo, CTTT,  │    │       UniSupport        │    │  (Ban Giám hiệu,       │
 │ Tài chính, Kỹ thuật)   │    │  (Aurora University)    │    │   Trưởng phòng ban)    │
 └────────────────────────┘    └─────────────────────────┘    └────────────────────────┘
    Tiếp nhận, Phân loại,          tiếp nhận & Quản lý           Xem Dashboard, Báo cáo,
    Xử lý & Đóng Ticket           Vòng đời Ticket hỗ trợ         Quản trị phân quyền
```

---

## 3. Các Luồng Tương Tác Chính
* **Sinh viên**: Truy cập qua trình duyệt Web Desktop/Mobile để gửi yêu cầu, theo dõi trạng thái qua mã Ticket, tải lên file bổ sung và đánh giá chất lượng dịch vụ.
* **Nhân viên**: Tiếp nhận yêu cầu thuộc phòng ban, điều phối chuyển tiếp, yêu cầu sinh viên bổ sung tài liệu và cập nhật kết quả xử lý chính thức.
8 **Quản lý**: Giám sát tổng quan chỉ số vận hành, khối lượng công việc, theo dõi xu hướng sự cố và cấp quyền tài khoản.