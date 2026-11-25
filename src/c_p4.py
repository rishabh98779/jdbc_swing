"""PART 4 — The Connection Interface."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_hub():
    b = []
    b.append(node(248, 92, 164, 66, "Connection", "one open session", TEAL_L, TEAL, TEAL, 10.6, 700, 8.0))
    left = [("Statement", "createStatement()"), ("PreparedStatement", "prepareStatement(sql)"),
            ("CallableStatement", "prepareCall(sql)")]
    right = [("DatabaseMetaData", "getMetaData()"), ("Transaction control", "setAutoCommit / commit / rollback"),
             ("Session end", "close()")]
    for i, (t, m) in enumerate(left):
        y = 14 + i * 74
        b.append(node(14, y, 176, 52, t, m, NAVY, NAVY, WHITE, 8.6, 700, 7.0, "#b9cbdd"))
        b.append(arrow(192, y + 26, 246, 118 + (i - 1) * 10, TEAL2, 1.2, hs=5.4))
    for i, (t, m) in enumerate(right):
        y = 14 + i * 74
        fill = ORANGE_L if i == 1 else (RED_L if i == 2 else WHITE)
        stroke = ORANGE if i == 1 else (RED if i == 2 else NAVY)
        b.append(node(470, y, 176, 52, t, m, fill, stroke, stroke, 8.6, 700, 7.0))
        b.append(arrow(414, 118 + (i - 1) * 10, 468, y + 26, TEAL2, 1.2, hs=5.4))
    b.append(txt(330, 80, "FACTORY", 7.6, TEAL, 700, "middle", ls="0.14em"))
    b.append(txt(330, 178, "the session", 7.6, TEAL, 700, "middle", ls="0.1em"))
    return svg(660, 240, "".join(b))


def fig_txn():
    b = []
    b.append(txt(12, 18, "AUTO-COMMIT ON (THE DEFAULT)", 8.4, NAVY, 700, ls="0.08em"))
    y = 40
    steps = ["INSERT", "UPDATE", "DELETE"]
    for i, s in enumerate(steps):
        b.append(node(12 + i * 96, y, 84, 26, s, None, TEAL_L, TEAL, TEAL, 8.0, 600))
        b.append(txt(96 + i * 96 - 4, y + 17, "committed", 7.0, TEAL, 700, "end"))
    b.append(txt(12, y + 46, "every statement is its own transaction — a crash keeps the first two", 7.6, MUTED, 400))

    b.append(line(12, 108, 648, 108, LINE, 0.8))
    b.append(txt(12, 130, "AUTO-COMMIT OFF (EXPLICIT TRANSACTION)", 8.4, NAVY, 700, ls="0.08em"))
    y2 = 152
    b.append(node(12, y2, 84, 26, "setAutoCommit(false)", None, ORANGE_L, ORANGE, ORANGE, 7.4, 600))
    for i, s in enumerate(steps):
        b.append(node(112 + i * 96, y2, 84, 26, s, None, GREY, LINE, INK, 8.0, 600))
    b.append(rect(106, y2 - 6, 288, 38, "none", ORANGE, 3, 1.0, "4 3"))
    b.append(txt(250, y2 + 46, "one unit of work", 7.6, ORANGE, 700, "middle"))
    b.append(node(410, y2 - 14, 76, 26, "commit()", None, TEAL, TEAL, WHITE, 8.0, 700))
    b.append(node(410, y2 + 20, 76, 26, "rollback()", None, RED, RED, WHITE, 8.0, 700))
    b.append(arrow(398, y2 + 4, 408, y2 - 1, TEAL2, 1.1, hs=5.0))
    b.append(arrow(398, y2 + 20, 408, y2 + 33, RED, 1.1, hs=5.0))
    b.append(txt(496, y2 - 2, "all three statements are kept", 7.6, TEAL, 400))
    b.append(txt(496, y2 + 34, "all three are undone", 7.6, RED, 400))
    b.append(txt(12, 232, "A transaction is all-or-nothing: the database either applies every statement in the block, or none of them.",
                 7.8, MUTED, 400))
    return svg(660, 244, "".join(b))


def fig_conn_lifecycle():
    b = []
    st = [("getConnection()", "URL + credentials", NAVY, WHITE),
          ("configure", "setAutoCommit, setReadOnly,\nsetTransactionIsolation", WHITE, NAVY3),
          ("work", "statements, queries,\ncommit or rollback", TEAL_L, TEAL),
          ("close()", "returns the socket to the pool\nor closes it", ORANGE_L, ORANGE)]
    x = 12
    for i, (t, s, fill, tc) in enumerate(st):
        b.append(node(x, 30, 148, 74, t, s.replace("\n", " "), fill, fill if fill is NAVY else tc, tc, 9.2, 700, 7.4,
                      "#d5e2ee" if fill is NAVY else MUTED))
        if i < 3:
            b.append(arrow(x + 150, 67, x + 166, 67, NAVY3, 1.4, hs=6.2))
        x += 168
    b.append(poly([(570, 106), (570, 130), (86, 130), (86, 108)], MUTED, 1.0, dash="4 3", hs=5.4))
    b.append(txt(330, 144, "reuse: a pooled connection goes back to the pool instead of being destroyed", 7.6, MUTED, 400, "middle"))
    return svg(660, 154, "".join(b))


def html():
    o = []
    o.append(part(4, "Working with the Connection Interface",
                  "The object that represents an open session — what creates it, what it creates, and "
                  "how it ends cleanly.", art_icon=4))

    o.append(sec("4.1", "What a Connection is"))
    o.append(p("A <span class='mono'>Connection</span> object is the physical session between your Java program "
               "and the database. Everything you do — every query, every update, every transaction boundary — "
               "happens inside a connection. It is the object that holds the network socket, the "
               "authentication state and the current transaction."))
    o.append(box("def", "Definition",
                 "<p>A <b>Connection</b> is the session between the Java application and the database. The "
                 "<span class='mono'>Connection</span> interface is a <b>factory of Statement, PreparedStatement "
                 "and DatabaseMetaData</b> — the object of Connection can be used to get the objects of Statement "
                 "and DatabaseMetaData. It also provides methods for transaction management such as "
                 "<span class='mono'>commit()</span> and <span class='mono'>rollback()</span>. By default, a "
                 "connection commits the changes after executing queries.</p>"))
    o.append(p("The word <b>factory</b> is the key. You do not construct a Statement with "
               "<span class='mono'>new</span>; the connection manufactures it, because only the connection knows "
               "which driver, which protocol and which session the statement belongs to. This is the factory "
               "method pattern, and it is why the same line of code works against every database."))
    o.append(fig(fig_hub(),
                 "Connection as a hub. Everything the program needs is manufactured by the connection, and the "
                 "labels show the exact method that manufactures it."))
    o.append(box("imp", "Important",
                 "<p>One connection can create many statements, and one statement can be executed many times. A "
                 "connection is <b>expensive</b> to create (TCP handshake, authentication, session setup) and "
                 "cheap to reuse. That single fact explains connection pooling, Spring's "
                 "<span class='mono'>DataSource</span>, and the main disadvantage of plain JDBC in Part 7.</p>"))

    o.append(sec("4.2", "How a Connection is obtained"))
    o.append(p("There is exactly one standard way to obtain a connection in plain JDBC: ask "
               "<span class='mono'>DriverManager</span>. The class offers two overloads, and the second is the one "
               "you should use, because a database that accepts anonymous connections is a database waiting to be "
               "misused."))
    o.append(code('''// 1. URL only - rarely used; the database must not require credentials
Connection con1 = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/mydb");

// 2. URL + user + password - the normal form
Connection con2 = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/mydb", "root", "your_password");

// 3. URL + properties (useful for SSL and timeouts)
Properties props = new Properties();
props.setProperty("user", "root");
props.setProperty("password", "your_password");
props.setProperty("useSSL", "true");
Connection con3 = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/mydb", props);''', "java", "The three overloads of DriverManager.getConnection()"))
    o.append(p("Each call throws <span class='mono'>SQLException</span>. The exception is checked, so the call must "
               "be inside a <span class='mono'>try</span> block or the method must declare "
               "<span class='mono'>throws SQLException</span>. In a real application you catch it, log it and "
               "translate it into something the caller can act on; in an examination answer, either is acceptable "
               "as long as the exception is handled."))
    o.append(box("mistake", "Common mistake",
                 "<p>Calling <span class='mono'>getConnection()</span> inside a loop, once per query. Each call "
                 "opens a new session, and a few hundred of them exhaust the server's connection limit. Open once, "
                 "reuse, close once.</p>"))

    o.append(sec("4.3", "The methods that matter"))
    o.append(tbl("Commonly used methods of the Connection interface",
                 ["Method", "What it does"],
                 [["<code>Statement createStatement()</code>", "Creates a Statement object for executing SQL queries"],
                  ["<code>Statement createStatement(int type, int concurrency)</code>",
                   "Creates a Statement whose ResultSets have the given type and concurrency (for example scrollable or updatable)"],
                  ["<code>PreparedStatement prepareStatement(String sql)</code>",
                   "Creates a precompiled statement with <code>?</code> placeholders"],
                  ["<code>CallableStatement prepareCall(String sql)</code>",
                   "Creates a statement for calling a stored procedure"],
                  ["<code>DatabaseMetaData getMetaData()</code>", "Describes the database: product name, version, capabilities"],
                  ["<code>void setAutoCommit(boolean status)</code>", "Sets the commit mode; true by default"],
                  ["<code>void commit()</code>", "Makes all changes since the last commit or rollback permanent"],
                  ["<code>void rollback()</code>", "Drops all changes since the last commit or rollback"],
                  ["<code>void close()</code>", "Closes the connection and releases JDBC resources immediately"]],
                 ["46%", "54%"]))
    o.append(p("The lecture material stresses two of these: "
               "<span class='mono'>createStatement(int resultSetType, int resultSetConcurrency)</span> exists so "
               "that you can ask for a <i>scrollable</i> or <i>updatable</i> result set, and "
               "<span class='mono'>setAutoCommit()</span> exists so that several statements can be grouped into one "
               "transaction. Both are examined as “what does this overload add?”."))

    o.append(sec("4.4", "Transactions: commit and rollback"))
    o.append(p("By default a connection runs in <b>auto-commit</b> mode: every statement is committed the moment it "
               "succeeds, and there is no way to undo it. That is fine for a single INSERT typed at a prompt, and "
               "wrong for a money transfer, which must debit one account and credit another or do neither."))
    o.append(fig(fig_txn(),
                 "Auto-commit versus an explicit transaction. Turning auto-commit off groups statements into one "
                 "unit of work that is ended either by commit() or by rollback()."))
    o.append(code('''Connection con = DriverManager.getConnection(URL, USER, PASS);
try {
    con.setAutoCommit(false);                     // begin a transaction

    PreparedStatement debit = con.prepareStatement(
            "UPDATE account SET balance = balance - ? WHERE id = ?");
    debit.setDouble(1, 500.00);
    debit.setInt(2, 101);
    debit.executeUpdate();

    PreparedStatement credit = con.prepareStatement(
            "UPDATE account SET balance = balance + ? WHERE id = ?");
    credit.setDouble(1, 500.00);
    credit.setInt(2, 102);
    credit.executeUpdate();

    con.commit();                                 // both updates become permanent
    System.out.println("Transfer complete");
} catch (SQLException e) {
    con.rollback();                               // neither update survives
    System.out.println("Transfer cancelled: " + e.getMessage());
} finally {
    con.setAutoCommit(true);                      // restore the default
    con.close();
}''', "java", "A money transfer as one transaction — the classic commit/rollback example"))
    o.append(box("tip", "Exam tip",
                 "<p>If a question asks “what is the default value of auto-commit?”, the answer is <b>true</b>. If it "
                 "asks why <span class='mono'>rollback()</span> matters, answer with atomicity: a transaction is "
                 "all-or-nothing, so a half-finished transfer can never be left in the database.</p>"))

    o.append(sec("4.5", "Metadata: asking the database about itself"))
    o.append(p("A connection can also describe its database. <span class='mono'>getMetaData()</span> returns a "
               "<span class='mono'>DatabaseMetaData</span> object with the product name, version, supported SQL "
               "features and the list of tables. This is what makes a generic tool — an IDE's database browser, a "
               "reporting engine — possible: it can discover the schema at run time instead of being written for "
               "one database."))
    o.append(code('''DatabaseMetaData md = con.getMetaData();
System.out.println("Product : " + md.getDatabaseProductName());   // MySQL
System.out.println("Version : " + md.getDatabaseProductVersion()); // 8.0.36
System.out.println("Driver  : " + md.getDriverName());             // MySQL Connector/J''',
                 "java", "Reading database metadata through the connection"))

    o.append(sec("4.6", "Ending a session"))
    o.append(p("Closing a connection releases the socket, the server-side session and any locks it holds. The order "
               "matters: close the <span class='mono'>ResultSet</span> first, then the "
               "<span class='mono'>Statement</span>, then the <span class='mono'>Connection</span>. Closing a "
               "connection also closes the statements created from it, which is why the lecture material can say "
               "that “by closing the connection object, the statement and ResultSet will be closed automatically” — "
               "true, but only in that direction."))
    o.append(fig(fig_conn_lifecycle(),
                 "The life of a connection: obtain it, configure it, use it, close it. With a pool, closing returns "
                 "it for reuse instead of destroying the socket."))
    o.append(code('''// Lecture style: explicit closes
Connection con = null;
Statement stmt = null;
ResultSet rs = null;
try {
    con = DriverManager.getConnection(URL, USER, PASS);
    stmt = con.createStatement();
    rs = stmt.executeQuery("SELECT * FROM student");
    while (rs.next()) { /* ... */ }
} catch (SQLException e) {
    System.out.println(e);
} finally {
    if (rs != null)   rs.close();
    if (stmt != null) stmt.close();
    if (con != null)  con.close();
}''', "java", "The classic close pattern, safe even when an earlier step failed"))
    o.append(p("Since Java 7 the same thing can be written without the null checks. A resource declared in the "
               "<span class='mono'>try</span> header is closed automatically, in reverse order, even if an exception "
               "is thrown — and the exception is never swallowed."))
    o.append(code('''try (Connection con = DriverManager.getConnection(URL, USER, PASS);
     Statement stmt = con.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM student")) {
    while (rs.next()) { /* ... */ }
} catch (SQLException e) {
    System.out.println(e);
}''', "java", "The same code with try-with-resources — recommended in modern Java"))
    o.append(box("mistake", "Common mistake",
                 "<p>Closing in the wrong order, or closing only the connection after an exception has already "
                 "skipped the close lines. The <span class='mono'>finally</span> block (or "
                 "<span class='mono'>try-with-resources</span>) exists precisely so that clean-up happens on both "
                 "paths.</p>"))

    o.append(sec("4.7", "Summary"))
    o.append(ul(["A Connection is an open session and a factory for Statement, PreparedStatement, "
                 "CallableStatement and DatabaseMetaData.",
                 "Obtain it with <span class='mono'>DriverManager.getConnection(url, user, password)</span>.",
                 "Auto-commit is <b>true</b> by default; switch it off to group statements into a transaction.",
                 "commit() makes changes permanent; rollback() undoes them.",
                 "Close ResultSet, then Statement, then Connection — or let try-with-resources do it."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Why is Connection called a factory? "
                 "<b>2.</b> What is the default value of auto-commit? "
                 "<b>3.</b> Which method would you call to make a ResultSet scrollable?</p>"
                 "<p class='small'><i>Answers:</i> (1) Because it creates Statement, PreparedStatement and "
                 "DatabaseMetaData objects. (2) true. (3) "
                 "<span class='mono'>createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, "
                 "ResultSet.CONCUR_READ_ONLY)</span>.</p>"))
    o.append(recap("Part 4 recap", [
        ["<b>What it is</b>", "One open session with one database; a factory for statements and metadata."],
        ["<b>Creation</b>", "<span class='mono'>DriverManager.getConnection(url, user, pass)</span> — the only way in plain JDBC."],
        ["<b>Factory methods</b>", "<span class='mono'>createStatement</span>, <span class='mono'>prepareStatement</span>, <span class='mono'>prepareCall</span>."],
        ["<b>Transactions</b>", "<span class='mono'>setAutoCommit(false)</span>, then <span class='mono'>commit()</span> or <span class='mono'>rollback()</span>."],
        ["<b>Metadata</b>", "<span class='mono'>getMetaData()</span> returns <span class='mono'>DatabaseMetaData</span>: product, version, capabilities."],
        ["<b>Closing</b>", "<span class='mono'>close()</span> releases the session; try-with-resources closes it for you."],
    ], terms=["Connection interface", "auto-commit", "commit()", "rollback()", "transaction", "DatabaseMetaData", "try-with-resources", "connection leak", "statement factory"], practice=[
        "Which Connection method creates a CallableStatement?",
        "Write the three calls that switch off auto-commit, commit, and roll back.",
        "What does <span class='mono'>getMetaData()</span> return, and name one fact you can ask it?",
    ], trap="Leaving auto-commit on and then calling <span class='mono'>rollback()</span>. Every statement already committed."))
    return "".join(o)
