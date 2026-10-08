# QTTN 01: Sinh Viên Gửi Yêu Cầu Hỗ Trợ & Nhận Mã Ticket (WF-01)

## 1. Mục Tiêu Quy Trình
Mô tả trình tự thao tác giúp sinh viên khởi tạo một yêu cầu hỗ trợ mới trên hệ thống UniSupport, đính kèm minh chứng hợp lệ và nhận mã Ticket duy nhất để theo dõi.

---

## 2. Tác Nhân Tham Gia (Actors)
* **Sinh viên:** Người khởi tạo yêu cầu.
* **Hệ thống UniSupport:** Tiếp nhận, xác thực validation, sinh mã Ticket và lưu CSDL.

---

## 3. Lược Đồ Quy Trình (Sequence Diagram)

```text
[Sinh viên]                  [Giao diện Web]                [Backend / CSDL]
    │                               │                              │
    │ ─── 1. Chọn Tạo Ticket ──────>│                              │
    │ ─── 2. Nhập thông tin & File ─>│                              │
    │ ─── 3. Nhấn "Gửi yêu cầu" ───>│                              │
    │                               │ ─── 4. Kiểm tra Validation ─>│
    │                               │                              │ (Hợp lệ)
    │                               │ ─── 5. Sinh Mã Ticket ──────>│
    │                               │ ─── 6. Lưu Ticket (NEW) ────>│
    │                               │<─── 7. Trả về thành công ────│
    │<─── 8. Hiển thị Mã Ticket ────│                              │
```
---

## 4. Các Bước Thực Hiện
* **Sinh viên**: Đăng nhập hệ thống bằng tài khoản sinh viên, chọn chức năng Tạo Ticket hỗ trợ.
* **Sinh viên**: Chọn Nhóm vấn đề, nhập Tiêu đề, nội dung Mô tả chi tiết và đính kèm file (ảnh PNG/JPG hoặc PDF, tối đa 5MB/file) nếu có.
* **Sinh viên**: Bấm nút Gửi yêu cầu.
* **Hệ thống**: Kiểm tra tính hợp lệ của dữ liệu (kiểm tra trường bắt buộc, khoảng trắng, dung lượng/định dạng file, chống click đúp/retry trùng lặp).
* **Hệ thống**: Sinh mã Ticket duy nhất (ví dụ: TK-20261007-001), gán trạng thái NEW và lưu dữ liệu gắn liền với sinh viên gửi.
* **Hệ thống**: Hiển thị thông báo gửi thành công kèm Mã Ticket, đồng thời phát thông báo nội bộ xác nhận cho sinh viên.

---

## 5. Ràng Buộc & Quy Tắc Nghiệp Vụ Liên Quan
* Bắt buộc phải có thông tin Mô tả vấn đề và Nhóm vấn đề.
* Một thao tác gửi chỉ tạo đúng 01 Ticket, chống tạo trùng do mạng lag hay nhấp nút nhiều lần liên tiếp.