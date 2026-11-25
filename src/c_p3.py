"""PART 3 — JDBC Drivers and Establishing Connectivity."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_four_types():
    b = []
    titles = [("TYPE 1", "JDBC-ODBC bridge driver", RED),
              ("TYPE 2", "Native-API, partly Java", ORANGE),
              ("TYPE 3", "Network protocol, pure Java", TEAL),
              ("TYPE 4", "Thin driver, 100% Java", NAVY2)]
    chains = [
        [("Java app", NAVY, WHITE), ("JDBC-ODBC bridge", RED, WHITE), ("ODBC driver (C)", RED_L, RED), ("Database", NAVY2, WHITE)],
        [("Java app", NAVY, WHITE), ("Native-API driver", ORANGE, WHITE), ("Vendor library (C)", ORANGE_L, ORANGE), ("Database", NAVY2, WHITE)],
        [("Java app", NAVY, WHITE), ("Network driver", TEAL, WHITE), ("Middleware server", TEAL_L, TEAL), ("Database", NAVY2, WHITE)],
        [("Java app", NAVY, WHITE), ("Thin driver (Java)", NAVY2, WHITE), ("Database", NAVY2, WHITE)],
    ]
    notes = ["Slowest. Needs ODBC and a DSN on every client.",
             "Faster. Needs the vendor library on every client.",
             "Flexible. One driver reaches many databases.",
             "Fastest. One JAR, nothing else to install."]
    for i in range(4):
        x0 = 10 + i * 162
        b.append(rect(x0, 10, 152, 300, "#fbfcfd", LINE, 2))
        b.append(txt(x0 + 10, 28, titles[i][0], 7.2, titles[i][2], 700, ls="0.1em"))
        b.append(txtw(x0 + 10, 42, titles[i][1], 132, 7.8, INK, 600, "start")[0])
        y = 76
        for j, (lab, fill, tc) in enumerate(chains[i]):
            b.append(node(x0 + 14, y, 124, 36, lab, None, fill, fill if fill in (NAVY, NAVY2, TEAL, ORANGE, RED) else tc, tc, 7.8, 600))
            if j < len(chains[i]) - 1:
                b.append(arrow(x0 + 76, y + 36, x0 + 76, y + 52, MUTED, 1.1, hs=5.0))
            y += 52
        b.append(txtw(x0 + 10, 278, notes[i], 132, 6.9, MUTED, 400, "start")[0])
    return svg(660, 318, "".join(b))


def fig_type_paths():
    b = []
    # type 1 and type 2 zoom: show translation layers
    b.append(txt(12, 16, "WHAT EACH DRIVER CONVERTS", 7.2, MUTED, 700, ls="0.1em"))
    rows = [("Type 1", "JDBC call", "→ ODBC call", "→ native DB call", RED),
            ("Type 2", "JDBC call", "→ vendor C API call", "→ native DB call", ORANGE),
            ("Type 3", "JDBC call", "→ middleware protocol", "→ native DB call", TEAL),
            ("Type 4", "JDBC call", "→ DBMS wire protocol", "(no further translation)", NAVY2)]
    y = 34
    for name, a, bb, c, col in rows:
        b.append(txt(12, y + 12, name, 7.8, col, 700))
        b.append(rect(60, y, 108, 18, WHITE, col, 2))
        b.append(txt(114, y + 12.5, a, 7.2, INK, 400, "middle"))
        b.append(arrow(170, y + 9, 186, y + 9, col, 1.0, hs=4.6))
        b.append(rect(188, y, 148, 18, col, col, 2))
        b.append(txt(262, y + 12.5, bb, 7.2, WHITE, 600, "middle"))
        b.append(arrow(338, y + 9, 354, y + 9, col, 1.0, hs=4.6))
        b.append(rect(356, y, 176, 18, WHITE, col, 2))
        b.append(txt(444, y + 12.5, c, 7.2, MUTED, 400, "middle"))
        y += 26
    b.append(txt(12, y + 6, "The fewer arrows, the faster the call — and the fewer things to install on the client.", 7.2, MUTED, 400))
    return svg(660, y + 16, "".join(b))


def fig_seven_steps():
    b = []
    steps = [("1", "Import", "java.sql.*"), ("2", "Load driver", "Class.forName"), ("3", "Connect", "getConnection"),
             ("4", "Statement", "createStatement"), ("5", "Execute", "executeQuery"), ("6", "Process", "rs.next()"),
             ("7", "Close", "close()")]
    x = 10
    for i, (n, t, s) in enumerate(steps):
        fill, stroke, tc = (NAVY, NAVY, WHITE) if i < 3 else ((TEAL_L, TEAL, TEAL) if i < 6 else (ORANGE_L, ORANGE, ORANGE))
        b.append(node(x, 40, 84, 56, t, s, fill, stroke, tc, 8.0, 700, 6.6, MUTED if tc != WHITE else "#d5e2ee"))
        b.append(f'<circle cx="{x + 12}" cy="40" r="8.5" fill="{ORANGE}"/>')
        b.append(txt(x + 12, 43.2, n, 7.6, WHITE, 700, "middle"))
        if i < 6:
            b.append(arrow(x + 86, 68, x + 94, 68, NAVY3, 1.2, hs=5.4))
        x += 94
    b.append(rect(10, 110, 84, 22, GREY, LINE, 2))
    b.append(txt(52, 125, "once", 7.0, MUTED, 600, "middle"))
    b.append(rect(104, 110, 274, 22, GREY, LINE, 2))
    b.append(txt(241, 125, "once per connection", 7.0, MUTED, 600, "middle"))
    b.append(rect(388, 110, 262, 22, GREY, LINE, 2))
    b.append(txt(519, 125, "repeat per query", 7.0, MUTED, 600, "middle"))
    b.append(txt(10, 20, "THE SEVEN STEPS — AND HOW OFTEN EACH ONE RUNS", 7.2, MUTED, 700, ls="0.1em"))
    return svg(660, 142, "".join(b))


def fig_url():
    b = []
    segs = [("jdbc:", "API", TEAL_L, TEAL), ("mysql:", "sub-protocol (DBMS)", ORANGE_L, ORANGE),
            ("//localhost:", "host", BLUE_L, NAVY3), ("3306", "port", GREY2, MUTED), ("/mydb", "database", TEAL_L, TEAL)]
    x = 14
    y = 52
    b.append(txt(14, 26, "ANATOMY OF A JDBC URL", 8.6, MUTED, 700, ls="0.1em"))
    for text_, label, fill, stroke in segs:
        w = 20 + len(text_) * 7.4
        b.append(rect(x, y, w, 34, fill, stroke, 2.5))
        b.append(txt(x + w / 2, y + 22, text_, 10.4, MUTED if fill is GREY2 else stroke, 600, "middle", MONO))
        b.append(line(x + w / 2, y + 36, x + w / 2, y + 46, stroke if fill is not GREY2 else MUTED, 0.9, "2 2"))
        b.append(txt(x + w / 2, y + 62, label, 8.4, MUTED if fill is GREY2 else stroke, 700, "middle"))
        x += w
    b.append(txt(14, 140, "Oracle form", 8.4, MUTED, 700))
    b.append(txt(96, 140, "jdbc:oracle:thin:@localhost:1521:xe", 9.6, INK, 400, "start", MONO))
    b.append(txt(14, 160, "Only host, port and database name change between installations; the prefix is fixed by the driver.",
                 8.2, MUTED, 400))
    return svg(660, 172, "".join(b))


def fig_lifecycle():
    b = []
    lanes = [150, 340, 530]
    names = ["JVM / driver registry", "Application objects", "Database session"]
    b.append(rect(20, 14, 620, 26, GREY, LINE, 2))
    for i, n in enumerate(names):
        b.append(txt(lanes[i], 31, n, 8.4, NAVY, 700, "middle", ls="0.04em"))
    for x in lanes:
        b.append(line(x, 42, x, 268, LINE, 0.8, "3 3"))
    msgs = [
        (64, "Class.forName(\"com.mysql.cj.jdbc.Driver\")", 1, 0, "call"),
        (88, "registerDriver(d)", 0, 0, "self"),
        (118, "getConnection(url, user, pass)", 1, 2, "call"),
        (142, "Connection object", 2, 1, "ret"),
        (170, "createStatement()", 1, 1, "self"),
        (198, "executeQuery(sql)", 1, 2, "call"),
        (222, "ResultSet object", 2, 1, "ret"),
        (248, "rs.close(), stmt.close(), con.close()", 1, 2, "call"),
    ]
    for y, label, a, bb, kind in msgs:
        x1, x2 = lanes[a], lanes[bb]
        if kind == "self":
            b.append(poly([(x1, y), (x1 + 54, y), (x1 + 54, y + 9), (x1 + 4, y + 9)], TEAL2, 1.1, hs=5.2))
            b.append(txt(x1 + 62, y + 8, label, 8.2, INK, 400, "start", MONO))
        elif kind == "call":
            b.append(arrow(x1 + 2, y, x2 - 2, y, NAVY3, 1.1, hs=5.6))
            b.append(txt((x1 + x2) / 2, y - 8, label, 8.2, INK, 400, "middle", MONO))
        else:
            b.append(arrow(x1 - 2, y, x2 + 2, y, TEAL, 1.0, hs=5.2, dash="4 2"))
            b.append(txt((x1 + x2) / 2, y - 8, label, 8.2, TEAL, 600, "middle"))
    b.append(txt(20, 288, "Solid arrows are calls; dashed arrows are values coming back. Every object is created by the one before it.",
                 8.2, MUTED, 400))
    return svg(660, 296, "".join(b))


def html():
    o = []
    o.append(part(3, "JDBC Drivers and Connectivity",
                  "Four ways to build a driver, seven steps to open a session, and one URL that ties "
                  "them together.", art_icon=3))

    o.append(sec("3.1", "What a JDBC driver is"))
    o.append(p("A driver is the only part of JDBC that knows anything about a particular database product. "
               "Everything above it is a standard interface; everything below it is the vendor's own network "
               "protocol. Without a driver, JDBC is just a list of method signatures with no implementation."))
    o.append(box("def", "Definition",
                 "<p>A <b>JDBC driver</b> is a software component that enables a Java application to interact with "
                 "a database. It implements the interfaces defined in the JDBC API for interacting with a "
                 "particular database server, so that you can open database connections and send SQL commands, "
                 "then receive results, using Java.</p>"))
    o.append(p("The <span class='mono'>java.sql</span> package that ships with the JDK contains the interfaces with "
               "their behaviour defined; the actual implementations are done in third-party drivers. Vendors "
               "implement <span class='mono'>java.sql.Driver</span> in their own classes — which is why the driver "
               "class name differs for every database, and why the JAR must be on the classpath."))
    o.append(p("An analogy: a driver is a <b>travel adapter</b>. Your laptop's plug (the JDBC call) is the same "
               "everywhere; the wall socket (the database) differs by country. The adapter does not change your "
               "laptop or the wall — it only converts one shape into the other. Four kinds of adapter exist, and "
               "the next sections explain why the cheap ones are slow."))

    o.append(sec("3.2", "The four driver types at a glance"))
    o.append(p("Sun divided driver implementations into four categories, numbered 1 to 4. The number tells you "
               "<b>how many translations</b> a call must pass through before it reaches the database — and therefore "
               "how fast it is and how much software must be installed on the client."))
    o.append(box("trick", "Memory trick",
                 "<p>Count the layers: <b>1 = two bridges</b> (JDBC → ODBC → native), <b>2 = one bridge</b> "
                 "(JDBC → native API), <b>3 = one hop</b> (JDBC → middleware → database), <b>4 = no bridge</b> "
                 "(JDBC → database directly). Type 4 is “pure Java, pure protocol, pure speed”.</p>"))
    o.append(fig(fig_four_types(),
                 "The four JDBC driver types. Each column is one driver; each box is a layer the call must pass "
                 "through. Count the boxes: the shorter the chain, the faster the driver."))
    o.append(fig(fig_type_paths(),
                 "What each driver type converts a JDBC call into. Type 4 speaks the DBMS's own wire protocol, so "
                 "no further translation happens."))
    o.append(sec("3.3", "Type 1 — the JDBC-ODBC bridge"))
    o.append(p("A Type 1 driver translates all JDBC calls into ODBC calls and sends them to the ODBC driver. ODBC is "
               "a generic API, so the bridge can reach almost any database — but every call pays for two "
               "translations. Using ODBC also requires a <b>Data Source Name (DSN)</b> to be configured on each "
               "client machine, describing the target database."))
    o.append(p("When Java first appeared this was a useful driver, because most databases supported only ODBC. "
               "Today it is recommended only for experimental use, or when no other alternative is available. The "
               "JDBC-ODBC Bridge that shipped with JDK 1.2 is the classic example; it lives in the "
               "<span class='mono'>sun.jdbc.odbc</span> package and contains a native library, and it was removed "
               "from the JDK in Java 8."))
    o.append(cards("Advantages", ["Access to almost any database, because ODBC drivers already exist for it.",
                                  "No vendor-specific Java driver needed.",
                                  "Useful for prototypes and for legacy data sources."],
                   "Disadvantages", ["Not written fully in Java, so not portable.",
                                     "Slowest of all types: JDBC → bridge → ODBC → database, and back.",
                                     "ODBC must be installed and a DSN configured on every client.",
                                     "Not suitable for the web."]))

    o.append(sec("3.4", "Type 2 — native-API, partly Java"))
    o.append(p("A Type 2 driver converts JDBC calls into <b>database-specific native calls</b> — the C or C++ API "
               "supplied by the database vendor, such as Oracle's OCI. The driver is therefore specific to one "
               "database, and the vendor's client library must be installed on every client machine."))
    o.append(cards("Advantages", ["Better performance than Type 1: fewer communication layers.",
                                  "Uses the vendor's native API, which is database-specific and efficient."],
                   "Disadvantages", ["The native API must be installed on the client, so it cannot be used for the Internet.",
                                     "Not written in Java, so portability suffers.",
                                     "Changing the database means changing the native API.",
                                     "Mostly obsolete now, and usually not thread-safe."]))

    o.append(sec("3.5", "Type 3 — network protocol, pure Java"))
    o.append(p("A Type 3 driver sends database requests through the network to a <b>middle-tier server</b>, which "
               "translates them into the database's own protocol. The client needs no vendor library at all: it "
               "speaks one generic protocol to the middleware, and the middleware may itself use Type 1, Type 2 or "
               "Type 4 drivers to reach the database. Think of the middleware as a JDBC <b>proxy</b> that makes "
               "calls on the client's behalf."))
    o.append(cards("Advantages", ["Server-based: no vendor library on client machines.",
                                  "Fully written in Java, hence portable and suitable for the web.",
                                  "One driver can access multiple databases.",
                                  "Supports caching, load balancing, logging and auditing.",
                                  "The most efficient of the network-based types."],
                   "Disadvantages", ["Requires a middleware server to install, configure and maintain.",
                                     "Traversing the recordset may take longer, because data comes through the backend server.",
                                     "Extra network hop adds a point of failure."]))

    o.append(sec("3.6", "Type 4 — thin driver, 100% Java"))
    o.append(p("A Type 4 driver is a pure-Java driver that communicates <b>directly</b> with the vendor's database "
               "through a socket connection, speaking the DBMS's native wire protocol. It is the highest-performance "
               "driver available for that database, and it is usually supplied by the vendor itself, because the "
               "network protocol is proprietary. MySQL's Connector/J and the modern "
               "<span class='mono'>mysql-connector-j</span> are Type 4 drivers."))
    o.append(cards("Advantages", ["Completely written in Java: platform independence and no deployment administration.",
                                  "Fewest translation layers, so performance is typically very good.",
                                  "Nothing to install on the client or the server except the JVM and the JAR.",
                                  "The JAR can be downloaded dynamically; ideal for the web."],
                   "Disadvantages", ["A different driver is needed for each database product.",
                                     "Larger JAR than a thin Type 3 client, because the protocol lives inside it."]))
    o.append(box("mistake", "Common mistake",
                 "<p>Writing <span class='mono'>Class.forName(\"com.mysql.jdbc.Driver\")</span> in new code. That was "
                 "the MySQL 5 class name; MySQL Connector/J 8+ uses "
                 "<span class='mono'>com.mysql.cj.jdbc.Driver</span>. The old name still resolves in some versions but "
                 "prints a deprecation warning, and it disappears in newer ones.</p>"))

    o.append(sec("3.7", "Choosing a driver"))
    o.append(tbl("Comparison of the four driver types",
                 ["Feature", "Type 1", "Type 2", "Type 3", "Type 4"],
                 [["Name", "JDBC-ODBC bridge", "Native API", "Network protocol", "Thin driver"],
                  ["Written in", "Java + ODBC", "Java + native", "Pure Java", "Pure Java"],
                  ["Platform dependent", "Yes", "Yes", "No", "No"],
                  ["Performance", "Low", "Better", "Good", "High"],
                  ["Requires middleware", "No", "No", "Yes", "No"],
                  ["Client install", "ODBC + DSN", "Vendor library", "Nothing", "Nothing"],
                  ["Example", "Old JDBC-ODBC", "Oracle OCI", "Middleware server", "MySQL Connector/J"]],
                 ["24%", "19%", "19%", "19%", "19%"]))
    o.append(p("The lecture material gives a decision rule that is worth memorizing verbatim:"))
    o.append(ul(["Accessing <b>one</b> type of database (Oracle, Sybase, IBM)? Prefer <b>Type 4</b>.",
                 "Accessing <b>multiple</b> types of database at the same time? Prefer <b>Type 3</b>.",
                 "Type 3 or Type 4 not yet available for your database? Use <b>Type 2</b>.",
                 "<b>Type 1</b> is not a deployment-level driver; it is for development and testing only."]))

    o.append(sec("3.8", "Establishing connectivity: the seven steps"))
    o.append(p("The lecture material describes opening a connection in seven steps. They are the same seven steps "
               "seen in Part 1, now with their API calls attached."))
    o.append(fig(fig_seven_steps(),
                 "The seven steps, and how often each runs. Steps 1 and 2 happen once per program; step 3 once per "
                 "connection; steps 4 to 7 repeat for each unit of work."))
    o.append(ol([
        "<b>Import the packages</b> — <span class='mono'>import java.sql.*;</span> for the standard JDBC classes, "
        "and <span class='mono'>import java.math.*;</span> when decimal and integer support is needed.",
        "<b>Load the JDBC driver</b> — <span class='mono'>Class.forName(\"com.mysql.cj.jdbc.Driver\");</span> "
        "registers the driver with DriverManager.",
        "<b>Open a connection</b> — "
        "<span class='mono'>DriverManager.getConnection(url, user, password)</span> returns a "
        "<span class='mono'>Connection</span>.",
        "<b>Create a Statement object</b> — <span class='mono'>con.createStatement()</span>, "
        "<span class='mono'>con.prepareStatement(sql)</span> or <span class='mono'>con.prepareCall(sql)</span>.",
        "<b>Execute a query and get a ResultSet</b> — <span class='mono'>stmt.executeQuery(sql)</span>.",
        "<b>Process the ResultSet</b> — loop with <span class='mono'>while (rs.next()) { ... }</span>.",
        "<b>Close the ResultSet, Statement and Connection</b> — <span class='mono'>close()</span> on each, "
        "innermost first."]))
    o.append(box("imp", "Important",
                 "<p>Step 7 is not optional decoration. Closing frees server-side cursors and network sockets. Java's "
                 "garbage collector will eventually close a stale connection, but “eventually” can be minutes, and a "
                 "database has a hard limit on concurrent sessions. A program that leaks connections works in a lab "
                 "and fails under load.</p>"))

    o.append(sec("3.9", "The JDBC URL"))
    o.append(p("A JDBC URL is the address of a database, written in a form that lets DriverManager choose the right "
               "driver before any network traffic happens. Its grammar is fixed:"))
    o.append(fig(fig_url(),
                 "Anatomy of a JDBC URL. DriverManager matches the sub-protocol (<span class='mono'>mysql</span>, "
                 "<span class='mono'>oracle</span>, <span class='mono'>postgresql</span>) to decide which driver "
                 "should handle the request."))
    o.append(tbl("Popular JDBC driver names and URL formats",
                 ["RDBMS", "Driver class", "URL format"],
                 [["Oracle", "<code>oracle.jdbc.driver.OracleDriver</code>", "<code>jdbc:oracle:thin:@host:port:dbName</code>"],
                  ["MySQL", "<code>com.mysql.cj.jdbc.Driver</code>", "<code>jdbc:mysql://host:3306/dbName</code>"],
                  ["DB2", "<code>COM.ibm.db2.jdbc.net.DB2Driver</code>", "<code>jdbc:db2:host:port/dbName</code>"],
                  ["Sybase", "<code>com.sybase.jdbc.SybDriver</code>", "<code>jdbc:sybase:Tds:host:port/dbName</code>"],
                  ["MS Access", "<code>sun.jdbc.odbc.JdbcOdbcDriver</code>", "<code>jdbc:odbc:dsnName</code>"]],
                 ["14%", "44%", "42%"]))
    o.append(p("For MySQL, <span class='mono'>jdbc</span> is the API, <span class='mono'>mysql</span> is the "
               "database sub-protocol, <span class='mono'>localhost</span> is the server name (an IP address works "
               "equally well), <span class='mono'>3306</span> is the port, and <span class='mono'>mydb</span> is the "
               "database name. The default MySQL user is <span class='mono'>root</span>; the password is whatever was "
               "set when the server was installed."))

    o.append(sec("3.10", "Loading the driver, and what can go wrong"))
    o.append(p("<span class='mono'>Class.forName()</span> dynamically loads the driver class into memory. The class "
               "creates an instance of itself and registers that instance with "
               "<span class='mono'>java.sql.DriverManager</span>, which is responsible for managing all the JDBC "
               "drivers installed on the system. The method throws "
               "<span class='mono'>ClassNotFoundException</span> when the driver class cannot be found, so the call "
               "must appear in a <span class='mono'>try</span> block with an appropriate "
               "<span class='mono'>catch</span>."))
    o.append(tbl("Three failures every beginner meets",
                 ["Symptom", "Cause", "Fix"],
                 [["<code>ClassNotFoundException: com.mysql.cj.jdbc.Driver</code>",
                   "The driver JAR is not on the classpath",
                   "Add <code>-cp lib/mysql-connector-j-9.x.jar</code> (or a Maven dependency)"],
                  ["<code>SQLException: No suitable driver found for jdbc:mysql://...</code>",
                   "The driver was never loaded, or the URL prefix is wrong",
                   "Call <code>Class.forName</code>, and check the sub-protocol spelling"],
                  ["<code>SQLException: Access denied for user 'root'@'localhost'</code>",
                   "Wrong username or password, or the user lacks privileges",
                   "Use the real credentials; grant privileges in MySQL"]],
                 ["36%", "30%", "34%"]))
    o.append(code('''import java.sql.*;      // for standard JDBC programs
import java.math.*;     // for Decimal and Integer support

public class LoadDriver {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver registered successfully");
        } catch (ClassNotFoundException e) {
            System.out.println("Driver JAR missing from the classpath: " + e);
        }
    }''', "java", "Loading and registering a driver, with the exception that actually occurs"))
    o.append(box("tip", "Exam tip",
                 "<p>A common one-mark question: “Which exception does "
                 "<span class='mono'>Class.forName()</span> throw?” — <b>ClassNotFoundException</b>, a checked "
                 "exception from <span class='mono'>java.lang</span>. Do not confuse it with "
                 "<span class='mono'>SQLException</span>, which is thrown by the JDBC calls that follow.</p>"))

    o.append(sec("3.11", "Making the driver available: JAR and classpath"))
    o.append(p("The driver is distributed as a JAR. For MySQL the file is "
               "<span class='mono'>mysql-connector-j-9.x.x.jar</span>. There are two ways to make it visible to the "
               "JVM, and the lecture material shows both:"))
    o.append(ol(["<b>Copy the JAR into the extension folder</b> — "
                 "<span class='mono'>jre/lib/ext</span>. The JVM loads it automatically for every program, which is "
                 "convenient for a lab machine and a bad idea for a real project, because the dependency becomes "
                 "invisible.",
                 "<b>Set the classpath</b> — the correct approach. Compile and run with "
                 "<span class='mono'>javac -cp \".;lib/mysql-connector-j-9.x.x.jar\" App.java</span> and "
                 "<span class='mono'>java -cp \".;lib/mysql-connector-j-9.x.x.jar\" App</span> (on Windows the "
                 "separator is <span class='mono'>;</span>, on Linux and macOS it is <span class='mono'>:</span>)."]))
    o.append(box("imp", "Important",
                 "<p>A Maven or Gradle project never touches the classpath by hand: the dependency in "
                 "<span class='mono'>pom.xml</span> is downloaded into the local repository and added to the "
                 "classpath automatically. That is the subject of Part 12.</p>"))

    o.append(sec("3.12", "The end-to-end workflow"))
    o.append(p("Putting the steps on a timeline makes the ownership clear: which object exists when, and which "
               "object talks to which. The sequence diagram below is the one to sketch if a question asks for "
               "\"the connection lifecycle\"."))
    o.append(fig(fig_lifecycle(),
                 "Sequence diagram of one complete JDBC session. Solid arrows are calls; dashed arrows are values "
                 "returned. Notice that every object is created by the one above it."))
    o.append(p("The lecture material compresses this into a one-line shortcut: "
               "<b>Load → Connect → Prepare → Execute → Result</b>. Write it at the top of your answer sheet before "
               "you start any JDBC question; the marks are almost always distributed along it."))
    o.append(code('''// The whole workflow, with resource handling done correctly
import java.sql.*;

public class LifecycleDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydb";
        try (Connection con = DriverManager.getConnection(url, "root", "your_password");
             Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT id, name FROM student")) {
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getString("name"));
            }
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        }
    }
}''', "java", "The same seven steps using try-with-resources (Java 7+)"))
    o.append(box("tip", "Exam tip",
                 "<p>If the question shows the classic explicit-close style, answer in that style — it is what the "
                 "lecture uses. Add one line noting that <span class='mono'>try-with-resources</span> closes "
                 "automatically and is preferred in modern Java; that sentence usually earns the last mark.</p>"))

    o.append(sec("3.13", "Summary"))
    o.append(ul(["A driver is the vendor-supplied implementation of the JDBC interfaces.",
                 "Type 1 bridges to ODBC, Type 2 to a native API, Type 3 to a middleware server, Type 4 speaks the "
                 "database protocol directly in pure Java.",
                 "Fewer translation layers means better performance; fewer client installs means easier deployment.",
                 "Connecting is seven steps: import, load, connect, statement, execute, process, close.",
                 "The URL's sub-protocol is what DriverManager uses to pick a driver."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Which driver type is the fastest, and why? "
                 "<b>2.</b> Which driver type needs a middleware server? "
                 "<b>3.</b> What are the four parts of <span class='mono'>jdbc:mysql://localhost:3306/mydb</span>?</p>"
                 "<p class='small'><i>Answers:</i> (1) Type 4 — it is pure Java and talks the DBMS protocol directly, "
                 "with the fewest translation layers. (2) Type 3. (3) API (<span class='mono'>jdbc</span>), "
                 "sub-protocol (<span class='mono'>mysql</span>), host and port "
                 "(<span class='mono'>localhost:3306</span>), database (<span class='mono'>mydb</span>).</p>"))
    o.append(recap("Part 3 recap", [
        ["<b>Driver</b>", "The vendor's implementation of the JDBC interfaces for one database product."],
        ["<b>Type 1</b>", "JDBC → ODBC → native; portable in theory, slowest in practice."],
        ["<b>Type 2</b>", "JDBC → vendor C library; fast, but the library must be installed everywhere."],
        ["<b>Type 3</b>", "JDBC → middleware server; one driver reaches many databases."],
        ["<b>Type 4</b>", "Pure Java, direct protocol; the default choice for a single database."],
        ["<b>URL</b>", "<span class='mono'>jdbc:subprotocol://host:port/database</span> — the sub-protocol "
                       "selects the driver."],
        ["<b>Loading</b>", "<span class='mono'>Class.forName()</span> runs the driver's static initializer, which "
                           "registers it with DriverManager."],
        ["<b>Classpath</b>", "The driver JAR must be on the classpath — Maven does this automatically."],
        ["<b>Failures</b>", "ClassNotFound = no JAR; no suitable driver = not loaded or bad URL; access denied = "
                            "credentials."],
    ], terms=["Type 1 driver", "Type 2 driver", "Type 3 driver", "Type 4 driver", "JDBC URL", "sub-protocol", "Class.forName", "getConnection()", "classpath"], practice=[
        "List the four driver types, each with its one disadvantage.",
        "Write a JDBC URL for database <span class='mono'>mydb</span> on localhost (MySQL).",
        "<span class='mono'>ClassNotFoundException</span> at connect time means what, exactly?",
    ], trap="Type 4 is the fastest, but its URL and driver class are vendor-specific — they do not move between databases."))
    return "".join(o)
