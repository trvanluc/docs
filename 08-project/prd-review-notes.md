# Ghi nhận đối chiếu PRD và tài liệu hiện tại

## Các sửa đổi nghiệp vụ đã thực hiện

- Đồng bộ 14 mã FR giữa PRD, README, Product Scope, Workflows, RTM và kịch bản nghiệm thu; 17 dòng Resources dùng mã R độc lập.
- Giữ đúng 187 giá trị giờ của 17 dòng công việc (8 vai trò, cơ sở, dự phòng, kế hoạch), cùng PM 70 và DevOps 30; tổng 640.
- Tách MANAGER/ADMIN, Staff Claim và Manager/Admin Assign; danh mục nhóm vấn đề do ADMIN quản lý và gắn phòng ban mặc định.
- Làm rõ 5MB/tệp, tối đa 5 tệp sinh viên / 3 tệp kết quả, PDF/PNG/JPG/JPEG; sửa message thiếu trường và phân biệt sai định dạng/quá dung lượng.
- Nối luồng bổ sung trên cùng Ticket, phân biệt NEED_MORE_INFO/IN_PROGRESS/TRANSFERRED/RESOLVED/CLOSED; phân biệt hoàn tất xử lý với đóng.
- Nghiệm thu theo các giới hạn đã có, không yêu cầu FAQ, mở lại xử lý, Escalation nhiều cấp, ghi chú nội bộ, tự sinh/gửi mật khẩu hoặc UI dọn dẹp mới.
- Bỏ phân giờ giai đoạn không có trong nguồn; giữ lịch hiện tại nhưng không khẳng định đã kiểm chứng công suất từng người/tuần.
- Tạo tài liệu đối chiếu Resources đang thiếu và tạo lại bản tổng hợp từ file hiện tại.

## Những sai lệch thuộc nội dung kỹ thuật được giữ nguyên theo yêu cầu người dùng

Các mục dưới đây là **quan sát trực tiếp trong file**, không phải bug ứng dụng đã tái hiện. Bản sửa không thay API, schema, enum, thuật toán, kiến trúc hoặc nội dung triển khai của các tài liệu này. Chúng không được dùng để mở rộng PRD nghiệp vụ đã chốt.

| Tài liệu/vị trí | Sai lệch hiện tại | Cách đọc trong bản sửa |
| --- | --- | --- |
| 02-domain/ticket-model.md; 07-architecture/data-model.md | WAITING_STUDENT/CANCELLED, tên trường sinh viên/phụ trách và 10MB/255 ký tự khác PRD | Giữ bảng kỹ thuật; đầu vào nghiệp vụ theo FR-STU-02/03. Không tự thêm trạng thái hoặc đổi schema. |
| 05-non-functional-requirements/performance.md; 07-architecture/security-design.md | Còn ghi 10MB và một số định dạng thiếu JPEG | Nghiệp vụ/AC theo 5MB và bốn định dạng của PRD. Không chỉnh NFR hoặc phương án file. |
| 05-non-functional-requirements/security.md; 07-architecture/security-design.md; ADR-002 | Gộp 3 vai trò/MANAGEMENT và quyền quản trị toàn trường, khác MANAGER/ADMIN trong PRD | Quyền nghiệp vụ theo Actors & Roles/FR-MNG-01/04. Nội dung kỹ thuật giữ nguyên, chưa xác nhận đã đồng bộ triển khai. |
| M04 prd.md/README.md | FR-STU-04 bị gọi là thông báo; FR-STF-03 bị gọi là SLA; WAITING_STUDENT; cảnh báo 2 giờ thay vì ngưỡng PRD; thêm mark-all-read/âm thanh/xem tất cả | Tài liệu hỗ trợ hiện tại, không phải FR nghiệp vụ mới. Giữ giờ R-STU-04 19 và giờ nguồn liên quan; không chốt các mở rộng đó. |
| M05 prd.md/README.md | Dùng FR-ADM-01/03/04 theo dòng công sức, mã FR-SEC trùng cách gọi NFR, timeout 24 giờ, hành vi đổi mật khẩu liên thiết bị | Đối chiếu bằng R-ADM; không cộng FR hoặc effort mới, không chốt cơ chế phiên mới. |
| 07-architecture/api-design.md | Cổng Management gộp quyền; đường dẫn rating khác PRD rate; mô tả Resolve/Close còn gộp | Giữ API hiện tại. Không thay endpoint hoặc coi mô tả này là quyền mới cho Manager. |
| ADR-001 và README ADR | Mã Ticket dùng YYYYMM/random, khác ví dụ YYYYMMDD-XXXX trong PRD | Giữ quyết định kỹ thuật gốc hiện tại; bản sửa nghiệp vụ chỉ dùng ví dụ của PRD, không chọn bộ sinh mã thay thế. |
| 02-domain/state-transition.md | Chưa liệt kê NEED_MORE_INFO → TRANSFERRED trong khi FR-STF-03 cho phép chuyển trong trạng thái đó; quyền Staff cũ xem sau chuyển còn chưa thống nhất | Workflow dẫn về điều kiện FR-STF-03 đã có; không tự thêm hàng vào FSM hoặc quyền dữ liệu trong triển khai. |
| BR-09 / vòng đời | Cách ghi 3 ngày làm việc và 72 giờ làm việc chưa cùng cách tính | Giữ quy tắc Auto-close hiện có, không chọn thuật toán hoặc deadline mới. |
| 05-deployment và timeline | Môi trường Production trước/sau nghiệm thu còn mô tả khác nhau | Giữ nội dung triển khai; lịch không được dùng làm estimate giờ mới. |

## Nguồn video và giới hạn bằng chứng

Các điểm sửa về tài khoản, nhóm vấn đề và độ rõ PRD đối chiếu review V1 00:55–01:15, 02:20–05:06, 05:17–06:26; mã FR/giờ và luồng đối chiếu V2 00:42–05:57, 07:42–10:50. Mốc là khoảng tìm đoạn review tài liệu, không phải thời điểm một bug app. Ý lời nói dùng bản nhận dạng đã nêu giới hạn ở báo cáo video trước, không trích nguyên văn hay coi là phê duyệt thêm chức năng.

## Quy tắc giữ phạm vi

Nguồn FR là 3 PRD nghiệp vụ, nguồn giờ là workbook Resource. Tài liệu tổng hợp cũ và thư mục unisupport-prd-extracted là bản tham chiếu, không trộn vào bản hiện tại. Không xác nhận QA/UAT đã Pass khi chưa có kết quả chạy. Không tính lại chi phí nhân sự trong lần sửa PRD này.
