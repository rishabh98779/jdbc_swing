"""PART 5 — Statement, PreparedStatement and CallableStatement."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_hierarchy():
    b = []
    b.append(node(238, 12, 184, 46, "Statement", "simple SQL, no parameters", NAVY, NAVY, WHITE, 10.0, 700, 7.6, "#d5e2ee"))
    b.append(node(238, 86, 184, 46, "PreparedStatement", "precompiled, ? parameters", TEAL_L, TEAL, TEAL, 9.6, 700, 7.4))
    b.append(node(238, 160, 184, 46, "CallableStatement", "stored procedures, IN/OUT", ORANGE_L, ORANGE, ORANGE, 9.6, 700, 7.4))
    b.append(arrow(330, 58, 330, 84, NAVY3, 1.4, hs=6.4))
    b.append(arrow(330, 132, 330, 158, NAVY3, 1.4, hs=6.4))
    b.append(txt(344, 76, "extends", 7.4, MUTED, 600, "start"))
    b.append(txt(344, 150, "extends", 7.4, MUTED, 600, "start"))
    # who creates them, and what they return
    b.append(node(8, 92, 150, 62, "Connection", "creates each of the three", WHITE, NAVY3, NAVY3, 9.0, 700, 7.0))
    for y in (35, 109, 183):
        b.append(arrow(160, y, 234, y, MUTED, 1.1, dash="4 2", hs=5.0))
    b.append(node(452, 86, 196, 46, "ResultSet", "what executeQuery() returns", WHITE, NAVY3, NAVY3, 9.0, 700, 7.2))
    b.append(arrow(424, 109, 450, 109, MUTED, 1.1, dash="4 2", hs=5.0))
    b.append(txt(330, 226, "Solid arrows are inheritance (extends); dashed arrows are objects created at run time.",
                 7.8, MUTED, 400, "middle"))
    return svg(660, 238, "".join(b))


def fig_three_way():
    b = []
    cols = [
        ("Statement", NAVY, WHITE, ["SQL built by string", "compiled every time", "no parameters", "one row-set at a time"]),
        ("PreparedStatement", TEAL, WHITE, ["SQL with ? holes", "compiled once, reused", "typed setters", "immune to injection"]),
        ("CallableStatement", ORANGE, WHITE, ["calls a procedure", "logic lives in the DB", "IN, OUT, INOUT", "batch of business work"]),
    ]
    for i, (name, fill, tc, bullets) in enumerate(cols):
        x = 12 + i * 216
        b.append(rect(x, 12, 200, 150, "#fbfcfd", fill, 3))
        b.append(rect(x, 12, 200, 30, fill, fill, 3))
        b.append(txt(x + 100, 32, name, 9.2, tc, 700, "middle"))
        for j, bl in enumerate(bullets):
            b.append(txt(x + 14, 62 + j * 22, "—", 8.0, fill, 700))
            b.append(txt(x + 26, 62 + j * 22, bl, 8.2, INK, 400))
    b.append(txt(330, 182, "All three are created by the connection and all three return a ResultSet for SELECT.",
                 7.8, MUTED, 400, "middle"))
    return svg(660, 192, "".join(b))


def fig_callable():
    b = []
    b.append(node(12, 16, 150, 52, "Java program", "CallableStatement", NAVY, NAVY, WHITE, 8.8, 700, 7.4, "#d5e2ee"))
    b.append(node(196, 16, 164, 52, 'prepareCall("{call p(?,?)}")', None, TEAL_L, TEAL, TEAL, 7.4, 600))
    b.append(rect(392, 10, 256, 104, WHITE, ORANGE, 2))
    b.append(txt(520, 30, "Stored procedure in the DBMS", 8.6, ORANGE, 700, "middle"))
    b.append(rect(404, 44, 108, 22, GREY, LINE, 2))
    b.append(txt(458, 59, "IN emp_id", 7.4, NAVY3, 600, "middle", MONO))
    b.append(rect(520, 44, 116, 22, GREY, LINE, 2))
    b.append(txt(578, 59, "OUT emp_name", 7.4, ORANGE, 600, "middle", MONO))
    b.append(txt(495, 88, "compiled once, stored in the catalog", 7.0, MUTED, 400, "middle"))
    b.append(arrow(164, 40, 194, 40, NAVY3, 1.3, hs=5.8))
    b.append(arrow(362, 40, 390, 40, ORANGE, 1.3, hs=5.8))
    b.append(node(100, 152, 280, 36, "registerOutParameter(2, Types.VARCHAR)", None, WHITE, TEAL, TEAL, 7.2, 600))
    b.append(arrow(240, 150, 240, 70, TEAL, 1.2, hs=5.4))
    b.append(rect(392, 158, 256, 40, TEAL_L, TEAL, 2))
    b.append(txt(520, 174, "execute()  then  getString(2)", 7.6, TEAL, 700, "middle", MONO))
    b.append(txt(520, 189, "the OUT value, read after the call", 6.9, MUTED, 400, "middle"))
    b.append(arrow(578, 68, 578, 156, TEAL2, 1.1, dash="4 2", hs=5.2))
    return svg(660, 206, "".join(b))


def html():
    o = []
    o.append(part(5, "Statement, PreparedStatement and CallableStatement",
                  "Three ways to send SQL, one inheritance chain, and the difference that decides marks, "
                  "performance and security.", art_icon=5))

    o.append(sec("5.1", "The three statement types"))
    o.append(p("A <span class='mono'>Statement</span> is the object that carries SQL to the database. JDBC offers "
               "three versions of it, and the differences are not cosmetic: they change when SQL is compiled, "
               "whether parameters are allowed, and whether the query is safe from injection."))
    o.append(fig(fig_hierarchy(),
                 "The statement hierarchy. PreparedStatement is a subinterface of Statement, and "
                 "CallableStatement is a subinterface of PreparedStatement — so a CallableStatement can do "
                 "everything a PreparedStatement can do."))
    o.append(fig(fig_three_way(),
                 "The three interfaces side by side. The left column is what you write for a one-off query; the "
                 "middle column is what you write for anything that takes input; the right column is what you write "
                 "when the logic lives in the database."))

    o.append(sec("5.2", "Statement: the plain sender"))
    o.append(p("The <span class='mono'>Statement</span> interface provides methods to execute queries with the "
               "database. It is a <b>factory of ResultSet</b>: it provides the factory method that returns a "
               "<span class='mono'>ResultSet</span> object. It is created with "
               "<span class='mono'>Connection.createStatement()</span> and is intended for <b>simple SQL statements "
               "with no parameters</b>."))
    o.append(tbl("Commonly used methods of the Statement interface",
                 ["Method", "Description"],
                 [["<code>ResultSet executeQuery(String sql)</code>", "Executes a SELECT query and returns a ResultSet"],
                  ["<code>int executeUpdate(String sql)</code>",
                   "Executes INSERT, UPDATE, DELETE, CREATE, DROP; returns the row count (0 for DDL)"],
                  ["<code>boolean execute(String sql)</code>", "Executes any SQL; returns true if the result is a ResultSet"],
                  ["<code>int[] executeBatch()</code>", "Executes a batch of commands and returns per-command counts"],
                  ["<code>void addBatch(String sql)</code>", "Adds a statement to the batch"],
                  ["<code>void setMaxRows(int n)</code>", "Limits the number of rows a ResultSet may contain"],
                  ["<code>void close()</code>", "Releases the statement's resources"]],
                 ["44%", "56%"]))
    o.append(code('''import java.sql.*;

public class FetchRecord {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/mydb", "root", "your_password");
        Statement stmt = con.createStatement();

        int result = stmt.executeUpdate("DELETE FROM student WHERE id = 33");
        System.out.println(result + " records affected");

        con.close();
    }
}''', "java", "The lecture's Statement example — executeUpdate returns the number of affected rows"))
    o.append(p("Three observations about that program. It uses "
               "<span class='mono'>executeUpdate</span> because DELETE changes data rather than returning rows; it "
               "prints the return value, which is the count of rows actually deleted (0 if the id did not exist); "
               "and it closes only the connection, which also closes the statement."))

    o.append(sec("5.3", "PreparedStatement: compile once, run many times"))
    o.append(p("A <span class='mono'>PreparedStatement</span> is a subinterface of "
               "<span class='mono'>Statement</span> used to execute <b>parameterized queries</b>. Instead of "
               "building SQL by gluing strings together, you write the query once with "
               "<span class='mono'>?</span> placeholders and supply the values afterwards through typed setter "
               "methods."))
    o.append(code('''String sql = "INSERT INTO emp VALUES (?, ?, ?)";   // three placeholders
PreparedStatement ps = con.prepareStatement(sql);
ps.setInt(1, 33);
ps.setString(2, "Irfan");
ps.setDouble(3, 50000);
ps.executeUpdate();''', "java", "A parameterized query: the structure is fixed, the values are separate"))
    o.append(p("Two benefits follow immediately. <b>Performance</b>: the database parses, validates and plans the "
               "statement once, and every later execution reuses that plan — so the query is compiled only once. "
               "<b>Security</b>: because the value never becomes part of the SQL text, a value such as "
               "<span class='mono'>' OR '1'='1</span> is treated as a literal string, not as syntax."))
    o.append(tbl("Methods of the PreparedStatement interface",
                 ["Method", "Description"],
                 [["<code>void setInt(int index, int value)</code>", "Sets an integer value at the given parameter index"],
                  ["<code>void setString(int index, String value)</code>", "Sets a String value at the given index"],
                  ["<code>void setFloat(int index, float value)</code>", "Sets a float value"],
                  ["<code>void setDouble(int index, double value)</code>", "Sets a double value"],
                  ["<code>void setDate(int index, java.sql.Date d)</code>", "Sets a date (use java.sql.Date, not java.util.Date)"],
                  ["<code>void setNull(int index, int sqlType)</code>", "Sets an explicit SQL NULL"],
                  ["<code>int executeUpdate()</code>", "Runs INSERT, UPDATE, DELETE, or DDL; returns the row count"],
                  ["<code>ResultSet executeQuery()</code>", "Runs a SELECT; returns a ResultSet"]],
                 ["48%", "52%"]))
    o.append(box("imp", "Important",
                 "<p>Parameter indexes start at <b>1</b>, not 0. This single fact causes more "
                 "<span class='mono'>SQLException: Parameter index out of range</span> errors in student code than "
                 "any other.</p>"))
    o.append(code('''// The three standard operations, written as prepared statements
String insert = "INSERT INTO student (id, name) VALUES (?, ?)";
String update = "UPDATE student SET name = ? WHERE id = ?";
String delete = "DELETE FROM student WHERE id = ?";
String select = "SELECT id, name FROM student WHERE id = ?";

try (PreparedStatement psIns = con.prepareStatement(insert);
     PreparedStatement psUpd = con.prepareStatement(update);
     PreparedStatement psDel = con.prepareStatement(delete);
     PreparedStatement psSel = con.prepareStatement(select)) {

    psIns.setInt(1, 6);   psIns.setString(2, "Harinder");
    int inserted = psIns.executeUpdate();

    psUpd.setString(1, "Kaur"); psUpd.setInt(2, 1);
    int updated = psUpd.executeUpdate();

    psDel.setInt(1, 2);
    int deleted = psDel.executeUpdate();

    psSel.setInt(1, 101);
    try (ResultSet rs = psSel.executeQuery()) {
        while (rs.next()) {
            System.out.println(rs.getInt("id") + " " + rs.getString("name"));
        }
    }
}''', "java", "INSERT, UPDATE, DELETE and SELECT with one prepared statement each"))

    o.append(sec("5.4", "CallableStatement: running stored procedures"))
    o.append(p("A <span class='mono'>CallableStatement</span> extends "
               "<span class='mono'>PreparedStatement</span> and adds support for <b>both input and output "
               "parameters</b>. It represents a <b>stored procedure</b>: a subroutine stored in the database and "
               "used by applications to access data."))
    o.append(box("def", "Definition",
                 "<p>A <b>stored procedure</b> is a subroutine used by applications to access data from a database. "
                 "Business logic can be kept in the database through stored procedures and functions, which makes "
                 "performance better because they are <b>precompiled</b>.</p>"))
    o.append(p("Suppose you need the age of an employee from the date of birth. Instead of shipping the birth date "
               "to Java and computing there, you can create a function in the database that receives a date and "
               "returns the age. The logic runs next to the data, one round trip instead of many, and every "
               "application that calls it gets the same answer."))
    o.append(fig(fig_callable(),
                 "How a CallableStatement works. The call text names the procedure and its placeholders; IN values "
                 "are set like PreparedStatement parameters; OUT values must be registered before the call and read "
                 "after it."))
    o.append(code('''-- Step 1: create the procedure inside MySQL
CREATE PROCEDURE getStudentById(IN sid INT)
BEGIN
    SELECT id, name FROM student WHERE id = sid;
END''', "sql", "A stored procedure with one IN parameter"))
    o.append(code('''// Step 2: call it from Java
CallableStatement cs = con.prepareCall("{call getStudentById(?)}");
cs.setInt(1, 3);
ResultSet rs = cs.executeQuery();
while (rs.next()) {
    System.out.println("ID: " + rs.getInt("id"));
    System.out.println("Name: " + rs.getString("name"));
}''', "java", "Calling the procedure — note the JDBC escape syntax {call ...}"))
    o.append(code('''-- A procedure with an OUT parameter
CREATE PROCEDURE studentCount(OUT total INT)
BEGIN
    SELECT COUNT(*) INTO total FROM student;
END''', "sql", "A procedure that returns a value through an OUT parameter"))
    o.append(code('''CallableStatement cs = con.prepareCall("{call studentCount(?)}");
cs.registerOutParameter(1, Types.INTEGER);   // must come before execute
cs.execute();
int count = cs.getInt(1);                    // read after execute
System.out.println("Students: " + count);''', "java", "Registering and reading an OUT parameter"))
    o.append(box("mistake", "Common mistake",
                 "<p>Forgetting <span class='mono'>registerOutParameter()</span>, or calling it after "
                 "<span class='mono'>execute()</span>. The driver must know the OUT type <i>before</i> the call is "
                 "sent, because that information is part of the request.</p>"))

    o.append(sec("5.5", "Stored procedures versus functions"))
    o.append(p("Both live in the database and both are precompiled, so students often treat them as synonyms. The "
               "lecture material distinguishes them by purpose, return value and parameter direction."))
    o.append(tbl("Difference between stored procedures and functions",
                 ["Stored procedure", "Function"],
                 [["Used to perform business logic", "Used to perform calculation"],
                  ["Must not have a return type", "Must have a return type"],
                  ["May return 0 or more values", "May return only one value"],
                  ["A function can be called from a procedure", "A procedure cannot be called from a function"],
                  ["Supports input and output parameters", "Supports only input parameters"],
                  ["Exception handling with try/catch can be used", "Exception handling with try/catch cannot be used in user-defined functions"]],
                 ["50%", "50%"], firstcol=False))
    o.append(box("trick", "Memory trick",
                 "<p><b>Functions compute, procedures do.</b> A function must hand back exactly one value (that is "
                 "why it can be used inside a SELECT); a procedure is a script that may change data and report "
                 "through OUT parameters.</p>"))

    o.append(sec("5.6", "Choosing between the three"))
    o.append(tbl("Statement compared with PreparedStatement and CallableStatement",
                 ["Feature", "Statement", "PreparedStatement", "CallableStatement"],
                 [["Purpose", "Execute simple SQL queries", "Execute precompiled SQL queries", "Execute stored procedures"],
                  ["Query type", "Dynamic (built at run time)", "Precompiled (faster execution)", "Calls database procedures"],
                  ["Parameters", "Not supported", "Supported using <code>?</code> placeholders", "Supported (IN, OUT, INOUT)"],
                  ["Performance", "Slower — compiled every time", "Faster — compiled once", "Depends on the procedure"],
                  ["Security", "Vulnerable to SQL injection", "Prevents SQL injection", "Secure — uses parameters"],
                  ["Reusability", "Low", "High", "High"],
                  ["Example call", "<code>stmt.executeQuery(\"SELECT * FROM users\")</code>", "<code>pstmt.setInt(1, id)</code>", "<code>cstmt.registerOutParameter(...)</code>"]],
                 ["16%", "26%", "29%", "29%"]))
    o.append(p("The decision rule is short enough to memorize: <b>no parameters → Statement; parameters → "
               "PreparedStatement; stored procedure → CallableStatement</b>. In professional code the middle column "
               "covers almost everything, because any query that takes user input is a query with parameters."))

    o.append(sec("5.7", "Summary"))
    o.append(ul(["Statement sends SQL text as-is; it is a factory of ResultSet.",
                 "PreparedStatement is precompiled and parameterized with <span class='mono'>?</span> — faster and "
                 "injection-safe.",
                 "CallableStatement calls stored procedures and supports IN, OUT and INOUT parameters.",
                 "The hierarchy is Statement → PreparedStatement → CallableStatement.",
                 "Procedures do work and may return nothing; functions compute and must return one value."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Which interface would you use for a login query, and why? "
                 "<b>2.</b> What does <span class='mono'>executeUpdate()</span> return? "
                 "<b>3.</b> Name the method that creates a CallableStatement.</p>"
                 "<p class='small'><i>Answers:</i> (1) PreparedStatement — the query has parameters and must not be "
                 "vulnerable to injection. (2) The number of rows affected (0 for DDL). (3) "
                 "<span class='mono'>Connection.prepareCall(\"{call proc(?)} \")</span>.</p>"))
    o.append(recap("Part 5 recap", [
        ["<b>Hierarchy</b>", "Statement → PreparedStatement → CallableStatement; each adds capability."],
        ["<b>Statement</b>", "Static SQL, no parameters, compiled every time. Use for DDL and one-off queries."],
        ["<b>PreparedStatement</b>", "Compiled once, <span class='mono'>?</span> placeholders, typed setters, safe from injection. The default choice."],
        ["<b>CallableStatement</b>", "Calls a stored procedure with <span class='mono'>{call p(?,?)}</span>; IN values set as usual, OUT values registered and read."],
        ["<b>When to use which</b>", "No input → Statement; input → PreparedStatement; logic in the database → CallableStatement."],
    ], terms=["Statement", "PreparedStatement", "CallableStatement", "? placeholder", "stored procedure", "precompiled query", "IN parameter", "OUT parameter", "setInt()"], practice=[
        "Give the statement hierarchy in one line.",
        "Why is a PreparedStatement immune to the classic injection?",
        "What must be called before reading an OUT parameter, and why?",
    ], trap="Sending user input through a <span class='mono'>Statement</span>. That one habit is the injection hole."))
    return "".join(o)
