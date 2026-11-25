# Unit 3 textbook build — repository guide

## What this repo produces

`Unit_3_GUI_and_Database_Connectivity_Complete_Notes.pdf` — a 125-page A4 textbook for
Object Oriented Programming (25CSH-208), Unit 3 "GUI and Database Connectivity"
(JDBC, annotations, Spring Boot, XML/DTD/XSD, Maven, Spring JDBC, POJO/JavaBean),
built from `PPT 3 (1).pdf` and styled after `linkedlist_trees_hashings_Striver.pdf`.

## Build

```bash
cd src && python3 build.py      # ~1-2 min, writes the PDF at the repo root
```

The pipeline is pure Python: HTML + inline SVG → WeasyPrint → PDF, then a pymupdf
post-pass. `build.py` renders up to three times so that the printed table of contents
and the PDF outline carry real page numbers (`toc_css()` emits static `leader()` rules
from the previous pass; `measure()` reads anchor page numbers from internal links).

## Source layout

| File | Role |
| --- | --- |
| `src/build.py` | render loop, TOC CSS injection, `measure()`, `clean_outline()` |
| `src/common.py` | `part()`, `sec()`, `tbl()`, `fig()`, `code()`, `box()`, `recap()`; `TOC` / `CODE_REGISTRY` |
| `src/dia.py` | SVG primitives (`svg`, `node`, `arrow`, `rect`, `txt`, `legend`, palette) |
| `src/art.py` | part-banner and cover artwork |
| `src/style.css` | all page, type, table, code and callout styling |
| `src/c_front.py` | cover, title page, contents, how-to-use, objectives, coverage map |
| `src/c_p1.py` … `c_p18.py` | one module per PART; each exposes `html()` |

## Conventions that matter when editing content

- **Registered, not hard-coded, numbering.** Figures, tables and programs are numbered
  by CSS counters per part (`Figure 10.2`, `Table 5.3`, `PROGRAM 5.6`). Never type a
  number by hand; add the element and the counter does it. Cross-references in prose are
  the exception — re-check them after inserting elements into a part.
- **Page numbers.** Front-matter pages are fixed: contents 3, how-to-use 7, objectives 9,
  coverage map 10, Part 1 starts 11 (`c_front.py` and `clean_outline()` both assume this).
  Changing front matter means updating those constants.
- **`recap()`** closes every part: keepertbl recap table + "ask yourself" + a three-column
  vocabulary grid (`terms=`) + one trap. Keep it `break-inside: avoid`; letting the recap
  table split produced near-empty pages.
- **Diagrams** are inline SVG with `viewBox` width 660 and unit-sized text. A 7.0-unit
  label renders at ≈5.5 pt, which is too small for legends — use ≥8.0 for anything a
  student must read.

## QA recipe (used before each delivery)

```python
import pymupdf, itertools
d = pymupdf.open(PDF)
# 1. overlaps: bounding boxes of text spans sharing >35% of their area
# 2. fill ratio per page: lowest block/drawing y, ignoring the footer (page height - 62)
# 3. outline sanity: every level-2 bookmark must contain its "N.M" number and first word
# 4. rasterise suspect pages at 100-300 dpi and look at them
```

Current baseline: 125 pages, 150 contents entries, 154 bookmarks, 55 figures,
57 tables, 67 programs, 0 overlapping text spans, mean page fill 0.845 (lowest 0.51 on
part-closing recap pages, which is intentional).
