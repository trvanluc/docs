# Vai trò và phạm vi quyền UniSupport

## Bốn vai trò đã có trong PRD

- **STUDENT:** Sinh viên được nhà trường/ADMIN cấp tài khoản; tạo, theo dõi, bổ sung theo yêu cầu và đánh giá chính Ticket của mình. Không tự đăng ký tài khoản.
- **STAFF:** Nhân viên được ADMIN cấp tài khoản và gán phòng ban; xem hàng đợi của phòng ban và thực hiện các thao tác theo quyền trên Ticket/người phụ trách.
- **MANAGER:** Quản lý phòng ban; giám sát, báo cáo và phân công trong phòng ban mình. Không quản trị tài khoản toàn hệ thống hoặc xem dữ liệu phòng ban khác.
- **ADMIN:** Quản trị viên; cấp tài khoản, gán vai trò/phòng ban, khóa/mở khóa, quản lý danh mục, tra soát và xem báo cáo toàn trường theo quyền gốc.

Đây là phân biệt bốn vai trò đã có trong FR-MNG-01/04, không tạo thêm cấp phân quyền. Các cổng nghiệp vụ vẫn gồm Student, Staff và Management.

## Ma trận quyền nghiệp vụ

| Thao tác | STUDENT | STAFF | MANAGER | ADMIN |
| --- | --- | --- | --- | --- |
| Đăng nhập | Có | Có | Có | Có |
| Tạo Ticket cá nhân | Có | Không | Không | Không |
| Xem/bổ sung/đánh giá Ticket cá nhân | Chỉ Ticket của mình | Không | Không | Không |
| Xem Queue và tiếp nhận Ticket | Không | Trong phòng ban | Trong phòng ban | Toàn trường theo quyền đã có |
| Chuyển phòng, yêu cầu bổ sung, ghi kết quả | Không | Theo quyền Ticket/người phụ trách | Trong phòng ban theo quyền đã có | Theo quyền đã có |
| Phân công/thu hồi/phân công lại | Không | Không | Trong phòng ban | Theo quyền đã có |
| Dashboard/báo cáo | Không | Không | Phòng ban phụ trách | Toàn trường |
| Tạo/sửa/khóa/mở khóa tài khoản và gán quyền | Không | Không | Không | Có |
| Quản lý danh mục nhóm vấn đề | Không | Không | Không | Quyền đã có trong tài liệu gốc |
| Xem Audit Log hệ thống | Không | Không | Không | Có; chỉ đọc |

## Các điểm không được nhầm

- STAFF tự nhận Ticket (Claim); MANAGER/ADMIN phân công cho người khác (Assign/Reassign). Chuyển phòng ban là thao tác khác, đặc tả tại FR-STF-03.
- Không coi chức danh “Ban Giám hiệu” là tự động có ADMIN: phạm vi dữ liệu phụ thuộc vai trò đã được cấp.
- Sau chuyển phòng ban, quyền xử lý thuộc đơn vị tiếp nhận theo PRD; không cấp thêm quyền xem/sửa ngoài phòng ban cho STAFF cũ.
- Danh mục nhóm vấn đề gắn phòng ban mặc định. Quyền ADMIN đã có không đồng nghĩa lần sửa này mở thêm FR hoặc màn hình quản trị mới.
