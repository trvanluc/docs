# Phân Hệ Sinh Viên (M01 - Student Portal)

## 1. Tổng Quan Phân Hệ

Phân hệ **Sinh viên (Student Portal)** là điểm giao tiếp số duy nhất dành cho khoảng 3.000 sinh viên tại **Aurora University**. Phân hệ này cho phép sinh viên khởi tạo, theo dõi, tương tác và đánh giá toàn bộ các yêu cầu hỗ trợ (Ticket) từ hành chính, đào tạo, học phí cho đến kỹ thuật mà không cần phải đến trực tiếp văn phòng một cửa hay gửi email rời rạc.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Đơn giản hóa thao tác**: Giao diện thân thiện, responsive tối ưu trên cả Máy tính desktop và Thiết bị di động.
- **Minh bạch hóa tiến độ**: Sinh viên nắm bắt chính xác Ticket của mình đang ở đâu, thuộc phòng ban nào, ai xử lý và dự kiến khi nào hoàn tất.
- **Tương tác hai chiều dễ dàng**: Bổ sung giấy tờ/file đính kèm (PDF, Ảnh) trực tiếp trên Ticket khi có yêu cầu từ nhà trường.
- **Ghi nhận phản hồi**: Chấm điểm CSAT (1-5 sao) để góp phần nâng cao chất lượng dịch vụ của Aurora University.

---

## 3. Danh Mục Yêu Cầu Chức Năng & Phân Rã Effort (Functional Requirements & Effort Decomposition)

*Tổng Effort Baseline M01: **128 giờ***

| Mã Yêu Cầu | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Effort Dự Kiến (Giờ) |
| :--- | :--- | :--- | :---: |
| **FR-STU-01** | Đăng nhập hệ thống | Sinh viên đăng nhập bằng tài khoản cá nhân do nhà trường cấp. | **16h** |
| **FR-STU-02** | Gửi yêu cầu hỗ trợ | Chọn nhóm vấn đề, mô tả tình huống, tải file đính kèm (PDF/Ảnh), nhận Mã Ticket duy nhất. | **36h** |
| **FR-STU-03** | Xem tiến độ & Lịch sử Ticket | Xem danh sách Ticket đã gửi, trạng thái thời gian thực (`NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`), nhật ký trao đổi. | **32h** |
| **FR-STU-04** | Bổ sung thông tin / Hồ sơ | Cập nhật câu trả lời hoặc đăng tải thêm giấy tờ minh chứng khi nhân viên yêu cầu bổ sung. | **20h** |
| **FR-STU-05** | Xem kết quả & Đánh giá (CSAT) | Xem nội dung/file kết quả giải quyết, thực hiện chấm điểm hài lòng (1-5 sao) và để lại phản hồi. | **24h** |
| **TỔNG CỘNG** | | | **128h** |

---

## 4. Sơ Đồ Luồng Tương Tác Của Sinh Viên (User Journey)
```
[Đăng nhập FR-STU-01] ──► [Tạo Ticket FR-STU-02] ──► [Nhận Mã Ticket]
                                                        │
                                                        ▼
                                      [Theo dõi tiến độ FR-STU-03]
                                                        │
                              ┌─────────────────────────┤
                              │                         │
                              │ (Nếu Nhân viên yêu cầu) │
                              ▼                         ▼
                   [Bổ sung giấy tờ FR-STU-04]   [Nhận kết quả giải quyết]
                              │                         ▲
                              └─────────────────────────┘
                                                        │
                                                        ▼
                                      [Đánh giá CSAT FR-STU-05]
                                                        │
                                                        ▼
                                          [Đóng Ticket hoàn tất]
```

---

## 5. Các Ràng Buộc & Quy Tắc Thiết Kế Giao Diện (UI/UX Guidelines)

1. **Responsive Mobile First**: Thiết kế chuẩn trên di động để sinh viên có thể chụp ảnh giấy tờ bằng điện thoại và upload trực tiếp.
2. **Đa ngôn ngữ**: Hỗ trợ chuyển đổi nhanh giao diện Tiếng Việt và Tiếng Anh cơ bản.
3. **Trạng thái trực quan (Visual Badges)**: Trạng thái Ticket phải được hiển thị bằng màu sắc rõ ràng:
   - `NEW` - Xanh dương
   - `IN_PROGRESS` - Cam
   - `WAITING_STUDENT` - Vàng
   - `RESOLVED` - Xanh lá
   - `CLOSED` - Xám
4. **An toàn file đính kèm**: Kiểm tra dung lượng file (tối đa 10MB) ngay tại client trước khi thực hiện upload.