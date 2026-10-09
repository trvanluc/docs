# [ARC-01] Sơ đồ ngữ cảnh hệ thống UniSupport (System Context)

Tài liệu này mô tả sơ đồ ngữ cảnh (System Context Diagram - C4 Model Level 1) của hệ thống **UniSupport**, xác định ranh giới giữa hệ thống Web Application UniSupport với các đối tượng người dùng (Actors) và môi trường hạ tầng của **Aurora University**.

---

## 1. Tổng quan phạm vi hệ thống (System Scope)

UniSupport là hệ thống **Web Application** đóng vai trò là đầu mối tập trung toàn bộ quy trình tiếp nhận, phân loại, xử lý, theo dõi và đánh giá chất lượng yêu cầu hỗ trợ sinh viên tại Aurora University.

* **Phạm vi phục vụ:** Khối lượng người dùng khoảng **3.000 sinh viên** cùng đội ngũ Nhân viên hỗ trợ và Quản lý các phòng ban.
* **Loại ứng dụng:** Web Application (Responsive Web hỗ trợ trình duyệt Máy tính và Thiết bị di động).
* **Ranh giới tích hợp:** Độc lập, không kết nối/tích hợp với các hệ thống bên thứ ba ngoài phạm vi đã thỏa thuận.

---

## 2. Các Tác nhân tương tác (Actors)

### 2.1 Sinh viên (Student)
* **Mô tả:** Người dùng gửi các yêu cầu cần giải đáp hoặc hỗ trợ hành chính/đào tạo/mạng/cơ sở vật chất.
* **Tương tác:**
  * Đăng nhập tài khoản cá nhân.
  * Tạo phiếu hỗ trợ (Ticket), đính kèm minh chứng (ảnh/PDF).
  * Theo dõi tiến độ xử lý và lịch sử cập nhật.
  * Bổ sung thông tin/giấy tờ theo yêu cầu của nhân viên.
  * Nhận kết quả và thực hiện đánh giá mức độ hài lòng (1-5 sao).

### 2.2 Nhân viên hỗ trợ (Staff)
* **Mô tả:** Nhân viên các phòng ban nghiệp vụ thuộc Aurora University chịu trách nhiệm giải quyết yêu cầu của sinh viên.
* **Tương tác:**
  * Đăng nhập hệ thống theo phòng ban.
  * Tiếp nhận, phân loại nhóm vấn đề và gán mức độ ưu tiên cho Ticket.
  * Chuyển tiếp Ticket sang phòng ban khác nếu sai thẩm quyền.
  * Yêu cầu sinh viên bổ sung giấy tờ/thông tin.
  * Cập nhật tiến độ, ghi nhận kết quả giải quyết và đóng Ticket.

### 2.3 Quản lý / Quản trị viên (Management & Admin)
* **Mô tả:** Ban quản lý đơn vị/trường và Quản trị viên hệ thống.
* **Tương tác:**
  * Xem Dashboard báo cáo tổng quan về khối lượng công việc, tỷ lệ Ticket đúng/quá hạn SLA.
  * Phân tích xu hướng các nhóm vấn đề sinh viên thường gặp.
  * Quản trị tài khoản, phân quyền vai trò (Student, Staff, Management) và quản lý danh mục phòng ban.
  * Tra soát nhật ký hoạt động (Audit log) cơ bản của hệ thống.

---

## 3. Sơ đồ ngữ cảnh C4 (System Context Diagram)

```
                    +-----------------------------------+
                    |        Aurora University          |
                    +-----------------------------------+
                                      |
      +-------------------------------+-------------------------------+
      |                               |                               |
      v                               v                               v
+------------------+           +-------------------+           +-------------------+
|  Sinh viên       |           |  Nhân viên        |           |  Quản lý / Admin  |
|  (Student)       |           |  (Staff)          |           |  (Management)     |
+------------------+           +-------------------+           +-------------------+
        |                               |                               |
        | HTTP / HTTPS                  | HTTP / HTTPS                  | HTTP / HTTPS
        | (Web Browser PC/Mobile)       | (Web Browser PC/Mobile)       | (Web Browser PC)
        v                               v                               v
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                              HỆ THỐNG UNISUPPORT                                  |
|                            (Web Application Platform)                             |
|                                                                                   |
|  - Student Portal: Tạo ticket, theo dõi tiến độ, bổ sung hồ sơ, đánh giá         |
|  - Staff Operations: Phân loại, điều phối, xử lý, cập nhật trạng thái             |
|  - Management Dashboard: Báo cáo thống kê, xu hướng, quản trị tài khoản           |
|  - Notification Service: Thông báo cập nhật trạng thái nội bộ                     |
|  - Security & Storage: Phân quyền RBAC, lưu trữ file đính kèm (PDF/Image)          |
|                                                                                   |
+-----------------------------------------------------------------------------------+
                                      |
                                      | Lưu trữ dữ liệu & File
                                      v
                    +-----------------------------------+
                    | Hạ tầng Server & Storage          |
                    | (Do Aurora University cung cấp)   |
                    +-----------------------------------+
```

---

## 4. Các Giả định & Ràng buộc ngữ cảnh (Contextual Assumptions & Constraints)

* **Hạ tầng triển khai:** Hệ thống được vận hành hoàn toàn trên hạ tầng Server và tên miền nội bộ/Cloud do Aurora University cấp.
* **Không kết nối SSO/Third-party:** Xác thực được thực hiện trực tiếp thông qua Cơ sở dữ liệu của UniSupport (không tích hợp LDAP/OAuth ngoài phạm vi).
* **Truy cập tệp đính kèm:** Tệp đính kèm (Ảnh/PDF) được lưu trữ trên Server local/cloud và được kiểm soát quyền truy cập trực tiếp bởi phân hệ `M05-rbac-security`.