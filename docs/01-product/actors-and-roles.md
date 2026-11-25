# Các Vai Trò Trong Hệ Thống (Actors & Roles)

## 1. Danh Sách Vai Trò

UniSupport có **3 nhóm người dùng chính**, tương ứng với 3 phân hệ của sản phẩm:

```text
                    UNISUPPORT
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
    SINH VIÊN       NHÂN VIÊN        QUẢN LÝ
     Student           Staff          Management
```

Các chức năng quản trị hệ thống thuộc phạm vi của phân hệ **Management** và được phân quyền cho các tài khoản Quản lý phù hợp.

---

## 2. Vai Trò & Trách Nhiệm Chính

### 2.1 Sinh viên (Student)

**Mô tả**  
Người dùng gửi yêu cầu hỗ trợ và theo dõi quá trình xử lý các yêu cầu của chính mình.

**Khả năng chính**
- Đăng nhập hệ thống.
- Tra cứu hướng dẫn/FAQ.
- Tạo và gửi Ticket hỗ trợ.
- Chọn nhóm vấn đề và cung cấp nội dung, tài liệu liên quan.
- Xem trạng thái, lịch sử cập nhật và đơn vị/người phụ trách.
- Bổ sung thông tin hoặc giấy tờ khi được yêu cầu.
- Nhận thông báo và xem kết quả xử lý.
- Phản hồi nếu kết quả chưa giải quyết được vấn đề.
- Đánh giá mức độ hài lòng sau khi yêu cầu được giải quyết.

**Phạm vi dữ liệu**
- Chỉ được truy cập các Ticket và dữ liệu thuộc chính tài khoản sinh viên đó.

### 2.2 Nhân viên (Staff)

**Mô tả**  
Nhân viên thuộc các phòng ban chịu trách nhiệm tiếp nhận và xử lý Ticket hỗ trợ sinh viên.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem, tìm kiếm và lọc các yêu cầu trong phạm vi được phép.
- Tiếp nhận và phân loại Ticket.
- Xử lý các Ticket được giao.
- Xác định mức độ ưu tiên và theo dõi thời hạn xử lý.
- Cập nhật trạng thái và ghi nhận hoạt động xử lý.
- Yêu cầu sinh viên bổ sung thông tin hoặc giấy tờ.
- Phân công/phân công lại người phụ trách trong cùng phòng ban khi được cấp quyền.
- Chuyển Ticket sang phòng ban phù hợp hoặc thực hiện chuyển cấp xử lý khi cần thiết và được cấp quyền.
- Ghi nhận kết quả xử lý và chuyển Ticket sang `RESOLVED`.
- Tiếp tục xử lý Ticket khi sinh viên mở lại hợp lệ về `IN_PROGRESS`.

**Phạm vi dữ liệu**
- Chỉ được truy cập và thao tác trên Ticket trong phạm vi phòng ban, nhiệm vụ và quyền được cấp.

### 2.3 Quản lý (Management)

**Mô tả**  
Người dùng chịu trách nhiệm giám sát hoạt động hỗ trợ và thực hiện các chức năng quản lý/quản trị được cấp quyền.

**Khả năng chính**
- Đăng nhập hệ thống.
- Xem Dashboard và số liệu tổng hợp trong phạm vi được cấp.
- Theo dõi số lượng Ticket mới, đang xử lý, sắp quá hạn và đã quá hạn.
- Theo dõi khối lượng công việc theo phòng ban hoặc nhân viên.
- Xem báo cáo về loại yêu cầu, thời gian xử lý và mức độ hài lòng.
- Quản lý tài khoản, vai trò và quyền khi được cấp quyền quản trị.
- Quản lý phòng ban và danh mục Ticket.
- Tra soát Audit Trail và các thay đổi quan trọng.
- Quản lý thời hạn lưu trữ dữ liệu theo chính sách của hệ thống.
- Xuất dữ liệu/báo cáo theo chức năng được cung cấp.

**Phạm vi dữ liệu**
- Truy cập dữ liệu và chức năng theo phạm vi quyền được cấp.
- Các chức năng quản trị chỉ được sử dụng bởi tài khoản Management có quyền phù hợp.

---

## 3. Ma Trận Quyền Theo Nhóm Người Dùng

Ma trận dưới đây mô tả phạm vi chức năng chính của từng nhóm người dùng trong UniSupport.

| Chức năng / Hành động | Sinh viên | Nhân viên | Quản lý |
| :--- | :---: | :---: | :---: |
| Đăng nhập hệ thống | Được phép | Được phép | Được phép |
| Tra cứu FAQ/hướng dẫn | Được phép | Không áp dụng | Không áp dụng |
| Tạo và gửi Ticket | Được phép | Không áp dụng | Không áp dụng |
| Xem Ticket | Ticket của mình | Theo phạm vi phụ trách | Theo phạm vi quản lý |
| Tiếp nhận và xử lý Ticket | Không áp dụng | Theo nhiệm vụ/phạm vi | Chỉ tiếp nhận cho Staff khi được cấp quyền; không ghi kết quả |
| Phân loại Category | Không áp dụng | Người phụ trách hoặc khi được phân quyền | Khi được phân quyền |
| Thay đổi Priority | Không áp dụng | Người phụ trách hoặc khi được phân quyền | Khi được phân quyền |
| Tiếp nhận Ticket chưa có người phụ trách | Không áp dụng | Được phép trong phạm vi phòng ban | Khi được phân quyền |
| Phân công / phân công lại | Không áp dụng | Khi được phân quyền | Khi được phân quyền |
| Transfer sang phòng ban khác | Không áp dụng | Khi được phân quyền | Khi được phân quyền |
| Escalation tới Management | Không áp dụng | Khi được phân quyền | Không áp dụng |
| Yêu cầu sinh viên bổ sung thông tin | Không áp dụng | Người phụ trách hoặc khi được phân quyền | Không áp dụng |
| Bổ sung thông tin theo yêu cầu | Được phép | Không áp dụng | Không áp dụng |
| Ghi nhận kết quả và chuyển `RESOLVED` | Không áp dụng | Người phụ trách hoặc khi được phân quyền | Không áp dụng |
| Xác nhận kết quả / yêu cầu mở lại | Được phép | Không áp dụng | Không áp dụng |
| Đánh giá mức độ hài lòng | Được phép | Không áp dụng | Không áp dụng |
| Xem Dashboard và báo cáo | Không áp dụng | Không áp dụng | Được phép |
| Quản lý tài khoản và phân quyền | Không áp dụng | Không áp dụng | Được phép |
| Quản lý phòng ban và danh mục | Không áp dụng | Không áp dụng | Được phép |
| Xem Audit Trail | Không áp dụng | Không áp dụng | Được phép |
| Quản lý thời hạn lưu trữ dữ liệu | Không áp dụng | Không áp dụng | Được phép |
| Xuất báo cáo / dữ liệu | Không áp dụng | Không áp dụng | Được phép |

> **Quy ước:**  
> **Được phép**: chức năng thuộc trách nhiệm chính của nhóm; quyền quản trị/xuất dữ liệu vẫn phải được cấp theo mục 4, không mặc nhiên theo tên nhóm.
> **Không áp dụng**: chức năng không thuộc phạm vi sử dụng của nhóm.  
> **Khi được phân quyền**: chỉ được thực hiện khi tài khoản có quyền phù hợp với vai trò và phạm vi trách nhiệm.

> **Quy tắc vòng đời:** Sinh viên xác nhận kết quả hoặc yêu cầu mở lại trong giai đoạn `RESOLVED`; hệ thống tự động đóng Ticket khi hết thời hạn phản hồi. Staff không có thao tác đóng hoặc mở lại Ticket độc lập với các quy tắc này.

> Chi tiết quyền theo dữ liệu, trạng thái Ticket và từng hành động được đặc tả trong phần Domain, Functional Requirements, Workflows và Security.

## 4. Danh Mục Quyền Chức Năng Hữu Hạn

Ba nhóm `STUDENT`, `STAFF`, `MANAGEMENT` cố định; không tạo role, nhóm hoặc quyền tùy ý. Quyền dưới đây là cờ cấp/thu hồi **trên tài khoản**, dùng cơ chế phân quyền sẵn có, không phải phân hệ mới.

| Mã quyền | Nhóm đủ điều kiện | Hành động được ủy quyền trong phạm vi dữ liệu hiện có |
| --- | --- | --- |
| `TICKET_ASSIGN` | STAFF, MANAGEMENT | Tiếp nhận cho Staff hợp lệ; phân công/phân công lại Staff trong phòng ban xử lý |
| `CATEGORY_OVERRIDE` | STAFF, MANAGEMENT | Phân loại thay người phụ trách; đổi phòng ban phải dùng Transfer |
| `PRIORITY_OVERRIDE` | STAFF, MANAGEMENT | Đổi ưu tiên thay người phụ trách |
| `SUPPLEMENT_OVERRIDE` | STAFF | Yêu cầu bổ sung thay người phụ trách |
| `RESOLVE_OVERRIDE` | STAFF | Ghi kết quả và chuyển `RESOLVED` thay người phụ trách |
| `TICKET_TRANSFER` | STAFF, MANAGEMENT | Transfer theo Category/phòng ban hợp lệ |
| `ESCALATION_SEND` | STAFF | Gửi escalation nội bộ |
| `ESCALATION_RECEIVE` | MANAGEMENT | Được chọn làm người nhận escalation trong phạm vi |
| `ACCOUNT_MANAGE` | MANAGEMENT | Tạo/cập nhật/khóa/mở khóa, gán nhóm/phạm vi và cấp/thu hồi các quyền hữu hạn |
| `CATALOGUE_MANAGE` | MANAGEMENT | Quản lý phòng ban và Category |
| `AUDIT_READ` | MANAGEMENT | Tra cứu audit theo phạm vi (giao diện MS-05) |
| `RETENTION_MANAGE` | MANAGEMENT | Cấu hình chính sách lưu trữ cơ bản |
| `REPORT_EXPORT` | MANAGEMENT | Xuất báo cáo trong phạm vi |

**Mặc định:** tài khoản mới không có cờ quyền bổ sung nào. Student có quyền cơ sở với Ticket của mình; Staff có quyền cơ sở xem hàng chờ/tiếp nhận Ticket chưa gán trong phòng ban và xử lý Ticket mình phụ trách (phân loại, ưu tiên, ghi chú nội bộ, yêu cầu bổ sung, ghi kết quả); Management có quyền cơ sở xem Ticket/Dashboard/báo cáo trong phạm vi, không mặc nhiên có quyền quản trị hoặc xuất dữ liệu. Quyền cơ sở không phải quyền ủy quyền: Staff là assignee không mặc nhiên có `TICKET_ASSIGN`, `TICKET_TRANSFER`, `ESCALATION_SEND` hay quyền xử lý thay người khác. Management dùng `TICKET_ASSIGN` để tiếp nhận cho Staff hợp lệ theo FR-STF-02, không trở thành assignee.

**Từ chối mặc định:** ngoài quyền cơ sở nêu trên, thiếu cờ, sai nhóm, ngoài phạm vi, tài khoản bị khóa hoặc trạng thái không hợp lệ đều bị từ chối ở backend; ẩn nút không thay thế kiểm tra API. Không có cờ `CLOSE`/`REOPEN`: chỉ Student sở hữu xác nhận/mở lại theo thời hạn; hệ thống tự đóng sau 03 ngày làm việc. Chỉ Staff hợp lệ được ghi kết quả/chuyển `RESOLVED`; Management không được làm việc này.

**Cấp/thu hồi:** Management có `ACCOUNT_MANAGE` chọn tài khoản trong phạm vi, xem cờ hiện tại, cấp/thu hồi từ danh mục rồi lưu; backend kiểm tra lại và lưu nguyên tử, ghi audit trước/sau + tác nhân + thời điểm. Cờ mới có hiệu lực ở yêu cầu được bảo vệ tiếp theo, kể cả phiên đang mở. Khi đổi nhóm, loại các cờ không còn đủ điều kiện trong cùng giao dịch. Không tự tăng quyền/phạm vi; không cấp vượt **thẩm quyền quản trị** của người thực hiện; phạm vi đích không vượt phạm vi người cấp. `ACCOUNT_MANAGE` bao gồm thẩm quyền cấp/thu hồi các cờ dành cho STAFF trong phạm vi (không cho người quản trị dùng các chức năng Staff). Với cờ đủ điều kiện MANAGEMENT, người cấp phải đang có chính cờ đó; không tự cấp cờ mình thiếu. Đây là danh mục ủy quyền cố định, không có cấu hình chính sách ủy quyền tùy ý. Thu hồi, hạ nhóm/phạm vi hoặc khóa không được làm mất tài khoản Management đang hoạt động cuối cùng có `ACCOUNT_MANAGE` và phạm vi toàn trường; quản trị phòng ban không thay thế quản trị toàn trường. Tài khoản quản trị toàn trường ban đầu có các cờ đủ điều kiện MANAGEMENT trong danh mục và được nạp khi triển khai, không phát sinh chức năng bootstrap mới.

**Giới hạn xác nhận:** đây là làm rõ quyền sẵn có trong FR-MGT-01, không thêm task, role builder hay quy trình phê duyệt nhiều tầng. BA/TL cần xác nhận danh mục, mặc định và khả năng nằm trong effort hiện hữu trước gửi; nếu vượt effort phải trình CR, không tự giữ giá bằng cách bỏ kiểm soát quyền.
