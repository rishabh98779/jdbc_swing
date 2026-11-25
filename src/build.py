import os
import sys
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from common import TOC, CODE_REGISTRY
import c_front

MODULES = ["c_p1", "c_p2", "c_p3", "c_p4", "c_p5", "c_p6", "c_p7",
           "c_p8", "c_p9", "c_p10", "c_p11", "c_p12", "c_p13", "c_p14", "c_p15",
           "c_p16", "c_p17", "c_p18"]

CSS = open(os.path.join(HERE, "style.css")).read()


def toc_css(pages):
    """Static page numbers for the contents list, measured from a rendered pass."""
    if not pages:
        return ""
    rules = ["/* contents */"]
    for i, (level, anchor, label) in enumerate(TOC):
        if anchor in pages:
            rules.append('.toc a#t%d::after { content: leader(".") "%d"; }' % (i, pages[anchor]))
    return "\n".join(rules)


def measure(path):
    """Map anchor id -> 1-based page number using the internal links of the PDF."""
    import pymupdf
    doc = pymupdf.open(path)
    found = {}
    for page in doc:
        for link in page.get_links():
            dest = link.get("nameddest")
            if dest and dest not in found and link.get("page", -1) >= 0:
                found[dest] = link["page"] + 1
    doc.close()
    return found


def clean_outline(path, pages):
    """Replace WeasyPrint's heading-derived outline with the book's own structure."""
    import re
    import pymupdf
    toc = [[1, "Contents", 3],
           [1, "How to use this book", 7],
           [1, "Learning objectives", 9],
           [1, "Where every syllabus line is taught", 10]]
    for level, anchor, label in TOC:
        if anchor in pages:
            toc.append([level, re.sub(r"\s+", " ", label).strip(), pages[anchor]])
    doc = pymupdf.open(path)
    doc.set_toc(toc)
    doc.saveIncr()
    doc.close()
    return len(toc)


def build(out_pdf="Unit_3_GUI_and_Database_Connectivity_Complete_Notes.pdf", pages=None):
    TOC.clear()
    CODE_REGISTRY.clear()
    content = []
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            print(f"  (skipping missing module {name})")
            continue
        content.append(mod.html())
        print(f"  built {name}")

    parts = [c_front.cover(), c_front.titlepage(), c_front.contents(TOC),
             c_front.howto(), c_front.objectives(), c_front.coverage()]
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>GUI and Database Connectivity — Unit 3 (25CSH-208)</title>
<meta name="author" content="Object Oriented Programming · Chandigarh University">
<meta name="description" content="Complete textbook notes on JDBC, XML, Maven and Spring JDBC for Unit 3, Object Oriented Programming (25CSH-208).">
<style>{CSS}{toc_css(pages)}</style></head><body>{''.join(parts)}{''.join(content)}</body></html>'''

    html_path = os.path.join(HERE, "..", "build", "book.html")
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    open(html_path, "w").write(doc)
    from weasyprint import HTML
    target = os.path.join(HERE, "..", out_pdf)
    HTML(string=doc, base_url=HERE).write_pdf(target)
    print(f"  wrote {out_pdf}: {len(TOC)} TOC entries, {len(CODE_REGISTRY)} code listings")
    return target


if __name__ == "__main__":
    import sys as _sys
    pages = None
    for _ in range(3):
        path = build(pages=pages)
        measured = measure(path)
        if pages == measured:
            break
        pages = measured
    print(f"  contents: {len(pages)} anchors resolved")
    print(f"  outline: {clean_outline(path, pages)} bookmarks")
