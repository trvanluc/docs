# [WF-01] Sinh viên gửi yêu cầu hỗ trợ (Submit Support Request)

### [FR-STU-02] Sinh viên gửi yêu cầu hỗ trợ

**Mô tả**
Hệ thống cho phép sinh viên tạo một Ticket hỗ trợ bằng cách chọn nhóm vấn đề, nhập nội dung mô tả tình huống, đính kèm tệp tài liệu (ảnh hoặc PDF nếu cần) và gửi yêu cầu đến bộ phận phụ trách của Aurora University.

**Actor**
Sinh viên đã đăng nhập vào hệ thống.

**Preconditions**
- Sinh viên đã đăng nhập thành công vào hệ thống UniSupport.
- Sinh viên có quyền tạo Ticket hỗ trợ.

**Luồng chính**
1. Sinh viên mở chức năng **Tạo Ticket**.
2. Hệ thống hiển thị form tạo Ticket.
3. Sinh viên chọn **Nhóm vấn đề** (Category) từ danh mục ADMIN quản lý; mỗi nhóm gắn phòng ban mặc định.
4. Sinh viên nhập các thông tin bắt buộc, bao gồm tiêu đề và **Mô tả vấn đề**.
5. Sinh viên đính kèm tệp tài liệu (ảnh JPG/JPEG/PNG hoặc tệp PDF) nếu cần.
6. Sinh viên chọn **Gửi yêu cầu**.
7. Hệ thống kiểm tra tính hợp lệ của dữ liệu đầu vào và tệp đính kèm.
8. Nếu dữ liệu hợp lệ, hệ thống khởi tạo Ticket mới, tự động sinh mã Ticket duy nhất và gán trạng thái ban đầu là `NEW` (Mới tạo).
9. Hệ thống hiển thị thông báo tạo Ticket thành công, cung cấp mã Ticket cho sinh viên và gửi thông báo nội bộ hệ thống.

**Business Rules**
- Nhóm vấn đề, tiêu đề (10–150 ký tự) và mô tả (20–2000 ký tự) là các thông tin bắt buộc theo FR-STU-02.
- Nội dung mô tả chỉ chứa khoảng trắng được xem là không hợp lệ.
- Tệp đính kèm hỗ trợ PDF, PNG, JPG, JPEG; tối đa 5 tệp, 5MB/tệp theo FR-STU-02.
- Một thao tác gửi của sinh viên chỉ được tạo tối đa **một Ticket**, kể cả khi yêu cầu bị gửi nhiều lần do double-click, retry hoặc vấn đề mạng.
- Ticket sau khi được tạo phải được liên kết chính xác với tài khoản sinh viên đã gửi yêu cầu.

**Alternative / Error Flows**
- **Thiếu thông tin bắt buộc:** Hệ thống không tạo Ticket, hiển thị thông báo lỗi validation chi tiết tại từng trường thông tin.
- **Tệp đính kèm không hợp lệ (sai định dạng hoặc vượt dung lượng):** Hệ thống chặn gửi, báo lỗi tệp không hợp lệ và yêu cầu chọn lại.
- **Lỗi hệ thống trong quá trình tạo:** Hệ thống thông báo lỗi và không tạo Ticket ở trạng thái dữ liệu không hoàn chỉnh (rollback).
- **Trùng lặp request do kết nối:** Nếu cùng một request được gửi lại do retry/network retry, hệ thống không tạo thêm Ticket trùng lặp.

**Acceptance Criteria**
- **AC-01:** Sinh viên chọn nhóm vấn đề, nhập đầy đủ thông tin hợp lệ và chọn **Gửi yêu cầu** -> Hệ thống tạo đúng một Ticket, sinh mã Ticket duy nhất và hiển thị thông báo thành công.
- **AC-02:** Sinh viên để trống trường mô tả hoặc nhóm vấn đề -> Hệ thống không tạo Ticket và hiển thị lỗi validation.
- **AC-03:** Sinh viên nhập nội dung chỉ gồm khoảng trắng -> Hệ thống không tạo Ticket.
- **AC-04:** Sinh viên tải lên tệp đính kèm đúng chuẩn (.pdf, .jpg, .jpeg, .png) -> Hệ thống lưu trữ tệp và gắn liên kết vào Ticket.
- **AC-05:** Sinh viên tải lên tệp sai định dạng (ví dụ .docx, .zip) -> Hệ thống từ chối tệp và báo lỗi.
- **AC-06:** Sinh viên nhấn nút **Gửi yêu cầu** nhiều lần liên tiếp -> Hệ thống chỉ tạo một Ticket duy nhất.
- **AC-07:** Ticket được tạo phải lưu đúng thông tin sinh viên gửi yêu cầu và gửi thông báo xác nhận.

**Ví dụ Edge Case**
Sinh viên nhấn nút **Gửi yêu cầu** 5 lần liên tiếp trong thời gian ngắn do mạng giật lag.

**Expected Result:** Hệ thống chỉ ghi nhận **một Ticket duy nhất** cho thao tác gửi đó, loại bỏ 4 request trùng lặp còn lại.
