"""PART 11 — XML Namespaces, XSLT and the XML DOM."""
from common import *
from dia import (svg, txt, txtw, rect, line, arrow, poly, node, note, pill, legend, head,
                 NAVY, NAVY2, NAVY3, TEAL, TEAL2, TEAL_L, TEAL_M, ORANGE, ORANGE_L, ORANGE_M,
                 INK, MUTED, LINE, GREY, GREY2, RED, RED_L, WHITE, VIOLET, GOLD, GOLD_L, BLUE_L,
                 MONO, SANS)


def fig_conflict():
    b = []
    b.append(txt(12, 18, "ONE NAME, TWO MEANINGS", 8.4, MUTED, 700, ls="0.1em"))
    # left fragment
    b.append(rect(12, 30, 200, 126, "#fbfcfd", NAVY3, 2))
    b.append(txt(112, 48, "from the HTML world", 7.6, NAVY3, 700, "middle"))
    b.append(txt(24, 70, "<table>", 8.0, INK, 400, "start", MONO))
    b.append(txt(34, 84, "<tr><td>Apples</td>", 8.0, INK, 400, "start", MONO))
    b.append(txt(34, 98, "<td>Bananas</td></tr>", 8.0, INK, 400, "start", MONO))
    b.append(txt(24, 112, "</table>", 8.0, INK, 400, "start", MONO))
    b.append(txt(24, 136, "a layout table", 7.2, MUTED, 400))
    # right fragment
    b.append(rect(232, 30, 200, 126, "#fbfcfd", ORANGE, 2))
    b.append(txt(332, 48, "from the furniture world", 7.6, ORANGE, 700, "middle"))
    b.append(txt(244, 70, "<table>", 8.0, INK, 400, "start", MONO))
    b.append(txt(254, 84, "<name>African Coffee</name>", 7.4, INK, 400, "start", MONO))
    b.append(txt(254, 98, "<width>80</width>", 7.4, INK, 400, "start", MONO))
    b.append(txt(244, 112, "</table>", 8.0, INK, 400, "start", MONO))
    b.append(txt(244, 136, "a piece of furniture", 7.2, MUTED, 400))
    b.append(arrow(214, 93, 230, 93, RED, 1.4, hs=6.0))
    b.append(txt(320, 166, "Put them together and the application cannot tell the two <table> elements apart.",
                 7.8, RED, 600, "middle"))
    # solution
    b.append(rect(452, 30, 196, 126, TEAL_L, TEAL, 2))
    b.append(txt(550, 48, "with prefixes", 7.6, TEAL, 700, "middle"))
    b.append(txt(462, 70, "<h:table>", 8.0, TEAL, 700, "start", MONO))
    b.append(txt(472, 84, "<h:td>Apples</h:td>", 7.4, INK, 400, "start", MONO))
    b.append(txt(462, 98, "</h:table>", 8.0, TEAL, 700, "start", MONO))
    b.append(txt(462, 112, "<f:table>", 8.0, ORANGE, 700, "start", MONO))
    b.append(txt(472, 126, "<f:width>80</f:width>", 7.4, INK, 400, "start", MONO))
    b.append(txt(462, 140, "</f:table>", 8.0, ORANGE, 700, "start", MONO))
    b.append(txt(320, 182, "The prefix makes the two names different, so both can coexist in one document.",
                 7.8, TEAL, 600, "middle"))
    return svg(660, 200, "".join(b))


def fig_ns_scope():
    b = []
    b.append(txt(12, 18, "NAMESPACE RESOLUTION AND SCOPE", 8.4, MUTED, 700, ls="0.1em"))
    b.append(node(12, 40, 250, 150, None, None, WHITE, LINE, INK, 8, 400))
    b.append(txt(24, 62, "<root>", 8.2, NAVY, 700, "start", MONO))
    b.append(rect(30, 74, 220, 52, TEAL_L, TEAL, 2))
    b.append(txt(38, 90, "<h:table", 7.8, TEAL, 700, "start", MONO))
    b.append(txt(46, 104, "  xmlns:h=\".../TR/html4/\">", 7.3, TEAL, 400, "start", MONO))
    b.append(txt(38, 118, "  <h:td>Apples</h:td>", 7.3, INK, 400, "start", MONO))
    b.append(rect(30, 132, 220, 50, ORANGE_L, ORANGE, 2))
    b.append(txt(38, 148, "<f:table", 7.8, ORANGE, 700, "start", MONO))
    b.append(txt(46, 162, "  xmlns:f=\"https://.../furniture\">", 7.3, ORANGE, 400, "start", MONO))
    b.append(txt(38, 176, "  <f:width>80</f:width>", 7.3, INK, 400, "start", MONO))
    b.append(txt(24, 200, "</root>", 8.2, NAVY, 700, "start", MONO))

    b.append(arrow(266, 100, 292, 78, TEAL2, 1.2, hs=5.4))
    b.append(arrow(266, 156, 292, 178, ORANGE, 1.2, hs=5.4))
    b.append(rect(296, 50, 200, 56, TEAL_L, TEAL, 2))
    b.append(txt(306, 68, "prefix h →", 7.6, TEAL, 700))
    b.append(txt(306, 82, "http://www.w3.org/TR/html4/", 6.9, INK, 400, "start", MONO))
    b.append(txt(306, 96, "inherited by h:td", 7.0, TEAL, 400))
    b.append(rect(296, 150, 200, 56, ORANGE_L, ORANGE, 2))
    b.append(txt(306, 168, "prefix f →", 7.6, ORANGE, 700))
    b.append(txt(306, 182, "https://www.w3schools.com/furniture", 6.6, INK, 400, "start", MONO))
    b.append(txt(306, 196, "inherited by f:width", 7.0, ORANGE, 400))

    b.append(rect(510, 50, 138, 156, "#fbfcfd", LINE, 2))
    b.append(txt(520, 68, "Rules", 7.8, NAVY, 700))
    b.append(txtw(520, 86, "A prefix must be declared before it is used.", 120, 7.2, MUTED, 400, "start")[0])
    b.append(txtw(520, 118, "The declaration applies to the element and all its descendants.", 120, 7.2, MUTED, 400, "start")[0])
    b.append(txtw(520, 162, "A later redeclaration wins inside its own subtree.", 120, 7.2, MUTED, 400, "start")[0])
    return svg(660, 214, "".join(b))


def fig_xslt():
    b = []
    b.append(node(12, 40, 130, 56, "book.xml", "source tree", NAVY, NAVY, WHITE, 8.8, 700, 7.2, "#d5e2ee"))
    b.append(node(184, 40, 130, 56, "book.xsl", "stylesheet, uses XPath", TEAL_L, TEAL, TEAL, 8.8, 700, 7.2))
    b.append(node(366, 40, 120, 56, "XSLT processor", None, ORANGE_L, ORANGE, ORANGE, 8.6, 700))
    b.append(node(526, 40, 122, 56, "result", "HTML or XML", WHITE, NAVY3, NAVY3, 8.8, 700, 7.2))
    b.append(arrow(144, 68, 182, 68, NAVY3, 1.3, hs=5.8))
    b.append(arrow(316, 68, 364, 68, TEAL, 1.3, hs=5.8))
    b.append(arrow(488, 68, 524, 68, ORANGE, 1.3, hs=5.8))
    b.append(rect(12, 118, 636, 56, GREY, LINE, 2))
    b.append(txt(24, 136, "XSL", 7.8, NAVY, 700))
    b.append(txt(56, 136, "= the family of style-sheet languages for XML;", 7.8, INK, 400))
    b.append(txt(24, 152, "XSLT", 7.8, NAVY, 700))
    b.append(txt(56, 152, "= XSL Transformations, the most important part of XSL: it transforms one XML document into another.", 7.8, INK, 400))
    b.append(txt(24, 166, "XPath", 7.8, NAVY, 700))
    b.append(txt(66, 166, "= the language XSLT uses to navigate and select nodes in the source tree.", 7.8, INK, 400))
    b.append(txt(330, 196, "CSS styles HTML for a browser; XSLT transforms XML into HTML (or into any other XML).",
                 7.6, MUTED, 400, "middle"))
    return svg(660, 204, "".join(b))


def fig_dom():
    b = []
    b.append(txt(12, 18, "THE DOCUMENT AS A TREE OF NODES", 8.4, MUTED, 700, ls="0.1em"))
    b.append(node(270, 32, 120, 28, "bookstore", None, NAVY, NAVY, WHITE, 8.4, 700))
    b.append(line(330, 60, 180, 84, LINE, 1.0))
    b.append(node(120, 84, 120, 28, "book", "element node", TEAL_L, TEAL, TEAL, 8.0, 700, 6.8))
    b.append(node(270, 84, 120, 28, "book", "element node", TEAL_L, TEAL, TEAL, 8.0, 700, 6.8))
    b.append(node(420, 84, 120, 28, "book", "element node", TEAL_L, TEAL, TEAL, 8.0, 700, 6.8))
    b.append(line(500, 60, 500, 84, LINE, 1.0))
    b.append(line(330, 60, 480, 84, LINE, 1.0))
    # children of first book
    for i, (t, v) in enumerate([("title", "Java"), ("author", "James"), ("year", "1991")]):
        x = 40 + i * 110
        b.append(line(180, 112, x + 45, 140, LINE, 1.0))
        b.append(node(x, 140, 90, 26, t, None, WHITE, NAVY3, NAVY3, 7.8, 700))
        b.append(node(x, 176, 90, 26, "\"" + v + "\"", "text node", GREY, LINE, MUTED, 7.4, 400, 6.6))
        b.append(arrow(x + 45, 166, x + 45, 175, LINE, 0.9, hs=4.2))
    # property callouts
    b.append(rect(404, 132, 244, 100, "#fbfcfd", LINE, 2))
    b.append(txt(416, 150, "Node properties", 7.8, NAVY, 700))
    props = ["nodeName — the name of x", "nodeValue — the value of x", "parentNode — parent of x",
             "childNodes — children of x", "attributes — attribute nodes of x"]
    for i, p_ in enumerate(props):
        b.append(txt(416, 166 + i * 12, "· " + p_, 7.0, INK, 400))
    b.append(txt(330, 250, "Every element, every attribute and every piece of text is a node. Navigation is the same",
                 7.6, MUTED, 400, "middle"))
    b.append(txt(330, 262, "operation at every level, which is why the DOM is described as a uniform tree.", 7.6, MUTED, 400, "middle"))
    return svg(660, 270, "".join(b))


def html():
    o = []
    o.append(part(11, "XML Namespaces, XSLT and the XML DOM",
                  "How XML avoids name collisions, how it is transformed for display, and how a program "
                  "walks it node by node.", art_icon=11))

    o.append(sec("11.1", "The name-conflict problem"))
    o.append(p("In XML the element names are defined by the developer, not by a standard. That freedom creates a "
               "collision: two documents from two different systems may use the same element name for completely "
               "different things, and a program that receives both cannot tell them apart."))
    o.append(p("The lecture's example is a <span class='mono'>table</span>. In one document it is an HTML layout "
               "table; in another it is a piece of furniture with a name, a width and a length. If those fragments "
               "are combined, there are two <span class='mono'>table</span> elements with different content and "
               "different meaning, and neither a user nor an application knows how to handle the difference."))
    o.append(fig(fig_conflict(),
                 "Left and centre: the same element name for two unrelated concepts. Right: the same two fragments "
                 "with prefixes, which makes the names distinct and the collision impossible."))

    o.append(sec("11.2", "Prefixes and the xmlns attribute"))
    o.append(p("The fix is a <b>prefix</b>, and a prefix must be <b>declared</b>. The declaration is an attribute "
               "called <span class='mono'>xmlns:prefix</span> whose value is a URI; that URI is the "
               "<b>namespace</b> — a name space that is guaranteed to be unique because it is owned by an "
               "organization."))
    o.append(code('''<root>
    <h:table xmlns:h="http://www.w3.org/TR/html4/">
        <h:tr>
            <h:td>Apples</h:td>
            <h:td>Bananas</h:td>
        </h:tr>
    </h:table>

    <f:table xmlns:f="https://www.w3schools.com/furniture">
        <f:name>African Coffee Table</f:name>
        <f:width>80</f:width>
        <f:length>120</f:length>
    </f:table>
</root>''', "xml", "Two namespaces in one document — the lecture's example"))
    o.append(p("The <span class='mono'>xmlns:h</span> attribute gives the prefix <span class='mono'>h:</span> a "
               "qualified namespace, and <span class='mono'>xmlns:f</span> does the same for "
               "<span class='mono'>f:</span>. Because the two table elements now have different qualified names, "
               "there is no conflict."))
    o.append(fig(fig_ns_scope(),
                 "Namespace resolution. The declaration is attached to one element and inherited by its "
                 "descendants, so <span class='mono'>h:td</span> belongs to the HTML namespace without repeating "
                 "the declaration."))
    o.append(box("imp", "Important",
                 "<p>The URI is a <b>name</b>, not an address. The parser never downloads "
                 "<span class='mono'>http://www.w3.org/TR/html4/</span>; it only compares the string. That is why a "
                 "namespace URI should be stable and controlled by the organization that defines the vocabulary.</p>"))
    o.append(mini("Default namespaces"))
    o.append(code('''<!-- declare a default namespace: no prefix needed on elements -->
<student xmlns="http://www.example.com/school">
    <name>Rajesh</name>
    <age>25</age>
</student>

<!-- elements from a different namespace keep their prefix -->
<student xmlns="http://www.example.com/school"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.example.com/school student.xsd">
    <name>Rajesh</name>
</student>''', "xml", "A default namespace, and a second namespace declared only where it is needed"))
    o.append(box("mistake", "Common mistake",
                 "<p>Confusing a namespace with a schema location. <span class='mono'>xmlns</span> says <i>which "
                 "vocabulary</i> a name belongs to; <span class='mono'>xsi:schemaLocation</span> says <i>where the "
                 "grammar for that vocabulary can be found</i>. The first is required for correctness, the second is "
                 "a hint for validation.</p>"))

    o.append(sec("11.3", "XSLT: turning XML into something displayable"))
    o.append(p("XML does not use predefined tags, so a browser has no idea what a "
               "<span class='mono'>&lt;table&gt;</span> means — it could be furniture. HTML has predefined tags and "
               "CSS styles them; XML has neither, so it needs both a vocabulary for presentation and a way to "
               "transform one document into another."))
    o.append(p("<b>XSL</b> — EXtensible Stylesheet Language — is the styling language for XML; the analogy in the "
               "lecture material is <i>XSL is to XML what CSS is to HTML</i>. <b>XSLT</b> stands for XSL "
               "Transformations and is the most important part of XSL: it transforms an XML document into another "
               "XML document, uses XPath to navigate, and is a W3C Recommendation."))
    o.append(fig(fig_xslt(),
                 "The XSLT transformation. The source tree and the stylesheet are both inputs; the processor "
                 "produces a result tree, which is usually HTML but may be any XML."))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="book.xsl"?>
<book_store>
    <book>
        <title>JAVA</title>
        <author>James</author>
    </book>
    <book>
        <title>DBMS</title>
        <author>Raghu</author>
    </book>
</book_store>''', "xml", "book.xml — the source document, linked to its stylesheet"))
    o.append(code('''<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <body>
                <h2>Book Details</h2>
                <table border="1">
                    <tr><th>Title</th><th>Author</th></tr>
                    <xsl:for-each select="book_store/book">
                        <tr>
                            <td><xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="author"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>''', "xml", "book.xsl — the stylesheet"))
    o.append(raw_code('''Book Details
+-------------+-------------+
| Title       | Author      |
+-------------+-------------+
| JAVA        | James       |
| DBMS        | Raghu       |
+-------------+-------------+''', "What the browser renders when book.xml is opened"))
    o.append(p("Three elements do all the work. <span class='mono'>xsl:template match=\"/\"</span> matches the "
               "document root — the template that is applied to start the transformation. "
               "<span class='mono'>xsl:for-each select=\"book_store/book\"</span> iterates over the nodes selected by "
               "an XPath expression. <span class='mono'>xsl:value-of select=\"title\"</span> extracts the text value "
               "of a node. Everything else in the file is literal HTML, copied to the output unchanged."))

    o.append(sec("11.4", "The XML DOM"))
    o.append(p("The DOM — Document Object Model — is a standard for accessing and manipulating documents. The HTML "
               "DOM presents an HTML document as a tree and lets scripts change it; the XML DOM does the same for "
               "XML. It is a standard object model, a standard programming interface, platform- and "
               "language-independent, and a W3C standard."))
    o.append(box("def", "Definition",
                 "<p>The <b>XML DOM</b> is a standard for how to get, change, add or delete XML elements. It models "
                 "an XML document as a set of <b>node objects</b>, which can be accessed with JavaScript or any other "
                 "programming language through a standard set of properties and methods.</p>"))
    o.append(p("The distinction that the lecture material draws is worth keeping: <b>properties</b> are things that "
               "<i>are</i> (the node name of this node is \"book\"), and <b>methods</b> are things that are "
               "<i>done</i> (delete the node called \"book\")."))
    o.append(fig(fig_dom(),
                 "An XML document as a tree of nodes. Element nodes, text nodes and attribute nodes all share the "
                 "same navigation properties, which is what makes the DOM uniform."))
    o.append(tbl("XML DOM properties and methods",
                 ["Member", "Kind", "Meaning"],
                 [["<code>x.nodeName</code>", "property", "The name of x"],
                  ["<code>x.nodeValue</code>", "property", "The value of x"],
                  ["<code>x.parentNode</code>", "property", "The parent node of x"],
                  ["<code>x.childNodes</code>", "property", "The child nodes of x"],
                  ["<code>x.attributes</code>", "property", "The attribute nodes of x"],
                  ["<code>x.getElementsByTagName(name)</code>", "method", "All elements with the given tag name"],
                  ["<code>x.appendChild(node)</code>", "method", "Insert a child node into x"],
                  ["<code>x.removeChild(node)</code>", "method", "Remove a child node from x"],
                  ["<code>document.getElementById(id)</code>", "method", "The element with the given id"]],
                 ["38%", "14%", "48%"]))

    o.append(sec("11.5", "Parsing XML in a program"))
    o.append(p("The browser example in the lecture material shows the mechanics in three lines: build a string of "
               "XML, parse it into a document, then navigate by tag name and index."))
    o.append(code('''<html><body>
<p id="demo">this is paragraph text</p>
<button type="button" onclick="myfun()">click me</button>
<script>
function myfun() {
    var text, parser, xmlDoc;
    text = "<bookstore><book>" +
           "<title>Java</title><author>James</author><year>1991</year>" +
           "<book><title>DBMS</title><author>Raghu</author><year>1970</year></book>" +
           "</book></bookstore>";
    parser = new DOMParser();
    xmlDoc = parser.parseFromString(text, "text/xml");
    document.getElementById("demo").innerHTML =
        xmlDoc.getElementsByTagName("year")[0].childNodes[0].nodeValue;
}
</script>
</body></html>''', "html", "The DOM example from the lecture material (output: 1991)"))
    o.append(p("The chain in the last line reads exactly as the tree does: "
               "<span class='mono'>getElementsByTagName(\"year\")[0]</span> takes the first "
               "<span class='mono'>year</span> element, <span class='mono'>childNodes[0]</span> takes its first child "
               "— which is the text node — and <span class='mono'>nodeValue</span> reads the text itself."))
    o.append(box("mistake", "Common mistake",
                 "<p>The slide fragment above is missing a closing tag on the first book: the string reads "
                 "<span class='mono'>&lt;book&gt;...&lt;year&gt;1991&lt;/year&gt;&lt;book&gt;</span>, so the second "
                 "opening <span class='mono'>book</span> should be "
                 "<span class='mono'>&lt;/book&gt;&lt;book&gt;</span>. A DOM parser would usually still recover, "
                 "but the document is not well-formed — exactly the distinction of Part 10.</p>"))
    o.append(mini("The same idea in Java"))
    o.append(code('''import javax.xml.parsers.*;
import org.w3c.dom.*;

public class DomRead {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(new java.io.File("book.xml"));

        NodeList books = doc.getElementsByTagName("title");
        for (int i = 0; i < books.getLength(); i++) {
            Element e = (Element) books.item(i);
            System.out.println(e.getTextContent());       // JAVA, DBMS
        }
    }
}''', "java", "Reading book.xml with the JDK's own DOM parser"))
    o.append(p("The Java version is the same three ideas — parse, select, read — with explicit types. The JDK ships "
               "the parser in <span class='mono'>javax.xml.parsers</span>; the DOM interfaces it returns are the "
               "W3C's <span class='mono'>org.w3c.dom</span>, which is why the code looks the same in every language "
               "that implements the standard."))
    o.append(box("tip", "Exam tip",
                 "<p>A frequent question asks to “differentiate the HTML DOM and the XML DOM”. Answer on two lines: "
                 "both present a document as a tree with the same properties and methods; the HTML DOM's vocabulary "
                 "is fixed and used to change rendering, whereas the XML DOM's vocabulary is arbitrary and is used to "
                 "read or modify data.</p>"))

    o.append(sec("11.6", "Summary"))
    o.append(ul(["Namespaces solve name conflicts by qualifying element names with a URI through a prefix.",
                 "A prefix must be declared with <span class='mono'>xmlns:prefix</span>; the scope is the element "
                 "and its descendants.",
                 "XSLT transforms XML into another XML document (usually HTML), using XPath to select nodes.",
                 "The XML DOM models a document as nodes with standard properties and methods, available in every "
                 "language that implements the standard.",
                 "In Java, <span class='mono'>DocumentBuilder</span> produces a W3C "
                 "<span class='mono'>Document</span> that you traverse with <span class='mono'>getElementsByTagName</span>."]))
    o.append(box("viva", "Check yourself",
                 "<p><b>1.</b> Why does XML need namespaces? "
                 "<b>2.</b> What does the processor do with a namespace URI? "
                 "<b>3.</b> Name the three DOM properties used to walk from a node to its relatives.</p>"
                 "<p class='small'><i>Answers:</i> (1) Because element names are chosen by the developer, so two "
                 "vocabularies can collide. (2) Nothing — it compares the string; the URI is an identifier, not an "
                 "address. (3) <span class='mono'>parentNode</span>, <span class='mono'>childNodes</span> and "
                 "<span class='mono'>nodeName</span>/<span class='mono'>nodeValue</span> for identity.</p>"))
    o.append(recap("Part 11 recap", [
        ["<b>Name conflict</b>", "Two vocabularies can both define <span class='mono'>&lt;table&gt;</span>; a "
                                  "prefix disambiguates them."],
        ["<b>Declaration</b>", "<span class='mono'>xmlns:pfx=\"uri\"</span> on an element; it applies to that "
                               "element and all its descendants."],
        ["<b>Default namespace</b>", "<span class='mono'>xmlns=\"uri\"</span> — no prefix, applies to unprefixed "
                                     "child elements."],
        ["<b>URI vs URL</b>", "The namespace URI is a name, never fetched. Only its string value matters."],
        ["<b>XSLT</b>", "A stylesheet with <span class='mono'>template match</span> rules; XPath selects, the "
                        "processor writes the output."],
        ["<b>DOM</b>", "The whole document in memory as a tree of nodes; navigate with "
                       "<span class='mono'>parentNode</span>, <span class='mono'>childNodes</span>, "
                       "<span class='mono'>nodeName</span>."],
        ["<b>Java DOM</b>", "<span class='mono'>DocumentBuilder</span> parses; "
                            "<span class='mono'>getElementsByTagName()</span> searches."],
    ], terms=["namespace", "prefix", "xmlns declaration", "default namespace", "XSLT", "XPath", "DOM", "node", "DocumentBuilder"], practice=[
        "Declare a prefix for the XHTML namespace on <span class='mono'>&lt;root&gt;</span>.",
        "What does a processor actually do with a namespace URI?",
        "Name three DOM properties used to walk from a node to its relatives.",
    ], trap="Thinking the namespace URI is downloaded. It is an identifier; nothing is fetched."))
    return "".join(o)
