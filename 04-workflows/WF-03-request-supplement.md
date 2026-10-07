# QTTN 03: Yêu Cầu Sinh Viên Bổ Sung Thông Tin / Giấy Tờ (WF-03)

## 1. Mục Tiêu Quy Trình
Xử lý tình huống Ticket thiếu minh chứng hoặc thông tin chưa rõ ràng, cho phép nhân viên yêu cầu sinh viên cung cấp thêm giấy tờ/file đính kèm[cite: 1].

---

## 2. Tác Nhân Tham Gia (Actors)
* **Nhân viên:** Người phát yêu cầu bổ sung[cite: 1].
* **Sinh viên:** Người nhận thông báo và tải lên minh chứng bổ sung[cite: 1].
* **Hệ thống UniSupport:** Chuyển đổi trạng thái hai chiều giữa `IN_PROGRESS` và `NEED_MORE_INFO`[cite: 1].

---

## 3. Các Bước Thực Hiện

1. **Nhân viên:** Trong màn hình chi tiết Ticket đang xử lý (`IN_PROGRESS`), chọn nút **Yêu cầu bổ sung hồ sơ**[cite: 1].
2. **Nhân viên:** Nhập chi tiết nội dung/giấy tờ cần sinh viên cung cấp thêm và bấm **Gửi**[cite: 1].
3. **Hệ thống:** Đổi trạng thái Ticket thành `NEED_MORE_INFO` và phát thông báo nội bộ tới sinh viên[cite: 1].
4. **Sinh viên:** Nhận thông báo, mở chi tiết Ticket và chọn **Bổ sung thông tin**[cite: 1].
5. **Sinh viên:** Tải lên các file đính kèm bổ sung (ảnh/PDF) hoặc nhập ghi chú giải trình, sau đó bấm **Xác nhận gửi**[cite: 1].
6. **Hệ thống:** Kiểm tra file hợp lệ (PNG/JPG/PDF <= 5MB), lưu thông tin bổ sung và tự động đổi trạng thái Ticket quay lại `IN_PROGRESS`[cite: 1].
7. **Hệ thống:** Phát thông báo cho Nhân viên phụ trách biết sinh viên đã nộp bổ sung hồ sơ[cite: 1].