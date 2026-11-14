# ADR-001 - Mã Ticket Duy Nhất

## Bối Cảnh

Mỗi Ticket cần có một mã nhận diện duy nhất để phục vụ tra cứu và trao đổi trong suốt vòng đời xử lý.

## Quyết Định

- Mỗi Ticket phải có **một mã Ticket duy nhất**, hiển thị được cho Sinh viên/Staff/Management khi có quyền.
- Mã phải ổn định trong suốt vòng đời Ticket và không thay đổi khi Transfer, reopen hoặc đóng Ticket.
- Định dạng hiển thị và loại khóa chính trong database là quyết định triển khai kỹ thuật, không phải requirement nghiệp vụ.

## Hệ Quả

Giải pháp triển khai phải bảo đảm tính duy nhất của mã Ticket nhưng không phụ thuộc vào một định dạng hiển thị hoặc kiểu khóa chính cố định.
