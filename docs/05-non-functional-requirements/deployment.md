# NFR-DEP - Triển Khai Và Bàn Giao

## 1. Phạm Vi

UniSupport được triển khai dưới dạng Web Application trên hạ tầng do Aurora University cung cấp. Phạm vi triển khai bao gồm chuẩn bị môi trường, cấu hình ứng dụng, triển khai, kiểm tra sau triển khai và bàn giao; không bao gồm vận hành hạ tầng lâu dài.

## 2. Trách Nhiệm Hạ Tầng

Aurora University cung cấp:
- môi trường máy chủ phù hợp;
- tên miền hoặc địa chỉ truy cập;
- điều kiện mạng và quyền truy cập cần thiết để triển khai.

Đội dự án chịu trách nhiệm:
- chuẩn bị phiên bản triển khai;
- cấu hình ứng dụng phù hợp môi trường được cung cấp;
- triển khai và kiểm tra các chức năng chính;
- bàn giao mã nguồn và hướng dẫn cài đặt/vận hành.

## 3. Giới Hạn Phạm Vi

- Hệ điều hành, cấu hình CPU/RAM và công nghệ đóng gói được xác định theo môi trường triển khai thực tế.
- Không bao gồm thiết lập sao lưu tự động, giám sát vận hành máy chủ lâu dài hoặc hỗ trợ hạ tầng ngoài phạm vi bảo hành.
- Không tích hợp hệ thống bên thứ ba ngoài phạm vi sản phẩm.
- Bảo hành kỹ thuật (`08-project/constraints.md` mục 1) chỉ áp dụng cho lỗi kỹ thuật phát sinh từ phía đội dự án; yêu cầu tính năng mới hoặc thay đổi ngoài phạm vi không thuộc bảo hành.

## 4. Danh Mục Bàn Giao

| Nhóm | Hạng mục bàn giao |
| :--- | :--- |
| Hệ thống | Hệ thống UniSupport sử dụng được trên trình duyệt máy tính và thiết bị di động, đã triển khai trên môi trường bàn giao |
| Mã nguồn | Mã nguồn frontend và backend; tài liệu hướng dẫn cài đặt và vận hành |
| Cơ sở dữ liệu | Cấu trúc cơ sở dữ liệu và ERD; dữ liệu mẫu phục vụ kiểm thử |
| Tài liệu | Tài liệu phạm vi và yêu cầu đã xác nhận; hướng dẫn sử dụng cho từng vai trò; test case và kết quả kiểm thử |

## 5. Nghiệm Thu

- Hệ thống được triển khai và truy cập được trên môi trường Aurora University cung cấp.
- Các luồng chính của ba phân hệ hoạt động sau triển khai.
- Các hạng mục tại mục 4 được bàn giao đầy đủ.
