# Phân Hệ Sinh Viên (M01 - Student Portal)

> Nguồn phân bổ công sức chuẩn hóa: `Phan_bo_Resources_Antigravity.md` (Sheet M1 – Student)

## 1. Tổng Quan Phân Hệ

Phân hệ **Sinh viên (Student Portal)** là điểm giao tiếp số duy nhất dành cho khoảng 3.000 sinh viên tại **Aurora University**. Phân hệ này cho phép sinh viên tra cứu kiến thức hướng dẫn/FAQ, khởi tạo yêu cầu hỗ trợ (Ticket), theo dõi tiến độ thời gian thực, nhận thông báo trạng thái tức thời và bổ sung thông tin/đánh giá kết quả dịch vụ.

---

## 2. Mục Tiêu & Giá Trị Mang Lại

- **Tra cứu tiện lợi (Self-service Knowledge)**: Tìm kiếm nhanh quy trình, thủ tục hành chính và FAQ trước khi tạo yêu cầu.
- **Đơn giản hóa thao tác**: Giao diện thân thiện, responsive tối ưu trên cả Máy tính desktop và Thiết bị di động.
- **Minh bạch hóa tiến độ**: Sinh viên nắm bắt chính xác Ticket của mình đang ở đâu, thuộc phòng ban nào, ai xử lý và dự kiến khi nào hoàn tất.
- **Tương tác hai chiều dễ dàng**: Bổ sung giấy tờ/file đính kèm (PDF, Ảnh) trực tiếp trên Ticket khi có yêu cầu từ nhà trường.
- **Ghi nhận phản hồi**: Chấm điểm CSAT (1-5 sao) để góp phần nâng cao chất lượng dịch vụ của Aurora University.

---

## 3. Danh Mục Yêu Cầu Chức Năng & Phân Bổ Effort (Effort Breakdown)

*Tổng Effort Phân hệ M1: **124h cơ sở + 4h buffer = 128h kế hoạch***

| Mã Chức Năng | Tên Chức Năng | Tóm Tắt Nghiệp Vụ | Effort Cơ Sở (h) | Buffer (h) | Effort Kế Hoạch (h) | Phân Bổ Role (h) |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **FR-STU-01** | Tra cứu hướng dẫn & FAQ | Tìm kiếm nhanh bài viết hướng dẫn, quy trình thủ tục và câu hỏi thường gặp theo Phòng ban. | 14 | 0 | **14h** | BA: 3, UI/UX: 3, FE1: 4, QA: 4 |
| **FR-STU-02** | Tạo & gửi yêu cầu hỗ trợ | Chọn nhóm vấn đề, mô tả chi tiết, tải file đính kèm (PDF/Ảnh), sinh Mã Ticket duy nhất. | 34 | 3 | **37h** | BA: 5, UI/UX: 5, TL: 1, FE1: 10, FE2: 1, BE1: 6, BE2: 1, QA: 5 |
| **FR-STU-03** | Xem & theo dõi yêu cầu | Xem danh sách Ticket cá nhân, trạng thái thời gian thực (`NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED`, `CLOSED`), nhật ký trao đổi. | 32 | 1 | **33h** | BA: 4, UI/UX: 3, TL: 1, FE1: 8, FE2: 3, BE1: 5, BE2: 3, QA: 5 |
| **FR-STU-04** | Nhận thông báo trạng thái | Trung tâm thông báo quả chuông (Bell Icon), thông báo In-app khi có cập nhật trên Ticket. | 19 | 0 | **19h** | BA: 3, UI/UX: 1, FE1: 4, BE1: 4, BE2: 4, QA: 3 |
| **FR-STU-05** | Bổ sung thông tin & phản hồi | Cập nhật câu trả lời/file minh chứng khi có yêu cầu bổ sung, xem kết quả và đánh giá CSAT (1-5 sao). | 25 | 0 | **25h** | BA: 3, UI/UX: 1, FE1: 5, FE2: 3, BE1: 5, BE2: 3, QA: 5 |
| **TỔNG M1** | **TỔNG PHÂN HỆ SINH VIÊN** | | **124h** | **4h** | **128h** | **BA: 18, UI/UX: 13, TL: 2, FE1: 31, FE2: 7, BE1: 20, BE2: 11, QA: 22** |

---

## 4. Sơ Đồ Luồng Tương Tác Của Sinh Viên (User Journey)
```
[Tra cứu FAQ FR-STU-01] ──► (Chưa giải quyết được) ──► [Tạo Ticket FR-STU-02] ──► [Nhận Mã Ticket]
                                                                                        │
                                                                                        ▼
                                                                      [Theo dõi tiến độ FR-STU-03]
                                                                      [Nhận thông báo FR-STU-04]
                                                                                        │
                                                              ┌─────────────────────────┤
                                                              │                         │
                                                              │ (Nếu Nhân viên yêu cầu) │
                                                              ▼                         ▼
                                                   [Bổ sung giấy tờ FR-STU-05]   [Nhận kết quả giải quyết]
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