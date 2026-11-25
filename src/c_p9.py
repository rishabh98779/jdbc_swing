"""PART 9 — Introduction to Spring JDBC."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_side_by_side():
    b = []
    b.append(rect(10, 10, 310, 268, "#fbfcfd", RED, 2))
    b.append(rect(10, 10, 310, 26, RED, RED, 2))
    b.append(txt(165, 28, "PLAIN JDBC", 8.4, WHITE, 700, "middle", ls="0.1em"))
    plain = [("Class.forName(driver)", "load"),
             ("DriverManager.getConnection(...)", "connect"),
             ("con.createStatement()", "prepare"),
             ("stmt.executeQuery(sql)", "execute"),
             ("while (rs.next()) { map }", "map by hand"),
             ("rs.close(); stmt.close(); con.close()", "close"),
             ("catch (SQLException e)", "handle")]
    for i, (code_, role) in enumerate(plain):
        y = 48 + i * 32
        b.append(rect(20, y, 290, 26, WHITE, LINE, 2))
        b.append(txt(28, y + 17, code_, 7.6, INK, 400, "start", MONO))
        b.append(txt(302, y + 17, role, 7.0, RED, 700, "end"))
    b.append(txt(165, 270, "you write every line, every time", 7.8, RED, 700, "middle"))

    b.append(rect(340, 10, 310, 268, "#fbfcfd", TEAL, 2))
    b.append(rect(340, 10, 310, 26, TEAL, TEAL, 2))
    b.append(txt(495, 28, "SPRING JDBC", 8.4, WHITE, 700, "middle", ls="0.1em"))
    spring = [("jdbcTemplate.update(sql, args)", "insert / update / delete"),
              ("jdbcTemplate.queryForObject(sql, RowMapper, args)", "one row"),
              ("jdbcTemplate.query(sql, RowMapper, args)", "many rows"),
              ("jdbcTemplate.execute(sql)", "DDL")]
    for i, (code_, role) in enumerate(spring):
        y = 48 + i * 40
        b.append(rect(350, y, 290, 34, WHITE, LINE, 2))
        b.append(txtw(358, y + 14, code_, 274, 7.6, INK, 400, "start", family=MONO)[0])
        b.append(txt(632, y + 30, role, 7.0, TEAL, 700, "end"))
    b.append(rect(350, 214, 290, 46, TEAL_L, TEAL, 2))
    b.append(txtw(495, 232, "connection, statement, ResultSet, exception translation and close are handled "
                            "by the template", 280, 7.6, TEAL, 600)[0])
    b.append(txt(495, 270, "you write one line, the template writes the rest", 7.8, TEAL, 700, "middle"))
    return svg(660, 284, "".join(b))


def fig_stack():
    b = []
    b.append(node(210, 10, 240, 34, "your DAO / service class", None, NAVY, NAVY, WHITE, 8.8, 700))
    b.append(node(210, 58, 240, 34, "JdbcTemplate", None, TEAL, TEAL, WHITE, 9.0, 700))
    b.append(node(210, 106, 240, 34, "DataSource (DriverManagerDataSource)", None, ORANGE_L, ORANGE, ORANGE, 7.8, 700))
    b.append(node(210, 154, 240, 34, "JDBC driver", None, WHITE, ORANGE, ORANGE, 8.8, 700))
    b.append(node(210, 202, 240, 34, "database", None, NAVY2, NAVY2, WHITE, 8.8, 700))
    for y in (44, 92, 140, 188):
        b.append(arrow(330, y, 330, y + 12, NAVY3, 1.2, hs=5.4))
    b.append(txt(470, 75, "translates JDBC into Spring's", 7.6, MUTED, 400))
    b.append(txt(470, 86, "DataAccessException hierarchy", 7.6, MUTED, 400))
    b.append(txt(470, 123, "supplies Connection objects", 7.6, MUTED, 400))
    b.append(txt(470, 134, "from the configured URL and credentials", 7.6, MUTED, 400))
    b.append(txt(470, 171, "implements the interfaces", 7.6, MUTED, 400))
    b.append(txt(470, 182, "vendor-specific protocol", 7.6, MUTED, 400))
    b.append(txt(470, 219, "stores the rows", 7.6, MUTED, 400))
    return svg(660, 246, "".join(b))


def html():
    o = []
    o.append(part(9, "Introduction to Spring JDBC",
                  "Same SQL, a fraction of the code: what Spring adds, what it hides, and when plain JDBC "
                  "is still the better choice.", art_icon=9))

    o.append(sec("9.1", "Why Spring JDBC exists"))
    o.append(p("Part 7 ended with a list of problems. Spring JDBC is the framework's answer to them, and it answers "
               "them without hiding SQL: you still write the query, but you no longer write the plumbing around it."))
    o.append(box("def", "Definition",
                 "<p><b>Spring JDBC</b> is the part of the Spring Framework that simplifies database operations by "
                 "removing boilerplate JDBC code. It provides a clean and efficient way to interact with relational "
                 "databases using SQL queries, and it handles connection management, exception handling and resource "
                 "cleanup automatically. It internally uses the JDBC API, but eliminates a lot of the problems of "
                 "that API.</p>"))
    o.append(p("The problems it removes are exactly the four in the lecture material: the code written before and "
               "after every query (creating the connection, statement, closing the ResultSet and connection); the "
               "exception-handling code inside the database logic; the transaction handling; and the repetition of "
               "all of this from one database operation to the next."))
    o.append(fig(fig_side_by_side(),
                 "The same database work, written twice. On the left, seven lines of plumbing around one query. On "
                 "the right, one call — the template does everything the left column shows."))

    o.append(sec("9.2", "The three ideas behind it"))
    o.append(ol(["<b>A template</b> — a class that owns the repetitive part (open, execute, map, close) and accepts "
                 "the variable part (the SQL and the parameters) as arguments. "
                 "<span class='mono'>JdbcTemplate</span> is that class.",
                 "<b>A DataSource</b> — an object that knows how to supply a "
                 "<span class='mono'>Connection</span>. The template asks the DataSource for a connection and gives "
                 "it back; it never builds one itself. That indirection is what later allows connection pooling.",
                 "<b>Exception translation</b> — every <span class='mono'>SQLException</span> is converted into a "
                 "runtime exception from the <span class='mono'>org.springframework.dao</span> package, so the "
                 "calling code can choose to catch it or not, and never has to read vendor error codes."]))
    o.append(fig(fig_stack(),
                 "The Spring JDBC stack. Each layer has exactly one job, and each one is replaceable — which is why "
                 "a test can substitute a different DataSource without touching the DAO."))

    o.append(sec("9.3", "JDBC compared with Spring JDBC"))
    o.append(p("The lecture material gives six points of difference. They are ordered from “what it is” to “when to "
               "choose which”, and they make a complete long-answer answer in that order."))
    o.append(tbl("Difference between JDBC and Spring JDBC",
                 ["#", "Point of difference"],
                 [["1", "Spring JDBC provides a simplified and effective way to interact with relational databases in "
                        "Java applications. Plain JDBC represents the standard Java API for database access, without "
                        "the additional features that Spring offers."],
                  ["2", "Spring JDBC handles resource management (such as connections) automatically, while plain JDBC "
                        "requires manual management."],
                  ["3", "Spring JDBC provides a consistent error-handling mechanism through its exception hierarchy, "
                        "which is more comprehensive than the <span class='mono'>SQLException</span> handling of plain "
                        "JDBC."],
                  ["4", "Spring JDBC supports the <b>template design pattern</b>, which reduces boilerplate code "
                        "significantly compared with plain JDBC."],
                  ["5", "Use Spring JDBC for a more manageable and less error-prone implementation when interacting "
                        "with databases."],
                  ["6", "Opt for plain JDBC where you require minimal abstraction and want to fully control database "
                        "interactions."]],
                 ["6%", "94%"], firstcol=False))
    o.append(tbl("The same differences as a comparison table",
                 ["Criterion", "Plain JDBC", "Spring JDBC"],
                 [["Level", "Standard Java API", "Framework built on that API"],
                  ["Connection handling", "You open and close it", "Template obtains and releases it"],
                  ["Resource cleanup", "Manual (finally or try-with-resources)", "Automatic"],
                  ["Exceptions", "Checked <code>SQLException</code> everywhere",
                   "Runtime <code>DataAccessException</code> hierarchy"],
                  ["Boilerplate", "Repeated in every method", "Removed by the template pattern"],
                  ["Row mapping", "Hand-written getters", "<code>RowMapper</code>"],
                  ["Best for", "Learning, tiny tools, full control", "Real applications"]],
                 ["24%", "38%", "38%"]))
    o.append(box("imp", "Important",
                 "<p>Spring JDBC does not replace JDBC — it <b>wraps</b> it. "
                 "<span class='mono'>JdbcTemplate</span> calls <span class='mono'>Connection</span>, "
                 "<span class='mono'>PreparedStatement</span> and <span class='mono'>ResultSet</span> exactly as you "
                 "did in Part 6. Every JDBC concept you learned is still underneath, which is why it comes first in "
                 "the syllabus.</p>"))

    o.append(sec("9.4", "What stays the same"))
    o.append(p("Students often assume that Spring JDBC hides SQL. It does not. You still write:"))
    o.append(ul(["the SQL text, including <span class='mono'>?</span> placeholders;",
                 "the parameter values, passed as varargs or an <span class='mono'>Object[]</span>;",
                 "the mapping from a row to an object, either as a <span class='mono'>RowMapper</span> or by asking "
                 "for a single result.",
                 "the transaction boundary, when more than one statement must succeed together."]))
    o.append(p("What changes is who writes the try/finally, who converts exceptions, and who remembers to close the "
               "ResultSet. That is a large fraction of the lines, and almost all of the defects."))
    o.append(box("tip", "Exam tip",
                 "<p>“Difference between JDBC and Spring JDBC” is a guaranteed question. Write the six numbered "
                 "points, then draw the stack figure. The six points alone are worth full marks; the figure "
                 "convinces the examiner that you know where the template sits.</p>"))

    o.append(sec("9.5", "Summary"))
    o.append(ul(["Spring JDBC removes boilerplate — connection handling, exception handling, resource cleanup and "
                 "repetition.",
                 "It works through a template class (<span class='mono'>JdbcTemplate</span>) and a DataSource.",
                 "Errors arrive as runtime <span class='mono'>DataAccessException</span> subtypes instead of checked "
                 "<span class='mono'>SQLException</span>.",
                 "SQL itself is unchanged, and JDBC is still underneath.",
                 "Plain JDBC remains the right choice when you want minimal abstraction and full control."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Name the two Spring objects that make Spring JDBC work. "
                 "<b>2.</b> What kind of exception does Spring JDBC throw? "
                 "<b>3.</b> Give one situation in which plain JDBC is preferable.</p>"
                 "<p class='small'><i>Answers:</i> (1) <span class='mono'>JdbcTemplate</span> and a "
                 "<span class='mono'>DataSource</span> (for example "
                 "<span class='mono'>DriverManagerDataSource</span>). (2) A runtime exception from the "
                 "<span class='mono'>org.springframework.dao</span> hierarchy, such as "
                 "<span class='mono'>DataAccessException</span>. (3) A tiny utility where you want minimal "
                 "abstraction and complete control over every JDBC call.</p>"))
    o.append(recap("Part 9 recap", [
        ["<b>Why Spring JDBC</b>", "Removes the seven-step boilerplate, closes resources, translates SQLException into a runtime DataAccessException."],
        ["<b>What JDBC keeps</b>", "The same driver, URL, SQL and ResultSet semantics — Spring wraps, it does not replace."],
        ["<b>Core pieces</b>", "<span class='mono'>JdbcTemplate</span> for the work, <span class='mono'>DataSource</span> for the connections, <span class='mono'>RowMapper</span> for the mapping."],
        ["<b>Service layer</b>", "The DAO calls the template; the template calls the DataSource; nothing else knows about SQL."],
        ["<b>Trade-off</b>", "Less code and better error handling, at the cost of one dependency and one indirection layer."],
    ], terms=["Spring JDBC", "JdbcTemplate", "boilerplate", "DataAccessException", "DAO", "RowMapper", "dependency injection", "DataSource", "unchecked exception"], practice=[
        "Give six differences between JDBC and Spring JDBC.",
        "What must a JdbcTemplate be given before it can run anything?",
        "Which exception does Spring throw in place of checked SQLException?",
    ], trap="Believing Spring JDBC removes SQL. It removes boilerplate; the SQL and its tuning stay yours."))
    return "".join(o)
