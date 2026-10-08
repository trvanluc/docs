# Vòng Đời Phiếu Hỗ Trợ (Ticket Lifecycle)

Vòng đời của một Ticket hỗ trợ trong hệ thống UniSupport trải qua 5 giai đoạn chính từ khi khởi tạo cho đến khi hoàn tất và đánh giá:

```text
[1. Khởi tạo] ──> [2. Tiếp nhận & Phân loại] ──> [3. Xử lý & Bổ sung] ──> [4. Hoàn thành] ──> [5. Đánh giá]
Chi Tiết Các Giai Đoạn
Giai đoạn 1: Khởi Tạo (Created)
Thao tác: Sinh viên chọn nhóm vấn đề, nhập nội dung mô tả, đính kèm file minh chứng (ảnh/PDF) và bấm Gửi yêu cầu.

Kết quả: Hệ thống sinh mã Ticket duy nhất và lưu trạng thái ban đầu là NEW (Mới).

Giai đoạn 2: Tiếp Nhận & Phân Loại (Triage & Assignment)
Thao tác: Nhân viên thuộc phòng ban liên quan kiểm tra danh sách Ticket mới, xác định tính hợp lệ, gán độ ưu tiên và phân công cho nhân viên cụ thể (IN_PROGRESS).

Chuyển tiếp (nếu có): Nếu Ticket gửi sai phòng ban, nhân viên thực hiện chuyển tiếp sang phòng ban phù hợp (TRANSFERRED).

Giai đoạn 3: Xử Lý & Yêu Cầu Bổ Sung (Processing & Supplementation)
Thao tác: Nhân viên nghiên cứu và xử lý nghiệp vụ.

Trường hợp thiếu thông tin: Nhân viên đổi trạng thái sang NEED_MORE_INFO và gửi tin nhắn yêu cầu sinh viên bổ sung hồ sơ/giấy tờ.

Phản hồi từ sinh viên: Sinh viên cập nhật file/thông tin bổ sung, Ticket chuyển lại về IN_PROGRESS.

Giai đoạn 4: Hoàn Thành & Giải Quyết (Resolved / Closed)
Thao tác: Nhân viên ghi nhận rõ nội dung kết quả giải quyết lên hệ thống và chuyển trạng thái Ticket sang CLOSED (Hoàn thành).

Kết quả: Sinh viên nhận được thông báo kết quả giải quyết trực tiếp trên hệ thống.

Giai đoạn 5: Nhận Kết Quả & Đánh Giá (Feedback & Rating)
Thao tác: Sinh viên xem kết quả xử lý. Nếu thỏa mãn, sinh viên thực hiện đánh giá mức độ hài lòng (thang điểm 1 - 5 sao và lời nhắn bổ sung).