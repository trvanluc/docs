# Actors và role model

## 1. Role model thống nhất

Proposal xác định 3 nhóm người dùng nghiệp vụ. Toàn bộ PRD/spec dùng thống nhất 3 role baseline:

| Role | Tên tiếng Việt | Mô tả | Trạng thái |
| :--- | :--- | :--- | :--- |
| `STUDENT` | Sinh viên | Người tạo Ticket, theo dõi tiến độ, bổ sung thông tin, xem kết quả và đánh giá hài lòng. | Baseline |
| `STAFF` | Nhân viên | Người tiếp nhận, phân loại, xử lý, chuyển xử lý, yêu cầu bổ sung, ghi nhận kết quả và đóng Ticket. | Baseline |
| `MANAGEMENT` | Quản lý | Người xem dashboard/báo cáo và thực hiện quản trị account/permission theo quyền được cấp. | Baseline |

`ADMIN` không được dùng như role baseline riêng trong PRD. Nếu cần phân biệt người quản trị kỹ thuật khi triển khai, Architecture có thể mô tả đó là permission/sub-role vận hành thuộc `MANAGEMENT`.

## 2. Quyền nghiệp vụ chính

| Chức năng / dữ liệu | STUDENT | STAFF | MANAGEMENT |
| :--- | :---: | :---: | :---: |
| Đăng nhập hệ thống | Có | Có | Có |
| Tạo Ticket | Có | Không | Không |
| Xem Ticket do mình tạo | Có | Không mặc định | Theo quyền quản lý/tra soát |
| Xem Ticket thuộc phòng ban/phạm vi xử lý | Không | Có | Có |
| Tiếp nhận/phân công/xử lý Ticket | Không | Có | Có nếu được cấp permission xử lý |
| Yêu cầu bổ sung thông tin | Không | Có | Có nếu được cấp permission xử lý |
| Bổ sung thông tin cho Ticket của mình | Có | Không | Không |
| Xem kết quả và đánh giá | Có | Không | Xem tổng hợp/báo cáo |
| Dashboard/báo cáo | Không | Không | Có |
| Tạo/chỉnh sửa account và gán quyền | Không | Không | Có nếu được cấp permission quản trị |
| Xem file đính kèm | Chỉ file thuộc Ticket của mình | Chỉ file thuộc Ticket trong phạm vi xử lý | Theo phạm vi quản lý/tra soát |

## 3. Nguyên tắc phân quyền

- Quyền hiển thị trên UI không thay thế kiểm tra quyền ở backend.
- Student chỉ thao tác với Ticket của chính mình.
- Staff chỉ xử lý Ticket thuộc phòng ban/phạm vi được giao.
- Management chỉ xem hoặc quản trị dữ liệu trong phạm vi được cấp quyền.
- Các thao tác quan trọng phải được lưu lịch sử để phục vụ tra soát.
