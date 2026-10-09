# 06-acceptance: Tiêu chí & Kịch bản Nghiệm thu UniSupport

Thư mục này đóng vai trò làm bộ tài liệu căn cứ phục vụ cho quá trình kiểm thử nội bộ và **giai đoạn Nghiệm thu UAT 10 ngày làm việc** của Aurora University (được quy định tại Mục 5.2 của Project Proposal).

---

## Danh mục Tài liệu

| Tên File | Nội dung chính |
| :--- | :--- |
| **[traceability-matrix.md](./traceability-matrix.md)** | Ma trận truy xuất yêu cầu (RTM) liên kết giữa Yêu cầu nghiệp vụ, Quy trình, Phân hệ và Test Scenario. |
| **[test-scenarios.md](./test-scenarios.md)** | Chi tiết các kịch bản kiểm thử UAT cho 3 phân hệ (Sinh viên, Nhân viên, Quản lý) và Bảo mật. |

---

## Phạm vi truy xuất

RTM và kịch bản bám 14 FR đã chốt. 17 dòng Resources là công sức được đối chiếu riêng; không dùng chúng đổi mã yêu cầu hoặc cộng thêm 17 chức năng. Các ca hiện là dự kiến, chưa có bằng chứng chạy để xác nhận Pass. QA/UAT dùng giờ trong bảng nguồn, không tự tạo một ngân sách giờ khác.

## Quy trình & Tiêu chí Nghiệm thu (Acceptance Process)

### 1. Thời gian Nghiệm thu
- Quý trường (Aurora University) có **10 ngày làm việc** kể từ ngày bàn giao chính thức để tiến hành kiểm thử UAT trên môi trường Staging/Production.

### 2. Tiêu chí Đạt Nghiệm thu (Pass Criteria)
- Các luồng chính của 3 phân hệ (Sinh viên, Nhân viên, Quản lý) hoạt động đúng kịch bản và ổn định.
- Phân quyền RBAC hoạt động chính xác theo từng vai trò; bảo mật tệp đính kèm được đảm bảo.
- Không còn lỗi làm gián đoạn chức năng chính (Blocking/Critical bugs).
- Bàn giao đầy đủ tài liệu hướng dẫn sử dụng, tài liệu cài đặt, ERD và mã nguồn theo cam kết.

### 3. Quy định xử lý lỗi phát sinh
- Các lỗi kỹ thuật nhỏ phát sinh do phía đơn vị phát triển (nếu có) được ghi nhận và có kế hoạch khắc phục cụ thể, không tính là điều kiện từ chối nghiệm thu nếu không ảnh hưởng trực tiếp đến chức năng chính của hệ thống.
