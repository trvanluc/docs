# QTTN 04: Chuyển Tiếp Yêu Cầu Sang Phòng Ban Khác (WF-04)

## 1. Mục Tiêu Quy Trình
Đảm bảo việc điều chuyển các Ticket bị gửi nhầm đơn vị sang đúng phòng ban có thẩm quyền giải quyết mà không làm gián đoạn lịch sử giao dịch.

---

## 2. Tác Nhân Tham Gia (Actors)
* **Nhân viên phòng ban cũ:** Người thực hiện chuyển giao.
* **Nhân viên/Phòng ban mới:** Đơn vị tiếp nhận mới.
* **Hệ thống UniSupport:** Cập nhật phòng ban thụ lý và ghi log chuyển tiếp.

---

## 3. Các Bước Thực Hiện

1. **Nhân viên:** Xác định Ticket không thuộc phạm vi xử lý của phòng ban mình, chọn nút **Chuyển phòng ban**.
2. **Nhân viên:** Chọn **Phòng ban đích** từ danh sách và nhập **Lý do chuyển tiếp** (bắt buộc).
3. **Nhân viên:** Bấm **Xác nhận chuyển**.
4. **Hệ thống:** Đổi trạng thái Ticket thành `TRANSFERRED`, xóa thông tin `Assignee` cũ và cập nhật `department_id` mới.
5. **Hệ thống:** Ghi nhật ký thao tác (Audit log) về việc điều chuyển phòng ban.
6. **Hệ thống:** Phát thông báo nội bộ cho Phòng ban mới biết có Ticket mới được chuyển đến.
7. **Nhân viên phòng ban mới:** Mở danh sách Ticket nhận chuyển tiếp và thực hiện quy trình tiếp nhận (`WF-02`).