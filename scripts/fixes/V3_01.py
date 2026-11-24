"""V3-01: trace task -> canonical WBS package -> Gantt -> budget/WP.

Run from repo root. Add --update-issues to correct GitHub's misleading WBS ID
field. This is a crosswalk, NOT a new per-task effort estimate.
"""
import json
import re
import subprocess
import sys
from copy import copy
from pathlib import Path

from openpyxl import load_workbook
from ooxml_cache import save_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

BASE = Path("docs/08-project/plans")
REPO = "trvanluc/docs"

def gh(*args):
    return subprocess.check_output(["rtk", "proxy", "gh", *args], encoding="utf8").strip()

def table(book, name, headers, rows, widths):
    if name in book:
        del book[name]
    s = book.create_sheet(name)
    s.append(headers)
    for row in rows:
        s.append(row)
    s.freeze_panes = "A2"
    s.auto_filter.ref = s.dimensions
    for row in s:
        s.row_dimensions[row[0].row].height = 32 if name == "Đối chiếu effort" else 140
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            if c.row == 1:
                c.font = Font(bold=True, color="FFFFFF")
                c.fill = PatternFill("solid", fgColor="4472C4")
    for i, width in enumerate(widths, 1):
        s.column_dimensions[get_column_letter(i)].width = width
    s.sheet_properties.pageSetUpPr.fitToPage = True
    s.page_setup.orientation = "landscape"
    s.page_setup.fitToWidth = 1
    s.page_setup.fitToHeight = 0
    s.print_title_rows = "1:1"
    return s

# The 540 functional hours are reconciled ONCE here, including many-to-many
# boundaries: 1.4.3=20 vs WP-STF-05=32, and 1.4.5=38 vs WP-STF-06=26.
BRIDGE = [
    ("1.3.1", "WP-STU-01", 3, 14), ("1.3.2", "WP-STU-02", 4, 37),
    ("1.3.3", "WP-STU-03", 5, 33), ("1.3.3", "WP-STU-04", 6, 19),
    ("1.3.4", "WP-STU-05", 7, 12), ("1.3.5", "WP-STU-05", 7, 13),
    ("1.4.1", "WP-STF-01", 12, 33), ("1.4.2", "WP-STF-02", 13, 38),
    ("1.4.2", "WP-STF-03", 14, 29), ("1.4.4", "WP-STF-04", 15, 39),
    ("1.4.3", "WP-STF-05", 16, 20), ("1.4.5", "WP-STF-05", 16, 12),
    ("1.4.5", "WP-STF-06", 17, 26),
    ("1.6.1", "WP-MGT-01", 22, 24), ("1.5.3", "WP-MGT-01", 22, 40),
    ("1.5.4", "WP-MGT-02", 23, 26), ("1.6.2", "WP-MGT-03", 24, 24),
    ("1.6.3", "WP-MGT-03", 24, 16), ("1.5.4", "WP-MGT-04", 25, 15),
    ("1.5.1", "WP-MGT-05", 26, 33), ("1.5.2", "WP-MGT-06", 27, 37),
]

# WBS codes; Gantt row(s); detail row; budget Resource rows.
MAP = {}
def group(codes, wbs, gantt, detail, resource):
    for code in codes.split():
        MAP[code] = (wbs, gantt, detail, resource)

group("PLN-01", ["1.1.1", "1.2.1"], [8], 5, [35, 36])
group("UX-01", ["1.2.2"], [9], 6, list(range(3, 8)) + list(range(12, 18)) + list(range(22, 28)))
group("ARCH-01 ARCH-02", ["1.2.3"], [10], 7, [4, 5, 12, 13, 14, 15, 16, 17, 22, 23, 24, 25, 26, 27])
group("ENV-01 ENV-02", ["1.8.1"], [11], 8, [37])
group("AUTH-01 AUTH-02", ["1.6.1"], [12], 9, [22])
group("ACC-01 ACC-02", ["1.5.3"], [13], 10, [22])
group("CFG-01 CFG-02", ["1.5.4"], [14], 11, [23])
group("SEC-01", ["1.6.2"], [15], 12, [24])
group("AUD-01", ["1.6.3"], [15], 12, [24])
group("SEC-02", ["1.6.2"], [11, 12, 13, 14, 15], 13, [24])
group("OBS-01", ["1.6.3", "1.8.1"], [11, 12, 13, 14, 15], 14, [24, 37])
group("UI-01", ["1.2.2", "1.3.1", "1.3.2", "1.5.3", "1.5.4", "1.6.1"], [12, 13, 14], 15, [3, 4, 22, 23])
group("FAQ-01", ["1.3.1"], [16], 16, [3])
group("TKT-01 TKT-02", ["1.3.2"], [17], 17, [4])
group("QUEUE-01 QUEUE-02", ["1.4.1"], [18], 18, [12])
group("ASSIGN-01 ASSIGN-02", ["1.4.2"], [18], 19, [13])
group("TRACK-01", ["1.3.3"], [19], 20, [5])
group("NOTI-01", ["1.3.3"], [19, 27], 20, [6])
group("UI-02", ["1.2.2", "1.3.1", "1.3.2", "1.3.3", "1.4.1", "1.4.2"], [16, 17, 18, 19], 21, [3, 4, 5, 6, 12, 13])
group("SLA-01 SLA-02", ["1.4.2"], [20], 22, [14])
group("SUP-01 SUP-02", ["1.4.4"], [21], 23, [15])
group("SUP-03", ["1.3.4"], [22], 24, [7])
group("TRANSFER-01", ["1.4.3"], [23], 25, [16])
group("ESC-01", ["1.4.3"], [23], 26, [16])
group("REL-01", ["1.3.2", "1.3.4", "1.4.2", "1.4.3", "1.4.4", "1.4.5"], [20, 21, 22, 23], 27, [4, 7, 13, 14, 15, 16, 17])
group("RES-01", ["1.4.5"], [24], 28, [16])
group("RES-02 RES-03 REOPEN-01", ["1.3.5"], [24, 25], 29, [7])
group("REOPEN-02", ["1.4.5"], [25], 30, [17])
group("CLOSE-01", ["1.3.5"], [25], 31, [7])
group("CSAT-01", ["1.3.5"], [26], 32, [7])
group("AUD-02", ["1.6.3"], [28], 33, [24])
group("RET-01 RET-02", ["1.5.4"], [29], 34, [25])
group("DASH-01 DASH-02", ["1.5.1"], [30], 35, [26])
group("RPT-01 RPT-02", ["1.5.2"], [31], 36, [27])
group("INT-01 INT-02", ["1.7.1"], [32], 37, [39])
group("TEST-01 TEST-02", ["1.7.2"], [33], 38, [40, 41])
group("FIX-01 REG-01", ["1.7.2"], [34], 39, [41, 43])
group("DEP-01", ["1.8.1"], [35], 40, [38])
group("DOC-01", ["1.1.5", "1.8.2", "1.8.3", "1.8.4"], [35], 40, [35, 38, 44])
group("PERF-01", ["1.7.2"], [33], 41, [40])

def main():
    wbs = load_workbook(BASE / "wbs.xlsx")
    schedule = load_workbook(BASE / "master-schedule.xlsx")
    budget = load_workbook(BASE / "ngan-sach-noi-bo.xlsx")
    # If V2-02 was merged first, it split RES-02 into its own detail row.
    if "Gantt MS-04" in schedule and schedule["Chi tiết công việc"]["B44"].value == "Xem kết quả":
        ids, rows, _, resource = MAP["RES-02"]
        MAP["RES-02"] = (ids, [24], 44, resource)
    wbs_rows = {wbs["WBS"].cell(r, 2).value: r for r in range(8, 51)}
    issues = json.loads(gh("issue", "list", "--repo", REPO, "--state", "all",
                           "--limit", "500", "--json", "number,title,body,url"))
    by_code = {m.group(1): i for i in issues
               if (m := re.match(r"\[([A-Z]+-\d+)\]", i["title"]))}
    assert set(MAP) <= set(by_code), set(MAP) - set(by_code)
    records = []
    for code, (ids, gantt, detail, resource) in MAP.items():
        issue = by_code[code]
        body_source = issue["body"].replace("\r","")
        owners_match = re.search(r"\*\*(?:Parent Assignee / Phụ trách|Owner):\*\* ([^\n]+)",body_source)
        if owners_match:
            owners = owners_match.group(1).split(" (")[0]
            expected = {x.strip() for x in owners.split(",")}
            actual = {x.strip() for x in schedule["Chi tiết công việc"].cell(detail,4).value.split(",")}
            assert expected <= actual, (code,detail,expected,actual)
        milestone = re.search(r"\*\*Milestone:\*\* (MS-\d+)",body_source)
        if milestone:
            assert schedule["Chi tiết công việc"].cell(detail,1).value == milestone.group(1), (code,detail)
        package_hours = "; ".join(f"{x}: {wbs['WBS'].cell(wbs_rows[x],10).value}h"
                                   for x in ids)
        wp = sorted({p for x, p, r, h in BRIDGE if x in ids and r in resource})
        note = ("Gói thiết kế 0h: giờ BA/UI/TL đã nằm trong gói chức năng, không cộng thêm."
                if code in ["UX-01", "ARCH-01", "ARCH-02"] else
                "Giờ của GÓI WBS dùng chung, không phải ước lượng riêng của task; không cộng cột này.")
        if code == "REOPEN-02":
            note += " 38h WBS 1.4.5 = 12h phần ghi kết quả + 26h WP-STF-06; 26h cũng gồm BA/UI/TL/QA, không chỉ giờ dev #153."
        if code in ["RES-02", "REOPEN-02"]:
            note += " Phân công chi tiết trên Gantt theo PR V2-02; các hàng này là nhóm tổng hợp."
        if code in ["UI-01", "UI-02", "SEC-02", "OBS-01", "REL-01"]:
            note += " Task xuyên mốc: hàng Gantt là phần việc tích hợp, không phải thanh độc lập."
        records.append([code, issue["number"], issue["url"], ", ".join(ids),
                        ", ".join(str(wbs_rows[x]) for x in ids),
                        ", ".join(map(str, gantt)), detail,
                        ", ".join(wp) or "Hoạt động/thiết kế cấp dự án",
                        ", ".join(map(str, resource)), package_hours, note])
        if "--update-issues" in sys.argv:
            body = issue["body"].replace("\r", "")
            body = re.sub(r"\*\*WBS ID:\*\*", "**Mã công việc:**", body)
            marker = "\n\n## Đối chiếu mã công việc (V3-01)"
            body = body.split(marker)[0]
            body += (marker + f"\n\n- **WBS thực:** {', '.join(ids)} (sheet WBS, hàng "
                     f"{', '.join(str(wbs_rows[x]) for x in ids)}).\n"
                     f"- **Giờ gói kế hoạch:** {package_hours}. {note}\n"
                     f"- **Gantt:** Master Schedule hàng {', '.join(map(str,gantt))}; "
                     f"Chi tiết công việc hàng {detail}.\n"
                     f"- **WP / Resource:** {', '.join(wp)}; ngân sách Resource hàng "
                     f"{', '.join(map(str,resource))}.\n"
                     f"- [Bảng đối chiếu đầy đủ](https://github.com/{REPO}/blob/fix/V3-01/"
                     "docs/08-project/plans/wbs.xlsx) — sheet Đối chiếu mã và Đối chiếu effort. "
                     "Nhánh PR này giữ được link cả trước/sau merge; nơi gốc sau merge là master.\n")
            if body != issue["body"].replace("\r", ""):
                gh("issue", "edit", str(issue["number"]), "--repo", REPO, "--body", body)
                print("Updated", code, issue["number"], flush=True)
    crosswalk = table(wbs, "Đối chiếu mã",
        ["Mã task", "Issue", "Link issue", "WBS thực", "Hàng WBS", "Hàng Gantt",
         "Hàng Chi tiết", "WP", "Hàng Resource", "Giờ gói WBS (không cộng)", "Quy tắc"],
        records, [18, 10, 35, 28, 18, 18, 18, 30, 24, 38, 65])
    for row in range(2, crosswalk.max_row + 1):
        crosswalk.cell(row, 3).hyperlink = crosswalk.cell(row, 3).value
    bridge_rows = [[x, wbs_rows[x], p, r, h] for x, p, r, h in BRIDGE]
    bridge = table(wbs, "Đối chiếu effort",
        ["WBS thực", "Hàng WBS", "WP", "Hàng Resource", "Giờ phân bổ (cộng đúng một lần)"],
        bridge_rows, [20, 18, 24, 20, 38])
    bridge.append(["TỔNG CHỨC NĂNG", None, None, None, "=SUM(E2:E22)"])
    assert sum(h for x, p, r, h in BRIDGE) == 540
    for code in {x for x,p,r,h in BRIDGE}:
        assert sum(h for x,p,r,h in BRIDGE if x == code) == wbs["WBS"].cell(wbs_rows[code],10).value
    resource = budget["Resource"]
    for r in {r for x,p,r,h in BRIDGE}:
        total = sum(resource.cell(r,c).value or 0 for c in range(2,10)) + (resource.cell(r,11).value or 0)
        assert sum(h for x,p,rr,h in BRIDGE if rr == r) == total, r
        resource.cell(r,15, next(p for x,p,rr,h in BRIDGE if rr == r))
        resource.cell(r,16, ", ".join(x for x,p,rr,h in BRIDGE if rr == r))
    for r in [2,11,21]:
        resource.cell(r,15,"Mã WP")._style = copy(resource.cell(r,1)._style)
        resource.cell(r,16,"WBS thực")._style = copy(resource.cell(r,1)._style)
    for row in resource:
        for c in row:
            if isinstance(c.value,str) and c.data_type != "f":
                c.value = c.value.replace("M1 – Student","M01 – Student Portal").replace(
                    "M2 – Staff","M02 – Staff Operations").replace("M3 – Admin","M03 – Management Dashboard").replace(
                    "M1–M3","M01–M03")
    resource.column_dimensions["O"].width = 25
    resource.column_dimensions["P"].width = 28
    listing = schedule["Danh sách issue"]
    for col, header in [(12,"WBS thực"),(13,"Giờ gói WBS (không cộng)"),(14,"Bảng đối chiếu gốc")]:
        listing.cell(4,col,header)._style = copy(listing.cell(4,3)._style)
        listing.column_dimensions[get_column_letter(col)].width = 32
    for row in range(6,64):
        code = listing.cell(row,3).value
        if code not in MAP:
            continue
        ids, gantt, detail, res = MAP[code]
        listing.cell(row,12,", ".join(ids))
        listing.cell(row,13,"; ".join(f"{x}: {wbs['WBS'].cell(wbs_rows[x],10).value}h" for x in ids))
        cell = listing.cell(row,14,"wbs.xlsx / Đối chiếu mã")
        cell.hyperlink = "wbs.xlsx"
    # Stable row IDs are retained; append task-code columns instead of inserting columns.
    gs, ds = schedule["Master Schedule"], schedule["Chi tiết công việc"]
    gs.cell(3,107,"Mã task (hàng tổng hợp)")
    gs.column_dimensions[get_column_letter(107)].width = 42
    ds.cell(4,7,"Mã task")
    ds.column_dimensions["G"].width = 42
    for r in range(8,36):
        gs.cell(r,107,", ".join(c for c,(_,rows,_,_) in MAP.items() if r in rows))
    for r in range(5,45):
        ds.cell(r,7,", ".join(c for c,(_,_,rr,_) in MAP.items() if r == rr))
    if not any(row[0].value == "v1.0.1-V3-01" for row in schedule["Change log"]):
        schedule["Change log"].append([
            "v1.0.1-V3-01", "24/11/2026", "#192",
            "Bảng đối chiếu task/WBS/Gantt/WP/Resource; làm rõ giờ gói dùng chung "
            "và ranh giới gói; chuẩn hóa nhãn module. Không đổi effort/giá.",
            "Toàn dự án", 885, 300000000, "Chờ PM review PR"])
    for name, book in [("wbs.xlsx",wbs),("master-schedule.xlsx",schedule),("ngan-sach-noi-bo.xlsx",budget)]:
        save_workbook(book, BASE/name)
    quote_path = BASE.parent / "quotation.xlsx"
    quote = load_workbook(quote_path)
    for s in quote:
        for row in s:
            for c in row:
                if isinstance(c.value, str) and c.data_type != "f":
                    for old, new in [("M1","M01"),("M2","M02"),("M3","M03")]:
                        c.value = re.sub(rf"\b{old}\b",new,c.value)
    if not any(row[0].value == "v1.0.1-V3-01" for row in quote["Phiên bản"]):
        quote["Phiên bản"].append([
            "v1.0.1-V3-01", "24/11/2026", "#192", "Chuẩn hóa nhãn module M01/M02/M03 theo ngân sách; không đổi giờ/giá.",
            300000000, 300000000, "Chờ PM review PR"])
    save_workbook(quote, quote_path)
    print(f"PASS: {len(records)} task crosswalks; 540 functional hours reconcile by WBS AND Resource.")

if __name__ == "__main__":
    main()
