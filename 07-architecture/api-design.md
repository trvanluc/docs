# [ARC-04] Thiết kế RESTful API (API Design Standard)

Tài liệu này chuẩn hóa quy cách thiết kế RESTful API cho toàn bộ các phân hệ trong hệ thống **UniSupport**, bao gồm chuẩn HTTP Status Codes, định dạng Request/Response và danh sách Endpoints chính.

---

## 🌐 1. Quy chuẩn API Tổng quan

* **Giao thức:** HTTPS
* **Đường dẫn cơ sở (Base URL):** `https://unisupport.aurora.edu.vn/api/v1`
* **Định dạng dữ liệu:** `application/json`
* **Mã hóa:** UTF-8

### **1.1. Cấu trúc Response Chuẩn (Standard Response Format)**

#### Response Thành công (`200 OK`, `201 Created`):
```json
{
  "success": true,
  "code": 200,
  "message": "Thao tác thành công",
  "data": { ... }
}
```

#### Response Phân trang (Pagination Response):
```json
{
  "success": true,
  "code": 200,
  "data": [ ... ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total_items": 45,
    "total_pages": 5
  }
}
```

#### Response Lỗi (`400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `500 Internal Error`):
```json
{
  "success": false,
  "code": 400,
  "error_code": "INVALID_INPUT",
  "message": "Nội dung mô tả là bắt buộc.",
  "errors": [
    {
      "field": "description",
      "message": "Mô tả không được để trống"
    }
  ]
}
```
# 📌 2. Danh sách API Endpoints Chính

## 2.1. Authentication & System (`/auth`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| --- | --- | --- | --- |
| **POST** | `/auth/login` | Public | Đăng nhập hệ thống & lấy JWT Token |
| **GET** | `/auth/me` | Authenticated | Lấy thông tin tài khoản đang đăng nhập |
| **POST** | `/auth/logout` | Authenticated | Đăng xuất |

## 2.2. Phân hệ Sinh viên (`/student`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| --- | --- | --- | --- |
| **POST** | `/student/tickets` | Student | Tạo mới Ticket hỗ trợ (kèm upload file) |
| **GET** | `/student/tickets` | Student | Xem danh sách Ticket cá nhân đã gửi |
| **GET** | `/student/tickets/{ticket_code}` | Student | Xem chi tiết tiến độ Ticket & lịch sử phản hồi |
| **POST** | `/student/tickets/{id}/supplement` | Student | Bổ sung thông tin/giấy tờ theo yêu cầu Nhân viên |
| **POST** | `/student/tickets/{id}/rating` | Student | Đánh giá mức độ hài lòng (1-5 sao) khi hoàn tất |

## 2.3. Phân hệ Nhân viên (`/staff`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| --- | --- | --- | --- |
| **GET** | `/staff/tickets` | Staff, Manager/Admin | Lấy danh sách Ticket thuộc phòng ban phụ trách |
| **POST** | `/staff/tickets/{id}/claim` | Staff | Nhận phụ trách (Claim) Ticket |
| **PATCH** | `/staff/tickets/{id}/triage` | Staff | Phân loại & cập nhật độ ưu tiên Ticket |
| **POST** | `/staff/tickets/{id}/transfer` | Staff | Chuyển Ticket sang phòng ban khác |
| **POST** | `/staff/tickets/{id}/request-supplement` | Staff | Yêu cầu Sinh viên bổ sung giấy tờ/thông tin |
| **POST** | `/staff/tickets/{id}/resolve` | Staff | Cập nhật kết quả giải quyết & Đóng Ticket |

## 2.4. Phân hệ Quản lý & Admin (`/management`)

| Method | Endpoint | Quyền truy cập | Mô tả |
| --- | --- | --- | --- |
| **GET** | `/management/dashboard/overview` | Manager/Admin | Số liệu tổng quan (Ticket mới, đang xử lý, quá hạn) |
| **GET** | `/management/dashboard/metrics` | Manager/Admin | Báo cáo SLA, thời gian xử lý trung bình, điểm đánh giá |
| **GET** | `/management/users` | Admin | Danh sách tài khoản hệ thống |
| **POST** | `/management/users` | Admin | Tạo tài khoản mới & phân quyền vai trò |
| **PATCH** | `/management/users/{id}` | Admin | Cập nhật thông tin/trạng thái tài khoản |
