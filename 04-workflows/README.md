# Quy Trình Nghiệp Vụ Tiêu Chuẩn (Workflows & Business Sequences)

## 1. Tổng Quan
Thư mục này tài liệu hóa chi tiết 6 quy trình nghiệp vụ tiêu chuẩn (Standard Workflows) thuộc hệ thống **UniSupport** tại **Aurora University**. Các quy trình đảm bảo tính liên tục, nhất quán dữ liệu giữa 3 vai trò: Sinh viên, Nhân viên các phòng ban và Quản lý.

---

## 2. Danh Sách Quy Trình Nghiệp Vụ

| Mã Workflow | Tên Quy Trình | Vai Trò Chính | Đầu Ra Chính |
| :--- | :--- | :--- | :--- |
| **`WF-01`** | Sinh viên gửi yêu cầu hỗ trợ & Nhận mã Ticket | Sinh viên | Ticket mới (`NEW`) + Mã Ticket duy nhất. |
| **`WF-02`** | Nhân viên tiếp nhận & Phân loại / Đánh giá độ ưu tiên | Nhân viên | Ticket đang xử lý (`IN_PROGRESS`) + Assignee. |
| **`WF-03`** | Yêu cầu sinh viên bổ sung thông tin / giấy tờ | Nhân viên & Sinh viên | Ticket chờ bổ sung (`NEED_MORE_INFO`). |
| **`WF-04`** | Chuyển tiếp yêu cầu sang phòng ban khác | Nhân viên | Ticket chuyển giao (`TRANSFERRED`). |
| **`WF-05`** | Cập nhật kết quả & Đóng yêu cầu | Nhân viên | Ticket hoàn tất (`CLOSED`) + Kết quả giải quyết. |
| **`WF-06`** | Sinh viên nhận kết quả & Đánh giá mức độ hài lòng | Sinh viên | Đánh giá sao & Nhận xét hài lòng. |