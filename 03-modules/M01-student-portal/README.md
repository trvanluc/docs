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

## 3. Danh Mục Yêu Cầu Chức Năng & Phân Rã Effort Theo Bảng Chi Phí Nội Bộ

*Tổng Effort kế hoạch M01: **128 giờ***

| Gói việc | Tóm Tắt Nghiệp Vụ | Effort |
| :--- | :--- | :---: |
| **Tra cứu hướng dẫn & FAQ** | Sinh viên tra cứu hướng dẫn/FAQ cơ bản trước hoặc trong quá trình tạo yêu cầu hỗ trợ. | **14h** |
| **Tạo & gửi yêu cầu hỗ trợ** | Chọn nhóm vấn đề, mô tả tình huống, tải file đính kèm (PDF/Ảnh), nhận Mã Ticket duy nhất. | **37h** |
| **Xem & theo dõi yêu cầu** | Xem danh sách Ticket đã gửi, trạng thái hiện tại, phòng ban/người phụ trách và lịch sử cập nhật. | **33h** |
| **Nhận thông báo trạng thái** | Nhận thông báo nội bộ khi Ticket được tiếp nhận, yêu cầu bổ sung, chuyển trạng thái hoặc hoàn tất. | **19h** |
| **Bổ sung thông tin & phản hồi** | Cập nhật câu trả lời hoặc đăng tải thêm giấy tờ minh chứng khi nhân viên yêu cầu bổ sung. | **25h** |
| **Tổng M1 - Student** | | **128h** |

Ghi chú: Đăng nhập, xem kết quả và đánh giá CSAT vẫn thuộc phạm vi M01 theo proposal; trong bảng chi phí nội bộ, các phần này được gộp vào các gói việc Student tương ứng thay vì tách thành dòng effort riêng.

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
