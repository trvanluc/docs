"""Add append-only version registers; never invent historical approvals."""
from datetime import datetime
from pathlib import Path
from copy import deepcopy

from docx import Document
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

root = Path("docs/08-project")
for name in ["wbs.xlsx", "ngan-sach-noi-bo.xlsx"]:
    path = root / "plans" / name
    book = load_workbook(path)
    if "Change log" not in book:
        s = book.create_sheet("Change log")
        s.append(["Lịch sử phiên bản — giữ nguyên tên file, chỉ thêm dòng"])
        s.merge_cells("A1:F1")
        s.append(["Ghi nhận hiện trạng không phải phê duyệt hồi tố. Khi được duyệt, "
                  "thêm dòng xác nhận kèm link bằng chứng; không sửa/xóa dòng cũ. "
                  "Người phụ trách: Trần Tiến Minh; PM xác nhận kế hoạch nội bộ, "
                  "Aurora University xác nhận CR ảnh hưởng cam kết."])
        s.merge_cells("A2:F2")
        s.append(["Phiên bản", "Ngày ghi nhận", "Issue / CR", "Thay đổi", "Người duyệt / trạng thái",
                  "Bằng chứng / phiên bản liên quan"])
        s.append(["v1.0-baseline", datetime(2026,11,24), "—",
                  "Ghi nhận hiện trạng master dfbc84f trước V3-03; chưa đổi số liệu.",
                  "Chưa có bằng chứng phê duyệt hồi tố", "Git master dfbc84f"])
        s.append(["v1.0.1-V3-03", datetime(2026,11,24),
                  "https://github.com/trvanluc/docs/issues/196",
                  "Thêm lịch sử phiên bản theo Team Charter. Giữ 885h, 300 triệu và mọi công thức.",
                  "Chờ PM review PR", "Không thay đổi WBS/Resource/chi phí"])
        for row in s:
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
                if c.row == 3:
                    c.font = Font(bold=True, color="FFFFFF")
                    c.fill = PatternFill("solid", fgColor="4472C4")
        for col, width in zip("ABCDEF", [25,20,42,65,42,42]):
            s.column_dimensions[col].width = width
        for row, height in [(1,32),(2,65),(3,36),(4,70),(5,90)]:
            s.row_dimensions[row].height = height
        for row in [4,5]:
            s.cell(row,2).number_format = "dd/mm/yyyy"
        s["C5"].hyperlink = s["C5"].value
        s.freeze_panes = "A4"
        s.auto_filter.ref = "A3:F5"
        s.print_title_rows = "1:3"
        s.page_setup.orientation = "landscape"
        s.sheet_properties.pageSetUpPr.fitToPage = True
        s.page_setup.fitToWidth = 1
        s.page_setup.fitToHeight = 1
        s.print_area = "A1:F5"
    book.save(path)
    assert load_workbook(path)["Change log"]["E5"].value == "Chờ PM review PR"

# Proposal's shared register is explicit INSIDE the Word file.
path = root / "Proposal.docx"
doc = Document(path)
doc.paragraphs[1].runs[0].text = (
    "Phiên bản v1.0.1-V3-03 (chưa gửi Nhà trường), cập nhật ngày 24/11/2026"
)
note = ("Lịch sử phiên bản Proposal dùng chung sheet Phiên bản của quotation.xlsx "
        "(bảng báo giá gửi kèm); mỗi dòng phải ghi tên tài liệu, phiên bản, ngày, "
        "thay đổi và người duyệt hoặc trạng thái chờ duyệt.")
if not any(note in p.text for p in doc.paragraphs):
    p = doc.paragraphs[1]
    run = p.add_run("\n" + note)
    if p.runs[0]._r.rPr is not None:
        run._r.insert(0, deepcopy(p.runs[0]._r.rPr))
for cell in doc.tables[1].rows[-2].cells:
    for p in cell.paragraphs:
        p.paragraph_format.keep_with_next = True
doc.save(path)
quote_path = root / "quotation.xlsx"
book = load_workbook(quote_path)
if not any(row[0].value == "v1.0.1-V3-03" for row in book["Phiên bản"]):
    book["Phiên bản"].append([
        "v1.0.1-V3-03", "24/11/2026", "https://github.com/trvanluc/docs/issues/196",
        "Proposal.docx: khai báo dùng chung lịch sử tại đây; "
        "wbs.xlsx và ngan-sach-noi-bo.xlsx có Change log riêng. Không đổi nội dung thương mại.",
        300000000, 300000000, "Chờ PM review PR"])
book.save(quote_path)

expected = {
    "quotation.xlsx": "Phiên bản",
    "plans/master-schedule.xlsx": "Change log",
    "plans/wbs.xlsx": "Change log",
    "plans/ngan-sach-noi-bo.xlsx": "Change log",
}
for name, log in expected.items():
    assert log in load_workbook(root / name).sheetnames
assert note in "\n".join(p.text for p in Document(path).paragraphs)
print("PASS: 4 Excel registers + explicit shared Proposal register; approvals remain pending.")
