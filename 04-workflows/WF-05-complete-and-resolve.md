# QTTN 05: Cập Nhật Kết Quả & Đóng Yêu Cầu (WF-05)

## 1. Mục Tiêu Quy Trình
Ghi nhận kết quả xử lý chính thức từ nhân viên và hoàn tất vòng đời giải quyết Ticket[cite: 1].

---

## 2. Tác Nhân Tham Gia (Actors)
* **Nhân viên phụ trách:** Người nhập kết quả và đóng Ticket[cite: 1].
* **Hệ thống UniSupport:** Lưu kết quả và cập nhật thời gian đóng (`closed_at`)[cite: 1].

---

## 3. Các Bước Thực Hiện

1. **Nhân viên:** Đã thực hiện xong các nghiệp vụ giải quyết cho sinh viên, bấm nút **Hoàn thành & Đóng Ticket**[cite: 1].
2. **Hệ thống:** Hiển thị ô nhập **Ghi chú kết quả giải quyết** (`resolution_note`)[cite: 1].
3. **Nhân viên:** Nhập chi tiết câu trả lời / phương án xử lý chính thức cho sinh viên và bấm **Xác nhận đóng**[cite: 1].
4. **Hệ thống:** Kiểm tra nội dung kết quả (không được để trống hoặc chỉ nhập khoảng trắng)[cite: 1].
5. **Hệ thống:** Cập nhật trạng thái Ticket thành `CLOSED`, ghi nhận mốc thời gian `closed_at`[cite: 1].
6. **Hệ thống:** Phát thông báo nội bộ cho sinh viên biết Ticket đã có kết quả giải quyết chính thức[cite: 1].