"""Front matter: cover, title page, how-to-use, objectives, coverage map, contents."""
import art
from common import box, tbl, ul, ol, p, fig, code
from dia import (svg, txt, rect, line, arrow, poly, ORANGE, TEAL, NAVY, WHITE, TEAL_L, GREY, MUTED)


def cover():
    return f'''
<div class="cover">
  <div class="art">{art.cover_art()}</div>
  <div class="meta">
    <div class="kicker">Chandigarh University · CSE · B.E. · Semester 3</div>
    <h1>GUI AND DATABASE<br>CONNECTIVITY</h1>
    <div class="sub">Complete Notes on JDBC, XML, Maven and Spring JDBC</div>
    <div class="rule"></div>
    <div class="tags">Object Oriented Programming — Unit 3 &nbsp;|&nbsp; 25CSH-208</div>
    <div class="foot"><b>15 contact hours</b> &nbsp;·&nbsp; 18 parts &nbsp;·&nbsp; 55 diagrams &nbsp;·&nbsp; 57 tables &nbsp;·&nbsp; 67 programs &nbsp;·&nbsp; viva and MCQ bank<br>
    Academic Session 2026–27 (Odd Semester, July–December 2026)</div>
  </div>
</div>'''


def titlepage():
    rows = [
        ("University", "Chandigarh University"),
        ("Institute", "University Institute of Engineering (UIE)"),
        ("Department", "Computer Science and Engineering"),
        ("Programme", "Bachelor of Engineering (B.E.) — CSE"),
        ("Semester", "3rd Semester"),
        ("Subject", "Object Oriented Programming"),
        ("Subject code", "25CSH-208"),
        ("Unit", "Unit 3 — GUI and Database Connectivity"),
        ("Contact hours", "15"),
        ("Academic session", "2026–27"),
        ("Coverage", "JDBC · JDBC architecture · driver types · Connection · Statement interfaces · ResultSet · "
                     "SQL injection · annotations · Spring Boot · Spring JDBC · XML · DTD · XSD · namespaces · "
                     "XSLT · DOM · Maven · pom.xml · JdbcTemplate · DataSource · POJO and JavaBean"),
    ]
    body = "".join(f'<tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in rows)
    return f'''
<div class="plain titlepage">
  <div class="mark">Textbook · Unit 3</div>
  <h1>GUI and Database<br>Connectivity</h1>
  <div class="st">Complete Notes on JDBC, XML, Maven and Spring JDBC</div>
  <table class="metagrid">{body}</table>
  {box("imp", "About this book", "<p>These notes follow the lecture material of Unit 3 closely and extend it into a "
      "complete textbook: every concept is introduced with an analogy, stated as an exam-ready definition, shown in a "
      "labelled diagram, demonstrated in runnable code, and finally reduced to the one line an examiner wants.</p>")}
  <div class="glance">
    <div class="cell"><div class="n">18</div><div class="l">Parts</div></div>
    <div class="cell"><div class="n">55</div><div class="l">Diagrams</div></div>
    <div class="cell"><div class="n">57</div><div class="l">Tables</div></div>
    <div class="cell"><div class="n">67</div><div class="l">Programs</div></div>
  </div>
  <p class="small">Every line of the lecture deck appears somewhere in these pages; the coverage map on
  page 10 shows exactly where each one is taught.</p>
</div>'''


def howto():
    return f'''
<div class="plain" style="break-after:page">
  <div class="mark" style="font-family:Sans;font-weight:700;letter-spacing:.18em;font-size:7.4pt;color:#0e6f6b;text-transform:uppercase">How to use this book</div>
  <h1 style="font-family:Sans;font-size:20pt;color:#10243c;margin:2mm 0 4mm">How to use this book</h1>
  <p>This unit has two halves that look unrelated but are one story. The first half shows how a Java
  program talks to a relational database by hand: JDBC. The second half shows how the same work is done
  once XML, Maven and Spring JDBC are in place. Read the parts in order — Part 9 (Spring JDBC) assumes
  that you are already uncomfortable with the boilerplate of Part 7, and Part 13 assumes you can read a
  <span class="mono">pom.xml</span> from Part 12.</p>

  <h3 class="sub">The five layers of every topic</h3>
  <p>Every major topic is built in the same five layers, so you always know where you are:</p>
  {ol(["<b>Intuition</b> — a plain-English explanation with a real-world analogy.",
       "<b>Definition</b> — the exam-ready sentence you should be able to write word for word.",
       "<b>Mechanism</b> — the step-by-step working, usually with a diagram.",
       "<b>Code</b> — a complete, compilable example with line-by-line commentary.",
       "<b>Examination angle</b> — the trap, the comparison table, the one-mark fact."])}

  <h3 class="sub">The callout system</h3>
  <p>Seven labels are used consistently throughout. Recognising them is half of revision.</p>
  <div class="cards">
    <div class="card"><h5>Knowledge callouts</h5>
    {box("def", "Definition", "<p class=\"small\">The precise statement to reproduce in the exam.</p>")}
    {box("imp", "Important", "<p class=\"small\">A point that is marked often, or that unlocks the next topic.</p>")}
    {box("tip", "Exam tip", "<p class=\"small\">How the question is usually framed, and how to answer it.</p>")}
    </div>
    <div class="card alt"><h5>Learning callouts</h5>
    {box("mistake", "Common mistake", "<p class=\"small\">The error that costs marks in the practical file or viva.</p>")}
    {box("trick", "Memory trick", "<p class=\"small\">A short hook for lists, orders and spellings.</p>")}
    {box("viva", "Interview / Viva", "<p class=\"small\">The follow-up question an examiner asks next.</p>")}
    </div>
  </div>

  <h3 class="sub">Diagram conventions</h3>
  <p>All figures follow one visual grammar, so a diagram can be read before its caption. Three colours
  identify who owns each block, and four connector styles identify what a line means.</p>
  {fig(legend_figure(),
       "Visual grammar. Left: who owns a block. Right: what a connector means. Every figure in the book "
       "uses only these shapes and colours.")}

  <h3 class="sub">A suggested study plan</h3>
  {tbl("Table — three passes over the unit",
       ["Pass", "What you do", "Time"],
       [["Pass 1 — Understand", "Read Parts 1–9 with a pencil; redraw every architecture figure from memory.", "5 hours"],
        ["Pass 2 — Build", "Type and run the programs of Part 16 against your own MySQL database.", "4 hours"],
        ["Pass 3 — Recall", "Work through Part 17 and the revision sheet; answer without looking back.", "3 hours"]],
       ["20%", "60%", "20%"])}

  {box("tip", "If you have only one evening",
       "<p>Read 3.4 (the seven steps), then 6.1–6.2 (how a query is executed), then 9.3 and 13.2 "
       "(why Spring exists and what JdbcTemplate does). Draw the two-layer architecture and the "
       "Spring stack from memory, then answer the ten MCQs of Part 17. That is a pass mark, honestly "
       "earned.</p>")}

  <h3 class="sub">Set up once, run everything</h3>
  <p>Every program in Part 16 runs against one database, one table and one driver. Build that
  environment now and the rest of the book is copy, paste and run.</p>
  {ol(["Install a JDK (17 or later) and MySQL 8, and start the MySQL server.",
       "Download the MySQL Connector/J JAR (<span class='mono'>mysql-connector-j-9.0.0.jar</span>) and keep it "
       "in a <span class='mono'>lib</span> folder beside your programs, or declare it once in "
       "<span class='mono'>pom.xml</span> (Part 12).",
       "Run the SQL below once; it creates the database and the table that every example queries.",
       "Change <span class='mono'>USER</span> and <span class='mono'>PASS</span> in the programs to your own "
       "MySQL account. Nothing else in the code changes."])}
  {code("CREATE DATABASE IF NOT EXISTS mydb;\nUSE mydb;\n\nCREATE TABLE student (\n    id     INT PRIMARY KEY,\n    name   VARCHAR(60) NOT NULL,\n    city   VARCHAR(60),\n    marks  INT\n);\n\nINSERT INTO student VALUES (101, 'Rajesh', 'Guntur', 88);\nINSERT INTO student VALUES (102, 'Simran', 'Patiala', 91);", "sql", "The database and table used by every program in this book", label="")}
</div>'''


def legend_figure():
    b = []
    b.append(txt(14, 14, "WHO OWNS THE BLOCK", 8.2, MUTED, 700, ls="0.08em"))
    blocks = [("Your Java code", WHITE, NAVY, NAVY), ("JDBC / Spring API", TEAL_L, TEAL, TEAL),
              ("Driver or database", WHITE, ORANGE, ORANGE)]
    for i, (name, fill, stroke, tc) in enumerate(blocks):
        x = 14 + i * 108
        b.append(rect(x, 24, 100, 34, fill, stroke, 2))
        b.append(txt(x + 50, 45, name, 8.0, tc, 700, "middle"))
    b.append(txt(14, 76, "navy = you write it    teal = the JDK supplies it    orange = the vendor or the DBMS",
                 7.4, MUTED, 400))

    b.append(txt(356, 14, "WHAT THE CONNECTOR MEANS", 8.2, MUTED, 700, ls="0.08em"))
    rows = [(36, "solid arrow", "a call, in this direction"),
            (64, "dashed arrow", "optional or under-the-hood path"),
            (92, "numbered arrow", "the order of the steps")]
    for y, name, meaning in rows:
        if name == "dashed arrow":
            b.append(arrow(364, y, 406, y, MUTED, 1.2, dash="4 2", hs=5.4))
        elif name == "numbered arrow":
            b.append(arrow(374, y, 406, y, TEAL, 1.4, hs=5.8))
            b.append(rect(350, y - 7.4, 15, 15, TEAL, TEAL, 7.5))
            b.append(txt(357.5, y + 2.8, "1", 8.0, WHITE, 700, "middle"))
        else:
            b.append(arrow(364, y, 406, y, NAVY, 1.4, hs=5.8))
        b.append(txt(414, y + 2.8, name, 7.8, NAVY, 700))
        b.append(txt(484, y + 2.8, meaning, 7.6, MUTED, 400))
    return svg(660, 106, "".join(b))


def objectives():
    items = [
        ("Understand", "Explain what JDBC is, why it exists, and how it differs from ODBC and from Spring JDBC."),
        ("Architect", "Draw and label the two-tier, three-tier and general JDBC architectures, and place "
                      "DriverManager and the four driver types correctly."),
        ("Apply", "Write a complete JDBC program that connects, executes a query and processes a ResultSet."),
        ("Compare", "Distinguish Statement, PreparedStatement and CallableStatement by purpose, performance, "
                    "parameters and security."),
        ("Secure", "Explain SQL injection, demonstrate the attack, and show how parameterised queries prevent it."),
        ("Configure", "Read and write Java annotations, XML, DTD, XSD, namespaces, XSLT and a Maven pom.xml."),
        ("Simplify", "Use JdbcTemplate with a DriverManagerDataSource to replace boilerplate JDBC code."),
        ("Distinguish", "Differentiate a POJO from a JavaBean and explain why frameworks care."),
    ]
    rows = "".join(f'<tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in items)
    return f'''
<div class="plain" style="break-after:page">
  <div class="mark" style="font-family:Sans;font-weight:700;letter-spacing:.18em;font-size:7.4pt;color:#0e6f6b;text-transform:uppercase">Unit 3 · 15 contact hours</div>
  <h1 style="font-family:Sans;font-size:20pt;color:#10243c;margin:2mm 0 4mm">Learning objectives</h1>
  <p>By the end of Unit 3 you should be able to do the following eight things without notes.
  Each objective is a verb, because each one is examinable as a task, not as a definition.</p>
  <table class="metagrid">{rows}</table>
  {box("imp", "Important", "<p>The unit is assessed on three levels. <b>Recall</b>: names, methods and signatures. "
      "<b>Comprehension</b>: why the API is layered, why a driver is needed. <b>Application</b>: write or repair a "
      "program. Most lost marks come from the third level — a program that connects but never closes, or a query "
      "that concatenates user input into SQL.</p>")}
</div>'''


def coverage():
    rows = [
        ["<b>Module A — Database Connectivity</b>", "", ""],
        ["JDBC — what it is and why it exists", "Parts 1, 3", "1.1–1.6, 3.1"],
        ["Architecture of JDBC", "Part 2", "2.1–2.5"],
        ["Two-tier and three-tier models", "Part 2", "2.2–2.3"],
        ["Establishing connectivity", "Part 3", "3.8–3.12"],
        ["Working with the Connection interface", "Part 4", "4.1–4.6"],
        ["Working with statements in database connections", "Parts 5, 6", "5.1–5.7, 6.1–6.9"],
        ["Problems of JDBC", "Part 7", "7.1–7.4"],
        ["Advantages and disadvantages of JDBC", "Part 7", "7.5–7.6"],
        ["<b>Module B — Spring Boot Basics</b>", "", ""],
        ["Annotations", "Part 8", "8.1–8.6"],
        ["Difference between JDBC and Spring JDBC", "Part 9", "9.3"],
        ["XML, XML Schema, XML Namespace", "Parts 10, 11", "10.1–10.8, 11.1–11.2"],
        ["pom.xml (Maven)", "Part 12", "12.1–12.5"],
        ["Spring JDBC Template", "Part 13", "13.1–13.7"],
        ["Spring DriverManagerDataSource", "Part 14", "14.1–14.6"],
        ["Beans vs POJO", "Part 15", "15.1–15.4"],
        ["<b>Additional material present in the slides</b>", "", ""],
        ["JDBC vs ODBC, the N × M problem", "Part 1", "1.5"],
        ["JDBC components, DriverManager, Driver", "Part 2", "2.5–2.7"],
        ["JDBC driver types 1–4", "Part 3", "3.2–3.7"],
        ["ResultSet cursor, navigation and getters", "Part 6", "6.4–6.7"],
        ["SQL injection and parameterised queries", "Part 7", "7.2–7.3"],
        ["Stored procedures, functions, callable statements", "Part 5", "5.4–5.5"],
        ["XSLT and DOM parsing", "Part 11", "11.3–11.5"],
        ["Swing + JDBC login application (the GUI part)", "Part 16", "16.9"],
        ["Complete programs and outputs", "Part 16", "16.1–16.9"],
        ["Exam preparation and revision", "Parts 17, 18", "17.1–17.7, 18.1–18.8"],
    ]
    body = []
    for r in rows:
        if r[1] == "":
            body.append(f'<tr><td colspan="3" style="background:#10243c;color:#fff;font-weight:600;'
                        f'letter-spacing:.04em">{r[0]}</td></tr>')
        else:
            body.append(f'<tr><td class="hl">{r[0]}</td><td>{r[1]}</td><td class="mono">{r[2]}</td></tr>')
    return f"""
<div class="plain" style="break-after:page">
  <div class="mark" style="font-family:Sans;font-weight:700;letter-spacing:.18em;font-size:7.4pt;color:#0e6f6b;text-transform:uppercase">Syllabus · coverage map</div>
  <h1 style="font-family:Sans;font-size:20pt;color:#10243c;margin:2mm 0 4mm">Where every syllabus line is taught</h1>
  <p>The official outline has two modules, but the slides go further — driver types, ResultSet navigation,
  stored procedures, XSLT, DOM and a Swing login application. Every one of those topics is covered; this table
  is the index.</p>
  <div class="tblwrap"><div class="tcap">Coverage map — syllabus line to part and section</div>
  <table class="dt compact"><colgroup><col style="width:46%"><col style="width:22%"><col style="width:32%"></colgroup>
  <thead><tr><th>Syllabus / lecture topic</th><th>Taught in</th><th>Sections</th></tr></thead>
  <tbody>{"".join(body)}</tbody></table></div>
  {box("tip", "Exam tip", "<p>Keep this page open while revising. If you can name the part and section for a topic "
      "without looking, you know the unit's map — which is exactly what a long-answer question tests first.</p>")}
</div>"""


def contents(entries):
    out = ['<div class="toc"><h2>Contents</h2>'
           '<div class="tsub">Parts, sections and page numbers</div><ol>']
    for i, (level, anchor, label) in enumerate(entries):
        if level == 1:
            num, name = label.split(" · ", 1)
            out.append(f'<li class="l1"><span class="partlbl">{num}</span><br>'
                       f'<a id="t{i}" href="#{anchor}">{name}</a></li>')
        else:
            out.append(f'<li class="l2"><a id="t{i}" href="#{anchor}">{label}</a></li>')
    out.append("</ol></div>")
    return "".join(out)
