# Kịch Bản UAT Chính

Tài liệu này liệt kê các kịch bản nghiệm thu đại diện cho phạm vi chức năng của UniSupport. Các điều kiện kiểm tra chi tiết được kế thừa từ tiêu chí nghiệm thu của từng FR.

## 1. M01 - Sinh Viên

| Mã | Kịch bản | Kết quả chính |
| :--- | :--- | :--- |
| TS-STU-01 | Tra cứu FAQ theo Nhóm vấn đề | Hiển thị nội dung hướng dẫn phù hợp và cho phép chuyển sang tạo Ticket khi cần. |
| TS-STU-02 | Tạo Ticket với Category, nội dung và file hợp lệ | Tạo đúng một Ticket `NEW`, mã duy nhất, đúng phòng ban và mức `MEDIUM`. |
| TS-STU-03 | Xem danh sách/chi tiết Ticket của mình | Chỉ hiển thị Ticket thuộc sinh viên và đúng lịch sử được phép xem. |
| TS-STU-04 | Nhận và mở thông báo Ticket | Thông báo đúng người, đúng Ticket và trạng thái đọc/chưa đọc. |
| TS-STU-05 | Bổ sung thông tin khi `WAITING_STUDENT` | Ticket quay về `IN_PROGRESS`, thời hạn tiếp tục từ phần còn lại. |
| TS-STU-06 | Chấp nhận kết quả hoặc yêu cầu mở lại | Chấp nhận → `CLOSED`; mở lại hợp lệ → `IN_PROGRESS`. |
| TS-STU-07 | Đánh giá sau khi Ticket đóng | Chỉ nhận 1 đánh giá 1–5 sao trong 07 ngày theo lịch. |

## 2. M02 - Nhân Viên

| Mã | Kịch bản | Kết quả chính |
| :--- | :--- | :--- |
| TS-STF-01 | Xem hàng chờ, tìm kiếm và lọc | Chỉ hiển thị Ticket trong phạm vi quyền và đúng bộ lọc. |
| TS-STF-02 | Tiếp nhận/phân công Ticket | Tối đa một người phụ trách; Ticket `NEW` chuyển `IN_PROGRESS`. |
| TS-STF-03 | Điều chỉnh mức độ ưu tiên | Deadline tính lại theo Business Rules, không reset đồng hồ. |
| TS-STF-04 | Yêu cầu sinh viên bổ sung | `IN_PROGRESS → WAITING_STUDENT`, tạm dừng thời hạn. |
| TS-STF-05 | Transfer sang phòng ban khác | Category + phòng ban đổi nhất quán, assignee cũ được gỡ, state được giữ. |
| TS-STF-06 | Escalation tới Quản lý | Không đổi Category/phòng ban/assignee/state; đúng người nhận được thông báo. |
| TS-STF-07 | Ghi nhận kết quả | `IN_PROGRESS → RESOLVED`, sinh viên xem được kết quả. |
| TS-STF-08 | Tiếp tục xử lý Ticket được mở lại | Giữ assignee cũ nếu hợp lệ; nếu không thì về hàng chờ phòng ban. |

## 3. M03 - Quản Lý

| Mã | Kịch bản | Kết quả chính |
| :--- | :--- | :--- |
| TS-MGT-01 | Tạo/cập nhật/khóa tài khoản | Đúng role/phạm vi; không làm mất tài khoản quản trị cuối cùng. |
| TS-MGT-02 | Quản lý phòng ban và Category | Category hoạt động có đúng một phòng ban; không vô hiệu hóa phòng ban còn Ticket cần xử lý/mở lại. |
| TS-MGT-03 | Xem nhật ký tra soát | Đúng phạm vi; bản ghi không sửa/xóa qua chức năng ứng dụng. |
| TS-MGT-04 | Cấu hình thời hạn lưu trữ | Chỉ đánh dấu dữ liệu đến hạn; không tự động xóa/ẩn danh/di chuyển. |
| TS-MGT-05 | Dashboard | Số liệu trạng thái, gần quá hạn, quá hạn và workload đúng Business Rules. |
| TS-MGT-06 | Báo cáo/CSAT/xuất dữ liệu | Đúng công thức thời gian xử lý, CSAT và phạm vi quyền. |

## 4. Năng Lực Dùng Chung

- Đăng nhập bằng tài khoản hợp lệ; tài khoản bị khóa không truy cập được.
- Sinh viên/Staff/Management không truy cập dữ liệu ngoài phạm vi.
- File đính kèm chỉ người liên quan có quyền mới truy cập được.
- Các thao tác quan trọng sinh bản ghi Audit tương ứng.
