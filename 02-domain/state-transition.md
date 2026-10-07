# Ma Trận Chuyển Đổi Trạng Thái Ticket (State Transition)

## 1. Danh Sách Các Trạng Thái (States)
* **`NEW` (Mới):** Ticket vừa được sinh viên khởi tạo, chưa có nhân viên nhận xử lý[cite: 1].
* **`IN_PROGRESS` (Đang xử lý):** Ticket đã được gán cho nhân viên và đang trong quá trình giải quyết[cite: 1].
* **`NEED_MORE_INFO` (Chờ bổ sung):** Nhân viên đã gửi yêu cầu và đang chờ sinh viên bổ sung tài liệu/giấy tờ[cite: 1].
* **`TRANSFERRED` (Đã chuyển tiếp):** Ticket được chuyển đổi phòng ban phụ trách[cite: 1].
* **`RESOLVED` / `CLOSED` (Đã hoàn tất):** Yêu cầu đã được xử lý xong và ghi nhận kết quả thành công[cite: 1].
* **`REJECTED` (Từ chối):** Yêu cầu không hợp lệ hoặc không đủ điều kiện xử lý[cite: 1].

---

## 2. Ma Trận Chuyển Đổi Trạng Thái (Transition Matrix)

| Trạng thái hiện tại | Trạng thái đích cho phép | Tác nhân thực hiện | Điều kiện / Hành động kích hoạt |
| :--- | :--- | :--- | :--- |
| **`NEW`** | `IN_PROGRESS` | Nhân viên | Tiếp nhận Ticket & gán độ ưu tiên/người xử lý[cite: 1]. |
| **`NEW`** | `TRANSFERRED` | Nhân viên | Chuyển Ticket sang phòng ban khác do sai thẩm quyền[cite: 1]. |
| **`NEW`** | `REJECTED` | Nhân viên | Từ chối do yêu cầu không đúng quy định/thiếu thông tin bắt buộc[cite: 1]. |
| **`IN_PROGRESS`** | `NEED_MORE_INFO` | Nhân viên | Yêu cầu sinh viên bổ sung thêm giấy tờ/minh chứng[cite: 1]. |
| **`IN_PROGRESS`** | `TRANSFERRED` | Nhân viên | Chuyển giao phòng ban chuyên trách khác[cite: 1]. |
| **`IN_PROGRESS`** | `CLOSED` | Nhân viên | Nhập ghi chú kết quả giải quyết & đóng Ticket[cite: 1]. |
| **`NEED_MORE_INFO`**| `IN_PROGRESS` | Sinh viên | Đã nộp/bổ sung đủ hồ sơ theo yêu cầu[cite: 1]. |
| **`TRANSFERRED`** | `IN_PROGRESS` | Nhân viên (PB mới)| Nhân viên thuộc phòng ban mới nhận xử lý[cite: 1]. |
| **`CLOSED`** | *(Trạng thái cuối)* | Sinh viên | Sinh viên thực hiện đánh giá mức độ hài lòng[cite: 1]. |