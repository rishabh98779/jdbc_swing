"""PART 13 — Spring JdbcTemplate."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_interaction():
    b = []
    b.append(txt(12, 18, "WHO CALLS WHOM FOR ONE UPDATE", 8.4, MUTED, 700, ls="0.1em"))
    lanes = [70, 240, 410, 580]
    names = ["DAO", "JdbcTemplate", "DataSource", "Driver / DB"]
    b.append(rect(12, 28, 636, 24, GREY, LINE, 2))
    for i, n in enumerate(names):
        b.append(txt(lanes[i], 44, n, 8.2, NAVY, 700, "middle", ls="0.04em"))
    for x in lanes:
        b.append(line(x, 54, x, 216, LINE, 0.8, "3 3"))
    msgs = [(76, "update(sql, args)", 0, 1, "call"),
            (100, "getConnection()", 1, 2, "call"),
            (118, "Connection", 2, 1, "ret"),
            (140, "prepareStatement + bind + execute", 1, 3, "call"),
            (162, "rows affected", 3, 1, "ret"),
            (184, "close the connection", 1, 2, "call"),
            (204, "int (1 row updated)", 1, 0, "ret")]
    for y, label, a, bb, kind in msgs:
        x1, x2 = lanes[a], lanes[bb]
        if kind == "call":
            b.append(arrow(x1 + 2, y, x2 - 2, y, NAVY3, 1.1, hs=5.4))
            b.append(txt((x1 + x2) / 2, y - 6, label, 7.6, INK, 400, "middle", MONO))
        else:
            b.append(arrow(x1 - 2, y, x2 + 2, y, TEAL, 1.0, hs=5.0, dash="4 2"))
            b.append(txt((x1 + x2) / 2, y - 6, label, 7.4, TEAL, 600, "middle"))
    b.append(txt(330, 236, "The DAO writes one line; the template performs six JDBC steps and hands back a plain int.",
                 7.8, MUTED, 400, "middle"))
    return svg(660, 244, "".join(b))


def fig_methods_map():
    b = []
    b.append(txt(12, 18, "FOUR INTENTS, FOUR METHODS", 8.4, MUTED, 700, ls="0.1em"))
    rows = [("I want to change data", "update(sql, args...)", "returns int: rows affected", ORANGE),
            ("I want exactly one row", "queryForObject(sql, RowMapper, args...)", "returns T", TEAL),
            ("I want many rows", "query(sql, RowMapper, args...)", "returns List<T>", TEAL),
            ("I want to run DDL", "execute(sql)", "returns void", NAVY2)]
    y = 34
    for intent, meth, ret, col in rows:
        b.append(rect(12, y, 200, 42, "#fbfcfd", LINE, 2))
        b.append(txt(112, y + 26, intent, 8.2, INK, 600, "middle"))
        b.append(arrow(214, y + 21, 232, y + 21, col, 1.2, hs=5.2))
        b.append(rect(234, y, 250, 42, col, col, 2))
        b.append(txtw(359, y + 18, meth, 240, 7.6, WHITE, 700, char_w=0.55)[0])
        b.append(arrow(486, y + 21, 504, y + 21, col, 1.2, hs=5.2))
        b.append(rect(506, y, 142, 42, "#fbfcfd", col, 2))
        b.append(txtw(577, y + 18, ret, 134, 7.4, MUTED, 400)[0])
        y += 50
    return svg(660, y + 4, "".join(b))


def html():
    o = []
    o.append(part(13, "Spring JdbcTemplate",
                  "The central class of Spring's JDBC support: what it owns, what you own, and the four "
                  "methods that cover almost every call.", art_icon=13))

    o.append(sec("13.1", "What JdbcTemplate is"))
    o.append(p("<span class='mono'>org.springframework.jdbc.core.JdbcTemplate</span> is the central class in the JDBC "
               "core package, and the central class in Spring's JDBC support. It takes care of the creation and "
               "release of resources — creating and closing the connection object, the statement and the result set "
               "— so it does not lead to any problem if you forget to close the connection. It handles exceptions "
               "and provides informative exception messages through the exception classes defined in "
               "<span class='mono'>org.springframework.dao</span>. It performs every database operation you need: "
               "insertion, updation, deletion and retrieval of data."))
    o.append(box("def", "Definition",
                 "<p><b>JdbcTemplate</b> is the central class of the Spring JDBC core package. It simplifies the use "
                 "of JDBC and helps avoid common errors: it handles resource acquisition and release, participates in "
                 "exception translation into the <span class='mono'>DataAccessException</span> hierarchy, and exposes "
                 "one-line methods for query, update and DDL execution.</p>"))
    o.append(code('''public class JdbcTemplate extends JdbcAccessor implements JdbcOperations''',
                 "java", "The class declaration, as given in the lecture material"))
    o.append(p("The declaration repays one minute of reading. <span class='mono'>JdbcAccessor</span> holds the "
               "DataSource and provides <span class='mono'>getConnection()</span>; "
               "<span class='mono'>JdbcOperations</span> is the interface with the query/update methods, which is why "
               "a DAO can depend on the interface rather than the class. "
               "<span class='mono'>SimpleJdbcTemplate</span>, mentioned in the slides, wraps "
               "<span class='mono'>JdbcTemplate</span> and provides an update method that accepts an arbitrary number "
               "of arguments; it has been deprecated since Spring 3.1 because varargs were added to "
               "<span class='mono'>JdbcTemplate</span> itself."))
    o.append(box("imp", "Important",
                 "<p>There is a property named <b>datasource</b> in <span class='mono'>JdbcTemplate</span>. The "
                 "template cannot open a connection by itself; it must be given a "
                 "<span class='mono'>DataSource</span>, which is the subject of Part 14. No DataSource, no "
                 "JdbcTemplate.</p>"))

    o.append(sec("13.2", "Using it: two steps"))
    o.append(ol(["Create a <span class='mono'>JdbcTemplate</span> object using a configured "
                 "<span class='mono'>DataSource</span>.",
                 "Use the <span class='mono'>JdbcTemplate</span> object's methods to perform database operations."]))
    o.append(code('''// Step 1: a template built on a configured DataSource
JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);

// Step 2: one method call per database operation
int rows = jdbcTemplate.update(
        "INSERT INTO STUDENT (id, name, country) VALUES (?, ?, ?)",
        101, "Rajesh", "India");''', "java", "The two usage steps, verbatim from the lecture"))
    o.append(p("In a Spring Boot application you write neither line: "
               "<span class='mono'>@EnableAutoConfiguration</span> sees "
               "<span class='mono'>spring-boot-starter-jdbc</span> on the classpath with a configured "
               "<span class='mono'>spring.datasource.*</span> URL, creates both the "
               "<span class='mono'>DataSource</span> and the <span class='mono'>JdbcTemplate</span>, and injects the "
               "template into your DAO. The two steps above are what the framework does for you."))

    o.append(sec("13.3", "The methods"))
    o.append(tbl("Methods of the JdbcTemplate class",
                 ["Method", "Description"],
                 [["<code>public int update(String query)</code>", "Used to insert, update and delete records"],
                  ["<code>public int update(String query, Object... args)</code>",
                   "Same, using a PreparedStatement with the given arguments"],
                  ["<code>public void execute(String query)</code>", "Used to execute a DDL query"],
                  ["<code>public &lt;T&gt; T execute(String sql, PreparedStatementCallback&lt;T&gt; action)</code>",
                   "Executes the query using a PreparedStatement callback"],
                  ["<code>public &lt;T&gt; T query(String sql, ResultSetExtractor&lt;T&gt; rse)</code>",
                   "Fetches records using a ResultSetExtractor"],
                  ["<code>public &lt;T&gt; List&lt;T&gt; query(String sql, RowMapper&lt;T&gt; rse)</code>",
                   "Fetches records using a RowMapper"],
                  ["<code>public &lt;T&gt; T queryForObject(String sql, RowMapper&lt;T&gt; mapper, Object... args)</code>",
                   "Fetches exactly one row and maps it"],
                  ["<code>public int queryForObject(String sql, Class&lt;Integer&gt; type)</code>",
                   "Fetches a single scalar value, such as COUNT(*)"]],
                 ["48%", "52%"]))
    o.append(fig(fig_methods_map(),
                 "The four methods that cover everyday work, chosen by intent rather than by signature. If the "
                 "answer is one row, use queryForObject; if it is many, use query; if nothing comes back, use update."))
    o.append(box("trick", "Memory trick",
                 "<p><b>update = change, query = read, execute = DDL, queryForObject = exactly one.</b> "
                 "If you remember only those four, you can write any DAO in this unit.</p>"))

    o.append(sec("13.4", "RowMapper: from row to object"))
    o.append(p("A <span class='mono'>RowMapper</span> is the one thing you must still write yourself, because only "
               "you know which object a row should become. It is a functional interface with a single method, "
               "<span class='mono'>mapRow(ResultSet rs, int rowNum)</span>, called once per row."))
    o.append(code('''public class StudentMapper implements RowMapper<Student> {
    @Override
    public Student mapRow(ResultSet rs, int rowNum) throws SQLException {
        Student s = new Student();
        s.setId(rs.getInt("id"));
        s.setName(rs.getString("name"));
        s.setCountry(rs.getString("country"));
        return s;
    }
}''', "java", "A RowMapper for the Student table"))
    o.append(code('''public int addStudent(int id, String name, String country) {
    return jdbcTemplate.update(
        "INSERT INTO STUDENT (id, name, country) VALUES (?, ?, ?)",
        id, name, country);
}

public List<Student> listStudents() {
    String selectQuery = "select * from Student";
    List<Student> students = jdbcTemplateObject.query(selectQuery, new StudentMapper());
    return students;
}''', "java", "Inserting and fetching, exactly as in the lecture material"))
    o.append(p("Notice what is <i>absent</i> from those two methods: no connection, no statement, no try/catch, no "
               "finally, no close. The template obtained a connection from its DataSource, created a "
               "PreparedStatement, bound three arguments, executed it, translated any exception, and closed "
               "everything — including on the failure path. That is the boilerplate of Part 7, deleted."))

    o.append(sec("13.5", "A complete DAO"))
    o.append(p("The class below is the pattern the lecture material builds in three pieces — an interface, a "
               "mapper and an implementation — assembled into one runnable example. It is what a Spring project "
               "actually contains."))
    o.append(code('''package com.example.dao;

import com.example.model.Student;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import javax.sql.DataSource;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

public class StudentDao {

    private final JdbcTemplate jdbcTemplate;

    // the template arrives through the constructor - no new JdbcTemplate() here
    public StudentDao(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    private static final RowMapper<Student> MAPPER = (rs, rowNum) -> {
        Student s = new Student();
        s.setId(rs.getInt("id"));
        s.setName(rs.getString("name"));
        s.setCountry(rs.getString("country"));
        return s;
    };

    public int create(int id, String name, String country) {
        return jdbcTemplate.update(
            "INSERT INTO STUDENT (id, name, country) VALUES (?, ?, ?)",
            id, name, country);
    }

    public Student findById(int id) {
        return jdbcTemplate.queryForObject(
            "SELECT id, name, country FROM STUDENT WHERE id = ?", MAPPER, id);
    }

    public List<Student> findAll() {
        return jdbcTemplate.query("SELECT id, name, country FROM STUDENT", MAPPER);
    }

    public int updateName(int id, String name) {
        return jdbcTemplate.update(
            "UPDATE STUDENT SET name = ? WHERE id = ?", name, id);
    }

    public int delete(int id) {
        return jdbcTemplate.update("DELETE FROM STUDENT WHERE id = ?", id);
    }

    public int count() {
        Integer n = jdbcTemplate.queryForObject(
            "SELECT COUNT(*) FROM STUDENT", Integer.class);
        return n == null ? 0 : n;
    }
}''', "java", "A DAO with CRUD, a RowMapper and a scalar query"))
    o.append(fig(fig_interaction(),
                 "One update, traced through the stack. The DAO's single call triggers six JDBC steps, all of "
                 "which the template performs and none of which the DAO sees."))

    o.append(sec("13.6", "Errors you will actually meet"))
    o.append(tbl("Common JdbcTemplate errors and their causes",
                 ["Exception", "Cause", "Fix"],
                 [["<code>EmptyResultDataAccessException</code>",
                   "queryForObject() found no row", "Use query() and an empty-list check if a row may be absent"],
                  ["<code>IncorrectResultSizeDataAccessException</code>",
                   "queryForObject() found more than one row", "Make the WHERE clause return one row, or use query()"],
                  ["<code>BadSqlGrammarException</code>", "The SQL is wrong, or the table does not exist",
                   "Check the table name and the column list"],
                  ["<code>DataAccessResourceFailureException</code>", "The database is unreachable",
                   "Check the URL, the port and that the server is running"],
                  ["<code>CannotGetJdbcConnectionException</code>", "No DataSource, or wrong credentials",
                   "Configure spring.datasource.* correctly"]],
                 ["36%", "28%", "36%"]))
    o.append(box("tip", "Exam tip",
                 "<p>Spring's exceptions are <b>unchecked</b>. A DAO does not declare "
                 "<span class='mono'>throws SQLException</span>, and the caller is not forced to catch anything. "
                 "That is a deliberate design decision: most database errors cannot be fixed where they occur, so "
                 "forcing every layer to declare them adds noise without adding safety.</p>"))

    o.append(sec("13.7", "Summary"))
    o.append(ul(["JdbcTemplate is the central class of Spring's JDBC support; it owns resource handling and "
                 "exception translation.",
                 "Usage is two steps: create it with a DataSource, then call its methods.",
                 "update() changes data, query() reads many rows, queryForObject() reads one, execute() runs DDL.",
                 "A RowMapper converts one row into one object and is the only code you must supply.",
                 "It is built on plain JDBC — every concept from Parts 4 to 6 is still underneath."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Which property must a JdbcTemplate be given before it can work? "
                 "<b>2.</b> Which method executes a DDL statement? "
                 "<b>3.</b> What does queryForObject() throw if it finds no row?</p>"
                 "<p class='small'><i>Answers:</i> (1) A DataSource. (2) <span class='mono'>execute(String sql)</span>. "
                 "(3) <span class='mono'>EmptyResultDataAccessException</span>.</p>"))
    o.append(recap("Part 13 recap", [
        ["<b>JdbcTemplate</b>", "The central class of Spring's JDBC support; it owns resource handling and "
                                "exception translation."],
        ["<b>Two steps</b>", "Create it with a DataSource, then call its methods."],
        ["<b>update()</b>", "INSERT, UPDATE, DELETE; returns the number of rows affected."],
        ["<b>query()</b>", "SELECT; returns a <span class='mono'>List&lt;T&gt;</span> mapped by a RowMapper."],
        ["<b>queryForObject()</b>", "SELECT exactly one row or one scalar; throws if the count is not one."],
        ["<b>execute()</b>", "DDL."],
        ["<b>RowMapper</b>", "One method, <span class='mono'>mapRow(rs, rowNum)</span>, called once per row."],
        ["<b>Errors</b>", "Runtime <span class='mono'>DataAccessException</span> subtypes — nothing to declare."],
        ["<b>Underneath</b>", "Plain JDBC: Connection, PreparedStatement, ResultSet, exactly as in Parts 4 to 6."],
    ], terms=["JdbcTemplate.update()", "queryForObject()", "query()", "RowMapper", "batchUpdate()", "JdbcTemplate bean", "auto-configuration", "@Autowired", "exception translation"], practice=[
        "Name four JdbcTemplate methods and what each returns.",
        "Which property of the template must be set, and with what?",
        "Where did the try/catch go when you moved to JdbcTemplate?",
    ], trap="Assuming <span class='mono'>JdbcTemplate</span> pools connections. Pooling belongs to the DataSource."))
    return "".join(o)
