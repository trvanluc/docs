# Phạm Vi Sản Phẩm & Các Giả Định Dự Án (Product Scope & Assumptions)

> **Nơi gốc của phạm vi với khách là [Proposal.docx](../08-project/Proposal.docx) mục 2.1–2.3 "Phạm Vi Chức Năng" và mục 2.5 "Các hạng mục ngoài phạm vi hiện tại (Out of Scope)"** (decision-log `D-05`); giả định ở mục 2.4. File này là bản chi tiết cho nhóm, liệt kê cùng phạm vi đó theo từng phân hệ. Nếu hai nơi lệch nhau thì Proposal là căn cứ, sửa file này cho khớp; muốn đổi phạm vi thì đi qua quy trình CR.

## 1. Phạm Vi Chức Năng Sản Phẩm (Functional Scope)

UniSupport gồm **3 phân hệ chính**. Thông báo, xác thực, RBAC và bảo mật là các năng lực dùng chung, không được xem là các phân hệ nghiệp vụ độc lập.

### 1.1 Module Sinh viên (Student Portal) — báo giá `Q-01`

- Đăng nhập hệ thống.
- Tra cứu hướng dẫn/FAQ.
- Gửi yêu cầu hỗ trợ.
- Chọn nhóm vấn đề và nhập nội dung yêu cầu.
- Đính kèm file minh chứng theo quy định của hệ thống.
- Nhận mã Ticket sau khi gửi thành công.
- Xem tiến độ xử lý và lịch sử cập nhật.
- Xem đơn vị/người phụ trách theo thông tin hệ thống cung cấp.
- Bổ sung thông tin hoặc giấy tờ khi nhân viên yêu cầu.
- Nhận thông báo và xem kết quả xử lý.
- Phản hồi khi kết quả chưa giải quyết được vấn đề.
- Đánh giá mức độ hài lòng sau khi yêu cầu được giải quyết.

### 1.2 Module Nhân viên (Staff Operations) — báo giá `Q-02`

- Đăng nhập hệ thống.
- Xem, tìm kiếm và lọc các yêu cầu mới/được giao trong phạm vi quyền.
- Tiếp nhận, phân loại và phân công yêu cầu.
- Xác định mức độ ưu tiên và theo dõi thời hạn xử lý.
- Cập nhật trạng thái vòng đời; ghi chú xử lý là nội bộ, không tự động công bố cho sinh viên.
- Yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ.
- Phân công lại người phụ trách trong cùng phòng ban, chuyển xử lý sang phòng ban phù hợp và thực hiện chuyển cấp khi cần.
- Ghi nhận kết quả xử lý và chuyển Ticket sang `RESOLVED`.
- Tiếp tục xử lý khi Ticket được sinh viên mở lại hợp lệ về `IN_PROGRESS`.

### 1.3 Module Quản lý (Management Dashboard) — báo giá `Q-03`

- Đăng nhập hệ thống.
- Xem số lượng yêu cầu mới, đang xử lý, sắp quá hạn hoặc đã quá hạn.
- Theo dõi tiến độ và khối lượng công việc theo phòng ban hoặc nhân viên.
- Xem xu hướng các nhóm yêu cầu.
- Xem thời gian xử lý trung bình và các chỉ số phục vụ quản lý.
- Xem tổng hợp phản hồi/CSAT của sinh viên.
- Xem và xuất các báo cáo thuộc phạm vi được cấp.
- Tạo/chỉnh sửa/khóa tài khoản và gán quyền/phòng ban khi được cấp quyền quản trị.
- Quản lý phòng ban, nhóm vấn đề/danh mục và cấu hình nghiệp vụ cơ bản.
- Tra soát các thao tác quan trọng.
- Quản lý chính sách lưu trữ dữ liệu cơ bản trong phạm vi hệ thống.

> Staff chỉ ghi kết quả/chuyển `RESOLVED`; Student sở hữu xác nhận hoặc hệ thống hết 03 ngày làm việc mới `CLOSED`. Sinh viên thấy trạng thái, đơn vị/người phụ trách và sự kiện được phép, không thấy ghi chú nội bộ.

> Các chức năng quản trị hệ thống thuộc phạm vi của phân hệ **Management** và được kiểm soát theo quyền của tài khoản Quản lý.

### 1.4 Năng lực dùng chung — báo giá `Q-03`

**Thông báo trong hệ thống**
- Tạo và hiển thị thông báo cho người dùng liên quan khi Ticket phát sinh các sự kiện nghiệp vụ được quy định.

**Xác thực, bảo mật & phân quyền**
- Cả 3 phân hệ sử dụng chung cơ chế xác thực.
- Người dùng đăng nhập bằng tài khoản được cấp.
- Mỗi người dùng chỉ được xem và thao tác trong phạm vi quyền của mình; cấp/thu hồi quyền hữu hạn trên tài khoản theo [Actors & Roles mục 4](actors-and-roles.md#4-danh-mục-quyền-chức-năng-hữu-hạn), không tạo role tùy ý.
- File đính kèm chỉ người liên quan và có quyền được truy cập.
- Các thao tác quan trọng được ghi nhận để phục vụ tra soát.

> Các quy tắc chi tiết về trạng thái Ticket, mức độ ưu tiên, thời hạn xử lý, file đính kèm, CSAT, chuyển xử lý, escalation, đóng/mở lại Ticket và lưu trữ dữ liệu được đặc tả tại Domain, Functional Requirements, Workflows và Acceptance.

---

## 2. Các Hạng Mục Ngoài Phạm Vi (Out of Scope)

Danh sách gốc ở Proposal mục 2.5 "Out of Scope"; lý do từng mục ở [goals-and-non-goals.md mục 2](goals-and-non-goals.md#2-các-mục-nằm-ngoài-phạm-vi-hiện-tại-out-of-scope--non-goals).

- Mobile App độc lập cho iOS/Android.
- Tích hợp hệ thống bên thứ ba ngoài phạm vi sản phẩm.
- Thiết lập sao lưu tự động, theo dõi vận hành máy chủ và hỗ trợ hạ tầng lâu dài.
- Cơ chế phân quyền tùy biến nhiều cấp hoặc mô hình phân quyền phức tạp ngoài phạm vi đã xác định.
- Hệ thống audit/kiểm toán chuyên sâu ngoài nhật ký thao tác cần thiết.
- Chat trực tiếp hoặc gọi thoại trong hệ thống.
- Tối ưu chịu tải lớn vượt quá quy mô khoảng 3.000 sinh viên.
- Chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.

---

## 3. Giả Định Dự Án (Project Assumptions)

1. **Quy mô sử dụng**: Hệ thống phục vụ khoảng 3.000 sinh viên.
2. **Nền tảng**: Hệ thống được triển khai dưới dạng Web Application, không phải Mobile App độc lập.
3. **Thiết bị**: Các luồng chính phải sử dụng được trên trình duyệt máy tính và thiết bị di động.
4. **Ngôn ngữ**: Giao diện hỗ trợ Tiếng Việt và Tiếng Anh ở mức cơ bản.
5. **Hạ tầng**: Máy chủ và tên miền do Aurora University cung cấp; hiệu năng và tính ổn định phụ thuộc vào hạ tầng này.
6. **Tích hợp**: Không yêu cầu tích hợp bên thứ ba trong phạm vi hiện tại.
7. **Bảo mật**: Không yêu cầu chứng nhận bảo mật hoặc kiểm thử bảo mật chuyên sâu.
8. **Phản hồi/phê duyệt**: Thời gian chờ phản hồi hoặc phê duyệt từ phía Client được quản lý như một phụ thuộc của kế hoạch dự án.

---

## 4. Ràng Buộc Dự Án (Project Constraints)

- **Thời gian thực hiện**: 108 ngày làm việc / 163 ngày lịch; dự kiến 07/12/2026–18/05/2027 theo lịch nghỉ và điều kiện xác nhận tại [Master Plan](../08-project/master-plan.md#thời-điểm-của-dự-án).
- **Ngân sách**: 300.000.000 VNĐ.
- **Nghiệm thu chính thức**: 10 ngày làm việc kể từ khi bàn giao.
- **Bảo hành kỹ thuật**: 30 ngày kể từ ngày hai bên xác nhận nghiệm thu.
- **Thay đổi phạm vi**: Mọi điều chỉnh ảnh hưởng phạm vi, chi phí hoặc tiến độ cần được xác nhận trước khi áp dụng.

---

## 5. Vị Trí Của Tài Liệu Chi Tiết

File này chỉ mô tả phạm vi sản phẩm ở mức cao. Chi tiết được tách sang các phần chuyên trách:

- `02-domain/`: mô hình nghiệp vụ, trạng thái Ticket, lifecycle và business rules dùng chung.
- `03-modules/`: Functional Requirements, luồng chính, error flow và Acceptance Criteria của 3 phân hệ.
- `04-workflows/`: các luồng nghiệp vụ xuyên nhiều chức năng/phân hệ.
- `05-non-functional-requirements/`: yêu cầu phi chức năng.
- `06-acceptance/`: traceability và test scenarios.
- `07-architecture/`: quyết định kỹ thuật và thiết kế triển khai.
