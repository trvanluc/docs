# NFR-SEC - Bảo Mật Và Phân Quyền

## 1. Phạm Vi

UniSupport áp dụng các kiểm soát bảo mật cần thiết cho xác thực, phân quyền, dữ liệu Ticket, file đính kèm và Audit trong phạm vi dự án.

## 2. Yêu Cầu

- Người dùng đăng nhập bằng tài khoản và mật khẩu riêng.
- Hệ thống có ba nhóm người dùng chính: Sinh viên, Nhân viên và Quản lý.
- Sinh viên chỉ truy cập Ticket của chính mình.
- Nhân viên chỉ truy cập Ticket thuộc phạm vi phòng ban/quyền được cấp.
- Quản lý chỉ truy cập dữ liệu và chức năng trong phạm vi quản lý/quyền được cấp.
- File đính kèm chỉ được xem bởi người dùng có liên quan và có quyền phù hợp.
- Mật khẩu không được lưu hoặc hiển thị ở dạng có thể đọc trực tiếp.
- Các thao tác quan trọng phải được ghi nhận để tra soát theo `BR-AUD`.
- Nhật ký tra soát không được sửa/xóa bằng chức năng thông thường của ứng dụng.

## 3. Giới Hạn Phạm Vi

- Không bao gồm penetration testing chuyên sâu hoặc chứng nhận bảo mật quốc tế.
- Cơ chế phiên đăng nhập, thuật toán băm mật khẩu và lớp kiểm soát truy cập cụ thể được xác định trong thiết kế kiến trúc.

## 4. Dữ Liệu Nhạy Cảm

| Nhóm dữ liệu | Phạm vi | Biện pháp bảo vệ | Tham chiếu |
| :--- | :--- | :--- | :--- |
| Thông tin định danh | Họ tên, tên đăng nhập/mã định danh | Chỉ hiển thị trong phạm vi vai trò và phạm vi dữ liệu được cấp | Mục 2; ADR-002 |
| Nội dung xử lý | Nội dung Ticket, nội dung bổ sung, kết quả xử lý, nhận xét CSAT | Chỉ người sở hữu Ticket và người có quyền trong phạm vi xử lý/quản lý được truy cập | Mục 2; FR-STU-03; FR-STF-01 |
| File đính kèm | File minh chứng, file bổ sung, tài liệu kết quả | Kiểm tra quyền đối với Ticket trước mỗi lần xem/tải | `BR-FILE-01`; ADR-003 |
| Thông tin xác thực | Mật khẩu, phiên đăng nhập | Lưu bằng cơ chế một chiều; không ghi vào nhật ký ở dạng đọc được | Mục 2; ARC-05; NFR-OBS |

- Thời hạn lưu trữ dữ liệu được quản lý theo FR-MGT-04.
- Môi trường phát triển và kiểm thử chỉ sử dụng dữ liệu giả lập (`08-project/assumptions.md` mục 5).

## 5. Ghi Nhận Truy Cập Và Thay Đổi

| Loại sự kiện | Cơ chế | Tham chiếu |
| :--- | :--- | :--- |
| Thay đổi dữ liệu nghiệp vụ và cấu hình quan trọng | Ghi Audit: tác nhân, thời điểm, loại sự kiện, giá trị trước/sau | `BR-AUD-01`; FR-MGT-03 |
| Truy cập dữ liệu (xem, tải file) | Kiểm tra quyền tại mỗi yêu cầu; truy cập ngoài phạm vi bị từ chối | Mục 2; ADR-002 |
| Lỗi kỹ thuật | Ghi nhật ký kỹ thuật | NFR-OBS |

- Nhật ký chi tiết cho từng lần đăng nhập, xem hoặc tải dữ liệu không thuộc phạm vi hiện tại (`01-product/product-scope.md` mục 2).
- Yêu cầu bổ sung nhật ký truy cập chi tiết được xử lý theo quy trình quản lý thay đổi.

## 6. Nghiệm Thu

- Người dùng không thể truy cập Ticket/file ngoài phạm vi quyền.
- Tài khoản bị khóa không đăng nhập được.
- Các sự kiện Audit bắt buộc được ghi nhận đúng tác nhân, thời điểm và nội dung thay đổi cần thiết.
