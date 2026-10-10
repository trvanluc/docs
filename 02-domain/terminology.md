# Thuật Ngữ Nghiệp Vụ (Domain Terminology)

Tài liệu này chuẩn hóa các thuật ngữ nghiệp vụ được sử dụng xuyên suốt **UniSupport** nhằm bảo đảm các tài liệu yêu cầu, quy trình nghiệp vụ, kiểm thử và thiết kế hệ thống sử dụng cùng một cách hiểu.

## 1. Danh Mục Thuật Ngữ Cốt Lõi

| Thuật ngữ (English) | Thuật ngữ (Tiếng Việt) | Định nghĩa |
| :--- | :--- | :--- |
| **Ticket** | Phiếu hỗ trợ / Yêu cầu hỗ trợ | Đơn vị nghiệp vụ đại diện cho một yêu cầu hỗ trợ do sinh viên gửi đến nhà trường và được theo dõi xuyên suốt quá trình xử lý. |
| **Ticket Code** | Mã Ticket | Mã định danh duy nhất do hệ thống tạo khi Ticket được gửi thành công, dùng để tra cứu và theo dõi yêu cầu. |
| **Category** | Nhóm vấn đề | Nhóm phân loại nội dung Ticket, dùng để hỗ trợ xác định phạm vi xử lý và điều phối đến đơn vị phù hợp. |
| **Department** | Phòng ban | Đơn vị thuộc Aurora University chịu trách nhiệm tiếp nhận hoặc xử lý Ticket trong phạm vi chức năng được giao. |
| **Student** | Sinh viên | Người dùng tạo Ticket, theo dõi tiến độ, bổ sung thông tin, nhận kết quả và đánh giá mức độ hài lòng. |
| **Staff** | Nhân viên | Người dùng thuộc các phòng ban thực hiện tiếp nhận, phân loại, xử lý, cập nhật tiến độ và ghi nhận kết quả Ticket. |
| **Management** | Quản lý | Nhóm người dùng thực hiện giám sát hoạt động hỗ trợ, theo dõi Dashboard/báo cáo và sử dụng các chức năng quản trị được phân quyền. |
| **Assignee** | Người phụ trách | Nhân viên được giao trách nhiệm chính để xử lý một Ticket tại một thời điểm. |
| **Triage** | Phân loại và điều phối | Quá trình kiểm tra Ticket để xác định nhóm vấn đề, mức độ ưu tiên và đơn vị/người phụ trách phù hợp. |
| **Assign** | Phân công | Hành động giao Ticket cho một nhân viên hoặc người phụ trách cụ thể theo phạm vi quyền được cấp. |
| **Transfer** | Chuyển xử lý | Hành động chuyển Ticket sang **phòng ban khác** chịu trách nhiệm xử lý. Khi Transfer, Nhóm vấn đề và phòng ban được cập nhật nhất quán theo cấu hình, người phụ trách hiện tại được gỡ khỏi Ticket và phòng ban mới thực hiện tiếp nhận/phân công lại. |
| **Escalation** | Chuyển cấp xử lý | Hành động gửi yêu cầu hỗ trợ lên tài khoản Quản lý phù hợp khi Ticket vượt thẩm quyền, cần hỗ trợ hoặc có nguy cơ trễ hạn. Escalation không tự thay đổi Nhóm vấn đề, phòng ban, người phụ trách hoặc trạng thái Ticket. |
| **Supplement Request** | Yêu cầu bổ sung | Yêu cầu do nhân viên gửi cho sinh viên để bổ sung thông tin hoặc tài liệu còn thiếu trước khi tiếp tục xử lý Ticket. |
| **Priority** | Mức độ ưu tiên | Mức thể hiện độ ưu tiên xử lý của Ticket, gồm **Thấp, Trung bình, Cao và Khẩn cấp**. |
| **Processing Deadline** | Thời hạn xử lý | Mốc thời gian được sử dụng để theo dõi tiến độ xử lý Ticket và xác định tình trạng sắp quá hạn hoặc quá hạn. |
| **Working Day** | Ngày làm việc | Ngày từ thứ Hai đến thứ Sáu, không bao gồm ngày nghỉ lễ hoặc ngày nghỉ chính thức của Aurora University. |
| **Overdue** | Quá hạn | Tình trạng Ticket chưa hoàn tất xử lý khi đã vượt quá thời hạn xử lý được xác định cho Ticket đó. |
| **Resolution** | Kết quả xử lý | Nội dung hoặc tài liệu phản hồi được ghi nhận sau khi nhân viên hoàn tất phần xử lý nghiệp vụ của Ticket. |
| **NEW** | Yêu cầu mới | Trạng thái của Ticket sau khi được tạo thành công và đang chờ tiếp nhận hoặc phân công xử lý. |
| **IN_PROGRESS** | Đang xử lý | Trạng thái của Ticket khi yêu cầu đang được nhân viên hoặc phòng ban phụ trách xử lý. |
| **WAITING_STUDENT** | Chờ sinh viên bổ sung | Trạng thái của Ticket khi quá trình xử lý đang chờ sinh viên cung cấp thêm thông tin hoặc tài liệu. |
| **RESOLVED** | Đã giải quyết | Trạng thái cho biết Ticket đã có kết quả xử lý và đang trong thời hạn để sinh viên xem, phản hồi hoặc xác nhận kết quả. |
| **CLOSED** | Đã đóng | Trạng thái kết thúc vòng đời xử lý khi sinh viên chấp nhận kết quả hoặc hết thời hạn phản hồi theo quy định. |
| **Reopen** | Mở lại Ticket | Hành động đưa Ticket từ `RESOLVED` trở lại `IN_PROGRESS` khi sinh viên phản hồi rằng vấn đề chưa được giải quyết và đáp ứng điều kiện mở lại. |
| **CSAT (Customer Satisfaction)** | Mức độ hài lòng | Chỉ số đánh giá chất lượng hỗ trợ do sinh viên chấm theo thang **1 đến 5 sao** sau khi Ticket đã đóng và còn trong thời hạn đánh giá. |
| **Activity History** | Lịch sử xử lý | Chuỗi các hoạt động và thay đổi quan trọng phát sinh trong suốt vòng đời Ticket, bao gồm cập nhật trạng thái, phân công, chuyển xử lý, yêu cầu bổ sung và ghi nhận kết quả. |
| **Audit Trail** | Nhật ký tra soát | Dữ liệu ghi nhận các thao tác quan trọng nhằm phục vụ kiểm tra, đối chiếu và tra soát khi cần. |
| **UAT (User Acceptance Testing)** | Kiểm thử chấp nhận người dùng | Giai đoạn kiểm thử nhằm xác nhận hệ thống đáp ứng yêu cầu nghiệp vụ và tiêu chí nghiệm thu trước khi bàn giao chính thức. |

## 2. Quy Ước Sử Dụng Thuật Ngữ

- **Ticket** là thuật ngữ thống nhất để chỉ yêu cầu hỗ trợ trong toàn bộ tài liệu dự án.
- **Staff** và **Management** là hai nhóm người dùng độc lập về phạm vi chức năng; các chức năng quản trị hệ thống thuộc phạm vi Management và được kiểm soát theo quyền.
- Bộ trạng thái nghiệp vụ thống nhất gồm `NEW`, `IN_PROGRESS`, `WAITING_STUDENT`, `RESOLVED` và `CLOSED`.
- **Transfer** và **Escalation** là hành động nghiệp vụ, không phải trạng thái Ticket.
- **Transfer** là chuyển sang phòng ban khác; đổi người phụ trách trong cùng phòng ban được thực hiện bằng phân công lại.
- **Escalation** là yêu cầu hỗ trợ từ Quản lý phù hợp và không tự thay đổi phòng ban, người phụ trách hoặc trạng thái Ticket.
- Các trạng thái và điều kiện chuyển trạng thái được quy định chi tiết tại `ticket-lifecycle.md` và `state-transition.md`.
- Các giá trị và điều kiện nghiệp vụ chi tiết như thời hạn xử lý, giới hạn file, điều kiện mở lại Ticket và quy tắc đánh giá được quy định tại `business-rules.md`.
