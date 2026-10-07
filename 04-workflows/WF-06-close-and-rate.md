# QTTN 06: Sinh Viên Nhận Kết Quả & Đánh Giá Mức Độ Hài Lòng (WF-06)

## 1. Mục Tiêu Quy Trình
Cho phép sinh viên xem kết quả xử lý và gửi phản hồi, đánh giá chất lượng phục vụ của nhà trường đối với Ticket đã đóng[cite: 1].

---

## 2. Tác Nhân Tham Gia (Actors)
* **Sinh viên:** Người nhận kết quả và thực hiện đánh giá[cite: 1].
* **Hệ thống UniSupport:** Ghi nhận điểm số rating và đóng biểu mẫu đánh giá[cite: 1].

---

## 3. Lược Đồ Quy Trình (Sequence Diagram)

```text
[Sinh viên]                  [Giao diện Web]                [Backend / CSDL]
    │                               │                              │
    │ ─── 1. Xem thông báo CLOSED ─>│                              │
    │ ─── 2. Đọc kết quả xử lý ────>│                              │
    │ ─── 3. Chọn Sao (1-5) & Ý kiến>│                              │
    │ ─── 4. Bấm "Gửi đánh giá" ───>│                              │
    │                               │ ─── 5. Kiểm tra chưa đánh giá>│
    │                               │ ─── 6. Lưu Rating & Comment ─>│
    │                               │<─── 7. Trả về thành công ────│
    │<─── 8. Ẩn form & Cảm ơn ──────│                              │
```

---

## 4. Các Bước Thực Hiện
* **Sinh viên**: Nhận được thông báo kết quả, nhấp mở xem thông báo hoặc truy cập danh sách Ticket cá nhân[cite: 1].
* **Sinh viên**: Đọc nội dung Ghi chú kết quả giải quyết từ nhân viên[cite: 1].
* **Sinh viên**: Hệ thống hiển thị biểu mẫu đánh giá hài lòng[cite: 1].
* **Sinh viên**: Chọn số sao (từ 1 đến 5 sao) và nhập nhận xét góp ý (không bắt buộc)[cite: 1].
* **Sinh viên**: Bấm nút Gửi đánh giá[cite: 1].
* **Hệ thống**: Kiểm tra lượt đánh giá (đảm bảo mỗi Ticket chỉ được đánh giá 01 lần duy nhất)[cite: 1].
* **Hệ thống**: Lưu số sao (rating_score) và nhận xét (rating_comment) vào bản ghi Ticket, đồng thời ẩn biểu mẫu đánh giá và hiển thị thông báo cảm ơn[cite: 1].
