"""PART 16 — Complete Practical Programs."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_program_map():
    b = []
    b.append(txt(12, 18, "THE NINE PROGRAMS AND WHAT EACH ONE TEACHES", 8.4, MUTED, 700, ls="0.1em"))
    rows = [("16.1", "Connect and SELECT", "the seven steps, ResultSet loop", TEAL),
            ("16.2", "Insert a row", "PreparedStatement setters", TEAL),
            ("16.3", "Update a row", "executeUpdate() return value", TEAL),
            ("16.4", "Delete a row", "parameter in a WHERE clause", TEAL),
            ("16.5", "Stored procedure", "CallableStatement, OUT parameter", ORANGE),
            ("16.6", "ResultSet metadata", "schema discovery at run time", ORANGE),
            ("16.7", "Spring JDBC DAO", "JdbcTemplate, RowMapper, DataSource", NAVY2),
            ("16.8", "XSLT in Java", "TransformerFactory, DOMSource", NAVY2),
            ("16.9", "Swing login form", "GUI plus JDBC: the unit title, made real", RED)]
    for i, (num, title, teaches, col) in enumerate(rows):
        y = 34 + i * 26
        b.append(rect(12, y, 636, 21, "#fbfcfd", LINE, 1.5))
        b.append(txt(22, y + 15, num, 7.8, col, 700, "start", MONO))
        b.append(txt(62, y + 15, title, 8.0, NAVY, 700, "start"))
        b.append(arrow(232, y + 11, 250, y + 11, col, 1.0, hs=4.4))
        b.append(txt(258, y + 15, teaches, 7.6, MUTED, 400, "start"))
    return svg(660, 34 + 9 * 26 + 6, "".join(b))


def html():
    o = []
    o.append(part(16, "Complete Practical Programs",
                  "Nine programs, each one complete, compilable and annotated line by line — the source "
                  "for every laboratory record and viva demonstration.", art_icon=16))

    o.append(p("Every program in this part uses the same database and the same table, so that they can be run in "
               "order and each one can be verified against the previous. Create the table once, with the SQL below, "
               "and keep the credentials in one place."))
    o.append(code('''CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE student (
    id     INT PRIMARY KEY,
    name   VARCHAR(60) NOT NULL,
    city   VARCHAR(60),
    marks  INT
);

INSERT INTO student VALUES (101, 'Rajesh', 'Guntur', 88);
INSERT INTO student VALUES (102, 'Simran', 'Patiala', 91);''', "sql", "The schema used by every program in this part", label=""))
    o.append(fig(fig_program_map(),
                 "A map of the nine programs and the single idea each one demonstrates. Programs 16.1 to 16.4 are "
                 "the CRUD core; 16.5 and 16.6 add procedures and metadata; 16.7 to 16.9 move to Spring, XML and the GUI."))
    o.append(box("imp", "Important",
                 "<p>Before running any of them, the MySQL driver JAR must be on the classpath. With Maven that is "
                 "one dependency (Part 12); with a plain <span class='mono'>javac</span> it is "
                 "<span class='mono'>-cp \"lib/mysql-connector-j-9.0.0.jar\"</span>. Without it, every program fails "
                 "at the same line with <span class='mono'>ClassNotFoundException</span>.</p>"))

    o.append(sec("16.1", "Connecting and reading rows"))
    o.append(code('''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class StudentSelect {
    private static final String URL  = "jdbc:mysql://localhost:3306/mydb";
    private static final String USER = "root";
    private static final String PASS = "your_password";

    public static void main(String[] args) {
        // 1. load the driver (JDBC 4+ would also do this automatically)
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.out.println("Driver not on the classpath: " + e.getMessage());
            return;
        }

        // 2-7. connect, execute, process, close
        String sql = "SELECT id, name, city, marks FROM student ORDER BY id";
        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            System.out.printf("%-6s %-12s %-12s %s%n", "ID", "NAME", "CITY", "MARKS");
            while (rs.next()) {
                int id       = rs.getInt("id");
                String name  = rs.getString("name");
                String city  = rs.getString("city");
                int marks    = rs.getInt("marks");
                System.out.printf("%-6d %-12s %-12s %d%n", id, name, city, marks);
            }
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        }
    }
}''', "java", "The seven steps, with try-with-resources", label="PROGRAM 16.1"))
    o.append(raw_code('''ID     NAME         CITY         MARKS
101    Rajesh       Guntur       88
102    Simran       Patiala      91''', "Output"))
    o.append(mini("Line by line"))
    o.append(ul(["<b>URL, USER, PASS as constants</b> — one place to change, and no credentials buried inside a method.",
                 "<b><span class='mono'>Class.forName</span></b> throws <span class='mono'>ClassNotFoundException</span>; "
                 "catching it separately means a missing JAR produces a clear message instead of a generic database "
                 "error.",
                 "<b>The try-with-resources header</b> declares three resources. They are closed in reverse order — "
                 "ResultSet, then Statement, then Connection — even if the loop throws.",
                 "<b><span class='mono'>executeQuery</span></b> is correct because the SQL returns rows; "
                 "<span class='mono'>executeUpdate</span> here would throw an error.",
                 "<b><span class='mono'>while (rs.next())</span></b> both advances the cursor and tests for the end. "
                 "There is no need for a separate <span class='mono'>hasNext()</span> — JDBC does not have one.",
                 "<b>Getters by column name</b> read more clearly than by index, and they survive a change in the "
                 "SELECT list. The index form <span class='mono'>rs.getInt(1)</span> is faster, because no name lookup "
                 "happens."]))
    o.append(box("mistake", "Common mistake",
                 "<p>Printing <span class='mono'>rs.getString(\"marks\")</span> and then wondering why an empty value "
                 "appears for NULL marks. Use the getter that matches the SQL type, and test "
                 "<span class='mono'>rs.wasNull()</span> when the column is nullable.</p>"))

    o.append(sec("16.2", "Inserting a row"))
    o.append(code('''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentInsert {
    private static final String URL  = "jdbc:mysql://localhost:3306/mydb";
    private static final String USER = "root";
    private static final String PASS = "your_password";

    public static void main(String[] args) {
        String sql = "INSERT INTO student (id, name, city, marks) VALUES (?, ?, ?, ?)";

        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement ps = con.prepareStatement(sql)) {

            // row 1
            ps.setInt(1, 103);
            ps.setString(2, "Aman");
            ps.setString(3, "Delhi");
            ps.setInt(4, 75);
            int first = ps.executeUpdate();

            // row 2 - the same prepared statement, new values
            ps.setInt(1, 104);
            ps.setString(2, "Isha");
            ps.setString(3, "Chandigarh");
            ps.setInt(4, 82);
            int second = ps.executeUpdate();

            System.out.println("Inserted rows: " + (first + second));
        } catch (SQLException e) {
            System.out.println("Insert failed: " + e.getMessage());
        }
    }
}''', "java", "One prepared statement, executed twice", label="PROGRAM 16.2"))
    o.append(raw_code('''Inserted rows: 2''', "Output"))
    o.append(mini("Line by line"))
    o.append(ul(["The SQL contains four <span class='mono'>?</span> placeholders, so four setters are needed before "
                 "each execution. Parameter indexes are <b>1-based</b> and are counted left to right.",
                 "<span class='mono'>executeUpdate()</span> returns 1 for each successful INSERT — the number of rows "
                 "affected.",
                 "The second execution reuses the compiled statement. Only the bound values change, which is the "
                 "performance benefit described in Part 5.",
                 "Re-using a PreparedStatement without resetting every parameter is a classic bug: a forgotten "
                 "<span class='mono'>setInt(4, ...)</span> silently reuses the previous value."]))
    o.append(box("mistake", "Common mistake",
                 "<p>Forgetting to close the PreparedStatement when it is created outside a "
                 "<span class='mono'>try-with-resources</span> header. It holds a server-side cursor, and a few "
                 "hundred unclosed statements will exhaust the server's limit.</p>"))

    o.append(sec("16.3", "Updating a row"))
    o.append(code('''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentUpdate {
    private static final String URL  = "jdbc:mysql://localhost:3306/mydb";
    private static final String USER = "root";
    private static final String PASS = "your_password";

    public static void main(String[] args) {
        String sql = "UPDATE student SET marks = ? WHERE id = ?";

        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setInt(1, 95);      // new marks
            ps.setInt(2, 101);     // target student
            int rows = ps.executeUpdate();

            if (rows == 0) {
                System.out.println("No student with id 101");
            } else {
                System.out.println(rows + " row(s) updated");
            }
        } catch (SQLException e) {
            System.out.println("Update failed: " + e.getMessage());
        }
    }
}''', "java", "Checking the return value", label="PROGRAM 16.3"))
    o.append(raw_code('''1 row(s) updated''', "Output"))
    o.append(p("The <span class='mono'>rows == 0</span> test is the important line. An UPDATE that matches nothing is "
               "not an error — the database reports success with zero rows affected. Programs that assume success "
               "because no exception was thrown silently lose data. Always check the count."))

    o.append(sec("16.4", "Deleting a row"))
    o.append(code('''import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentDelete {
    private static final String URL  = "jdbc:mysql://localhost:3306/mydb";
    private static final String USER = "root";
    private static final String PASS = "your_password";

    public static void main(String[] args) {
        String sql = "DELETE FROM student WHERE id = ?";

        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setInt(1, 104);
            int rows = ps.executeUpdate();
            System.out.println(rows + " row(s) deleted");
        } catch (SQLException e) {
            System.out.println("Delete failed: " + e.getMessage());
        }
    }
}''', "java", "DELETE with a parameter", label="PROGRAM 16.4"))
    o.append(raw_code('''1 row(s) deleted''', "Output"))
    o.append(box("imp", "Important",
                 "<p>A DELETE without a WHERE clause deletes every row and returns the total, which is legal, fast "
                 "and usually a mistake. In an examination answer, show the parameterized form — it is both safer and "
                 "more professional.</p>"))

    o.append(sec("16.5", "Calling a stored procedure"))
    o.append(code('''-- run once in MySQL to create the procedure
DELIMITER //
CREATE PROCEDURE student_stats(IN sid INT, OUT sname VARCHAR(60), OUT smarks INT)
BEGIN
    SELECT name, marks INTO sname, smarks FROM student WHERE id = sid;
END //
DELIMITER ;''', "sql", "Step 1 — the procedure", label=""))
    o.append(code('''import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Types;

public class StudentProcedure {
    private static final String URL  = "jdbc:mysql://localhost:3306/mydb";
    private static final String USER = "root";
    private static final String PASS = "your_password";

    public static void main(String[] args) {
        String call = "{call student_stats(?, ?, ?)}";

        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             CallableStatement cs = con.prepareCall(call)) {

            cs.setInt(1, 103);                              // IN parameter
            cs.registerOutParameter(2, Types.VARCHAR);      // OUT parameter
            cs.registerOutParameter(3, Types.INTEGER);      // OUT parameter
            cs.execute();

            System.out.println("Name  : " + cs.getString(2));
            System.out.println("Marks : " + cs.getInt(3));
        } catch (SQLException e) {
            System.out.println("Procedure failed: " + e.getMessage());
        }
    }
}''', "java", "IN and OUT parameters", label="PROGRAM 16.5"))
    o.append(raw_code('''Name  : Aman
Marks : 75''', "Output"))
    o.append(mini("Line by line"))
    o.append(ul(["The call text uses JDBC escape syntax: <span class='mono'>{call name(?, ?)}</span>. Braces are "
                 "required; the driver translates them into the database's own syntax.",
                 "<b>IN</b> parameters are set like ordinary parameters: <span class='mono'>setInt(1, 103)</span>.",
                 "<b>OUT</b> parameters must be <b>registered before</b> execution. "
                 "<span class='mono'>Types.VARCHAR</span> comes from <span class='mono'>java.sql.Types</span>.",
                 "After <span class='mono'>execute()</span> the values are read by position with the ordinary getters.",
                 "If the procedure returns a result set instead of OUT parameters, use "
                 "<span class='mono'>executeQuery()</span> and loop exactly as in Program 16.1."]))
    o.append(box("mistake", "Common mistake",
                 "<p>Calling <span class='mono'>getString(2)</span> before "
                 "<span class='mono'>execute()</span>. The OUT value does not exist until the procedure has run, so "
                 "the driver throws <span class='mono'>SQLException: no output parameters returned by the "
                 "procedure</span>.</p>"))

    o.append(sec("16.6", "Discovering the schema with metadata"))
    o.append(code('''import java.sql.*;

public class StudentMetaData {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String url = "jdbc:mysql://localhost:3306/mydb";

        try (Connection con = DriverManager.getConnection(url, "root", "your_password")) {

            DatabaseMetaData db = con.getMetaData();
            System.out.println(db.getDatabaseProductName() + " "
                             + db.getDatabaseProductVersion());

            try (Statement stmt = con.createStatement();
                 ResultSet rs = stmt.executeQuery("SELECT * FROM student")) {

                ResultSetMetaData md = rs.getMetaData();
                int columns = md.getColumnCount();
                for (int i = 1; i <= columns; i++) {
                    System.out.printf("%-12s %-10s nullable=%s%n",
                        md.getColumnName(i), md.getColumnTypeName(i),
                        md.isNullable(i) == ResultSetMetaData.columnNullable);
                }

                while (rs.next()) {           // rows are still readable
                    System.out.println(rs.getInt("id") + " " + rs.getString("name"));
                }
            }
        }
    }
}''', "java", "Metadata about the database and the result", label="PROGRAM 16.6"))
    o.append(raw_code('''MySQL 8.0.36
id           INT        nullable=false
name         VARCHAR    nullable=false
city         VARCHAR    nullable=true
marks        INT        nullable=true
101 Rajesh
102 Simran''', "Output (abridged)"))
    o.append(p("This is the program that makes generic tools possible: a report generator can discover the column "
               "names and types without being written for one table. Notice that the metadata columns are numbered "
               "from 1, exactly like getters, and that reading metadata does not consume the rows."))

    o.append(sec("16.7", "Spring JDBC: a DAO without boilerplate"))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <!-- coordinates and parent omitted for brevity; see Part 12 -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
        </dependency>
    </dependencies>
</project>''', "xml", "The two dependencies that make Spring JDBC work", label=""))
    o.append(code('''# src/main/resources/application.properties
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=your_password
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver''', "properties", "The four properties read by auto-configuration", label=""))
    o.append(code('''package com.example.student;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class StudentRepository {

    private final JdbcTemplate jdbc;

    public StudentRepository(JdbcTemplate jdbc) {   // injected by Spring
        this.jdbc = jdbc;
    }

    private static final RowMapper<Student> MAPPER = (rs, rowNum) -> new Student(
            rs.getInt("id"), rs.getString("name"),
            rs.getString("city"), rs.getInt("marks"));

    public List<Student> findAll() {
        return jdbc.query("SELECT id, name, city, marks FROM student ORDER BY id", MAPPER);
    }

    public Student findById(int id) {
        return jdbc.queryForObject(
                "SELECT id, name, city, marks FROM student WHERE id = ?", MAPPER, id);
    }

    public int save(Student s) {
        return jdbc.update(
                "INSERT INTO student (id, name, city, marks) VALUES (?, ?, ?, ?)",
                s.getId(), s.getName(), s.getCity(), s.getMarks());
    }

    public int delete(int id) {
        return jdbc.update("DELETE FROM student WHERE id = ?", id);
    }
}''', "java", "The repository — no connection, no close, no try/catch", label="PROGRAM 16.7"))
    o.append(code('''package com.example.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class StudentApplication {

    public static void main(String[] args) {
        SpringApplication.run(StudentApplication.class, args);
    }

    @Bean
    CommandLineRunner demo(StudentRepository repo) {
        return args -> {
            repo.save(new Student(105, "Karan", "Ludhiana", 79));
            repo.findAll().forEach(System.out::println);
            System.out.println(repo.findById(105));
        };
    }
}''', "java", "The application class: auto-configuration plus one runnable demonstration", label=""))
    o.append(raw_code('''Student{id=101, name='Rajesh', city='Guntur', marks=88}
Student{id=102, name='Simran', city='Patiala', marks=91}
Student{id=103, name='Aman', city='Delhi', marks=75}
Student{id=105, name='Karan', city='Ludhiana', marks=79}
Student{id=105, name='Karan', city='Ludhiana', marks=79}''', "Output"))
    o.append(mini("What Spring did, and what you did"))
    o.append(tbl("Responsibilities in Program 16.7",
                 ["Spring handled", "You wrote"],
                 [["Reading application.properties", "The SQL statements"],
                  ["Building the DataSource (HikariCP pool)", "The RowMapper lambda"],
                  ["Building JdbcTemplate and injecting it", "The method signatures"],
                  ["Opening and closing connections and statements", "The business decision of what to insert"],
                  ["Translating SQLException into DataAccessException", "Nothing about errors"]],
                 ["62%", "38%"], firstcol=False))
    o.append(p("Compare the length of <span class='mono'>findAll()</span> with Program 16.1: nine lines of try, "
               "query, loop, close and catch become one. That comparison is the answer to “why Spring JDBC” in an "
               "examination."))

    o.append(sec("16.8", "Transforming XML with XSLT in Java"))
    o.append(code('''import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import java.io.File;

public class XsltDemo {
    public static void main(String[] args) throws Exception {
        TransformerFactory factory = TransformerFactory.newInstance();
        Transformer transformer = factory.newTransformer(
                new StreamSource(new File("book.xsl")));

        transformer.transform(
                new StreamSource(new File("book.xml")),
                new StreamResult(new File("book.html")));

        System.out.println("book.html written");
    }
}''', "java", "Applying book.xsl to book.xml", label="PROGRAM 16.8"))
    o.append(p("The program mirrors the pipeline of Part 11 exactly: a factory creates a transformer from the "
               "stylesheet, and the transformer consumes the source document and writes the result. The three "
               "arguments are the three boxes of Figure 11.3 — stylesheet, source, result."))
    o.append(code('''<!-- book.xsl - a minimal stylesheet for the program above -->
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html><body>
            <h2>Book Details</h2>
            <ul>
                <xsl:for-each select="book_store/book">
                    <li><xsl:value-of select="title"/> — <xsl:value-of select="author"/></li>
                </xsl:for-each>
            </ul>
        </body></html>
    </xsl:template>
</xsl:stylesheet>''', "xml", "The stylesheet it reads", label=""))
    o.append(sec("16.9", "Swing + JDBC: the login window"))
    o.append(p("The unit is titled <b>GUI and Database Connectivity</b>, and the lecture material closes the loop "
               "with an application that has both: a Swing window collects a username and password, and a JDBC "
               "query checks them against a table. Nothing about the database layer changes — this is the same "
               "<span class='mono'>PreparedStatement</span> of Part 5, called from a button's action listener."))
    o.append(code('''CREATE TABLE users (
    username VARCHAR(40) PRIMARY KEY,
    password VARCHAR(40) NOT NULL
);

INSERT INTO users VALUES ('admin', 'admin123');
INSERT INTO users VALUES ('rajesh', 'welcome1');''', "sql", "The table the window authenticates against", label=""))
    o.append(code('''import javax.swing.*;
import java.awt.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class LoginFrame extends JFrame {

    private static final String URL  = "jdbc:mysql://localhost:3306/mydb";
    private static final String USER = "root";
    private static final String PASS = "your_password";

    private final JTextField     userField = new JTextField(18);
    private final JPasswordField passField = new JPasswordField(18);
    private final JLabel         status    = new JLabel(" ");

    public LoginFrame() {
        super("Student Portal - Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
        c.insets = new Insets(6, 6, 6, 6);
        c.fill = GridBagConstraints.HORIZONTAL;

        JButton login = new JButton("Log in");
        c.gridx = 0; c.gridy = 0; add(new JLabel("Username"), c);
        c.gridx = 1;               add(userField, c);
        c.gridx = 0; c.gridy = 1; add(new JLabel("Password"), c);
        c.gridx = 1;               add(passField, c);
        c.gridx = 0; c.gridy = 2; c.gridwidth = 2; add(login, c);
        c.gridy = 3;                               add(status, c);

        login.addActionListener(e -> authenticate());

        pack();
        setLocationRelativeTo(null);
    }

    private void authenticate() {
        String sql = "SELECT username FROM users WHERE username = ? AND password = ?";

        // try-with-resources closes the statement and connection on every path
        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setString(1, userField.getText().trim());
            ps.setString(2, new String(passField.getPassword()));

            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    status.setForeground(new Color(0x0a7d4f));
                    status.setText("Welcome, " + rs.getString("username"));
                } else {
                    status.setForeground(new Color(0xb3261e));
                    status.setText("Invalid username or password");
                }
            }
        } catch (SQLException ex) {
            status.setForeground(new Color(0xb3261e));
            status.setText("Database error: " + ex.getMessage());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new LoginFrame().setVisible(true));
    }
}''', "java", "The complete Swing + JDBC login application", label="PROGRAM 16.9"))
    o.append(mini("Why each part is there"))
    o.append(ul(["<b>The window is built once</b> in the constructor; the database work is isolated in "
                 "<span class='mono'>authenticate()</span>, so the two concerns never tangle.",
                 "<b><span class='mono'>EXIT_ON_CLOSE</span></b> ends the JVM when the window closes, which also "
                 "releases any open resource.",
                 "<b>The action listener is a lambda</b> — a single-method interface, exactly the "
                 "<span class='mono'>@FunctionalInterface</span> idea of Part 8.",
                 "<b>The connection is opened inside the listener</b> and closed by try-with-resources when it "
                 "returns. A real application with frequent queries would hold the connection, or a pool, in the "
                 "frame instead of reopening per click — the connection-cost argument of Part 7.6.",
                 "<b>The query is parameterized</b>, so typing <span class='mono'>' OR '1'='1</span> into the "
                 "username field produces “Invalid username or password”, not a login.",
                 "<b><span class='mono'>rs.next()</span> is the whole test</b>: a result set with at least one row "
                 "means the credentials matched.",
                 "<b>Errors go to a label, not to the console</b>, because a GUI user has no console."]))
    o.append(box("mistake", "Common mistake",
                 "<p>Reading the password with <span class='mono'>passField.getText()</span>. "
                 "<span class='mono'>JPasswordField</span> deliberately deprecates that method; use "
                 "<span class='mono'>getPassword()</span>, which returns a <span class='mono'>char[]</span> that can "
                 "be cleared after use. In a real system you would store a <b>hash</b> of the password, never the "
                 "password itself.</p>"))
    o.append(box("imp", "Important",
                 "<p>The GUI changes nothing in the JDBC layer. That is the point of the combination: the database "
                 "code of Program 16.1 can be lifted into any front end — a Swing window, a servlet or a Spring REST "
                 "controller — because it depends only on the standard interfaces.</p>"))
    o.append(box("tip", "Exam tip",
                 "<p>For a practical examination, Programs 16.1 to 16.4 are the ones you will be asked to write. "
                 "Memorize the shape — constants, <span class='mono'>Class.forName</span>, "
                 "<span class='mono'>try-with-resources</span>, one SQL string, one loop — and you can produce any of "
                 "them in five minutes.</p>"))
    o.append(recap("Part 16 recap", [
        ["<b>16.1 SELECT</b>", "Constants, Class.forName, try-with-resources, executeQuery, next() loop."],
        ["<b>16.2 INSERT</b>", "PreparedStatement with four setters; executeUpdate returns 1 per row."],
        ["<b>16.3 UPDATE</b>", "Check the returned count — zero rows is not an exception."],
        ["<b>16.4 DELETE</b>", "Always parameterize the WHERE clause; never delete without one."],
        ["<b>16.5 Procedure</b>", "prepareCall with {call ...}, registerOutParameter before execute."],
        ["<b>16.6 Metadata</b>", "DatabaseMetaData and ResultSetMetaData describe the database and the result."],
        ["<b>16.7 Spring DAO</b>", "Repository + JdbcTemplate + RowMapper + application.properties."],
        ["<b>16.8 XSLT</b>", "TransformerFactory, StreamSource, StreamResult — the Part 11 pipeline in code."],
        ["<b>16.9 Swing</b>", "A GUI front end over the same JDBC code; errors shown in a label."],
    ], terms=["try-with-resources", "batch insert", "generated keys", "ResultSetMetaData", "DatabaseMetaData", "DAO", "single connection", "SQLException handling", "formatted output"], practice=[
        "Trace Program 16.2 from <span class='mono'>getConnection</span> to the printed row.",
        "In Program 16.9, at which exact line does the injection attempt fail?",
        "Which program demonstrates metadata, and what does it print?",
    ], trap="Hard-coding the password in every program, and leaving the ResultSet unclosed."))
    return "".join(o)
