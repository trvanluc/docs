# Hiện Trạng & Bài Toán Nghiệp Vụ (Problem Statement)

## 1. Hiện Trạng Tiếp Nhận Yêu Cầu Tại Aurora University

Hiện tại, công tác tiếp nhận và phản hồi yêu cầu hỗ trợ sinh viên tại Aurora University đang phân tán qua nhiều kênh không chuẩn hóa:
1. **Email cá nhân / Email phòng ban**: Sinh viên gửi email đến giảng viên, chuyên viên hoặc hòm thư chung phòng Đào tạo/CTHSSV.
2. **Google Forms / Biểu mẫu trực tuyến lẻ tẻ**: Mỗi phòng ban tự tạo form riêng, dữ liệu không đồng bộ.
3. **Tin nhắn mạng xã hội / Ứng dụng chat**: Zalo, Fanpage, Messenger.
4. **Tiếp nhận trực tiếp**: Sinh viên đến nộp hồ sơ giấy tại văn phòng một cửa.

---

## 2. Các Điểm Nghẽn & Khó Khăn Chính (Key Pain Points)

### 2.1 Thiếu đầu mối tập trung và mất mát dữ liệu
- Yêu cầu của sinh viên bị rải rác ở nhiều nơi, không có cơ sở dữ liệu tập trung để tra cứu lại lịch sử hỗ trợ.
- Nguy cơ thất lạc thông tin hoặc trôi email trong các đợt cao điểm (đầu khóa học, đăng ký môn học, xét tốt nghiệp).

### 2.2 Phản hồi chậm và nguy cơ bỏ sót yêu cầu
- Thiếu hệ thống mã định danh (Ticket ID), khiến việc tra cứu trạng thái gặp khó khăn.
- Không có cơ chế cảnh báo yêu cầu quá hạn hoặc phân công trách nhiệm rõ ràng, dẫn đến tình trạng "đùn đẩy" công việc giữa các bộ phận.

### 2.3 Xử lý trùng lặp và phản hồi không thống nhất
- Nhiều nhân viên cùng phản hồi một email hoặc xử lý trùng một hồ sơ gây lãng phí nguồn lực.
- Thông tin hướng dẫn sinh viên giữa các nhân viên trong cùng phòng ban đôi khi không nhất quán.

### 2.4 Sinh viên thiếu thông tin tiến độ
- Sinh viên không biết yêu cầu của mình đang ở bước nào, ai đang thụ lý, khi nào có kết quả.
- Dẫn đến việc sinh viên phải gửi lại yêu cầu nhiều lần hoặc đến trực tiếp văn phòng để hỏi, gây quá tải bộ phận một cửa.

### 2.5 Ban quản lý thiếu công cụ giám sát và số liệu báo cáo
- Trưởng phòng ban và Ban giám hiệu không có số liệu thực tế về:
  - Tổng số yêu cầu tiếp nhận / đã giải quyết / còn tồn đọng.
  - Thời gian xử lý trung bình của từng phòng ban/nhân viên.
  - Các nhóm vấn đề phát sinh phổ biến nhất để cải tiến quy trình đào tạo/vận hành.
  - Mức độ hài lòng của sinh viên đối với dịch vụ hỗ trợ.

---

## 3. Tác Động Tiêu Cực (Impact Analysis)
[Kênh tiếp nhận rời rạc]
│
├──► Thất lạc / Bỏ sót yêu cầu ───────► Sinh viên bức xúc, giảm uy tín nhà trường
├──► Xử lý trùng lặp / Chậm trễ ──────► Lãng phí thời gian & nhân lực vận hành
└──► Thiếu báo cáo số liệu ───────────► Quản lý không thể điều phối & cải tiến quy trình

---

## 4. Giải Pháp Mong Muốn Từ UniSupport

Hệ thống UniSupport giải quyết các vấn đề trên thông qua:
1. **Chuẩn hóa đầu mối**: Mọi yêu cầu hỗ trợ phải đi qua duy nhất một Web Portal. Mỗi yêu cầu sinh ra một Mã Ticket duy nhất.
2. **Minh bạch tiến độ**: Sinh viên xem được nhật ký chuyển trạng thái và đơn vị đang thụ lý theo thời gian thực.
3. **Quy trình hóa vận hành**: Quy định rõ luồng Tiếp nhận/phân loại -> Bổ sung hoặc chuyển phòng khi cần -> Cập nhật kết quả -> Sinh viên xem/đánh giá -> Đóng theo vòng đời hiện có.
4. **Dashboard báo cáo trực quan**: Ban quản lý nắm bắt ngay các chỉ số KPI, ticket quá hạn và đánh giá mức độ hài lòng của sinh viên.
