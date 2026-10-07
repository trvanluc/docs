# Phân Hệ Quản Lý (M03 - Management Dashboard)

## I. TỔNG QUAN PHÂN HỆ
Phân hệ Quản lý cung cấp công cụ giúp ban quản lý nắm tổng quan tình hình xử lý yêu cầu, theo dõi tiến độ và khối lượng công việc, xem các báo cáo xu hướng/SLA/đánh giá, đồng thời thực hiện quản trị hệ thống (tạo, chỉnh sửa tài khoản và gán quyền phù hợp)[cite: 1].

---

## II. CHI TIẾT CÁC CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### [FR-MNG-01] Quản lý đăng nhập hệ thống

**Mô tả**  
Cho phép Ban quản lý đăng nhập hệ thống bằng tài khoản riêng để nắm tổng quan tình hình và thực hiện quản trị[cite: 1].

**Actor**  
Quản lý (Manager / Admin)[cite: 1].

**Preconditions**  
- Tài khoản quản lý đã được thiết lập sẵn trong hệ thống[cite: 1].

**Luồng chính**  
1. Quản lý truy cập đường dẫn quản trị UniSupport[cite: 1].
2. Nhập **Tên đăng nhập / Email quản trị** và **Mật khẩu**[cite: 1].
3. Nhấn **Đăng nhập**.
4. Hệ thống xác thực quyền và chuyển hướng đến Dashboard Quản lý[cite: 1].

**Business Rules**  
- Mỗi vai trò chỉ thấy và thao tác được trong phạm vi quyền của mình[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Đăng nhập đúng tài khoản Quản lý -> Truy cập giao diện Dashboard quản trị thành công[cite: 1].

---

### [FR-MNG-02] Nắm tổng quan tình hình & Giám sát tiến độ

**Mô tả**  
Xem số lượng yêu cầu mới, đang xử lý và những yêu cầu sắp hoặc đã quá hạn; theo dõi tiến độ và khối lượng công việc theo từng phòng ban hoặc nhân viên[cite: 1].

**Actor**  
Quản lý đã đăng nhập hệ thống[cite: 1].

**Preconditions**  
- Quản lý đã đăng nhập thành công[cite: 1].

**Luồng chính**  
1. Quản lý mở trang **Tổng Quan Tình Hình**[cite: 1].
2. Hệ thống tổng hợp và hiển thị các khối thẻ chỉ số:
   - Số lượng yêu cầu mới[cite: 1].
   - Số lượng yêu cầu đang xử lý[cite: 1].
   - Những yêu cầu sắp hoặc đã quá hạn[cite: 1].
3. Hệ thống hiển thị bảng/biểu đồ theo dõi tiến độ và khối lượng công việc theo từng phòng ban hoặc nhân viên[cite: 1].
4. Quản lý có thể chọn lọc chỉ số theo mốc thời gian.

**Business Rules**  
- Dữ liệu tổng quan tình hình được cập nhật chính xác theo thời gian thực hoặc phiên làm việc[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Hiển thị chính xác số lượng yêu cầu mới, đang xử lý, sắp hoặc đã quá hạn[cite: 1].
- **AC-02:** Hiển thị rõ ràng khối lượng công việc theo phòng ban và nhân viên[cite: 1].

---

### [FR-MNG-03] Xem báo cáo thống kê

**Mô tả**  
Xem báo cáo để biết được nhóm yêu cầu nào đang nhiều nhất và có xu hướng tăng giảm ra sao; xem thời gian xử lý trung bình và tổng hợp phản hồi của sinh viên theo từng giai đoạn[cite: 1].

**Actor**  
Quản lý đã đăng nhập hệ thống[cite: 1].

**Preconditions**  
- Hệ thống đã có dữ liệu giao dịch Ticket[cite: 1].

**Luồng chính**  
1. Quản lý truy cập chức năng **Xem Báo Cáo**[cite: 1].
2. Chọn loại báo cáo cần xem:
   - Báo cáo nhóm yêu cầu đang nhiều nhất và xu hướng tăng giảm[cite: 1].
   - Báo cáo thời gian xử lý trung bình[cite: 1].
   - Báo cáo tổng hợp phản hồi của sinh viên theo từng giai đoạn[cite: 1].
3. Chọn khoảng thời gian và nhấn **Xem báo cáo**.
4. Hệ thống xuất biểu đồ và bảng số liệu báo cáo tương ứng.

**Business Rules**  
- Tổng hợp phản hồi sinh viên dựa trên điểm số đánh giá hài lòng sau khi Ticket hoàn thành[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Báo cáo phản ảnh đúng xu hướng nhóm yêu cầu, thời gian xử lý trung bình và tổng hợp phản hồi của sinh viên[cite: 1].

---

### [FR-MNG-04] Quản trị hệ thống & Phân quyền

**Mô tả**  
Tạo, chỉnh sửa tài khoản và gán quyền phù hợp với từng vai trò, đảm bảo an toàn bảo mật và phân quyền hệ thống[cite: 1].

**Actor**  
Quản lý hệ thống (Admin)[cite: 1].

**Preconditions**  
- Quản lý đăng nhập bằng tài khoản có thẩm quyền Quản trị[cite: 1].

**Luồng chính**  
1. Quản lý mở chức năng **Quản Trị Hệ Thống**[cite: 1].
2. Để tạo tài khoản: Nhấn **Tạo tài khoản** -> Nhập thông tin, gán vai trò (`Student`, `Staff`, `Manager`) -> Nhấn **Lưu**[cite: 1].
3. Để chỉnh sửa: Chọn tài khoản -> Chỉnh sửa thông tin/gán quyền phù hợp -> Nhấn **Cập nhật**[cite: 1].
4. Hệ thống cập nhật quyền hạn và lưu vết lịch sử thao tác để tra soát khi cần[cite: 1].

**Business Rules**  
- Người dùng đăng nhập bằng tài khoản và mật khẩu riêng[cite: 1].
- Mỗi vai trò chỉ thấy và thao tác được trong phạm vi quyền của mình[cite: 1].
- Các thao tác quan trọng trong hệ thống đều được ghi lại để tra soát khi cần[cite: 1].

**Acceptance Criteria**  
- **AC-01:** Tạo, chỉnh sửa tài khoản và gán quyền thành công -> Người dùng đăng nhập thao tác đúng phạm vi quyền[cite: 1].
- **AC-02:** Thao tác quản trị được ghi lại đầy đủ trong log tra soát[cite: 1].