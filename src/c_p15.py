"""PART 15 — POJO and JavaBean."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_pojo_bean():
    b = []
    b.append(txt(12, 16, "TWO CONCENTRIC IDEAS", 8.4, MUTED, 700, ls="0.1em"))
    b.append(rect(12, 28, 636, 176, "#fbfcfd", NAVY3, 2))
    b.append(txt(24, 46, "POJO — plain old Java object", 8.6, NAVY, 700))
    b.append(txt(24, 60, "no framework interface, no annotation required, no base class", 7.4, MUTED, 400))
    b.append(rect(36, 72, 588, 110, "#f6fbfc", TEAL, 2))
    b.append(txt(48, 90, "JavaBean — a POJO that follows three more rules", 8.4, TEAL, 700))
    rules = [("public class with a public no-argument constructor", "so a framework can instantiate it"),
             ("private fields exposed through getX() and setX()", "so access is controlled"),
             ("implements Serializable", "so its state can be written to a stream")]
    for i, (r, why) in enumerate(rules):
        y = 112 + i * 22
        b.append(txt(52, y, "·", 8.4, TEAL, 700))
        b.append(txt(62, y, r, 7.6, INK, 400))
        b.append(txt(330, y, why, 7.2, MUTED, 400))
    b.append(txt(330, 196, "Every JavaBean is a POJO. Not every POJO is a JavaBean.", 7.8, NAVY, 600, "middle"))
    return svg(660, 208, "".join(b))


def fig_two_classes():
    b = []
    b.append(txt(12, 16, "THE SAME DATA, TWO STYLES", 8.4, MUTED, 700, ls="0.1em"))
    b.append(rect(12, 30, 310, 200, "#fbfcfd", ORANGE, 2))
    b.append(txt(24, 48, "POJO", 8.4, ORANGE, 700))
    pojo = ["public class Employee {",
            "    public String name;",
            "    public int age;",
            "",
            "    public Employee() { }",
            "}",
            "",
            "// usage",
            "Employee e = new Employee();",
            "e.name = \"Ravi\";",
            "e.age = 30;"]
    for i, l in enumerate(pojo):
        b.append(txt(24, 68 + i * 13, l, 7.4, INK, 400, "start", MONO))
    b.append(rect(340, 30, 308, 200, "#fbfcfd", TEAL, 2))
    b.append(txt(352, 48, "JavaBean", 8.4, TEAL, 700))
    bean = ["public class Employee implements Serializable {",
            "    private String name;",
            "    private int age;",
            "",
            "    public Employee() { }",
            "    public String getName() { return name; }",
            "    public void setName(String n) { name = n; }",
            "    public int getAge() { return age; }",
            "    public void setAge(int a) { age = a; }",
            "}",
            "",
            "Employee e = new Employee();",
            "e.setName(\"Ravi\");  e.setAge(30);"]
    for i, l in enumerate(bean):
        b.append(txt(352, 68 + i * 12.4, l, 6.9, INK, 400, "start", MONO))
    b.append(txt(330, 246, "The bean's fields are hidden, the pojo's are not — and that is the whole difference in practice.",
                 7.6, MUTED, 400, "middle"))
    return svg(660, 256, "".join(b))


def html():
    o = []
    o.append(part(15, "POJO and JavaBean",
                  "Two words that are used interchangeably and are not the same thing — with the three rules "
                  "that separate them.", art_icon=15))

    o.append(sec("15.1", "POJO"))
    o.append(p("POJO stands for <b>Plain Old Java Object</b>. The name is a reaction to the early 2000s, when "
               "frameworks required classes to extend their base class or implement their interfaces. A POJO is a "
               "class that is ordinary: it has fields, a constructor and methods, and it depends on nothing but the "
               "JDK."))
    o.append(box("def", "Definition",
                 "<p>A <b>POJO</b> is a plain Java object that does not extend any framework-specific class, does not "
                 "implement any framework-specific interface, and does not require any annotation to be usable. It "
                 "contains business data and behaviour and nothing that ties it to a container.</p>"))
    o.append(fig(fig_two_classes(),
                 "The same employee, written as a POJO and as a JavaBean. Both compile, both hold the same data; the "
                 "bean controls access through methods."))

    o.append(sec("15.2", "JavaBean: a POJO with conventions"))
    o.append(p("A JavaBean is a POJO that follows three additional conventions. The conventions exist for one "
               "reason: they make the object <b>discoverable and instantiable by a framework</b> through reflection. "
               "If a class has a public no-argument constructor and public getters and setters, a container can "
               "create it and populate it without knowing anything else about it."))
    o.append(fig(fig_pojo_bean(),
                 "The relationship between the two ideas. POJO is the outer set; JavaBean is the inner set defined "
                 "by the three conventions."))
    o.append(ol(["It is a <b>public class</b> with a <b>public no-argument constructor</b>.",
                 "Its fields are <b>private</b> and are exposed through <b>getter and setter methods</b> following "
                 "the naming convention <span class='mono'>getX()</span> / <span class='mono'>setX()</span> (and "
                 "<span class='mono'>isX()</span> for booleans).",
                 "It <b>implements Serializable</b>, so its state can be persisted or sent across a network."]))
    o.append(code('''import java.io.Serializable;

public class Student implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;              // private fields
    private String name;
    private boolean active;      // boolean getters use isX()

    public Student() { }         // public no-argument constructor

    public Student(int id, String name) {   // extra constructors are allowed
        this.id = id;
        this.name = name;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public boolean isActive() { return active; }
    public void setActive(boolean active) { this.active = active; }
}''', "java", "A textbook JavaBean"))
    o.append(box("imp", "Important",
                 "<p>Three naming rules decide whether your getters are discoverable: "
                 "<span class='mono'>getName()</span> maps to the property <b>name</b>; "
                 "<span class='mono'>isActive()</span> — not <span class='mono'>getActive()</span> — is the "
                 "convention for a <span class='mono'>boolean</span>; and a setter's parameter type must match its "
                 "getter's return type. Frameworks such as Jackson and Spring rely on exactly these rules.</p>"))

    o.append(sec("15.3", "Why the distinction matters in this unit"))
    o.append(p("Two sections of this textbook depend on JavaBean conventions without ever spelling them out. "
               "Spring's dependency injection populates a bean by calling setters, or by constructor injection when "
               "only a constructor exists. Spring's property editors, the older XML configuration of Part 14, and "
               "JSON serialization all read properties through the getter/setter pairs. A POJO with public fields "
               "works when you write all the code yourself; a JavaBean works when a <b>framework</b> has to write "
               "some of it for you."))
    o.append(tbl("JavaBean compared with a generic POJO",
                 ["Aspect", "POJO", "JavaBean"],
                 [["Full form", "Plain Old Java Object", "A POJO following the bean conventions"],
                  ["Rules", "None beyond valid Java", "Public class, public no-arg constructor, private fields with "
                                                        "getters/setters, Serializable"],
                  ["Field access", "Public fields are allowed", "Fields must be private"],
                  ["Framework friendly", "Not necessarily", "Yes — can be instantiated and populated by reflection"],
                  ["Typical use", "Data holder inside your own code", "Spring beans, JPA entities, DTOs in JSON APIs"],
                  ["Example", "<code>class E { public String name; }</code>",
                   "<code>class E { private String name; public String getName() {...} }</code>"]],
                 ["22%", "34%", "44%"]))
    o.append(box("mistake", "Common mistake",
                 "<p>Writing “a JavaBean is a POJO” as if that were the definition. A JavaBean is a POJO <i>plus</i> "
                 "conventions; the correct one-line answer is “a JavaBean is a special POJO that follows naming and "
                 "construction conventions”.</p>"))
    o.append(mini("Spring's use of the word “bean”"))
    o.append(p("One more source of confusion must be cleared up before an examination. In Spring, a <b>bean</b> is "
               "not necessarily a JavaBean in the strict sense: it is any object whose lifecycle is managed by the "
               "Spring container. A Spring bean may be created by a <span class='mono'>@Bean</span> method, by "
               "component scanning, or by an XML declaration, and it may or may not follow the getter/setter "
               "conventions. When the slides say “Spring bean”, read “container-managed object”; when they say "
               "“JavaBean”, read “class following the three conventions”."))

    o.append(sec("15.4", "Summary"))
    o.append(ul(["A POJO is an ordinary Java class with no framework dependencies.",
                 "A JavaBean is a POJO that adds a public no-arg constructor, private fields with getters and "
                 "setters, and Serializable.",
                 "The conventions exist so containers can create and populate objects by reflection.",
                 "Boolean getters use <span class='mono'>isX()</span>, not <span class='mono'>getX()</span>.",
                 "A Spring bean is a container-managed object, which is a different idea from a JavaBean."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> State the three JavaBean conventions. "
                 "<b>2.</b> Is every JavaBean a POJO? Is every POJO a JavaBean? "
                 "<b>3.</b> Why does a no-argument constructor matter to a framework?</p>"
                 "<p class='small'><i>Answers:</i> (1) Public class with a public no-arg constructor; private fields "
                 "with getters and setters; implements Serializable. (2) Yes; no. (3) Because the container must be "
                 "able to create the object before it can inject anything into it.</p>"))
    o.append(recap("Part 15 recap", [
        ["<b>POJO</b>", "A plain Java object: no framework base class, no special interface — just fields and methods."],
        ["<b>JavaBean</b>", "A POJO plus three conventions: public no-arg constructor, private fields with getters and setters, <span class='mono'>implements Serializable</span>."],
        ["<b>Naming rule</b>", "A field <span class='mono'>name</span> becomes <span class='mono'>getName()</span> and <span class='mono'>setName()</span> — capital first letter."],
        ["<b>Why frameworks care</b>", "They create the object with the no-arg constructor, then inject through setters."],
        ["<b>Relationship</b>", "Every JavaBean is a POJO; not every POJO is a JavaBean."],
    ], terms=["POJO", "JavaBean", "no-arg constructor", "getter", "setter", "Serializable", "encapsulation", "convention", "record"], practice=[
        "State the three JavaBean conventions.",
        "Is every POJO a JavaBean? Answer in one line.",
        "Why does a container need a no-argument constructor?",
    ], trap="Calling a class a JavaBean when its fields are public or it has no no-argument constructor."))
    return "".join(o)
