# CẤU TRÚC PHÂN RÃ CÔNG VIỆC (WBS)

**WORK BREAKDOWN STRUCTURE | DỰ ÁN UNISUPPORT – STUDENT SUPPORT MANAGEMENT SYSTEM**

Đơn vị thực hiện: Nhóm 3 · Người lập: Project Manager · Căn cứ: Proposal; được chi tiết hóa trong PRD

Bản gốc dạng bảng tính: [wbs.xlsx](wbs.xlsx). Cấp 1: dự án. Cấp 2: hạng mục chính. Cấp 3: gói công việc.

## 1. Sơ đồ WBS

```text
1 UniSupport – Student Support Management System
    1.1 Quản lý dự án
        1.1.1 Tài liệu khởi động dự án
        1.1.2 Kế hoạch dự án
        1.1.3 Báo cáo tình hình dự án
        1.1.4 Hồ sơ kiểm soát thay đổi và rủi ro
        1.1.5 Hồ sơ đóng dự án
    1.2 Phân tích và thiết kế
        1.2.1 Tài liệu yêu cầu sản phẩm (PRD)
        1.2.2 Thiết kế giao diện
        1.2.3 Thiết kế kỹ thuật
    1.3 Phân hệ Sinh viên
        1.3.1 Chức năng tra cứu hướng dẫn
        1.3.2 Chức năng gửi yêu cầu hỗ trợ
        1.3.3 Chức năng theo dõi yêu cầu và thông báo
        1.3.4 Chức năng bổ sung thông tin
        1.3.5 Chức năng nhận kết quả và đánh giá
    1.4 Phân hệ Nhân viên
        1.4.1 Hàng chờ xử lý
        1.4.2 Chức năng phân loại, phân công và ưu tiên
        1.4.3 Chức năng chuyển xử lý
        1.4.4 Chức năng cập nhật tiến độ
        1.4.5 Chức năng ghi kết quả và đóng yêu cầu
    1.5 Phân hệ Quản lý
        1.5.1 Dashboard tổng quan
        1.5.2 Báo cáo quản trị
        1.5.3 Chức năng quản trị tài khoản
        1.5.4 Chức năng cấu hình hệ thống
    1.6 Bảo mật dùng chung
        1.6.1 Chức năng đăng nhập và xác thực
        1.6.2 Cơ chế kiểm soát truy cập
        1.6.3 Nhật ký thao tác
    1.7 Tích hợp và kiểm thử
        1.7.1 Hệ thống tích hợp
        1.7.2 Kết quả kiểm thử hệ thống
        1.7.3 Kết quả nghiệm thu người dùng (UAT)
    1.8 Triển khai và bàn giao
        1.8.1 Môi trường và bản triển khai
        1.8.2 Mã nguồn và tài liệu vận hành
        1.8.3 Cơ sở dữ liệu
        1.8.4 Hướng dẫn sử dụng
        1.8.5 Bảo hành
```

## 2. Bảng WBS

| Cấp | Mã WBS | Thành phần WBS | Loại thành phần | Chịu trách nhiệm | Tham gia | Mốc thực hiện |
|---|---|---|---|---|---|---|
| 1 | 1 | **UniSupport – Student Support Management System** | Dự án | PM | Toàn nhóm | Mốc 0–6; bảo hành |
| 2 | 1.1 | **Quản lý dự án** | Hạng mục chính | PM | — | Mốc 0–6 |
| 3 | 1.1.1 | Tài liệu khởi động dự án | Gói công việc | PM | BA | Mốc 0 |
| 3 | 1.1.2 | Kế hoạch dự án | Gói công việc | PM | BA, TL, QA/QC | Mốc 0 |
| 3 | 1.1.3 | Báo cáo tình hình dự án | Gói công việc | PM | TL, BA, QA/QC, UI/UX | Mốc 0–6 |
| 3 | 1.1.4 | Hồ sơ kiểm soát thay đổi và rủi ro | Gói công việc | PM | BA | Mốc 0–6 |
| 3 | 1.1.5 | Hồ sơ đóng dự án | Gói công việc | PM | — | Mốc 6 |
| 2 | 1.2 | **Phân tích và thiết kế** | Hạng mục chính | BA | UI/UX, TL | Mốc 0 |
| 3 | 1.2.1 | Tài liệu yêu cầu sản phẩm (PRD) | Gói công việc | BA | PM, QA/QC | Mốc 0 |
| 3 | 1.2.2 | Thiết kế giao diện | Gói công việc | UI/UX | BA | Mốc 0 |
| 3 | 1.2.3 | Thiết kế kỹ thuật | Gói công việc | TL | BE1 | Mốc 0 |
| 2 | 1.3 | **Phân hệ Sinh viên** | Hạng mục chính | TL | FE1, BE1 | Mốc 2–4 |
| 3 | 1.3.1 | Chức năng tra cứu hướng dẫn | Gói công việc | FE1 | BE1, UI/UX | Mốc 2 |
| 3 | 1.3.2 | Chức năng gửi yêu cầu hỗ trợ | Gói công việc | FE1 | BE1, UI/UX | Mốc 2 |
| 3 | 1.3.3 | Chức năng theo dõi yêu cầu và thông báo | Gói công việc | FE1 | BE1 | Mốc 2 |
| 3 | 1.3.4 | Chức năng bổ sung thông tin | Gói công việc | BE1 | FE1 | Mốc 3 |
| 3 | 1.3.5 | Chức năng nhận kết quả và đánh giá | Gói công việc | BE1 | FE1 | Mốc 4 |
| 2 | 1.4 | **Phân hệ Nhân viên** | Hạng mục chính | TL | FE2, BE2 | Mốc 2–4 |
| 3 | 1.4.1 | Hàng chờ xử lý | Gói công việc | FE2 | BE2 | Mốc 2 |
| 3 | 1.4.2 | Chức năng phân loại, phân công và ưu tiên | Gói công việc | BE2 | FE2 | Mốc 2–3 |
| 3 | 1.4.3 | Chức năng chuyển xử lý | Gói công việc | BE2 | FE2 | Mốc 3 |
| 3 | 1.4.4 | Chức năng cập nhật tiến độ | Gói công việc | BE2 | FE2 | Mốc 3 |
| 3 | 1.4.5 | Chức năng ghi kết quả và đóng yêu cầu | Gói công việc | BE2 | FE2 | Mốc 4 |
| 2 | 1.5 | **Phân hệ Quản lý** | Hạng mục chính | TL | FE1, FE2, BE1, BE2 | Mốc 1, 5 |
| 3 | 1.5.1 | Dashboard tổng quan | Gói công việc | BE1 | FE1 | Mốc 5 |
| 3 | 1.5.2 | Báo cáo quản trị | Gói công việc | BE1 | FE1 | Mốc 5 |
| 3 | 1.5.3 | Chức năng quản trị tài khoản | Gói công việc | BE1 | FE1 | Mốc 1 |
| 3 | 1.5.4 | Chức năng cấu hình hệ thống | Gói công việc | BE2 | FE2 | Mốc 1, 5 |
| 2 | 1.6 | **Bảo mật dùng chung** | Hạng mục chính | TL | BE1, BE2 | Mốc 1, 5 |
| 3 | 1.6.1 | Chức năng đăng nhập và xác thực | Gói công việc | BE1 | FE1 | Mốc 1 |
| 3 | 1.6.2 | Cơ chế kiểm soát truy cập | Gói công việc | BE2 | FE1, FE2 | Mốc 1 |
| 3 | 1.6.3 | Nhật ký thao tác | Gói công việc | BE2 | — | Mốc 1, 5 |
| 2 | 1.7 | **Tích hợp và kiểm thử** | Hạng mục chính | QA/QC | TL | Mốc 1–6 |
| 3 | 1.7.1 | Hệ thống tích hợp | Gói công việc | TL | FE1, FE2, BE1, BE2 | Mốc 6 |
| 3 | 1.7.2 | Kết quả kiểm thử hệ thống | Gói công việc | QA/QC | FE1, FE2, BE1, BE2 | Mốc 1–6 |
| 3 | 1.7.3 | Kết quả nghiệm thu người dùng (UAT) | Gói công việc | QA/QC | BA, PM | Mốc 6 |
| 2 | 1.8 | **Triển khai và bàn giao** | Hạng mục chính | DevOps | PM, TL | Mốc 1, 6; bảo hành |
| 3 | 1.8.1 | Môi trường và bản triển khai | Gói công việc | DevOps | TL | Mốc 1, 6 |
| 3 | 1.8.2 | Mã nguồn và tài liệu vận hành | Gói công việc | TL | DevOps | Mốc 6 |
| 3 | 1.8.3 | Cơ sở dữ liệu | Gói công việc | TL | BE1, BE2 | Mốc 6 |
| 3 | 1.8.4 | Hướng dẫn sử dụng | Gói công việc | BA | UI/UX, QA/QC | Mốc 6 |
| 3 | 1.8.5 | Bảo hành | Gói công việc | TL | FE1, FE2, BE1, BE2, QA/QC | 30 ngày sau nghiệm thu |

Số hạng mục chính (cấp 2): 8. Số gói công việc (cấp 3): 33.

## 3. Từ điển WBS

### 1.1 Quản lý dự án

Chịu trách nhiệm: PM · Tham gia: — · Mốc: Mốc 0–6 · Tài liệu tham chiếu: Proposal mục 3, 6; Team Charter; Kế hoạch quản trị và giám sát

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.1.1 | Tài liệu khởi động dự án | Mục tiêu, phạm vi, vai trò người dùng và quy tắc làm việc của nhóm. | Biên bản khởi động; Team Charter | Phạm vi và vai trò được toàn nhóm thống nhất. | PM | BA | Mốc 0 | — |
| 1.1.2 | Kế hoạch dự án | Lịch thực hiện, ngân sách, kế hoạch chất lượng, kế hoạch quản trị và giám sát. | Master Schedule; kế hoạch ngân sách nội bộ; Kế hoạch quản lý chất lượng; Kế hoạch quản trị và giám sát | Các kế hoạch được Nhà tài trợ dự án phê duyệt. | PM | BA, TL, QA/QC | Mốc 0 | — |
| 1.1.3 | Báo cáo tình hình dự án | Báo cáo định kỳ về tiến độ, chi phí, chất lượng và rủi ro. | Báo cáo tuần; báo cáo tháng; báo cáo mốc | Báo cáo được lập đúng kỳ, đúng mẫu tại Kế hoạch quản trị và giám sát. | PM | TL, BA, QA/QC, UI/UX | Mốc 0–6 | — |
| 1.1.4 | Hồ sơ kiểm soát thay đổi và rủi ro | Ghi nhận và đánh giá yêu cầu thay đổi; theo dõi rủi ro. | Sổ rủi ro; Decision Log | Mọi thay đổi được đánh giá và xác nhận trước khi thực hiện. | PM | BA | Mốc 0–6 | Thay đổi yêu cầu sát thời điểm bàn giao làm phát sinh lỗi mới. |
| 1.1.5 | Hồ sơ đóng dự án | Tổng kết dự án và hoàn tất nghiệm thu. | Báo cáo tổng kết; biên bản nghiệm thu | Aurora University ký xác nhận nghiệm thu. | PM | — | Mốc 6 | — |

### 1.2 Phân tích và thiết kế

Chịu trách nhiệm: BA · Tham gia: UI/UX, TL · Mốc: Mốc 0 · Tài liệu tham chiếu: Proposal giai đoạn 1–2

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.2.1 | Tài liệu yêu cầu sản phẩm (PRD) | Yêu cầu chức năng, quy tắc nghiệp vụ, luồng xử lý và tiêu chí nghiệm thu của ba phân hệ. | PRD | PRD được thống nhất; không còn câu hỏi mở ảnh hưởng đến phạm vi. | BA | PM, QA/QC | Mốc 0 | — |
| 1.2.2 | Thiết kế giao diện | Luồng màn hình và prototype cho Sinh viên, Nhân viên và Quản lý. | Luồng màn hình; prototype | Các luồng thao tác chính đầy đủ và nhất quán với PRD. | UI/UX | BA | Mốc 0 | — |
| 1.2.3 | Thiết kế kỹ thuật | Kiến trúc hệ thống, mô hình dữ liệu, API, cơ chế xác thực và phân quyền. | Tài liệu kiến trúc; mô hình dữ liệu; thiết kế API | Đủ cơ sở để bắt đầu lập trình. | TL | BE1 | Mốc 0 | — |

### 1.3 Phân hệ Sinh viên

Chịu trách nhiệm: TL · Tham gia: FE1, BE1 · Mốc: Mốc 2–4 · Tài liệu tham chiếu: Proposal Module 1; PRD M01

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.3.1 | Chức năng tra cứu hướng dẫn | Tra cứu hướng dẫn theo nhóm vấn đề trước khi gửi yêu cầu. | Trang hướng dẫn (FAQ) | Sinh viên tìm được hướng dẫn theo nhóm vấn đề và chuyển sang gửi yêu cầu khi cần. | FE1 | BE1, UI/UX | Mốc 2 | — |
| 1.3.2 | Chức năng gửi yêu cầu hỗ trợ | Chọn nhóm vấn đề, mô tả tình huống, đính kèm file và nhận mã Ticket. | Biểu mẫu gửi yêu cầu; mã Ticket | Mỗi lần gửi tạo đúng một Ticket có mã duy nhất và chuyển đến đúng phòng ban. | FE1 | BE1, UI/UX | Mốc 2 | Quy tắc nghiệp vụ theo nhóm vấn đề; liên kết biểu mẫu với Ticket; phụ thuộc giữa FE và BE. |
| 1.3.3 | Chức năng theo dõi yêu cầu và thông báo | Danh sách, chi tiết, lịch sử xử lý và thông báo về yêu cầu của sinh viên. | Màn hình theo dõi yêu cầu; thông báo trong hệ thống | Sinh viên chỉ xem được yêu cầu của mình; trạng thái và thông báo hiển thị đúng. | FE1 | BE1 | Mốc 2 | Đồng bộ trạng thái và lịch sử giữa Sinh viên và Nhân viên; kiểm soát phạm vi dữ liệu. |
| 1.3.4 | Chức năng bổ sung thông tin | Bổ sung thông tin hoặc tài liệu khi nhân viên yêu cầu. | Màn hình bổ sung thông tin | Sau khi bổ sung hợp lệ, yêu cầu trở lại trạng thái đang xử lý. | BE1 | FE1 | Mốc 3 | — |
| 1.3.5 | Chức năng nhận kết quả và đánh giá | Xem kết quả; chấp nhận hoặc yêu cầu xử lý lại; đánh giá mức độ hài lòng. | Màn hình kết quả và đánh giá | Chấp nhận, mở lại và đánh giá được ghi nhận đúng quy tắc trong PRD. | BE1 | FE1 | Mốc 4 | — |

### 1.4 Phân hệ Nhân viên

Chịu trách nhiệm: TL · Tham gia: FE2, BE2 · Mốc: Mốc 2–4 · Tài liệu tham chiếu: Proposal Module 2; PRD M02

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.4.1 | Hàng chờ xử lý | Danh sách yêu cầu mới và yêu cầu được giao; tìm kiếm, lọc và xem chi tiết. | Màn hình hàng chờ | Nhân viên chỉ thấy yêu cầu trong phạm vi được phép. | FE2 | BE2 | Mốc 2 | — |
| 1.4.2 | Chức năng phân loại, phân công và ưu tiên | Phân loại theo nhóm vấn đề, gán người phụ trách, đặt mức ưu tiên và thời hạn xử lý. | Chức năng phân loại và phân công | Mỗi yêu cầu có đúng một người phụ trách; thời hạn được tính đúng quy tắc trong PRD. | BE2 | FE2 | Mốc 2–3 | Ánh xạ phòng ban – nhân viên; quy tắc mức ưu tiên, thời hạn và ngày nghỉ. |
| 1.4.3 | Chức năng chuyển xử lý | Chuyển yêu cầu sang phòng ban khác hoặc chuyển cấp lên quản lý. | Chức năng chuyển phòng ban và chuyển cấp | Yêu cầu được chuyển đúng nơi nhận và giữ nguyên lịch sử xử lý. | BE2 | FE2 | Mốc 3 | Chuyển quyền phụ trách và chuyển cấp phụ thuộc mức ưu tiên, thời hạn. |
| 1.4.4 | Chức năng cập nhật tiến độ | Cập nhật trạng thái xử lý; yêu cầu sinh viên bổ sung thông tin. | Chức năng cập nhật tiến độ | Sinh viên xem được trạng thái mới nhất của yêu cầu. | BE2 | FE2 | Mốc 3 | Luồng nhiều trạng thái; yêu cầu bổ sung phải đồng bộ với vòng đời Ticket. |
| 1.4.5 | Chức năng ghi kết quả và đóng yêu cầu | Ghi kết quả xử lý, đóng yêu cầu và tiếp nhận lại yêu cầu được mở lại. | Chức năng ghi kết quả | Yêu cầu chuyển trạng thái đúng vòng đời trong PRD. | BE2 | FE2 | Mốc 4 | — |

### 1.5 Phân hệ Quản lý

Chịu trách nhiệm: TL · Tham gia: FE1, FE2, BE1, BE2 · Mốc: Mốc 1, 5 · Tài liệu tham chiếu: Proposal Module 3; PRD M03

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.5.1 | Dashboard tổng quan | Số yêu cầu mới, đang xử lý, sắp và đã quá hạn; khối lượng công việc theo phòng ban và nhân viên. | Dashboard | Số liệu khớp với dữ liệu xử lý thực tế. | BE1 | FE1 | Mốc 5 | Số liệu Dashboard không khớp dữ liệu xử lý thực tế. |
| 1.5.2 | Báo cáo quản trị | Nhóm vấn đề, xu hướng, thời gian xử lý, mức độ hài lòng; xuất dữ liệu. | Báo cáo; chức năng xuất dữ liệu | Báo cáo đúng công thức và phạm vi quyền trong PRD. | BE1 | FE1 | Mốc 5 | Số liệu báo cáo không khớp dữ liệu xử lý thực tế. |
| 1.5.3 | Chức năng quản trị tài khoản | Tạo, chỉnh sửa, khóa tài khoản; gán vai trò và phạm vi quản lý. | Màn hình quản trị tài khoản | Quyền truy cập phản ánh đúng cấu hình tài khoản. | BE1 | FE1 | Mốc 1 | Gán sai vai trò dẫn đến truy cập sai quyền. |
| 1.5.4 | Chức năng cấu hình hệ thống | Quản lý phòng ban, nhóm vấn đề và thời hạn lưu trữ dữ liệu. | Màn hình cấu hình danh mục và thời hạn lưu trữ | Mỗi nhóm vấn đề đang hoạt động có đúng một phòng ban tiếp nhận. | BE2 | FE2 | Mốc 1, 5 | — |

### 1.6 Bảo mật dùng chung

Chịu trách nhiệm: TL · Tham gia: BE1, BE2 · Mốc: Mốc 1, 5 · Tài liệu tham chiếu: Proposal mục Bảo mật và phân quyền; PRD yêu cầu bảo mật

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.6.1 | Chức năng đăng nhập và xác thực | Đăng nhập bằng tài khoản riêng, duy trì phiên và điều hướng theo vai trò. | Chức năng đăng nhập | Tài khoản hợp lệ vào đúng khu vực; tài khoản bị khóa bị từ chối. | BE1 | FE1 | Mốc 1 | Sai sót xác thực làm lộ tài khoản. |
| 1.6.2 | Cơ chế kiểm soát truy cập | Kiểm tra quyền phía máy chủ đối với dữ liệu, chức năng và file đính kèm. | Cơ chế phân quyền phía máy chủ | Mọi truy cập ngoài phạm vi quyền bị chặn. | BE2 | FE1, FE2 | Mốc 1 | Phân quyền sai đối với Ticket hoặc file đính kèm. |
| 1.6.3 | Nhật ký thao tác | Ghi nhận và tra cứu các thao tác quan trọng. | Nhật ký thao tác | Thao tác quan trọng đều có bản ghi; bản ghi không sửa, xóa được bằng chức năng thông thường. | BE2 | — | Mốc 1, 5 | Nhật ký không nhất quán giữa các phân hệ. |

### 1.7 Tích hợp và kiểm thử

Chịu trách nhiệm: QA/QC · Tham gia: TL · Mốc: Mốc 1–6 · Tài liệu tham chiếu: Proposal giai đoạn 4–5; Kế hoạch quản lý chất lượng

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.7.1 | Hệ thống tích hợp | Tích hợp giao diện với backend; kết nối dữ liệu xử lý với Dashboard và báo cáo. | Bản build tích hợp hoàn chỉnh | Luồng yêu cầu chạy thông suốt từ khi gửi đến khi đóng. | TL | FE1, FE2, BE1, BE2 | Mốc 6 | — |
| 1.7.2 | Kết quả kiểm thử hệ thống | Kiểm thử chức năng, tích hợp, phân quyền, hồi quy và độ ổn định. | Test case; kết quả kiểm thử; danh sách lỗi | Đạt các điều kiện tại Kế hoạch quản lý chất lượng. | QA/QC | FE1, FE2, BE1, BE2 | Mốc 1–6 | — |
| 1.7.3 | Kết quả nghiệm thu người dùng (UAT) | Thực hiện kịch bản nghiệm thu cùng khách hàng; khắc phục lỗi phát sinh. | Kết quả UAT | Không còn lỗi làm gián đoạn chức năng chính. | QA/QC | BA, PM | Mốc 6 | Thông tin, phản hồi từ phía Aurora University chậm so với kế hoạch. |

### 1.8 Triển khai và bàn giao

Chịu trách nhiệm: DevOps · Tham gia: PM, TL · Mốc: Mốc 1, 6; bảo hành · Tài liệu tham chiếu: Proposal giai đoạn 6, mục 5.1, 5.3

| Mã WBS | Gói công việc | Mô tả công việc | Sản phẩm bàn giao | Tiêu chí chấp nhận | Chịu trách nhiệm | Tham gia | Mốc thực hiện | Rủi ro chính |
|---|---|---|---|---|---|---|---|---|
| 1.8.1 | Môi trường và bản triển khai | Môi trường phát triển và kiểm thử; triển khai hệ thống lên môi trường của khách hàng. | Môi trường Dev/Test; hệ thống trên môi trường khách hàng | Hệ thống truy cập được trên trình duyệt máy tính và thiết bị di động. | DevOps | TL | Mốc 1, 6 | Hiệu năng phụ thuộc hạ tầng do Aurora University cung cấp. |
| 1.8.2 | Mã nguồn và tài liệu vận hành | Mã nguồn frontend, backend và tài liệu cài đặt, vận hành hệ thống. | Mã nguồn; tài liệu cài đặt và vận hành | Bên nhận cài đặt được hệ thống theo tài liệu. | TL | DevOps | Mốc 6 | — |
| 1.8.3 | Cơ sở dữ liệu | Cấu trúc cơ sở dữ liệu, ERD và dữ liệu mẫu phục vụ kiểm thử. | Cấu trúc cơ sở dữ liệu; ERD; dữ liệu mẫu | Đủ hạng mục theo cam kết bàn giao trong Proposal. | TL | BE1, BE2 | Mốc 6 | — |
| 1.8.4 | Hướng dẫn sử dụng | Hướng dẫn sử dụng cho Sinh viên, Nhân viên và Quản lý. | Hướng dẫn sử dụng theo vai trò | Mỗi vai trò có hướng dẫn cho các luồng thao tác chính. | BA | UI/UX, QA/QC | Mốc 6 | — |
| 1.8.5 | Bảo hành | Sửa lỗi kỹ thuật phát sinh từ phía nhóm phát triển; không bao gồm tính năng mới hoặc thay đổi ngoài phạm vi. | Danh sách lỗi đã khắc phục trong thời gian bảo hành | Lỗi thuộc trách nhiệm nhóm phát triển được khắc phục trong thời gian bảo hành. | TL | FE1, FE2, BE1, BE2, QA/QC | 30 ngày sau nghiệm thu | — |

## 4. Thuật ngữ

| Thuật ngữ | Định nghĩa |
|---|---|
| WBS (Work Breakdown Structure) | Cấu trúc phân rã toàn bộ phạm vi dự án thành các thành phần nhỏ hơn theo dạng phân cấp, hướng tới sản phẩm bàn giao. |
| Thành phần WBS | Một mục trong WBS ở bất kỳ cấp nào. |
| Mã WBS | Mã số phân cấp xác định vị trí của thành phần trong WBS, ví dụ 1.3.2. |
| Hạng mục chính | Thành phần cấp 2, gom các gói công việc cùng tạo ra một nhóm sản phẩm bàn giao hoặc cùng thuộc một lĩnh vực công việc. |
| Gói công việc (work package) | Thành phần ở cấp thấp nhất của WBS; là đơn vị để ước lượng chi phí, lập lịch và giao trách nhiệm. |
| Sản phẩm bàn giao | Kết quả hữu hình mà một gói công việc phải tạo ra. |
| Chịu trách nhiệm | Người duy nhất chịu trách nhiệm hoàn thành gói công việc. |
| Tham gia | Các vai trò cùng thực hiện hoặc hỗ trợ gói công việc. |
| Từ điển WBS | Tài liệu mô tả chi tiết từng gói công việc: phạm vi, sản phẩm bàn giao, tiêu chí chấp nhận, người chịu trách nhiệm và rủi ro. |
| Quy tắc 100% | WBS bao gồm toàn bộ công việc của dự án, không thiếu và không trùng lặp; tổng các thành phần con bằng thành phần cha. |
