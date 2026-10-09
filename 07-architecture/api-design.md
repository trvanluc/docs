# Thiết Kế RESTful API Chuẩn (RESTful API Design Specification)

## 1. Nguyên Tắc Thiết Kế Chung (General API Standards)
- **Base URL:** `https://api-unisupport.aurora.edu.vn/api/v1`
- **Định dạng Truyền/Nhận dữ liệu:** `application/json` (trừ API Upload file sử dụng `multipart/form-data`).
- **Authentication & Authorization:** Header `Authorization: Bearer <JWT_ACCESS_TOKEN>` áp dụng cho tất cả API Private.
- **Pagination Standard:** Quản lý bằng Request Query Params `page` (Mặc định `1`) và `limit` (Mặc định `20`, Tối đa `50`).
- **Idempotency Handling:** API tạo mới (`POST /tickets`) bắt buộc gửi Header `X-Client-Request-ID: <UUID_v4>`.

---

## 2. Phân Hệ Xác Thực (`/api/v1/auth`)

### 2.1. `POST /api/v1/auth/login`
- **Mô tả:** Đăng nhập hệ thống bằng tài khoản nhà trường (SSO hoặc Local Account).
- **Headers:** `Content-Type: application/json`
- **Request Body:**
```json
{
  "username": "stu20260001",
  "password": "Password123!"
}
```
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "user_id": "usr_stu_20260001",
    "full_name": "Nguyễn Văn A",
    "role": "STUDENT",
    "department_id": null,
    "access_token": "eyJhbGciOi...xYZ123",
    "token_type": "Bearer",
    "expires_in": 900
  }
}
```

### 2.2. `POST /api/v1/auth/logout`
- **Mô tả:** Đăng xuất hệ thống, thêm Token hiện tại vào Redis Blacklist.
- **Headers:** `Authorization: Bearer <token>`
- **Response (200 OK):**
```json
{
  "success": true,
  "message": "Đăng xuất thành công."
}
```

---

## 3. Phân Hệ Sinh Viên (`/api/v1/student`)

### 3.1. `POST /api/v1/student/tickets`
- **Mô tả:** Khởi tạo Ticket mới kèm minh chứng.
- **Headers:** `Authorization: Bearer <token>`, `Content-Type: multipart/form-data`, `X-Client-Request-ID: <UUID_v4>`
- **Request Form-Data:**
  - `category_id`: `"cat_edu_01"` (String, Required)
  - `title`: `"Xin hoãn thi môn CSDL"` (String, Required, 10-200 chars)
  - `description`: `"Em bị ốm vào ngày thi..."` (String, Required, 20-2000 chars)
  - `attachments`: Binary File Array (Optional, Max 3 files, $\le 5\text{MB/file}$)
- **Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "ticket_id": "TK-20261009-0001",
    "status": "NEW",
    "created_at": "2026-10-09T13:15:00.000Z",
    "sla_target_at": "2026-10-10T13:15:00.000Z"
  }
}
```

### 3.2. `GET /api/v1/student/tickets`
- **Mô tả:** Lấy danh sách Ticket cá nhân của Sinh viên.
- **Query Params:** `status` (Optional), `page` (Default 1), `limit` (Default 20).
- **Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "ticket_id": "TK-20261009-0001",
      "category_name": "Đào tạo",
      "title": "Xin hoãn thi môn CSDL",
      "status": "NEW",
      "created_at": "2026-10-09T13:15:00.000Z"
    }
  ],
  "pagination": {
    "current_page": 1,
    "limit": 20,
    "total_records": 1,
    "total_pages": 1
  }
}
```

### 3.3. `POST /api/v1/student/tickets/{ticket_id}/supplement`
- **Mô tả:** Gửi bổ sung tài liệu/ghi chú khi Ticket ở trạng thái `NEED_MORE_INFO`.
- **Headers:** `Content-Type: multipart/form-data`
- **Request Form-Data:**
  - `note`: `"Em đã bổ sung giấy khám sức khỏe."` (String, Required)
  - `attachments`: Binary File Array (Optional)
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "ticket_id": "TK-20261009-0001",
    "status": "IN_PROGRESS",
    "updated_at": "2026-10-09T14:00:00.000Z"
  }
}
```

### 3.4. `POST /api/v1/student/tickets/{ticket_id}/rate`
- **Mô tả:** Gửi đánh giá sao và nhận xét cho Ticket đã hoàn tất.
- **Request Body:**
```json
{
  "rating_score": 5,
  "rating_comment": "Nhân viên hỗ trợ rất nhanh và nhiệt tình!"
}
```

---

## 4. Phân Hệ Nhân Viên (`/api/v1/staff`)

### 4.1. `POST /api/v1/staff/tickets/{ticket_id}/claim`
- **Mô tả:** Tiếp nhận Ticket từ Queue chung của phòng ban và thiết lập độ ưu tiên.
- **Request Body:**
```json
{
  "priority": "HIGH"
}
```
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "ticket_id": "TK-20261009-0001",
    "status": "IN_PROGRESS",
    "assignee_id": "usr_stf_1002",
    "priority": "HIGH"
  }
}
```

### 4.2. `POST /api/v1/staff/tickets/{ticket_id}/transfer`
- **Mô tả:** Điều chuyển Ticket sang phòng ban khác.
- **Request Body:**
```json
{
  "target_department_id": "dept_finance_01",
  "transfer_reason": "Yêu cầu này thuộc thẩm quyền giải quyết học phí của Phòng Tài chính."
}
```

### 4.3. `POST /api/v1/staff/tickets/{ticket_id}/resolve`
- **Mô tả:** Nhập kết quả giải quyết và chuyển trạng thái Ticket sang `RESOLVED`.
- **Request Body:**
```json
{
  "resolution_note": "Đã chấp nhận đơn hoãn thi môn CSDL. Sinh viên xem lịch thi bổ sung trên Portal.",
  "attachments": []
}
```

---

## 5. Phân Hệ Quản Lý (`/api/v1/manager`)

### 5.1. `GET /api/v1/manager/dashboard/summary`
- **Mô tả:** Lấy danh mục chỉ số KPI Dashboard (Sử dụng Cache Redis).
- **Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "total_tickets": 1250,
    "new_tickets": 45,
    "in_progress_tickets": 120,
    "resolved_tickets": 1050,
    "overdue_tickets": 12,
    "csat_avg_score": 4.85
  }
}
```

### 5.2. `POST /api/v1/manager/users`
- **Mô tả:** Tạo mới tài khoản nhân viên/quản lý và phân quyền.
- **Request Body:**
```json
{
  "user_code": "STF20260010",
  "full_name": "Trần Thị B",
  "email": "b.tran@aurora.edu.vn",
  "role": "STAFF",
  "department_id": "dept_edu_01"
}
```

---

## 6. File & Storage (`/api/v1/common`)

### 6.1. `GET /api/v1/attachments/{file_id}`
- **Mô tả:** Stream file đính kèm trực tiếp (Kiểm tra quyền sở hữu qua `DataScopeMiddleware`).
- **Headers:** `Authorization: Bearer <token>`
- **Response (200 OK):** Binary Data Stream (`Content-Type: application/pdf` hoặc `image/png`).

---

## 7. Mã Lỗi Hệ Thống Chuẩn (Global Error Response Spec)
Mọi trường hợp lỗi hệ thống hoặc Validation đều trả về Cấu trúc JSON thống nhất:
```json
{
  "success": false,
  "error": {
    "code": "INVALID_INPUT",
    "message": "Dữ liệu đầu vào không hợp lệ.",
    "details": [
      {
        "field": "description",
        "issue": "Mô tả vấn đề phải có độ dài tối thiểu 20 ký tự."
      }
    ]
  },
  "timestamp": "2026-10-09T13:15:00.123Z",
  "trace_id": "tr_9988776655443322"
}
```

| HTTP Code | Enum `error.code` | Nguyên Nhân & Kịch Bản |
| :--- | :--- | :--- |
| **400** | `INVALID_INPUT` | Lỗi Validation dữ liệu Form / Query Params. |
| **400** | `FILE_EXCEEDS_LIMIT` | File upload vượt quá $5\text{MB}$ hoặc sai extension. |
| **401** | `UNAUTHORIZED` | Token hết hạn, sai chữ ký hoặc bị đưa vào Blacklist. |
| **403** | `FORBIDDEN_ACCESS` | Vi phạm ma trận phân quyền RBAC hoặc Data Scope. |
| **404** | `RESOURCE_NOT_FOUND` | Không tìm thấy Ticket ID hoặc File ID yêu cầu. |
| **409** | `DUPLICATE_REQUEST` | Vi phạm Idempotency Key (`X-Client-Request-ID` bị trùng). |
| **429** | `TOO_MANY_REQUESTS` | Vi phạm ngưỡng Rate Limit ($> 60\text{ requests/phút}$). |
| **500** | `INTERNAL_SERVER_ERROR` | Lỗi ngoại lệ Server / Database connection failure. |