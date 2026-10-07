# Tổng Quan Nghiệp Vụ Hỗ Trợ Sinh Viên (Domain Overview)

## 1. Bối Cảnh Nghiệp Vụ Tại Aurora University
Tại **Aurora University**, dịch vụ hỗ trợ sinh viên đóng vai trò cầu nối quan trọng giữa Sinh viên và các Đơn vị/Phòng ban chuyên trách trong toàn trường. Các nhóm nghiệp vụ hỗ trợ phổ biến bao gồm:

- **Phòng Đào tạo**: Giải quyết các vấn đề đăng ký tín chỉ, miễn giảm học phần, cấp bảng điểm, xác nhận điểm, đăng ký tốt nghiệp, hoãn thi.
- **Phòng Công tác Học sinh Sinh viên (CTHSSV)**: Xác nhận sinh viên, giải quyết chế độ chính sách, học bổng, khen thưởng, kỷ luật, thẻ sinh viên, ký túc xá.
- **Phòng Tài chính - Kế toán**: Giải đáp thắc mắc về học phí, hóa đơn, hoàn phí, gia hạn nộp học phí.
- **Trung tâm Công nghệ Thông tin**: Cấp lại mật khẩu tài khoản portal, lỗi kết nối Wi-Fi, hỗ trợ phần mềm học tập, email sinh viên.
- **Thư viện & Bộ phận Khác**: Mượn trả giáo trình, cấp tài khoản thư viện số, xác nhận nghĩa vụ thư viện.

---

## 2. Mục Tiêu Chuẩn Hóa Miền Nghiệp Vụ (Domain Objectives)

Trước khi triển khai UniSupport, quy trình trao đổi mang tính thủ công, thiếu tính nhất quán và không lưu vết. Việc chuẩn hóa miền nghiệp vụ hướng tới 4 nguyên tắc cốt lõi:
```
┌────────────────────────────────────────────────────────────────────────┐
│                        4 NGUYÊN TẮC CỐT LÕI                            │
├───────────────────┬───────────────────┬────────────────┬───────────────┤
│ 1. ĐỊNH DANH      │ 2. PHÂN ĐỊNH      │ 3. LƯU VẾT     │ 4. RÕ RÀNG    │
│    DUY NHẤT       │    TRÁCH NHIỆM    │    MINH BẠCH   │    TRẠNG THÁI │
│ (Ticket ID)       │ (Department/Agent)│ (Audit Trail)  │ (Lifecycle)   │
└───────────────────┴───────────────────┴────────────────┴───────────────┘
```

1. **Định danh duy nhất (Single Identifier)**: Mọi yêu cầu từ sinh viên được đóng gói thành một đơn vị nghiệp vụ gọi là **Ticket** với một mã định danh duy nhất (Ticket ID).
2. **Phân định trách nhiệm (Ownership Assignment)**: Mỗi Ticket luôn thuộc về **01 Phòng ban phụ trách**. Sau khi trải qua bước Tiếp nhận (Claim) hoặc Phân công (Assign), Ticket mới được gắn với **01 Nhân viên thụ lý (Assignee)** chính. Ở giai đoạn khởi tạo (`NEW`) hoặc khi đang chuyển phòng ban, trường Nhân viên thụ lý có thể để trống (`NULL`).
3. **Lưu vết minh bạch (Complete Auditability)**: Các thao tác quan trọng liên quan đến quá trình xử lý Ticket như thay đổi trạng thái, thay đổi đơn vị/người phụ trách, yêu cầu bổ sung và ghi nhận kết quả được lưu lại để phục vụ tra soát.
4. **Vòng đời trạng thái rõ ràng (Strict Lifecycle)**: Ticket được quản lý theo các trạng thái và quy tắc chuyển trạng thái thống nhất trong toàn hệ thống.
---

## 3. Bản Đồ Tổng Quan Các Luồng Nghiệp Vụ (Business Process Map)
```
[Sinh viên tạo Ticket]
        |
        v
[Hệ thống tạo mã Ticket và ghi nhận yêu cầu]
        |
        v
[Ticket được đưa vào hàng chờ xử lý]
        |
        v
[Nhân viên tiếp nhận / được phân công]
        |
        v
[Phân loại và xử lý Ticket]
        |
        +-----------------------------+
        |                             |
        | Cần bổ sung thông tin       | Cần chuyển đơn vị xử lý
        v                             v
[Nhân viên yêu cầu bổ sung]     [Chuyển phòng ban / người phụ trách]
        |                             |
        v                             v
[Sinh viên bổ sung thông tin]   [Đơn vị/người phụ trách mới tiếp nhận]
        |                             |
        +-------------+---------------+
                      |
                      v
             [Tiếp tục xử lý Ticket]
                      |
                      v
             [Ghi nhận kết quả xử lý]
                      |
                      v
                [Đóng Ticket]
                      |
                      v
         [Sinh viên xem kết quả và đánh giá]
```