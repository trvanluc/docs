# TEAM CHARTER (BẢN ĐIỀU LỆ NHÓM)

*Dự án: UniSupport - Student Support Management System*

## Mục đích của Team Charter

Team Charter này quy định cách Nhóm 3 phối hợp và làm việc trong dự án UniSupport. Tài liệu giúp mỗi thành viên, bao gồm thành viên mới, hiểu rõ vai trò, trách nhiệm, công cụ sử dụng, quy trình thực hiện công việc, nguyên tắc giao tiếp và người cần liên hệ khi gặp vấn đề.

## 1. Tổng quan nhóm và Giá trị làm việc

| Hạng mục | Thông tin |
|---|---|
| Dự án | UniSupport – Student Support Management System (Aurora University) |
| Đơn vị thực hiện | Nhóm 3 |

**Giá trị làm việc của nhóm:**

- Minh bạch: chủ động chia sẻ tiến độ thật, kể cả khi chưa xong hoặc gặp khó khăn.
- Tôn trọng: lắng nghe ý kiến khác biệt trước khi phản biện, không áp đặt quan điểm cá nhân.
- Chủ động nhận trách nhiệm: khi có sai sót, ưu tiên khắc phục trước khi tìm nguyên nhân/lỗi của ai.
- Chất lượng trên tốc độ: không bàn giao việc ẩu chỉ để kịp deadline cá nhân.

## 2. Nguồn lực và Công cụ làm việc

| Hạng mục | Công cụ | Mục đích sử dụng |
|---|---|---|
| Kênh trao đổi chính | Discord (chia kênh chuyên môn) | Giao tiếp hàng ngày, họp nhanh, thông báo khẩn |
| Quản lý công việc | Clickup | Theo dõi tiến độ theo mô hình Kanban (To do/Doing/Done) |
| Kho mã nguồn | GitHub | Lưu trữ mã nguồn, quản lý phiên bản theo Git Flow |
| Review & CI/CD | GitHub Pull Request | Review code trước khi merge vào nhánh chính |
| Thiết kế giao diện | Figma | Thiết kế Design System, Wireframe, Prototype |
| Lưu trữ tài liệu | Google Drive | Lưu trữ đặc tả, biên bản họp và tài liệu dự án |
| Hạ tầng phát triển & kiểm thử | Môi trường local và môi trường test nội bộ | Phát triển, tích hợp và kiểm thử trước khi triển khai |
| Hạ tầng triển khai | Server do Aurora University cấp | Triển khai môi trường kiểm thử (Staging) và Production |

## 3. Vai trò và Trách nhiệm

| STT | Vai trò | Trách nhiệm cốt lõi |
|---|---|---|
| 1 | Project Manager (PM) | Điều phối tiến độ chung, quản lý rủi ro, liên hệ khách hàng, chủ trì họp nhóm |
| 2 | Business Analyst (BA) | Khảo sát nghiệp vụ, lập đặc tả (SRS), xác nhận tiêu chí nghiệm thu UAT |
| 3 | UI/UX Designer | Thiết kế Design System, Wireframe, Prototype |
| 4 | Technical Lead (TL) | Kiến trúc hệ thống, lựa chọn công nghệ, review các thay đổi kỹ thuật quan trọng, gỡ vướng kỹ thuật. |
| 5 | Frontend Developer 1 | Lập trình màn hình/component theo mockup, phối hợp cùng FE2 chia màn hình phụ trách |
| 6 | Frontend Developer 2 | Lập trình màn hình/component theo mockup, phối hợp cùng FE1 chia màn hình phụ trách |
| 7 | Backend Developer 1 | Lập trình API, xử lý nghiệp vụ, viết Unit Test BE, phối hợp cùng BE2 chia module phụ trách |
| 8 | Backend Developer 2 | Lập trình API, xử lý nghiệp vụ, viết Unit Test BE, phối hợp cùng BE1 chia module phụ trách |
| 9 | QA/QC Engineer | Lập kế hoạch kiểm thử, thiết kế test case, điều phối kiểm thử chức năng và hồi quy |
| 10 | DevOps / Deployment Engineer | Cấu hình CI/CD, chuẩn bị môi trường, hỗ trợ kiểm thử và đóng gói bàn giao |

***Nguyên tắc uỷ quyền (Backup):*** Khi PM vắng mặt, BA tạm quyền điều phối. Việc review Pull Request thông thường được thực hiện bởi reviewer phù hợp. Khi TL vắng mặt, các quyết định kỹ thuật quan trọng hoặc thay đổi ảnh hưởng kiến trúc/toàn hệ thống được chuyển cho thành viên được ủy quyền.

## 4. Quy tắc hoạt động và Phối hợp nhóm

### 4.1 Giờ làm việc & Cam kết tiến độ

- **Khung giờ làm việc chung:** 20h00–22h00 các ngày trong tuần (linh hoạt theo lịch cá nhân).
- **Cam kết deadline:** thành viên tự quản lý tiến độ task; Nếu có nguy cơ chậm deadline, thành viên phải thông báo cho PM ngay khi phát hiện, ưu tiên trước deadline 24–48 giờ.
- **Báo cáo công việc:** cập nhật trạng thái (To do/Doing/Done) trên Kanban board trước 22h00 hàng ngày.
- **Quy chuẩn Git:** nhánh sử dụng định dạng *feature/[task-id]-[short-description]* hoặc bugfix/[task-id]-[short-description], sử dụng lowercase và kebab-case. Mọi Pull Request vào nhánh chính phải được ít nhất một reviewer có đủ chuyên môn trong phạm vi liên quan review và approve trước khi merge. Technical Lead chỉ bắt buộc tham gia review đối với các thay đổi ảnh hưởng đến kiến trúc hệ thống, công nghệ dùng chung, bảo mật hoặc nhiều module.
- **Chuẩn hoàn thành (DoD):** task chỉ tính là xong khi code chạy đúng chức năng, vượt qua kiểm thử cơ bản (Unit Test/QA verify) và tài liệu liên quan đã cập nhật.

### 4.2 Chuẩn mực giao tiếp & Họp nhóm

- **Thời gian phản hồi (SLA):** kênh chung phản hồi trong vòng 6–12 giờ; kênh khẩn cấp/tag trực tiếp phản hồi trong vòng 1–2 giờ.
- **Họp định kỳ:** 1 buổi/tuần vào tối Chủ Nhật. PM gửi Agenda trước 4 giờ. Vắng mặt phải báo trước tối thiểu 2 giờ.
- **Biên bản họp:** luân phiên ghi biên bản, ghi rõ Action Items, người chịu trách nhiệm và deadline.

### 4.3 Quy trình thực hiện công việc

Mọi task trong dự án được thực hiện theo quy trình chung:

1. **Nhận task:** Thành viên nhận task được phân công trên clickup và kiểm tra mô tả, deadline, tài liệu liên quan và tiêu chí hoàn thành.
2. **Bắt đầu thực hiện:** Thành viên chuyển trạng thái task từ **To do → Doing**. Nếu yêu cầu chưa rõ, phải trao đổi với người phụ trách liên quan trước khi thực hiện.
3. **Thực hiện và cập nhật:** Thành viên thực hiện công việc theo trách nhiệm của vai trò được giao và cập nhật tiến độ trên clickup . Với task lập trình, code được thực hiện trên branch riêng theo Git convention của nhóm.
4. **Review và kiểm thử:** Khi hoàn thành phần thực hiện, code được tạo Pull Request để review. Các chức năng cần kiểm thử được QA/QC kiểm tra trước khi xác nhận hoàn thành.
5. **Hoàn thành:** Task chỉ được chuyển sang **Done** khi đáp ứng Definition of Done và các tài liệu liên quan đã được cập nhật.

**Luồng chung đối với development task:**

Task Assigned → To do → Doing → Review → QA Verify → Done

***Lưu ý:*** Đối với non-development task, bước review/verification được thực hiện bởi người có thẩm quyền tương ứng với vai trò và deliverable.

### 4.4 Kênh liên hệ và xử lý chuyển cấp

Khi gặp vấn đề trong quá trình làm việc, thành viên ưu tiên liên hệ với người phụ trách trực tiếp của lĩnh vực trước khi chuyển vấn đề lên cấp cao hơn.

| Vấn đề | Liên hệ đầu tiên | Người xử lý tiếp theo |
|---|---|---|
| Yêu cầu nghiệp vụ | Business Analyst | Project Manager (PM) |
| UI/UX / Design | UI/UX Designer | Project Manager |
| Frontend / Component | Frontend Developer phụ trách | Technical Lead |
| Backend / API | Backend Developer phụ trách | Technical Lead |
| Kiến trúc / Vấn đề kỹ thuật | Technical Lead | Project Manager |
| Testing / Quality / Bug | QA/QC Engineer | Technical Lead / Project Manager |
| Git / Pull Request | Technical Lead | Project Manager |
| CI/CD / Server / Deployment | DevOps Engineer | Technical Lead / Project Manager |
| Task / Deadline / Phân công | Project Manager | — |
| Conflict giữa thành viên | Trao đổi trực tiếp giữa các bên | Project Manager |

*Các trao đổi được thực hiện trên Discord. Nếu vấn đề ảnh hưởng đến task, tiến độ hoặc quyết định kỹ thuật, kết quả trao đổi phải được cập nhật vào clickup, GitHub hoặc Decision Log tương ứng.*

## 5. Quy trình ra quyết định và Giải quyết mâu thuẫn

### 5.1 Cơ chế ra quyết định

- **Cấp kỹ thuật/module:** người phụ trách trực tiếp module đó (FE1/FE2 với component được giao, BE1/BE2 với API/module được giao) có quyền quyết định giải pháp triển khai; TL quyết định các vấn đề kiến trúc ảnh hưởng toàn hệ thống.
- **Cấp ảnh hưởng nhiều bên:** thảo luận tập thể trong buổi họp, biểu quyết theo đa số (tối thiểu 6/10 thành viên đồng thuận).
- **Trường hợp bế tắc hoặc khẩn cấp:** PM là người quyết định cuối cùng. Mọi thay đổi lớn được ghi vào Decision Log.

### 5.2 Quy trình 3 bước giải quyết xung đột

- Bước 1 — Đối thoại trực tiếp: hai bên bất đồng trao đổi trực tiếp, tôn trọng, trong vòng 24 giờ.
- Bước 2 — Thảo luận tập thể: nếu không đồng thuận, đưa ra buổi họp nhóm gần nhất.
- Bước 3 — Phân xử bởi PM: PM lắng nghe các bên, đánh giá tác động tiến độ/chất lượng và đưa ra quyết định cuối cùng.

## 6. Trách nhiệm và Chế tài xử lý vi phạm

*Nhóm kỳ vọng: tỷ lệ hoàn thành task đúng hạn ≥85%, tham gia họp đầy đủ ≥90%, tuân thủ SLA phản hồi 100%. Đây là kỳ vọng chung để cả nhóm tự đánh giá, không phải hệ thống theo dõi hiệu suất chính thức.*

Áp dụng đối với vi phạm lặp lại (trễ deadline không báo trước, vắng họp không lý do, không cập nhật tiến độ):

- Lần 1 — Nhắc nhở riêng: PM trao đổi trực tiếp, làm rõ khó khăn và nhắc lại cam kết.
- Lần 2 — Ghi nhận biên bản: nêu trong họp nhóm và ghi chính thức vào biên bản.
- Lần 3 — Tái cấu trúc công việc: PM điều chỉnh/tái phân bổ task; ghi nhận vào đánh giá cuối dự án.
