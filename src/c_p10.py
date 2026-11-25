"""PART 10 — XML Fundamentals, DTD and XML Schema."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_tree():
    b = []
    b.append(txt(12, 14, "THE SAME DOCUMENT AS A TREE", 8.4, MUTED, 700, ls="0.1em"))
    # root
    b.append(node(250, 26, 160, 30, "bookstore", None, NAVY, NAVY, WHITE, 9.0, 700))
    b.append(txt(424, 42, "root element", 7.4, NAVY, 700))
    b.append(txt(424, 53, "exactly one, always", 7.0, MUTED, 400))
    b.append(arrow(418, 40, 412, 40, NAVY3, 1.0, hs=4.6))
    # three books
    books = [("book", "category = cooking", 20), ("book", "category = children", 240), ("book", "category = web", 460)]
    for name, attr, x in books:
        b.append(poly([(330, 56), (330, 74), (x + 90, 74), (x + 90, 92)], LINE, 1.0, arrow_end=False))
        b.append(node(x, 92, 180, 32, name, attr, TEAL_L, TEAL, TEAL, 8.8, 700, 7.2))
    b.append(txt(12, 152, "The three books are children of the root, and siblings of one another.",
                 7.2, MUTED, 400))
    # leaves of the middle book
    kids = [("title", "Everyday Italian"), ("author", "Giada De Laurentiis"), ("year", "2005"), ("price", "30.00")]
    for i, (t, v) in enumerate(kids):
        cx = 244 + i * 58
        b.append(line(cx, 124, cx, 168, LINE, 1.0))
        b.append(node(cx - 24, 168, 48, 26, t, None, WHITE, NAVY3, NAVY3, 7.6, 700))
        b.append(txt(cx, 206, v, 6.4, MUTED, 400, "middle"))
    b.append(line(330, 124, 330, 142, LINE, 1.0))
    b.append(line(244, 142, 418, 142, LINE, 1.0))
    b.append(txt(478, 172, "leaves: elements with", 7.2, MUTED, 400))
    b.append(txt(478, 183, "text content and", 7.2, MUTED, 400))
    b.append(txt(478, 194, "no children", 7.2, MUTED, 400))
    b.append(txt(478, 212, "attributes are not", 7.0, MUTED, 400))
    b.append(txt(478, 223, "child nodes", 7.0, MUTED, 400))
    b.append(txt(330, 232, "root \u2192 book \u2192 title / author / year / price is the path the parser walks.",
                 7.4, MUTED, 400, "middle"))
    return svg(660, 240, "".join(b))


def fig_wellformed():
    b = []
    b.append(rect(8, 10, 308, 134, RED_L, RED, 2))
    b.append(txt(24, 32, "NOT WELL-FORMED", 8.6, RED, 700, ls="0.08em"))
    bad = ["<title>Java</Title>", "<author>James</book>", "<price>570"]
    reasons = ["start and end tag differ in case", "tags are not properly nested", "no closing tag"]
    for i, (x, r) in enumerate(zip(bad, reasons)):
        b.append(txt(24, 58 + i * 30, x, 8.0, INK, 400, "start", MONO))
        b.append(txt(186, 58 + i * 30, r, 7.4, MUTED, 400, "start"))

    b.append(rect(340, 10, 312, 134, TEAL_L, TEAL, 2))
    b.append(txt(356, 32, "WELL-FORMED", 8.6, TEAL, 700, ls="0.08em"))
    good = ["<title>Java</title>", "<author>James</author>", "<price>500</price>"]
    for i, g in enumerate(good):
        b.append(txt(356, 58 + i * 30, g, 8.0, INK, 400, "start", MONO))
        b.append(txt(504, 58 + i * 30, "matched, nested, closed", 7.4, TEAL, 400, "start"))

    b.append(arrow(320, 76, 338, 76, NAVY3, 1.4, hs=5.6))
    b.append(txt(330, 168, "well-formed = correct XML syntax", 8.2, NAVY, 700, "middle"))
    b.append(txt(330, 184, "valid = well-formed + conforms to a DTD or an XSD", 8.2, ORANGE, 700, "middle"))
    b.append(txt(330, 202, "Every valid document is well-formed; a well-formed document need not be valid.",
                 7.8, MUTED, 400, "middle"))
    return svg(660, 214, "".join(b))


def fig_validation():
    b = []
    # pipeline with two validators
    b.append(node(12, 40, 120, 50, "XML document", None, NAVY, NAVY, WHITE, 8.6, 700))
    b.append(node(166, 40, 110, 50, "XML parser", "checks syntax", TEAL_L, TEAL, TEAL, 8.4, 700, 7.0))
    b.append(node(310, 40, 130, 50, "validation against", None, WHITE, NAVY3, NAVY3, 8.4, 700))
    b.append(node(474, 16, 170, 40, "DTD  (.dtd)", "elementary grammar", ORANGE_L, ORANGE, ORANGE, 8.4, 700, 7.0))
    b.append(node(474, 76, 170, 40, "XML Schema  (.xsd)", "typed grammar", ORANGE_L, ORANGE, ORANGE, 8.4, 700, 7.0))
    b.append(node(310, 104, 130, 48, "valid or invalid", "with the error message", GREY, LINE, NAVY, 8.0, 700, 6.9))
    b.append(arrow(134, 65, 164, 65, NAVY3, 1.2, hs=5.4))
    b.append(arrow(278, 65, 308, 65, NAVY3, 1.2, hs=5.4))
    b.append(arrow(442, 54, 472, 38, ORANGE, 1.2, hs=5.0))
    b.append(arrow(442, 74, 472, 94, ORANGE, 1.2, hs=5.0))
    b.append(arrow(375, 92, 375, 102, NAVY3, 1.2, hs=5.0))
    b.append(txt(12, 24, "TWO DOORS TO \"VALID\"", 8.4, MUTED, 700, ls="0.1em"))
    b.append(txt(12, 138, "A DTD checks structure only; an XSD also checks data types.",
                 7.4, MUTED, 400))
    return svg(660, 160, "".join(b))


def fig_markup():
    b = []
    b.append(txt(12, 18, "THE SIX KINDS OF MARKUP", 8.4, MUTED, 700, ls="0.1em"))
    rows = [("<?xml version=\"1.0\" encoding=\"UTF-8\"?>", "declaration — optional, always first", TEAL),
            ("<contact_info>", "start tag / element opening", NAVY3),
            ("<name>Rajesh</name>", "element with text content", NAVY3),
            ("<book category=\"cooking\">", "attribute (name = value, value quoted)", ORANGE),
            ("<!-- note -->", "comment", MUTED),
            ("&amp;  &#65;", "entity reference and character reference", ORANGE)]
    for i, (code_, desc, col) in enumerate(rows):
        y = 32 + i * 26
        b.append(rect(12, y, 300, 22, GREY, LINE, 1.5))
        b.append(txt(20, y + 15, code_, 7.4, INK, 400, "start", MONO))
        b.append(arrow(316, y + 11, 332, y + 11, col, 1.0, hs=4.6))
        b.append(txt(340, y + 15, desc, 7.6, col, 600))
    return svg(660, 32 + 6 * 26 + 4, "".join(b))


def html():
    o = []
    o.append(part(10, "XML Fundamentals, DTD and XML Schema",
                  "A language for describing data, two grammars for checking it, and the rules that separate "
                  "\"well-formed\" from \"valid\".", art_icon=10))

    o.append(sec("10.1", "What XML is"))
    o.append(p("XML stands for <b>Extensible Markup Language</b>. It is a text-based markup language derived from "
               "SGML, the Standard Generalized Markup Language, and it is a W3C Recommendation. It is software- and "
               "hardware-independent: a file written on one machine is readable on another, by any language, a "
               "decade later."))
    o.append(box("def", "Definition",
                 "<p><b>XML</b> is a markup language much like HTML, but it was designed to <b>store and transport "
                 "data</b>, and it was designed to be self-descriptive: the tags describe what the data <i>is</i>. "
                 "XML tags identify data and are used to store and organize it, rather than specifying how to "
                 "display it.</p>"))
    o.append(p("Three characteristics make XML useful in a variety of systems, and they are worth memorizing as a "
               "three-part answer:"))
    o.append(ol(["<b>XML is extensible</b> — you can create your own self-descriptive tags, or your own language, "
                 "that suits your application. Nobody has to approve the name <span class='mono'>&lt;student&gt;</span>.",
                 "<b>XML carries the data, it does not present it</b> — the data is stored irrespective of how it "
                 "will be presented, so one document can feed a web page, a PDF and a mobile app.",
                 "<b>XML is a public standard</b> — it was developed by the World Wide Web Consortium and is "
                 "available as an open standard, not owned by a vendor."]))
    o.append(p("The uses listed in the lecture material follow from those three properties: XML can work behind the "
               "scenes to simplify the creation of HTML for large web sites; it can exchange information between "
               "organizations and systems; it can be used for offloading and reloading databases; it can store and "
               "arrange data in ways that suit your own handling needs; it can be merged with style sheets to "
               "produce almost any desired output; and virtually any type of data can be expressed as an XML "
               "document."))

    o.append(sec("10.2", "XML and HTML"))
    o.append(p("The two languages look alike, and their goals are opposite. XML was designed to <b>carry data</b>, "
               "with the focus on what the data is. HTML was designed to <b>display data</b>, with the focus on how "
               "it looks. XML tags are not predefined, whereas every HTML tag already has a meaning to a browser. And "
               "an XML document always forms a tree that starts at a root and branches to the leaves."))
    o.append(tbl("XML compared with HTML",
                 ["Question", "HTML", "XML"],
                 [["Designed for", "Displaying data", "Carrying and storing data"],
                  ["Focus", "How data looks", "What data is"],
                  ["Tag set", "Fixed, predefined", "You invent the tags"],
                  ["Case sensitivity", "Insensitive", "Sensitive"],
                  ["Closing tags", "Optional for some elements", "Mandatory for every element"],
                  ["Errors", "Tolerated, page still renders", "Fatal — the document is rejected"]],
                 ["24%", "38%", "38%"]))
    o.append(box("imp", "Important",
                 "<p>XML will not replace HTML. HTML continues to be the presentation language of the web; XML "
                 "supplies the data behind it, and XSLT (Part 11) is what turns one into the other.</p>"))

    o.append(sec("10.3", "Document structure and syntax rules"))
    o.append(p("A complete XML document looks like this. It contains two kinds of information: <b>markup</b>, such "
               "as <span class='mono'>&lt;contact_info&gt;</span>, and <b>text</b>, such as "
               "<span class='mono'>Rajesh</span>."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<contact_info>
    <name>Rajesh</name>
    <company>TCS</company>
    <phone>9333332354</phone>
</contact_info>''', "xml", "A minimal but complete XML document"))
    o.append(fig(fig_markup(),
                 "The six kinds of markup found in an XML document. A well-formed document uses only these "
                 "constructs, spelled exactly like this."))
    o.append(mini("Element rules"))
    o.append(ul(["Every element must be <b>closed</b>: <span class='mono'>&lt;element&gt;...&lt;/element&gt;</span>, "
                 "or the empty-element form <span class='mono'>&lt;element/&gt;</span>.",
                 "Elements must be <b>properly nested</b>: an end tag must match the most recent unmatched start "
                 "tag, so <span class='mono'>&lt;b&gt;&lt;i&gt;x&lt;/b&gt;&lt;/i&gt;</span> is illegal.",
                 "A document has <b>exactly one root element</b>; two top-level elements are not a document.",
                 "Element names are <b>case sensitive</b>: <span class='mono'>&lt;contact_info&gt;</span> and "
                 "<span class='mono'>&lt;Contact_Info&gt;</span> are different elements."]))
    o.append(mini("Attribute rules"))
    o.append(ul(["An attribute specifies a single property of an element as a name/value pair; an element may have "
                 "several attributes.",
                 "Attribute names are case sensitive, unlike in HTML.",
                 "The same attribute cannot appear twice on one element: "
                 "<span class='mono'>&lt;a b=\"x\" c=\"y\" b=\"z\"&gt;</span> is an error.",
                 "Attribute values <b>must be quoted</b>: <span class='mono'>&lt;a b=x&gt;</span> is an error."]))
    o.append(mini("References and reserved characters"))
    o.append(p("A reference begins with <span class='mono'>&amp;</span> and ends with "
               "<span class='mono'>;</span>. An <b>entity reference</b> contains a name, such as "
               "<span class='mono'>&amp;amp;</span>; a <b>character reference</b> contains "
               "<span class='mono'>#</span> followed by a Unicode number, such as "
               "<span class='mono'>&amp;#65;</span>, which is the letter A. Five characters are reserved by the "
               "syntax itself and must be written as references."))
    o.append(tbl("Reserved characters and their replacement entities",
                 ["Character", "Entity", "Description"],
                 [["<code>&lt;</code>", "<code>&amp;lt;</code>", "less than"],
                  ["<code>&gt;</code>", "<code>&amp;gt;</code>", "greater than"],
                  ["<code>&amp;</code>", "<code>&amp;amp;</code>", "ampersand"],
                  ["<code>'</code>", "<code>&amp;apos;</code>", "apostrophe"],
                  ["<code>\"</code>", "<code>&amp;quot;</code>", "quotation mark"]],
                 ["20%", "24%", "56%"], firstcol=False))
    o.append(box("tip", "Exam tip",
                 "<p>To avoid character-encoding problems, save all XML files as Unicode (UTF-8 or UTF-16). "
                 "Whitespace between elements and attributes is ignored by the parser, which is why XML can be "
                 "indented for human readers without changing its meaning.</p>"))

    o.append(sec("10.4", "The XML tree"))
    o.append(p("XML documents are <b>trees</b>. A tree starts at a root element and branches to child elements, and "
               "each element can have sub-elements. The terms <i>parent</i>, <i>child</i> and <i>sibling</i> "
               "describe the relationships: parents have children, children have parents, and siblings are children "
               "on the same level."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
    <book category="web">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
</bookstore>''', "xml", "The bookstore document used throughout the lecture material"))
    o.append(fig(fig_tree(),
                 "The bookstore document as a tree. bookstore is the root, the three book elements are its "
                 "children and each other's siblings, and title/author/year/price are leaves."))

    o.append(sec("10.5", "Well-formed and valid"))
    o.append(p("These two words are not synonyms, and the difference is a guaranteed examination question."))
    o.append(box("def", "Definition",
                 "<p>An XML document with correct syntax is <b>well-formed</b>. A well-formed document is not "
                 "necessarily <b>valid</b>: a valid document must be well-formed <i>and</i> conform to a document "
                 "type definition — a DTD or an XML Schema.</p>"))
    o.append(fig(fig_wellformed(),
                 "The two verdicts. On the left, three independent syntax faults. On the right, the same data "
                 "written correctly, which is well-formed but still not necessarily valid."))
    o.append(code('''<!-- NOT well-formed: three separate faults -->
<?xml version="1.0"?>
<book>
    <title>Java</Title>          <!-- case mismatch -->
    <author>James</book>         <!-- wrong nesting -->
    <price>570                   <!-- never closed -->
</author>

<!-- well-formed: every tag matched, nested and closed -->
<?xml version="1.0"?>
<book>
    <title>Java</title>
    <author>James</author>
    <price>500</price>
</book>''', "xml", "The lecture's two examples, with each fault annotated"))
    o.append(box("mistake", "Common mistake",
                 "<p>Writing that “a well-formed document is valid”. The implication runs one way only: valid ⇒ "
                 "well-formed. A document can be perfectly well-formed and still be invalid, because “valid” is a "
                 "statement about a grammar, not about syntax.</p>"))

    o.append(sec("10.6", "DTD: the original grammar"))
    o.append(p("An XML DTD — Document Type Definition — is the original way to define the rules, the legal elements "
               "and the attributes of an XML document. It is the basic building block of XML, and its purpose is to "
               "define the structure of a document with a list of legal elements."))
    o.append(code('''<!DOCTYPE book [
    <!ELEMENT book (title, author, price)>
    <!ELEMENT title (#PCDATA)>
    <!ELEMENT author (#PCDATA)>
    <!ELEMENT price (#PCDATA)>
]>''', "xml", "An internal DTD — declared inside the document"))
    o.append(p("The declaration reads as follows: <span class='mono'>!DOCTYPE book</span> defines that the root "
               "element is <span class='mono'>book</span>; <span class='mono'>!ELEMENT book</span> requires the "
               "children <span class='mono'>title, author, price</span> in that order; and each of those elements is "
               "declared to contain parsed character data, <span class='mono'>#PCDATA</span>. Note that "
               "<b>PCDATA</b> means parsable character data, while <b>CDATA</b> means character data that the parser "
               "should not parse."))
    o.append(mini("Internal and external DTDs"))
    o.append(p("There are two kinds of DTD. An <b>internal (embedded) DTD</b> is written inside the document, as "
               "above. An <b>external DTD</b> lives in its own file and is referenced by a SYSTEM identifier, so that "
               "many documents can share one grammar."))
    o.append(code('''<!-- student.dtd - the shared grammar -->
<!ELEMENT student (id, name, age, addr, email)>
<!ELEMENT id    (#PCDATA)>
<!ELEMENT name  (#PCDATA)>
<!ELEMENT age   (#PCDATA)>
<!ELEMENT addr  (#PCDATA)>
<!ELEMENT email (#PCDATA)>''', "xml", "An external DTD saved as student.dtd"))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE student SYSTEM "student.dtd">
<student>
    <id>543</id>
    <name>Ravi</name>
    <age>21</age>
    <addr>Guntur</addr>
    <email>nsr@gmail.com</email>
</student>''', "xml", "A document that references the external DTD"))
    o.append(p("If the document follows the rules of the DTD exactly, it is a <b>valid</b> document; otherwise it is "
               "invalid. The lecture example also shows what happens when it is not: adding a "
               "<span class='mono'>&lt;gender&gt;</span> element to a document whose DTD lists only "
               "id, name, age, addr, email, ph makes the document invalid, even though it is still well-formed."))
    o.append(box("imp", "Important",
                 "<p>With a DTD, independent groups of people can agree to use a standard grammar for interchanging "
                 "data; you can verify that data received from the outside world is valid; and you can verify your "
                 "own data before shipping it. Those three sentences are the lecture's answer to “when to use a "
                 "DTD?”.</p>"))

    o.append(sec("10.7", "XML Schema (XSD)"))
    o.append(p("An XML Schema describes the structure of an XML document, just like a DTD — but it is itself written "
               "in XML, and it can describe <b>data types</b>. It is commonly called XML Schema Definition, or XSD. "
               "It defines the elements, the attributes and the data types, and it supports namespaces. It is "
               "similar to a database schema that describes the data in a database."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="http://www.w3schools.com"
           elementFormDefault="qualified">

    <xs:element name="student">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="name" type="xs:string"/>
                <xs:element name="age"  type="xs:integer"/>
                <xs:element name="addr">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="city"    type="xs:string"/>
                            <xs:element name="pincode" type="xs:long"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="ph" type="xs:integer"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>''', "xml", "student.xsd — the lecture's schema, with the closing tag corrected"))
    o.append(p("Read it from the outside in: <span class='mono'>xs:element name=\"student\"</span> declares the root; "
               "<span class='mono'>xs:complexType</span> says the element has a structure rather than a simple value; "
               "<span class='mono'>xs:sequence</span> fixes the order of the children; and each inner "
               "<span class='mono'>xs:element</span> gives a name and a type, such as "
               "<span class='mono'>xs:string</span> or <span class='mono'>xs:integer</span>. Note that "
               "<span class='mono'>addr</span> is itself complex — it contains city and pincode — which a DTD cannot "
               "express as neatly."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<student xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.w3schools.com student.xsd">
    <name>rajesh</name>
    <age>25</age>
    <addr>
        <city>mylavaram</city>
        <pincode>53333</pincode>
    </addr>
    <ph>9343434</ph>
</student>''', "xml", "A document validated against student.xsd"))
    o.append(box("mistake", "Common mistake",
                 "<p>Two printing errors appear in the slide version of this example, and they matter because the "
                 "document would not validate: the closing tag is written "
                 "<span class='mono'>&lt;/add&gt;</span> instead of "
                 "<span class='mono'>&lt;/addr&gt;</span>, and the instance document does not declare the "
                 "<span class='mono'>xmlns:xsi</span> prefix it uses. Both are corrected above. Copy the corrected "
                 "form into the exam.</p>"))
    o.append(fig(fig_validation(),
                 "The two validation routes. Parsing (well-formedness) always happens first; validation against a "
                 "grammar happens only if parsing succeeds."))
    o.append(tbl("DTD compared with XML Schema",
                 ["Aspect", "DTD", "XML Schema (XSD)"],
                 [["Written in", "Its own syntax", "XML itself"],
                  ["Data types", "Only #PCDATA and simple content models", "Rich types: xs:string, xs:integer, xs:date, ..."],
                  ["Namespaces", "Not supported", "Fully supported"],
                  ["Structure", "Elements and attributes", "Elements, attributes, complex types, groups"],
                  ["Reuse", "Limited entities", "Types can be extended and restricted"],
                  ["Tooling", "Simple, universally supported", "Better for validation and code generation"],
                  ["Typical use", "Legacy systems, quick checks", "Modern systems, web services, Spring config"]],
                 ["22%", "39%", "39%"]))

    o.append(sec("10.8", "Summary"))
    o.append(ul(["XML stores and transports data; HTML displays it.",
                 "Well-formed means correct syntax; valid means well-formed plus conformance to a grammar.",
                 "A document has exactly one root; all elements must be closed, nested and case-matched; attributes "
                 "are quoted and unique per element.",
                 "A DTD declares legal elements and attributes; an XSD does the same with data types and namespaces.",
                 "XSD is itself XML, which is why it can be validated, extended and used by tooling."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Define well-formed and valid, and state which implies which. "
                 "<b>2.</b> Give three differences between a DTD and an XSD. "
                 "<b>3.</b> How many root elements may an XML document have?</p>"
                 "<p class='small'><i>Answers:</i> (1) Well-formed: correct syntax. Valid: well-formed and conforms "
                 "to a DTD or XSD. Valid implies well-formed, not the reverse. (2) XSD is written in XML, supports "
                 "data types, supports namespaces. (3) Exactly one.</p>"))
    o.append(recap("Part 10 recap", [
        ["<b>XML</b>", "A self-descriptive markup language for storing and transporting data."],
        ["<b>XML vs HTML</b>", "Carry data versus display data; invented tags versus a fixed tag set."],
        ["<b>Markup kinds</b>", "Declaration, start tag, element with text, attribute, comment, reference."],
        ["<b>Reserved characters</b>", "<span class='mono'>&lt; &gt; &amp; &apos; &quot;</span> must be written as "
                                       "entities."],
        ["<b>Tree</b>", "One root, children, siblings; attributes belong to their element."],
        ["<b>Well-formed</b>", "Correct syntax — closed, nested, one root, quoted unique attributes."],
        ["<b>Valid</b>", "Well-formed and conforms to a DTD or an XSD."],
        ["<b>DTD</b>", "Its own syntax, element and attribute declarations, <span class='mono'>#PCDATA</span>."],
        ["<b>XSD</b>", "Written in XML, rich data types, namespace aware, extensible. Itself validated."],
    ], terms=["XML", "well-formed", "valid", "DTD", "XML Schema (XSD)", "root element", "attribute", "entity reference", "CDATA"], practice=[
        "Distinguish well-formed from valid in one sentence each.",
        "Write the DTD line that declares an element containing only text.",
        "Give three differences between DTD and XSD.",
    ], trap="Confusing well-formed with valid. Parsing proves the first; only a DTD or XSD proves the second."))
    return "".join(o)
