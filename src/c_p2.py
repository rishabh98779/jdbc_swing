"""PART 2 — JDBC Architecture."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_layers():
    b = []
    b.append(node(20, 20, 140, 40, "Java application", None, NAVY, NAVY, WHITE, 8.8, 700))
    # JDBC API layer
    b.append(rect(20, 74, 620, 52, TEAL_L, TEAL, 2))
    b.append(txt(34, 96, "JDBC API layer", 9.4, TEAL, 700))
    b.append(txt(34, 112, "java.sql · javax.sql — what your program calls", 7.6, TEAL, 400))
    b.append(node(330, 82, 130, 36, "Connection", None, WHITE, TEAL, TEAL, 8.2, 600))
    b.append(node(470, 82, 152, 36, "Statement · ResultSet", None, WHITE, TEAL, TEAL, 8.2, 600))
    # Driver API layer
    b.append(rect(20, 140, 620, 52, ORANGE_L, ORANGE, 2))
    b.append(txt(34, 162, "JDBC Driver API layer", 9.4, ORANGE, 700))
    b.append(txt(34, 178, "java.sql.Driver — implemented by the vendor", 7.6, ORANGE, 400))
    b.append(node(330, 148, 130, 36, "Driver", None, WHITE, ORANGE, ORANGE, 8.2, 600))
    b.append(node(470, 148, 150, 36, "DriverManager", None, WHITE, ORANGE, ORANGE, 8.2, 600))
    # drivers
    for i, lab in enumerate(["MySQL driver", "Oracle driver", "PostgreSQL driver"]):
        b.append(node(30 + i * 205, 214, 180, 34, lab, None, WHITE, NAVY3, NAVY3, 8.2, 600))
    b.append(node(240, 272, 180, 38, "Relational database", None, NAVY2, NAVY2, WHITE, 8.6, 700))
    b.append(arrow(90, 60, 90, 72, NAVY3, 1.2, hs=5.6))
    b.append(arrow(90, 126, 90, 138, TEAL, 1.2, hs=5.6))
    b.append(arrow(120, 192, 120, 212, ORANGE, 1.2, hs=5.6))
    b.append(arrow(330, 248, 330, 270, NAVY3, 1.2, hs=5.6))
    b.append(legend(20, 336, [("JDBC API layer (JDK)", TEAL_L, TEAL), ("Driver layer (vendor JAR)", ORANGE_L, ORANGE)], 7.2))
    return svg(660, 348, "".join(b))


def fig_two_tier():
    b = []
    b.append(rect(16, 16, 286, 200, "#fbfcfd", NAVY3, 3))
    b.append(txt(159, 36, "CLIENT MACHINE", 7.6, NAVY3, 700, "middle", ls="0.1em"))
    b.append(node(40, 52, 238, 40, "Java application", None, NAVY, NAVY, WHITE, 8.8, 700))
    b.append(node(40, 106, 238, 40, "JDBC driver", "Type 3 or Type 4", WHITE, ORANGE, ORANGE, 8.6, 700, 7.2))
    b.append(node(40, 160, 238, 34, "Connection / Statement objects", None, TEAL_L, TEAL, TEAL, 8.0, 600))
    b.append(arrow(90, 92, 90, 104, NAVY3, 1.2, hs=5.6))

    b.append(rect(400, 16, 244, 200, "#fbfcfd", NAVY3, 3))
    b.append(txt(522, 36, "SERVER MACHINE", 7.6, NAVY3, 700, "middle", ls="0.1em"))
    b.append(node(424, 74, 196, 44, "DBMS process", None, NAVY2, NAVY2, WHITE, 8.8, 700))
    b.append(node(424, 132, 196, 68, "Data files", "tables · indexes · logs", WHITE, NAVY3, NAVY3, 8.4, 600, 7.2))
    b.append(arrow(280, 112, 420, 92, ORANGE, 1.5, hs=6.6))
    b.append(arrow(420, 104, 280, 132, TEAL2, 1.5, hs=6.6))
    b.append(txt(350, 84, "SQL over", 7.2, ORANGE, 700, "middle"))
    b.append(txt(350, 95, "the network", 7.2, ORANGE, 700, "middle"))
    b.append(txt(350, 148, "rows back", 7.2, TEAL2, 700, "middle"))
    b.append(txt(330, 234, "the network may be an intranet or the Internet", 7.4, MUTED, 400, "middle"))
    return svg(660, 246, "".join(b))


def fig_three_tier():
    b = []
    b.append(rect(10, 16, 168, 176, "#fbfcfd", NAVY3, 3))
    b.append(txt(94, 34, "TIER 1 · CLIENT", 7.2, NAVY3, 700, "middle", ls="0.08em"))
    b.append(node(28, 52, 132, 46, "Browser or", "Swing client", WHITE, NAVY, NAVY, 8.4, 600, 7.2))
    b.append(node(28, 112, 132, 52, "Thin JDBC", "or HTTP client", WHITE, TEAL, TEAL, 8.4, 600, 7.2))

    b.append(rect(200, 16, 244, 176, "#fbfcfd", TEAL, 3))
    b.append(txt(322, 34, "TIER 2 · MIDDLE TIER", 7.2, TEAL, 700, "middle", ls="0.08em"))
    b.append(node(216, 48, 212, 40, "Application server", None, TEAL_L, TEAL, TEAL, 8.4, 700))
    b.append(node(216, 96, 212, 30, "business logic / EJB / Spring", None, WHITE, TEAL, INK, 7.6, 400))
    b.append(node(216, 132, 212, 34, "JDBC driver", None, WHITE, ORANGE, ORANGE, 8.2, 600))

    b.append(rect(462, 16, 182, 176, "#fbfcfd", NAVY3, 3))
    b.append(txt(553, 34, "TIER 3 · DATA", 7.2, NAVY3, 700, "middle", ls="0.08em"))
    b.append(node(480, 52, 146, 46, "DBMS", None, NAVY2, NAVY2, WHITE, 8.6, 700))
    b.append(node(480, 112, 146, 52, "Data files", None, WHITE, NAVY3, NAVY3, 8.2, 600))

    b.append(arrow(162, 76, 214, 68, NAVY3, 1.3, hs=5.8))
    b.append(arrow(214, 88, 162, 96, TEAL2, 1.3, hs=5.8))
    b.append(arrow(430, 146, 478, 80, ORANGE, 1.3, hs=5.8))
    b.append(arrow(478, 96, 430, 158, ORANGE, 1.3, hs=5.8))
    b.append(txt(322, 212, "commands go up the middle tier; results come back down", 7.4, MUTED, 400, "middle"))
    return svg(660, 224, "".join(b))


def fig_call_path():
    b = []
    steps = [
        ("1", "Your Java code", "con.createStatement()", NAVY, NAVY, WHITE),
        ("2", "JDBC API interface", "java.sql.Connection", TEAL_L, TEAL, TEAL),
        ("3", "DriverManager", "picks a registered driver", ORANGE_L, ORANGE, ORANGE),
        ("4", "Vendor driver", "speaks the DBMS protocol", WHITE, ORANGE, ORANGE),
        ("5", "DBMS", "parses SQL, reads pages", NAVY2, NAVY2, WHITE),
    ]
    x = 12
    for i, (n, t, s, fill, stroke, tc) in enumerate(steps):
        b.append(node(x, 40, 118, 62, t, s, fill, stroke, tc, 8.2, 700, 7.0,
                      MUTED if tc != WHITE else "#dbe6f0"))
        b.append(f'<circle cx="{x + 10}" cy="40" r="9" fill="{ORANGE}" />')
        b.append(txt(x + 10, 43.4, n, 8, WHITE, 700, "middle"))
        if i < 4:
            b.append(arrow(x + 120, 71, x + 136, 71, NAVY3, 1.4, hs=6.2))
        x += 138
    b.append(rect(12, 118, 636, 30, GREY, LINE, 2))
    b.append(txt(24, 137, "Interface on the left, implementation on the right — your code never names a vendor class.", 7.6, MUTED, 400))
    b.append(txt(24, 26, "A CALL TRAVELS LEFT TO RIGHT; THE RESULT TRAVELS BACK", 7.4, MUTED, 700, ls="0.08em"))
    return svg(660, 158, "".join(b))


def fig_components():
    b = []
    b.append(rect(200, 10, 260, 34, NAVY, NAVY, 2))
    b.append(txt(330, 32, "JDBC product", 9.6, WHITE, 700, "middle"))
    comps = [("JDBC API", "interfaces your code calls", TEAL_L, TEAL, TEAL),
             ("JDBC Driver Manager", "loads and selects drivers", ORANGE_L, ORANGE, ORANGE),
             ("JDBC Test Suite", "checks a driver's compliance", WHITE, NAVY3, NAVY3),
             ("JDBC-ODBC Bridge", "Type 1 access to ODBC sources", WHITE, RED, RED)]
    for i, (t, s, fill, stroke, tc) in enumerate(comps):
        x = 10 + i * 162
        b.append(line(x + 72, 44, x + 72, 64, LINE, 1.0))
        b.append(node(x, 64, 145, 54, t, s, fill, stroke, tc, 8.2, 700, 7.0))
    b.append(txt(330, 140, "The four components named in the lecture material. The first two are Java code;", 7.4, MUTED, 400, "middle"))
    b.append(txt(330, 152, "the test suite is a conformance tool, and the bridge is a legacy Type 1 driver.", 7.4, MUTED, 400, "middle"))
    return svg(660, 160, "".join(b))


def html():
    o = []
    o.append(part(2, "JDBC Architecture",
                  "Two layers, two deployment models, five moving parts — and the exact path a single "
                  "SQL call takes.", art_icon=2))

    o.append(sec("2.1", "Two layers, not one"))
    o.append(p("The word “architecture” frightens students because it sounds like a building. In JDBC it means "
               "something simpler: <b>which layer talks to which</b>. JDBC splits the work into two layers so that "
               "the Java side can be frozen while database vendors keep changing their own software."))
    o.append(ul(["<b>JDBC API layer</b> — provides the application-to-DriverManager connection. It is what your "
                 "program calls: <span class='mono'>Connection</span>, <span class='mono'>Statement</span>, "
                 "<span class='mono'>ResultSet</span>.",
                 "<b>JDBC Driver API layer</b> — supports the DriverManager-to-driver connection. It is what the "
                 "vendor implements: <span class='mono'>java.sql.Driver</span> and friends."]))
    o.append(p("Think of a wall socket. The shape of the socket is the JDBC API, fixed by a standard committee. "
               "Any appliance built to that shape (any driver) can be plugged in, and any appliance works in any "
               "house. You never rewire the house when you buy a new appliance — you buy a new plug."))
    o.append(fig(fig_layers(),
                 "The two layers of JDBC. Your program only ever sees the teal layer; the orange layer is supplied "
                 "by the database vendor as a JAR file. DriverManager sits on the boundary and selects the right "
                 "driver at run time."))
    o.append(box("def", "Definition",
                 "<p><b>JDBC architecture</b> consists of two layers: the <b>JDBC API</b>, which provides the "
                 "application-to-JDBC-Manager connection, and the <b>JDBC Driver API</b>, which supports the "
                 "JDBC-Manager-to-Driver connection. The API uses a driver manager and database-specific drivers "
                 "to provide transparent connectivity to heterogeneous databases.</p>"))
    o.append(p("The word <b>transparent</b> in that definition is the examinable one. Transparent connectivity "
               "means your program is not aware of which DBMS it is talking to: the same "
               "<span class='mono'>executeQuery()</span> call reaches MySQL or Oracle unchanged. The DriverManager "
               "ensures that the correct driver is used for each data source, and it can support multiple "
               "concurrent drivers connected to multiple heterogeneous databases."))

    o.append(sec("2.2", "Two-tier architecture (client–server)"))
    o.append(p("In the two-tier model a Java application talks <b>directly</b> to the data source. This requires a "
               "JDBC driver that can communicate with that particular data source. A user's commands are "
               "delivered to the database and the results are sent straight back to the user."))
    o.append(p("The data source may be on another machine reached over a network. That is a "
               "<b>client/server configuration</b>: the user's machine is the client, the machine holding the data "
               "is the server. The network may be an intranet connecting employees of one corporation, or the "
               "Internet."))
    o.append(fig(fig_two_tier(),
                 "Two-tier architecture. The driver lives with the application on the client; only SQL and rows "
                 "cross the network. Simple, but the client must be trusted with database credentials."))
    o.append(box("imp", "Important",
                 "<p>Two-tier is simple and fast because there is no middle layer to traverse. It is also the least "
                 "secure and least scalable model: every client holds credentials and a driver, so the database "
                 "must accept connections from many machines, and business rules cannot be changed centrally.</p>"))

    o.append(sec("2.3", "Three-tier architecture"))
    o.append(p("In the three-tier model, commands are sent to a <b>middle tier</b> of services, which then sends "
               "them to the data source. The data source processes the commands and returns the results to the "
               "middle tier, which passes them to the user. Nothing reaches the database except through the middle."))
    o.append(fig(fig_three_tier(),
                 "Three-tier architecture. The middle tier is where the JDBC driver now lives, and where access "
                 "control, connection pooling and business logic are enforced."))
    o.append(p("The lecture material gives three reasons why organizations prefer this model. They are worth "
               "memorizing as a three-mark answer:"))
    o.append(ol(["<b>Control</b> — the middle tier makes it possible to maintain control over access and the kinds "
                 "of updates that can be made to corporate data. MIS directors find this very attractive.",
                 "<b>Deployment</b> — it simplifies the deployment of applications, because the client is thin.",
                 "<b>Performance</b> — in many cases the three-tier architecture can provide performance advantages, "
                 "especially with connection pooling and caching in the middle tier."]))
    o.append(p("Historically the middle tier was written in C or C++ for speed. With optimizing compilers that "
               "translate Java bytecode into efficient machine-specific code, and technologies such as "
               "Enterprise JavaBeans, the Java platform has become a standard middle-tier platform — which is why "
               "JDBC is used more and more in the middle tier. Its support for connection pooling, distributed "
               "transactions and disconnected rowsets is what makes it a server technology."))
    o.append(tbl("Two-tier compared with three-tier",
                 ["Criterion", "Two-tier (client–server)", "Three-tier"],
                 [["Path of a call", "Client → database", "Client → middle tier → database"],
                  ["Where the driver lives", "On each client", "On the application server"],
                  ["Security", "Weak: credentials on every client", "Strong: single controlled entry point"],
                  ["Scalability", "Limited by open database connections", "Good: pooling and load balancing"],
                  ["Maintenance", "Redeploy every client", "Change the middle tier only"],
                  ["Typical example", "Desktop app connecting to MySQL", "Web app: browser → Java server → database"]],
                 ["22%", "39%", "39%"]))
    o.append(box("tip", "Exam tip",
                 "<p>When a question says “explain the architecture of JDBC”, draw <b>both</b> models, then the "
                 "general two-layer diagram, then the call path. Four small labelled sketches earn more than one "
                 "large paragraph.</p>"))

    o.append(sec("2.4", "The complete call path"))
    o.append(p("Both deployment models share the same internal path. The figure below is the single most useful "
               "diagram in the unit: almost every long answer about JDBC can be built on top of it."))
    o.append(fig(fig_call_path(),
                 "The complete JDBC call path. Interfaces are on the left of the boundary, implementations on the "
                 "right. Numbered arrows show the order of resolution for one call."))
    o.append(p("Read the diagram as a sentence: <i>my code calls an interface; the interface is implemented by "
               "DriverManager, which chooses a registered driver; the driver converts the call into the DBMS "
               "protocol; the DBMS executes it.</i> Two consequences follow. First, your code compiles without any "
               "vendor JAR — only the interfaces from the JDK are needed. Second, the driver must be present at "
               "run time, or the same code throws "
               "<span class='mono'>No suitable driver found</span>."))

    o.append(sec("2.5", "The four JDBC product components"))
    o.append(p("The lecture material lists four components of the JDBC product. They are often confused with the "
               "interfaces, so learn them as a set of four names with one sentence each."))
    o.append(fig(fig_components(),
                 "The four JDBC product components and what each one is responsible for."))
    o.append(tbl("The four components and their roles",
                 ["Component", "Role"],
                 [["JDBC API", "Provides access to the relational database from Java. Supplies the industrial "
                               "standard for connecting Java to a wide range of databases, and gives “write once, "
                               "run anywhere” access — even to tabular sources such as spreadsheets and flat files."],
                  ["JDBC Driver Manager", "Manages the list of database drivers. Matches connection requests from "
                                          "the application with the proper driver using a communication sub-protocol; "
                                          "the first driver that recognizes the sub-protocol is used."],
                  ["JDBC Test Suite", "Ensures that JDBC drivers will run the user's program. Useful for testing a "
                                      "driver during its development, and for checking the requirements of the "
                                      "Java platform."],
                  ["JDBC-ODBC Bridge", "A Type 1 driver that translates JDBC method calls into ODBC function calls, "
                                       "giving JDBC access to any database for which an ODBC driver exists. It lives "
                                       "in the <span class='mono'>sun.jdbc.odbc</span> package and contains a native "
                                       "library."]],
                 ["22%", "78%"]))
    o.append(box("mistake", "Common mistake",
                 "<p>Students list <span class='mono'>Connection</span>, <span class='mono'>Statement</span> and "
                 "<span class='mono'>ResultSet</span> as “components of JDBC”. They are <i>interfaces of the JDBC "
                 "API</i>. The four <b>components</b> are the API, the Driver Manager, the Test Suite and the "
                 "JDBC-ODBC Bridge.</p>"))

    o.append(sec("2.6", "DriverManager: the dispatcher"))
    o.append(p("The <span class='mono'>DriverManager</span> class acts as an interface between the user and the "
               "drivers. It keeps track of the drivers that are available and handles establishing a connection "
               "between a database and the appropriate driver. It maintains a list of <span class='mono'>Driver</span> "
               "classes that have registered themselves by calling "
               "<span class='mono'>DriverManager.registerDriver()</span>."))
    o.append(tbl("Commonly used methods of DriverManager",
                 ["Method", "Description"],
                 [["<code>static void registerDriver(Driver d)</code>", "Registers the given driver with DriverManager"],
                  ["<code>static void deregisterDriver(Driver d)</code>", "Removes the driver from the list"],
                  ["<code>static Connection getConnection(String url)</code>", "Establishes a connection to the given URL"],
                  ["<code>static Connection getConnection(String url, String user, String password)</code>",
                   "Establishes a connection with credentials"],
                  ["<code>static Driver getDriver(String url)</code>", "Returns the driver that understands this URL"],
                  ["<code>static Enumeration&lt;Driver&gt; getDrivers()</code>", "Lists all registered drivers"]],
                 ["44%", "56%"]))
    o.append(p("Two details are frequently examined. First, <span class='mono'>getConnection()</span> throws "
               "<span class='mono'>SQLException</span>, not <span class='mono'>ClassNotFoundException</span> — the "
               "driver-loading method is the one that throws the class exception. Second, since JDBC 4.0 the call to "
               "<span class='mono'>Class.forName()</span> is technically optional, because drivers are discovered "
               "through the service-provider mechanism (<span class='mono'>META-INF/services/java.sql.Driver</span>). "
               "The lecture examples keep the explicit call, and so do we: it is still the safest habit, and it is "
               "what examiners expect to see."))

    o.append(sec("2.7", "The Driver interface"))
    o.append(p("A JDBC driver is a software component that enables a Java application to interact with a database. "
               "It <b>implements the interfaces defined in the JDBC API</b> for interacting with a particular "
               "database server. Vendors implement <span class='mono'>java.sql.Driver</span> in their own driver "
               "classes; the JDK only ships the interfaces, plus a couple of utilities."))
    o.append(p("You rarely touch a <span class='mono'>Driver</span> object directly. You use "
               "<span class='mono'>DriverManager</span>, which manages objects of that type and hides the details. "
               "The driver's job is to answer one question — <i>do I understand this URL?</i> — and, if the answer is "
               "yes, to open the socket, perform the handshake and hand back a "
               "<span class='mono'>Connection</span>."))
    o.append(code('''// What Class.forName() causes, in effect:
Driver d = (Driver) Class.forName("com.mysql.cj.jdbc.Driver")
                       .getDeclaredConstructor().newInstance();
DriverManager.registerDriver(new DriverShim(d));

// DriverManager then chooses by URL prefix:
//   jdbc:mysql://...     -> the MySQL driver claims it
//   jdbc:oracle:thin:@... -> the Oracle driver claims it''', "java",
              "Driver registration, shown explicitly — this is what the static initializer of the driver class does"))
    o.append(box("viva", "Interview / Viva",
                 "<p><b>Q.</b> Why does a driver class register itself in a static block?<br>"
                 "<b>A.</b> Because <span class='mono'>Class.forName()</span> runs the class's static initializer. "
                 "The driver puts <span class='mono'>DriverManager.registerDriver(new Driver())</span> there, so "
                 "merely loading the class makes it available — no explicit registration call is needed in your "
                 "program.</p>"))

    o.append(sec("2.8", "Summary"))
    o.append(ul(["JDBC has two layers: the JDBC API (application → DriverManager) and the JDBC Driver API "
                 "(DriverManager → driver).",
                 "Two-tier: client talks to the database directly. Three-tier: a middle tier sits between them and "
                 "provides control, easier deployment and better performance.",
                 "The call path is always: code → API interface → DriverManager → driver → DBMS.",
                 "The four product components are the JDBC API, the Driver Manager, the Test Suite and the "
                 "JDBC-ODBC Bridge.",
                 "DriverManager selects a driver by URL sub-protocol; drivers register themselves when loaded."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Name the two layers of JDBC architecture and say what each connects. "
                 "<b>2.</b> Give two advantages and one disadvantage of three-tier over two-tier. "
                 "<b>3.</b> Which method of DriverManager returns a Connection?</p>"
                 "<p class='small'><i>Answers:</i> (1) JDBC API: application-to-DriverManager; JDBC Driver API: "
                 "DriverManager-to-driver. (2) Central access control, easier deployment and better performance; but "
                 "an extra server to install, configure and maintain. (3) "
                 "<span class='mono'>getConnection(String url, String user, String password)</span>.</p>"))
    o.append(recap("Part 2 recap", [
        ["<b>Two layers</b>", "JDBC API (you → DriverManager) and JDBC Driver API (DriverManager → driver)."],
        ["<b>Call path</b>", "Code → API interface → DriverManager → driver → DBMS. Learn this as one line."],
        ["<b>Two-tier</b>", "Client program talks to the database directly; simple, fast, but the driver lives on "
                            "every client."],
        ["<b>Three-tier</b>", "A middle tier (application server) owns the driver and connections; adds control and "
                              "central deployment."],
        ["<b>Four components</b>", "JDBC API, Driver Manager, JDBC Test Suite, JDBC-ODBC Bridge (historical)."],
        ["<b>Registration</b>", "A driver registers itself when its class is loaded — that is why "
                                "<span class='mono'>Class.forName()</span> used to matter."],
        ["<b>Selection</b>", "DriverManager picks a driver by the URL sub-protocol, e.g. "
                             "<span class='mono'>jdbc:mysql:</span>."],
    ], terms=["two-tier architecture", "three-tier architecture", "JDBC API", "JDBC driver API", "DriverManager", "Driver interface", "middleware server", "database protocol", "JDBC components"], practice=[
        "Name both layers of the architecture and say what each one connects.",
        "Draw two-tier and three-tier; give one disadvantage of three-tier.",
        "Complete the chain: code → ? → ? → ? → DBMS.",
    ], trap="DriverManager belongs to the JDBC API layer. Placing it inside the driver layer costs the diagram mark."))
    return "".join(o)
