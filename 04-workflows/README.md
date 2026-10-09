# 04-workflows: Quy trình Nghiệp vụ UniSupport

Thư mục này chứa toàn bộ tài liệu mô tả chi tiết các **Quy trình Nghiệp vụ (Workflows)** của hệ thống UniSupport tại Aurora University. Các quy trình được chuẩn hóa nhằm đảm bảo tính minh bạch, đúng phân quyền và theo sát vòng đời của một Ticket hỗ trợ.

---

## Danh sách Quy trình Nghiệp vụ

| Mã Workflow | Tên Quy trình | Vai trò chính | Mô tả ngắn gọn |
| :--- | :--- | :--- | :--- |
| **[WF-01](./WF-01-submit-support-request.md)** | Gửi yêu cầu hỗ trợ | Sinh viên | Sinh viên tạo Ticket, chọn nhóm vấn đề, đính kèm file (ảnh/PDF) và nhận mã Ticket. |
| **[WF-02](./WF-02-claim-and-triage.md)** | Tiếp nhận & Phân loại | Nhân viên | Nhân viên tiếp nhận (claim) Ticket, cập nhật độ ưu tiên và kiểm tra nhóm vấn đề. |
| **[WF-03](./WF-03-request-supplement.md)** | Yêu cầu bổ sung hồ sơ | Nhân viên & Sinh viên | Nhân viên yêu cầu bổ sung giấy tờ; sinh viên phản hồi và đính kèm file bổ sung. |
| **[WF-04](./WF-04-transfer-department.md)** | Chuyển tiếp phòng ban | Nhân viên | Chuyển Ticket sang phòng ban khác kèm lý do chuyển minh bạch. |
| **[WF-05](./WF-05-complete-and-resolve.md)** | Cập nhật kết quả & Hoàn tất xử lý | Nhân viên | Ghi kết quả, tệp kết quả nếu có và chuyển RESOLVED; đóng theo WF-06/vòng đời hiện có. |
| **[WF-06](./WF-06-close-and-rate.md)** | Nhận kết quả & Đánh giá | Sinh viên | Sinh viên xem kết quả xử lý và đánh giá độ hài lòng (1–5 sao). |

---

## Quy chuẩn Cấu trúc tài liệu Workflow

Mỗi file quy trình nghiệp vụ trong thư mục này tuân thủ thống nhất các phần nội dung sau:
1. **Mô tả (Description):** Tóm tắt mục đích nghiệp vụ.
2. **Actor:** Các vai trò tham gia thực hiện.
3. **Preconditions:** Điều kiện tiên quyết để kích hoạt quy trình.
4. **Luồng chính (Main Flow):** Các bước thực hiện theo thứ tự chuẩn.
5. **Business Rules:** Quy tắc nghiệp vụ bắt buộc tuân thủ.
6. **Alternative / Error Flows:** Khả năng xử lý các trường hợp ngoại lệ/lỗi.
7. **Acceptance Criteria (AC):** Tiêu chí nghiệm thu rõ ràng.
8. **Ví dụ Edge Case:** Minh họa tình huống biên cụ thể và kết quả mong đợi.
