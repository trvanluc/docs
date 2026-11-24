"""V1-03: create real kickoff parent tasks BEFORE updating the workbook.

Run from the repository root: python -X utf8 scripts/fixes/V1_03.py
Requires openpyxl and an authenticated gh CLI. Existing task titles are reused.
"""
import json
import subprocess
from copy import copy
from pathlib import Path

from openpyxl import load_workbook
from ooxml_cache import save_workbook

REPO = "trvanluc/docs"
ROOT = Path(__file__).resolve().parents[2]


def gh(*args):
    return subprocess.check_output(
        ["rtk", "proxy", "gh", *args], encoding="utf8"
    ).strip()


def main():
    path = ROOT / "docs/08-project/plans/master-schedule.xlsx"
    book = load_workbook(path)
    sheet = book["Danh sách issue"]
    existing = json.loads(gh("issue", "list", "--repo", REPO, "--state", "all",
                             "--limit", "500", "--json", "title,url"))
    tasks = {}
    for row, gantt, wbs in [(6, 8, "1.1.1, 1.2.1"), (7, 9, "1.2.2"),
                             (8, 10, "1.2.3"), (9, 10, "1.2.3")]:
        code, title, owner, description, acceptance, refs = [
            sheet.cell(row, col).value for col in [3, 4, 5, 6, 7, 11]
        ]
        start = book["Master Schedule"].cell(gantt, 5).value
        end = book["Master Schedule"].cell(gantt, 6).value
        approval = (
            "Aurora University xác nhận phạm vi, vai trò và AC trước MS-01."
            if code == "PLN-01" else
            "Aurora University duyệt luồng màn hình và prototype ba vai trò."
            if code == "UX-01" else
            "TL review thiết kế; PM xác nhận đầu vào kỹ thuật sẵn sàng cho MS-01."
        )
        full_title = f"[{code}] {title}"
        body = (
            f"**FR:** {refs}\n**Priority:** Cao\n"
            f"**Milestone:** Khởi động (không gắn MS-xx)\n"
            f"**Owner:** {owner} (đội thực thi Mô phỏng)\n"
            f"**Hạn:** {end:%d/%m/%Y}\n"
            f"**Dự kiến:** {start:%d/%m/%Y}–{end:%d/%m/%Y}\n"
            f"**Mã công việc:** {code}\n**WBS:** {wbs}\n\n"
            f"## Mô tả\n\n{description}\n\n"
            f"Nơi gốc: [Master Schedule](https://github.com/{REPO}/blob/master/"
            "docs/08-project/plans/master-schedule.xlsx), "
            f"sheet Master Schedule hàng {gantt}; Danh sách issue hàng {row}.\n\n"
            f"## Điều kiện hoàn thành\n\n- [ ] {acceptance}\n"
            f"- [ ] {approval}\n"
            "- [ ] Lưu bằng chứng review/phê duyệt vào issue; cập nhật tài liệu liên quan.\n"
            "- [ ] Người có thẩm quyền xác minh theo Team Charter trước khi đóng.\n\n"
            "## Theo dõi\n\n"
            "Task kế hoạch để open, theo luồng To do → Doing → Review → QA verify → Done. "
            "Các ngày trên là lịch cơ sở; điều chỉnh lịch theo V1-02 phải cập nhật cả issue này. "
            "Không cộng thêm giờ: 78h khởi động đã có trong Resources "
            "(PM 11h, BA 28h, UI/UX 27h, TL 8h, BE1 4h); "
            "hai task ARCH cùng dùng hàng Gantt 10, không nhân đôi effort.\n\n"
            "Liên quan: #182 (V1-03)."
        )
        url = next((i["url"] for i in existing if i["title"] == full_title), None)
        if not url:
            url = gh("issue", "create", "--repo", REPO, "--title", full_title,
                     "--label", "task", "--body", body)
        tasks[code] = (row, url, approval)
        print(code, url)

    # All four issues must exist before the first Excel mutation/save.
    assert len(tasks) == 4
    for code, (row, url, approval) in tasks.items():
        sheet.cell(row, 9, "#" + url.rsplit("/", 1)[1])
        cell = sheet.cell(row, 10, url)
        cell.hyperlink = url
        if approval not in sheet.cell(row, 7).value:
            sheet.cell(row, 7, sheet.cell(row, 7).value + " " + approval)
        sheet.row_dimensions[row].height = max(sheet.row_dimensions[row].height or 0, 78)
    sheet["A65"] = (
        "Quy ước: QA-01 xuyên suốt, kiểm thử nằm trong DoD từng task. "
        "PLN-01, UX-01, ARCH-01, ARCH-02 có parent task nhãn task, nhận diện bằng "
        "mã công việc và giai đoạn Khởi động; không gắn MS-xx. "
        "Đếm cả bốn task khi báo cáo tiến độ toàn dự án, không cộng vào tỷ lệ của MS-01…MS-06. "
        "Các task còn lại gắn milestone tương ứng."
    )
    sheet.row_dimensions[65].height = 60
    log = book["Change log"]
    if not any(row[0].value == "v1.0.1-V1-03" for row in log):
        log.append(["v1.0.1-V1-03", "24/11/2026", "#182",
                    "Bổ sung bốn parent task khởi động; không đổi ngày, effort hoặc giá.",
                    "Khởi động", 885, 300000000, "Chờ PM review PR"])
    for cell in log[5]:
        cell._style = copy(log.cell(4, cell.column)._style)
    save_workbook(book, path)
    check = load_workbook(path)
    assert all(check["Danh sách issue"].cell(r, 10).value.startswith("https://github.com/")
               for r in range(6, 10))
    print("PASS: 4 parent issues; workbook links match; schedule/effort unchanged.")


if __name__ == "__main__":
    main()
