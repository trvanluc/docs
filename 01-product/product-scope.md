# Phạm Vi Sản Phẩm & Các Giả Định Dự Án

## 1. Tóm Tắt Phạm Vi Chức Năng
Sản phẩm UniSupport bao gồm 3 phân hệ chức năng tương ứng với 3 vai trò người dùng[cite: 1]:

| Phân hệ | Chức năng cốt lõi |
| :--- | :--- |
| **Module 1: Sinh viên** | Đăng nhập; Tạo Ticket (chọn nhóm, mô tả, đính kèm file); Theo dõi tiến độ qua mã Ticket; Bổ sung giấy tờ; Nhận kết quả & Đánh giá mức độ hài lòng[cite: 1]. |
| **Module 2: Nhân viên** | Đăng nhập; Tiếp nhận & Phân loại Ticket; Chuyển tiếp phòng ban; Cập nhật tiến độ; Yêu cầu bổ sung thông tin; Ghi kết quả & Đóng Ticket[cite: 1]. |
| **Module 3: Quản lý** | Đăng nhập; Dashboard tổng quan; Báo cáo thống kê (xu hướng, thời gian xử lý, đánh giá); Quản trị tài khoản & Phân quyền vai trò[cite: 1]. |

---

## 2. Các Giả Định Triển Khai (Assumptions)
Đội ngũ phát triển và Aurora University thống nhất các giả định nền tảng sau[cite: 1]:

1. **Quy mô hệ thống:** Phục vụ tối đa khoảng **3.000 sinh viên**, kiến trúc hệ thống không thiết kế cho tải lớn vượt mốc này[cite: 1].
2. **Hình thức sản phẩm:** Hệ thống được triển khai dưới dạng **Web Application**, hỗ trợ giao diện Responsive trên Web Desktop và Mobile Browser[cite: 1].
3. **Đa ngôn ngữ:** Hệ thống hỗ trợ giao diện cơ bản bằng Tiếng Việt và Tiếng Anh[cite: 1].
4. **Hạ tầng & Tên miền:** Khách hàng (Aurora University) chịu trách nhiệm cung cấp máy chủ (Server) và Tên miền (Domain) đáp ứng tiêu chuẩn triển khai[cite: 1].
5. **Tiến độ phản hồi:** Thời gian triển khai 14 tuần (70 ngày làm việc) không bao gồm thời gian chờ phản hồi, phê duyệt hoặc nghiệm thu chậm trễ từ phía Client[cite: 1].
6. **Bảo mật & Tích hợp:** Không yêu cầu tích hợp hệ thống bên thứ ba ngoài danh mục thống nhất và không yêu cầu chứng nhận bảo mật chuyên sâu[cite: 1].