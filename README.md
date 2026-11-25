# GUI and Database Connectivity — Unit 3 textbook

`Unit_3_GUI_and_Database_Connectivity_Complete_Notes.pdf` — a 125-page A4 textbook for
**Object Oriented Programming (25CSH-208), Unit 3 "GUI and Database Connectivity"**,
B.E. CSE Semester 3, Chandigarh University (UIE).

It covers JDBC (architecture, driver types, Connection, Statement / PreparedStatement /
CallableStatement, ResultSet, transactions, SQL injection), Java annotations and Spring
Boot, XML with DTD and XSD, namespaces, XSLT and DOM, Maven and `pom.xml`, Spring JDBC
(`JdbcTemplate`, `DataSource`, `DriverManagerDataSource`), and POJO versus JavaBean —
with 55 original SVG diagrams, 57 tables, 67 complete programs, exam preparation
(definitions, MCQs, viva, practical questions) and a last-minute revision sheet.

## Build the PDF

```bash
cd src
python3 build.py      # writes the PDF at the repository root
```

Requirements: Python 3, `weasyprint`, `pymupdf`. The pipeline is HTML + inline SVG rendered
by WeasyPrint, then post-processed by pymupdf (table-of-contents page numbers and PDF
bookmarks). See `AGENTS.md` for the source layout and the QA recipe.

## Layout

| Path | Contents |
| --- | --- |
| `Unit_3_GUI_and_Database_Connectivity_Complete_Notes.pdf` | the book |
| `src/` | build script, stylesheet, one module per part, SVG primitives |
| `fonts/` | Source Serif 4, Source Sans 3, JetBrains Mono (SIL OFL) |
| `AGENTS.md` | architecture notes and quality-check procedure |
