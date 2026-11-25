# Phân Hệ Quản Lý (M03 - Management Dashboard)

## I. TỔNG QUAN PHÂN HỆ

Phân hệ **Management Dashboard** cho phép người dùng Quản lý giám sát hoạt động hỗ trợ sinh viên, xem báo cáo và thực hiện các chức năng quản trị trong phạm vi quyền được cấp.

- **Actor chính:** Quản lý (Management).
- **Phạm vi quản lý:** Mỗi tài khoản Quản lý được cấu hình ở phạm vi **toàn trường** hoặc **một phòng ban cụ thể**. Mọi dữ liệu hiển thị và thao tác phải giới hạn theo phạm vi này.
- **Phạm vi quyền:** Không phải mọi tài khoản Quản lý đều mặc định có toàn bộ chức năng quản trị; mỗi chức năng phải kiểm tra quyền tương ứng.
- **Vai trò hệ thống:** UniSupport sử dụng ba nhóm người dùng chính: Sinh viên, Nhân viên và Quản lý.
- **Tác động lên Ticket:** Việc xem Dashboard, báo cáo hoặc tra soát không làm thay đổi trạng thái Ticket. Quản lý chỉ tham gia thao tác xử lý Ticket khi được phân quyền theo ma trận vai trò/quyền dùng chung.

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-MGT-00] Đăng nhập và truy cập Management Dashboard

**Priority:** Cao: mọi chức năng quản trị và giám sát cần đăng nhập theo phạm vi. **Mốc giao:** MS-01.

#### 1. Mô tả & Phạm vi
Cho phép người dùng Management đăng nhập UniSupport và truy cập các chức năng quản lý đúng với phạm vi quyền được cấp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Quản lý (Management).
- **Preconditions:** Tài khoản tồn tại, đang hoạt động và có vai trò Management.

#### 3. Quy tắc Dữ liệu & Validation
- **Tên đăng nhập:** bắt buộc, sử dụng tài khoản do nhà trường cấp.
- **Mật khẩu:** bắt buộc.
- Không chấp nhận dữ liệu chỉ chứa khoảng trắng.
- Sau khi đăng nhập, hệ thống chỉ hiển thị chức năng và dữ liệu nằm trong quyền và phạm vi quản lý của tài khoản.

#### 4. Luồng xử lý chi tiết
1. Người dùng truy cập UniSupport.
2. Hệ thống yêu cầu đăng nhập nếu chưa có phiên hợp lệ.
3. Người dùng nhập thông tin đăng nhập.
4. Hệ thống xác thực tài khoản, trạng thái hoạt động, vai trò và phạm vi quyền.
5. Nếu hợp lệ, hệ thống cho phép truy cập Management Dashboard.
6. Dashboard và các chức năng quản trị được hiển thị theo đúng quyền của tài khoản.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Thông tin đăng nhập không hợp lệ: từ chối truy cập.
- Tài khoản bị khóa hoặc vô hiệu hóa: không tạo phiên đăng nhập.
- Tài khoản không có vai trò Management: không cho truy cập Management Dashboard.
- Phiên hết hạn: yêu cầu xác thực lại.

#### 6. Quy tắc nghiệp vụ
- Quản lý phạm vi toàn trường được xem dữ liệu toàn trường theo quyền chức năng được cấp.
- Quản lý phạm vi phòng ban chỉ được xem dữ liệu thuộc phòng ban được cấu hình.
- Quyền truy cập tuân thủ [Actors & Roles](../../01-product/actors-and-roles.md).

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-00/AC-01:** Tài khoản Management hợp lệ đăng nhập thành công và được đưa vào Management Dashboard.
- **FR-MGT-00/AC-02:** Tài khoản không có vai trò Management mở Management Dashboard: hiển thị trang "không có quyền truy cập".
- **FR-MGT-00/AC-03:** Chức năng quản trị không thuộc quyền của tài khoản không hiển thị trên menu; gọi trực tiếp tới hệ thống bị từ chối với thông báo "không có quyền thực hiện".
- **FR-MGT-00/AC-04:** Dữ liệu ngoài phạm vi quản lý không được hiển thị hoặc mở trực tiếp bằng đường dẫn.
- **FR-MGT-00/AC-05:** Sai thông tin đăng nhập hoặc tài khoản bị khóa: thông báo tương ứng ("thông tin đăng nhập không đúng" / "tài khoản đã bị khóa"), không tạo phiên.
- **FR-MGT-00/AC-06:** Phiên hết hạn: thao tác tiếp theo đưa người dùng về màn hình đăng nhập kèm thông báo "phiên đã hết hạn"; dữ liệu chưa lưu không được ghi.
- **FR-MGT-00/AC-07:** Quản lý phạm vi toàn trường thấy dữ liệu mọi phòng ban; quản lý phạm vi một phòng ban chỉ thấy dữ liệu phòng ban đó trên mọi màn hình (Dashboard, báo cáo, tra soát).

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Quản lý phạm vi phòng ban** đăng nhập: chỉ thấy dữ liệu và chức năng của phòng ban đó.
- **A2 — Quản lý không có quyền quản trị tài khoản:** đăng nhập được nhưng không thấy menu Quản lý tài khoản.

#### 9. Ví dụ Edge Case
- Quản lý bị đổi phạm vi từ toàn trường sang một phòng ban khi đang đăng nhập: lần tải tiếp theo áp dụng phạm vi mới.
- Gọi trực tiếp API quản trị bằng tài khoản không có quyền: bị từ chối (FR-MGT-00/AC-03).

---

### [FR-MGT-01] Quản lý tài khoản, vai trò và phạm vi quyền

**Priority:** Cao: cần tài khoản và vai trò đúng trước khi kiểm thử mọi luồng khác. **Mốc giao:** MS-01.

#### 1. Mô tả & Phạm vi
Cho phép Management có quyền quản trị tạo và cập nhật tài khoản, khóa/mở khóa tài khoản, gán nhóm người dùng và xác định phạm vi phòng ban/quyền phù hợp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Management có quyền quản lý tài khoản và phân quyền.
- **Preconditions:** Người dùng đã đăng nhập và có quyền quản trị tài khoản.

#### 3. Quy tắc Dữ liệu & Validation
- **Tên đăng nhập/Mã định danh:** bắt buộc và duy nhất trong hệ thống.
- **Họ tên:** bắt buộc.
- **Nhóm người dùng:** bắt buộc chọn một trong Sinh viên (`STUDENT`), Nhân viên (`STAFF`) hoặc Quản lý (`MANAGEMENT`).
- **Trạng thái tài khoản:** đang hoạt động hoặc bị khóa.
- **Mật khẩu khởi tạo:** bắt buộc khi tạo tài khoản mới; do người có quyền quản lý tài khoản thiết lập và bàn giao cho người dùng theo quy trình của nhà trường.
- Tài khoản Nhân viên phải được gắn với **một phòng ban đang hoạt động**.
- Tài khoản Quản lý phải được xác định phạm vi **toàn trường** hoặc **một phòng ban đang hoạt động**.
- **Lý do khóa tài khoản:** bắt buộc, từ **10 đến 500 ký tự**.
- Người thực hiện không được tự khóa chính tài khoản đang đăng nhập.
- Hệ thống phải luôn còn ít nhất **một tài khoản Quản lý toàn trường đang hoạt động có ACCOUNT_MANAGE**.
- Người quản trị không được cấp cho tài khoản khác quyền hoặc phạm vi quản lý vượt quá thẩm quyền/phạm vi mà chính mình được phép quản lý.

- Quyền chức năng được cấp/thu hồi trên tài khoản từ [danh mục hữu hạn, nhóm đủ điều kiện và mặc định](../../01-product/actors-and-roles.md#4-danh-mục-quyền-chức-năng-hữu-hạn); không tạo role tùy ý. Mặc định không có cờ bổ sung. Quyền cơ sở của assignee không phải quyền ủy quyền. ACCOUNT_MANAGE được ủy quyền cố định để cấp/thu hồi cờ STAFF trong phạm vi, không được sử dụng chúng; cờ MANAGEMENT chỉ được cấp khi chính người cấp đang có cờ đó.

#### 4. Luồng xử lý chi tiết

**Luồng A — Tạo tài khoản**
1. Management mở chức năng **Quản lý tài khoản**.
2. Hệ thống hiển thị danh sách tài khoản trong phạm vi được phép quản trị.
3. Người dùng chọn **Tạo tài khoản**.
4. Người dùng nhập thông tin bắt buộc, thiết lập mật khẩu khởi tạo, chọn nhóm người dùng và cấu hình phòng ban/phạm vi nếu cần.
5. Hệ thống kiểm tra dữ liệu, tính duy nhất, phạm vi được phép cấp và quyền thao tác.
6. Hệ thống tạo tài khoản ở trạng thái hoạt động.
7. Hệ thống ghi nhận thao tác vào nhật ký tra soát.

**Luồng B — Cập nhật vai trò/phạm vi**
1. Management chọn một tài khoản được phép quản trị.
2. Hệ thống hiển thị thông tin hiện tại.
3. Người dùng thay đổi nhóm người dùng, phòng ban hoặc phạm vi quyền.
4. Hệ thống kiểm tra cấu hình mới, bảo đảm người thực hiện không cấp quyền vượt quá phạm vi của mình và thao tác không làm mất toàn bộ tài khoản Quản lý toàn trường đang hoạt động có ACCOUNT_MANAGE.
5. Nếu hợp lệ, hệ thống lưu thay đổi và áp dụng phạm vi quyền mới.
6. Hệ thống ghi nhận giá trị trước/sau và người thực hiện vào nhật ký tra soát.

**Luồng D — Cấp/thu hồi quyền chức năng**
1. Management có `ACCOUNT_MANAGE` mở tài khoản trong phạm vi; chọn cấp/thu hồi từng cờ của danh mục cố định.
2. Backend kiểm nhóm đủ điều kiện, quyền/phạm vi người cấp, cấm tự tăng quyền và bảo vệ quản trị toàn trường cuối cùng.
3. Lưu nguyên tử quyền trước/sau và audit; yêu cầu được bảo vệ tiếp theo của phiên đang mở dùng quyền mới. Đổi nhóm đồng thời loại cờ không còn hợp lệ.
4. Thiếu quyền, mã lạ, sai nhóm hoặc vi phạm giới hạn: thông báo lý do; không lưu thay đổi.

**Luồng C — Khóa hoặc mở khóa**
1. Management chọn tài khoản.
2. Người dùng chọn khóa hoặc mở khóa và nhập lý do.
3. Hệ thống kiểm tra quyền, điều kiện thao tác và bảo đảm việc khóa không làm mất tài khoản Quản lý toàn trường đang hoạt động cuối cùng có ACCOUNT_MANAGE.
4. Khi khóa tài khoản Nhân viên, hệ thống kiểm tra các Ticket chưa hoàn tất mà tài khoản đang là người phụ trách chính. Nếu có Ticket ở `NEW`, `IN_PROGRESS` hoặc `WAITING_STUDENT`, hệ thống gỡ người phụ trách hiện tại và đưa các Ticket đó về hàng chờ chưa có người phụ trách của phòng ban đang xử lý để được phân công lại.
5. Hệ thống khóa tài khoản ngay sau khi hoàn tất việc cập nhật trách nhiệm xử lý Ticket.
6. Hệ thống ghi nhận lý do khóa, các Ticket bị ảnh hưởng và người thực hiện vào nhật ký tra soát.
7. Với thao tác mở khóa, hệ thống cập nhật tài khoản về trạng thái hoạt động nhưng không tự động gán lại các Ticket đã được đưa về hàng chờ trước đó.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Tên đăng nhập/Mã định danh đã tồn tại: từ chối tạo mới.
- Tài khoản Nhân viên không có phòng ban hợp lệ: từ chối lưu.
- Người dùng cố tự khóa tài khoản đang đăng nhập: từ chối.
- Thao tác khóa/hạ quyền sẽ làm hệ thống không còn tài khoản Quản lý toàn trường đang hoạt động có ACCOUNT_MANAGE: từ chối.
- Người thực hiện cố cấp quyền hoặc phạm vi vượt quá thẩm quyền/phạm vi được phép quản trị của chính mình: từ chối.
- Người dùng không có quyền quản trị tài khoản: từ chối thao tác.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ ma trận quyền tại [Actors & Roles](../../01-product/actors-and-roles.md).
- Thay đổi quyền/phạm vi không làm thay đổi lịch sử các Ticket trước đó.
- Khóa tài khoản Nhân viên có hiệu lực ngay sau khi các Ticket đang được gán cho tài khoản đó được gỡ người phụ trách và đưa về hàng chờ của phòng ban hiện tại.
- Việc khóa tài khoản không làm thay đổi phòng ban hoặc trạng thái nghiệp vụ của Ticket.
- Hệ thống luôn phải còn ít nhất một tài khoản Quản lý toàn trường đang hoạt động có ACCOUNT_MANAGE.
- Người quản trị chỉ được cấp quyền trong giới hạn thẩm quyền và phạm vi quản lý của chính mình.
- Tạo, thay đổi quyền, khóa và mở khóa tài khoản đều phải được ghi nhận để tra soát.

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-01/AC-01:** Tài khoản hợp lệ được tạo ở trạng thái hoạt động với đúng nhóm người dùng, phạm vi và mật khẩu khởi tạo.
- **FR-MGT-01/AC-02:** Tên đăng nhập/Mã định danh đã tồn tại (không phân biệt hoa thường): không tạo tài khoản, thông báo "tên đăng nhập đã tồn tại", số tài khoản không đổi.
- **FR-MGT-01/AC-03:** Tài khoản Nhân viên không gắn phòng ban đang hoạt động: không lưu, thông báo tại trường phòng ban.
- **FR-MGT-01/AC-04:** Khóa Nhân viên đang phụ trách Ticket hợp lệ sẽ gỡ người phụ trách và đưa các Ticket liên quan về hàng chờ của phòng ban trước khi tài khoản bị khóa.
- **FR-MGT-01/AC-05:** Khóa hoặc hạ quyền tài khoản Quản lý toàn trường đang hoạt động cuối cùng có ACCOUNT_MANAGE: bị từ chối với thông báo nêu lý do; tài khoản giữ nguyên trạng thái và quyền.
- **FR-MGT-01/AC-06:** Cấp quyền hoặc phạm vi vượt quá thẩm quyền/phạm vi quản trị của chính người thực hiện: bị từ chối với thông báo, quyền của tài khoản đích không đổi.
- **FR-MGT-01/AC-07:** Mọi lần tạo, thay đổi vai trò/phạm vi, khóa và mở khóa tài khoản được ghi trong nhật ký tra soát với giá trị trước/sau và người thực hiện.
- **FR-MGT-01/AC-08:** Người dùng không có thao tác khóa cho chính tài khoản đang đăng nhập; yêu cầu tự khóa gửi trực tiếp bị từ chối, tài khoản vẫn hoạt động.
- **FR-MGT-01/AC-09:** Người không có quyền quản trị tài khoản: người dùng không thấy thao tác này; nếu gửi trực tiếp tới hệ thống thì nhận thông báo "không có quyền thực hiện" và dữ liệu không đổi.
- **FR-MGT-01/AC-10:** Thay đổi quyền/phạm vi hoặc khóa tài khoản không làm thay đổi lịch sử, phòng ban hay trạng thái của Ticket (ngoài việc gỡ người phụ trách theo FR-MGT-01/AC-04).
- **FR-MGT-01/AC-11:** Lý do khóa rỗng, dưới 10 hoặc trên 500 ký tự: thông báo tại trường lý do, tài khoản không bị khóa.
- **FR-MGT-01/AC-12:** Mở khóa đưa tài khoản về trạng thái hoạt động nhưng không tự gán lại các Ticket đã được đưa về hàng chờ trước đó.
- **FR-MGT-01/AC-13:** Tài khoản mới chỉ có quyền cơ sở theo nhóm/phạm vi; danh sách cấp quyền chỉ chứa danh mục hữu hạn tại Actors & Roles mục 4; không có tạo role/quyền tùy ý.
- **FR-MGT-01/AC-14:** Cấp rồi thu hồi một cờ hợp lệ trong phạm vi được lưu cùng audit trước/sau, tác nhân và thời điểm; yêu cầu được bảo vệ tiếp theo của phiên đang mở áp dụng cờ mới, thu hồi làm thao tác ủy quyền bị từ chối, không làm mất lịch sử cũ.
- **FR-MGT-01/AC-15:** Mã quyền ngoài danh mục hoặc cấp cho nhóm không đủ điều kiện (Student có quyền quản trị, Management có RESOLVE_OVERRIDE): bị từ chối kèm lý do, dữ liệu không đổi; đổi nhóm loại cờ không tương thích nguyên tử.
- **FR-MGT-01/AC-16:** Hai tài khoản cùng nhóm/phạm vi nhưng khác cờ chỉ thực hiện được thao tác ủy quyền khi có cờ; thiếu cờ bị ẩn thao tác và gọi trực tiếp bị từ chối. Quyền assignee cơ sở không cho phép xử lý thay người khác hoặc bỏ qua trạng thái/phạm vi.
- **FR-MGT-01/AC-17:** Người cấp không được tự tăng quyền/phạm vi hoặc cấp cho người khác quyền vượt thẩm quyền/phạm vi được phép quản trị (bao gồm cờ MANAGEMENT người cấp đang thiếu); yêu cầu trực tiếp cũng bị từ chối kèm lý do, tài khoản đích giữ nguyên.
- **FR-MGT-01/AC-18:** Thu hồi ACCOUNT_MANAGE, hạ nhóm/phạm vi hoặc khóa quản trị toàn trường đang hoạt động cuối cùng bị từ chối nguyên tử kèm lý do; một quản trị phòng ban không được tính là quản trị toàn trường thay thế.

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (cập nhật vai trò/phạm vi) và Luồng C (khóa/mở khóa) ở mục 4 là các luồng thay thế của Luồng A (tạo tài khoản).
- **A1 — Mở khóa tài khoản Nhân viên:** tài khoản hoạt động lại nhưng không tự nhận lại Ticket cũ.

#### 9. Ví dụ Edge Case
- Khóa tài khoản Quản lý cuối cùng có quyền quản trị: bị từ chối (FR-MGT-01/AC-05).
- Lý do khóa 9 ký tự: từ chối; 500 ký tự: chấp nhận; 501: từ chối.
- Tên đăng nhập trùng nhưng khác hoa/thường (`sv001` và `SV001`): coi là trùng, bị từ chối.
- Khóa Nhân viên đang phụ trách 3 Ticket (`NEW`, `IN_PROGRESS`, `WAITING_STUDENT`): cả 3 về hàng chờ phòng ban, trạng thái giữ nguyên (FR-MGT-01/AC-04).

---

### [FR-MGT-02] Quản lý phòng ban và Nhóm vấn đề

**Priority:** Cao: Ticket cần Category và phòng ban tiếp nhận hợp lệ ngay từ lúc tạo. **Mốc giao:** MS-01.

#### 1. Mô tả & Phạm vi
Cho phép Management có quyền cấu hình quản lý danh sách phòng ban và **Nhóm vấn đề (Category)** dùng trong quá trình tạo, phân loại và chuyển xử lý Ticket.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Management có quyền quản lý cấu hình nghiệp vụ.
- **Preconditions:** Người dùng đã đăng nhập và có quyền quản lý phòng ban/Nhóm vấn đề.

#### 3. Quy tắc Dữ liệu & Validation
- **Phòng ban:** có tên duy nhất trong danh sách đang hoạt động.
- **Nhóm vấn đề (Category):**
  - Có tên hiển thị và trạng thái hoạt động.
  - Tên Category phải **duy nhất trong toàn bộ danh mục**, bao gồm cả Category đang hoạt động và đã vô hiệu hóa.
  - Nếu cần sử dụng lại tên của Category đã vô hiệu hóa, phải kích hoạt lại Category cũ thay vì tạo Category mới cùng tên.
  - Mỗi Category đang hoạt động phải được cấu hình với **một phòng ban tiếp nhận mặc định**.
  - Category đang hoạt động mới được hiển thị cho Student khi tạo Ticket và cho Staff khi phân loại/Transfer.
- Không xóa dữ liệu lịch sử của phòng ban hoặc Category đã từng được Ticket sử dụng; sử dụng trạng thái hoạt động/không hoạt động.
- Thay đổi ánh xạ Category → phòng ban chỉ áp dụng cho Ticket được tạo hoặc Transfer sau thời điểm thay đổi; Ticket hiện có không tự động chuyển phòng ban.
- Không cho vô hiệu hóa phòng ban nếu vẫn còn Ticket ở `NEW`, `IN_PROGRESS`, `WAITING_STUDENT` hoặc Ticket `RESOLVED` vẫn còn trong thời hạn 03 ngày làm việc để sinh viên phản hồi/mở lại thuộc phòng ban đó.

#### 4. Luồng xử lý chi tiết

**Luồng A — Quản lý phòng ban**
1. Management mở **Phòng ban & Nhóm vấn đề**.
2. Hệ thống hiển thị danh sách phòng ban và trạng thái hiện tại.
3. Người dùng tạo mới, chỉnh sửa tên hoặc thay đổi trạng thái hoạt động.
4. Hệ thống kiểm tra tính duy nhất và Ticket đang hoạt động liên quan.
5. Nếu hợp lệ, hệ thống lưu thay đổi và ghi nhận lịch sử.

**Luồng B — Quản lý Nhóm vấn đề**
1. Management mở danh sách Nhóm vấn đề.
2. Người dùng tạo mới hoặc chọn một Category hiện có.
3. Người dùng nhập/chỉnh sửa tên Category, trạng thái và phòng ban tiếp nhận mặc định.
4. Hệ thống kiểm tra Category và phòng ban được chọn đang hợp lệ.
5. Nếu hợp lệ, hệ thống lưu cấu hình.
6. Hệ thống ghi nhận Category/phòng ban trước và sau vào nhật ký tra soát.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Tên phòng ban hoặc Category vi phạm quy tắc duy nhất: từ chối lưu.
- Category đang hoạt động nhưng không có phòng ban tiếp nhận hợp lệ: từ chối lưu.
- Vô hiệu hóa phòng ban còn Ticket cần tiếp tục xử lý hoặc có thể được mở lại trong thời hạn phản hồi: từ chối thao tác.
- Phòng ban được gán cho Category đã không còn hoạt động: không cho kích hoạt Category.
- Người dùng không có quyền cấu hình: từ chối thao tác.

#### 6. Quy tắc nghiệp vụ
- Cấu hình Category → phòng ban là cơ sở để M01 xác định nơi tiếp nhận Ticket mới.
- M02 sử dụng cùng cấu hình này khi Staff thay đổi Category hoặc Transfer.
- Thay đổi cấu hình không được tự động sửa Category/phòng ban của Ticket đã tồn tại.
- Mọi thay đổi cấu hình phải được ghi nhận trong nhật ký tra soát.

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-02/AC-01:** Category đang hoạt động luôn có đúng một phòng ban tiếp nhận mặc định.
- **FR-MGT-02/AC-02:** M01 chỉ hiển thị Category đang hoạt động khi sinh viên tạo Ticket.
- **FR-MGT-02/AC-03:** Thay đổi ánh xạ Nhóm vấn đề → phòng ban không tự động thay đổi Category/phòng ban của Ticket đã tồn tại.
- **FR-MGT-02/AC-04:** Vô hiệu hóa phòng ban còn Ticket ở `NEW`, `IN_PROGRESS`, `WAITING_STUDENT` hoặc `RESOLVED` còn thời hạn phản hồi: bị từ chối với thông báo nêu số Ticket còn mở, phòng ban giữ trạng thái hoạt động.
- **FR-MGT-02/AC-05:** M02 dùng cấu hình mới cho các thao tác phân loại/chuyển xử lý phát sinh sau khi cấu hình được cập nhật.
- **FR-MGT-02/AC-06:** Mọi thay đổi phòng ban/Category được ghi trong nhật ký tra soát với giá trị trước/sau.
- **FR-MGT-02/AC-07:** Tên phòng ban trùng phòng ban đang hoạt động, hoặc tên Category trùng bất kỳ Category nào (kể cả đã vô hiệu hóa): không lưu, thông báo nêu tên bị trùng; nếu trùng Category đã vô hiệu hóa thì thông báo gợi ý kích hoạt lại.
- **FR-MGT-02/AC-08:** Lưu Category đang hoạt động mà không có phòng ban tiếp nhận hợp lệ: không lưu, thông báo tại trường phòng ban.
- **FR-MGT-02/AC-09:** Kích hoạt Category khi phòng ban được gán đã ngừng hoạt động: bị từ chối với thông báo, Category giữ trạng thái không hoạt động.
- **FR-MGT-02/AC-10:** Người không có quyền cấu hình: người dùng không thấy thao tác này; nếu gửi trực tiếp tới hệ thống thì nhận thông báo "không có quyền thực hiện" và dữ liệu không đổi.
- **FR-MGT-02/AC-11:** Ticket mới tạo ở M01 được gắn phòng ban theo cấu hình Category → phòng ban hiện hành tại thời điểm tạo.

#### 8. Luồng thay thế (Alternative Flows)
- Luồng B (Nhóm vấn đề) ở mục 4 là luồng song song với Luồng A (phòng ban).
- **A1 — Kích hoạt lại Category đã vô hiệu hóa** thay cho tạo mới cùng tên.

#### 9. Ví dụ Edge Case
- Vô hiệu hóa phòng ban còn một Ticket `RESOLVED` ở ngày làm việc thứ 3: bị từ chối; sang ngày thứ 4: được phép (FR-MGT-02/AC-04).
- Đổi ánh xạ Category → phòng ban khi đang có Ticket mở: Ticket cũ giữ phòng ban cũ (FR-MGT-02/AC-03).
- Tạo Category trùng tên với Category đã vô hiệu hóa: bị từ chối và gợi ý kích hoạt lại.

---

### [FR-MGT-03] Tra soát lịch sử thao tác

**Priority:** Trung bình: nền tảng ghi lịch sử làm từ MS-01; màn hình tra soát phục vụ khiếu nại và sự cố, không chặn luồng Ticket. **Mốc giao:** MS-01 (ghi nhận, kiểm bằng chứng kỹ thuật) và MS-05 (màn hình tra soát).

**Nghiệm thu tăng dần:** TS-AUTH-05 kiểm ghi nhận của các chức năng đã có ở MS-01 qua truy vấn/trích xuất chỉ đọc có phân quyền do DevOps/TL cung cấp, QA đối chiếu actor/thời điểm/trước–sau; che mật khẩu/token/dữ liệu nhạy cảm, không cấp quyền sửa/xóa. Mỗi mốc sau kiểm sự kiện mới khi chức năng tương ứng được giao. TS-MGT-03/09 kiểm UI tra cứu/lọc/phạm vi ở MS-05; không yêu cầu UI audit sớm.

#### 1. Mô tả & Phạm vi
Cho phép Management có quyền tra soát xem các thao tác quan trọng đã phát sinh trên Ticket và các chức năng quản trị hệ thống.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Management có quyền xem nhật ký tra soát.
- **Preconditions:** Người dùng đã đăng nhập và có quyền tra soát trong phạm vi dữ liệu tương ứng.

#### 3. Quy tắc Dữ liệu & Validation
- Có thể tìm/lọc tối thiểu theo: khoảng thời gian, người thực hiện, Mã Ticket nếu sự kiện liên quan Ticket và loại sự kiện.
- Mỗi bản ghi phải xác định tối thiểu: thời điểm, người/hệ thống thực hiện, loại sự kiện và nội dung thay đổi.
- Với sự kiện thay đổi dữ liệu, lịch sử phải lưu được giá trị trước và sau khi phù hợp.
- Nhật ký tra soát không được sửa hoặc xóa thông qua chức năng thông thường của ứng dụng, kể cả bởi tài khoản Management.

#### 4. Luồng xử lý chi tiết
1. Management mở **Nhật ký tra soát**.
2. Hệ thống hiển thị các bản ghi trong phạm vi quyền, mới nhất trước.
3. Người dùng nhập điều kiện tìm kiếm/lọc.
4. Hệ thống trả về các bản ghi phù hợp.
5. Người dùng mở một bản ghi để xem nội dung chi tiết của thay đổi.

Các sự kiện tối thiểu cần tra soát gồm:
- Thay đổi trạng thái Ticket.
- Phân công/phân công lại.
- Thay đổi mức độ ưu tiên/thời hạn xử lý.
- Chuyển xử lý và chuyển cấp xử lý.
- Ghi nhận kết quả, mở lại và đóng Ticket.
- Tạo/thay đổi/khóa tài khoản và quyền.
- Thay đổi phòng ban/Nhóm vấn đề và cấu hình liên quan.
- Thay đổi chính sách lưu trữ.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Không có bản ghi phù hợp: hiển thị danh sách trống.
- Bản ghi ngoài phạm vi quản lý: không hiển thị.
- Người dùng không có quyền tra soát: từ chối truy cập.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-AUD-01` và `BR-AUD-02`.
- Nhật ký tra soát là dữ liệu chỉ đọc trong ứng dụng, kể cả đối với tài khoản Management.
- Việc xử lý nhật ký đã hết thời hạn lưu trữ chỉ được thực hiện theo chính sách lưu trữ được phê duyệt, không phải bằng thao tác sửa/xóa nhật ký thông thường.
- Việc tra cứu nhật ký không làm thay đổi Ticket hoặc dữ liệu nghiệp vụ được tra soát.

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-03/AC-01:** Mỗi sự kiện bắt buộc trong danh sách ở mục 4 tạo một bản ghi tra soát có thời điểm, người/hệ thống thực hiện, loại sự kiện và giá trị trước/sau khi phù hợp.
- **FR-MGT-03/AC-02:** Lọc được nhật ký theo khoảng thời gian, tác nhân, Mã Ticket và loại sự kiện, dùng riêng hay kết hợp.
- **FR-MGT-03/AC-03:** Không tài khoản nào, kể cả Management, sửa hoặc xóa được bản ghi tra soát qua ứng dụng: màn hình không có thao tác sửa/xóa và yêu cầu sửa/xóa gửi trực tiếp bị từ chối.
- **FR-MGT-03/AC-04:** Management chỉ xem nhật ký thuộc phạm vi quyền được cấp; bản ghi ngoài phạm vi không xuất hiện trong kết quả.
- **FR-MGT-03/AC-05:** Không có bản ghi phù hợp: danh sách trống kèm thông báo "không có bản ghi phù hợp".
- **FR-MGT-03/AC-06:** Người không có quyền tra soát: không thấy mục Nhật ký tra soát; mở đường dẫn trực tiếp nhận trang "không có quyền truy cập".
- **FR-MGT-03/AC-07:** Xem và lọc nhật ký không tạo thay đổi nào trên Ticket hay dữ liệu được tra soát.
- **FR-MGT-03/AC-08:** Bản ghi đã hết thời hạn lưu trữ chỉ được đánh dấu theo chính sách của FR-MGT-04, không bị xóa qua màn hình tra soát.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Tra soát sự kiện quản trị:** lọc theo loại sự kiện (ví dụ khóa tài khoản) mà không nhập mã Ticket, vì sự kiện quản trị không gắn Ticket.

#### 9. Ví dụ Edge Case
- Lọc khoảng thời gian có ngày bắt đầu sau ngày kết thúc: bị từ chối.
- Gọi API sửa/xóa bản ghi tra soát bằng tài khoản Management: bị từ chối (FR-MGT-03/AC-03).
- Quản lý phòng ban A lọc theo mã Ticket của phòng ban B: không trả bản ghi nào (FR-MGT-03/AC-04).

---

### [FR-MGT-04] Quản lý chính sách lưu trữ dữ liệu

**Priority:** Thấp: chỉ đánh dấu dữ liệu đến hạn, không ảnh hưởng luồng xử lý; có thể dời qua CR nếu thiếu thời gian. **Mốc giao:** MS-05.

#### 1. Mô tả & Phạm vi
Cho phép Management có quyền cấu hình thời hạn lưu trữ cơ bản cho Ticket đã đóng, file đính kèm và nhật ký tra soát.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Management có quyền quản lý chính sách lưu trữ.
- **Preconditions:** Người dùng đã đăng nhập và có quyền cấu hình chính sách.

#### 3. Quy tắc Dữ liệu & Validation
- Chính sách được cấu hình riêng cho: **Ticket đã đóng**, **file đính kèm** và **nhật ký tra soát**.
- Thời hạn lưu trữ được nhập theo **số tháng nguyên dương**.
- Giá trị hợp lệ: từ **01 đến 120 tháng**.
- Thời hạn lưu trữ của Ticket được tính từ thời điểm Ticket chuyển sang `CLOSED`.
- Thời hạn lưu trữ của file đính kèm gắn với Ticket được tính theo thời điểm đóng của Ticket tương ứng.
- Thời hạn lưu trữ của nhật ký tra soát được tính từ thời điểm bản ghi nhật ký được tạo.
- Ticket chưa ở `CLOSED` không được xác định là dữ liệu Ticket đã đến hạn lưu trữ.
- Thay đổi chính sách không được làm mất lịch sử cấu hình trước đó.

#### 4. Luồng xử lý chi tiết
1. Management mở **Chính sách lưu trữ**.
2. Hệ thống hiển thị thời hạn hiện tại của từng loại dữ liệu.
3. Người dùng thay đổi thời hạn cần thiết.
4. Hệ thống kiểm tra giá trị và quyền thực hiện.
5. Nếu hợp lệ, hệ thống lưu chính sách mới và ghi nhận thời điểm có hiệu lực.
6. Hệ thống ghi nhận giá trị trước/sau và người thay đổi vào nhật ký tra soát.
7. Hệ thống sử dụng chính sách hiện hành để xác định và đánh dấu dữ liệu đã đạt thời hạn lưu trữ phục vụ tra soát/xử lý theo quy trình của nhà trường.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Giá trị không phải số tháng nguyên dương hoặc ngoài khoảng 01–120 tháng: từ chối lưu.
- Người dùng không có quyền cấu hình: từ chối thao tác.

#### 6. Quy tắc nghiệp vụ
- Chính sách lưu trữ chỉ áp dụng cho dữ liệu đáp ứng điều kiện của loại dữ liệu tương ứng.
- FR-MGT-04 chỉ quản lý thời hạn và xác định dữ liệu đã đến hạn; **không tự động xóa, ẩn danh hoặc di chuyển dữ liệu**.
- Thay đổi thời hạn không được làm thay đổi nội dung lịch sử nghiệp vụ của Ticket đang hoạt động.
- Việc thay đổi chính sách phải được ghi nhận để tra soát.

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-04/AC-01:** Chỉ chấp nhận số tháng nguyên từ 01 đến 120; giá trị như 0, 121, 12,5 hoặc chữ không được lưu, thông báo nêu khoảng hợp lệ, chính sách cũ giữ nguyên.
- **FR-MGT-04/AC-02:** Ticket chưa `CLOSED` không bị xác định là dữ liệu Ticket đã đến hạn lưu trữ.
- **FR-MGT-04/AC-03:** Ticket/file được tính thời hạn từ thời điểm Ticket `CLOSED`; nhật ký được tính từ thời điểm bản ghi được tạo.
- **FR-MGT-04/AC-04:** Dữ liệu đến hạn chỉ được đánh dấu để xử lý theo quy trình được phê duyệt; hệ thống không tự động xóa/ẩn danh/di chuyển dữ liệu.
- **FR-MGT-04/AC-05:** Mọi thay đổi chính sách có lịch sử trước/sau và thời điểm hiệu lực để tra soát.
- **FR-MGT-04/AC-06:** Người không có quyền cấu hình chính sách lưu trữ: người dùng không thấy thao tác này; nếu gửi trực tiếp tới hệ thống thì nhận thông báo "không có quyền thực hiện" và dữ liệu không đổi.
- **FR-MGT-04/AC-07:** Đổi thời hạn lưu trữ không làm thay đổi nội dung lịch sử nghiệp vụ của Ticket đang hoạt động.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Chỉ đổi một loại dữ liệu** (ví dụ file đính kèm); hai loại còn lại giữ nguyên chính sách cũ.

#### 9. Ví dụ Edge Case
- Nhập 0 hoặc 121 tháng: từ chối; 1 và 120: chấp nhận; 12,5: từ chối (FR-MGT-04/AC-01).
- Ticket mở lại sau khi đã tính thời hạn lưu trữ: không phát sinh vì Ticket `CLOSED` không mở lại được; Ticket chưa `CLOSED` không bao giờ đến hạn (FR-MGT-04/AC-02).

---

### [FR-MGT-05] Dashboard giám sát hoạt động hỗ trợ

**Priority:** Cao: giám sát khối lượng và Ticket quá hạn là mục tiêu cốt lõi G-04 của dự án. **Mốc giao:** MS-05.

#### 1. Mô tả & Phạm vi
Cung cấp màn hình tổng quan để Management theo dõi tình trạng xử lý hiện tại và khối lượng công việc trong phạm vi quản lý được cấp.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Management có quyền xem Dashboard.
- **Preconditions:** Người dùng đã đăng nhập và có phạm vi dữ liệu quản lý hợp lệ.

#### 3. Quy tắc Dữ liệu & Validation
Dashboard hiển thị tối thiểu:
- **Ticket mới:** số Ticket hiện ở `NEW`.
- **Đang xử lý:** số Ticket hiện ở `IN_PROGRESS`.
- **Chờ sinh viên:** số Ticket hiện ở `WAITING_STUDENT`.
- **Sắp quá hạn:** số Ticket đạt ngưỡng từ 80% đến dưới 100% thời gian xử lý mục tiêu.
- **Quá hạn:** số Ticket đạt từ 100% thời gian xử lý mục tiêu trở lên và chưa `RESOLVED`/`CLOSED`.
- **Khối lượng theo phòng ban:** số Ticket đang hoạt động (`NEW`, `IN_PROGRESS`, `WAITING_STUDENT`) của từng phòng ban.
- **Khối lượng theo nhân viên:** số Ticket đang hoạt động mà nhân viên hiện là người phụ trách chính.

Bộ lọc hỗ trợ tối thiểu:
- Phòng ban.
- Nhóm vấn đề.
- Trạng thái.

#### 4. Luồng xử lý chi tiết
1. Management mở Dashboard.
2. Hệ thống xác định phạm vi dữ liệu được phép xem.
3. Hệ thống tính các chỉ số hiện tại theo quy tắc Ticket và thời hạn dùng chung.
4. Hệ thống hiển thị các chỉ số và số liệu khối lượng công việc.
5. Người dùng áp dụng một hoặc nhiều bộ lọc.
6. Hệ thống tính lại số liệu trong phạm vi điều kiện đã chọn.
7. Người dùng có thể mở một chỉ số để xem danh sách Ticket cấu thành chỉ số đó nếu có quyền xem Ticket.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Không có dữ liệu: hiển thị giá trị 0 và trạng thái danh sách trống.
- Ticket ngoài phạm vi quản lý: không được tính vào số liệu.
- Người dùng không có quyền xem chi tiết Ticket: chỉ hiển thị số liệu tổng hợp được phép.

#### 6. Quy tắc nghiệp vụ
- Chỉ số sắp quá hạn/quá hạn tuân thủ `BR-DUE-01` và `BR-DUE-02`.
- Dashboard là ảnh chụp tình trạng hiện tại; không thay đổi trạng thái hay người phụ trách Ticket.
- Ticket `RESOLVED` và `CLOSED` không được tính vào khối lượng Ticket đang hoạt động.

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-05/AC-01:** Số lượng `NEW`, `IN_PROGRESS` và `WAITING_STUDENT` khớp với trạng thái hiện tại của Ticket trong phạm vi.
- **FR-MGT-05/AC-02:** Sắp quá hạn/quá hạn được tính đúng theo Business Rules, bao gồm việc loại trừ thời gian `WAITING_STUDENT`.
- **FR-MGT-05/AC-03:** Khối lượng phòng ban/nhân viên chỉ tính Ticket đang hoạt động; Ticket `RESOLVED`, `CLOSED` không được tính.
- **FR-MGT-05/AC-04:** Bộ lọc chỉ làm thay đổi số liệu trong phạm vi dữ liệu người dùng được phép xem.
- **FR-MGT-05/AC-05:** Mở một chỉ số chỉ hiển thị Ticket mà Management có quyền truy cập.
- **FR-MGT-05/AC-06:** Không có dữ liệu trong phạm vi: mọi chỉ số hiển thị 0 và danh sách trống, không có lỗi.
- **FR-MGT-05/AC-07:** Người không có quyền xem chi tiết Ticket thấy số liệu tổng hợp nhưng không mở được danh sách Ticket cấu thành chỉ số.
- **FR-MGT-05/AC-08:** Xem Dashboard và dùng bộ lọc không thay đổi trạng thái hay người phụ trách của Ticket nào.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Mở một chỉ số** để xem danh sách Ticket cấu thành (bước 7 mục 4).
- **A2 — Quản lý không có quyền xem Ticket:** chỉ thấy số liệu tổng hợp.

#### 9. Ví dụ Edge Case
- Không có Ticket nào trong phạm vi: mọi chỉ số bằng 0, không lỗi.
- Ticket ở `WAITING_STUDENT` lâu hơn thời hạn: không bị tính quá hạn (FR-MGT-05/AC-02).
- Ticket vừa chuyển `RESOLVED`: lần tải tiếp theo không còn trong khối lượng đang hoạt động (FR-MGT-05/AC-03).

---

### [FR-MGT-06] Báo cáo, mức độ hài lòng (CSAT) và xuất dữ liệu

**Priority:** Cao: báo cáo xu hướng, thời gian xử lý và CSAT là cam kết trong Proposal. Riêng xuất CSV ở mức Trung bình. **Mốc giao:** MS-05.

#### 1. Mô tả & Phạm vi
Cho phép Management xem báo cáo theo khoảng thời gian về xu hướng Nhóm vấn đề, thời gian xử lý và mức độ hài lòng của sinh viên; người có quyền có thể xuất dữ liệu báo cáo.

#### 2. Actors & Điều kiện tiên quyết
- **Actor:** Management có quyền xem báo cáo.
- **Actor bổ sung:** Management có quyền xuất báo cáo nếu thực hiện chức năng xuất.
- **Preconditions:** Người dùng đã đăng nhập và có phạm vi dữ liệu hợp lệ.

#### 3. Quy tắc Dữ liệu & Validation
- **Khoảng thời gian:** bắt buộc; ngày bắt đầu không được sau ngày kết thúc.
- Bộ lọc hỗ trợ tối thiểu: phòng ban và Nhóm vấn đề.
- **Xu hướng Nhóm vấn đề:** đếm Ticket theo Category dựa trên thời điểm Ticket được tạo trong khoảng báo cáo.
- **Thời gian xử lý:** chỉ tính Ticket có lần chuyển sang `RESOLVED` trong khoảng báo cáo. Với Ticket chưa từng mở lại, thời gian xử lý được tính từ lúc tạo đến `RESOLVED`, loại trừ thời gian `WAITING_STUDENT` và thời gian ngoài lịch làm việc. Với Ticket đã mở lại, tổng thời gian xử lý bằng tổng các khoảng thời gian Ticket thực sự ở quá trình xử lý đến từng lần `RESOLVED`; khoảng thời gian Ticket nằm ở `RESOLVED` để chờ sinh viên phản hồi không được tính là thời gian xử lý của nhân viên.
- **CSAT trung bình:** trung bình cộng điểm 1–5 của các đánh giá hợp lệ có **thời điểm gửi đánh giá** nằm trong khoảng báo cáo.
- **Tỷ lệ phản hồi CSAT:** được tính trên nhóm Ticket có **thời điểm chuyển sang `CLOSED` nằm trong khoảng báo cáo** và đã hết đủ 07 ngày theo lịch để sinh viên gửi đánh giá. Tỷ lệ = số Ticket trong nhóm này đã có đánh giá / tổng số Ticket trong nhóm này. Ticket chưa hết thời hạn 07 ngày không được đưa vào mẫu số.
- Dữ liệu xuất phải tuân thủ cùng bộ lọc và phạm vi quyền như dữ liệu đang xem.
- **Định dạng xuất:** CSV (UTF-8), mở được bằng Microsoft Excel với nội dung tiếng Việt hiển thị đúng.

#### 4. Luồng xử lý chi tiết
1. Management mở **Báo cáo**.
2. Người dùng chọn khoảng thời gian và bộ lọc cần thiết.
3. Hệ thống kiểm tra điều kiện lọc và phạm vi dữ liệu.
4. Hệ thống tổng hợp:
   - số lượng Ticket theo Nhóm vấn đề;
   - thời gian xử lý trung bình;
   - điểm CSAT trung bình và số lượng đánh giá;
   - khối lượng theo phòng ban/nhân viên khi cần.
5. Hệ thống hiển thị kết quả báo cáo.
6. Nếu người dùng có quyền xuất, người dùng chọn **Xuất báo cáo**.
7. Hệ thống tạo dữ liệu xuất đúng với phạm vi và bộ lọc hiện tại.

#### 5. Luồng ngoại lệ (lỗi và từ chối)
- Ngày kết thúc trước ngày bắt đầu: từ chối chạy báo cáo.
- Không có dữ liệu phù hợp: hiển thị báo cáo trống/0 thay vì tạo số liệu giả.
- Không có đánh giá CSAT trong phạm vi: không tính điểm trung bình và hiển thị trạng thái chưa có dữ liệu đánh giá.
- Người dùng không có quyền xuất: không cho thực hiện chức năng xuất.

#### 6. Quy tắc nghiệp vụ
- Thời gian xử lý sử dụng cùng cách tính thời gian làm việc tại `BR-DUE-01` và `BR-DUE-02`.
- CSAT tuân thủ `BR-CSAT-01`.
- Báo cáo không làm thay đổi dữ liệu Ticket.
- Dữ liệu xuất không được vượt quá phạm vi quyền của người thực hiện.

#### 7. Tiêu chí nghiệm thu
- **FR-MGT-06/AC-01:** Báo cáo xu hướng Category tính đúng Ticket được tạo trong khoảng thời gian đã chọn.
- **FR-MGT-06/AC-02:** Thời gian xử lý trung bình loại trừ thời gian `WAITING_STUDENT`, thời gian ngoài lịch làm việc và khoảng thời gian chờ phản hồi của sinh viên khi Ticket ở `RESOLVED`.
- **FR-MGT-06/AC-03:** Điểm CSAT trung bình chỉ sử dụng đánh giá hợp lệ 1–5 sao được gửi trong khoảng báo cáo.
- **FR-MGT-06/AC-04:** Tỷ lệ phản hồi CSAT chỉ sử dụng Ticket `CLOSED` trong khoảng báo cáo đã hết đủ 07 ngày đánh giá; Ticket còn thời hạn đánh giá không được tính vào mẫu số.
- **FR-MGT-06/AC-05:** Ngày kết thúc trước ngày bắt đầu, hoặc thiếu ngày: không chạy báo cáo, thông báo tại trường ngày.
- **FR-MGT-06/AC-06:** Người không có quyền xuất không thấy nút Xuất báo cáo; yêu cầu xuất gửi trực tiếp bị từ chối, không tạo file.
- **FR-MGT-06/AC-07:** Dữ liệu xuất khớp với bộ lọc và phạm vi quyền của báo cáo đang xem.
- **FR-MGT-06/AC-08:** Dữ liệu xuất ở định dạng CSV và hiển thị đúng tiếng Việt khi mở bằng Microsoft Excel.
- **FR-MGT-06/AC-09:** Không có dữ liệu phù hợp: báo cáo hiển thị 0 hoặc trống, không có số liệu giả.
- **FR-MGT-06/AC-10:** Không có đánh giá CSAT trong phạm vi: điểm trung bình hiển thị "chưa có dữ liệu đánh giá" thay vì 0.
- **FR-MGT-06/AC-11:** Chạy và xuất báo cáo không thay đổi dữ liệu Ticket.

#### 8. Luồng thay thế (Alternative Flows)
- **A1 — Chỉ xem, không xuất:** Quản lý không có quyền xuất vẫn xem được báo cáo.

#### 9. Ví dụ Edge Case
- Khoảng báo cáo một ngày (bắt đầu = kết thúc): hợp lệ.
- Ticket mở lại hai lần: thời gian xử lý là tổng các đoạn xử lý, không tính thời gian chờ ở `RESOLVED` (FR-MGT-06/AC-02).
- Ticket `CLOSED` cách đây 6 ngày: không vào mẫu số tỷ lệ phản hồi CSAT (FR-MGT-06/AC-04).
- Tên Category có dấu tiếng Việt và dấu phẩy: file CSV mở bằng Excel đúng dấu, đúng cột (FR-MGT-06/AC-08).

---

## III. QUY TẮC THAM CHIẾU

Các Functional Requirements của M03 phải tuân thủ thống nhất với:

- [Actors & Roles](../../01-product/actors-and-roles.md)
- [Ticket Model](../../02-domain/ticket-model.md)
- [Ticket Lifecycle](../../02-domain/ticket-lifecycle.md)
- [State Transition](../../02-domain/state-transition.md)
- [Business Rules](../../02-domain/business-rules.md)
