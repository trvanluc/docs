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

#### 5. Luồng ngoại lệ
- Thông tin đăng nhập không hợp lệ: từ chối truy cập.
- Tài khoản bị khóa hoặc vô hiệu hóa: không tạo phiên đăng nhập.
- Tài khoản không có vai trò Management: không cho truy cập Management Dashboard.
- Phiên hết hạn: yêu cầu xác thực lại.

#### 6. Quy tắc nghiệp vụ
- Quản lý phạm vi toàn trường được xem dữ liệu toàn trường theo quyền chức năng được cấp.
- Quản lý phạm vi phòng ban chỉ được xem dữ liệu thuộc phòng ban được cấu hình.
- Quyền truy cập tuân thủ [Actors & Roles](../../01-product/actors-and-roles.md).

#### 7. Tiêu chí nghiệm thu
- **AC-00-01:** Tài khoản Management hợp lệ truy cập được Management Dashboard.
- **AC-00-02:** Tài khoản không có vai trò Management không truy cập được phân hệ.
- **AC-00-03:** Các chức năng quản trị không thuộc quyền của tài khoản không được phép sử dụng.
- **AC-00-04:** Dữ liệu ngoài phạm vi quản lý không được hiển thị hoặc truy cập trực tiếp.

---

### [FR-MGT-01] Quản lý tài khoản, vai trò và phạm vi quyền

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
- Hệ thống phải luôn còn ít nhất **một tài khoản Quản lý đang hoạt động có quyền quản lý tài khoản và phân quyền**.
- Người quản trị không được cấp cho tài khoản khác quyền hoặc phạm vi quản lý vượt quá quyền/phạm vi mà chính mình được phép quản lý.

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
4. Hệ thống kiểm tra cấu hình mới, bảo đảm người thực hiện không cấp quyền vượt quá phạm vi của mình và thao tác không làm mất toàn bộ tài khoản Quản lý có quyền quản lý tài khoản/phân quyền.
5. Nếu hợp lệ, hệ thống lưu thay đổi và áp dụng phạm vi quyền mới.
6. Hệ thống ghi nhận giá trị trước/sau và người thực hiện vào nhật ký tra soát.

**Luồng C — Khóa hoặc mở khóa**
1. Management chọn tài khoản.
2. Người dùng chọn khóa hoặc mở khóa và nhập lý do.
3. Hệ thống kiểm tra quyền, điều kiện thao tác và bảo đảm việc khóa không làm mất tài khoản Quản lý cuối cùng có quyền quản lý tài khoản/phân quyền.
4. Khi khóa tài khoản Nhân viên, hệ thống kiểm tra các Ticket chưa hoàn tất mà tài khoản đang là người phụ trách chính. Nếu có Ticket ở `NEW`, `IN_PROGRESS` hoặc `WAITING_STUDENT`, hệ thống gỡ người phụ trách hiện tại và đưa các Ticket đó về hàng chờ chưa có người phụ trách của phòng ban đang xử lý để được phân công lại.
5. Hệ thống khóa tài khoản ngay sau khi hoàn tất việc cập nhật trách nhiệm xử lý Ticket.
6. Hệ thống ghi nhận lý do khóa, các Ticket bị ảnh hưởng và người thực hiện vào nhật ký tra soát.
7. Với thao tác mở khóa, hệ thống cập nhật tài khoản về trạng thái hoạt động nhưng không tự động gán lại các Ticket đã được đưa về hàng chờ trước đó.

#### 5. Luồng ngoại lệ
- Tên đăng nhập/Mã định danh đã tồn tại: từ chối tạo mới.
- Tài khoản Nhân viên không có phòng ban hợp lệ: từ chối lưu.
- Người dùng cố tự khóa tài khoản đang đăng nhập: từ chối.
- Thao tác khóa/hạ quyền sẽ làm hệ thống không còn tài khoản Quản lý đang hoạt động có quyền quản lý tài khoản/phân quyền: từ chối.
- Người thực hiện cố cấp quyền hoặc phạm vi vượt quá quyền/phạm vi của chính mình: từ chối.
- Người dùng không có quyền quản trị tài khoản: từ chối thao tác.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ ma trận quyền tại [Actors & Roles](../../01-product/actors-and-roles.md).
- Thay đổi quyền/phạm vi không làm thay đổi lịch sử các Ticket trước đó.
- Khóa tài khoản Nhân viên có hiệu lực ngay sau khi các Ticket đang được gán cho tài khoản đó được gỡ người phụ trách và đưa về hàng chờ của phòng ban hiện tại.
- Việc khóa tài khoản không làm thay đổi phòng ban hoặc trạng thái nghiệp vụ của Ticket.
- Hệ thống luôn phải còn ít nhất một tài khoản Quản lý đang hoạt động có quyền quản lý tài khoản và phân quyền.
- Người quản trị chỉ được cấp quyền trong giới hạn quyền và phạm vi quản lý của chính mình.
- Tạo, thay đổi quyền, khóa và mở khóa tài khoản đều phải được ghi nhận để tra soát.

#### 7. Tiêu chí nghiệm thu
- **AC-01-01:** Tài khoản hợp lệ được tạo với đúng nhóm người dùng, phạm vi và mật khẩu khởi tạo.
- **AC-01-02:** Không thể tạo hai tài khoản có cùng Tên đăng nhập/Mã định danh.
- **AC-01-03:** Tài khoản Nhân viên chỉ được lưu khi được gắn với một phòng ban đang hoạt động.
- **AC-01-04:** Khóa Nhân viên đang phụ trách Ticket hợp lệ sẽ gỡ người phụ trách và đưa các Ticket liên quan về hàng chờ của phòng ban trước khi tài khoản bị khóa.
- **AC-01-05:** Không thể khóa/hạ quyền nếu thao tác làm hệ thống mất tài khoản Quản lý cuối cùng có quyền quản lý tài khoản và phân quyền.
- **AC-01-06:** Người quản trị không thể cấp quyền hoặc phạm vi vượt quá quyền/phạm vi của chính mình.
- **AC-01-07:** Mọi thay đổi vai trò/phạm vi và trạng thái tài khoản được ghi nhận trong nhật ký tra soát.

---

### [FR-MGT-02] Quản lý phòng ban và Nhóm vấn đề

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

#### 5. Luồng ngoại lệ
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
- **AC-02-01:** Category hoạt động luôn có đúng một phòng ban tiếp nhận mặc định.
- **AC-02-02:** M01 chỉ hiển thị Category đang hoạt động khi sinh viên tạo Ticket.
- **AC-02-03:** Thay đổi ánh xạ Nhóm vấn đề → phòng ban không tự động thay đổi Ticket đã tồn tại.
- **AC-02-04:** Không thể vô hiệu hóa phòng ban nếu còn Ticket ở `NEW`, `IN_PROGRESS`, `WAITING_STUDENT` hoặc `RESOLVED` vẫn còn thời hạn phản hồi/mở lại.
- **AC-02-05:** M02 sử dụng cấu hình mới cho các thao tác phân loại/chuyển xử lý phát sinh sau khi cấu hình được cập nhật.
- **AC-02-06:** Thay đổi phòng ban/Category được ghi nhận để tra soát.

---

### [FR-MGT-03] Tra soát lịch sử thao tác

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

#### 5. Luồng ngoại lệ
- Không có bản ghi phù hợp: hiển thị danh sách trống.
- Bản ghi ngoài phạm vi quản lý: không hiển thị.
- Người dùng không có quyền tra soát: từ chối truy cập.

#### 6. Quy tắc nghiệp vụ
- Tuân thủ `BR-AUD-01` và `BR-AUD-02`.
- Nhật ký tra soát là dữ liệu chỉ đọc trong ứng dụng, kể cả đối với tài khoản Management.
- Việc xử lý nhật ký đã hết thời hạn lưu trữ chỉ được thực hiện theo chính sách lưu trữ được phê duyệt, không phải bằng thao tác sửa/xóa nhật ký thông thường.
- Việc tra cứu nhật ký không làm thay đổi Ticket hoặc dữ liệu nghiệp vụ được tra soát.

#### 7. Tiêu chí nghiệm thu
- **AC-03-01:** Các sự kiện quan trọng bắt buộc có bản ghi tra soát tương ứng.
- **AC-03-02:** Có thể lọc nhật ký theo khoảng thời gian, tác nhân, Mã Ticket và loại sự kiện.
- **AC-03-03:** Không tài khoản nào, kể cả Management, có thể sửa/xóa bản ghi tra soát qua chức năng thông thường của ứng dụng.
- **AC-03-04:** Management chỉ xem nhật ký thuộc phạm vi quyền được cấp.

---

### [FR-MGT-04] Quản lý chính sách lưu trữ dữ liệu

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

#### 5. Luồng ngoại lệ
- Giá trị không phải số tháng nguyên dương hoặc ngoài khoảng 01–120 tháng: từ chối lưu.
- Người dùng không có quyền cấu hình: từ chối thao tác.

#### 6. Quy tắc nghiệp vụ
- Chính sách lưu trữ chỉ áp dụng cho dữ liệu đáp ứng điều kiện của loại dữ liệu tương ứng.
- FR-MGT-04 chỉ quản lý thời hạn và xác định dữ liệu đã đến hạn; **không tự động xóa, ẩn danh hoặc di chuyển dữ liệu**.
- Thay đổi thời hạn không được làm thay đổi nội dung lịch sử nghiệp vụ của Ticket đang hoạt động.
- Việc thay đổi chính sách phải được ghi nhận để tra soát.

#### 7. Tiêu chí nghiệm thu
- **AC-04-01:** Chỉ chấp nhận giá trị thời hạn từ 01 đến 120 tháng.
- **AC-04-02:** Ticket chưa `CLOSED` không bị xác định là dữ liệu Ticket đã đến hạn lưu trữ.
- **AC-04-03:** Ticket/file được tính thời hạn từ thời điểm Ticket `CLOSED`; nhật ký được tính từ thời điểm bản ghi được tạo.
- **AC-04-04:** Dữ liệu đến hạn chỉ được đánh dấu để xử lý theo quy trình được phê duyệt; hệ thống không tự động xóa/ẩn danh/di chuyển dữ liệu.
- **AC-04-05:** Mọi thay đổi chính sách có lịch sử trước/sau để tra soát.

---

### [FR-MGT-05] Dashboard giám sát hoạt động hỗ trợ

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

#### 5. Luồng ngoại lệ
- Không có dữ liệu: hiển thị giá trị 0 và trạng thái danh sách trống.
- Ticket ngoài phạm vi quản lý: không được tính vào số liệu.
- Người dùng không có quyền xem chi tiết Ticket: chỉ hiển thị số liệu tổng hợp được phép.

#### 6. Quy tắc nghiệp vụ
- Chỉ số sắp quá hạn/quá hạn tuân thủ `BR-DUE-01` và `BR-DUE-02`.
- Dashboard là ảnh chụp tình trạng hiện tại; không thay đổi trạng thái hay người phụ trách Ticket.
- Ticket `RESOLVED` và `CLOSED` không được tính vào khối lượng Ticket đang hoạt động.

#### 7. Tiêu chí nghiệm thu
- **AC-05-01:** Số lượng `NEW`, `IN_PROGRESS` và `WAITING_STUDENT` khớp với trạng thái hiện tại của Ticket trong phạm vi.
- **AC-05-02:** Sắp quá hạn/quá hạn được tính đúng theo Business Rules, bao gồm việc loại trừ thời gian `WAITING_STUDENT`.
- **AC-05-03:** Khối lượng phòng ban/nhân viên chỉ tính Ticket đang hoạt động.
- **AC-05-04:** Bộ lọc chỉ làm thay đổi số liệu trong phạm vi dữ liệu người dùng được phép xem.
- **AC-05-05:** Mở chỉ số chỉ hiển thị Ticket mà Management có quyền truy cập.

---

### [FR-MGT-06] Báo cáo, mức độ hài lòng (CSAT) và xuất dữ liệu

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

#### 5. Luồng ngoại lệ
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
- **AC-06-01:** Báo cáo xu hướng Category tính đúng Ticket được tạo trong khoảng thời gian đã chọn.
- **AC-06-02:** Thời gian xử lý trung bình loại trừ thời gian `WAITING_STUDENT`, thời gian ngoài lịch làm việc và khoảng thời gian chờ phản hồi của sinh viên khi Ticket ở `RESOLVED`.
- **AC-06-03:** Điểm CSAT trung bình chỉ sử dụng đánh giá hợp lệ 1–5 sao được gửi trong khoảng báo cáo.
- **AC-06-04:** Tỷ lệ phản hồi CSAT chỉ sử dụng Ticket `CLOSED` trong khoảng báo cáo đã hết đủ 07 ngày đánh giá; Ticket còn thời hạn đánh giá không được tính vào mẫu số.
- **AC-06-05:** Khoảng thời gian không hợp lệ bị từ chối.
- **AC-06-06:** Người không có quyền xuất không thể xuất báo cáo.
- **AC-06-07:** Dữ liệu xuất khớp với bộ lọc và phạm vi quyền của báo cáo đang xem.


---

## III. QUY TẮC THAM CHIẾU

Các Functional Requirements của M03 phải tuân thủ thống nhất với:

- [Actors & Roles](../../01-product/actors-and-roles.md)
- [Ticket Model](../../02-domain/ticket-model.md)
- [Ticket Lifecycle](../../02-domain/ticket-lifecycle.md)
- [State Transition](../../02-domain/state-transition.md)
- [Business Rules](../../02-domain/business-rules.md)
