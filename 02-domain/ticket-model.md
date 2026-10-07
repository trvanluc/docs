# Mô hình nghiệp vụ Ticket

Tài liệu này mô tả Ticket ở mức domain/business. Kiểu dữ liệu, khóa ngoại, index và bảng vật lý nằm trong `07-architecture/data-model.md`.

## 1. Thuộc tính Ticket

| Thuộc tính nghiệp vụ | Mô tả | Bắt buộc | Trạng thái |
| :--- | :--- | :---: | :--- |
| Ticket ID | Mã định danh hiển thị cho người dùng. | Có | Baseline |
| Student owner | Sinh viên tạo Ticket. | Có | Baseline |
| Description | Nội dung mô tả yêu cầu của sinh viên. | Có | Baseline |
| Category | Nhóm vấn đề sinh viên chọn hoặc Staff điều chỉnh khi phân loại. | Có | Baseline |
| Department | Phòng ban/đơn vị đang chịu trách nhiệm xử lý. | Có sau khi Ticket được đưa vào queue | Derived/TBD |
| Assignee | Staff đang phụ trách Ticket. Có thể trống khi Ticket mới hoặc vừa transfer. | Không | Derived |
| Status | Trạng thái hiện tại của Ticket. | Có | Baseline |
| Priority | Mức ưu tiên/hạn theo dõi xử lý nếu được áp dụng. | Không/TBD | Baseline/TBD |
| Attachments | Ảnh/PDF do Student hoặc Staff đính kèm. | Không | Baseline |
| Resolution | Kết quả xử lý do Staff ghi nhận. | Có trước khi đóng | Baseline |
| History | Lịch sử cập nhật, bổ sung, chuyển xử lý và kết quả. | Có | Baseline |
| CSAT rating | Đánh giá hài lòng sau khi Ticket hoàn tất. | Không | Baseline/Proposed |
| Created/Updated time | Mốc tạo và cập nhật gần nhất. | Có | Derived |
| Deadline/SLA data | Dữ liệu phục vụ theo dõi sắp quá hạn/quá hạn. | TBD | Baseline/TBD |
| Title | Tiêu đề ngắn của Ticket. Proposal chưa nêu trực tiếp nhưng hữu ích cho danh sách Ticket. | Không/TBD | Derived/TBD |

## 2. Trạng thái Ticket baseline

| Status | Ý nghĩa |
| :--- | :--- |
| `NEW` | Ticket đã được tạo và đang chờ tiếp nhận/phân công. |
| `IN_PROGRESS` | Ticket đang được Staff xử lý. |
| `WAITING_STUDENT` | Staff đã yêu cầu bổ sung và đang chờ Student phản hồi. |
| `RESOLVED` | Staff đã ghi nhận kết quả xử lý, chờ đóng/hoàn tất quy trình. |
| `CLOSED` | Ticket đã đóng, Student có thể xem kết quả và đánh giá hài lòng theo rule đã xác nhận. |

Các trạng thái `CANCELLED`, `REOPENED` hoặc auto-close không thuộc baseline proposal; nếu cần sẽ ghi Proposed/TBD.

## 3. Attachment policy

Proposal chỉ xác nhận sinh viên có thể đính kèm **ảnh/PDF**. Các giới hạn như dung lượng tối đa, số lượng file, MIME type chi tiết và cơ chế quét file là **TBD/Proposed Engineering Target**.

## 4. Rating policy

Proposal xác nhận Student có thể đánh giá mức độ hài lòng sau khi yêu cầu hoàn tất. Thang điểm 1-5 sao là đề xuất phổ biến và được ghi **Proposed** cho đến khi được xác nhận.
