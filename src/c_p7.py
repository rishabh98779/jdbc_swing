"""PART 7 — Problems, Limitations and Security of JDBC."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_injection():
    b = []
    b.append(txt(12, 16, "HOW SQL INJECTION WORKS", 8.4, MUTED, 700, ls="0.1em"))
    # step 1: form
    b.append(rect(12, 30, 200, 132, "#fbfcfd", LINE, 2))
    b.append(txt(112, 48, "Log-in form", 8.6, NAVY, 700, "middle"))
    b.append(rect(24, 58, 176, 24, WHITE, LINE, 2))
    b.append(txt(32, 74, "user:  ' OR '1'='1", 7.8, RED, 600, "start", MONO))
    b.append(rect(24, 88, 176, 24, WHITE, LINE, 2))
    b.append(txt(32, 104, "pass:  anything", 7.8, MUTED, 600, "start", MONO))
    b.append(txt(24, 128, "The attacker does not need a", 7.2, MUTED, 400))
    b.append(txt(24, 140, "password - only a quote mark.", 7.2, MUTED, 400))

    b.append(arrow(216, 96, 244, 96, RED, 1.5, hs=6.4))

    # step 2: concatenated SQL
    b.append(rect(246, 30, 402, 132, RED_L, RED, 2))
    b.append(txt(258, 48, "String concatenation in Java", 8.6, RED, 700))
    b.append(txt(258, 68, "SELECT * FROM users", 8.0, INK, 400, "start", MONO))
    b.append(txt(258, 82, "WHERE username = '' OR '1'='1'", 8.0, RED, 700, "start", MONO))
    b.append(txt(258, 96, "AND password = 'anything'", 8.0, INK, 400, "start", MONO))
    b.append(txt(258, 118, "The condition is always true, so the query", 7.4, RED, 600))
    b.append(txt(258, 130, "returns every row of the users table.", 7.4, RED, 600))
    b.append(txt(258, 150, "Authentication is bypassed.", 8.0, RED, 700))

    b.append(arrow(330, 166, 330, 190, RED, 1.5, hs=6.4))
    b.append(rect(198, 192, 264, 34, RED, RED, 2))
    b.append(txt(330, 214, "login succeeds as the first user in the table", 8.2, WHITE, 700, "middle"))
    return svg(660, 236, "".join(b))


def fig_parameterized():
    b = []
    b.append(txt(12, 16, "WHY PARAMETERS STOP THE ATTACK", 8.4, MUTED, 700, ls="0.1em"))
    # left: statement
    b.append(rect(12, 28, 314, 190, "#fbfcfd", RED, 2))
    b.append(txt(24, 46, "String concatenation", 8.6, RED, 700))
    b.append(txt(24, 62, "\"SELECT * FROM users WHERE username='\"", 7.6, INK, 400, "start", MONO))
    b.append(txt(24, 74, "  + user + \"' AND password='\" + pass + \"'\"", 7.6, INK, 400, "start", MONO))
    b.append(rect(24, 86, 290, 44, WHITE, RED, 2))
    b.append(txt(30, 102, "SQL sent to the DBMS:", 7.2, MUTED, 600))
    b.append(txt(30, 118, "... username='' OR '1'='1' ...", 7.6, RED, 700, "start", MONO))
    b.append(txt(24, 148, "input and code are mixed in one string,", 7.6, RED, 600))
    b.append(txt(24, 160, "so the database parses the input as code.", 7.6, RED, 600))
    b.append(txt(24, 182, "Every value must be escaped by hand -", 7.4, MUTED, 400))
    b.append(txt(24, 194, "and hand-made escaping is never complete.", 7.4, MUTED, 400))

    # right: prepared
    b.append(rect(340, 28, 308, 190, "#fbfcfd", TEAL, 2))
    b.append(txt(352, 46, "Parameterized query", 8.6, TEAL, 700))
    b.append(txt(352, 62, "\"SELECT * FROM users WHERE username=?\"", 7.6, INK, 400, "start", MONO))
    b.append(txt(352, 74, "  + \" AND password=?\"", 7.6, INK, 400, "start", MONO))
    b.append(rect(352, 86, 284, 44, WHITE, TEAL, 2))
    b.append(txt(358, 102, "SQL sent to the DBMS (structure fixed first):", 7.2, MUTED, 600))
    b.append(txt(358, 118, "... username=? AND password=? ...", 7.6, TEAL, 700, "start", MONO))
    b.append(rect(352, 136, 284, 26, TEAL_L, TEAL, 2))
    b.append(txt(360, 153, "then bound: 1 = \"' OR '1'='1\"  (a value, not code)", 7.4, TEAL, 600, "start"))
    b.append(txt(352, 180, "The plan is compiled before the values are seen,", 7.6, TEAL, 600))
    b.append(txt(352, 192, "so no value can ever change the query shape.", 7.6, TEAL, 600))
    return svg(660, 226, "".join(b))


def fig_boilerplate():
    b = []
    b.append(txt(12, 16, "THE SAME OPERATION, COUNTED", 8.4, MUTED, 700, ls="0.1em"))
    # left: plain jdbc
    b.append(rect(12, 28, 300, 152, "#fbfcfd", RED, 2))
    b.append(txt(24, 46, "Plain JDBC", 8.8, RED, 700))
    steps = ["load driver", "open connection", "create statement", "set parameters",
             "execute", "read ResultSet", "handle SQLException", "close rs / stmt / con"]
    for i, s in enumerate(steps):
        b.append(txt(28, 64 + i * 14, "·", 8, RED, 700))
        b.append(txt(38, 64 + i * 14, s, 7.6, INK, 400))
    b.append(txt(240, 176, "8 concerns", 7.8, RED, 700, "end"))
    # right: spring
    b.append(rect(348, 28, 300, 152, "#fbfcfd", TEAL, 2))
    b.append(txt(360, 46, "Spring JdbcTemplate", 8.8, TEAL, 700))
    steps2 = ["inject DataSource", "call one template method", "map the row (RowMapper)",
              "handle DataAccessException", "no explicit close"]
    for i, s in enumerate(steps2):
        b.append(txt(364, 64 + i * 16, "·", 8, TEAL, 700))
        b.append(txt(374, 64 + i * 16, s, 7.6, INK, 400))
    b.append(txt(636, 176, "3 concerns", 7.8, TEAL, 700, "end"))
    b.append(txt(330, 196, "Same SQL. The difference is who writes the plumbing.", 7.8, MUTED, 400, "middle"))
    return svg(660, 206, "".join(b))


def html():
    o = []
    o.append(part(7, "Problems, Limitations and Security of JDBC",
                  "What plain JDBC makes you write by hand, and the one flaw that turns a login form into "
                  "an open door.", art_icon=7))

    o.append(sec("7.1", "Six problems of the plain JDBC API"))
    o.append(p("JDBC is a low-level API. It does what a low-level API should do — give you complete control — and it "
               "makes you pay for that control in repeated code. The lecture material lists four problems under "
               "“Problems of JDBC API”; two more follow from them."))
    o.append(ol(["<b>A lot of code before and after the query.</b> Creating the connection, creating the statement, "
                 "closing the ResultSet, closing the connection — every time.",
                 "<b>Exception handling on the database logic.</b> Each call throws "
                 "<span class='mono'>SQLException</span>, so every method needs its own try/catch and its own "
                 "recovery decision.",
                 "<b>Transaction handling by hand.</b> Switching auto-commit off, committing, rolling back and "
                 "restoring the previous mode is repeated in every business method.",
                 "<b>Repetition from one database logic to another.</b> The same twenty lines appear in every DAO "
                 "method, which is time-consuming and error-prone.",
                 "<b>Vendor-specific SQL and error codes.</b> Error handling that inspects vendor codes ties your "
                 "code to one database.",
                 "<b>Connection cost.</b> A connection is expensive to create; naive code creates one per request."]))
    o.append(fig(fig_boilerplate(),
                 "The same operation, counted. The right-hand column is what Parts 9 and 13 are about; the left-hand "
                 "column is what you are asked to write by hand in Part 16."))
    o.append(box("imp", "Important",
                 "<p>These are problems of <b>plain JDBC as used directly</b>, not defects of the JDBC API. JDBC is "
                 "designed to be the layer underneath a helper — which is exactly how Spring JDBC, Hibernate and "
                 "every ORM use it.</p>"))

    o.append(sec("7.2", "SQL injection"))
    o.append(p("SQL injection is the security consequence of building SQL by concatenation. If user input becomes "
               "part of the SQL text, the user can supply SQL syntax instead of data — and the database has no way "
               "to know it was not invited."))
    o.append(p("The lecture material uses the textbook example: a login query built from two strings."))
    o.append(code('''String query = "SELECT * FROM users WHERE username='" + user + "' AND password='" + pass + "'";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);''', "java", "The vulnerable pattern — do not copy this into a project"))
    o.append(p("If the user types <span class='mono'>' OR '1'='1</span> into the username field, the string becomes:"))
    o.append(raw_code('''SELECT * FROM users WHERE username='' OR '1'='1' AND password='anything\'''',
                       "The query the database actually receives"))
    o.append(p("The condition <span class='mono'>'1'='1'</span> is always true, so the WHERE clause matches every "
               "row. Authentication is bypassed, and the application has just handed out the first account in the "
               "table — very often the administrator."))
    o.append(fig(fig_injection(),
                 "The anatomy of the attack: input becomes syntax, the WHERE clause becomes always-true, and the "
                 "login succeeds without a password."))
    o.append(box("mistake", "Common mistake",
                 "<p>Believing that “no quotes in the input” is a defence. Injection also works without quotes, "
                 "through numeric contexts, <span class='mono'>UNION SELECT</span>, and comment characters "
                 "(<span class='mono'>--</span>). Escaping by hand is a losing game; parameter binding is the "
                 "correct fix.</p>"))

    o.append(sec("7.3", "The fix: parameterized queries"))
    o.append(p("A <span class='mono'>PreparedStatement</span> sends the SQL <b>structure first</b> and the values "
               "afterwards. The database compiles the statement while the "
               "<span class='mono'>?</span> placeholders are still empty, so by the time the values arrive the query "
               "shape is already fixed. A value can therefore never become syntax."))
    o.append(code('''String query = "SELECT * FROM users WHERE username=? AND password=?";
PreparedStatement pstmt = conn.prepareStatement(query);
pstmt.setString(1, user);
pstmt.setString(2, pass);
ResultSet rs = pstmt.executeQuery();''', "java", "The safe pattern — structure first, values second"))
    o.append(fig(fig_parameterized(),
                 "Why binding defeats injection. On the left, input is parsed as code; on the right, the plan is "
                 "compiled before the input is seen, so the input can only ever be a value."))
    o.append(box("trick", "Memory trick",
                 "<p><b>Instructions are code; data is data.</b> A PreparedStatement keeps them in separate "
                 "channels — the SQL goes through the compiler, the values go through the binder. Never let the two "
                 "meet in a string.</p>"))
    o.append(p("Note the two side benefits, because they are often worth more marks than the security argument: the "
               "query is compiled once and reused (performance), and the setter performs type checking "
               "(<span class='mono'>setInt</span> cannot be given a string), so invalid data is rejected before it "
               "reaches the database."))

    o.append(sec("7.4", "Other limitations worth knowing"))
    o.append(tbl("Practical limitations of plain JDBC",
                 ["Limitation", "Consequence", "Usual remedy"],
                 [["No connection pooling in DriverManager", "Every getConnection() opens a new session", "Use a DataSource with HikariCP or DBCP"],
                  ["Checked exceptions everywhere", "Business code fills with try/catch", "Spring's DataAccessException hierarchy"],
                  ["Manual resource management", "Leaked connections and cursors", "try-with-resources, or JdbcTemplate"],
                  ["No object mapping", "Rows must be copied into objects by hand", "RowMapper, or an ORM"],
                  ["Vendor-specific SQL", "Code is not portable between databases", "Standard SQL, or a dialect layer"],
                  ["Manual transaction propagation", "Nested calls do not share a transaction", "A transaction manager"]],
                 ["30%", "37%", "33%"]))

    o.append(sec("7.5", "Advantages of JDBC"))
    o.append(p("The lecture material gives four advantages, and they are the standard answer to “why is JDBC still "
               "used?” even in a Spring project."))
    o.append(tbl("The four advantages, in the lecture's words",
                 ["Advantage", "Explanation"],
                 [["<b>Provides existing enterprise data</b>",
                   "Businesses can continue to use their installed databases and access information even if it is "
                   "stored on different database management systems."],
                  ["<b>Simplified enterprise development</b>",
                   "The combination of the Java API and the JDBC API makes application development easy and "
                   "cost-effective."],
                  ["<b>Zero configuration for network computers</b>",
                   "No configuration is required on the client side, which centralizes software maintenance. Because "
                   "the driver is written in Java, everything needed to make a connection is defined by the JDBC URL "
                   "or by a DataSource object registered with a JNDI naming service."],
                  ["<b>Full access to metadata</b>",
                   "The capabilities of a specific database connection can be discovered at run time; the JDBC API "
                   "provides metadata access that enables sophisticated, generic applications."]],
                 ["34%", "66%"], firstcol=False))
    o.append(p("There is also a short list of “why use JDBC” points that appears in the lecture material and makes a "
               "good five-mark answer on its own:"))
    o.append(ul(["Ease of programming — you write Java, not a mixture of languages.",
                 "You can write Java instead of embedding SQL strings inside another language's runtime.",
                 "Performance improvement through prepared statements and batching.",
                 "Ability to roll back to a savepoint.",
                 "Support for batch updates.",
                 "Many optional packages built on top of the API."]))

    o.append(sec("7.6", "Disadvantages of JDBC"))
    o.append(p("The disadvantage that the lecture material emphasizes is <b>connection cost</b>. Creating a "
               "connection is always an expensive, time-consuming operation, and that cost is multiplied in "
               "environments where a large number of users access the database in short, unconnected operations. "
               "Creating connections over and over in such environments is simply too expensive, and repeatedly "
               "creating and closing connections affects performance."))
    o.append(p("A second, subtler disadvantage is portability of <i>SQL</i>. JDBC makes the <i>API</i> portable, but "
               "not the SQL dialect: <span class='mono'>LIMIT</span>, <span class='mono'>ROWNUM</span>, date "
               "functions and sequences differ between MySQL and Oracle, so a query written for one may fail on the "
               "other. The API travels; the SQL may not."))
    o.append(box("tip", "Exam tip",
                 "<p>A question such as “Discuss the advantages and disadvantages of JDBC” wants the four advantages "
                 "by name, then the connection-cost disadvantage, then one sentence of conclusion: the disadvantages "
                 "are what connection pooling and Spring JDBC were invented to fix.</p>"))

    o.append(sec("7.7", "Summary"))
    o.append(ul(["Plain JDBC repeats connection, statement, exception and close code in every method.",
                 "SQL built by concatenation is vulnerable to injection; the fix is parameter binding, not escaping.",
                 "Advantages: existing enterprise data, simplified development, zero client configuration, full "
                 "metadata access.",
                 "The main disadvantage is the cost of repeatedly creating and closing connections.",
                 "These problems motivate Spring JDBC (Part 9) and JdbcTemplate (Part 13)."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Show the vulnerable login query and its safe replacement. "
                 "<b>2.</b> Why is a PreparedStatement faster as well as safer? "
                 "<b>3.</b> State the main disadvantage of JDBC in one sentence.</p>"
                 "<p class='small'><i>Answers:</i> (1) <span class='mono'>\"... username='\" + user + \"'\"</span> "
                 "versus <span class='mono'>\"... username=?\"</span> with "
                 "<span class='mono'>pstmt.setString(1, user)</span>. (2) The statement is parsed and planned once "
                 "and reused. (3) Opening and closing a connection is expensive, and doing it per operation destroys "
                 "performance.</p>"))
    o.append(recap("Part 7 recap", [
        ["<b>Boilerplate</b>", "Open, create, execute, close — repeated in every method, with exceptions in between."],
        ["<b>Repetition</b>", "The same twenty lines appear in every DAO method, which invites copy-paste defects."],
        ["<b>SQL injection</b>", "Input becomes syntax when SQL is built by concatenation."],
        ["<b>Fix</b>", "Compile the structure first, bind the values second — that is a PreparedStatement."],
        ["<b>Not a fix</b>", "Escaping quotes by hand; injection also works through numeric and UNION contexts."],
        ["<b>Advantages</b>", "Existing enterprise data, simplified development, zero client configuration, "
                             "metadata access."],
        ["<b>Disadvantage</b>", "Connections are expensive; opening one per operation destroys performance."],
        ["<b>Consequence</b>", "Pooling and Spring JDBC exist to remove exactly these costs."],
    ], terms=["SQL injection", "parameterized query", "string concatenation", "stored procedure", "least privilege", "vendor-specific SQL", "connection cost", "boilerplate", "credential handling"], practice=[
        "Show the attack string that defeats <span class='mono'>' OR '1'='1</span> style code.",
        "Rewrite that vulnerable query with a placeholder and two setters.",
        "Name four advantages of JDBC and its one real disadvantage.",
    ], trap="Assuming <span class='mono'>SQLException</span> alone is the problem. The marks are lost on missing cleanup, not on the exception type."))
    return "".join(o)
