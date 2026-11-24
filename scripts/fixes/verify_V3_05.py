"""Regression check for success metric -> scenario references."""
import re
from pathlib import Path

base = Path("docs/06-acceptance")
metrics = (base / "success-metrics.md").read_text(encoding="utf8")
scenarios = (base / "test-scenarios.md").read_text(encoding="utf8")
known = set(re.findall(r"^\| (TS-[A-Z]+-\d+) \|", scenarios, re.M))
methods = metrics.split("## 3. Phương Pháp Đo",1)[1].split("## 4.",1)[0]
rows = [line for line in methods.splitlines() if re.match(r"\| SM-\d+ \|", line)]
assert len(rows) == 7
for line in rows:
    fields = [x.strip() for x in line.split("|")[1:-1]]
    code, tests = fields[0], set(re.findall(r"TS-[A-Z]+-\d+", fields[3]))
    assert tests and tests <= known, (code,tests-known)
    if code == "SM-07":
        assert {"TS-AUTH-04","TS-STU-10","TS-MGT-09","TS-NFR-03"} <= tests
    if code == "SM-03":
        assert {"TS-STU-09","TS-STF-10"} <= tests
    print("PASS", code, sorted(tests))
assert any("TS-NFR-03" in line and "SM-07" in line for line in scenarios.splitlines())
print("PASS: seven metrics resolve to existing scenarios; SM-07 reverse reference exists.")
