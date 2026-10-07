# QTTN 02: Nhân Viên Tiếp Nhận & Phân Loại / Đánh Giá Độ Ưu Tiên (WF-02)

## 1. Mục Tiêu Quy Trình
Chuẩn hóa các bước nhân viên phòng ban tiếp nhận Ticket mới (`NEW`), kiểm tra phân loại nhóm vấn đề và gán mức độ ưu tiên xử lý[cite: 1].

---

## 2. Tác Nhân Tham Gia (Actors)
* **Nhân viên phòng ban:** Người tiếp nhận và thụ lý Ticket[cite: 1].
* **Hệ thống UniSupport:** Cập nhật trạng thái và người phụ trách (`Assignee`)[cite: 1].

---

## 3. Các Bước Thực Hiện

1. **Nhân viên:** Đăng nhập vào phân hệ Nhân viên, truy cập danh sách **Ticket chờ tiếp nhận** của phòng ban[cite: 1].
2. **Nhân viên:** Chọn một Ticket để xem chi tiết thông tin, file đính kèm và yêu cầu của sinh viên[cite: 1].
3. **Nhân viên:** Nhấn nút **Tiếp nhận xử lý**[cite: 1].
4. **Nhân viên:** Kiểm tra nhóm vấn đề (điều chỉnh lại nếu sinh viên chọn sai) và thiết lập mức **Độ ưu tiên** (`LOW`, `MEDIUM`, `HIGH`, `URGENT`)[cite: 1].
5. **Nhân viên:** Nhấn **Xác nhận tiếp nhận**.
6. **Hệ thống:** Cập nhật trạng thái Ticket từ `NEW` sang `IN_PROGRESS`, gán ID nhân viên vào trường `Assignee`[cite: 1].
7. **Hệ thống:** Ghi vết lịch sử tiếp nhận và gửi thông báo in-app cho sinh viên biết Ticket đã được tiếp nhận xử lý[cite: 1].

---

## 4. Ngoại Lệ (Exception Flows)
* Nếu Ticket bị người khác tiếp nhận trước: Hệ thống báo lỗi "Ticket đã được tiếp nhận bởi nhân viên khác" và tải lại danh sách[cite: 1].