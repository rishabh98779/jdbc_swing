"""PART 17 — Examination Preparation."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_marks_map():
    b = []
    b.append(txt(12, 18, "WHERE THE MARKS ARE", 8.4, MUTED, 700, ls="0.1em"))
    rows = [("Architecture of JDBC", 18, TEAL), ("JDBC vs Spring JDBC", 14, TEAL),
            ("Statements comparison", 16, ORANGE), ("Annotation categories", 12, ORANGE),
            ("XML / DTD / XSD", 14, NAVY2), ("Maven and pom.xml", 12, NAVY2),
            ("POJO vs JavaBean", 8, MUTED), ("Programs (practical)", 6, MUTED)]
    y = 36
    for name, w, col in rows:
        b.append(txt(12, y + 12, name, 7.8, INK, 600))
        b.append(rect(230, y + 2, w * 14, 14, col, col, 0))
        b.append(txt(230 + w * 14 + 6, y + 12, str(w) + "%", 7.2, col, 700))
        y += 22
    b.append(line(228, 30, 228, y - 8, LINE, 1.0))
    return svg(660, y + 4, "".join(b))


def html():
    o = []
    o.append(part(17, "Examination Preparation",
                  "Definitions, differences, short answers, long answers, viva questions and twenty MCQs — "
                  "all answerable from this book.", art_icon=17))

    o.append(fig(fig_marks_map(),
                 "An estimate of how the marks are distributed across the unit. Architecture, statements and XML "
                 "carry the most weight in a typical paper."))

    o.append(sec("17.1", "Definitions you must be able to write"))
    o.append(tbl("Twelve definitions, each in one sentence",
                 ["Term", "Definition"],
                 [["JDBC", "A Java API that lets Java applications execute SQL statements against any relational "
                            "database through a driver, using a standard set of interfaces."],
                  ["JDBC driver", "A vendor-supplied component that implements the JDBC interfaces for one database "
                                   "product and translates calls into that product's protocol."],
                  ["DriverManager", "The class that keeps the list of registered drivers and returns a Connection "
                                    "for a given JDBC URL."],
                  ["Connection", "The session between the Java application and the database; a factory for "
                                  "Statement, PreparedStatement, CallableStatement and DatabaseMetaData."],
                  ["Statement", "An object that executes a static SQL statement and returns the ResultSet it "
                                 "produces."],
                  ["PreparedStatement", "A precompiled Statement with <code>?</code> placeholders, used for "
                                        "parameterized and repeated queries."],
                  ["CallableStatement", "A PreparedStatement used to execute stored procedures, supporting IN, OUT "
                                        "and INOUT parameters."],
                  ["ResultSet", "A table of rows returned by a query, with a cursor pointing at the current row."],
                  ["SQL injection", "An attack in which user input is interpreted as SQL code because the query was "
                                    "built by string concatenation."],
                  ["Annotation", "A form of metadata, beginning with @, that does not change what a compiled program "
                                 "does but can be read by the compiler or the framework."],
                  ["XML", "A self-descriptive, extensible markup language for storing and transporting data, "
                          "independent of software and hardware."],
                  ["POJO", "A plain Java object with no framework-specific superclass, interface or annotation."]],
                 ["22%", "78%"], firstcol=False))
    o.append(box("tip", "Exam tip",
                 "<p>In a definition question, always include the <i>purpose</i> in the same sentence. “A ResultSet is "
                 "a table of rows with a cursor” is a fact; “A ResultSet is a table of rows with a cursor that "
                 "iterates the data returned by a query” is an answer.</p>"))

    o.append(sec("17.2", "Frequently confused pairs"))
    o.append(qa("Well-formed versus valid",
                "Well-formed = correct XML <b>syntax</b> (closed, nested, one root, quoted attributes). "
                "Valid = well-formed <b>and</b> conforming to a DTD or XSD. Valid implies well-formed; the reverse "
                "does not hold."))
    o.append(qa("executeQuery() versus executeUpdate()",
                "<span class='mono'>executeQuery()</span> returns a <span class='mono'>ResultSet</span> and is used "
                "for SELECT. <span class='mono'>executeUpdate()</span> returns an <span class='mono'>int</span> row "
                "count and is used for INSERT, UPDATE, DELETE and DDL."))
    o.append(qa("Statement versus PreparedStatement",
                "Statement compiles the SQL on every execution and cannot take parameters. PreparedStatement is "
                "compiled once, takes <span class='mono'>?</span> parameters and is immune to injection."))
    o.append(qa("JavaBean versus POJO",
                "A POJO is any ordinary class. A JavaBean is a POJO with a public no-arg constructor, private fields "
                "with getters/setters, and Serializable."))
    o.append(qa("DTD versus XSD",
                "DTD has its own syntax, no data types and no namespaces. XSD is written in XML, has rich data types "
                "and supports namespaces."))
    o.append(qa("commit() versus rollback()",
                "Both end a transaction. <span class='mono'>commit()</span> makes all changes permanent; "
                "<span class='mono'>rollback()</span> undoes every change since the last commit or rollback."))
    o.append(qa("Two-tier versus three-tier JDBC",
                "Two-tier: the application talks directly to the database. Three-tier: a middle tier of services "
                "sits between them and provides control, easier deployment and better performance."))
    o.append(qa("DataSource versus DriverManager",
                "DriverManager is a static utility that opens a new connection per call. A DataSource is an object "
                "that supplies connections and can be pooled, configured and injected."))

    o.append(sec("17.3", "Short-answer questions"))
    o.append(p("Each answer below is the length expected for a 2- or 3-mark question — two to four sentences, with "
               "the technical term used correctly."))
    o.append(qa("What is JDBC and why is it needed?",
                "JDBC — Java Database Connectivity — is a Java API for executing SQL on relational databases. It is "
                "needed because Java cannot safely call the C interface of ODBC, and because one standard API replaces "
                "the N × M problem of connecting N programs to M databases."))
    o.append(qa("Name the two layers of JDBC architecture.",
                "The JDBC API layer, which provides the application-to-DriverManager connection, and the JDBC Driver "
                "API layer, which supports the DriverManager-to-driver connection."))
    o.append(qa("List the four JDBC driver types.",
                "Type 1 JDBC-ODBC bridge, Type 2 native-API (partly Java), Type 3 network protocol (pure Java, "
                "middleware), Type 4 thin driver (pure Java, direct protocol)."))
    o.append(qa("Which driver type would you choose for one database, and why?",
                "Type 4. It is pure Java, requires nothing on the client but the JAR, and has the fewest translation "
                "layers, so it is the fastest deployment option."))
    o.append(qa("What is the default value of auto-commit?",
                "true. Every statement is committed as soon as it succeeds, so several statements cannot be grouped "
                "into one transaction until <span class='mono'>setAutoCommit(false)</span> is called."))
    o.append(qa("Why is PreparedStatement safer than Statement?",
                "Because the SQL structure is compiled before the values are supplied. A parameter can only be a "
                "value, never SQL syntax, so injection such as <span class='mono'>' OR '1'='1</span> is neutralised."))
    o.append(qa("What does ResultSet.next() do?",
                "It moves the cursor one row forward and returns true if the new row exists, or false when the cursor "
                "is past the last row — which is why it is used as the loop condition."))
    o.append(qa("What is the difference between IN and OUT parameters?",
                "IN passes a value into the procedure; OUT returns a value from it and must be registered with "
                "<span class='mono'>registerOutParameter()</span> before execution."))
    o.append(qa("What does @SpringBootApplication combine?",
                "@SpringBootConfiguration, @EnableAutoConfiguration and @ComponentScan, each with its default "
                "attributes."))
    o.append(qa("What are the five categories of annotations?",
                "Marker, single-value, full, type and repeating annotations."))
    o.append(qa("What is the purpose of pom.xml?",
                "It is the Project Object Model: it declares the project's coordinates, dependencies, plugins, "
                "profiles and build configuration — the single source of truth Maven uses to build the project."))
    o.append(qa("What does DriverManagerDataSource do, and what does it not do?",
                "It holds the driver class, URL, username and password and returns a new Connection each time. It "
                "does not pool connections, so it is unsuitable for high-concurrency production use."))
    o.append(qa("State the three JavaBean conventions.",
                "Public class with a public no-argument constructor; private fields exposed through getters and "
                "setters; implements Serializable."))
    o.append(qa("What is XSLT used for?",
                "To transform an XML document into another XML document — most often into HTML for display — using "
                "XPath to select nodes from the source tree."))

    o.append(sec("17.4", "Long-answer questions"))
    o.append(p("A 6- to 10-mark answer needs a diagram, a structured list and one example. The outline below is what "
               "each answer should contain; the parts named give the full material."))
    o.append(qa("Explain the architecture of JDBC with a neat diagram.",
                "Two-layer architecture (JDBC API and JDBC Driver API) → two-tier and three-tier deployment models "
                "with advantages of each → the call path Application → JDBC API → DriverManager → Driver → Database "
                "→ the four product components. See Parts 2.1 to 2.5."))
    o.append(qa("Explain the four types of JDBC drivers with their advantages and disadvantages.",
                "One paragraph and one small diagram per type, then the comparison table and the selection rule "
                "(Type 4 for one database, Type 3 for many, Type 2 if neither exists, Type 1 only for testing). "
                "See Part 3."))
    o.append(qa("Explain the steps to connect a Java application to a database.",
                "The seven steps with the exact API call for each, then a complete program, then the sequence "
                "diagram, then the three common failures (no JAR, no suitable driver, access denied). See Parts 3 and "
                "16.1."))
    o.append(qa("Compare Statement, PreparedStatement and CallableStatement.",
                "Inheritance hierarchy, then the comparison table on six criteria, then one code fragment for each, "
                "ending with the selection rule. See Part 5."))
    o.append(qa("What is SQL injection? How does PreparedStatement prevent it?",
                "Define the attack, show the vulnerable concatenated query, show the input <span class='mono'>' OR "
                "'1'='1</span> and the resulting always-true WHERE clause, then the parameterized replacement with "
                "the reason (structure compiled before values). See Part 7."))
    o.append(qa("Discuss the advantages and disadvantages of JDBC.",
                "Four advantages by name (existing enterprise data, simplified development, zero client "
                "configuration, metadata access), then the connection-cost disadvantage and the SQL-dialect "
                "portability point, then a concluding sentence about pooling and Spring JDBC. See Parts 7.5 and 7.6."))
    o.append(qa("Differentiate JDBC and Spring JDBC.",
                "The six numbered points from the lecture, then the comparison table, then the stack diagram showing "
                "JdbcTemplate over DataSource over the driver. See Part 9."))
    o.append(qa("Explain XML, DTD and XML Schema with examples.",
                "XML syntax rules and the tree, well-formed versus valid, an internal and an external DTD, an XSD "
                "with a complex type, then the DTD-versus-XSD table. See Part 10."))
    o.append(qa("Explain XML namespaces and XSLT with examples.",
                "The name-conflict problem, the <span class='mono'>xmlns:prefix</span> declaration and its scope, the "
                "default namespace, then the XSLT pipeline with a stylesheet and its rendered output. See Part 11."))
    o.append(qa("Explain Maven and the structure of pom.xml.",
                "Definition of Maven and the POM, the nine capabilities, the minimal POM, then the section map with "
                "the XML for coordinates, dependencies, build, plugins and profiles, then the lifecycle. See Part 12."))
    o.append(qa("Explain JdbcTemplate and DriverManagerDataSource with a program.",
                "The class declaration and its two supertypes, the two usage steps, the four methods, a RowMapper, "
                "then DriverManagerDataSource's four properties, the wiring, and the pooling limitation. See Parts 13 "
                "and 14."))
    o.append(qa("Differentiate POJO and JavaBean.",
                "Definition of each, the three conventions, two code examples side by side, the comparison table, and "
                "the note that a Spring bean is a different idea. See Part 15."))

    o.append(sec("17.5", "Viva questions with answers"))
    o.append(qa("Why is JDBC called a “write once, run anywhere” API?",
                "Because the interfaces are in the JDK and the vendor supplies only the implementation, so the same "
                "Java code runs against any database once the appropriate driver is on the classpath."))
    o.append(qa("Which exception does Class.forName() throw?",
                "<span class='mono'>ClassNotFoundException</span>, a checked exception from "
                "<span class='mono'>java.lang</span>."))
    o.append(qa("Can you use JDBC without loading the driver explicitly?",
                "Yes, since JDBC 4.0, through the service-provider mechanism in "
                "<span class='mono'>META-INF/services/java.sql.Driver</span>. The explicit "
                "<span class='mono'>Class.forName()</span> is still the safer habit and is what most courses teach."))
    o.append(qa("What happens if you call executeQuery() with an UPDATE statement?",
                "The driver throws a <span class='mono'>SQLException</span>, because the statement does not produce a "
                "result set."))
    o.append(qa("Why are parameter indexes 1-based?",
                "It is the convention inherited from the original JDBC specification, which followed SQL's 1-based "
                "column numbering."))
    o.append(qa("Can a Connection be reused after close()?",
                "No. <span class='mono'>close()</span> releases the session; any further use throws "
                "<span class='mono'>SQLException: No operations allowed after connection closed</span>."))
    o.append(qa("What is the difference between execute() and executeQuery()?",
                "<span class='mono'>execute()</span> returns a boolean indicating whether a ResultSet is available "
                "and works for any SQL; <span class='mono'>executeQuery()</span> returns the ResultSet directly and "
                "works only for statements that produce rows."))
    o.append(qa("What does getMetaData() on a ResultSet tell you?",
                "The number, names, types and nullability of the columns in the result — useful for generic tools."))
    o.append(qa("Is a JavaBean required to implement Serializable?",
                "In the strict JavaBeans specification, yes. Many modern frameworks relax it, but for an examination "
                "answer state that it is one of the conventions."))
    o.append(qa("What is the difference between @Component and @Bean?",
                "<span class='mono'>@Component</span> is placed on a class and found by component scanning; "
                "<span class='mono'>@Bean</span> is placed on a method inside a "
                "<span class='mono'>@Configuration</span> class and the method's return value becomes the bean."))
    o.append(qa("What is the Super POM?",
                "Maven's default POM, which every project POM inherits from; it supplies default repositories, plugin "
                "versions and directories."))
    o.append(qa("What is the difference between mvn install and mvn deploy?",
                "<span class='mono'>install</span> copies the artifact into the local repository "
                "(<span class='mono'>~/.m2</span>); <span class='mono'>deploy</span> uploads it to a remote "
                "repository for other developers."))
    o.append(qa("Why does a namespace URI not need to be a working web address?",
                "Because it is only compared as a string to identify the vocabulary; nothing is ever downloaded from "
                "it."))
    o.append(qa("What is the root of an XML document?",
                "The single top-level element that contains all others."))
    o.append(qa("Can an XML document have two root elements?",
                "No. A document with two top-level elements is not well-formed."))

    o.append(sec("17.6", "Multiple-choice questions"))
    o.append(p("Twenty questions in the pattern of a university paper. Cover the answers, attempt all twenty, then "
               "mark yourself: 16 or more is examination-ready."))
    mcqs = [
     ("JDBC stands for:", ["Java Database Connectivity", "Java Data Binding Component",
                           "Java Driver Base Connectivity", "Joint Database Connectivity"], "A"),
     ("Which package contains the core JDBC interfaces?", ["java.db", "java.sql", "javax.jdbc", "java.jdbc"], "B"),
     ("The two layers of JDBC architecture are:",
      ["API and Network", "API and Driver API", "Driver and ResultSet", "Application and Database"], "B"),
     ("A Type 4 driver is:", ["A JDBC-ODBC bridge", "Partly written in Java",
                              "A pure-Java driver using the database's own protocol", "A middleware driver"], "C"),
     ("Which driver type needs a middleware server?", ["Type 1", "Type 2", "Type 3", "Type 4"], "C"),
     ("DriverManager.getConnection() returns:", ["Statement", "Connection", "ResultSet", "Driver"], "B"),
     ("Class.forName() throws:", ["SQLException", "IOException", "ClassNotFoundException",
                                  "InstantiationException"], "C"),
     ("Which method executes a SELECT statement?",
      ["executeUpdate()", "executeQuery()", "executeBatch()", "addBatch()"], "B"),
     ("executeUpdate() returns:", ["A ResultSet", "A boolean", "The number of rows affected", "void"], "C"),
     ("The default ResultSet type is:", ["Scrollable", "Updatable", "Forward-only and read-only", "Sensitive"], "C"),
     ("Which interface is used for stored procedures?",
      ["Statement", "PreparedStatement", "CallableStatement", "DatabaseMetaData"], "C"),
     ("SQL injection is prevented by:",
      ["Using Statement", "Concatenating strings carefully", "Using PreparedStatement with parameters",
       "Using executeBatch()"], "C"),
     ("Which is NOT a JavaBean convention?",
      ["Public no-argument constructor", "Private fields with getters and setters", "Implements Serializable",
       "Extends a framework base class"], "D"),
     ("@SpringBootApplication does NOT include:", ["@EnableAutoConfiguration", "@ComponentScan",
                                                   "@SpringBootConfiguration", "@Autowired"], "D"),
     ("Which exception does Spring JDBC throw?",
      ["SQLException", "DataAccessException", "IOException", "ClassNotFoundException"], "B"),
     ("Which is a valid JDBC URL for MySQL?",
      ["jdbc:mysql://localhost:3306/mydb", "mysql:jdbc://localhost/mydb",
       "jdbc://mysql:localhost/mydb", "http://localhost/mydb"], "A"),
     ("A document that follows a DTD is called:", ["Well-formed", "Valid", "Parsed", "Normalised"], "B"),
     ("A DTD element containing only text is declared as:",
      ["(#CDATA)", "(#PCDATA)", "(TEXT)", "(#ANY)"], "B"),
     ("The Maven model version must be:", ["1.0.0", "2.0", "4.0.0", "5.0"], "C"),
     ("Which property must be set on JdbcTemplate?", ["url", "driverClassName", "dataSource", "username"], "C"),
    ]
    for q, opts, ans_ in mcqs:
        expl = {
         "A": "JDBC = Java Database Connectivity, the standard API for SQL access from Java.",
         "B": "java.sql holds Connection, Statement, ResultSet and DriverManager.",
         "C": "Type 3 talks to a middleware server which then reaches the database.",
         "D": "Extending a framework base class is exactly what a POJO avoids.",
        }.get("", "")
        o.append(mcq(q, opts, ans_))
    o.append(box("viva", "Answer key",
                 "<p>1 A · 2 B · 3 B · 4 C · 5 C · 6 B · 7 C · 8 B · 9 C · 10 C · 11 C · 12 C · 13 D · 14 D · "
                 "15 B · 16 A · 17 B · 18 B · 19 C · 20 C</p>"
                 "<p class='small'>Where a question could be argued, the explanation is in the corresponding part: "
                 "Type 4 (Part 3.6), ResultSet defaults (6.4), injection (7.3), Spring exceptions (9.2), statistics "
                 "(10.6), lifecycle (12.5).</p>"))

    o.append(sec("17.7", "Practical and application-oriented questions"))
    o.append(ol(["Write a Java program to display all records of a <span class='mono'>student</span> table, ordered "
                 "by name, using only the JDBC API.",
                 "Write a program that inserts a record using PreparedStatement and prints whether the insertion "
                 "succeeded, distinguishing a duplicate key from a connection failure.",
                 "Write a program that accepts an <span class='mono'>id</span> from the user and deletes that record, "
                 "printing the number of rows deleted.",
                 "Create a stored procedure that returns the total number of students, and call it from Java with a "
                 "CallableStatement.",
                 "Write a DAO class using <span class='mono'>JdbcTemplate</span> that supports insert, find-by-id, "
                 "find-all and delete for the <span class='mono'>student</span> table.",
                 "Give an XML document for a book list, write its DTD, and explain why a document with an extra "
                 "element is invalid but still well-formed.",
                 "Write an XSD for the same book list that restricts <span class='mono'>year</span> to an integer and "
                 "<span class='mono'>price</span> to a decimal.",
                 "Write a <span class='mono'>pom.xml</span> for a project that needs Spring JDBC and the MySQL driver, "
                 "with the Java version set to 17 through a property.",
                 "Demonstrate SQL injection against a login query built by concatenation, then rewrite it safely and "
                 "explain the difference in one paragraph.",
                 "Write a Java program that reads <span class='mono'>book.xml</span> with DOM and prints every title "
                 "together with its <span class='mono'>lang</span> attribute."]))
    o.append(box("tip", "Exam tip",
                 "<p>For every practical question: declare the constants, load the driver, use try-with-resources, "
                 "use a PreparedStatement whenever there is a parameter, check the returned count, and print one "
                 "line of sample output. Those six habits are what examiners look for.</p>"))
    o.append(recap("Part 17 recap — answering strategy", [
        ["<b>Definition question</b>", "One sentence with the term, its purpose and its distinguishing feature."],
        ["<b>Architecture question</b>", "Draw first: two layers, then the call path, then the deployment model."],
        ["<b>Comparison question</b>", "A table with criteria down the left; four to six rows is enough."],
        ["<b>Program question</b>", "Constants, load driver, try-with-resources, one SQL string, check the count."],
        ["<b>Security question</b>", "Show the vulnerable string, the attack input, then the parameterized fix."],
        ["<b>Spring question</b>", "Name the annotation or class, say what it replaces, then show one line of code."],
        ["<b>XML question</b>", "Example first, rules second, DTD or XSD third, verdict (well-formed or valid) last."],
        ["<b>Marks lost</b>", "Missing diagram, wrong method for the SQL type, unclosed resources, no example."],
    ], terms=["definition question", "architecture question", "comparison question", "program question",
              "security question", "Spring question", "XML question", "marks lost", "answer structure"],
       trap="Writing a description where the question asked for a comparison — answer in the two-column table."))
    return "".join(o)
