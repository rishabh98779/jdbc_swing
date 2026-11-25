"""Shared HTML helpers used by all content modules."""
import html as _html
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

_fmt = HtmlFormatter(nowrap=True, classprefix="")

TOC = []            # collected (level, anchor, label) while content is generated
CODE_REGISTRY = []  # (lang, source, caption) for the syntax audit


def code(src, lang="java", caption=None, cls="", wrap=True, label=None):
    src = src.strip("\n")
    try:
        lexer = get_lexer_by_name(lang)
    except Exception:
        lexer = get_lexer_by_name("text")
    CODE_REGISTRY.append((lang, src, caption or ""))
    body = highlight(src, lexer, _fmt).rstrip("\n")
    out = ""
    if caption:
        if label is None:
            out += f'<div class="cap">{caption}</div>'
        elif label == "":
            out += f'<div class="cap capplain">{caption}</div>'
            cls += " capplain"
        else:
            out += f'<div class="cap capfixed"><span class="capnum">{label}</span> · {caption}</div>'
            cls += " capfixed"
    out += f'<pre class="code {cls}">{body}</pre>'
    keep = " keep" if src.count("\n") + 1 <= 20 else ""
    return f'<div class="codewrap {cls}{keep}">{out}</div>' if wrap else out


def raw_code(src, caption=None, cls=""):
    """Terminal output or plain text - excluded from the program counter."""
    return code(src, "text", caption, (cls + " outp").strip())


def box(kind, label, inner):
    return (f'<div class="box {kind}"><span class="lbl">{label}</span>'
            f'{inner}</div>')


def fig(svg, caption, cls=""):
    return (f'<figure class="{cls}">{svg}'
            f'<figcaption>{caption}</figcaption></figure>')


def tbl(caption, headers, rows, widths=None, cls="", firstcol=True, keep=False):
    out = ['<div class="tblwrap%s">' % (" keepertbl" if keep else "")]
    if caption:
        out.append(f'<div class="tcap">{caption}</div>')
    out.append(f'<table class="dt {cls}">')
    if widths:
        out.append("<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>")
    out.append("<thead><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr></thead><tbody>")
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            klass = ' class="hl"' if (i == 0 and firstcol) else ""
            cells.append(f"<td{klass}>{c}</td>")
        out.append("<tr>" + "".join(cells) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def part(num, title, sub, icon="", art_icon=None):
    anchor = f"part{num}"
    if art_icon is not None:
        import art
        icon = art.icon(art_icon)
    TOC.append((1, anchor, f"PART {num} · {title}"))
    head = f"PART {num} · {title}"
    if len(head) > 44:
        head = head[:43].rsplit(" ", 1)[0] + "\u2026"
    return (f'<h1 class="part" id="{anchor}" style="string-set: partname &quot;{head}&quot;">'
            f'<span class="partname">PART {num} · {title}</span></h1>'
            f'<div class="partbanner">'
            f'<div class="pnum">Part {num}</div>'
            f'<h2>{title}</h2>'
            f'<div class="psub">{sub}</div>'
            f'<div class="picon">{icon}</div>'
            f'</div>')


def sec(num, title):
    TOC.append((2, f"s{num}", f"{num}  {title}"))
    return f'<h2 class="sec" id="s{num}"><span class="num">{num}</span>{title}</h2>'


def sub(num, title):
    return f'<h3 class="sub" id="s{num}"><span class="num">{num}</span>{title}</h3>'


def mini(title):
    return f'<h4 class="mini">{title}</h4>'


def p(t):
    return f"<p>{t}</p>"


def lead(t):
    return f'<p class="lead">{t}</p>'


def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items, cls=""):
    return f'<ol class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def qa(q, a):
    return f'<div class="qa"><div class="q">{q}</div><div class="a">{a}</div></div>'


def mcq(q, opts, ans, why=""):
    letters = "ABCD"
    longest = max(len(x) for x in opts)
    cells = [f'<td><span class="ol">{letters[i]}.</span> {x}</td>' for i, x in enumerate(opts)]
    if longest <= 54:
        rows = "".join(f"<tr>{cells[i]}{cells[i + 1]}</tr>" for i in range(0, 4, 2))
    else:
        rows = "".join(f"<tr>{c}<td></td></tr>" for c in cells)
    w = f" &#8212; {why}" if why else ""
    return (f'<div class="mcq"><div class="q">{q}</div>'
            f'<table class="opts">{rows}</table>'
            f'<div class="ans">Answer: {ans}{w}</div></div>')


def cards(left_title, left_items, right_title, right_items):
    def card(t, items, alt=False):
        lis = "".join(f"<li>{i}</li>" for i in items)
        return (f'<div class="card{" alt" if alt else ""}"><h5>{t}</h5>'
                f'<ul>{lis}</ul></div>')
    return f'<div class="cards">{card(left_title, left_items)}{card(right_title, right_items, True)}</div>'

def recap(title, rows, trap=None, practice=None, terms=None):
    """Compact end-of-part revision table, optionally closed by one exam trap."""
    out = ['<div class="tblwrap keepertbl">',
           f'<div class="tcap">{title} — one line per idea</div>',
           '<table class="dt compact"><colgroup><col style="width:30%"><col style="width:70%">'
           '</colgroup><thead><tr><th>Idea</th><th>Say it in one line</th></tr></thead><tbody>']
    for k, v in rows:
        out.append(f"<tr><td class='hl'>{k}</td><td>{v}</td></tr>")
    out.append("</tbody></table>")
    if practice:
        items = "".join(f"<li>{q}</li>" for q in practice)
        out.append('<div class="practnote"><div class="ph">Ask yourself now</div>'
                   f'<ol class="pq">{items}</ol></div>')
    if terms:
        items = "".join(f"<li>{t}</li>" for t in terms)
        out.append('<div class="termgrid"><div class="ph">Define these aloud before you turn the page</div>'
                   f'<ul>{items}</ul></div>')
    if trap:
        out.append(f'<div class="trapnote"><b>Trap to avoid.</b> {trap}</div>')
    out.append("</div>")
    return "".join(out)
