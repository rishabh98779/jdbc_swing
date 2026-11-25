"""PART 12 — Maven and pom.xml."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_structure():
    b = []
    b.append(txt(12, 18, "THE STANDARD MAVEN LAYOUT", 8.4, MUTED, 700, ls="0.1em"))
    rows = [("my-app/", 0, NAVY, True, "project root"),
            ("pom.xml", 1, ORANGE, False, "the Project Object Model"),
            ("src/", 1, NAVY, True, ""),
            ("main/", 2, NAVY, True, ""),
            ("java/", 3, TEAL, True, "production sources → .class"),
            ("resources/", 3, TEAL, False, "config files, kept with the classes"),
            ("test/", 2, NAVY, True, ""),
            ("java/", 3, ORANGE, True, "test sources, not packaged"),
            ("target/", 1, MUTED, True, "build output (generated)"),
            ("classes/", 2, MUTED, False, "compiled classes"),
            ("my-app-1.0.jar", 2, MUTED, False, "the artifact")]
    items = []
    y = 40
    for name, depth, col, is_dir, note_ in rows:
        x = 24 + depth * 22
        items.append(txt(x, y, name, 8.0, col, 700 if is_dir else 400, "start", MONO))
        if note_:
            items.append(txt(300, y, note_, 7.4, MUTED, 400, "start"))
        y += 16
    b.append(rect(12, 28, 636, y - 30, "#fbfcfd", LINE, 2))
    b.extend(items)
    b.append(txt(330, y + 12, "Maven's value is that every project looks like this, so any Maven project can be built by any Maven user.",
                 7.6, MUTED, 400, "middle"))
    return svg(660, y + 26, "".join(b))


def fig_lifecycle():
    b = []
    b.append(txt(12, 18, "THE DEFAULT BUILD LIFECYCLE", 8.4, MUTED, 700, ls="0.1em"))
    phases = ["validate", "compile", "test", "package", "verify", "install", "deploy"]
    x = 12
    for i, p_ in enumerate(phases):
        col = ORANGE if p_ in ("package", "install", "deploy") else TEAL
        b.append(node(x, 34, 84, 30, p_, None, WHITE, col, col, 8.0, 600))
        if i < len(phases) - 1:
            b.append(arrow(x + 86, 49, x + 96, 49, NAVY3, 1.1, hs=5.0))
        x += 96
    b.append(txt(12, 84, "Running any phase runs every phase before it:  mvn package = validate → compile → test → package",
                 7.8, MUTED, 400))
    b.append(rect(12, 96, 636, 54, GREY, LINE, 2))
    b.append(txt(24, 114, "What each phase produces", 7.8, NAVY, 700))
    b.append(txt(24, 128, "compile → target/classes      test → surefire reports      package → target/my-app-1.0.jar", 7.4, INK, 400, "start", MONO))
    b.append(txt(24, 142, "install → ~/.m2/repository      deploy → the remote repository", 7.4, INK, 400, "start", MONO))
    return svg(660, 158, "".join(b))


def fig_resolution():
    b = []
    b.append(txt(12, 18, "HOW A DEPENDENCY IS FOUND", 8.4, MUTED, 700, ls="0.1em"))
    steps = [("pom.xml", "declares a dependency", NAVY, WHITE),
             ("local repository", "~/.m2/repository", TEAL_L, TEAL),
             ("remote repository", "Maven Central, or a company Nexus", ORANGE_L, ORANGE),
             ("classpath", "added to compile and run", NAVY2, WHITE)]
    x = 12
    for i, (t, s, fill, tc) in enumerate(steps):
        b.append(node(x, 34, 140, 50, t, s, fill, fill if fill in (NAVY, NAVY2) else tc, tc, 8.4, 700, 7.0,
                      "#d5e2ee" if fill in (NAVY, NAVY2) else MUTED))
        if i < 3:
            b.append(arrow(x + 142, 59, x + 158, 59, NAVY3, 1.2, hs=5.4))
        x += 160
    b.append(rect(12, 100, 636, 66, "#fbfcfd", LINE, 2))
    b.append(txt(24, 118, "Transitive dependencies", 7.8, NAVY, 700))
    b.append(txt(24, 132, "spring-boot-starter-jdbc  →  spring-jdbc  →  spring-tx, spring-core  →  HikariCP", 7.4, INK, 400, "start", MONO))
    b.append(txt(24, 148, "You declare one dependency; Maven resolves the tree and downloads everything it needs, once.", 7.4, MUTED, 400))
    b.append(txt(24, 160, "That is what \"the project has everything it needs to run independently\" means in the slides.", 7.4, MUTED, 400))
    return svg(660, 172, "".join(b))


def fig_pom_map():
    b = []
    b.append(txt(12, 18, "THE SECTIONS OF A pom.xml", 8.4, MUTED, 700, ls="0.1em"))
    secs = [("<project>", "root element; carries the XSD declaration", NAVY, 0),
            ("<modelVersion>", "always 4.0.0", MUTED, 1),
            ("<groupId> / <artifactId> / <version>", "project coordinates (the GAV)", ORANGE, 1),
            ("<properties>", "reusable variables such as ${java.version}", TEAL, 1),
            ("<dependencies>", "external libraries, each with GAV and optional scope", TEAL, 1),
            ("<dependencyManagement>", "versions for dependencies declared elsewhere", TEAL, 1),
            ("<repositories>", "where to fetch from; defaults to Maven Central", ORANGE, 1),
            ("<build><plugins>", "compiler, jar, test and reporting tools", ORANGE, 1),
            ("<profiles>", "environment-specific settings: dev, qa, prod", VIOLET, 1),
            ("<pluginManagement>", "default versions and configuration for plugins", VIOLET, 1),
            ("<reporting>", "plugins that generate Javadoc and test reports", VIOLET, 1)]
    y = 34
    for name, desc, col, depth in secs:
        x = 14 + depth * 18
        b.append(rect(12, y - 12, 636, 20, "#fbfcfd", LINE, 0, 0.6))
        b.append(txt(x, y + 1, name, 7.8, col, 700, "start", MONO))
        b.append(txt(300, y + 1, desc, 7.4, MUTED, 400, "start"))
        y += 21
    return svg(660, y + 4, "".join(b))


def html():
    o = []
    o.append(part(12, "Maven and the Project Object Model",
                  "One XML file that describes a project well enough for a machine to build, test and "
                  "ship it.", art_icon=12))

    o.append(sec("12.1", "What Maven is"))
    o.append(p("Maven is an open-source <b>build automation tool</b> used primarily for Java projects. It is also a "
               "project management tool, and it is based on the concept of the <b>POM — the Project Object Model</b>. "
               "It is used for project build, dependency resolution and documentation."))
    o.append(box("def", "Definition",
                 "<p><b>Maven</b> is a build automation and project management tool for Java that operates through a "
                 "Project Object Model: an XML file that defines the project's structure, its dependencies, its "
                 "plugins and its configuration.</p>"))
    o.append(p("The lecture material lists nine things that the POM makes possible. They are also the reasons to use "
               "Maven, so learn them as a list:"))
    o.append(ol(["<b>Dependency management</b> — Maven downloads the required libraries and their dependencies from "
                 "a central repository, so the project has everything it needs to run independently.",
                 "<b>Standard project structure</b> — a fixed folder layout for sources, tests and other files.",
                 "<b>Build lifecycle</b> — standard phases such as compile, test and deploy.",
                 "<b>Plugins</b> — support for compiling, testing, packaging and more.",
                 "<b>POM file</b> — <span class='mono'>pom.xml</span> holds the configuration and dependencies.",
                 "<b>Central repository</b> — dependencies are fetched from a shared online repository.",
                 "<b>Build profiles</b> — different settings for development, QA and production.",
                 "<b>Reporting</b> — generates Javadoc, test reports and project documentation.",
                 "<b>IDE support</b> — integrates with Eclipse, IntelliJ and NetBeans."]))
    o.append(box("tip", "Exam tip",
                 "<p>“What is Maven?” is a two-part answer: a definition (build automation tool based on the POM) and "
                 "then three or four of the nine capabilities by name. Naming them is what separates a 5-mark answer "
                 "from a 2-mark answer.</p>"))

    o.append(sec("12.2", "The POM"))
    o.append(p("POM is an acronym for <b>Project Object Model</b>. The <span class='mono'>pom.xml</span> file "
               "contains the project's information and the configuration Maven needs to build it: dependencies, the "
               "build directory, the source and test source directories, plugins, goals and so on. Maven reads "
               "<span class='mono'>pom.xml</span> and then executes the goal you asked for."))
    o.append(p("<span class='mono'>pom.xml</span> is used because it is the <b>single source of truth</b> for a Maven "
               "project. It tells Maven what the project is, how it should be built, and which dependencies it needs. "
               "Everything else — the folder layout, the classpath, the JAR name — is derived from it."))
    o.append(mini("The Super POM and the minimal POM"))
    o.append(p("The <b>Super POM</b> is Maven's default POM. Every POM extends the Super POM unless it is explicitly "
               "told otherwise, which means the configuration in the Super POM is inherited by every project you "
               "create — that is why you never write the default repository URL, the default plugin versions or the "
               "default output directory."))
    o.append(p("The minimum requirement for a POM is small: a project root element, a "
               "<span class='mono'>modelVersion</span> that must be <span class='mono'>4.0.0</span>, and the three "
               "coordinates — <span class='mono'>groupId</span> (the id of the project's group), "
               "<span class='mono'>artifactId</span> (the id of the artifact) and "
               "<span class='mono'>version</span> (the version of the artifact inside that group)."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-first-project</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>''', "xml", "The minimal POM — every other element is optional"))

    o.append(sec("12.3", "The sections of a pom.xml"))
    o.append(p("A real POM is larger, and its sections are easier to remember as a map than as a list. The figure "
               "below is that map; the subsections that follow give the XML for the ones you will actually write."))
    o.append(fig(fig_pom_map(),
                 "The sections of a pom.xml, grouped by purpose: identity (navy), dependencies (teal), build and "
                 "sources (orange), and environment or reporting (violet)."))
    o.append(mini("Project coordinates and properties"))
    o.append(code('''<groupId>com.geeks</groupId>               <!-- organization, domain reversed -->
<artifactId>maven-pom-example</artifactId>  <!-- project or module name -->
<version>1.0-SNAPSHOT</version>             <!-- current version -->

<properties>
    <java.version>17</java.version>
    <selenium.version>4.6.0</selenium.version>
    <testng.version>7.4.0</testng.version>
</properties>''', "xml", "Coordinates and reusable properties"))
    o.append(p("Properties are the answer to “why is the version written twice?”. Declare it once, refer to it as "
               "<span class='mono'>${selenium.version}</span>, and a version upgrade becomes a one-line change."))
    o.append(mini("Dependencies and repositories"))
    o.append(code('''<dependencies>
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>9.0.0</version>
    </dependency>
    <dependency>
        <groupId>org.seleniumhq.selenium</groupId>
        <artifactId>selenium-java</artifactId>
        <version>${selenium.version}</version>
    </dependency>
</dependencies>

<repositories>
    <repository>
        <id>central</id>
        <url>https://repo.maven.apache.org/maven2</url>
    </repository>
</repositories>''', "xml", "Dependencies and an explicit repository declaration"))
    o.append(p("Each dependency has three identifiers: <span class='mono'>groupId</span> (the library's "
               "organization), <span class='mono'>artifactId</span> (the library's name) and "
               "<span class='mono'>version</span>. If no repository is specified, Maven defaults to Maven Central."))
    o.append(fig(fig_resolution(),
                 "How a dependency becomes a classpath entry: the POM is read, the local repository is checked, the "
                 "remote repository is queried, and the artifact — with its own dependencies — is added."))
    o.append(mini("Build, plugins and profiles"))
    o.append(code('''<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>${java.version}</source>
                <target>${java.version}</target>
            </configuration>
        </plugin>
    </plugins>
</build>

<profiles>
    <profile>
        <id>dev</id>
        <properties>
            <environment>development</environment>
            <debug>true</debug>
        </properties>
    </profile>
</profiles>''', "xml", "The build section, a plugin with configuration, and a build profile"))
    o.append(p("Plugins define the build tools — compiler, JAR packager, reporting tools — and "
               "<span class='mono'>configuration</span> customizes how each plugin behaves. A profile is a named set "
               "of settings that is applied only when activated: <span class='mono'>mvn clean install -Pdev</span> "
               "runs the same build with the <span class='mono'>dev</span> profile switched on."))
    o.append(mini("Plugin management and reporting"))
    o.append(code('''<pluginManagement>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.1.2</version>
        </plugin>
    </plugins>
</pluginManagement>

<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-site-plugin</artifactId>
            <version>3.9.1</version>
        </plugin>
    </plugins>
</reporting>''', "xml", "Plugin management and the reporting section"))

    o.append(sec("12.4", "A complete, realistic pom.xml"))
    o.append(p("The listing below is a complete Spring Boot project that can run the JdbcTemplate examples of "
               "Part 13. Read it top to bottom: coordinates first, then properties, then the parent and the one "
               "dependency that brings in Spring JDBC, then the plugin that produces an executable JAR."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.5</version>
        <relativePath/>
    </parent>

    <groupId>com.example</groupId>
    <artifactId>student-jdbc</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>student-jdbc</name>
    <description>JDBC and Spring JDBC examples for Unit 3</description>

    <properties>
        <java.version>17</java.version>
    </properties>

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
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>''', "xml", "A complete Spring Boot pom.xml with Spring JDBC and MySQL"))
    o.append(box("imp", "Important",
                 "<p>Two details in that file are worth pointing out in an examination. Version numbers are missing "
                 "from the dependencies because the <span class='mono'>spring-boot-starter-parent</span> supplies "
                 "them through its own <span class='mono'>dependencyManagement</span> — this is inheritance from the "
                 "parent POM. And <span class='mono'>&lt;scope&gt;runtime&lt;/scope&gt;</span> says the MySQL driver "
                 "is needed when the program runs, but not when it is compiled, because no source file names a "
                 "MySQL class.</p>"))

    o.append(sec("12.5", "The build lifecycle and the standard layout"))
    o.append(p("Maven defines three lifecycles; the one you use every day is the <b>default</b> lifecycle, which "
               "builds and deploys the project. It is an ordered list of phases, and asking for a later phase runs "
               "every earlier one."))
    o.append(fig(fig_lifecycle(),
                 "The default lifecycle. mvn package runs validate, compile and test first — which is why a "
                 "compile error stops a packaging run."))
    o.append(fig(fig_structure(),
                 "The standard directory layout. Because every Maven project looks like this, any Maven user can "
                 "build any Maven project without reading its documentation."))
    o.append(tbl("Commands you will actually type",
                 ["Command", "What it does"],
                 [["<code>mvn clean</code>", "Deletes target/, so the next build starts from nothing"],
                  ["<code>mvn compile</code>", "Compiles src/main/java into target/classes"],
                  ["<code>mvn test</code>", "Compiles and runs the tests; writes surefire reports"],
                  ["<code>mvn package</code>", "Produces target/my-app-1.0.jar (or .war)"],
                  ["<code>mvn install</code>", "Copies the artifact into ~/.m2 so other projects can use it"],
                  ["<code>mvn clean install -Pdev</code>", "A clean build with the dev profile activated"],
                  ["<code>mvn dependency:tree</code>", "Shows why each JAR is on the classpath"]],
                 ["38%", "62%"]))
    o.append(box("trick", "Memory trick",
                 "<p><b>Validate, Compile, Test, Package, Verify, Install, Deploy</b> — "
                 "<i>“Very Clever Teams Pack Verified Installs Daily”.</i> The order is fixed, and every command runs "
                 "the prefix of the list.</p>"))

    o.append(sec("12.6", "Summary"))
    o.append(ul(["Maven is a build automation and project management tool built around the POM.",
                 "pom.xml is the single source of truth: coordinates, dependencies, plugins, profiles.",
                 "The minimal POM needs a modelVersion of 4.0.0 and the three coordinates.",
                 "Every POM inherits from the Super POM, which supplies defaults you never see.",
                 "The default lifecycle runs validate → compile → test → package → verify → install → deploy."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> What does POM stand for, and what is the model version? "
                 "<b>2.</b> Name the three coordinates of an artifact. "
                 "<b>3.</b> What does <span class='mono'>mvn package</span> run before packaging?</p>"
                 "<p class='small'><i>Answers:</i> (1) Project Object Model; 4.0.0. (2) groupId, artifactId, version. "
                 "(3) validate, compile and test.</p>"))
    o.append(recap("Part 12 recap", [
        ["<b>Maven</b>", "Build automation and project management tool driven by the Project Object Model."],
        ["<b>pom.xml</b>", "The single source of truth: identity, dependencies, plugins, profiles, reporting."],
        ["<b>Super POM</b>", "Maven's default POM, inherited by every project, which supplies the defaults."],
        ["<b>Minimum POM</b>", "<span class='mono'>modelVersion 4.0.0</span> plus groupId, artifactId, version."],
        ["<b>Dependency</b>", "groupId + artifactId + version, with an optional scope such as "
                              "<span class='mono'>runtime</span> or <span class='mono'>test</span>."],
        ["<b>Repositories</b>", "Local <span class='mono'>~/.m2</span> first, then the remote repository, defaulting "
                                "to Maven Central."],
        ["<b>Lifecycle</b>", "validate → compile → test → package → verify → install → deploy; a later phase runs the "
                             "earlier ones."],
        ["<b>Profiles</b>", "Named sets of settings activated with <span class='mono'>-P&lt;id&gt;</span> for dev, qa "
                            "or prod."],
        ["<b>Layout</b>", "<span class='mono'>src/main/java</span>, <span class='mono'>src/test/java</span> and "
                          "<span class='mono'>target/</span> are fixed by convention."],
    ], terms=["Maven", "POM", "pom.xml", "groupId", "artifactId", "dependency", "build lifecycle", "plugin", "repository"], practice=[
        "Name the three Maven coordinates of a project.",
        "What is <span class='mono'>modelVersion</span> and what value does it take?",
        "Name the three built-in build lifecycles.",
    ], trap="Omitting <span class='mono'>modelVersion</span>, or mixing dependencies from two different Spring Boot versions."))
    return "".join(o)
