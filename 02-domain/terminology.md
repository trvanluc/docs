# Thuật Ngữ Nghiệp Vụ (Domain Terminology)

Tài liệu này định nghĩa toàn bộ các thuật ngữ, khái niệm và từ viết tắt được sử dụng nhất quán trong tài liệu thiết kế, mã nguồn và quy trình vận hành của hệ thống **UniSupport**.

## 1. Danh Mục Thuật Ngữ Cốt Lõi

| Thuật Ngữ (English) | Thuật Ngữ (Tiếng Việt) | Định Nghĩa & Giải Thích Chi Tiết |
| :--- | :--- | :--- |
| **Ticket** | Phiếu hỗ trợ / Yêu cầu | Đơn vị dữ liệu trung tâm đại diện cho 01 yêu cầu, thắc mắc hoặc đề nghị giải quyết thủ tục của sinh viên gửi tới nhà trường. |
| **Ticket ID** | Mã phiếu hỗ trợ | Chuỗi ký tự định danh duy nhất được hệ thống tự động sinh ra khi sinh viên gửi yêu cầu thành công (Ví dụ: `TK-20261004-0001`). |
| **Category** | Nhóm vấn đề | Danh mục phân loại nội dung yêu cầu do ADMIN quản lý, ví dụ Học phí, Đăng ký môn học, Giấy xác nhận. Mỗi nhóm gắn mặc định với một phòng ban. Không đặc tả thêm phân loại nhiều cấp. |
| **Department** | Phòng ban chuyên trách | Đơn vị hành chính trong Aurora University có thẩm quyền xử lý Ticket (Ví dụ: Phòng Đào tạo, Phòng CTHSSV...). |
| **Student** | Sinh viên | Người dùng khởi tạo Ticket và là người thụ hưởng kết quả xử lý. |
| **Agent / Staff** | Nhân viên xử lý | Chuyên viên thuộc Phòng ban chức năng có nhiệm vụ tiếp nhận, xử lý và phản hồi Ticket. |
| **Manager** | Quản lý phòng ban | Giám sát, báo cáo và phân công trong phòng ban mình; không quản trị tài khoản toàn trường. |
| **Admin** | Quản trị viên | Quản trị tài khoản, vai trò, danh mục, tra soát và báo cáo toàn trường theo quyền đã có. |
| **Triage** | Phân loại & Điều phối | Quá trình kiểm tra nội dung Ticket mới để xác định đúng nhóm vấn đề, độ ưu tiên và gán cho nhân viên/phòng ban phù hợp. |
| **Claim** | Tiếp nhận | Hành động nhân viên tự nhận một Ticket chưa có người phụ trách về cho chính mình xử lý. |
| **Assign** | Phân công | Hành động gán trách nhiệm xử lý Ticket cho một nhân viên cụ thể trong cùng phòng ban. |
| **Transfer** | Chuyển phòng ban | Hành động điều chuyển Ticket từ phòng ban hiện tại sang một phòng ban khác do gửi nhầm hoặc cần phối hợp. |
| **Supplement Request** | Yêu cầu bổ sung | Yêu cầu từ nhân viên đề nghị sinh viên cung cấp thêm thông tin hoặc upload thêm giấy tờ minh chứng. |
| **SLA (Service Level Agreement)** | Cam kết thời gian xử lý | Khung thời gian tiêu chuẩn quy định hạn chót nhân viên phải phản hồi hoặc xử lý xong Ticket. |
| **Priority** | Mức độ ưu tiên | Tầm quan trọng/mức độ khẩn cấp của Ticket (Bao gồm 4 mức: *Thấp, Trung bình, Cao, Khẩn cấp*). |
| **Resolution** | Kết quả giải quyết | Nội dung trả lời, quyết định hoặc tài liệu đính kèm do nhân viên cung cấp để hoàn thành yêu cầu của sinh viên. |
| **CSAT (Customer Satisfaction)** | Mức độ hài lòng | Chỉ số đánh giá chất lượng dịch vụ do sinh viên chấm điểm (từ 1 đến 5 sao) khi Ticket đã RESOLVED hoặc CLOSED và chưa có đánh giá, theo FR-STU-04. |
| **Audit Log / Activity Log** | Nhật ký tra soát | Bản ghi lịch sử ghi nhận lại từng hành động làm thay đổi dữ liệu hoặc trạng thái của Ticket. |
| **UAT (User Acceptance Testing)** | Kiểm thử chấp nhận người dùng | Giai đoạn người dùng thực tế (sinh viên, nhân viên Aurora University) kiểm thử hệ thống trước khi vận hành chính thức. |
