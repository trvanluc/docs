# 03 - Functional Modules

Thư mục `03-modules` đặc tả yêu cầu chức năng của **UniSupport** theo ba phân hệ nghiệp vụ chính. Nội dung tại đây được xây dựng trên các quy tắc và mô hình nghiệp vụ đã xác lập trong `02-domain`.

## Các Phân Hệ Nghiệp Vụ Chính

| Phân hệ | Phạm vi |
| :--- | :--- |
| [M01 - Student Portal](./M01-student-portal/) | Tra cứu hướng dẫn, tạo Ticket, theo dõi tiến độ, bổ sung thông tin, nhận kết quả và đánh giá mức độ hài lòng. |
| [M02 - Staff Operations](./M02-staff-operations/) | Tiếp nhận, phân loại, phân công, xử lý, chuyển xử lý/chuyển cấp, yêu cầu bổ sung và ghi nhận kết quả Ticket. |
| [M03 - Management Dashboard](./M03-management-dashboard/) | Giám sát hoạt động hỗ trợ, Dashboard/báo cáo và các chức năng quản trị được phân quyền. |

## Năng Lực Dùng Chung

Một số chức năng được áp dụng xuyên suốt các phân hệ và không được xem là phân hệ nghiệp vụ độc lập:

- **Notification:** tạo và hiển thị thông báo khi phát sinh các sự kiện Ticket liên quan.
- **Authentication, RBAC & Security:** xác thực, kiểm soát quyền truy cập và bảo vệ dữ liệu theo vai trò/phạm vi trách nhiệm.

Các năng lực dùng chung được đặc tả tại Domain, Workflows, yêu cầu phi chức năng và thiết kế hệ thống, đồng thời được áp dụng xuyên suốt M01, M02 và M03.

## Cấu Trúc Đặc Tả

Mỗi phân hệ gồm:

- `README.md`: phạm vi, đối tượng sử dụng, danh sách yêu cầu chức năng, luồng nghiệp vụ chính và quan hệ với các phần còn lại.
- `prd.md`: mỗi FR gồm dòng **Priority** (kèm mốc giao), rồi 9 mục: 1. Mô tả & phạm vi, 2. Actors & điều kiện tiên quyết, 3. Validation, 4. Luồng xử lý chính, 5. Luồng ngoại lệ (lỗi và từ chối), 6. Quy tắc nghiệp vụ, 7. Tiêu chí nghiệm thu (AC), 8. Luồng thay thế (Alternative Flows), 9. Ví dụ Edge Case. Mục 8–9 được thêm sau mục 7 để giữ nguyên số mục mà các issue GitHub đang dẫn tới.

## Quy Ước Tiêu Chí Nghiệm Thu (AC)

- **Mã AC** có dạng `FR-XXX-nn/AC-nn`, ví dụ `FR-STU-02/AC-06`, duy nhất trong toàn repo. Mọi nơi dẫn tới AC (kịch bản test, task, ma trận truy vết, chỉ tiêu thành công) ghi đủ mã này.
- **Mỗi luồng ngoại lệ (mục 5) và mỗi quy tắc nghiệp vụ (mục 6) của FR có ít nhất một AC kiểm nó.** Lỗi do không có quyền và lỗi do dữ liệu đã bị người khác thay đổi được viết AC riêng trong từng FR.
- **AC dạng "bị từ chối"** luôn nêu được điều tester quan sát được: (1) thông báo nêu lý do (trường nào sai, không có quyền, hay trạng thái đã đổi), (2) dữ liệu giữ nguyên (không tạo/sửa bản ghi, trạng thái không đổi). Với thao tác không có quyền: người dùng không thấy thao tác; nếu gửi trực tiếp tới hệ thống thì nhận thông báo "không có quyền thực hiện".
- Kịch bản test kiểm các AC nằm ở [06-acceptance/test-scenarios.md](../06-acceptance/test-scenarios.md).

## Mức Ưu Tiên FR

Priority của FR là nơi gốc; dòng **Priority** trong parent task trên GitHub lấy theo PRD. Liên kết chỉ ghi một phía: parent task ghi mã FR, PRD không ghi ngược số issue. Một FR có thể có task con ở mức thấp hơn, ví dụ phần xuất CSV của FR-MGT-06.

| Mức | Tiêu chí | Khi thiếu thời gian hoặc có CR |
| --- | --- | --- |
| **Cao** | Thiếu thì luồng Ticket chính (tạo → tiếp nhận → xử lý → trả kết quả → đóng) không chạy được, hoặc vi phạm phân quyền/bảo mật, hoặc là cam kết trực tiếp trong Proposal (Dashboard, báo cáo). | Giữ nguyên; dùng dự phòng `Q-11` trước. |
| **Trung bình** | Hỗ trợ trải nghiệm hoặc giám sát; luồng chính vẫn chạy nếu chậm. | Có thể thu hẹp phạm vi, nhưng phải qua CR với client. |
| **Thấp** | Tiện ích quản trị không ảnh hưởng xử lý Ticket. | Cắt hoặc dời sau bàn giao trước tiên, qua CR. |

| FR | Priority | Mốc | FR | Priority | Mốc |
| --- | --- | --- | --- | --- | --- |
| FR-STU-00 | Cao | MS-01 | FR-STF-03 | Cao | MS-03 |
| FR-STU-01 | Trung bình | MS-02 | FR-STF-04 | Cao | MS-03 |
| FR-STU-02 | Cao | MS-02 | FR-STF-05 | Cao (Escalation: Trung bình) | MS-03 |
| FR-STU-03 | Cao | MS-02 → MS-04 theo sự kiện | FR-STF-06 | Cao | MS-04 |
| FR-STU-04 | Trung bình | MS-02 → MS-04 theo sự kiện | FR-MGT-00 | Cao | MS-01 |
| FR-STU-05 | Cao | MS-03 | FR-MGT-01 | Cao | MS-01 |
| FR-STU-06 | Cao | MS-04 | FR-MGT-02 | Cao | MS-01 |
| FR-STU-07 | Trung bình | MS-04 | FR-MGT-03 | Trung bình | MS-01, MS-05 |
| FR-STF-00 | Cao | MS-01 | FR-MGT-04 | Thấp | MS-05 |
| FR-STF-01 | Cao | MS-02 | FR-MGT-05 | Cao | MS-05 |
| FR-STF-02 | Cao | MS-02 | FR-MGT-06 | Cao (xuất CSV: Trung bình) | MS-05 |

Thứ tự mốc đi theo luồng Ticket, nên khớp với ưu tiên: mọi FR mức Cao của luồng Ticket nằm ở MS-01…MS-04. FR-MGT-05/06 tuy mức Cao vẫn ở MS-05 vì cần dữ liệu của vòng đời Ticket đầy đủ. FR-STU-01 (Trung bình) làm ở MS-02 vì nhỏ (14h) và gắn với màn hình tạo Ticket; nếu thiếu thời gian, đây là FR được thu hẹp đầu tiên.

Các trạng thái Ticket, thời hạn xử lý, quy tắc file đính kèm, mở lại Ticket và CSAT phải tuân thủ thống nhất theo [02-domain](../02-domain/).
