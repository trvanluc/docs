# [PRJ-02] Ràng buộc Dự án (Project Constraints)

Tài liệu này xác định các giới hạn và ràng buộc cố định về thời gian, ngân sách, phân bổ nguồn lực và hạ tầng kỹ thuật đối với dự án **UniSupport** tại **Aurora University**.

---

## 1. Ràng buộc về Thời gian & Tiến độ (Time Constraints)

* **Tổng thời gian phát triển:** **14 tuần** (tương đương khoảng **70 ngày làm việc**), tính từ ngày khởi động chính thức đến khi hoàn tất triển khai bàn giao.
* **Quy trình nghiệm thu:** Sau khi bàn giao, Aurora University có **10 ngày làm việc** (Tuần 15–16) để tiến hành kiểm thử UAT và nghiệm thu chính thức (không tính gộp vào 14 tuần phát triển).
* **Thời gian bảo hành:** **30 ngày** hỗ trợ kỹ thuật miễn phí kể từ ngày ký biên bản nghiệm thu.
* **Điều chỉnh tiến độ:** Thời gian chờ phản hồi, xác nhận hoặc cung cấp thông tin/hạ tầng từ phía Client vượt quá thỏa thuận (quá 03 ngày làm việc) sẽ được cộng tương ứng vào tiến độ chung của dự án.

---

## 2. Ràng buộc về Chi phí & Ngân sách (Budget & Cost Breakdown)

### 2.1 Tổng ngân sách hợp đồng
* **Tổng kinh phí cố định:** **300.000.000 VNĐ** (Ba trăm triệu đồng chẵn).

### 2.2 Cơ cấu Chi phí Nhân sự Nội bộ (Internal Resource Cost Baseline)

| STT | Vị trí Nhân sự | Đơn giá / Giờ (VNĐ) | Thời gian làm việc (h) | Lương Gross phân bổ (VNĐ) | Bảo hiểm 21,5% (VNĐ) | Chi phí Nhân sự Nội bộ (VNĐ) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Project Manager (PM) | 409.091 | 70 | 28.636.364 | 6.156.818 | 34.793.182 |
| 2 | Business Analyst (BA) | 236.364 | 63 | 14.890.909 | 3.201.545 | 18.092.455 |
| 3 | UI/UX Designer | 218.182 | 27 | 5.890.909 | 1.266.545 | 7.157.455 |
| 4 | Technical Lead (TL) | 454.545 | 31 | 14.090.909 | 3.029.545 | 17.120.455 |
| 5 | Frontend Developer 1 | 254.545 | 56 | 14.254.545 | 3.064.727 | 17.319.273 |
| 6 | Frontend Developer 2 | 181.818 | 61 | 11.090.909 | 2.384.545 | 13.475.455 |
| 7 | Backend Developer 1 | 254.545 | 107 | 27.236.364 | 5.855.818 | 33.092.182 |
| 8 | Backend Developer 2 | 181.818 | 75 | 13.636.364 | 2.931.818 | 16.568.182 |
| 9 | QA/QC Engineer | 181.818 | 98 | 17.818.182 | 3.830.909 | 21.649.091 |
| 10 | DevOps / Deployment Engineer | 200.000 | 30 | 6.000.000 | 1.290.000 | 7.290.000 |
| | **TỔNG CƠ SỞ** | | **618h** | **153.545.455** | **33.012.273** | **186.557.727** |

### 2.3 Tổng hợp Chi phí Kế hoạch & Dự phòng
* **Tổng công sức cơ sở của Business Functions:** 518h
* **Hoạt động cấp dự án (PM & DevOps):** 100h
* **Tổng công sức cơ sở toàn dự án:** **618h**
* **Chi phí nhân sự nội bộ cơ sở:** **186.557.727 VNĐ**
* **Dự phòng rủi ro công sức (Risk Reserve / Buffer):** **22h**
* **Chi phí dự phòng rủi ro ước tính:** **6.641.214 VNĐ**
* **Tổng công sức kế hoạch:** **640h**
* **Tổng chi phí nhân sự kế hoạch (sử dụng toàn bộ dự phòng):** **193.198.941 VNĐ**
* **Phần ngân sách còn lại (Quản lý dự án, chi phí hạ tầng hỗ trợ & lợi nhuận định mức):** **106.801.059 VNĐ** (Tổng ngân sách: 300.000.000 VNĐ).

---

## 3. Ràng buộc về Nguồn lực & Phân bổ Công sức (Resource Allocation Breakdown)

* **M1 – Student (Phân hệ Sinh viên):** 124h cơ sở + 4h buffer = **128h kế hoạch** (5 chức năng).
* **M2 – Staff (Phân hệ Nhân viên):** 187h cơ sở + 10h buffer = **197h kế hoạch** (6 chức năng).
* **M3 – Admin (Phân hệ Quản trị & Báo cáo):** 207h cơ sở + 8h buffer = **215h kế hoạch** (6 chức năng).
* **Hoạt động cấp dự án (PM + DevOps):** 100h cơ sở + 0h buffer = **100h kế hoạch**.
* **Tổng toàn bộ chức năng & hoạt động:** **618h cơ sở + 22h buffer = 640h kế hoạch**.

---

## 4. Ràng buộc Kỹ thuật & Hạ tầng (Technical Constraints)

* **Hạ tầng triển khai:** Hệ thống hoàn toàn phụ thuộc vào Server, tên miền và môi trường mạng do Aurora University cung cấp.
* **Quy mô hệ thống:** Tối ưu cho khoảng **3.000 sinh viên**; không thiết kế chịu tải lớn (Load balancing / Auto-scaling) hoặc kiến trúc phân tán phức tạp.
* **Loại ứng dụng:** Chỉ triển khai dưới dạng **Web Application** (Responsive UI cho máy tính và thiết bị di động), không phát triển Mobile App độc lập (iOS/Android).
* **Tích hợp:** Không tích hợp hệ thống bên thứ ba (SSO, CRM, LMS...) ngoài phạm vi đã xác định trong PRD.
* **Bảo mật:** Không bao gồm các yêu cầu chứng nhận bảo mật quốc tế (ISO, PCI-DSS) hoặc đánh giá an ninh mạng chuyên sâu (Penetration Testing).

---

## 5. Ràng buộc về Giao tiếp & Quản lý Thay đổi (Change Management Constraints)

* **Đầu mối liên lạc:** Mỗi bên chỉ định 01 Quản lý dự án (PM) làm đầu mối chính để trao đổi và phê duyệt tài liệu/kết quả.
* **Yêu cầu thay đổi (Change Request):** Mọi yêu cầu phát sinh thêm tính năng hoặc thay đổi phạm vi ngoài thỏa thuận ban đầu sẽ được đánh giá tác động về tiến độ và chi phí bổ sung bằng văn bản riêng.