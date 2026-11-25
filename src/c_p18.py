"""PART 18 — Last-Minute Revision and Coverage Checklist."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_map():
    b = []
    b.append(node(252, 112, 156, 52, "UNIT 3", "GUI and database connectivity",
                  NAVY, NAVY, WHITE, 10.8, 700, 7.6, "#d5e2ee"))
    left = [("JDBC API", "architecture, drivers, Connection,\nStatement, ResultSet", TEAL, TEAL_L),
            ("Security", "SQL injection and parameterized SQL", RED, RED_L),
            ("Annotations", "five categories, Spring Boot", ORANGE, ORANGE_L)]
    right = [("XML", "well-formed, DTD, XSD, namespaces,\nXSLT, DOM", NAVY2, BLUE_L),
             ("Maven", "POM, dependencies, lifecycle, profiles", VIOLET, "#f1eefb"),
             ("Spring JDBC", "JdbcTemplate, DataSource,\nPOJO versus JavaBean", TEAL, TEAL_L)]
    for col, items in ((16, left), (424, right)):
        for i, (name, sub, edge, fill) in enumerate(items):
            y = 6 + i * 74
            b.append(node(col, y, 220, 62, name, sub, fill, edge, edge, 9.4, 700, 7.9))
    b.append(arrow(238, 37, 250, 122, TEAL, 1.1, hs=5.0))
    b.append(arrow(238, 111, 250, 138, RED, 1.1, hs=5.0))
    b.append(arrow(238, 185, 250, 154, ORANGE, 1.1, hs=5.0))
    b.append(arrow(422, 37, 410, 122, NAVY2, 1.1, hs=5.0))
    b.append(arrow(422, 111, 410, 138, VIOLET, 1.1, hs=5.0))
    b.append(arrow(422, 185, 410, 154, TEAL, 1.1, hs=5.0))
    return svg(660, 228, "".join(b))


def html():
    o = []
    o.append(part(18, "Last-Minute Revision",
                  "The whole unit compressed into eight pages: interfaces, methods, comparisons, mistakes and "
                  "a coverage checklist.", art_icon=18))

    o.append(fig(fig_map(),
                 "The unit on one page. Six clusters, each of which is a part of this book."))

    o.append(sec("18.1", "Interfaces and what they do"))
    o.append(tbl("The JDBC interfaces in one table",
                 ["Interface", "Role", "Created by"],
                 [["<code>Driver</code>", "Translates JDBC calls into a database protocol", "The vendor, as a class in the JAR"],
                  ["<code>DriverManager</code>", "Registers drivers and returns a Connection for a URL", "The JDK"],
                  ["<code>Connection</code>", "An open session; factory for statements; transaction control", "<code>DriverManager.getConnection()</code>"],
                  ["<code>Statement</code>", "Executes static SQL; factory for ResultSet", "<code>con.createStatement()</code>"],
                  ["<code>PreparedStatement</code>", "Precompiled, parameterized SQL", "<code>con.prepareStatement(sql)</code>"],
                  ["<code>CallableStatement</code>", "Stored procedures with IN/OUT parameters", "<code>con.prepareCall(sql)</code>"],
                  ["<code>ResultSet</code>", "Rows plus a cursor", "<code>stmt.executeQuery()</code>"],
                  ["<code>DatabaseMetaData</code>", "Describes the database", "<code>con.getMetaData()</code>"],
                  ["<code>ResultSetMetaData</code>", "Describes the columns of a result", "<code>rs.getMetaData()</code>"],
                  ["<code>DataSource</code>", "Supplies connections; can pool", "Spring configuration"]],
                 ["24%", "48%", "28%"]))

    o.append(sec("18.2", "Methods worth memorizing"))
    o.append(tbl("Methods and their purpose",
                 ["Method", "Purpose"],
                 [["<code>getConnection(url, user, pass)</code>", "Open a session (DriverManager)"],
                  ["<code>createStatement()</code>", "Plain statement"],
                  ["<code>prepareStatement(sql)</code>", "Parameterized statement"],
                  ["<code>prepareCall(sql)</code>", "Stored procedure call"],
                  ["<code>setAutoCommit(false)</code>", "Begin an explicit transaction"],
                  ["<code>commit()</code> / <code>rollback()</code>", "End it: keep or discard"],
                  ["<code>executeQuery(sql)</code>", "SELECT → ResultSet"],
                  ["<code>executeUpdate(sql)</code>", "INSERT/UPDATE/DELETE/DDL → row count"],
                  ["<code>execute(sql)</code>", "Any SQL → boolean"],
                  ["<code>addBatch()</code> / <code>executeBatch()</code>", "Many commands, one round trip"],
                  ["<code>setInt/setString/...</code>", "Bind a parameter (1-based)"],
                  ["<code>registerOutParameter()</code>", "Declare an OUT parameter before execute"],
                  ["<code>next()</code>", "Advance the cursor; false at the end"],
                  ["<code>getInt/getString/...</code>", "Read a column of the current row"],
                  ["<code>wasNull()</code>", "Distinguish NULL from zero"],
                  ["<code>close()</code>", "Release, innermost first"]],
                 ["40%", "60%"]))
    o.append(box("trick", "Memory trick",
                 "<p><b>Load → Connect → Prepare → Execute → Process → Close.</b> Six words that generate every JDBC "
                 "answer in the paper.</p>"))

    o.append(sec("18.3", "The comparisons, in one line each"))
    o.append(ul(["<b>Two-tier</b> — client talks to the database. <b>Three-tier</b> — a middle tier does, and gives "
                 "control, easier deployment and better performance.",
                 "<b>Type 1</b> bridge to ODBC, <b>Type 2</b> native API, <b>Type 3</b> middleware, <b>Type 4</b> "
                 "direct pure-Java protocol. Fewer layers = faster; fewer installs = easier.",
                 "<b>Statement</b> no parameters, compiled each time. <b>PreparedStatement</b> parameters, compiled "
                 "once, injection-safe. <b>CallableStatement</b> procedures, IN/OUT.",
                 "<b>executeQuery</b> returns rows, <b>executeUpdate</b> returns a count, <b>execute</b> returns a "
                 "boolean, <b>executeBatch</b> returns an array of counts.",
                 "<b>JDBC</b> — manual resources, checked exceptions, boilerplate. <b>Spring JDBC</b> — automatic "
                 "resources, runtime exceptions, template.",
                 "<b>DTD</b> — own syntax, no types, no namespaces. <b>XSD</b> — XML syntax, rich types, namespaces.",
                 "<b>Well-formed</b> — syntax correct. <b>Valid</b> — well-formed plus conforms to a grammar.",
                 "<b>POJO</b> — ordinary class. <b>JavaBean</b> — POJO with a no-arg constructor, private fields with "
                 "getters/setters, and Serializable.",
                 "<b>@Component</b> — class, found by scanning. <b>@Configuration</b> — class that declares "
                 "<b>@Bean</b> methods."]))

    o.append(sec("18.4", "Annotations in one table"))
    o.append(tbl("The annotations this unit requires",
                 ["Annotation", "Meaning in one line"],
                 [["<code>@SpringBootApplication</code>", "The three-in-one start-up annotation"],
                  ["<code>@SpringBootConfiguration</code>", "This class is a configuration source"],
                  ["<code>@EnableAutoConfiguration</code>", "Configure from the classpath, opinionated default"],
                  ["<code>@ComponentScan</code>", "Scan this package and below for beans"],
                  ["<code>@Configuration</code>", "Declares bean definitions in @Bean methods"],
                  ["<code>@Component</code> / <code>@Service</code> / <code>@Repository</code>", "This class is a bean"],
                  ["<code>@Autowired</code>", "Inject this dependency"],
                  ["<code>@Override</code> / <code>@Deprecated</code>", "Compiler-checked annotations"]],
                 ["42%", "58%"]))

    o.append(sec("18.5", "XML, Maven, Spring: the essentials"))
    o.append(ul(["<b>XML</b>: one root; every tag closed, nested and case-matched; attributes quoted and unique; five "
                 "reserved characters written as entities; <span class='mono'>#PCDATA</span> is parsed text, "
                 "<span class='mono'>CDATA</span> is unparsed.",
                 "<b>Namespaces</b>: <span class='mono'>xmlns:prefix=\"uri\"</span>; the URI is a name, not an "
                 "address; the declaration is inherited by descendants.",
                 "<b>XSLT</b>: source + stylesheet → processor → result; <span class='mono'>xsl:template</span>, "
                 "<span class='mono'>xsl:for-each</span>, <span class='mono'>xsl:value-of</span>.",
                 "<b>Maven</b>: POM = Project Object Model; minimal POM = modelVersion 4.0.0 + groupId + artifactId + "
                 "version; lifecycle = validate, compile, test, package, verify, install, deploy.",
                 "<b>Spring JDBC</b>: JdbcTemplate + DataSource; update/query/queryForObject/execute; RowMapper maps "
                 "one row."]))

    o.append(sec("18.6", "Ten mistakes that cost marks"))
    o.append(ol(["Writing “well-formed document is valid” — the implication is one-way.",
                 "Confusing <span class='mono'>executeQuery()</span> with "
                 "<span class='mono'>executeUpdate()</span> in an example.",
                 "Forgetting that parameter indexes start at <b>1</b>.",
                 "Claiming a <span class='mono'>PreparedStatement</span> is only about performance, and omitting the "
                 "security reason.",
                 "Calling <span class='mono'>registerOutParameter()</span> after "
                 "<span class='mono'>execute()</span>.",
                 "Listing Connection, Statement and ResultSet as the four JDBC <i>components</i>.",
                 "Saying Type 1 is the recommended driver for the web.",
                 "Writing that <span class='mono'>pom.xml</span> is optional, or that the modelVersion is 1.0.",
                 "Defining a JavaBean as “a POJO” without the three conventions.",
                 "Forgetting to close resources, or closing them in the wrong order."]))

    o.append(sec("18.7", "Twenty facts for a viva"))
    o.append(ol(["JDBC = Java Database Connectivity, part of the JDK since 1.1.",
                 "The API lives in <span class='mono'>java.sql</span> (client) and "
                 "<span class='mono'>javax.sql</span> (server).",
                 "Two layers: JDBC API and JDBC Driver API.",
                 "Four components: API, Driver Manager, Test Suite, JDBC-ODBC Bridge.",
                 "Four driver types; Type 4 is fastest, Type 3 needs middleware.",
                 "<span class='mono'>Class.forName()</span> throws "
                 "<span class='mono'>ClassNotFoundException</span>.",
                 "<span class='mono'>getConnection()</span> throws "
                 "<span class='mono'>SQLException</span>.",
                 "Auto-commit defaults to true.",
                 "The ResultSet cursor starts before the first row.",
                 "Column indexes are 1-based; <span class='mono'>wasNull()</span> detects NULL.",
                 "Statement → PreparedStatement → CallableStatement is the hierarchy.",
                 "Prepared statements are precompiled: performance and security.",
                 "Spring JDBC wraps JDBC; it does not replace it.",
                 "JdbcTemplate needs a DataSource through its <span class='mono'>dataSource</span> property.",
                 "DriverManagerDataSource does not pool connections.",
                 "@SpringBootApplication = Configuration + AutoConfiguration + ComponentScan.",
                 "Annotations are metadata; retention decides compile-time versus run-time visibility.",
                 "XSD is itself XML, which is why it supports types and namespaces.",
                 "Maven's POM inherits from the Super POM.",
                 "A JavaBean is a POJO plus three conventions."]))

    o.append(sec("18.8", "Five minutes before the exam"))
    o.append(p("Close the book and run this list. Each line is a place where marks are lost, not a topic to learn "
               "again."))
    o.append(ol(["Can I draw the two-layer architecture and place DriverManager between the application and the "
                 "driver?",
                 "Can I list the seven steps and name the class or method for each one?",
                 "Can I state the four driver types in order with one disadvantage each?",
                 "Can I write the three statement interfaces in their hierarchy and give one use for each?",
                 "Can I show a vulnerable query, the attack string, and the parameterized replacement in three lines?",
                 "Can I name the four advantages of JDBC and the one real disadvantage?",
                 "Can I expand <span class='mono'>@SpringBootApplication</span> into its three annotations?",
                 "Can I write a valid DTD and a valid XSD fragment for the same three-element document?",
                 "Can I write a minimal pom.xml from memory, including the model version?",
                 "Can I explain why <span class='mono'>DriverManagerDataSource</span> is not used in production?"]))
    o.append(box("tip", "Exam tip",
                 "<p>If a question asks for “the architecture” and you have three minutes, draw the general "
                 "architecture, label the two layers, and add the call path as a numbered sequence inside it. That "
                 "single diagram answers two-tier, three-tier and component questions at once.</p>"))
    o.append(sec("18.9", "Syllabus coverage checklist"))
    o.append(p("Every topic named in the syllabus outline and in the lecture slides, mapped to the section where it "
               "is taught. Use this table as the final revision checklist: tick a row only when you can explain it "
               "without looking."))
    rows = [
        ["JDBC and why it exists", "1.1 – 1.4"],
        ["JDBC versus ODBC, the N × M problem", "1.5"],
        ["Architecture of JDBC: two layers", "2.1"],
        ["Two-tier and three-tier architecture", "2.2 – 2.3"],
        ["The complete call path", "2.4"],
        ["JDBC components", "2.5"],
        ["DriverManager and the Driver interface", "2.6 – 2.7"],
        ["Establishing connectivity: seven steps", "3.8"],
        ["JDBC URL anatomy, driver class names", "3.9"],
        ["Class.forName, classpath and JAR", "3.10 – 3.11"],
        ["Connection lifecycle (sequence diagram)", "3.12"],
        ["JDBC driver types 1–4 and comparison", "3.2 – 3.7"],
        ["Connection interface and its methods", "4.1 – 4.3"],
        ["Transactions: auto-commit, commit, rollback", "4.4"],
        ["Metadata, closing, try-with-resources", "4.5 – 4.6"],
        ["Statement interface and methods", "5.2"],
        ["PreparedStatement and parameterized queries", "5.3"],
        ["CallableStatement and stored procedures", "5.4"],
        ["Procedures versus functions", "5.5"],
        ["Statement / PreparedStatement / CallableStatement comparison", "5.6"],
        ["executeQuery, executeUpdate, execute, executeBatch", "6.1 – 6.2"],
        ["ResultSet, cursor, next() and navigation", "6.4 – 6.5"],
        ["Reading columns, getXXX, wasNull", "6.6"],
        ["ResultSet types and concurrency", "6.7"],
        ["CRUD examples with output", "6.8"],
        ["Problems of the JDBC API", "7.1"],
        ["SQL injection and parameterized defence", "7.2 – 7.3"],
        ["Advantages of JDBC (four points)", "7.5"],
        ["Disadvantages: connection cost, SQL portability", "7.6"],
        ["Java annotation fundamentals and key points", "8.1 – 8.2"],
        ["Five categories of annotations", "8.3"],
        ["Built-in annotations", "8.4"],
        ["@SpringBootApplication and its three parts", "8.5"],
        ["Start-up sequence and dependency injection", "8.6"],
        ["JDBC versus Spring JDBC (six points)", "9.3"],
        ["Spring JDBC stack and responsibilities", "9.2, 9.4"],
        ["XML: definition, characteristics, uses", "10.1"],
        ["XML versus HTML", "10.2"],
        ["XML syntax, elements, attributes, entities", "10.3"],
        ["XML tree (bookstore example)", "10.4"],
        ["Well-formed versus valid", "10.5"],
        ["DTD: internal and external", "10.6"],
        ["XML Schema (XSD) with types and namespaces", "10.7"],
        ["DTD versus XSD comparison", "10.7"],
        ["XML namespaces, prefixes, scope, defaults", "11.1 – 11.2"],
        ["XSL / XSLT transformation", "11.3"],
        ["XML DOM: nodes, properties, methods", "11.4"],
        ["DOM parsing in JavaScript and Java", "11.5"],
        ["Maven: definition and nine capabilities", "12.1"],
        ["POM, Super POM, minimal POM", "12.2"],
        ["pom.xml sections, dependencies, repositories", "12.3"],
        ["Build, plugins, pluginManagement, reporting, profiles", "12.3"],
        ["A complete Spring Boot pom.xml", "12.4"],
        ["Build lifecycle and standard layout", "12.5"],
        ["JdbcTemplate: definition, declaration, two steps", "13.1 – 13.2"],
        ["JdbcTemplate methods and RowMapper", "13.3 – 13.5"],
        ["DataSource and DriverManagerDataSource", "14.1 – 14.2"],
        ["Java and XML configuration, pooling", "14.3 – 14.5"],
        ["POJO definition and example", "15.1"],
        ["JavaBean conventions and comparison", "15.2 – 15.3"],
        ["Complete practical programs", "16.1 – 16.8"],
        ["Examination preparation", "17.1 – 17.7"],
    ]
    o.append(tbl("Coverage map: syllabus topic → where it is taught",
                 ["Topic from the syllabus or lecture material", "Section"],
                 rows, ["76%", "24%"], cls="compact", firstcol=False))
    o.append(box("imp", "Final note",
                 "<p>Every row of this table. If each one can be explained in two or three sentences, with the diagram "
                 "it drawn from memory, the unit is finished. The diagrams to be able to reproduce are: the two-layer "
                 "architecture, the call path, the seven steps, the statement hierarchy, the cursor, the injection "
                 "comparison, the Spring stack, the XML tree, the namespace declaration and the POM sections.</p>"
                 "<p class='small'><b>End of Unit 3</b> — GUI and Database Connectivity · 25CSH-208 · "
                 "Chandigarh University, B.E. CSE Semester 3.</p>"))

    return "".join(o)
