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
3. **Lưu vết minh bạch (Complete Auditability)**: Tất cả hành động (chuyển trạng thái, nhắn phản hồi, chuyển phòng ban, đăng tải file) đều được ghi nhật ký và không thể sửa/xóa.
4. **Vòng đời trạng thái rõ ràng (Strict Lifecycle)**: Ticket chuyển đổi trạng thái dựa trên các quy tắc nghiệp vụ chặt chẽ, tránh trạng thái mập mờ hoặc treo không thời hạn.

---

## 3. Bản Đồ Tổng Quan Các Luồng Nghiệp Vụ (Business Process Map)
```
[Sinh viên tạo Ticket]
        │
        ▼
[Hệ thống cấp Mã Ticket & Gửi về Phòng ban]
        │
        ▼
[Nhân viên tiếp nhận (Claim) / Phân công (Assign)]
        │
        ├───► [Cần bổ sung hồ sơ] ───► [Sinh viên cập nhật file/thông tin]
        │                                        │
        │                                        │
        ├───► [Gửi nhầm phòng ban] ──► [Chuyển phòng ban chuyên trách]
        │                                        │
        ▼                                        ▼
[Xử lý & Cập nhật kết quả giải quyết] ◄──────────┘
        │
        ▼
[Đóng Ticket & Sinh viên đánh giá hài lòng (CSAT)]
```