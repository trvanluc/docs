# Đối chiếu giờ Resources UniSupport

Nguồn số giờ: **Phân bổ Resources.xlsx**, sheet **Resource**, do người dùng cung cấp tại `C:/Users/ACER/Downloads/Phân bổ Resources.xlsx`. Tài liệu này sao lại giờ và tên công việc để tra cứu; không thay thế workbook nguồn, không phải bảng estimate mới và không xác nhận thêm chức năng.

## Bảng giờ theo dòng và vai trò

| Mã dòng | Dòng Resource | Tên công việc nguồn | BA | UI/UX | TL | FE1 | FE2 | BE1 | BE2 | QA | Cơ sở | Dự phòng | Kế hoạch | Đối chiếu phạm vi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-STU-01 | 3 | Tra cứu hướng dẫn & FAQ | 3 | 3 | 0 | 4 | 0 | 0 | 0 | 4 | 14 | 0 | 14 | Chưa có FR FAQ được chốt; giữ dòng nguồn, không thay mã đăng nhập |
| R-STU-02 | 4 | Tạo & gửi yêu cầu hỗ trợ | 5 | 5 | 1 | 10 | 1 | 6 | 1 | 5 | 34 | 3 | 37 | FR-STU-02 |
| R-STU-03 | 5 | Xem & theo dõi yêu cầu | 4 | 3 | 1 | 8 | 3 | 5 | 3 | 5 | 32 | 1 | 33 | FR-STU-03 |
| R-STU-04 | 6 | Nhận thông báo trạng thái | 3 | 1 | 0 | 4 | 0 | 4 | 4 | 3 | 19 | 0 | 19 | FR-STU-03; thông báo trạng thái đã có |
| R-STU-05 | 7 | Bổ sung thông tin & phản hồi | 3 | 1 | 0 | 5 | 3 | 5 | 3 | 5 | 25 | 0 | 25 | FR-STU-03; FR-STU-04 (đối chiếu phần phản hồi/đánh giá; chưa có phân bổ riêng) |
| R-STF-01 | 12 | Tiếp nhận, tìm kiếm & lọc yêu cầu | 3 | 3 | 1 | 4 | 5 | 8 | 3 | 6 | 33 | 0 | 33 | FR-STF-02; Queue phòng ban đã có |
| R-STF-02 | 13 | Phân loại & phân công xử lý | 4 | 0 | 3 | 4 | 3 | 9 | 5 | 9 | 37 | 1 | 38 | FR-STF-02; quyền phân công MANAGER/ADMIN đã có |
| R-STF-03 | 14 | Quản lý ưu tiên & thời hạn | 4 | 0 | 4 | 3 | 3 | 6 | 3 | 3 | 26 | 3 | 29 | FR-STF-02; FR-MNG-02 |
| R-STF-04 | 15 | Xử lý & cập nhật yêu cầu | 4 | 1 | 1 | 4 | 4 | 9 | 4 | 9 | 36 | 3 | 39 | FR-STF-04 |
| R-STF-05 | 16 | Chuyển xử lý, Escalation & hoàn tất | 3 | 0 | 3 | 3 | 3 | 8 | 4 | 5 | 29 | 3 | 32 | FR-STF-03; FR-STF-05 |
| R-STF-06 | 17 | Đóng & mở lại yêu cầu | 3 | 0 | 1 | 3 | 3 | 8 | 3 | 5 | 26 | 0 | 26 | FR-STF-05; FR-STU-04; không chốt phần mở lại xử lý |
| R-ADM-01 | 22 | Quản lý tài khoản, vai trò & RBAC | 5 | 3 | 6 | 3 | 8 | 13 | 9 | 13 | 60 | 4 | 64 | FR-MNG-04; FR-STU-01, FR-STF-01, FR-MNG-01 dùng chung |
| R-ADM-02 | 23 | Quản lý phòng ban & danh mục | 4 | 1 | 3 | 0 | 4 | 5 | 5 | 4 | 26 | 0 | 26 | Danh mục ADMIN quản lý tại Actors & Roles / Terminology; không thêm FR |
| R-ADM-03 | 24 | Kiểm soát quyền truy cập & Audit Trail | 4 | 0 | 4 | 1 | 4 | 9 | 5 | 9 | 36 | 4 | 40 | FR-MNG-04; FR-MNG-05; quyền dữ liệu đã có |
| R-ADM-04 | 25 | Quản lý thời hạn lưu trữ | 3 | 0 | 1 | 0 | 0 | 4 | 4 | 3 | 15 | 0 | 15 | Giữ giờ nguồn; chưa có FR nghiệp vụ riêng về cấu hình/dọn dẹp lưu trữ |
| R-ADM-05 | 26 | Dashboard & thống kê quản trị | 4 | 3 | 1 | 0 | 9 | 3 | 9 | 4 | 33 | 0 | 33 | FR-MNG-02 |
| R-ADM-06 | 27 | Báo cáo, mức độ hài lòng & xuất dữ liệu | 4 | 3 | 1 | 0 | 8 | 5 | 10 | 6 | 37 | 0 | 37 | FR-MNG-03; sử dụng dữ liệu FR-STU-04 |
| Tổng | — | Mỗi dòng tính một lần | 63 | 27 | 31 | 56 | 61 | 107 | 75 | 98 | 518 | 22 | 540 | Không cộng lại khi nhiều FR dùng chung |

## Tổng công sức

| Nhóm | Cơ sở | Dự phòng | Kế hoạch |
| --- | ---: | ---: | ---: |
| Student (Resource!3:7) | 124 | 4 | 128 |
| Staff (Resource!12:17) | 187 | 10 | 197 |
| Admin/Management (Resource!22:27) | 207 | 8 | 215 |
| Chức năng | 518 | 22 | 540 |
| PM (Resource!35) | 70 | 0 | 70 |
| DevOps (Resource!36) | 30 | 0 | 30 |
| Toàn dự án | 618 | 22 | 640 |

Giờ vai trò toàn dự án: PM 70; BA 63; UI/UX 27; TL 31; FE1 56; FE2 61; BE1 107; BE2 75; QA 98; DevOps 30. Dự phòng 22 giờ giữ theo dòng nguồn và chưa tự gán cho người. Ô giờ BE2 ở sheet chi phí đang trống; giờ BE2 lấy từ Resource là 75, không coi ô trống là 0.

Giờ bao gồm các công việc thuộc dự án trong bảng nguồn. Không cộng thêm giờ triển khai, tích hợp, QA/UAT hoặc bảo hành ngoài tổng 640 khi tài liệu nguồn chưa phân bổ; lịch có giai đoạn nào không có nghĩa được thêm giờ cho giai đoạn đó. Bản sửa không tính lại đơn giá, lương, bảo hiểm hoặc lợi nhuận.

## Giới hạn phạm vi và giờ nguồn

- 14 mã FR trong M01–M03 là mã yêu cầu sản phẩm. 17 dòng Excel dùng mã R-STU/R-STF/R-ADM để đối chiếu công sức; không đổi các dòng đó thành FR mới.
- Một dòng công sức có thể liên quan nhiều FR. Chỉ tính dòng đó một lần; không tự tách hoặc chia lại giờ cho FR, vai trò hay tuần.
- FAQ có 14 giờ ở dòng nguồn nhưng chưa có đặc tả FR được chốt. Giữ giờ; không tự thêm màn hình, tìm kiếm FAQ hay đổi FR-STU-01 từ đăng nhập thành FAQ.
- Dòng “Đóng & mở lại yêu cầu” giữ 26 giờ; bản PRD/vòng đời hiện có không hỗ trợ mở lại quá trình xử lý Ticket đã CLOSED. Mở lại trang chi tiết là thao tác xem lại.
- Phản hồi/CSAT đã có tại FR-STU-04. Ghép với R-STU-05 chỉ là đối chiếu; chưa xác nhận chia effort riêng và không cộng thêm giờ.
- Dòng danh mục và lưu trữ được giữ nguyên giờ. Quyền cấu hình danh mục đã có trong tài liệu; không tự tạo FR, UI dọn dẹp/archiving hoặc chính sách lưu trữ mới.
- Tên “Escalation” trong dòng nguồn không đủ để chốt thêm luồng báo cáo vượt cấp. Bản sửa giữ luồng chuyển phòng ban/hoàn tất đã có.
- M04/M05 là tài liệu hỗ trợ kỹ thuật hiện tại, không phải hai phân hệ nghiệp vụ có effort bổ sung. Các mã FR-NTF/FR-SEC trong đó không được cộng vào 14 FR sản phẩm.
