# Mô Hình Nghiệp Vụ Ticket (Ticket Domain Model)

Ticket là thực thể nghiệp vụ trung tâm của **UniSupport**, đại diện cho một yêu cầu hỗ trợ của sinh viên và được theo dõi xuyên suốt từ khi tạo đến khi hoàn tất xử lý.

Tài liệu này mô tả các thông tin nghiệp vụ chính của Ticket và các thực thể liên quan. Chi tiết triển khai kỹ thuật như kiểu dữ liệu, khóa chính/khóa ngoại, cấu trúc bảng hoặc định dạng lưu trữ được đặc tả ở phần thiết kế hệ thống.

## 1. Thực Thể Ticket

| Thông tin | Bắt buộc | Ý nghĩa nghiệp vụ |
| :--- | :---: | :--- |
| **Mã Ticket** | Có | Mã định danh duy nhất do hệ thống tạo khi Ticket được gửi thành công, dùng để tra cứu và theo dõi yêu cầu. |
| **Sinh viên tạo Ticket** | Có | Sinh viên sở hữu yêu cầu và theo dõi quá trình xử lý của Ticket. |
| **Nhóm vấn đề** | Có | Nhóm phân loại nội dung yêu cầu, dùng để hỗ trợ điều phối xử lý. |
| **Nội dung yêu cầu** | Có | Mô tả vấn đề hoặc nhu cầu hỗ trợ do sinh viên cung cấp. |
| **Phòng ban phụ trách** | Có | Đơn vị chịu trách nhiệm tiếp nhận hoặc xử lý Ticket tại thời điểm hiện tại. |
| **Người phụ trách** | Không | Nhân viên được giao trách nhiệm chính để xử lý Ticket; có thể chưa được xác định ngay khi Ticket vừa được tạo hoặc sau khi chuyển xử lý. |
| **Trạng thái** | Có | Trạng thái hiện tại của Ticket trong vòng đời xử lý. Tập trạng thái và quy tắc chuyển trạng thái được quy định tại `ticket-lifecycle.md` và `state-transition.md`. |
| **Mức độ ưu tiên** | Có | Mức độ ưu tiên xử lý của Ticket theo quy tắc nghiệp vụ. |
| **Thời hạn xử lý** | Có | Mốc thời gian dùng để theo dõi tiến độ và xác định Ticket sắp hoặc đã quá hạn. |
| **Kết quả xử lý** | Không | Nội dung hoặc tài liệu phản hồi được ghi nhận khi Ticket đã được xử lý. |
| **Thời điểm tạo** | Có | Thời điểm Ticket được tạo thành công trên hệ thống. |
| **Thời điểm cập nhật gần nhất** | Có | Thời điểm phát sinh thay đổi nghiệp vụ gần nhất trên Ticket. |
| **Thời điểm giải quyết** | Không | Thời điểm Ticket được ghi nhận là đã có kết quả xử lý. |
| **Thời điểm đóng** | Không | Thời điểm Ticket chuyển sang trạng thái kết thúc vòng đời xử lý. |

---

## 2. File Đính Kèm Ticket (Ticket Attachment)

File đính kèm là tài liệu minh chứng hoặc tài liệu trao đổi gắn với một Ticket. UniSupport hỗ trợ file ảnh và PDF theo phạm vi chức năng đã xác định.

| Thông tin | Bắt buộc | Ý nghĩa nghiệp vụ |
| :--- | :---: | :--- |
| **Ticket liên quan** | Có | Ticket mà file đính kèm thuộc về. |
| **Tên file** | Có | Tên file được người dùng tải lên. |
| **Loại file** | Có | Loại tài liệu được hệ thống chấp nhận theo quy tắc file đính kèm. |
| **Dung lượng file** | Có | Dung lượng của file để hệ thống kiểm tra giới hạn cho phép. |
| **Người tải lên** | Có | Người dùng thực hiện thao tác tải file lên Ticket. |
| **Thời điểm tải lên** | Có | Thời điểm file được ghi nhận trong hệ thống. |

Các giới hạn cụ thể về định dạng, dung lượng và số lượng file được quy định tại `business-rules.md`.

---

## 3. Lịch Sử Xử Lý Ticket (Ticket Activity History)

Lịch sử xử lý ghi nhận các hoạt động và thay đổi quan trọng phát sinh trong toàn bộ vòng đời Ticket nhằm bảo đảm khả năng theo dõi và tra soát.

Các sự kiện nghiệp vụ được ghi nhận bao gồm:

- Tạo Ticket.
- Phân loại Ticket.
- Phân công người phụ trách.
- Thay đổi trạng thái.
- Thay đổi mức độ ưu tiên hoặc thời hạn xử lý.
- Yêu cầu sinh viên bổ sung thông tin hoặc tài liệu.
- Sinh viên bổ sung thông tin hoặc tài liệu.
- Chuyển người/phòng ban xử lý.
- Escalation.
- Ghi nhận kết quả xử lý.
- Mở lại Ticket.
- Đóng Ticket.

Mỗi bản ghi lịch sử phải xác định được Ticket liên quan, nội dung sự kiện, người hoặc hệ thống thực hiện và thời điểm phát sinh.

---

## 4. Đánh Giá Hài Lòng (Ticket Rating)

Đánh giá hài lòng ghi nhận phản hồi của sinh viên sau khi Ticket đã có kết quả xử lý và đáp ứng điều kiện đánh giá.

| Thông tin | Bắt buộc | Ý nghĩa nghiệp vụ |
| :--- | :---: | :--- |
| **Ticket liên quan** | Có | Ticket được sinh viên đánh giá. |
| **Sinh viên đánh giá** | Có | Sinh viên sở hữu Ticket và thực hiện đánh giá. |
| **Điểm đánh giá** | Có | Điểm hài lòng theo thang từ **1 đến 5 sao**. |
| **Nội dung phản hồi** | Không | Ý kiến hoặc góp ý bổ sung của sinh viên về kết quả và chất lượng hỗ trợ. |
| **Thời điểm đánh giá** | Có | Thời điểm đánh giá được ghi nhận. |

Điều kiện, thời hạn và số lần được phép đánh giá được quy định tại `business-rules.md`.

---

## 5. Quan Hệ Nghiệp Vụ Chính

- Một **Sinh viên** có thể tạo nhiều Ticket.
- Mỗi **Ticket** thuộc về một Sinh viên.
- Mỗi **Ticket** được gắn với một nhóm vấn đề và một phòng ban phụ trách tại một thời điểm.
- Một **Ticket** có thể có hoặc chưa có người phụ trách tùy theo giai đoạn xử lý.
- Một **Ticket** có thể có nhiều file đính kèm và nhiều bản ghi lịch sử xử lý.
- Mỗi **Ticket** chỉ có tối đa một đánh giá hài lòng.
- Việc chuyển xử lý, mở lại hoặc thay đổi trạng thái không làm mất lịch sử của các giai đoạn xử lý trước đó.
