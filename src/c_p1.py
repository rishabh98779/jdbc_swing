"""PART 1 — Introduction to Database Connectivity."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_universal():
    b = []
    # left: without JDBC
    b.append(rect(8, 8, 300, 236, "#fbfcfd", LINE, 2))
    b.append(txt(158, 26, "WITHOUT A STANDARD API", 8, RED, 700, "middle", ls="0.08em"))
    apps = ["Payroll", "Library", "Result portal"]
    dbs = ["Oracle", "MySQL", "SQL Server"]
    for i in range(3):
        b.append(node(22, 40 + i * 62, 74, 34, apps[i], None, WHITE, NAVY, NAVY, 8.2, 600))
        b.append(node(216, 40 + i * 62, 76, 34, dbs[i], None, WHITE, RED, RED, 8.2, 600))
    for i in range(3):
        for j in range(3):
            y1, y2 = 57 + i * 62, 57 + j * 62
            b.append(f'<path d="M96 {y1} C 140 {y1}, 150 {y2}, 216 {y2}" fill="none" '
                     f'stroke="{RED}" stroke-width="0.7" opacity="0.55"/>')
    b.append(txt(158, 232, "9 different adapters for 3 programs × 3 databases", 7.4, RED, 600, "middle"))

    # right: with JDBC
    b.append(rect(322, 8, 350, 236, "#fbfcfd", LINE, 2))
    b.append(txt(497, 26, "WITH JDBC", 8, TEAL, 700, "middle", ls="0.08em"))
    for i in range(3):
        b.append(node(336, 44 + i * 56, 76, 32, apps[i], None, WHITE, NAVY, NAVY, 8.2, 600))
        b.append(node(566, 44 + i * 56, 92, 32, dbs[i], None, WHITE, TEAL, TEAL, 8.2, 600))
    b.append(rect(432, 40, 110, 176, TEAL_L, TEAL, 3))
    b.append(f'<text x="487" y="120" font-family="{SANS}" font-size="9.4" font-weight="700" '
             f'fill="{TEAL}" text-anchor="middle">JDBC</text>')
    b.append(f'<text x="487" y="134" font-family="{SANS}" font-size="7.2" fill="{TEAL}" '
             f'text-anchor="middle">one API</text>')
    b.append(f'<text x="487" y="146" font-family="{SANS}" font-size="7.2" fill="{TEAL}" '
             f'text-anchor="middle">one set of classes</text>')
    for i in range(3):
        y = 60 + i * 56
        b.append(arrow(414, y, 430, y, NAVY3, 1.0, hs=4.6))
        b.append(arrow(544, y, 564, y, ORANGE, 1.0, hs=4.6))
    b.append(txt(497, 232, "3 programs + 3 drivers = 6 pieces, written once", 7.4, TEAL, 600, "middle"))
    return svg(680, 250, "".join(b))


def fig_three_activities():
    b = []
    y = 34
    b.append(node(14, y, 168, 56, "1  Connect", "open a session to the data source", WHITE, NAVY, NAVY, 9.0, 700, 7.2))
    b.append(node(238, y, 168, 56, "2  Send SQL", "executeQuery / executeUpdate", WHITE, TEAL, TEAL, 9.0, 700, 7.2))
    b.append(node(462, y, 168, 56, "3  Process", "walk the ResultSet with next()", WHITE, ORANGE, ORANGE, 9.0, 700, 7.2))
    b.append(arrow(184, y + 28, 234, y + 28, NAVY3, 1.4, hs=6.4))
    b.append(arrow(408, y + 28, 458, y + 28, NAVY3, 1.4, hs=6.4))
    # repeat loop
    b.append(poly([(546, y + 58), (546, 126), (322, 126), (322, y + 60)], TEAL2, 1.2, dash="4 3", hs=6.0))
    b.append(txt(434, 140, "repeat steps 2 and 3 for every query or update", 7.4, TEAL2, 600, "middle"))
    b.append(poly([(98, y + 58), (98, 160), (20, 160), (20, y + 62)], MUTED, 1.1, dash="4 3", hs=5.6))
    b.append(txt(120, 174, "close once, at the very end (reverse order)", 7.4, MUTED, 400, "start"))
    b.append(rect(300, 168, 340, 26, GREY, LINE, 2))
    b.append(txt(470, 185, "Connection lives for the whole session", 7.4, MUTED, 600, "middle"))
    return svg(660, 204, "".join(b))


def fig_packages():
    b = []
    b.append(rect(10, 10, 320, 200, WHITE, TEAL, 2.5))
    b.append(rect(10, 10, 320, 24, TEAL, TEAL, 2.5))
    b.append(txt(24, 26, "java.sql  —  the client-side API", 8.6, WHITE, 700))
    left = ["Driver", "DriverManager", "Connection", "Statement", "PreparedStatement",
            "CallableStatement", "ResultSet", "ResultSetMetaData", "DatabaseMetaData", "SQLException"]
    for i, s in enumerate(left):
        col, row = i // 5, i % 5
        b.append(txt(26 + col * 156, 52 + row * 20, s, 7.8, INK, 400, "start", MONO))
    b.append(rect(350, 10, 320, 200, WHITE, NAVY2, 2.5))
    b.append(rect(350, 10, 320, 24, NAVY2, NAVY2, 2.5))
    b.append(txt(364, 26, "javax.sql  —  the server-side API", 8.6, WHITE, 700))
    right = ["DataSource", "ConnectionPoolDataSource", "PooledConnection",
             "XADataSource", "XAConnection", "RowSet", "StatementEventListener"]
    for i, s in enumerate(right):
        b.append(txt(366, 52 + i * 20, s, 7.8, INK, 400, "start", MONO))
    b.append(txt(366, 200, "Added in JDBC 2.0 for pooling and distributed work.", 7.2, MUTED, 400))
    return svg(680, 220, "".join(b))


def html():
    o = []
    o.append(part(1, "Introduction to Database Connectivity",
                  "Why a Java program has to cross a boundary to reach its data, and the single API "
                  "Java uses to make that crossing.", art_icon=1))
    o.append(sec("1.1", "The problem JDBC solves"))
    o.append(p("Almost every real program outlives its own memory. A student record, an invoice, a "
               "login credential — these must survive the end of the program, be visible to other users, "
               "and be searchable without loading everything into RAM. The component that stores data "
               "permanently and answers questions about it is a <b>database management system</b> (DBMS). "
               "For a Java program, the DBMS is a separate process, often on a separate machine."))
    o.append(p("So a Java program faces a boundary problem: on one side there is Java, with objects, "
               "references and a garbage collector; on the other side there is a relational database, with "
               "tables, rows, SQL and its own network protocol. Data has to travel across that boundary in "
               "both directions — a query goes out, rows come back."))
    o.append(p("The naive solution is to let each program speak the vendor's protocol directly. That works, "
               "and it fails at scale: three programs and three databases need nine pieces of glue code, and "
               "changing one database means editing every program that touches it."))
    o.append(fig(fig_universal(),
                 "Why a standard API matters. Without one, every program must be rewritten for every "
                 "database (left). With JDBC, each program is written once against the API and each vendor "
                 "supplies one driver (right)."))
    o.append(p("JDBC is that standard API. It is a set of Java interfaces — not a program, not a server — "
               "that both sides agree to implement. Your code calls the interfaces; the database vendor "
               "supplies a <b>driver</b> that implements them for its product. The result is the same code "
               "for MySQL, Oracle, PostgreSQL or SQL Server; only the driver, the URL and the credentials change."))

    o.append(box("def", "Definition",
                 "<p><b>JDBC (Java Database Connectivity)</b> is a Java-based API that provides a standard "
                 "interface for connecting Java applications with relational databases. It allows Java "
                 "programs to interact with databases, execute SQL queries, and retrieve or update data. "
                 "JDBC was developed by JavaSoft of Sun Microsystems and is part of the Java platform "
                 "(packages <span class='mono'>java.sql</span> and <span class='mono'>javax.sql</span>).</p>"))

    o.append(sec("1.2", "What JDBC actually does: three activities"))
    o.append(p("The JDBC documentation reduces the whole API to three programming activities. Everything "
               "in Parts 3 to 6 is a detail of one of them."))
    o.append(ol(["<b>Connect to a data source</b>, such as a database — establish a session with the DBMS.",
                 "<b>Send queries and update statements</b> to the database — usually SQL.",
                 "<b>Retrieve and process the results</b> received from the database in answer to your query."]))
    o.append(fig(fig_three_activities(),
                 "The three activities of JDBC. Connection happens once; send and process repeat in a loop; "
                 "closing happens once at the end."))
    o.append(p("An analogy makes the boundary concrete. Think of the database as a records office in another "
               "building, and JDBC as the <b>standardized request form</b> that every office in the country "
               "agrees to accept. You fill in the form in your own language (Java). A courier (the driver) "
               "carries it. The office answers on the same form (the <span class='mono'>ResultSet</span>). "
               "You never need to learn the internal filing system of each office, and the office never needs "
               "to learn your program."))

    o.append(sec("1.3", "JDBC and ODBC"))
    o.append(p("Before JDBC, the dominant database API was Microsoft's <b>ODBC</b> (Open Database Connectivity). "
               "ODBC performs the same task — it lets an application call a database through a uniform "
               "interface — and JDBC was deliberately built on ODBC's design, retaining ideas such as the "
               "X/Open SQL Call Level Interface. The difference is the language they are written for."))
    o.append(tbl("JDBC compared with ODBC",
                 ["Aspect", "ODBC", "JDBC"],
                 [["Target language", "Any language that can call C", "Java only"],
                  ["Written in", "C — platform dependent", "Java — platform independent"],
                  ["Pointers", "Uses C pointers", "No pointers; object references only"],
                  ["Security model", "Native calls outside the JVM's protection", "Runs inside the JVM sandbox"],
                  ["Design philosophy", "Mixes simple and advanced features", "Simple by default, advanced when needed"],
                  ["Portability", "Recompile per platform", "Write once, run anywhere (WORA)"]],
                 ["22%", "39%", "39%"]))
    o.append(box("imp", "Important",
                 "<p>ODBC cannot be used directly from Java because it uses a C interface. Calls from Java to "
                 "native C code have drawbacks in <b>security, implementation, robustness and automatic "
                 "portability</b>. ODBC also makes use of pointers, which have been removed from Java "
                 "altogether. This is the whole reason Java defined its own API.</p>"))
    o.append(p("The exam usually asks this as “Why is JDBC preferred over ODBC?” — answer with the four "
               "drawbacks plus one sentence on pointers, and you have the full mark."))

    o.append(sec("1.4", "When should you use JDBC?"))
    o.append(p("The lecture material lists four situations in which JDBC is the natural choice. They are "
               "useful as a ready-made answer to “justify the use of JDBC”."))
    o.append(ul(["<b>Java environment</b> — JDBC is a natural choice for Java applications, and provides a "
                 "native, well-integrated solution on the JVM.",
                 "<b>Platform independence</b> — the same program runs on any operating system for which a JVM "
                 "exists, because the driver is written in Java.",
                 "<b>Object-oriented programming</b> — JDBC lets you keep Java's object-oriented features; "
                 "rows become objects, and connections are objects with behaviour.",
                 "<b>Direct connectivity</b> — JDBC talks to the database without an intermediate layer, using "
                 "a database-specific driver."]))
    o.append(box("tip", "Exam tip",
                 "<p>“Justify the use of JDBC” wants <i>reasons</i>, not a definition. Use the four headings "
                 "above as four bullet points, then add one example each. Four bullets with examples is a "
                 "complete 5-mark answer.</p>"))

    o.append(sec("1.5", "The shape of the API: two packages"))
    o.append(p("JDBC is delivered as two packages. <span class='mono'>java.sql</span> contains everything a "
               "client program needs; <span class='mono'>javax.sql</span> adds server-side facilities such as "
               "connection pooling and distributed transactions. Both are part of Java SE, so no separate "
               "download is required to compile JDBC code — only the vendor's driver JAR is needed at run time."))
    o.append(fig(fig_packages(),
                 "The two JDBC packages. The interfaces you will use in this unit are all in "
                 "<span class='mono'>java.sql</span>; <span class='mono'>DataSource</span> from "
                 "<span class='mono'>javax.sql</span> returns in Part 14."))
    o.append(p("<span class='mono'>java.sql</span> also contains classes (<span class='mono'>DriverManager</span>, "
               "<span class='mono'>Date</span>, <span class='mono'>Time</span>, <span class='mono'>Timestamp</span>, "
               "<span class='mono'>Types</span>) and exceptions (<span class='mono'>SQLException</span>, "
               "<span class='mono'>SQLWarning</span>, <span class='mono'>DataTruncation</span>). In an exam, "
               "“name the interfaces of java.sql” is a one-mark question with a long answer; the six that matter "
               "are <b>Driver, DriverManager, Connection, Statement, ResultSet</b> and <b>SQLException</b>."))

    o.append(sec("1.6", "A first look at the whole journey"))
    o.append(p("Before the details, look at the complete path once. A JDBC program always performs the same "
               "seven steps; later parts explain each one, but the order never changes."))
    o.append(code('''import java.sql.*;                       // 1. import the package

public class FirstQuery {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");        // 2. load the driver
        Connection con = DriverManager.getConnection(     // 3. open a connection
                "jdbc:mysql://localhost:3306/mydb", "root", "your_password");
        Statement stmt = con.createStatement();           // 4. create a statement
        ResultSet rs = stmt.executeQuery("SELECT id, name FROM student");  // 5. execute
        while (rs.next()) {                               // 6. process the ResultSet
            System.out.println(rs.getInt("id") + "  " + rs.getString("name"));
        }
        rs.close();                                       // 7. close, innermost first
        stmt.close();
        con.close();
    }
}''', "java", "The seven steps, in order, with nothing else"))
    o.append(p("Read it as a sentence: <i>load a driver, open a session, ask a question, walk through the "
               "answer, then shut everything down in reverse order</i>. That sentence is the skeleton of every "
               "program in Part 16."))
    o.append(box("trick", "Memory trick",
                 "<p><b>I L C S E P C</b> — <b>I</b>mport, <b>L</b>oad, <b>C</b>onnect, <b>S</b>tatement, "
                 "<b>E</b>xecute, <b>P</b>rocess, <b>C</b>lose. The lecture's short form is "
                 "<i>Load → Connect → Prepare → Execute → Result</i>. Both compress to the same five ideas.</p>"))

    o.append(sec("1.7", "Summary"))
    o.append(ul(["JDBC is an API — a contract of interfaces — not a database and not a server.",
                 "It exists because Java cannot call ODBC's C interface safely, and because a single API "
                 "removes N × M glue code.",
                 "Every JDBC program connects, sends SQL, processes results and closes.",
                 "The API lives in <span class='mono'>java.sql</span> (client side) and "
                 "<span class='mono'>javax.sql</span> (server side).",
                 "A vendor-supplied driver is what actually talks to the database."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Expand JDBC and name the company that developed it. "
                 "<b>2.</b> Give two technical reasons why Java does not simply use ODBC. "
                 "<b>3.</b> Which two packages make up the JDBC API?</p>"
                 "<p class='small'><i>Answers:</i> (1) Java Database Connectivity, JavaSoft of Sun Microsystems. "
                 "(2) ODBC uses a C interface and pointers; native calls weaken security, robustness and "
                 "portability. (3) <span class='mono'>java.sql</span> and <span class='mono'>javax.sql</span>.</p>"))
    o.append(recap("Part 1 recap", [
        ["<b>JDBC</b>", "Java Database Connectivity — a Java API for executing SQL on relational databases."],
        ["<b>Why not ODBC</b>", "Java cannot safely call ODBC's C interface, and native calls weaken security, "
                                "robustness and portability."],
        ["<b>The N × M problem</b>", "One API removes the need for N programs to write M different integrations."],
        ["<b>Packages</b>", "<span class='mono'>java.sql</span> on the client side, "
                            "<span class='mono'>javax.sql</span> on the server side."],
        ["<b>Vendor role</b>", "The JDK ships interfaces; the vendor ships a driver that implements them."],
        ["<b>Seven steps</b>", "Import, load driver, connect, create statement, execute, process, close."],
        ["<b>Minimum table</b>", "Connection, Statement, ResultSet — the three objects every JDBC program needs."],
    ], terms=["JDBC", "ODBC", "JDBC driver", "Connection", "Statement", "ResultSet", "the N × M problem", "java.sql", "javax.sql"], practice=[
        "Expand JDBC and name the two packages that make up the API.",
        "Give two technical reasons Java does not call ODBC directly.",
        "State the seven steps of a JDBC program in order.",
    ], trap="Do not say that JDBC is a driver. JDBC is the API; a vendor's driver implements it."))
    return "".join(o)
