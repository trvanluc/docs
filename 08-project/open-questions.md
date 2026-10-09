# Các đầu vào và sai lệch cần theo dõi

## Đầu vào từ hồ sơ hiện có

| Mục | Cần theo dõi | Trạng thái trong tài liệu |
| --- | --- | --- |
| Hạ tầng nhà trường | Thông tin Server, tên miền, môi trường được cung cấp theo hồ sơ triển khai hiện có | Chưa có bằng chứng cung cấp trong bộ file này; không đổi giải pháp |
| Dữ liệu tài khoản ban đầu | Danh sách người dùng, vai trò và phòng ban để ADMIN cấp tài khoản theo FR-MNG-04 | Không tự thêm import Excel hoặc tự đăng ký |
| Danh mục đầu vào | Danh sách nhóm vấn đề và phòng ban mặc định do ADMIN quản lý | Quyền đã có; chưa tự đặt thêm danh mục hoặc màn hình |
| Lý do chuyển phòng | FR-STF-03 đã quy định bắt buộc 10–500 ký tự, không toàn khoảng trắng | Đã có trong PRD; không còn là câu hỏi tùy chọn/không bắt buộc |
| Phạm vi dòng FAQ/mở lại/lưu trữ | Xem [giới hạn Resources](../Phan_bo_Resources_Antigravity.md) | Giữ giờ, không tự tạo FR hay ca nghiệm thu mới |
| Sai lệch tài liệu kỹ thuật | Xem [prd-review-notes.md](./prd-review-notes.md) | Ghi nhận để đối chiếu, không tự sửa triển khai |

## Nguyên tắc cập nhật

Ghi quyết định dựa trên bằng chứng nguồn thực tế, không coi dòng công sức hoặc nội dung do công cụ tạo là phê duyệt thêm chức năng. Giữ 14 FR và 640 giờ; không yêu cầu xác nhận lại những quy tắc đã được PRD quy định rõ.
