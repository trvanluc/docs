# Định Nghĩa Các Vai Trò Trong Hệ Thống (Actors & Roles)

Hệ thống UniSupport phân quyền người dùng dựa trên 3 vai trò chính (Role-Based Access Control - RBAC)[cite: 1]:

---

## 1. Sinh Viên (Student)
* **Mô tả:** Người dùng gửi yêu cầu hỗ trợ về các vấn đề học tập, hành chính, học phí hoặc kỹ thuật tại Aurora University[cite: 1].
* **Quyền hạn chính:**
  * Đăng nhập hệ thống bằng tài khoản cá nhân[cite: 1].
  * Tạo Ticket hỗ trợ mới (chọn phân loại, nhập mô tả, đính kèm file ảnh/PDF)[cite: 1].
  * Xem tiến độ, lịch sử cập nhật và người/đơn vị đang phụ trách xử lý Ticket của mình[cite: 1].
  * Bổ sung thông tin/giấy tờ khi nhân viên yêu cầu[cite: 1].
  * Xem kết quả giải quyết và thực hiện đánh giá mức độ hài lòng[cite: 1].

---

## 2. Nhân Viên (Staff)
* **Mô tả:** Nhân viên thuộc các phòng ban nghiệp vụ (Phòng Đào tạo, Phòng Công tác sinh viên, Phòng Tài chính,...)[cite: 1].
* **Quyền hạn chính:**
  * Đăng nhập hệ thống bằng tài khoản nhân viên[cite: 1].
  * Xem danh sách Ticket mới và Ticket được giao cho cá nhân/phòng ban[cite: 1].
  * Tiếp nhận, phân loại nhóm vấn đề và gắn mức độ ưu tiên[cite: 1].
  * Chuyển tiếp Ticket sang phòng ban/nhân viên khác nếu sai thẩm quyền[cite: 1].
  * Cập nhật trạng thái xử lý, gửi thông báo yêu cầu sinh viên bổ sung giấy tờ[cite: 1].
  * Ghi nhận kết quả xử lý và hoàn tất/đóng Ticket[cite: 1].

---

## 3. Quản Lý (Admin / Manager)
* **Mô tả:** Ban giám hiệu hoặc Trưởng/Phó các phòng ban quản lý vận hành hệ thống[cite: 1].
* **Quyền hạn chính:**
  * Đăng nhập bằng tài khoản quản lý[cite: 1].
  * Theo dõi Dashboard tổng quan về tình hình xử lý Ticket (mới, đang xử lý, quá hạn)[cite: 1].
  * Giám sát tải công việc và thời gian xử lý của từng phòng ban, nhân viên[cite: 1].
  * Xem báo cáo thống kê xu hướng sự cố, thời gian xử lý trung bình và chỉ số hài lòng[cite: 1].
  * Quản trị hệ thống: Tạo mới, cập nhật thông tin và phân quyền tài khoản người dùng[cite: 1].