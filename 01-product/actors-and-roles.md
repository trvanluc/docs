# Định Nghĩa Các Vai Trò Trong Hệ Thống (Actors & Roles)

Hệ thống UniSupport phân quyền người dùng dựa trên 3 vai trò chính (Role-Based Access Control - RBAC):

---

## 1. Sinh Viên (Student)
* **Mô tả:** Người dùng gửi yêu cầu hỗ trợ về các vấn đề học tập, hành chính, học phí hoặc kỹ thuật tại Aurora University.
* **Quyền hạn chính:**
  * Đăng nhập hệ thống bằng tài khoản cá nhân.
  * Tạo Ticket hỗ trợ mới (chọn phân loại, nhập mô tả, đính kèm file ảnh/PDF).
  * Xem tiến độ, lịch sử cập nhật và người/đơn vị đang phụ trách xử lý Ticket của mình.
  * Bổ sung thông tin/giấy tờ khi nhân viên yêu cầu.
  * Xem kết quả giải quyết và thực hiện đánh giá mức độ hài lòng.

---

## 2. Nhân Viên (Staff)
* **Mô tả:** Nhân viên thuộc các phòng ban nghiệp vụ (Phòng Đào tạo, Phòng Công tác sinh viên, Phòng Tài chính,...).
* **Quyền hạn chính:**
  * Đăng nhập hệ thống bằng tài khoản nhân viên.
  * Xem danh sách Ticket mới và Ticket được giao cho cá nhân/phòng ban.
  * Tiếp nhận, phân loại nhóm vấn đề và gắn mức độ ưu tiên.
  * Chuyển tiếp Ticket sang phòng ban/nhân viên khác nếu sai thẩm quyền.
  * Cập nhật trạng thái xử lý, gửi thông báo yêu cầu sinh viên bổ sung giấy tờ.
  * Ghi nhận kết quả xử lý và hoàn tất/đóng Ticket.

---

## 3. Quản Lý (Admin / Manager)
* **Mô tả:** Ban giám hiệu hoặc Trưởng/Phó các phòng ban quản lý vận hành hệ thống.
* **Quyền hạn chính:**
  * Đăng nhập bằng tài khoản quản lý.
  * Theo dõi Dashboard tổng quan về tình hình xử lý Ticket (mới, đang xử lý, quá hạn).
  * Giám sát tải công việc và thời gian xử lý của từng phòng ban, nhân viên.
  * Xem báo cáo thống kê xu hướng sự cố, thời gian xử lý trung bình và chỉ số hài lòng.
  * Quản trị hệ thống: Tạo mới, cập nhật thông tin và phân quyền tài khoản người dùng.