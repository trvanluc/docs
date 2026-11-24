"""Number Proposal headings and relocate assumptions/out-of-scope under scope.

Keep main section numbers 1–6, existing runs/tables and commercial content.
"""
from pathlib import Path
from copy import deepcopy
import re

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

path = Path("docs/08-project/Proposal.docx")
doc = Document(path)
original_tables = [deepcopy(t._tbl) for t in doc.tables]
start = next(i for i,p in enumerate(doc.paragraphs) if p.text == "Assumptions (Giả định)")
stop = next(i for i,p in enumerate(doc.paragraphs) if p.text.startswith("2. Phạm"))
target = next(p for p in doc.paragraphs if p.text.startswith("3. THỜI"))
block = [p._p for p in doc.paragraphs[start:stop]]
for element in block:
    element.getparent().remove(element)
    target._p.addprevious(element)

renames = {
    "Giải pháp đề xuất": ("1.1 Giải pháp đề xuất", "Heading 2"),
    "Module 1: Sinh viên (Q-01)": ("2.1 Module 1 Sinh viên (Q-01)", "Heading 2"),
    "Module 2: Nhân viên (Q-02)": ("2.2 Module 2 Nhân viên (Q-02)", "Heading 2"),
    "Module 3: Quản lý và năng lực dùng chung (Q-03)": (
        "2.3 Module 3 Quản lý và năng lực dùng chung (Q-03)", "Heading 2"),
    "Bảo mật và phân quyền": ("2.3.1 Bảo mật và phân quyền", "Heading 3"),
    "Assumptions (Giả định)": ("2.4 Assumptions (Giả định)", "Heading 2"),
    "Các hạng mục ngoài phạm vi hiện tại (Out of Scope)": (
        "2.5 Các hạng mục ngoài phạm vi hiện tại (Out of Scope)", "Heading 2"),
}

def replace_preserving_runs(p, text):
    if p.runs:
        p.runs[0].text = text
        for run in p.runs[1:]:
            run.text = ""
    else:
        p.add_run(text)

headings = []
for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith("PROJECT PROPOSAL"):
        p.style = doc.styles["Title"]
        continue
    if text in renames:
        title, style = renames[text]
        replace_preserving_runs(p,title)
        p.style = doc.styles[style]
    elif re.match(r"^[1-6]\.\s",text):
        p.style = doc.styles["Heading 1"]
    elif re.match(r"^(3\.[12]|5\.[123])\s",text):
        p.style = doc.styles["Heading 2"]
    else:
        continue
    p.paragraph_format.keep_with_next = True
    numbering = p._p.pPr.find(qn("w:numPr"))
    if numbering is not None:
        p._p.pPr.remove(numbering)
    headings.append((p.text,p.style.name))

replace_preserving_runs(doc.paragraphs[1],
    "Phiên bản v1.0.1-V3-04 (chưa gửi Nhà trường), cập nhật ngày 24/11/2026")
note = doc.add_paragraph(
    "Lịch sử phiên bản: v1.0.1-V3-04, 24/11/2026 — chuẩn hóa heading, "
    "chuyển giả định sang mục 2.4 và ngoài phạm vi sang mục 2.5; "
    "không đổi phạm vi, ngày kế hoạch, effort hoặc giá. "
    "Người duyệt: chờ PM review PR; issue V3-04 #198."
)
note.style = doc.paragraphs[1].style
if doc.paragraphs[1].runs[0]._r.rPr is not None:
    note.runs[0]._r.insert(0,deepcopy(doc.paragraphs[1].runs[0]._r.rPr))

# Keep the final price row with its preceding item.
for cell in doc.tables[1].rows[-2].cells:
    for p in cell.paragraphs:
        p.paragraph_format.keep_with_next = True
doc.save(path)
check = Document(path)
top = [p.text for p in check.paragraphs if p.style.name == "Heading 1"]
assert len(top) == 6 and all(p.startswith(f"{i}.") for i,p in enumerate(top,1))
for title in ["2.4 Assumptions (Giả định)",
              "2.5 Các hạng mục ngoài phạm vi hiện tại (Out of Scope)"]:
    assert next(p for p in check.paragraphs if p.text == title).style.name == "Heading 2"
assert len(check.tables) == len(original_tables)
print("PASS: title + six numbered main headings; numbered 2.4/2.5 inside scope.")
print("\n".join(f"{style}: {text}" for text,style in headings))
