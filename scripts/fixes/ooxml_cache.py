"""Preserve cached values of unchanged formulas across openpyxl saves.

Only use when numeric inputs/formulas did not change. This is not a calculation
engine; new or changed formulas are recalculated by Excel on opening.
"""
from copy import deepcopy
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

from lxml import etree as ET

NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def retain_formula_cache(before, path):
    """Transfer caches by sheet name and formula identity, never by sheet order."""
    before = ZipFile(BytesIO(before))
    with ZipFile(path) as after:
        parts = {n: after.read(n) for n in after.namelist()}
    def sheet_parts(archive):
        relns = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}
        rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        ids = {r.get("Id"): "xl/" + r.get("Target").removeprefix("/xl/")
               for r in rels}
        out = {}
        for sheet in ET.fromstring(archive.read("xl/workbook.xml")).findall("s:sheets/s:sheet", NS):
            rid = sheet.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            out[sheet.get("name")] = ids[rid]
        return out
    old_sheets = sheet_parts(before)
    with ZipFile(path) as current:
        new_sheets = sheet_parts(current)
    count = 0
    for name in old_sheets.keys() & new_sheets.keys():
        src = ET.fromstring(before.read(old_sheets[name]))
        target = ET.fromstring(parts[new_sheets[name]])
        cells = {c.get("r"): c for c in src.findall(".//s:c", NS)}
        for c in target.findall(".//s:c", NS):
            old = cells.get(c.get("r"))
            if old is None:
                continue
            f, pf = c.find("s:f",NS), old.find("s:f",NS)
            if f is None or pf is None or f.text != pf.text or f.attrib != pf.attrib:
                continue
            v = old.find("s:v",NS)
            if v is None:
                continue
            newv = c.find("s:v",NS)
            if newv is not None:
                c.remove(newv)
            c.append(deepcopy(v))
            if old.get("t") is not None:
                c.set("t",old.get("t"))
            else:
                c.attrib.pop("t",None)
            count += 1
        parts[new_sheets[name]] = ET.tostring(target)
    with ZipFile(path,"w",ZIP_DEFLATED) as out:
        for name,data in parts.items():
            out.writestr(name,data)
    return count


def save_workbook(book, path):
    path = Path(path)
    original = path.read_bytes()
    book.save(path)
    retain_formula_cache(original,path)
