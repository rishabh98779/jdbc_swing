"""PART 6 — Executing Queries and Processing Result Sets."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_matrix():
    b = []
    b.append(txt(12, 16, "WHICH METHOD FOR WHICH SQL?", 8.4, MUTED, 700, ls="0.1em"))
    rows = [("SELECT", "executeQuery(String sql)", "returns a ResultSet", TEAL),
            ("INSERT / UPDATE / DELETE", "executeUpdate(String sql)", "returns int rows affected", ORANGE),
            ("CREATE / DROP / ALTER", "executeUpdate(String sql)", "returns 0 (DDL)", ORANGE),
            ("stored procedure", "prepareCall(sql).execute()", "OUT values via getX(n)", NAVY2),
            ("any SQL, unknown shape", "execute(String sql)", "true → getResultSet(), false → getUpdateCount()", NAVY2)]
    y = 34
    for sql, meth, ret, col in rows:
        b.append(rect(12, y, 168, 32, WHITE, col, 2))
        b.append(txt(96, y + 21, sql, 8.4, col, 700, "middle", MONO))
        b.append(arrow(182, y + 16, 200, y + 16, col, 1.2, hs=5.2))
        b.append(rect(202, y, 196, 32, col, col, 2))
        b.append(txt(300, y + 21, meth, 8.4, WHITE, 700, "middle", MONO))
        b.append(arrow(400, y + 16, 418, y + 16, col, 1.2, hs=5.2))
        b.append(rect(420, y, 228, 32, "#fbfcfd", col, 2))
        b.append(txt(434, y + 21, ret, 8.2, MUTED, 400, "start"))
        y += 40
    return svg(660, y + 4, "".join(b))


def fig_pipeline():
    b = []
    stages = [("1  SQL text", "sent by statement", NAVY, WHITE),
              ("2  Parse & plan", "syntax, privileges, optimizer", TEAL_L, TEAL),
              ("3  Execute", "engine reads pages", TEAL_L, TEAL),
              ("4  Buffer rows", "driver fetches result rows", ORANGE_L, ORANGE),
              ("5  ResultSet", "cursor over the buffer", ORANGE_L, ORANGE)]
    x = 12
    for i, (t, s, fill, tc) in enumerate(stages):
        b.append(node(x, 30, 116, 62, t, s, fill, fill if fill in (NAVY,) else tc, tc, 8.4, 700, 7.0,
                      "#d5e2ee" if fill is NAVY else MUTED))
        if i < 4:
            b.append(arrow(x + 118, 61, x + 128, 61, NAVY3, 1.3, hs=5.6))
        x += 130
    b.append(poly([(600, 94), (600, 116), (70, 116), (70, 94)], MUTED, 1.0, dash="4 3", hs=5.0))
    b.append(txt(330, 130, "rs.next() pulls the next row from the driver's buffer into the cursor", 7.8, MUTED, 400, "middle"))
    b.append(txt(12, 16, "FROM SQL TEXT TO A CURSOR YOU CAN READ", 8.4, MUTED, 700, ls="0.1em"))
    return svg(660, 142, "".join(b))


def fig_cursor():
    b = []
    cols = ["id", "name", "marks"]
    cw, rh = 108, 30
    x0, y0 = 118, 44
    b.append(txt(12, 26, "CURSOR STATES", 8.4, MUTED, 700, ls="0.1em"))
    # header
    for i, c in enumerate(cols):
        b.append(rect(x0 + i * cw, y0, cw, rh, NAVY, NAVY, 0))
        b.append(txt(x0 + i * cw + cw / 2, y0 + 20, c, 8.6, WHITE, 700, "middle"))
    data = [["101", "Rajesh", "88"], ["102", "Simran", "91"], ["103", "Aman", "75"]]
    for r, row in enumerate(data):
        for i, v in enumerate(row):
            b.append(rect(x0 + i * cw, y0 + rh * (r + 1), cw, rh, WHITE, LINE, 0, 0.8))
            b.append(txt(x0 + i * cw + cw / 2, y0 + rh * (r + 1) + 20, v, 8.6, INK, 400, "middle"))
    # side labels with cursors
    labels = [("before first row", y0 + rh / 2, "initial position"), 
              ("row 1", y0 + rh * 1.5, "first rs.next()"),
              ("row 2", y0 + rh * 2.5, "second rs.next()"),
              ("row 3", y0 + rh * 3.5, "third rs.next()"),
              ("after last row", y0 + rh * 4 + 14, "rs.next() returns false")]
    for i, (lab, y, sub) in enumerate(labels):
        col = RED if i == 0 or i == 4 else ORANGE
        b.append(f'<polygon points="{x0-6},{y} {x0-18},{y-5} {x0-18},{y+5}" fill="{col}"/>')
        b.append(txt(x0 - 24, y + 3, lab, 8.0, col, 700, "end"))
        b.append(txt(x0 - 24, y + 14, sub, 7.2, MUTED, 400, "end"))
    b.append(txt(470, y0 + 46, "The cursor starts before the first row, so", 7.8, MUTED, 400))
    b.append(txt(470, y0 + 58, "you must call next() before reading", 7.8, MUTED, 400))
    b.append(txt(470, y0 + 70, "any column of the first row.", 7.8, MUTED, 400))
    b.append(rect(x0, y0 + rh, cw * 3, rh, "none", ORANGE, 0, 1.6))
    return svg(660, y0 + rh * 4 + 32, "".join(b))


def fig_getters():
    b = []
    pairs = [("INT, SMALLINT", "getInt()"), ("VARCHAR, CHAR, TEXT", "getString()"),
             ("DECIMAL, NUMERIC", "getBigDecimal()"), ("DATE", "getDate()"),
             ("TIME", "getTime()"), ("TIMESTAMP", "getTimestamp()"),
             ("BOOLEAN / BIT", "getBoolean()"), ("BLOB", "getBytes() / getBlob()")]
    b.append(txt(12, 16, "SQL TYPE TO JAVA TYPE", 8.4, MUTED, 700, ls="0.1em"))
    for i, (s, g) in enumerate(pairs):
        col, row = i // 4, i % 4
        x = 12 + col * 322
        y = 40 + row * 34
        b.append(rect(x, y, 148, 26, WHITE, TEAL, 2))
        b.append(txt(x + 74, y + 17, s, 8.2, TEAL, 700, "middle", MONO))
        b.append(arrow(x + 150, y + 13, x + 162, y + 13, TEAL2, 1.1, hs=4.8))
        b.append(rect(x + 164, y, 144, 26, ORANGE_L, ORANGE, 2))
        b.append(txt(x + 236, y + 17, g, 8.2, ORANGE, 700, "middle", MONO))
    return svg(660, 178, "".join(b))


def html():
    o = []
    o.append(part(6, "Executing Queries and Processing Results",
                  "Four ways to execute, one cursor to walk, and the getXXX() family that turns SQL types "
                  "into Java types.", art_icon=6))

    o.append(sec("6.1", "Four ways to execute"))
    o.append(p("Every JDBC execution method answers two questions: <i>what kind of SQL is this?</i> and <i>what do "
               "I get back?</i> The API gives you four methods, and each combination of SQL and return value maps to "
               "exactly one of them."))
    o.append(tbl("The four execution methods",
                 ["Method", "Use it for", "Returns"],
                 [["<code>ResultSet executeQuery(String sql)</code>", "SELECT — statements that return rows", "A ResultSet"],
                  ["<code>int executeUpdate(String sql)</code>", "INSERT, UPDATE, DELETE, CREATE, DROP, ALTER",
                   "The number of rows affected (0 for DDL)"],
                  ["<code>boolean execute(String sql)</code>", "Any SQL whose shape is not known in advance",
                   "true if a ResultSet is available; then call getResultSet()"],
                  ["<code>int[] executeBatch()</code>", "A batch of commands added with addBatch()",
                   "One count per command, in order"]],
                 ["34%", "36%", "30%"]))
    o.append(fig(fig_matrix(),
                 "A decision table for the execution methods. If you can answer “does this SQL return rows?”, you "
                 "can pick the method without thinking."))
    o.append(p("<span class='mono'>execute()</span> deserves one extra sentence because it is the method students "
               "misuse. It is for SQL whose shape you cannot know at compile time — a tool that runs whatever the "
               "user typed. After it returns <span class='mono'>true</span> you call "
               "<span class='mono'>getResultSet()</span>; after <span class='mono'>false</span> you call "
               "<span class='mono'>getUpdateCount()</span>. If you know you are running a SELECT, use "
               "<span class='mono'>executeQuery()</span> and stop."))

    o.append(sec("6.2", "Batch execution"))
    o.append(p("A batch sends several commands in one round trip. For a hundred inserts this is the difference "
               "between a hundred network handshakes and one, which is why <span class='mono'>executeBatch()</span> "
               "exists even though the SQL is identical to a loop of "
               "<span class='mono'>executeUpdate()</span> calls."))
    o.append(code('''Statement stmt = con.createStatement();
stmt.addBatch("INSERT INTO student VALUES (7, 'Isha')");
stmt.addBatch("INSERT INTO student VALUES (8, 'Karan')");
stmt.addBatch("UPDATE student SET marks = 90 WHERE id = 7");

int[] counts = stmt.executeBatch();     // one count per command
for (int c : counts) System.out.print(c + " ");
// output: 1 1 1''', "java", "executeBatch() with plain statements"))
    o.append(box("imp", "Important",
                 "<p>Batch execution is a <b>performance</b> feature, not a transaction. If the third command fails, "
                 "the first two may already have been applied — unless auto-commit is off and you roll back "
                 "explicitly. Combine <span class='mono'>addBatch()</span> with "
                 "<span class='mono'>setAutoCommit(false)</span> if the whole batch must succeed or fail together.</p>"))

    o.append(sec("6.3", "What happens inside: the execution pipeline"))
    o.append(p("Understanding the pipeline explains three behaviours students find mysterious: why the first query "
               "on a connection is slow, why <span class='mono'>executeQuery()</span> can return before all rows are "
               "read, and why an updatable ResultSet costs memory."))
    o.append(fig(fig_pipeline(),
                 "The execution pipeline. Steps 1 and 2 are preparation, step 3 is the database's work, steps 4 and "
                 "5 are the driver's."))
    o.append(ul(["The SQL text is <b>parsed and planned</b> every time for a "
                 "<span class='mono'>Statement</span>, and only once for a "
                 "<span class='mono'>PreparedStatement</span> — that is the performance difference in one sentence.",
                 "The driver <b>buffers</b> rows. Many drivers fetch a batch (say 1000 rows) and go back for more "
                 "as the cursor advances, which is why reading a huge table does not exhaust memory.",
                 "The <span class='mono'>ResultSet</span> is therefore a <b>view</b> over a buffer, with a cursor "
                 "pointing at one row at a time."]))

    o.append(sec("6.4", "The ResultSet and its cursor"))
    o.append(p("A <span class='mono'>ResultSet</span> is a table of data representing a database result set. Its "
               "object maintains a <b>cursor pointing to a particular row</b> of that data. The object of ResultSet "
               "maintains a cursor pointing to a row of a table — not to a column, and not to the whole table. "
               "Initially the cursor points <b>before the first row</b>."))
    o.append(box("def", "Definition",
                 "<p>A <b>ResultSet</b> object holds data retrieved from a database after an SQL query is executed "
                 "using a Statement object. It acts as an iterator that allows you to move through its data. By "
                 "default a ResultSet object is <b>forward only</b> and <b>not updatable</b>.</p>"))
    o.append(fig(fig_cursor(),
                 "Cursor movement over a ResultSet. next() advances one row and returns true while the row is valid; "
                 "before the first call the cursor sits above row 1, and after the last row next() returns false."))
    o.append(code('''ResultSet rs = stmt.executeQuery("SELECT id, name, marks FROM student");
while (rs.next()) {                       // advance, then read
    int    id    = rs.getInt("id");       // by column name
    String name  = rs.getString(2);       // or by column index (1-based)
    int    marks = rs.getInt("marks");
    System.out.println(id + "  " + name + "  " + marks);
}''', "java", "The canonical ResultSet loop"))
    o.append(p("Two columns of the same row are read with two getter calls; the cursor does not move between them. "
               "This is the single most common misunderstanding: <span class='mono'>next()</span> moves rows, "
               "<span class='mono'>getXxx()</span> reads columns of the current row."))

    o.append(sec("6.5", "Moving the cursor"))
    o.append(tbl("Cursor navigation methods",
                 ["Method", "Description"],
                 [["<code>boolean next()</code>", "Moves the cursor one row forward from the current position"],
                  ["<code>boolean previous()</code>", "Moves the cursor one row back"],
                  ["<code>boolean first()</code>", "Moves the cursor to the first row"],
                  ["<code>boolean last()</code>", "Moves the cursor to the last row"],
                  ["<code>boolean absolute(int row)</code>", "Moves the cursor to the specified row number"],
                  ["<code>boolean relative(int rows)</code>", "Moves the cursor by a relative number of rows (may be negative)"],
                  ["<code>void beforeFirst()</code> / <code>afterLast()</code>", "Moves to the positions just outside the data"],
                  ["<code>int getRow()</code>", "Returns the current row number"]],
                 ["44%", "56%"]))
    o.append(box("mistake", "Common mistake",
                 "<p>Calling <span class='mono'>previous()</span>, <span class='mono'>first()</span> or "
                 "<span class='mono'>absolute()</span> on a default ResultSet throws "
                 "<span class='mono'>SQLException: Operation not supported</span>. Those methods need a scrollable "
                 "result set, which you must request when creating the statement: "
                 "<span class='mono'>con.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, "
                 "ResultSet.CONCUR_READ_ONLY)</span>.</p>"))

    o.append(sec("6.6", "Reading column values"))
    o.append(p("Each SQL type has a matching getter. The getter both retrieves the value and converts it to a Java "
               "type; if the conversion is impossible — asking for an "
               "<span class='mono'>int</span> from a text column that holds letters — it throws "
               "<span class='mono'>SQLException</span>."))
    o.append(fig(fig_getters(),
                 "The getXXX() family. The same value can often be read in more than one type — a numeric column "
                 "can be read with getInt() or getString() — but choosing the natural type avoids surprises with "
                 "rounding and nulls."))
    o.append(code('''// Column indexes are 1-based; column names are case-insensitive
int     id    = rs.getInt(1);
String  name  = rs.getString("name");
double  fee   = rs.getDouble("fee");
java.sql.Date dob = rs.getDate("dob");       // java.sql.Date, not java.util.Date

// Null handling: check first, because getInt() on NULL returns 0
int marks = rs.getInt("marks");
if (rs.wasNull()) {
    System.out.println("marks is NULL for this row");
}''', "java", "Getters by index and by name, plus the wasNull() idiom"))
    o.append(box("imp", "Important",
                 "<p><span class='mono'>rs.wasNull()</span> is the only reliable way to distinguish a stored "
                 "<span class='mono'>NULL</span> from a genuine zero, because "
                 "<span class='mono'>getInt()</span> returns 0 for both. This is a favourite viva question.</p>"))

    o.append(sec("6.7", "ResultSet types and concurrency"))
    o.append(tbl("ResultSet capabilities you can request",
                 ["Constant", "Meaning"],
                 [["<code>TYPE_FORWARD_ONLY</code>", "The default: the cursor moves forward only"],
                  ["<code>TYPE_SCROLL_INSENSITIVE</code>", "The cursor can move anywhere; changes made by others are not seen"],
                  ["<code>TYPE_SCROLL_SENSITIVE</code>", "The cursor can move anywhere and may see changes made by others"],
                  ["<code>CONCUR_READ_ONLY</code>", "The default: the ResultSet cannot update the database"],
                  ["<code>CONCUR_UPDATABLE</code>", "Rows can be changed through the ResultSet (updateRow, deleteRow)"]],
                 ["40%", "60%"]))
    o.append(p("Scrollable result sets are convenient but expensive: the driver must keep rows in memory or be able "
               "to re-query. For the great majority of programs, the forward-only default is both faster and enough, "
               "because you are streaming rows into a report or a collection anyway."))

    o.append(sec("6.8", "A complete CRUD walk-through"))
    o.append(p("The four operations below use the same table, <span class='mono'>student(id, name, marks)</span>, and "
               "the same connection. Run them in order and the output is exactly what the comments show."))
    o.append(code('''CREATE TABLE student (
    id    INT PRIMARY KEY,
    name  VARCHAR(50),
    marks INT
);''', "sql", "The table used by every example in this part"))
    o.append(code('''// INSERT - two rows
PreparedStatement ins = con.prepareStatement(
        "INSERT INTO student (id, name, marks) VALUES (?, ?, ?)");
ins.setInt(1, 101); ins.setString(2, "Rajesh"); ins.setInt(3, 88);
System.out.println(ins.executeUpdate());     // 1
ins.setInt(1, 102); ins.setString(2, "Simran"); ins.setInt(3, 91);
System.out.println(ins.executeUpdate());     // 1''', "java", "CREATE (insert) with a prepared statement"))
    o.append(code('''// SELECT - walk the rows
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery(
        "SELECT id, name, marks FROM student ORDER BY id");
while (rs.next()) {
    System.out.printf("%-5d %-10s %3d%n",
            rs.getInt("id"), rs.getString("name"), rs.getInt("marks"));
}''', "java", "READ (select) and process every row"))
    o.append(raw_code('''101   Rajesh      88
102   Simran      91''', "Output of the SELECT above"))
    o.append(code('''// UPDATE - change one column of one row
PreparedStatement upd = con.prepareStatement(
        "UPDATE student SET marks = ? WHERE id = ?");
upd.setInt(1, 95); upd.setInt(2, 101);
System.out.println(upd.executeUpdate() + " row(s) updated");   // 1 row(s) updated''',
                 "java", "UPDATE with executeUpdate()"))
    o.append(code('''// DELETE - remove one row
PreparedStatement del = con.prepareStatement(
        "DELETE FROM student WHERE id = ?");
del.setInt(1, 102);
System.out.println(del.executeUpdate() + " row(s) deleted");   // 1 row(s) deleted''',
                 "java", "DELETE with executeUpdate()"))

    o.append(sec("6.9", "Summary"))
    o.append(ul(["Use executeQuery for SELECT, executeUpdate for INSERT/UPDATE/DELETE/DDL, execute for unknown "
                 "shapes, executeBatch for many commands at once.",
                 "The ResultSet cursor starts before the first row; next() advances it and returns false at the end.",
                 "Column indexes are 1-based; getters read columns and never move the cursor.",
                 "wasNull() distinguishes SQL NULL from a zero value.",
                 "Scrollable and updatable result sets must be requested; forward-only read-only is the default."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Which method returns the number of rows affected by a DELETE? "
                 "<b>2.</b> Where does the cursor point before the first <span class='mono'>next()</span>? "
                 "<b>3.</b> How do you detect a NULL integer column?</p>"
                 "<p class='small'><i>Answers:</i> (1) <span class='mono'>executeUpdate()</span>. (2) Before the "
                 "first row. (3) Read it with <span class='mono'>getInt()</span> and then test "
                 "<span class='mono'>rs.wasNull()</span>.</p>"))
    o.append(recap("Part 6 recap", [
        ["<b>executeQuery</b>", "SELECT only; returns a ResultSet."],
        ["<b>executeUpdate</b>", "INSERT, UPDATE, DELETE, DDL; returns the affected row count."],
        ["<b>execute</b>", "Anything; returns <span class='mono'>true</span> if the first result is a ResultSet."],
        ["<b>executeBatch</b>", "Many commands in one round trip; returns per-command counts."],
        ["<b>Cursor</b>", "The ResultSet cursor starts <i>before</i> the first row; <span class='mono'>next()</span> moves it and returns false at the end."],
        ["<b>Reading</b>", "Fixed types with <span class='mono'>getInt/getString/getDate</span>, or <span class='mono'>getObject</span> when the type is unknown."],
        ["<b>NULL</b>", "<span class='mono'>getInt()</span> returns 0 for NULL — always test <span class='mono'>wasNull()</span>."],
    ], terms=["executeQuery()", "executeUpdate()", "execute()", "executeBatch()", "ResultSet cursor", "rs.next()", "TYPE_FORWARD_ONLY", "CONCUR_UPDATABLE", "wasNull()"], practice=[
        "Which method runs an INSERT, and what does it return?",
        "Where does the cursor sit before the first <span class='mono'>next()</span>?",
        "How do you detect a NULL in an <span class='mono'>int</span> column?",
    ], trap="Reading a column before <span class='mono'>next()</span>. The cursor starts before the first row, so there is nothing to read."))
    return "".join(o)
