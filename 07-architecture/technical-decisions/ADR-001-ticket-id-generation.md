# [ADR-001] Quy tắc sinh mã Ticket duy nhất (Ticket ID Generation Strategy)

* **Trạng thái:** Đã phê duyệt (Accepted)
* **Ngày quyết định:** 2026-10-05
* **Người quyết định:** Tech Lead / System Architect
* **Phân hệ liên quan:** `02-domain`, `M01-student-portal`, `M02-staff-operations`

---

## 1. Bối cảnh (Context)
Hệ thống UniSupport yêu cầu mỗi phiếu hỗ trợ (Ticket) phải có một định danh duy nhất để sinh viên dễ dàng tra cứu, nhân viên tiện trao đổi và hệ thống dễ truy vấn.
- Mã định danh trong CSDL sử dụng khóa chính dạng tự tăng (Auto-increment ID) hoặc UUID để tối ưu index.
- Tuy nhiên, giao diện người dùng cần một mã Ticket ngắn gọn, dễ đọc, dễ giao tiếp qua điện thoại/email nhưng vẫn đảm bảo tính duy nhất và không thể đoán trước quá dễ dàng.

## 2. Các phương án xem xét (Options Considered)
1. **Phương án 1: Dùng ID tự tăng của CSDL (Ví dụ: `1`, `2`, `1024`)**
   - *Ưu điểm:* Đơn giản, ngắn gọn.
   - *Nhược điểm:* Dễ lộ thông tin kinh doanh (số lượng Ticket của nhà trường), lộ quy luật số đếm.
2. **Phương án 2: Dùng UUID v4 (Ví dụ: `c9bf9e57-1685-4c89-bafb-ff5af830be8a`)**
   - *Ưu điểm:* Đảm bảo tính duy nhất tuyệt đối.
   - *Nhược điểm:* Quá dài, khó nhớ, không thân thiện khi đọc hoặc tìm kiếm nhanh.
3. **Phương án 3: Sinh mã định dạng Prefix + Timestamp/Random + Sequence (Ví dụ: `TK-202610-A89F`)**
   - *Ưu điểm:* Thân thiện, dễ phân biệt theo thời gian, độ dài vừa phải, chuyên nghiệp.
   - *Nhược điểm:* Cần xử lý logic sinh mã trùng lặp ở tầng ứng dụng hoặc DB constraint.

## 3. Quyết định (Decision)
Lựa chọn **Phương án 3**. Cấu trúc mã Ticket hiển thị cho người dùng sẽ bao gồm:
$$\text{Ticket Code} = \text{TK} + \text{[YYYYMM]} + \text{[4 Ký tự ngẫu nhiên AlphaNumeric/Sequence]}$$
*(Ví dụ: `TK-202610-8F3A`)*

- Khóa chính CSDL (Primary Key) vẫn lưu bằng `UUID` hoặc `BigInt` để đảm bảo hiệu năng liên kết bảng.
- Trường `ticket_code` lưu chuỗi trên, được gắn chỉ mục `UNIQUE INDEX` trong CSDL.

## 4. Hệ quả (Consequences)
* **Tích cực:** Mã Ticket thân thiện với người dùng, hỗ trợ nhận diện thời gian tạo, chuyên nghiệp và an toàn.
* **Tiêu cực:** Cần thêm bước validate hoặc hàm sinh mã bảo đảm không trùng lặp (retry mechanism nếu va chạm chuỗi ngẫu nhiên).