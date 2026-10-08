# ADR-001: Quy Tắc Sinh Mã Ticket Duy Nhất (Ticket ID Generation Strategy)

* **Trạng thái (Status):** Accepted (Đã chấp thuận)
* **Ngày quyết định:** Tuần 3 - Giai đoạn Thiết kế Kiến trúc

---

## 1. Bối Cảnh (Context)
Trong hệ thống UniSupport, mỗi yêu cầu hỗ trợ do sinh viên tạo ra cần một mã định danh duy nhất (Ticket ID) để sinh viên dễ dàng tra cứu, theo dõi tiến độ và để nhân viên/quản lý trao đổi, kiểm vết. 
Yêu cầu đặt ra:
* Mã Ticket phải ngắn gọn, dễ đọc, dễ truyền đạt qua lời nói/văn bản.
* Đảm bảo tính duy nhất tuyệt đối trong toàn bộ hệ thống.
* Chống trùng lặp ngay cả khi có nhiều yêu cầu gửi đồng thời (Concurrent Request/Retry).

---

## 2. Các Phương Án Cân Nhắc (Options Considered)
1. **Phương án A (UUID v4):** Sử dụng chuỗi ngẫu nhiên dài (ví dụ: `c9bf9e57-1685-4c89-bafb-ff5af830be8a`).
   * *Ưu điểm:* Duy nhất tuyệt đối.
   * *Nhược điểm:* Quá dài, sinh viên rất khó nhớ và bất tiện khi đọc tra cứu thủ công.
2. **Phương án B (Auto-increment ID):** Sử dụng số nguyên tăng dần của CSDL (ví dụ: `1`, `2`, `3`).
   * *Ưu điểm:* Ngắn gọn.
   * *Nhược điểm:* Dễ lộ quy mô giao dịch, không chứa thông tin ngữ cảnh thời gian.
3. **Phương án C (Formatted Business Key - Lựa chọn):** Cấu trúc chuỗi gồm Tiền tố + Ngày tháng + Số thứ tự tự tăng trong ngày (ví dụ: `TK-20261007-0001`).

---

## 3. Quyết Định (Decision)
Hệ thống chốt lựa chọn **Phương án C**: Sinh mã Ticket định dạng `TK-YYYYMMDD-XXXX`.

* `TK`: Tiền tố cố định đại diện cho Ticket UniSupport.
* `YYYYMMDD`: Năm, tháng, ngày khởi tạo yêu cầu (ví dụ: `20261007`).
* `XXXX`: Số thứ tự tự tăng trong ngày (4 chữ số, từ `0001` đến `9999`), sử dụng Redis Sequence hoặc CSDL Atomic Increment để đảm bảo tính duy nhất khi xử lý đồng thời.

---

## 4. Hệ Quả & Đánh Giá (Consequences)
* **Tích cực:** Mã Ticket trực quan, chuyên nghiệp, thể hiện rõ ngày tạo và dễ nhớ đối với sinh viên lẫn nhân viên.
* **Hạn chế:** Giới hạn tối đa 9.999 Ticket/ngày (phù hợp hoàn toàn với quy mô 3.000 sinh viên của dự án).