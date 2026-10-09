# Phạm vi sản phẩm và giới hạn Resources

## Yêu cầu sản phẩm đã chốt

Phạm vi PRD gồm **14 mã FR**: 4 Student, 5 Staff và 5 Management. Bảng Resources gồm **17 dòng công việc**, không phải 17 FR. Bản hiệu chỉnh giữ các mã và ý nghĩa hiện có; không đổi FR-STU-01 từ đăng nhập thành FAQ hoặc FR-STU-04 từ xem kết quả/đánh giá thành thông báo.

| Mã FR | Yêu cầu sản phẩm | Tài liệu chi tiết |
| --- | --- | --- |
| FR-STU-01 | Đăng nhập tài khoản sinh viên | [M01 PRD](../03-modules/M01-student-portal/prd.md) |
| FR-STU-02 | Gửi yêu cầu hỗ trợ (Tạo Ticket) | [M01 PRD](../03-modules/M01-student-portal/prd.md) |
| FR-STU-03 | Theo dõi tiến độ & Bổ sung thông tin/giấy tờ | [M01 PRD](../03-modules/M01-student-portal/prd.md) |
| FR-STU-04 | Xem kết quả giải quyết & Đánh giá mức độ hài lòng | [M01 PRD](../03-modules/M01-student-portal/prd.md) |
| FR-STF-01 | Nhân viên đăng nhập hệ thống | [M02 PRD](../03-modules/M02-staff-operations/prd.md) |
| FR-STF-02 | Tiếp nhận và phân loại yêu cầu (Claim & Triage) | [M02 PRD](../03-modules/M02-staff-operations/prd.md) |
| FR-STF-03 | Chuyển yêu cầu sang đúng phòng ban | [M02 PRD](../03-modules/M02-staff-operations/prd.md) |
| FR-STF-04 | Cập nhật tiến độ & Yêu cầu bổ sung thông tin (Request Supplement) | [M02 PRD](../03-modules/M02-staff-operations/prd.md) |
| FR-STF-05 | Ghi kết quả và hoàn tất xử lý yêu cầu | [M02 PRD](../03-modules/M02-staff-operations/prd.md) |
| FR-MNG-01 | Quản lý đăng nhập & Xác thực phân quyền | [M03 PRD](../03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-02 | Nắm tổng quan tình hình & Giám sát tiến độ (Real-time Dashboard & SLA Supervision) | [M03 PRD](../03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-03 | Xem báo cáo thống kê & Xuất dữ liệu (Analytics & Data Export) | [M03 PRD](../03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-04 | Quản trị người dùng & Phân quyền (User Management & RBAC) | [M03 PRD](../03-modules/M03-management-dashboard/prd.md) |
| FR-MNG-05 | Kiểm soát quyền truy cập & Nhật ký hệ thống (Audit Trail) | [M03 PRD](../03-modules/M03-management-dashboard/prd.md) |

## Giới hạn nghiệp vụ

Tài khoản do ADMIN cấp; Student chỉ thao tác Ticket của mình; Staff xử lý theo phòng ban; Manager giám sát/phân công phòng ban; Admin quản trị toàn trường theo quyền gốc. Nhóm vấn đề lấy từ danh mục hệ thống và gắn phòng ban mặc định.

Theo PRD: tiêu đề 10–150 ký tự, nội dung 20–2000 ký tự; tối đa 5 tệp sinh viên và 3 tệp kết quả nhân viên, mỗi tệp 5MB, PDF/PNG/JPG/JPEG. Cần bổ sung dùng NEED_MORE_INFO; sau bổ sung quay lại IN_PROGRESS. Hoàn tất xử lý hiển thị RESOLVED; đóng hiển thị CLOSED. CSAT 1–5 sao, nhận xét tùy chọn tối đa 500 ký tự, một lần/Ticket.

## Giới hạn phạm vi và giờ nguồn

- 14 mã FR trong M01–M03 là mã yêu cầu sản phẩm. 17 dòng Excel dùng mã R-STU/R-STF/R-ADM để đối chiếu công sức; không đổi các dòng đó thành FR mới.
- Một dòng công sức có thể liên quan nhiều FR. Chỉ tính dòng đó một lần; không tự tách hoặc chia lại giờ cho FR, vai trò hay tuần.
- FAQ có 14 giờ ở dòng nguồn nhưng chưa có đặc tả FR được chốt. Giữ giờ; không tự thêm màn hình, tìm kiếm FAQ hay đổi FR-STU-01 từ đăng nhập thành FAQ.
- Dòng “Đóng & mở lại yêu cầu” giữ 26 giờ; bản PRD/vòng đời hiện có không hỗ trợ mở lại quá trình xử lý Ticket đã CLOSED. Mở lại trang chi tiết là thao tác xem lại.
- Phản hồi/CSAT đã có tại FR-STU-04. Ghép với R-STU-05 chỉ là đối chiếu; chưa xác nhận chia effort riêng và không cộng thêm giờ.
- Dòng danh mục và lưu trữ được giữ nguyên giờ. Quyền cấu hình danh mục đã có trong tài liệu; không tự tạo FR, UI dọn dẹp/archiving hoặc chính sách lưu trữ mới.
- Tên “Escalation” trong dòng nguồn không đủ để chốt thêm luồng báo cáo vượt cấp. Bản sửa giữ luồng chuyển phòng ban/hoàn tất đã có.
- M04/M05 là tài liệu hỗ trợ kỹ thuật hiện tại, không phải hai phân hệ nghiệp vụ có effort bổ sung. Các mã FR-NTF/FR-SEC trong đó không được cộng vào 14 FR sản phẩm.

## Giới hạn công sức

Nguồn: [bảng đối chiếu Resources](../Phan_bo_Resources_Antigravity.md). Student 128 giờ; Staff 197 giờ; Admin/Management 215 giờ; PM 70 giờ; DevOps 30 giờ. Tổng **618 giờ cơ sở + 22 giờ dự phòng = 640 giờ**. Giữ nguyên mỗi giờ theo dòng/role, không phân lại theo FR hoặc giai đoạn.

## Các ràng buộc dự án giữ theo hồ sơ hiện có

Ứng dụng Web responsive cho khoảng 3.000 sinh viên; không phát triển Mobile App độc lập, không mở rộng tích hợp ngoài phạm vi. Lịch 14 tuần phát triển và 10 ngày làm việc UAT sau bàn giao, bảo hành 30 ngày giữ như tài liệu hiện tại. Bản sửa không thay giá hợp đồng, đơn giá nhân sự hoặc phương án triển khai.
