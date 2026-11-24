"""Align MS-04 with existing parent tasks without reallocating effort."""
from copy import copy
from datetime import datetime, timedelta
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

path = Path("docs/08-project/plans/master-schedule.xlsx")
book = load_workbook(path)
gantt = book["Master Schedule"]
# PERF-01 already assigns QA/QC + DevOps; show the existing support, no extra hours.
gantt["D33"] = "QA/QC, DevOps"
for row, description in [
    (24, "Ghi kết quả RES-01 (BE2, FE2); xem kết quả RES-02 (BE1, FE1)"),
    (25, "Phản hồi RES-03, REOPEN-01, CLOSE-01 (BE1, FE1); REOPEN-02 (BE2, FE2)"),
]:
    gantt.cell(row, 3, description + "; xem Gantt MS-04")
    gantt.cell(row, 4, "BE1, FE1, BE2, FE2")
    gantt.row_dimensions[row].height = 66

tasks = [
    ("RES-01", 149, "BE2, FE2", 20, 24, 11, 28),
    ("RES-02", 150, "BE1, FE1", 20, 24, 11, 44),
    ("RES-03", 151, "BE1, FE1", 25, 30, 11, 29),
    ("REOPEN-01", 152, "BE1, FE1", 25, 30, 11, 29),
    ("REOPEN-02", 153, "BE2, FE2", 25, 30, 11, 30),
    ("CLOSE-01", 154, "BE1", 25, 30, 11, 31),
    ("CSAT-01", 155, "BE1, FE1", 1, 2, 12, 32),
]
detail = book["Chi tiết công việc"]
detail["C29"] = "Sinh viên chấp nhận kết quả (RES-03) hoặc yêu cầu mở lại (REOPEN-01)."
for col, value in enumerate([
    "MS-04", "Xem kết quả", "Sinh viên xem nội dung và tài liệu kết quả (RES-02).",
    "BE1, FE1", "Kết quả đúng Ticket của sinh viên.",
    "Chỉ xem/tải được kết quả của Ticket thuộc tài khoản mình."
], 1):
    cell = detail.cell(44, col, value)
    cell._style = copy(detail.cell(29, col)._style)
detail.row_dimensions[44].height = 66
for col, value in enumerate(["Mã task MS-04", "Bắt đầu", "Kết thúc"], 7):
    detail.cell(4, col, value)._style = copy(detail["D4"]._style)
    detail.column_dimensions[get_column_letter(col)].width = 24

if "Gantt MS-04" in book:
    del book["Gantt MS-04"]
sheet = book.create_sheet("Gantt MS-04")
sheet.append(["MS-04 — phân công theo parent task; không phải effort bổ sung"])
sheet.append(["Ngày/owner khớp task GitHub; hàng 24–25 Gantt tổng hợp chỉ là nhóm việc. "
              "Không hiểu mọi người cùng làm mọi task. Thông báo/lịch sử ở hàng 27 giữ nguyên, "
              "việc thêm task của hàng đó thuộc V2-01."])
sheet.merge_cells("A1:G1")
sheet.merge_cells("A2:G2")
sheet.row_dimensions[2].height = 60
sheet.append(["Mã task", "Issue", "Phụ trách", "Bắt đầu", "Kết thúc",
              "Hàng Gantt tổng hợp", "Hàng Chi tiết công việc"])
for offset in range(19):
    cell = sheet.cell(3, 8 + offset, datetime(2026, 11, 20) + timedelta(days=offset))
    cell.number_format = "dd/mm"
    sheet.column_dimensions[cell.column_letter].width = 5
for index, (code, number, owners, start, end, month, detail_row) in enumerate(tasks, 4):
    start, end = datetime(2026, month, start), datetime(2026, month, end)
    group = 24 if number <= 150 else 26 if number == 155 else 25
    for col, value in enumerate([code, f"#{number}", owners, start, end, group, detail_row], 1):
        sheet.cell(index, col, value)
    sheet.cell(index, 2).hyperlink = f"https://github.com/trvanluc/docs/issues/{number}"
    for col in [4, 5]:
        sheet.cell(index, col).number_format = "dd/mm/yyyy"
    for col, value in [(7, code), (8, start), (9, end)]:
        cell = detail.cell(detail_row, col)
        if col == 7 and code not in str(cell.value or ""):
            cell.value = f"{cell.value}, {code}" if cell.value else code
        elif col != 7:
            cell.value = value
            cell.number_format = "dd/mm/yyyy"
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for col in range(8, 27):
        letter = get_column_letter(col)
        sheet.cell(index, col, f'=IF(AND({letter}$3>=$D{index},{letter}$3<=$E{index},'
                   f'WEEKDAY({letter}$3,2)<=5),1,"")').number_format = ";;;"

blue = PatternFill("solid", fgColor="4472C4")
sheet.conditional_formatting.add("H4:Z10", FormulaRule(formula=["H4=1"], fill=blue))
for row in sheet:
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        if cell.row == 3:
            cell.fill = blue
            cell.font = Font(bold=True, color="FFFFFF")
for col, width in zip("ABCDEFG", [18, 12, 24, 17, 17, 20, 22]):
    sheet.column_dimensions[col].width = width
sheet.freeze_panes = "H4"
sheet.auto_filter.ref = "A3:G10"
sheet.sheet_properties.pageSetUpPr.fitToPage = True
sheet.page_setup.orientation = "landscape"
sheet.page_setup.paperSize = sheet.PAPERSIZE_A3
sheet.page_setup.fitToWidth = 1
sheet.page_setup.fitToHeight = 1
sheet.print_area = "A1:Z10"
if not any(row[0].value == "Gantt MS-04" for row in book["Mục lục"]):
    book["Mục lục"].append(["Gantt MS-04", "Phân công/ngày theo từng parent task MS-04"])
if not any(row[0].value == "v1.0.1-V2-02" for row in book["Change log"]):
    book["Change log"].append([
    "v1.0.1-V2-02", "24/11/2026", "#190",
    "Làm rõ hai nhóm Gantt MS-04, bổ sung Gantt từng parent task và tách RES-02 "
    "khỏi phản hồi kết quả; giữ ngày/owner task, không đổi effort/giá.",
    "MS-04", 885, 300000000, "Chờ PM review PR"
    ])
book.save(path)
check = load_workbook(path)
assert len(list(check["Gantt MS-04"].iter_rows(min_row=4, max_row=10))) == 7
for row in check["Gantt MS-04"].iter_rows(min_row=4, max_row=10):
    assert row[3].value <= row[4].value
print("PASS: 7 tasks, owner/date bars and detail rows; no effort or role reassignment.")
