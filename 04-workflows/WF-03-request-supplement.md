# [WF-03] Yêu cầu bổ sung thông tin/giấy tờ (Request Supplement)

### [FR-STF-04 / FR-STU-03] Nhân viên yêu cầu bổ sung hồ sơ & Sinh viên phản hồi

**Mô tả**
Trong quá trình xử lý, nếu thông tin hoặc tài liệu sinh viên cung cấp bị thiếu hoặc chưa đủ cơ sở giải quyết, nhân viên có thể gửi yêu cầu sinh viên bổ sung thêm thông tin hoặc giấy tờ.

**Actor**
- Nhân viên phụ trách xử lý Ticket (Staff).
- Sinh viên gửi Ticket (Student).

**Preconditions**
- Ticket đang ở trạng thái `IN_PROGRESS` (Đang xử lý).
- Nhân viên thực hiện là người đang phụ trách Ticket đó.

**Luồng chính**
1. Nhân viên mở chi tiết Ticket đang xử lý và chọn chức năng **Yêu cầu bổ sung thông tin**.
2. Hệ thống hiển thị form nhập nội dung cần bổ sung.
3. Nhân viên nhập mô tả chi tiết các giấy tờ/thông tin sinh viên cần cung cấp thêm và nhấn **Gửi yêu cầu**.
4. Hệ thống chuyển trạng thái Ticket sang `NEED_MORE_INFO` (Cần bổ sung) và gửi thông báo nội bộ tới sinh viên.
5. Sinh viên nhận được thông báo, truy cập vào Ticket xem yêu cầu bổ sung.
6. Sinh viên nhập nội dung phản hồi và/hoặc tải lên tệp đính kèm bổ sung (ảnh/PDF).
7. Sinh viên nhấn **Xác nhận bổ sung**.
8. Hệ thống kiểm tra dữ liệu, cập nhật thông tin bổ sung vào Ticket, tự động chuyển trạng thái Ticket trở lại `IN_PROGRESS` (Đang xử lý) và thông báo cho nhân viên phụ trách.

**Business Rules**
- Ticket ở NEED_MORE_INFO để chờ sinh viên bổ sung. Không tự chốt thêm cơ chế dừng/tính lại SLA trong quy trình này; thời hạn giữ theo FR-MNG-02/BR-10 đã có.
- Chỉ có sinh viên chủ sở hữu Ticket mới có quyền tải tệp bổ sung hoặc gửi phản hồi.
- Tệp đính kèm bổ sung phải tuân thủ đúng định dạng hợp lệ (.pdf, .jpg, .jpeg, .png), tối đa 5 tệp, 5MB/tệp theo FR-STU-03.

**Alternative / Error Flows**
- **Sinh viên gửi phản hồi rỗng:** Hệ thống từ chối cập nhật và yêu cầu sinh viên phải nhập thông tin hoặc đính kèm tệp trước khi gửi.
- **Sinh viên gửi tệp đính kèm không đúng định dạng:** Hệ thống chặn và báo lỗi tệp không hợp lệ.

**Acceptance Criteria**
- **AC-01:** Nhân viên gửi yêu cầu bổ sung -> Ticket chuyển trạng thái thành `NEED_MORE_INFO`, sinh viên nhận được thông báo.
- **AC-02:** Sinh viên nhập nội dung phản hồi và đính kèm file hợp lệ -> Ticket chuyển lại trạng thái `Đang xử lý`, nhân viên nhận được thông báo.
- **AC-03:** Sinh viên bấm gửi phản hồi nhưng không nhập nội dung và không đính kèm file -> Hệ thống báo lỗi validation.
- **AC-04:** Sinh viên khác (không phải người tạo Ticket) tìm cách truy cập và nộp file bổ sung -> Hệ thống từ chối quyền truy cập (HTTP 403 Forbidden).

**Ví dụ Edge Case**
Sinh viên đính kèm file hình ảnh bị hỏng hoặc chọn nhầm file đuôi `.exe` khi phản hồi yêu cầu bổ sung của nhân viên.

**Expected Result:** Hệ thống kiểm tra định dạng tệp, từ chối tải lên file `.exe`, hiển thị thông báo lỗi "Chỉ chấp nhận định dạng PDF, JPG, JPEG, PNG" và giữ nguyên trạng thái Ticket là `NEED_MORE_INFO`.
