"""PART 8 — Java Annotations and Spring Boot Annotations."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, VIOLET_L, GOLD, GOLD_L,
                 BLUE_L, MONO, SANS)


def fig_syntax():
    b = []
    b.append(txt(12, 18, "ANATOMY OF AN ANNOTATION", 8.4, MUTED, 700, ls="0.1em"))
    y = 42
    parts = [("@", "@", ORANGE, WHITE, 24), ("Retention", "name of the annotation type", TEAL, WHITE, 96),
             ("(", "(", MUTED, WHITE, 20), ("value", "element", NAVY3, WHITE, 54),
             (" = ", "=", MUTED, WHITE, 26), ("\"runtime\"", "value (optional if single element)", TEAL_L, TEAL, 96),
             (")", ")", MUTED, WHITE, 20)]
    x = 12
    for text_, note_, fill, tc, w in parts:
        b.append(rect(x, y, w, 30, fill, fill if fill in (ORANGE, TEAL, NAVY3, MUTED) else tc, 2))
        b.append(txt(x + w / 2, y + 20, text_, 10.0, tc if fill in (TEAL_L,) else WHITE, 700, "middle", MONO))
        if len(note_) > 2:
            b.append(line(x + w / 2, y + 32, x + w / 2, y + 42, MUTED, 0.7, "2 2"))
            b.append(txtw(x + w / 2, y + 54, note_, w + 46, 7.4, MUTED, 400)[0])
        x += w
    b.append(rect(12, 118, 636, 46, GREY, LINE, 2))
    b.append(txt(24, 137, "Element types allowed:", 8.2, NAVY, 700))
    b.append(txt(150, 137, "primitive, String, Class, enum, annotation, or an array of these", 8.2, INK, 400, "start", MONO))
    b.append(txt(24, 155, "Not allowed:", 8.2, NAVY, 700))
    b.append(txt(90, 155, "null, or any expression that is not a compile-time constant", 8.2, INK, 400))
    return svg(660, 174, "".join(b))


def fig_categories():
    b = []
    cats = [("@TestAnnotation", "marker", "no elements at all — presence is the message", RED),
            ("@TestAnnotation(\"testing\")", "single value", "one element named value, so the name can be omitted", ORANGE),
            ("@TestAnnotation(owner=\"Rahul\", value=\"Class\")", "full", "several key=value pairs", TEAL),
            ("@NonNull  String  s", "type", "annotates a type, not a declaration (Java 8+)", NAVY3),
            ("@Schedule(day=\"Mon\")  @Schedule(day=\"Tue\")", "repeating", "the same annotation twice, via @Repeatable", VIOLET)]
    y = 30
    for code_, name, desc, col in cats:
        b.append(rect(12, y, 636, 40, "#fbfcfd", LINE, 2))
        b.append(rect(12, y, 4, 40, col, col, 0))
        b.append(txt(24, y + 17, code_, 8.2, INK, 600, "start", MONO))
        b.append(txtw(24, y + 32, desc, 400, 7.4, MUTED, 400, "start")[0])
        b.append(pill(548, y + 10, 92, 18, name, WHITE, col, col, 7.2))
        y += 46
    return svg(660, y + 2, "".join(b))


def fig_springbootapp():
    b = []
    b.append(node(180, 12, 300, 44, "@SpringBootApplication", None, NAVY, NAVY, WHITE, 10.0, 700))
    b.append(txt(318, 74, "a shortcut for three annotations, with their default attributes", 7.4, MUTED, 400, "end"))
    trio = [("@SpringBootConfiguration", "marks the class as a source of bean definitions\n(it is a specialised @Configuration)", ORANGE),
            ("@EnableAutoConfiguration", "configures the application by opinionated defaults\nbased on the dependencies on the classpath", TEAL),
            ("@ComponentScan", "scans this package and its sub-packages\nand registers discovered classes as beans", NAVY3)]
    for i, (name, desc, col) in enumerate(trio):
        x = 12 + i * 216
        b.append(poly([(330, 44), (330, 84), (x + 96, 84), (x + 96, 104)], col, 1.2, hs=5.4))
        b.append(node(x, 106, 192, 36, name, None, WHITE, col, col, 8.2, 700))
        b.append(txtw(x + 96, 158, desc, 192, 7.4, MUTED, 400)[0])
    b.append(rect(12, 196, 636, 24, GREY, LINE, 2))
    b.append(txt(330, 212, "One annotation on the main class therefore configures the whole application context.", 8.0, NAVY, 600, "middle"))
    return svg(660, 228, "".join(b))


def fig_startup():
    b = []
    steps = [("main() runs", "SpringApplication.run(App.class, args)"),
             ("scan the package", "@ComponentScan walks com.example and below"),
             ("register beans", "@Component/@Service/etc. become bean definitions"),
             ("auto-configure", "@EnableAutoConfiguration adds DataSource, JdbcTemplate, ..."),
             ("inject", "constructor/field injection wires the beans together"),
             ("start server", "Tomcat starts, the context is ready")]
    y = 16
    for i, (t, s) in enumerate(steps):
        col = TEAL if i in (1, 2) else (ORANGE if i == 3 else NAVY)
        b.append(rect(12, y, 636, 34, "#fbfcfd", col, 2))
        b.append(f'<circle cx="32" cy="{y+17}" r="10" fill="{col}"/>')
        b.append(txt(32, y + 21, str(i + 1), 8.4, WHITE, 700, "middle"))
        b.append(txt(50, y + 21, t, 8.6, NAVY, 700))
        b.append(txt(200, y + 21, s, 8.0, MUTED, 400, "start", MONO))
        y += 40
    return svg(660, y + 2, "".join(b))


def html():
    o = []
    o.append(part(8, "Java Annotations and Spring Boot",
                  "Metadata that changes how code is treated — and the single annotation that bootstraps an "
                  "entire Spring application.", art_icon=8))

    o.append(sec("8.1", "What an annotation is"))
    o.append(p("An annotation is <b>metadata</b>: information about the program, written in the program, that the "
               "compiler or the runtime can read. It is not a comment, because a comment is removed before anything "
               "can act on it, and it is not a statement, because it does not execute. It is a label that other "
               "software reads."))
    o.append(box("def", "Definition",
                 "<p><b>Annotations</b> in Java are a form of metadata that provide additional information about the "
                 "program. They do not change the action of a compiled program, but they can be used by the compiler "
                 "or at run time for processing.</p>"))
    o.append(p("The lecture material lists five key points. Each one is a one-mark answer in itself:"))
    o.append(ol(["Annotations start with <b>@</b>.",
                 "Annotations do not change the action of a compiled program.",
                 "Annotations help to associate metadata — information — with program elements: instance variables, "
                 "constructors, methods, classes.",
                 "Annotations are not pure comments, because they <i>can</i> change the way a program is treated by "
                 "the compiler.",
                 "Annotations provide additional information, so they can be an alternative to XML configuration and "
                 "to Java marker interfaces."]))
    o.append(p("The analogy that makes Spring click: an annotation is a <b>sticky note on a package</b>. The courier "
               "(the framework) reads the note and decides where to send the parcel. The note does not change what "
               "is inside the box; it changes what happens to it."))

    o.append(sec("8.2", "Anatomy and rules"))
    o.append(fig(fig_syntax(),
                 "Anatomy of an annotation. The @ sign, the annotation type name, and an optional parenthesised list "
                 "of element assignments. A single element called value may omit its name."))
    o.append(code('''@Retention(RetentionPolicy.RUNTIME)      // meta-annotation: keep it at run time
@Target({ElementType.METHOD, ElementType.TYPE})
public @interface Audited {              // declare a new annotation type
    String value() default "unknown";    // element with a default
    int level() default 1;
}

@Audited("payment")                      // use it: value = "payment", level = 1
public void transfer() { /* ... */ }''', "java", "Declaring and using a custom annotation"))
    o.append(p("Annotations are read in two different ways. The <b>compiler</b> can check them — that is how "
               "<span class='mono'>@Override</span> catches a misspelled method name. The <b>framework</b> can read "
               "them at run time through reflection — that is how Spring finds "
               "<span class='mono'>@Component</span> classes and wires them together. The retention policy decides "
               "which of the two is possible."))
    o.append(box("imp", "Important",
                 "<p>Retention is the examinable detail. <span class='mono'>SOURCE</span> annotations disappear after "
                 "compilation (used only for compiler checks, like <span class='mono'>@Override</span>); "
                 "<span class='mono'>CLASS</span> ones are in the class file but not visible at run time; "
                 "<span class='mono'>RUNTIME</span> ones are visible through reflection — which is what Spring needs.</p>"))

    o.append(sec("8.3", "The five categories of annotations"))
    o.append(p("The lecture material groups annotations into five categories by <i>shape</i>. The categories are "
               "about how the annotation is written, not about what it means."))
    o.append(fig(fig_categories(),
                 "The five categories. Marker annotations carry no data; single-value annotations have exactly one "
                 "element; full annotations have several; type annotations apply to types; repeating annotations may "
                 "appear more than once on the same element."))
    o.append(tbl("The five categories and their rules",
                 ["Category", "Rule", "Example"],
                 [["Marker", "No elements or values — presence is enough", "<code>@TestAnnotation()</code>"],
                  ["Single value", "One element, so the name can be omitted", "<code>@TestAnnotation(\"testing\")</code>"],
                  ["Full", "Several key=value pairs; all required unless defaults exist",
                   "<code>@TestAnnotation(owner=\"Rahul\", value=\"Class\")</code>"],
                  ["Type", "Applies to types (variables, generics, return types); Java 8+, declared with "
                           "<code>@Target(ElementType.TYPE_USE)</code>", "<code>@NonNull String s</code>"],
                  ["Repeating", "Same annotation applied several times, declared with <code>@Repeatable</code>",
                   "<code>@Schedule(day=\"Monday\") @Schedule(day=\"Tuesday\")</code>"]],
                 ["18%", "50%", "32%"]))

    o.append(sec("8.4", "Annotations built into Java"))
    o.append(tbl("The most common built-in annotations",
                 ["Annotation", "Applies to", "What it tells the compiler"],
                 [["<code>@Override</code>", "Method", "This method overrides one in the supertype; fail if it does not"],
                  ["<code>@Deprecated</code>", "Any declaration", "Do not use this; warn every caller"],
                  ["<code>@SuppressWarnings(\"...\")</code>", "Any declaration", "Do not report the named warnings here"],
                  ["<code>@FunctionalInterface</code>", "Interface", "This interface must have exactly one abstract method"],
                  ["<code>@SafeVarargs</code>", "Method, constructor", "Promise that the varargs use is type-safe"]],
                 ["26%", "20%", "54%"]))

    o.append(sec("8.5", "Spring Boot annotations"))
    o.append(p("Spring Boot annotations are metadata that give instructions to the Spring framework at compile time "
               "or at run time. Instead of complex XML configuration, annotations let developers configure the "
               "application directly in Java code. The lecture material lists the benefits: they reduce XML-based "
               "configuration, improve readability and maintainability, enable auto-configuration, simplify "
               "dependency injection and speed up development."))
    o.append(mini("The one annotation you must know in detail"))
    o.append(p("<span class='mono'>@SpringBootApplication</span> marks the main class of a Spring Boot application. "
               "It is not a primitive: it <b>encapsulates three other annotations</b>, each with its default "
               "attributes. Knowing the three is the difference between memorizing and understanding."))
    o.append(fig(fig_springbootapp(),
                 "One annotation, three responsibilities. The main class of a Spring Boot application carries only "
                 "@SpringBootApplication; the three parts are what actually do the work."))
    o.append(tbl("The three annotations inside @SpringBootApplication",
                 ["Annotation", "Responsibility"],
                 [["<code>@SpringBootConfiguration</code>",
                   "Marks the class as a configuration class — a specialised form of <code>@Configuration</code>. "
                   "There should be only one per application."],
                  ["<code>@EnableAutoConfiguration</code>",
                   "Provides the prominent functionality of Spring Boot: it configures the application using "
                   "opinionated defaults derived from the dependencies present on the classpath. Add "
                   "<span class='mono'>spring-boot-starter-jdbc</span> and a DataSource appears; add MySQL and the "
                   "driver is configured."],
                  ["<code>@ComponentScan</code>",
                   "Performs a full context scan of the package containing the class and all its sub-packages, "
                   "registering every annotated class it finds with the Spring context."]],
                 ["30%", "70%"], firstcol=False))
    o.append(code('''package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication                 // = @SpringBootConfiguration
public class DemoApplication {         // + @EnableAutoConfiguration
    public static void main(String[] args) {   // + @ComponentScan
        SpringApplication.run(DemoApplication.class, args);
    }
}''', "java", "The generated main class of every Spring Boot project"))
    o.append(mini("The individual annotations, written out"))
    o.append(code('''@SpringBootConfiguration
public class AppConfig {
}

@EnableAutoConfiguration
public class AppConfig {
}

@ComponentScan("com.example")
public class AppConfig {
}

@Configuration
public class AppConfig {
    // declares bean definitions; @Bean methods live here
}''', "java", "Each annotation on its own, as the lecture slide shows them"))

    o.append(sec("8.6", "What happens at start-up"))
    o.append(p("Annotations are inert until something reads them. In Spring Boot that something is "
               "<span class='mono'>SpringApplication.run()</span>, and the sequence it performs explains why a "
               "correctly annotated class is enough to start a working application."))
    o.append(fig(fig_startup(),
                 "The start-up sequence. Steps 2 to 4 are driven entirely by annotations; step 5 is dependency "
                 "injection, which is what makes the beans usable."))
    o.append(p("Dependency injection deserves one paragraph here because the slides rely on it implicitly. A bean "
               "does not create its own collaborators; it <b>declares</b> them — as constructor parameters, "
               "usually — and the container supplies instances that it has already built. That is why a DAO can "
               "receive a <span class='mono'>JdbcTemplate</span> without knowing how one is made, and why Part 13's "
               "classes have no <span class='mono'>new JdbcTemplate(...)</span> anywhere."))
    o.append(box("viva", "Interview / Viva",
                 "<p><b>Q.</b> What is the difference between <span class='mono'>@Configuration</span> and "
                 "<span class='mono'>@Component</span>?<br>"
                 "<b>A.</b> <span class='mono'>@Component</span> marks a class for component scanning so that an "
                 "instance becomes a bean. <span class='mono'>@Configuration</span> marks a class as a "
                 "<i>source of bean definitions</i> — it is itself a component, but its purpose is to declare beans "
                 "through <span class='mono'>@Bean</span> methods.</p>"))

    o.append(sec("8.7", "Summary"))
    o.append(ul(["Annotations are metadata that start with @; they do not change what a compiled program does, but "
                 "they change how it is treated.",
                 "The five categories are marker, single value, full, type and repeating.",
                 "@SpringBootApplication = @SpringBootConfiguration + @EnableAutoConfiguration + @ComponentScan.",
                 "@ComponentScan registers beans; @EnableAutoConfiguration configures them from the classpath; "
                 "dependency injection connects them.",
                 "Annotations replace much of the XML configuration of earlier Spring versions."]))
    o.append(box("trick", "Memory trick",
                 "<p><b>S-C-A</b> — <b>S</b>pringBootConfiguration (the class is a configuration), "
                 "<b>C</b>omponentScan (find the beans), <b>A</b>utoConfiguration (guess the rest). Say it once and "
                 "you can unpack @SpringBootApplication for ever.</p>"))
    o.append(recap("Part 8 recap", [
        ["<b>Annotation</b>", "Metadata prefixed with <span class='mono'>@</span>; read by the compiler or a framework, not executed."],
        ["<b>Five categories</b>", "Marker, single-value, full, type, repeating."],
        ["<b>Retention</b>", "<span class='mono'>SOURCE</span> (discarded), <span class='mono'>CLASS</span> (in the file, not at runtime), <span class='mono'>RUNTIME</span> (visible to reflection)."],
        ["<b>@SpringBootApplication</b>", "A shortcut that bundles Configuration, EnableAutoConfiguration and ComponentScan."],
        ["<b>@ComponentScan</b>", "Finds <span class='mono'>@Component</span> classes in the package and below, and registers them as beans."],
        ["<b>@Autowired</b>", "Asks the container for a matching bean instead of calling <span class='mono'>new</span>."],
    ], terms=["annotation", "marker annotation", "@Retention", "@Target", "SOURCE retention", "RUNTIME retention", "@SpringBootConfiguration", "@EnableAutoConfiguration", "@ComponentScan"], practice=[
        "Unpack <span class='mono'>@SpringBootApplication</span> into three annotations.",
        "Name the five categories of annotation.",
        "What changes if retention is <span class='mono'>SOURCE</span> instead of <span class='mono'>RUNTIME</span>?",
    ], trap="Expecting <span class='mono'>@Autowired</span> to work in a class you created with <span class='mono'>new</span>; Spring never sees that object."))
    return "".join(o)
