"""PART 14 — DataSource and DriverManagerDataSource."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_datasource():
    b = []
    b.append(txt(12, 18, "ONE INTERFACE, FOUR IMPLEMENTATIONS", 8.4, MUTED, 700, ls="0.1em"))
    b.append(rect(12, 32, 168, 132, "#fbfcfd", NAVY, 2))
    b.append(txt(24, 52, "javax.sql.DataSource", 8.2, NAVY, 700, "start"))
    b.append(txt(24, 66, "interface", 7.2, MUTED, 600))
    b.append(txt(24, 88, "getConnection()", 7.6, TEAL, 600, "start", MONO))
    b.append(txt(24, 102, "getConnection(u, p)", 7.6, TEAL, 600, "start", MONO))
    b.append(txtw(24, 122, "An object that knows how to make connections; nothing else in the application does.",
                  148, 7.0, MUTED, 400, "start")[0])

    impls = [("DriverManagerDataSource", "a new connection every time — no pooling", ORANGE_L, ORANGE),
             ("HikariDataSource", "a pool of ready connections (Boot's default)", TEAL_L, TEAL),
             ("BasicDataSource (DBCP)", "an Apache Commons connection pool", WHITE, NAVY3),
             ("SingleConnectionDataSource", "one shared connection, meant for tests", WHITE, NAVY3)]
    b.append(line(188, 48, 202, 48, LINE, 1.0))
    b.append(line(202, 48, 202, 178, LINE, 1.0))
    for i, (t, s_, fill, col) in enumerate(impls):
        x = 212 + (i % 2) * 222
        y = 32 + (i // 2) * 66
        b.append(arrow(202, y + 24, x - 2, y + 24, col, 1.0, hs=4.6))
        b.append(node(x, y, 210, 48, t, s_, fill, col, col, 8.0, 700, 6.8))

    b.append(rect(12, 186, 636, 66, GREY, LINE, 2))
    b.append(txt(24, 204, "Why an interface and not DriverManager?", 7.8, NAVY, 700))
    b.append(txtw(24, 220, "DriverManager is a static utility: every call opens a fresh connection and you cannot "
                           "substitute a pooled or test implementation. A DataSource is an object, so it can be "
                           "configured, injected, wrapped and replaced — Spring depends on the interface, never on "
                           "DriverManager.", 612, 7.4, MUTED, 400, "start")[0])
    b.append(txt(330, 272, "The application code is identical for all four: only the configuration changes.",
                 7.8, MUTED, 400, "middle"))
    return svg(660, 282, "".join(b))


def fig_wiring():
    b = []
    b.append(txt(12, 18, "HOW THE THREE OBJECTS ARE WIRED", 8.4, MUTED, 700, ls="0.1em"))
    b.append(node(12, 44, 150, 66, "application.properties", "url, username, password, driver", NAVY, NAVY, WHITE, 8.2, 700, 7.0, "#d5e2ee"))
    b.append(node(200, 44, 150, 66, "DriverManagerDataSource", "holds the four properties", ORANGE_L, ORANGE, ORANGE, 8.0, 700, 6.8))
    b.append(node(388, 44, 140, 66, "JdbcTemplate", "datasource property", TEAL_L, TEAL, TEAL, 8.4, 700, 7.0))
    b.append(node(566, 44, 82, 66, "StudentDao", "one field", WHITE, NAVY3, NAVY3, 8.2, 700))
    b.append(arrow(164, 77, 198, 77, NAVY3, 1.2, hs=5.4))
    b.append(arrow(352, 77, 386, 77, ORANGE, 1.2, hs=5.4))
    b.append(arrow(530, 77, 564, 77, TEAL, 1.2, hs=5.4))
    b.append(rect(12, 126, 636, 40, GREY, LINE, 2))
    b.append(txt(24, 143, "DriverManagerDataSource  →  used as the value of  jdbcTemplate.setDataSource(...)  →  ", 7.6, INK, 400, "start", MONO))
    b.append(txt(24, 157, "which the DAO receives through its constructor. Nothing constructs a Connection directly.", 7.6, MUTED, 400))
    b.append(rect(12, 178, 636, 54, "#fbfcfd", LINE, 2))
    b.append(txt(24, 196, "The equivalent XML (the lecture's bean declaration)", 7.8, NAVY, 700))
    b.append(txt(24, 212, "<bean id=\"dataSource\" class=\"org.springframework.jdbc.datasource.DriverManagerDataSource\">", 7.0, INK, 400, "start", MONO))
    b.append(txt(24, 224, "  <property name=\"url\" value=\"jdbc:mysql://localhost:3306/testdb\" /> ...", 7.0, INK, 400, "start", MONO))
    return svg(660, 240, "".join(b))


def fig_nopooling():
    b = []
    b.append(txt(12, 18, "WHY POOLING MATTERS", 8.4, MUTED, 700, ls="0.1em"))
    # without pooling
    b.append(rect(12, 30, 300, 120, RED_L, RED, 2))
    b.append(txt(24, 48, "DriverManagerDataSource", 8.0, RED, 700))
    for i in range(4):
        y = 62 + i * 20
        b.append(txt(24, y, "request", 7.0, MUTED, 400))
        b.append(rect(70, y - 9, 60, 12, WHITE, RED, 1))
        b.append(txt(100, y, "connect", 6.4, RED, 400, "middle"))
        b.append(arrow(132, y - 3, 152, y - 3, RED, 0.9, hs=4.0))
        b.append(txt(156, y, "handshake + auth", 6.6, MUTED, 400))
    b.append(txt(24, 144, "four requests = four full connections", 7.4, RED, 600))
    # with pooling
    b.append(rect(348, 30, 300, 120, TEAL_L, TEAL, 2))
    b.append(txt(360, 48, "HikariCP pool", 8.0, TEAL, 700))
    for i in range(4):
        y = 62 + i * 20
        b.append(txt(360, y, "request", 7.0, MUTED, 400))
        b.append(rect(406, y - 9, 60, 12, WHITE, TEAL, 1))
        b.append(txt(436, y, "borrow", 6.4, TEAL, 400, "middle"))
        b.append(txt(474, y, "already open", 6.6, TEAL, 400))
    b.append(txt(360, 144, "four requests = zero new handshakes", 7.4, TEAL, 600))
    b.append(txt(330, 168, "A handshake and an authentication round trip cost milliseconds; a page that runs twenty "
                           "queries pays it twenty times.", 7.6, MUTED, 400, "middle"))
    return svg(660, 178, "".join(b))


def html():
    o = []
    o.append(part(14, "DataSource and DriverManagerDataSource",
                  "The object that supplies connections — Spring's answer to DriverManager, and the "
                  "simplest implementation of it.", art_icon=14))

    o.append(sec("14.1", "DataSource: the connection supplier"))
    o.append(p("A <span class='mono'>DataSource</span> — from <span class='mono'>javax.sql</span> — is an object whose "
               "only job is to supply <span class='mono'>Connection</span> objects. Your code asks the DataSource for "
               "a connection; it does not know, and does not care, whether that connection is brand new, borrowed "
               "from a pool, or a test double."))
    o.append(box("def", "Definition",
                 "<p>A <b>DataSource</b> is a factory for connections to the physical data source that it represents. "
                 "It is the preferred alternative to <span class='mono'>DriverManager</span>, because it is an object "
                 "that can be configured, pooled, injected and replaced without changing application code.</p>"))
    o.append(fig(fig_datasource(),
                 "One interface, many implementations. Spring code depends on the interface, so switching from the "
                 "simplest implementation to a production pool is a configuration change, not a code change."))
    o.append(box("imp", "Important",
                 "<p>The lecture material describes Spring's simplest route: “Spring provides many ways to establish "
                 "a connection to a database — retrieval of records, insertion, updating, deletion. The most basic of "
                 "them is using <b>DriverManagerDataSource</b>.” Everything in this part is that basic route.</p>"))

    o.append(sec("14.2", "DriverManagerDataSource"))
    o.append(p("<span class='mono'>DriverManagerDataSource</span> is Spring's simplest "
               "<span class='mono'>DataSource</span> implementation. It contains the information about the database — "
               "driver class name, connection URL, username and password — and returns a new "
               "<span class='mono'>Connection</span> from "
               "<span class='mono'>DriverManager.getConnection()</span> on every call. In other words, it is a thin "
               "object wrapper around the plain JDBC call of Part 3."))
    o.append(p("There is a property named <span class='mono'>datasource</span> in the "
               "<span class='mono'>JdbcTemplate</span> class. To make the template work, you provide the reference of "
               "a <span class='mono'>DriverManagerDataSource</span> object for that property — which is exactly the "
               "\"wiring\" that the next figure shows."))
    o.append(tbl("The four properties of DriverManagerDataSource",
                 ["Property", "Setter", "Example value"],
                 [["Driver class name", "<code>setDriverClassName(String)</code>", "<code>com.mysql.cj.jdbc.Driver</code>"],
                  ["URL", "<code>setUrl(String)</code>", "<code>jdbc:mysql://localhost:3306/testdb</code>"],
                  ["Username", "<code>setUsername(String)</code>", "<code>root</code>"],
                  ["Password", "<code>setPassword(String)</code>", "<code>password</code>"]],
                 ["26%", "38%", "36%"]))
    o.append(fig(fig_wiring(),
                 "How the four objects are wired: properties → DataSource → JdbcTemplate → DAO. The DAO never sees "
                 "a URL, a password or a DriverManager call."))

    o.append(sec("14.3", "Configuring it in Java"))
    o.append(code('''import org.springframework.jdbc.datasource.DriverManagerDataSource;
import javax.sql.DataSource;

public class DataSourceExample {
    public static void main(String[] args) {
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl("jdbc:mysql://localhost:3306/testdb");
        dataSource.setUsername("root");
        dataSource.setPassword("password");
        System.out.println("DataSource configured successfully!");
    }
}''', "java", "Configuring DriverManagerDataSource programmatically — the lecture's example"))
    o.append(p("Declaring the variable as <span class='mono'>DataSource</span> rather than "
               "<span class='mono'>DriverManagerDataSource</span> is not pedantry: it is the habit that makes the "
               "next section's advice possible. When the day comes to pool connections, only the construction line "
               "changes."))

    o.append(sec("14.4", "Configuring it in XML"))
    o.append(p("In a classic Spring application the same three values are supplied as properties of a bean "
               "declaration in an XML file. This is the form the lecture material shows, and it still appears in "
               "older projects and in examination questions."))
    o.append(code('''<bean id="dataSource"
      class="org.springframework.jdbc.datasource.DriverManagerDataSource">
    <property name="driverClassName" value="com.mysql.cj.jdbc.Driver" />
    <property name="url"             value="jdbc:mysql://localhost:3306/testdb" />
    <property name="username"        value="root" />
    <property name="password"        value="password" />
</bean>

<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
    <property name="dataSource" ref="dataSource" />
</bean>''', "xml", "The bean declaration, plus the JdbcTemplate that consumes it"))
    o.append(p("The second bean is the part students forget. A <span class='mono'>DriverManagerDataSource</span> "
               "on its own does nothing: it must be <b>injected</b> into the template through the "
               "<span class='mono'>dataSource</span> property, and the template in turn is injected into the DAO. "
               "That chain of references is what \"wiring\" means."))
    o.append(box("mistake", "Common mistake",
                 "<p>Hard-coding credentials in a bean definition and committing the file. The XML example above uses "
                 "<span class='mono'>password</span> as a placeholder; in real projects these values come from "
                 "environment variables or <span class='mono'>application.properties</span>, and the password is "
                 "never in version control.</p>"))

    o.append(sec("14.5", "What it does not do: pooling"))
    o.append(p("<span class='mono'>DriverManagerDataSource</span> does <b>not</b> pool connections. Every call to "
               "<span class='mono'>getConnection()</span> opens a new physical connection and every "
               "<span class='mono'>close()</span> destroys it. That makes it unsuitable for production environments "
               "with high concurrency, and perfectly suitable for testing and for lightweight applications where "
               "connection pooling is unnecessary."))
    o.append(fig(fig_nopooling(),
                 "Four requests, two behaviours. Without a pool each request pays for a TCP handshake and an "
                 "authentication; with a pool the connections are already open and are merely borrowed and returned."))
    o.append(tbl("Key points to consider, from the lecture material",
                 ["Point", "Detail"],
                 [["<b>No connection pooling</b>", "The class does not pool connections, which makes it unsuitable "
                                                   "for production environments with high concurrency."],
                  ["<b>Use cases</b>", "Ideal for testing or for lightweight applications where connection pooling "
                                       "is unnecessary."],
                  ["<b>Alternatives</b>", "For production, consider connection pool implementations such as "
                                          "<b>HikariCP</b> or <b>Apache DBCP</b>."]],
                 ["24%", "76%"], firstcol=False))
    o.append(code('''# Spring Boot: the production form of the same four properties
spring.datasource.url=jdbc:mysql://localhost:3306/testdb
spring.datasource.username=root
spring.datasource.password=${DB_PASSWORD}
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver''', "properties",
                 "application.properties — the modern equivalent of the XML bean"))
    o.append(p("Spring Boot reads those four lines, builds a <b>HikariCP</b> DataSource by default (because it is on "
               "the classpath through <span class='mono'>spring-boot-starter-jdbc</span>), and injects it wherever a "
               "<span class='mono'>DataSource</span> is required. The code you write is identical to the code above; "
               "only the implementation object differs."))

    o.append(sec("14.6", "Summary"))
    o.append(ul(["A DataSource supplies Connection objects; it is the preferred alternative to DriverManager.",
                 "DriverManagerDataSource holds driver class, URL, username and password and returns a new connection "
                 "each time.",
                 "It is injected into JdbcTemplate through the <span class='mono'>dataSource</span> property.",
                 "It does not pool: fine for tests and small tools, wrong for production.",
                 "HikariCP and Apache DBCP are the production alternatives, and Spring Boot picks HikariCP by default."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> List the four properties of DriverManagerDataSource. "
                 "<b>2.</b> Why is it unsuitable for production? "
                 "<b>3.</b> Which property of JdbcTemplate must be set?</p>"
                 "<p class='small'><i>Answers:</i> (1) driverClassName, url, username, password. (2) It does not pool "
                 "connections, so every operation pays the full cost of opening one. (3) "
                 "<span class='mono'>dataSource</span>.</p>"))
    o.append(recap("Part 14 recap", [
        ["<b>DataSource</b>", "A factory of <span class='mono'>Connection</span> objects — the JDBC-standard way to supply connections."],
        ["<b>DriverManagerDataSource</b>", "A simple Spring DataSource holding driver class, URL, user and password."],
        ["<b>What it does not do</b>", "It does not pool: every <span class='mono'>getConnection()</span> opens a new physical connection."],
        ["<b>Production choice</b>", "HikariCP (Spring Boot default) or DBCP2 behind the same <span class='mono'>DataSource</span> interface."],
        ["<b>Wiring</b>", "Declare it as a bean, then set it on <span class='mono'>JdbcTemplate</span> with <span class='mono'>setDataSource()</span>."],
    ], terms=["DataSource", "DriverManagerDataSource", "pooled DataSource", "connection pool", "@Bean", "property injection", "HikariCP", "setUrl/setUsername", "production DataSource"], practice=[
        "What is a DataSource responsible for, in one sentence?",
        "Give the two limitations of <span class='mono'>DriverManagerDataSource</span>.",
        "Which pool does Spring Boot use by default?",
    ], trap="Calling <span class='mono'>DriverManagerDataSource</span> a pool. It opens a new physical connection per call."))
    return "".join(o)
