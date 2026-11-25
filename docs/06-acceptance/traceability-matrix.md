# Ma Trận Truy Xuất Yêu Cầu (RTM)

## 1. Mục Đích Và Cách Đọc

Ma trận **tổng hợp** chuỗi Báo giá → PRD → Master Plan → Parent task → Kịch bản test theo **từng AC**. Đây không phải nơi gốc để sửa: AC sửa ở `prd.md` của module, kịch bản sửa ở [test-scenarios.md](test-scenarios.md), task và milestone sửa trên GitHub, hạng mục giá sửa ở [quotation.xlsx](../08-project/quotation.xlsx). Khi một nơi gốc thay đổi, người phụ trách nghiệm thu (Team Charter mục 3.2) cập nhật lại bảng này trong cùng PR.

- **Parent task:** các issue GitHub hiện hữu triển khai phần tính năng tại mốc ghi trong dòng; test/AC bao quát nhiều mốc chỉ hoàn tất sau mốc cuối. Không thêm task (vẫn 58); thay đổi DoD/mốc trên remote chỉ là yêu cầu đồng bộ, chưa thực hiện trong lần sửa local này.
- **Báo giá:** `Q-01` M01, `Q-02` M02, `Q-03` M03 và năng lực dùng chung (đăng nhập FR-STU-00, FR-STF-00 dùng xác thực chung nên tính ở `Q-03`). Tích hợp, kiểm thử hệ thống, regression và sửa lỗi của mọi AC thuộc `Q-06`, `Q-07`, `Q-08`.
- Tổng: 187 AC, 23 NFR; mỗi mã có ít nhất một kịch bản test.


## 2. M01 - Sinh Viên

| AC | Kịch bản test | Parent task | Milestone | Báo giá |
| --- | --- | --- | --- | --- |
| `FR-STU-00/AC-01` | TS-AUTH-01 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-00/AC-02` | TS-AUTH-02 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-00/AC-03` | TS-AUTH-02 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-00/AC-04` | TS-AUTH-02 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-00/AC-05` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-00/AC-06` | TS-AUTH-03 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-00/AC-07` | TS-AUTH-01 | #120, #121 | MS-01 | `Q-03` |
| `FR-STU-01/AC-01` | TS-STU-01 | #131 | MS-02 | `Q-01` |
| `FR-STU-01/AC-02` | TS-STU-01 | #131 | MS-02 | `Q-01` |
| `FR-STU-01/AC-03` | TS-STU-01 | #131 | MS-02 | `Q-01` |
| `FR-STU-01/AC-04` | TS-STU-08 | #131 | MS-02 | `Q-01` |
| `FR-STU-01/AC-05` | TS-STU-01 | #131 | MS-02 | `Q-01` |
| `FR-STU-02/AC-01` | TS-STU-02 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-02` | TS-STU-02 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-03` | TS-STU-02 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-04` | TS-STU-09 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-05` | TS-STU-09 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-06` | TS-STU-09 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-07` | TS-STU-09 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-08` | TS-STU-02 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-02/AC-09` | TS-STU-02 | #132, #133 | MS-02 | `Q-01` |
| `FR-STU-03/AC-01` | TS-STU-03 | #138 | MS-02 | `Q-01` |
| `FR-STU-03/AC-02` | TS-STU-03 (MS-02), TS-STU-15 (MS-03), TS-STU-16 (MS-04) | #138 (MS-02); #143, #144, #145, #146, #147 (MS-03); #149, #150, #151, #152, #153, #154 (MS-04) | MS-02 → MS-04 | `Q-01` |
| `FR-STU-03/AC-03` | TS-STU-10 | #138 | MS-02 | `Q-01` |
| `FR-STU-03/AC-04` | TS-STU-03 (MS-02), TS-STU-15 (MS-03), TS-STU-16 (MS-04) | #138 (MS-02); #143, #144, #145, #146, #147 (MS-03); #149, #150, #151, #152, #153, #154 (MS-04) | MS-02 → MS-04 | `Q-01` |
| `FR-STU-03/AC-05` | TS-STU-03 | #138 | MS-02 | `Q-01` |
| `FR-STU-03/AC-06` | TS-STU-15 | #138 (nền tảng); #146, #147 (sự kiện) | MS-03 | `Q-01` |
| `FR-STU-03/AC-07` | TS-STU-03 (MS-02), TS-STU-15 (MS-03), TS-STU-16 (MS-04) | #138 (MS-02); #143, #144, #145, #146, #147 (MS-03); #149, #150, #151, #152, #153, #154 (MS-04) | MS-02 → MS-04 | `Q-01` |
| `FR-STU-04/AC-01` | TS-STU-04 (MS-02), TS-STU-15 (MS-03), TS-STU-16 (MS-04) | #139 (MS-02); #143, #144, #145, #146, #147 (MS-03); #149, #150, #151, #152, #153, #154 (MS-04) | MS-02 → MS-04 | `Q-01` |
| `FR-STU-04/AC-02` | TS-STU-04 (MS-02), TS-STU-15 (MS-03), TS-STU-16 (MS-04) | #139 (MS-02); #143, #144, #145, #146, #147 (MS-03); #149, #150, #151, #152, #153, #154 (MS-04) | MS-02 → MS-04 | `Q-01` |
| `FR-STU-04/AC-03` | TS-STU-04 (MS-02), TS-STU-15 (MS-03), TS-STU-16 (MS-04) | #139 (MS-02); #143, #144, #145, #146, #147 (MS-03); #149, #150, #151, #152, #153, #154 (MS-04) | MS-02 → MS-04 | `Q-01` |
| `FR-STU-04/AC-04` | TS-STU-10 | #139 | MS-02 | `Q-01` |
| `FR-STU-04/AC-05` | TS-STU-11 | #139 | MS-02 | `Q-01` |
| `FR-STU-04/AC-06` | TS-STU-04 | #139 | MS-02 | `Q-01` |
| `FR-STU-05/AC-01` | TS-STU-05 | #145 | MS-03 | `Q-01` |
| `FR-STU-05/AC-02` | TS-STU-05 | #145 | MS-03 | `Q-01` |
| `FR-STU-05/AC-03` | TS-STU-12 | #145 | MS-03 | `Q-01` |
| `FR-STU-05/AC-04` | TS-STU-05 | #145 | MS-03 | `Q-01` |
| `FR-STU-05/AC-05` | TS-STU-12 | #145 | MS-03 | `Q-01` |
| `FR-STU-05/AC-06` | TS-STU-12 | #145 | MS-03 | `Q-01` |
| `FR-STU-06/AC-01` | TS-STU-06 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-02` | TS-STU-06 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-03` | TS-STU-06 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-04` | TS-STU-13 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-05` | TS-STU-06 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-06` | TS-STU-13 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-07` | TS-STU-13 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-08` | TS-STU-06 | #150, #151, #152, #154 | MS-04 | `Q-01` |
| `FR-STU-06/AC-09` | TS-STU-16 | #152, #153 | MS-04 | `Q-01` |
| `FR-STU-07/AC-01` | TS-STU-07 | #155 | MS-04 | `Q-01` |
| `FR-STU-07/AC-02` | TS-STU-07 | #155 | MS-04 | `Q-01` |
| `FR-STU-07/AC-03` | TS-STU-14 | #155 | MS-04 | `Q-01` |
| `FR-STU-07/AC-04` | TS-STU-14 | #155 | MS-04 | `Q-01` |
| `FR-STU-07/AC-05` | TS-STU-07 | #155 | MS-04 | `Q-01` |
| `FR-STU-07/AC-06` | TS-STU-14 | #155 | MS-04 | `Q-01` |

## 3. M02 - Nhân Viên

| AC | Kịch bản test | Parent task | Milestone | Báo giá |
| --- | --- | --- | --- | --- |
| `FR-STF-00/AC-01` | TS-AUTH-01 | #120, #121 | MS-01 | `Q-03` |
| `FR-STF-00/AC-02` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-STF-00/AC-03` | TS-AUTH-02 | #120, #121 | MS-01 | `Q-03` |
| `FR-STF-00/AC-04` | TS-AUTH-03 | #120, #121 | MS-01 | `Q-03` |
| `FR-STF-00/AC-05` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-STF-00/AC-06` | TS-AUTH-01 | #120, #121 | MS-01 | `Q-03` |
| `FR-STF-01/AC-01` | TS-STF-01 | #134, #135 | MS-02 | `Q-02` |
| `FR-STF-01/AC-02` | TS-STF-01 | #134, #135 | MS-02 | `Q-02` |
| `FR-STF-01/AC-03` | TS-STF-09 | #134, #135 | MS-02 | `Q-02` |
| `FR-STF-01/AC-04` | TS-STF-01 (MS-02), TS-STF-08 (MS-04) | #134, #135 (hàng chờ); #152, #153 (mở lại) | MS-02; MS-04 | `Q-02` |
| `FR-STF-01/AC-05` | TS-STF-01 | #134, #135 | MS-02 | `Q-02` |
| `FR-STF-01/AC-06` | TS-STF-01 | #134, #135 | MS-02 | `Q-02` |
| `FR-STF-02/AC-01` | TS-STF-02 | #136, #137 | MS-02 | `Q-02` |
| `FR-STF-02/AC-02` | TS-STF-10 | #136, #137 | MS-02 | `Q-02` |
| `FR-STF-02/AC-03` | TS-STF-02 | #136, #137 | MS-02 | `Q-02` |
| `FR-STF-02/AC-04` | TS-STF-02 | #136, #137 | MS-02 | `Q-02` |
| `FR-STF-02/AC-05` | TS-STF-05 | #136, #137 (nền tảng); #146 (Transfer) | MS-03 | `Q-02` |
| `FR-STF-02/AC-06` | TS-STF-10 (Transfer) | #136, #137 (kiểm tiếp nhận); #146 (Transfer) | MS-03 | `Q-02` |
| `FR-STF-02/AC-07` | TS-STF-02 | #136, #137 | MS-02 | `Q-02` |
| `FR-STF-02/AC-08` | TS-STF-02 | #136, #137 | MS-02 | `Q-02` |
| `FR-STF-03/AC-01` | TS-STF-03 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-02` | TS-STF-03 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-03` | TS-STF-03 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-04` | TS-STF-03 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-05` | TS-STF-03 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-06` | TS-STF-11 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-07` | TS-STF-11 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-08` | TS-STF-11 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-09` | TS-STF-15 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-10` | TS-STF-15 | #141, #142 | MS-03 | `Q-02` |
| `FR-STF-03/AC-11` | TS-STF-16 | #141, #142 (quy tắc); #149, #151, #154 (trạng thái nguồn) | MS-04 | `Q-02` |
| `FR-STF-04/AC-01` | TS-STF-04 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-02` | TS-STF-04 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-03` | TS-STF-04 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-04` | TS-STF-04 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-05` | TS-STF-12 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-06` | TS-STF-12 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-07` | TS-STF-12 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-08` | TS-STF-04 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-04/AC-09` | TS-STU-05 | #143, #144 | MS-03 | `Q-02` |
| `FR-STF-05/AC-01` | TS-STF-05 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-02` | TS-STF-05 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-03` | TS-STF-05 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-04` | TS-STF-06 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-05` | TS-STF-06 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-06` | TS-STF-05 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-07` | TS-STF-13 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-08` | TS-STF-13 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-09` | TS-STF-13 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-10` | TS-STF-13 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-05/AC-11` | TS-STF-05 | #146, #147 | MS-03 | `Q-02` |
| `FR-STF-06/AC-01` | TS-STF-07 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-02` | TS-STF-07 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-03` | TS-STF-14 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-04` | TS-STF-07 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-05` | TS-STF-08 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-06` | TS-STF-08 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-07` | TS-STF-08 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-08` | TS-STF-14 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-09` | TS-STF-14 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-10` | TS-STU-07 | #149, #153 | MS-04 | `Q-02` |
| `FR-STF-06/AC-11` | TS-STU-06 | #149, #153 | MS-04 | `Q-02` |

## 4. M03 - Quản Lý

| AC | Kịch bản test | Parent task | Milestone | Báo giá |
| --- | --- | --- | --- | --- |
| `FR-MGT-00/AC-01` | TS-AUTH-01 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-00/AC-02` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-00/AC-03` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-00/AC-04` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-00/AC-05` | TS-AUTH-02 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-00/AC-06` | TS-AUTH-03 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-00/AC-07` | TS-AUTH-04 | #120, #121 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-01` | TS-MGT-01 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-02` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-03` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-04` | TS-MGT-01 | #122, #123 (khóa); #132, #133, #136, #137 (Ticket/assignee MS-02); #143 (WAITING_STUDENT MS-03) | MS-02; MS-03 | `Q-03` |
| `FR-MGT-01/AC-05` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-06` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-07` | TS-MGT-01 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-08` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-09` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-10` | TS-MGT-01 | #122, #123 (quyền/khóa); #132, #133, #136, #137, #143 (Ticket/assignee) | MS-01 (quyền); MS-02/03 (Ticket) | `Q-03` |
| `FR-MGT-01/AC-11` | TS-MGT-07 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-12` | TS-MGT-01 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-13` | TS-MGT-11 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-14` | TS-MGT-11 | #122, #123, #126 (MS-01); #136, #137 (MS-02); #141, #142, #143, #146, #147 (MS-03); #149 (MS-04); #156, #157, #158, #162 (MS-05) | MS-01; MS-02/03/04/05 theo thao tác dùng cờ | `Q-03` |
| `FR-MGT-01/AC-15` | TS-MGT-11 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-16` | TS-MGT-11 | #122, #123, #126 (MS-01); #136, #137 (MS-02); #141, #142, #143, #146, #147 (MS-03); #149 (MS-04); #156, #157, #158, #162 (MS-05) | MS-01; MS-02/03/04/05 theo thao tác dùng cờ | `Q-03` |
| `FR-MGT-01/AC-17` | TS-MGT-11 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-01/AC-18` | TS-MGT-11 | #122, #123 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-01` | TS-MGT-02 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-02` | TS-STU-02 | #124, #125 (cấu hình); #132, #133 (tạo Ticket) | MS-02 | `Q-03` |
| `FR-MGT-02/AC-03` | TS-MGT-02 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-04` | TS-MGT-08 | #124, #125 (cấu hình); #132, #136, #143, #149, #152, #154 (trạng thái nguồn) | MS-02/03; đầy đủ MS-04 | `Q-03` |
| `FR-MGT-02/AC-05` | TS-STF-05 | #124, #125 (cấu hình); #146 (Transfer) | MS-03 | `Q-03` |
| `FR-MGT-02/AC-06` | TS-MGT-02 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-07` | TS-MGT-08 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-08` | TS-MGT-08 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-09` | TS-MGT-08 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-10` | TS-MGT-08 | #124, #125 | MS-01 | `Q-03` |
| `FR-MGT-02/AC-11` | TS-STU-02 | #124, #125 (cấu hình); #132, #133 (tạo Ticket) | MS-02 | `Q-03` |
| `FR-MGT-03/AC-01` | TS-AUTH-05 (nền tảng MS-01), TS-MGT-03 (UI MS-05) | #126, #127 (MS-01); #156 (MS-05) | MS-01; MS-05 | `Q-03` |
| `FR-MGT-03/AC-02` | TS-MGT-03 | #156 | MS-05 | `Q-03` |
| `FR-MGT-03/AC-03` | TS-AUTH-05 (nền tảng MS-01), TS-MGT-03 (UI MS-05) | #126, #127 (MS-01); #156 (MS-05) | MS-01; MS-05 | `Q-03` |
| `FR-MGT-03/AC-04` | TS-MGT-03 | #156 | MS-05 | `Q-03` |
| `FR-MGT-03/AC-05` | TS-MGT-03 | #156 | MS-05 | `Q-03` |
| `FR-MGT-03/AC-06` | TS-MGT-09 | #156 | MS-05 | `Q-03` |
| `FR-MGT-03/AC-07` | TS-MGT-03 | #156 | MS-05 | `Q-03` |
| `FR-MGT-03/AC-08` | TS-MGT-03 | #156 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-01` | TS-MGT-04 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-02` | TS-MGT-04 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-03` | TS-MGT-04 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-04` | TS-MGT-04 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-05` | TS-MGT-04 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-06` | TS-MGT-09 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-04/AC-07` | TS-MGT-04 | #157, #158 | MS-05 | `Q-03` |
| `FR-MGT-05/AC-01` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-02` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-03` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-04` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-05` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-06` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-07` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-05/AC-08` | TS-MGT-05 | #159, #160, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-01` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-02` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-03` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-04` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-05` | TS-MGT-10 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-06` | TS-MGT-09 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-07` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-08` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-09` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-10` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |
| `FR-MGT-06/AC-11` | TS-MGT-06 | #161, #162, #164 | MS-05, MS-06 | `Q-03` |

## 5. Yêu Cầu Phi Chức Năng

| NFR | Kịch bản test | Parent task | Milestone | Báo giá |
| --- | --- | --- | --- | --- |
| `NFR-DEP-01` | TS-NFR-06 | #118, #119 (môi trường); #169, #170 (bàn giao) | MS-01 chuẩn bị; MS-06 nghiệm thu môi trường bàn giao | `Q-05` |
| `NFR-DEP-02` | TS-NFR-06 | #118, #119 (môi trường); #169, #170 (bàn giao) | MS-01 chuẩn bị; MS-06 nghiệm thu đủ danh mục | `Q-05` |
| `NFR-DEP-03` | TS-NFR-06 | #118, #119 (môi trường); #169, #170 (bàn giao) | MS-01 chuẩn bị; MS-06 kiểm luồng đầy đủ sau triển khai | `Q-05` |
| `NFR-OBS-01` | TS-NFR-05 | #129 (nền tảng), #167 (kiểm toàn hệ thống) | MS-01 nền tảng; MS-06 đối chiếu log toàn hệ thống | `Q-03, Q-07` |
| `NFR-OBS-02` | TS-AUTH-05, TS-MGT-03, TS-NFR-05 | #127, #129 (ghi nhận), #156 (UI), #167 (kiểm toàn hệ thống) | MS-01 và mốc sự kiện nguồn; MS-05 UI; MS-06 toàn hệ thống | `Q-03, Q-07` |
| `NFR-OBS-03` | TS-AUTH-05, TS-MGT-03, TS-NFR-05 | #127, #129 (ghi nhận), #156 (UI), #167 (kiểm toàn hệ thống) | MS-01 nền tảng; MS-05 UI; MS-06 toàn hệ thống | `Q-03, Q-07` |
| `NFR-PERF-01` | TS-NFR-01 | #171 | MS-06 | `Q-07` |
| `NFR-PERF-02` | TS-NFR-01 | #171 | MS-06 | `Q-07` |
| `NFR-PERF-03` | TS-NFR-01 | #171 | MS-06 | `Q-07` |
| `NFR-PERF-04` | TS-NFR-01 | #171 | MS-06 | `Q-07` |
| `NFR-REL-01` | TS-STF-10, TS-NFR-02 | #148 (nền tảng MS-03, hoàn thiện MS-04); #167 (hệ thống) | MS-02 kiểm phân công theo TS-STF-10; MS-03 kiểm chức năng đã có; MS-04 resolve/reopen; MS-06 toàn hệ thống | `Q-02, Q-07` |
| `NFR-REL-02` | TS-STF-05, TS-NFR-02 | #148 (nền tảng MS-03, hoàn thiện MS-04); #167 (hệ thống) | MS-02 kiểm phân công theo TS-STF-10; MS-03 kiểm chức năng đã có; MS-04 resolve/reopen; MS-06 toàn hệ thống | `Q-02, Q-07` |
| `NFR-REL-03` | TS-NFR-02 | #148 (nền tảng MS-03, hoàn thiện MS-04); #167 (hệ thống) | MS-02 kiểm phân công theo TS-STF-10; MS-03 kiểm chức năng đã có; MS-04 resolve/reopen; MS-06 toàn hệ thống | `Q-02, Q-07` |
| `NFR-REL-04` | TS-NFR-02 | #148 (nền tảng MS-03, hoàn thiện MS-04); #167 (hệ thống) | MS-02 kiểm phân công theo TS-STF-10; MS-03 kiểm chức năng đã có; MS-04 resolve/reopen; MS-06 toàn hệ thống | `Q-02, Q-07` |
| `NFR-SEC-01` | TS-AUTH-02, TS-NFR-03 | #126, #128, #166 | MS-01, MS-06 | `Q-03, Q-07` |
| `NFR-SEC-02` | TS-AUTH-04, TS-NFR-03 | #126, #128, #166 | MS-01, MS-06 | `Q-03, Q-07` |
| `NFR-SEC-03` | TS-STU-10, TS-NFR-03 | #126, #128, #166 | MS-01 policy/harness; MS-02 file Ticket; MS-03 bổ sung; MS-04 file kết quả; MS-06 toàn hệ thống | `Q-03, Q-07` |
| `NFR-SEC-04` | TS-MGT-01, TS-NFR-03 | #126, #128, #166 | MS-01, MS-06 | `Q-03, Q-07` |
| `NFR-SEC-05` | TS-NFR-03 | #126, #128, #166 | MS-01, MS-06 | `Q-03, Q-07` |
| `NFR-USA-01` | TS-NFR-04 | #130, #140 | MS-01/02 nền tảng UI; kiểm từng luồng MS-03…MS-05; TS-NFR-04 toàn hệ thống MS-06 | `Q-01…Q-03` |
| `NFR-USA-02` | TS-NFR-04 | #130, #140 | MS-01/02 nền tảng UI; kiểm từng luồng MS-03…MS-05; TS-NFR-04 toàn hệ thống MS-06 | `Q-01…Q-03` |
| `NFR-USA-03` | TS-STU-09, TS-NFR-04 | #130, #140 | MS-01/02 nền tảng UI; kiểm từng luồng MS-03…MS-05; TS-NFR-04 toàn hệ thống MS-06 | `Q-01…Q-03` |
| `NFR-USA-04` | TS-NFR-04 | #130, #140 | MS-01/02 nền tảng UI; kiểm từng luồng MS-03…MS-05; TS-NFR-04 toàn hệ thống MS-06 | `Q-01…Q-03` |

## Phụ Lục: Effort Theo Gói Công Việc

Bảng tổng hợp effort theo gói công việc (WP), dùng để đối chiếu với `Q-01`…`Q-11`. Giờ theo vai trò ở `08-project/plans/ngan-sach-noi-bo.xlsx` sheet `Resource`.

### A.1 M01 - Student

| Gói công việc | Effort | FR / Flow | Workflow |
| :--- | ---: | :--- | :--- |
| WP-STU-01 - Tra cứu hướng dẫn & FAQ | 14h | FR-STU-01 | - |
| WP-STU-02 - Tạo & gửi yêu cầu hỗ trợ | 37h | FR-STU-02 | WF-01 |
| WP-STU-03 - Xem & theo dõi yêu cầu | 33h | FR-STU-03 | WF-01, WF-03, WF-06 |
| WP-STU-04 - Nhận thông báo trạng thái | 19h | FR-STU-04 | WF-01, WF-03, WF-04, WF-05, WF-06 |
| WP-STU-05 - Bổ sung thông tin & phản hồi | 25h | FR-STU-05, FR-STU-06, FR-STU-07 | WF-03, WF-06 |

**Tổng M01: 128h.**

### A.2 M02 - Staff

| Gói công việc | Effort | FR / Flow | Workflow |
| :--- | ---: | :--- | :--- |
| WP-STF-01 - Tiếp nhận, tìm kiếm & lọc | 33h | FR-STF-01 | WF-02, WF-06 |
| WP-STF-02 - Phân loại & phân công | 38h | FR-STF-02 | WF-02 |
| WP-STF-03 - Quản lý ưu tiên & thời hạn | 29h | FR-STF-03 | WF-02 |
| WP-STF-04 - Xử lý & cập nhật yêu cầu | 39h | FR-STF-04 | WF-03 |
| WP-STF-05 - Chuyển xử lý, Escalation & hoàn tất | 32h | FR-STF-05 + luồng ghi nhận kết quả của FR-STF-06 | WF-04, WF-05, WF-07 |
| WP-STF-06 - Đóng & mở lại yêu cầu | 26h | FR-STF-01 + Luồng B của FR-STF-06 | WF-06 |

**Tổng M02: 197h.**

> WP-STF-06 bao gồm phần tiếp nhận và xử lý lại Ticket sau khi được mở lại. Quyền chuyển trạng thái vẫn tuân theo Ticket Lifecycle.

### A.3 M03 - Management

| Gói công việc | Effort | FR / Flow | Workflow |
| :--- | ---: | :--- | :--- |
| WP-MGT-01 - Tài khoản, vai trò & RBAC | 64h | FR-MGT-00, FR-MGT-01 + xác thực dùng chung | - |
| WP-MGT-02 - Phòng ban & danh mục | 26h | FR-MGT-02 | WF-01, WF-02, WF-04 |
| WP-MGT-03 - Kiểm soát quyền truy cập & Audit Trail | 40h | FR-MGT-03 + kiểm soát quyền xuyên M01-M03 | Tất cả workflow liên quan |
| WP-MGT-04 - Quản lý thời hạn lưu trữ | 15h | FR-MGT-04 | - |
| WP-MGT-05 - Dashboard & thống kê quản trị | 33h | FR-MGT-05 | - |
| WP-MGT-06 - Báo cáo, mức độ hài lòng & xuất dữ liệu | 37h | FR-MGT-06 | WF-06 |

**Tổng M03: 215h.**

> Ngân sách nội bộ dùng mã `M03 – Management Dashboard`, thống nhất với Product/PRD.

### A.4 Năng Lực Dùng Chung Và Hoạt Động Cấp Dự Án

- FR-STU-00 và FR-STF-00 mô tả hành vi truy cập của từng phân hệ nhưng cơ chế xác thực dùng chung được truy xuất về WP-MGT-01, không cộng effort riêng.
- Thông báo cho Staff/Management được truy xuất theo gói công việc nghiệp vụ phát sinh sự kiện tương ứng.
- Hoạt động cấp dự án gồm **305h** (chi tiết theo vai trò ở [ngan-sach-noi-bo.xlsx](../08-project/plans/ngan-sach-noi-bo.xlsx) sheet `Resource`):

| Hoạt động | Effort | Hạng mục báo giá | Mốc | Kiểm chứng |
| :--- | ---: | :--- | :--- |
| Quản lý dự án & điều phối; demo và thu feedback cuối mốc | 84h | `Q-04` | Khởi động, MS-01…MS-06 | Báo cáo mốc |
| Môi trường, CI/CD; triển khai production, bàn giao mã nguồn | 46h | `Q-05` | MS-01, MS-06 | NFR-DEP |
| Tích hợp toàn hệ thống | 36h | `Q-06` | MS-06 | WF-01…WF-07 |
| Kiểm thử hệ thống, regression mỗi mốc, hỗ trợ UAT | 65h | `Q-07` | MS-01…MS-06 | Toàn bộ TS, NFR |
| Sửa lỗi giữa các mốc (16h) và sau kiểm thử hệ thống/UAT (16h) | 32h | `Q-08` | MS-02…MS-06 | Regression |
| Hướng dẫn sử dụng | 16h | `Q-09` | MS-06 | Tài liệu bàn giao |
| Bảo hành 30 ngày | 26h | `Q-10` | Sau MS-06 | — |

- Dự phòng rủi ro dự án: **40h** (`Q-11`).
- Tổng effort kế hoạch: **885h** (= 540h chức năng + 305h cấp dự án + 40h dự phòng), khớp [quotation.xlsx](../08-project/quotation.xlsx).

### A.5 Đối chiếu WP với WBS và parent task

Nơi gốc mã gói và giờ kế hoạch là [wbs.xlsx](../08-project/plans/wbs.xlsx), sheet `WBS`. WP ở phụ lục này là cách nhóm theo chức năng trong ngân sách, **không phải mã WBS**. Sheet `Đối chiếu effort` phân bổ 540h chức năng giữa hai cách nhóm; tổng theo từng WBS và từng hàng `Resource` đều khớp.

- `1.3.3` (52h) = WP-STU-03 (33h) + WP-STU-04 (19h).
- WP-STU-05 (25h) = `1.3.4` (12h) + `1.3.5` (13h).
- `1.4.2` (67h) = WP-STF-02 (38h) + WP-STF-03 (29h).
- WP-STF-05 (32h) = `1.4.3` (20h chuyển xử lý/escalation) + 12h ghi kết quả thuộc `1.4.5`.
- `1.4.5` (38h) = 12h của WP-STF-05 + WP-STF-06 (26h). WP-STF-06 không cộng lại effort hàng chờ FR-STF-01 đã nằm ở `1.4.1`.
- WP-MGT-01 (64h) = `1.6.1` (24h) + `1.5.3` (40h).
- `1.5.4` (41h) = WP-MGT-02 (26h) + WP-MGT-04 (15h).
- WP-MGT-03 (40h) = `1.6.2` (24h) + `1.6.3` (16h).

Từ #153 (`REOPEN-02`), mở sheet `Đối chiếu mã`: WBS `1.4.5`, hàng WBS 30, Gantt tổng hợp hàng 25, `Chi tiết công việc` hàng 30, WP-STF-06, ngân sách `Resource` hàng 17. Giờ 38h là **giờ gói WBS dùng chung**; 26h là phần WP-STF-06 bao gồm cả phân tích, thiết kế, QA. Không coi 38h hay 26h là ước lượng riêng của #153 và không cộng cột giờ gói theo từng issue. Giờ thực tế cần ghi kèm mã WBS để so tổng gói; muốn kiểm soát riêng từng task thì phải duyệt phân bổ task-level trước, không suy đoán từ tổng gói.

Các gói thiết kế WBS `1.2.1`…`1.2.3` ghi 0h vì giờ các vai trò đã nằm trong gói chức năng. Bảng đối chiếu vẫn dẫn tới các gói có giờ và hàng `Resource`; không cộng thêm 78h khởi động. Các mã `FAQ-01`, `REOPEN-02`… trong issue được gọi đúng là **Mã công việc**, kèm trường WBS thực và liên kết bảng đối chiếu.
