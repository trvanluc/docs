"""Make the client Proposal + quotation self-contained, preserving source styles."""
import re
from copy import deepcopy, copy
from pathlib import Path

from docx import Document
from docx.text.paragraph import Paragraph
from openpyxl import load_workbook
from openpyxl.styles import Alignment

ROOT = Path("docs/08-project")
source = (ROOT / "assumptions.md").read_text(encoding="utf8")
quote = load_workbook(ROOT / "quotation.xlsx")
sheet = quote["Giả định"]
codes = [sheet.cell(r, 1).value for r in range(4, 14)]
texts = {}
for code in codes:
    line = re.search(rf"^- `{code}` (.+)$", source, re.M).group(1)
    texts[code] = line.replace("**", "").replace("`", "")
effects = {
    "A-01": "Vượt 3.000 sinh viên: đánh giá lại tải, kiến trúc và effort chức năng/kiểm thử.",
    "A-02": "Cần ứng dụng di động độc lập: bổ sung phạm vi phát triển, chưa nằm trong giá.",
    "A-03": "Thêm ngôn ngữ hoặc bản địa hóa nâng cao: đánh giá lại giao diện và hướng dẫn.",
    "A-05": "Có tích hợp bên thứ ba: bổ sung thiết kế, tích hợp và kiểm thử giao tiếp.",
    "A-07": "Cần chứng nhận hoặc kiểm thử bảo mật chuyên sâu: bổ sung effort/dịch vụ kiểm thử.",
    "A-08": "Đơn vị thực hiện phải cấp hạ tầng/tên miền: tính lại chi phí và lịch triển khai.",
    "A-10": "Cần sao lưu, giám sát hoặc hỗ trợ hạ tầng lâu dài: báo giá phạm vi vận hành riêng.",
    "A-11": "Chờ phê duyệt vượt kế hoạch: điều chỉnh lịch; đánh giá công điều phối phát sinh.",
    "A-13": "UAT bằng dữ liệu thật: đánh giá công chuẩn bị/làm sạch dữ liệu, bảo vệ dữ liệu "
             "và chấp thuận sử dụng; Q-07 phải được ước lượng, báo giá lại trước khi làm.",
    "A-16": "Phản hồi sau quá 02 ngày làm việc: đánh giá lại công điều phối/UAT và lịch liên quan.",
}
sheet["A1"] = (
    "Các giả định ảnh hưởng giá: nội dung, mã và hạng mục đầy đủ để khách đọc cùng Proposal. "
    "assumptions.md là nơi gốc nội bộ; hai tài liệu gửi khách lưu bản sao đồng bộ cùng phiên bản. "
    "Nếu giả định sai, hai bên đánh giá tác động và xác nhận CR/báo giá trước khi thực hiện; "
    "không tự động tăng giá và không lấy dự phòng Q-11 cho phạm vi mới."
)
sheet["C3"] = "Nội dung giả định"
sheet["D3"] = "Ảnh hưởng nếu không đúng"
for c in [sheet["C3"], sheet["D3"]]:
    c._style = copy(sheet["B3"]._style)
for row in range(4, 14):
    code = sheet.cell(row, 1).value
    for col, value in [(3, texts[code]), (4, effects[code])]:
        c = sheet.cell(row, col, value)
        c._style = copy(sheet.cell(row, 2)._style)
        c.alignment = Alignment(wrap_text=True, vertical="top")
    sheet.row_dimensions[row].height = 120
sheet.column_dimensions["A"].width = 14
sheet.column_dimensions["B"].width = 32
sheet.column_dimensions["C"].width = 64
sheet.column_dimensions["D"].width = 72
sheet.row_dimensions[1].height = 140
sheet["A1"].alignment = Alignment(wrap_text=True, vertical="top")
sheet.column_dimensions["A"].width = 18
# A1 is a long note; merge only the empty cells in this existing title row.
sheet.merge_cells("A1:D1")
sheet.print_area = "A1:D13"
sheet.print_title_rows = "1:3"
sheet.sheet_properties.pageSetUpPr.fitToPage = True
sheet.page_setup.orientation = "landscape"
sheet.page_setup.fitToWidth = 1
sheet.page_setup.fitToHeight = 0
if not any(row[0].value == "v1.0.1-V3-02" for row in quote["Phiên bản"]):
    quote["Phiên bản"].append([
        "v1.0.1-V3-02", "24/11/2026", "#194",
        "Đồng bộ 10 mã/nội dung/ảnh hưởng giả định với Proposal; bổ sung A-13. Không đổi giờ/giá.",
        300000000, 300000000, "Chờ PM review PR"
    ])

doc = Document(ROOT / "Proposal.docx")
start = next(i for i,p in enumerate(doc.paragraphs) if p.text == "Assumptions (Giả định)")
stop = next(i for i,p in enumerate(doc.paragraphs) if "Các hạng mục ngoài phạm vi" in p.text)
template = deepcopy(doc.paragraphs[start + 1]._p)
anchor = doc.paragraphs[stop]
for paragraph in list(doc.paragraphs)[start+1:stop]:
    paragraph._p.getparent().remove(paragraph._p)
assumptions = []
for row in range(4, 14):
    code = sheet.cell(row,1).value
    qs = sheet.cell(row,2).value
    text = f"{code} — {texts[code]} Hạng mục: {qs}. {effects[code]}"
    new = deepcopy(template)
    anchor._p.addprevious(new)
    p = Paragraph(new, anchor._parent)
    if p.runs:
        p.runs[0].text = text
        for run in p.runs[1:]:
            run.text = ""
    else:
        p.add_run(text)
    assumptions.append(text)
doc.paragraphs[1].runs[0].text = (
    "Phiên bản v1.0.1-V3-02 (chưa gửi Nhà trường), cập nhật ngày 24/11/2026"
)
for note in [
    "Giả định ảnh hưởng giá: mã, nội dung và hạng mục tại phần Assumptions của Proposal "
    "khớp sheet Giả định của quotation.xlsx. Nếu một giả định sai, hai bên xác nhận "
    "tác động và báo giá CR trước khi thực hiện; không tự động tăng giá.",
    "Lịch sử phiên bản: dùng chung sheet Phiên bản trong quotation.xlsx; "
    "v1.0.1-V3-02 ngày 24/11/2026 đồng bộ 10 giả định ảnh hưởng giá, bổ sung A-13; "
    "chờ PM review PR, chưa xác nhận phê duyệt."
]:
    p = next((p for p in doc.paragraphs if p.text == note), None)
    if p is None:
        p = doc.add_paragraph(note)
    p.style = doc.paragraphs[start+1].style
# Avoid orphaning the price total after the added assumption text changes pagination.
for cell in doc.tables[1].rows[-2].cells:
    for p in cell.paragraphs:
        p.paragraph_format.keep_with_next = True
doc.save(ROOT / "Proposal.docx")
quote.save(ROOT / "quotation.xlsx")
text = "\n".join(p.text for p in Document(ROOT / "Proposal.docx").paragraphs)
check = load_workbook(ROOT / "quotation.xlsx")["Giả định"]
for row in range(4,14):
    code = check.cell(row,1).value
    assert code in text and texts[code] in text and check.cell(row,2).value in text
assert "dữ liệu giả lập" in text and "Q-07 phải được" in text
print("PASS: all 10 assumptions have identical code/content/Q references in client artifacts.")
