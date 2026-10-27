# Chỉ Tiêu Thành Công Và Phương Pháp Kiểm Chứng (Success Metrics)

Tài liệu này định nghĩa các chỉ tiêu thành công của UniSupport, phương pháp đo, nguồn dữ liệu và bằng chứng nghiệm thu cho từng chỉ tiêu.

## 1. Quy Ước Kiểm Chứng

- **Thời điểm:** giai đoạn kiểm thử hệ thống và UAT.
- **Môi trường và dữ liệu:** môi trường kiểm thử với dữ liệu giả lập (`08-project/assumptions.md` mục 5).
- **Trách nhiệm:** QA/QC thực hiện đo và lưu bằng chứng; BA xác nhận kết quả so với chỉ tiêu.
- **Kết quả:** mỗi chỉ tiêu được ghi nhận `Đạt` hoặc `Không đạt` kèm số liệu đo và bằng chứng.

## 2. Danh Sách Chỉ Tiêu

| Mã | Chỉ tiêu | Ngưỡng đạt | Mục tiêu sản phẩm |
| :--- | :--- | :--- | :--- |
| SM-01 | Yêu cầu có người chịu trách nhiệm rõ ràng | ≥ 90% | G-03 |
| SM-02 | Yêu cầu có trạng thái theo dõi được | ≥ 90% | G-02 |
| SM-03 | Giảm yêu cầu bị bỏ sót hoặc xử lý trùng lặp | 0 Ticket bị mất, 0 Ticket trùng trong kịch bản kiểm thử | G-03 |
| SM-04 | Giảm số lần sinh viên phải liên hệ để hỏi tiến độ | Giảm ≥ 30% so với quy trình hiện tại | G-02 |
| SM-05 | Ban quản lý nhận biết được yêu cầu quá hạn | Số liệu sắp quá hạn/quá hạn khớp 100% với đáp án dữ liệu kiểm thử | G-04 |
| SM-06 | Xác định được các vấn đề sinh viên thường gặp | Số Ticket theo Nhóm vấn đề khớp 100% với đáp án dữ liệu kiểm thử | G-04 |
| SM-07 | Dữ liệu chỉ được truy cập bởi người có thẩm quyền | 0 trường hợp truy cập thành công ngoài phạm vi quyền | G-05 |

## 3. Phương Pháp Đo

| Mã | Công thức / cách đo | Nguồn dữ liệu | Kịch bản | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- |
| SM-01 | Số Ticket ở `IN_PROGRESS` hoặc `WAITING_STUDENT` có người phụ trách chính / tổng số Ticket ở hai trạng thái này, tại thời điểm đo. Mọi Ticket, kể cả `NEW`, có phòng ban phụ trách. | `BR-OWN-01`; FR-MGT-05 (khối lượng theo nhân viên, số Ticket theo trạng thái); FR-STF-01 (hàng chờ chưa có người phụ trách) | TS-STF-01, TS-STF-02, TS-STF-05, TS-MGT-05 | Ảnh Dashboard và hàng chờ tại thời điểm đo; bảng tính tỷ lệ |
| SM-02 | Số Ticket mà sinh viên sở hữu xem được trạng thái hiện tại và lịch sử được phép xem / tổng số Ticket trong bộ dữ liệu kiểm thử | `02-domain/ticket-model.md` (trạng thái là thông tin bắt buộc); FR-STU-03 | TS-STU-02, TS-STU-03 | Danh sách Ticket đã kiểm tra và kết quả từng Ticket |
| SM-03 | (a) Bỏ sót: mọi Ticket tạo thành công có mã Ticket và xuất hiện trong hàng chờ đúng phòng ban; Ticket chưa xử lý xong được nhận diện khi sắp quá hạn/quá hạn. (b) Trùng lặp: gửi lặp không tạo nhiều Ticket; một Ticket có tối đa một người phụ trách chính. | FR-STU-02 (AC-02-06); FR-STF-02 (AC-02-02); FR-STF-01; FR-STF-03 | TS-STU-02, TS-STF-01, TS-STF-02, TS-STF-03 | Kết quả kịch bản; số Ticket trước/sau khi chạy |
| SM-04 | Mức giảm = (L₀ − L₁) / L₀. L₀: số lần liên hệ trong quy trình hiện tại; L₁: số lần liên hệ khi dùng UniSupport. Đo trên bộ 5 câu hỏi tiến độ (mục 4), mỗi câu không trả lời được trong hệ thống tính là một lần liên hệ. | Quy trình hiện tại: `01-product/problem-statement.md` mục 2.4. UniSupport: FR-STU-03, FR-STU-04 | TS-STU-03, TS-STU-04, TS-STU-05, TS-STU-06 | Bảng đếm theo từng kịch bản và người thực hiện |
| SM-05 | So sánh số Ticket sắp quá hạn/quá hạn trên Dashboard với đáp án tính trước của dữ liệu kiểm thử | FR-MGT-05; FR-STF-03; `BR-DUE-02` | TS-STF-03, TS-MGT-05 | Bảng đáp án và ảnh Dashboard |
| SM-06 | So sánh số Ticket theo Nhóm vấn đề trên báo cáo xu hướng với đáp án tính trước | FR-MGT-06 | TS-MGT-06 | Bảng đáp án và ảnh báo cáo |
| SM-07 | Thực hiện truy cập Ticket, file và chức năng quản trị ngoài phạm vi quyền cho từng vai trò; đếm số lần truy cập thành công | NFR-SEC; `BR-FILE-01`; `01-product/actors-and-roles.md` mục 3 | `test-scenarios.md` mục 4 | Ma trận quyền kèm kết quả từng ca |

## 4. Bộ Câu Hỏi Tiến Độ (SM-04)

| STT | Câu hỏi của sinh viên | Thông tin tương ứng trong UniSupport |
| :---: | :--- | :--- |
| 1 | Yêu cầu đã được tiếp nhận chưa? | Mã Ticket và trạng thái (FR-STU-02, FR-STU-03) |
| 2 | Phòng ban hoặc ai đang xử lý? | Phòng ban/người phụ trách (FR-STU-03) |
| 3 | Yêu cầu đang ở bước nào? | Trạng thái và lịch sử xử lý (FR-STU-03) |
| 4 | Cần bổ sung thông tin gì? | Thông báo và nội dung yêu cầu bổ sung (FR-STU-04, FR-STU-05) |
| 5 | Đã có kết quả chưa? | Thông báo và kết quả xử lý (FR-STU-04, FR-STU-06) |

## 5. Phạm Vi Áp Dụng

- Kết quả SM-01 đến SM-07 phản ánh bộ dữ liệu và kịch bản kiểm thử, không phải số liệu vận hành thực tế.
- SM-04 được đo bằng kịch bản và usability test; số liệu vận hành thực tế chỉ có sau khi hệ thống được đưa vào sử dụng.
