"""Small SVG drawing helpers for the textbook figures.

Everything is emitted as plain SVG primitives (rect / line / path / text) so that
WeasyPrint's SVG renderer draws it without relying on markers or foreignObject.
"""
import math

# ---- palette -------------------------------------------------------------
NAVY = "#10243c"
NAVY2 = "#1b3a5c"
NAVY3 = "#2f5b86"
TEAL = "#0e6f6b"
TEAL2 = "#128b84"
TEAL_L = "#e7f3f1"
TEAL_M = "#bfe0da"
ORANGE = "#c96a12"
ORANGE_L = "#fdf2e4"
ORANGE_M = "#f2c58a"
INK = "#1b242e"
MUTED = "#5d6a77"
LINE = "#c9d3dd"
GREY = "#f2f5f8"
GREY2 = "#e6ecf2"
RED = "#9d2b25"
RED_L = "#fbeeec"
RED_M = "#e8b4ae"
VIOLET = "#4a3b7c"
VIOLET_L = "#efeaf9"
VIOLET_M = "#cfc4ea"
BLUE_L = "#eaf1f8"
GOLD = "#8a6d1f"
GOLD_L = "#fbf3dc"
WHITE = "#ffffff"

SANS = "Source Sans 3"
MONO = "JetBrains Mono"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg(w, h, body, cls="", extra="", bg="#ffffff"):
    back = f'<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'class="{cls}" {extra} preserveAspectRatio="xMidYMid meet">'
            f'{back}{body}</svg>')


def txt(x, y, s, size=9.5, color=INK, weight=400, anchor="start", family=SANS,
        opacity=None, style=None, ls=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    o = f' opacity="{opacity}"' if opacity else ""
    st = f' font-style="{style}"' if style else ""
    lsp = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'fill="{color}" font-weight="{weight}"{a}{o}{st}{lsp}>{esc(s)}</text>')


def wrap(s, width, size, char_w=0.505):
    """Greedy wrap by estimated character width (sans-serif metrics)."""
    limit = max(6, int(width / (size * char_w)))
    words, lines, cur = str(s).split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if len(cand) <= limit:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def txtw(x, y, s, width, size=9.5, color=INK, weight=400, anchor="middle",
         lh=1.22, family=SANS, char_w=0.505):
    """Multi-line text centred on x, first baseline at y."""
    lines = wrap(s, width, size, char_w)
    out = []
    for i, ln in enumerate(lines):
        out.append(txt(x, y + i * size * lh, ln, size, color, weight, anchor, family))
    return "".join(out), len(lines)


def rect(x, y, w, h, fill=WHITE, stroke=LINE, rx=2.2, sw=0.9, dash=None, opacity=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{opacity}"' if opacity else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')


def line(x1, y1, x2, y2, color=MUTED, sw=1.1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}"{d}/>')


def head(x, y, ang, color, size=6.2):
    """Filled triangular arrow head at (x, y) pointing along ang (radians)."""
    a1, a2 = ang + math.radians(152), ang - math.radians(152)
    p1 = (x + size * math.cos(a1), y + size * math.sin(a1))
    p2 = (x + size * math.cos(a2), y + size * math.sin(a2))
    return (f'<polygon points="{x:.2f},{y:.2f} {p1[0]:.2f},{p1[1]:.2f} '
            f'{p2[0]:.2f},{p2[1]:.2f}" fill="{color}"/>')


def arrow(x1, y1, x2, y2, color=MUTED, sw=1.1, dash=None, hs=6.2, start_dot=False):
    ang = math.atan2(y2 - y1, x2 - x1)
    # shorten line so the head sits neatly
    bx, by = x2 - hs * 0.85 * math.cos(ang), y2 - hs * 0.85 * math.sin(ang)
    out = line(x1, y1, bx, by, color, sw, dash) + head(x2, y2, ang, color, hs)
    if start_dot:
        out += f'<circle cx="{x1}" cy="{y1}" r="{sw*1.5}" fill="{color}"/>'
    return out


def poly(points, color=MUTED, sw=1.1, dash=None, arrow_end=True, hs=6.2, arrow_start=False):
    """Orthogonal / arbitrary polyline with arrow head on the last segment."""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    out = (f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{sw}" '
           f'stroke-linejoin="round"{d}/>')
    if arrow_end:
        (x1, y1), (x2, y2) = points[-2], points[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        out += head(x2, y2, ang, color, hs)
    if arrow_start:
        (x1, y1), (x2, y2) = points[0], points[1]
        ang = math.atan2(y2 - y1, x2 - x1)
        out += head(x1, y1, ang + math.pi, color, hs)
    return out


def node(x, y, w, h, title, sub=None, fill=WHITE, stroke=NAVY2, tc=INK, fs=9.6,
         bold=600, subfs=7.8, subc=MUTED, rx=2.4, sw=0.95, tcol=None):
    """Box with centred multi-line title and optional smaller second line."""
    tcol = tcol or tc
    tl = wrap(title, w - 8, fs)
    sl = wrap(sub, w - 8, subfs) if sub else []
    th = len(tl) * fs * 1.18
    sh = len(sl) * subfs * 1.24
    gap = 1.6
    total = th + (gap + sh if sl else 0)
    top = y + (h - total) / 2
    out = rect(x, y, w, h, fill, stroke, rx, sw)
    cy = top + fs * 0.85
    for ln in tl:
        out += txt(x + w / 2, cy, ln, fs, tcol, bold, "middle")
        cy += fs * 1.18
    if sl:
        cy = top + th + gap + subfs * 0.85
        for ln in sl:
            out += txt(x + w / 2, cy, ln, subfs, subc, 400, "middle")
            cy += subfs * 1.24
    return out


def nlines(s, width, size, char_w=0.505):
    return len(wrap(s, width, size, char_w))


def pill(x, y, w, h, label, fill=TEAL_L, stroke=TEAL, tc=TEAL, fs=7.6, weight=700):
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" '
           f'stroke="{stroke}" stroke-width="0.8"/>')
    out += txt(x + w / 2, y + h / 2 + fs * 0.35, label, fs, tc, weight, "middle")
    return out


def band(x, y, w, h, label, fill=NAVY, tc=WHITE, fs=8.4, weight=700, ls="0.08em"):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'
    out += txt(x + 6, y + h / 2 + fs * 0.35, label, fs, tc, weight, "start", ls=ls)
    return out


def legend(x, y, items, fs=7.2, gap=6, box=7, vertical=False):
    """items: list of (label, fill, stroke)."""
    out, cx = [], x
    for label, fill, stroke in items:
        if vertical:
            out.append(f'<rect x="{x}" y="{y-6}" width="{box}" height="{box}" rx="1.4" fill="{fill}" stroke="{stroke}" stroke-width="0.8"/>')
            out.append(txt(x + box + 3, y - 0.2, label, fs, MUTED, 400))
            y += 9
        else:
            out.append(f'<rect x="{cx}" y="{y-6}" width="{box}" height="{box}" rx="1.4" fill="{fill}" stroke="{stroke}" stroke-width="0.8"/>')
            out.append(txt(cx + box + 2.6, y - 0.2, label, fs, MUTED, 400))
            cx += box + 4 + len(label) * fs * 0.5 + gap
    return "".join(out)


def title(x, y, s, fs=10.6, color=NAVY):
    return txt(x, y, s, fs, color, 700)


def note(x, y, s, fs=7.3, color=MUTED, anchor="start", width=None):
    if width:
        body, n = txtw(x, y, s, width, fs, color, 400, anchor)
        return body
    return txt(x, y, s, fs, color, 400, anchor)


def layer_stack(x, y, w, rows, gap=2.0):
    """rows: list of (height, fill, stroke, label, sublabel)"""
    out = []
    cy = y
    for h, fill, stroke, label, sub in rows:
        out.append(rect(x, cy, w, h, fill, stroke))
        out.append(txt(x + 7, cy + h / 2 + (0 if not sub else -1.5), label, 9.2,
                       WHITE if fill in (NAVY, NAVY2, TEAL, TEAL2, ORANGE, VIOLET, RED) else INK, 700))
        if sub:
            out.append(txt(x + 7, cy + h / 2 + 8, sub, 7.4,
                           "#dbe6f0" if fill in (NAVY, NAVY2, TEAL, TEAL2, ORANGE, VIOLET, RED) else MUTED))
        cy += h + gap
    return "".join(out), cy


def brace_label(x, y1, y2, label, color=MUTED, side="left"):
    """Vertical bracket with a rotated label."""
    out = [line(x, y1, x, y2, color, 1.0)]
    out.append(line(x, y1, x + (4 if side == "left" else -4), y1, color, 1.0))
    out.append(line(x, y2, x + (4 if side == "left" else -4), y2, color, 1.0))
    cy = (y1 + y2) / 2
    out.append(f'<text x="{x}" y="{cy}" font-family="{SANS}" font-size="7.4" fill="{color}" '
               f'font-weight="700" text-anchor="middle" transform="rotate(-90 {x} {cy})">{esc(label)}</text>')
    return "".join(out)
