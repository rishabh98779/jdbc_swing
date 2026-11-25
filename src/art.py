"""Cover artwork and part icons (pure SVG, no external assets)."""
from dia import (rect, txt, arrow, line, node, NAVY, NAVY2, TEAL, ORANGE, WHITE, MUTED,
                 TEAL2, ORANGE_M, TEAL_M, MONO, SANS, svg, head, poly)

O = "#f0a860"      # orange on dark
T = "#5fb8b0"      # teal on dark
D = "#1b3a5c"      # panel on dark
L = "#9fb4c8"      # muted text on dark


def cover_art():
    b = []
    # faint blueprint grid
    for gx in range(0, 795, 40):
        b.append(line(gx, 0, gx, 640, "#16324f", 0.4))
    for gy in range(0, 641, 40):
        b.append(line(0, gy, 794, gy, "#16324f", 0.4))

    # ---- application window -------------------------------------------------
    b.append(rect(34, 34, 300, 250, "#0f2b47", "#2f5b86", 4))
    b.append(rect(34, 34, 300, 22, "#17395c", "#2f5b86", 4))
    for i, c in enumerate(["#e06c75", "#e5c07b", "#98c379"]):
        b.append(f'<circle cx="{48 + i*11}" cy="45" r="3.2" fill="{c}"/>')
    b.append(txt(84, 49, "StudentApp.java", 8.5, L, 600))
    code_lines = [
        ("1", "import java.sql.*;", T),
        ("2", "", L),
        ("3", "public class StudentApp {", "#c8d6e5"),
        ("4", "  public static void main(", "#c8d6e5"),
        ("5", "      String[] a) throws Exception {", "#c8d6e5"),
        ("6", "    Connection con =", T),
        ("7", "      DriverManager.getConnection(", "#e2c07a"),
        ("8", "        URL, USER, PASS);", O),
        ("9", "    PreparedStatement ps =", T),
        ("10", "      con.prepareStatement(", "#e2c07a"),
        ("11", "        \"SELECT * FROM student\");", "#9ecb8f"),
        ("12", "    ResultSet rs = ps.executeQuery();", "#c8d6e5"),
        ("13", "    while (rs.next())", "#c8d6e5"),
        ("14", "      print(rs.getInt(\"id\"));", "#c8d6e5"),
    ]
    y = 74
    for n, s_, c in code_lines:
        b.append(txt(48, y, n, 6.6, "#4d6b8a", 400, "end", MONO))
        b.append(txt(56, y, s_, 6.6, c, 400, "start", MONO))
        y += 13.6

    # ---- JDBC bridge -------------------------------------------------------
    b.append(f'<polygon points="470,72 552,118 552,206 470,252 388,206 388,118" fill="{D}" stroke="{T}" stroke-width="1.8"/>')
    b.append(txt(470, 138, "JDBC", 26, WHITE, 700, "middle"))
    b.append(txt(470, 160, "DriverManager", 9.2, T, 600, "middle"))
    b.append(txt(470, 176, "java.sql · javax.sql", 7.6, L, 400, "middle"))
    b.append(txt(470, 196, "one API, many drivers", 7.4, "#6f8aa5", 400, "middle"))
    b.append(arrow(338, 160, 380, 160, O, 1.8, hs=7.4))
    b.append(txt(358, 150, "calls", 7.4, O, 600, "middle"))
    b.append(arrow(560, 160, 610, 160, O, 1.8, hs=7.4))
    b.append(txt(584, 150, "SQL", 7.4, O, 600, "middle"))

    # ---- database ----------------------------------------------------------
    cx, cw = 620, 140
    for i, ytop in enumerate([84, 104, 124]):
        b.append(f'<rect x="{cx}" y="{ytop}" width="{cw}" height="30" fill="#123a52" stroke="{T}" stroke-width="1.3"/>')
        b.append(f'<ellipse cx="{cx+cw/2}" cy="{ytop}" rx="{cw/2}" ry="9" fill="#1c5673" stroke="{T}" stroke-width="1.3"/>')
        b.append(f'<ellipse cx="{cx+cw/2}" cy="{ytop+30}" rx="{cw/2}" ry="9" fill="#123a52" stroke="{T}" stroke-width="1.3"/>')
    b.append(txt(cx + cw / 2, 124, "student", 9.2, WHITE, 600, "middle"))
    b.append(txt(cx + cw / 2, 186, "MySQL / Oracle", 8, L, 400, "middle"))

    # ---- result table ------------------------------------------------------
    tx, ty, cwid, rh = 34, 344, 104, 22
    b.append(txt(tx, ty - 10, "ResultSet  ·  a cursor over the returned rows", 8.4, T, 700))
    for r in range(3):
        for c in range(3):
            fill = "#17395c" if r == 0 else "#0f2b47"
            b.append(rect(tx + c * cwid, ty + r * rh, cwid, rh, fill, "#2f5b86", 0, 0.8))
    for c, h in enumerate(["id", "name", "marks"]):
        b.append(txt(tx + c * cwid + cwid / 2, ty + 15, h, 7.8, T, 700, "middle"))
    for r, row in enumerate([["101", "Rajesh", "88"], ["102", "Simran", "91"]], start=1):
        for c, v in enumerate(row):
            b.append(txt(tx + c * cwid + cwid / 2, ty + r * rh + 15, v, 7.8, "#c8d6e5", 400, "middle"))
    b.append(f'<rect x="{tx}" y="{ty + rh}" width="{3*cwid}" height="{rh}" fill="none" stroke="{O}" stroke-width="1.8"/>')
    b.append(f'<polygon points="{tx-10},{ty+rh+4} {tx-3},{ty+rh+15} {tx-3},{ty+rh+4}" fill="{O}"/>')

    # ---- key facts strip ---------------------------------------------------
    b.append(line(34, 452, 760, 452, "#2f5b86", 0.9))
    facts = [("4", "driver types", "Type 1 to Type 4"), ("7", "connection steps", "import to close"),
             ("3", "statement types", "Statement, Prepared, Callable"), ("2", "tiers", "two-tier and three-tier")]
    for i, (n, t, sub) in enumerate(facts):
        x = 34 + i * 186
        b.append(txt(x, 496, n, 26, O, 700))
        b.append(txt(x + 26, 490, t, 8.6, WHITE, 600))
        b.append(txt(x + 26, 502, sub, 7.4, L, 400))
    b.append(line(34, 524, 760, 524, "#2f5b86", 0.9))
    b.append(txt(34, 552, "CONNECT  ·  EXECUTE  ·  PROCESS  ·  CLOSE", 8.6, T, 700, ls="0.2em"))
    b.append(txt(34, 572, "JDBC  ·  SPRING JDBC  ·  XML  ·  MAVEN", 8.6, "#6f8aa5", 600, ls="0.2em"))
    return svg(794, 600, "".join(b), bg=None)


# ---------------------------------------------------------------- part icons
def _base(inner, bg=None):
    return svg(120, 120, inner, bg=None)


def icon(n):
    g = []
    if n == 1:  # plug into database
        g.append(rect(14, 40, 34, 40, "none", O, 3, 2.2))
        g.append(rect(52, 44, 12, 32, O, O, 2))
        g.append(f'<ellipse cx="86" cy="46" rx="20" ry="8" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(f'<path d="M66 46 v30 a20 8 0 0 0 40 0 v-30" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(f'<ellipse cx="86" cy="76" rx="20" ry="8" fill="none" stroke="{T}" stroke-width="2.2"/>')
    elif n == 2:  # layered architecture
        for i, (y, w) in enumerate([(24, 84), (48, 68), (72, 52)]):
            g.append(rect(18 + i * 8, y, w, 18, "none", [O, T, T][i], 2, 2.2))
        g.append(line(60, 42, 60, 48, L, 1.6))
        g.append(line(60, 66, 60, 72, L, 1.6))
    elif n == 3:  # four driver chips
        for i in range(4):
            g.append(rect(16 + i * 23, 30, 18, 18, "none", O if i == 3 else T, 2, 2))
            g.append(txt(25 + i * 23, 43, str(i + 1), 8, O if i == 3 else T, 700, "middle"))
        g.append(arrow(18, 62, 102, 62, L, 1.6, hs=6))
        g.append(rect(38, 74, 44, 20, "none", T, 2, 2))
    elif n == 4:  # connection socket
        g.append(f'<circle cx="60" cy="60" r="36" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(f'<circle cx="60" cy="60" r="15" fill="none" stroke="{O}" stroke-width="2.2"/>')
        g.append(line(60, 24, 60, 45, O, 2.2))
        g.append(line(60, 75, 60, 96, O, 2.2))
        g.append(line(24, 60, 45, 60, T, 2.2))
        g.append(line(75, 60, 96, 60, T, 2.2))
    elif n == 5:  # three statement cards
        for i, (y, w) in enumerate([(22, 62), (48, 78), (74, 94)]):
            g.append(rect(60 - w / 2, y, w, 18, "none", [T, T, O][i], 2, 2.2))
    elif n == 6:  # table with cursor
        for r in range(3):
            for c in range(3):
                g.append(rect(24 + c * 24, 26 + r * 20, 24, 20, "#1b3a5c" if r == 0 else "none", T, 0, 1.6))
        g.append(f'<polygon points="18,50 30,72 34,64 44,64" fill="{O}"/>')
    elif n == 7:  # shield
        g.append(f'<path d="M60 20 L94 34 v26 c0 22-18 34-34 40 -16-6-34-18-34-40 V34 Z" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(f'<path d="M44 44 l12 26 8-14 10 8" fill="none" stroke="{O}" stroke-width="2.4"/>')
    elif n == 8:  # @ symbol
        g.append(f'<circle cx="60" cy="60" r="20" fill="none" stroke="{O}" stroke-width="2.6"/>')
        g.append(f'<path d="M80 60 v8 a12 12 0 0 0 24 0 V60 a44 44 0 1 0 -18 35" fill="none" stroke="{T}" stroke-width="2.4"/>')
    elif n == 9:  # leaf / spring
        g.append(f'<path d="M30 92 C30 52 58 26 96 26 C96 66 68 92 30 92 Z" fill="none" stroke="{T}" stroke-width="2.4"/>')
        g.append(f'<path d="M34 88 C50 70 66 56 88 40" fill="none" stroke="{O}" stroke-width="2.2"/>')
    elif n == 10:  # xml tree
        g.append(rect(38, 20, 44, 18, "none", O, 2, 2.2))
        g.append(txt(60, 33, "<root>", 8, O, 700, "middle", MONO))
        for i, x in enumerate([16, 48, 80]):
            g.append(rect(x, 58, 26, 16, "none", T, 2, 2))
            g.append(line(60, 38, x + 13, 58, L, 1.4))
            g.append(rect(x + 4, 84, 18, 12, "none", T, 2, 1.4))
            g.append(line(x + 13, 74, x + 13, 84, L, 1.4))
    elif n == 11:  # namespace brackets
        g.append(txt(28, 52, "{", 34, T, 400, "middle", MONO))
        g.append(txt(92, 52, "}", 34, T, 400, "middle", MONO))
        g.append(txt(60, 44, "ns:x", 9, O, 700, "middle", MONO))
        g.append(txt(60, 60, "URI", 9, L, 400, "middle", MONO))
        g.append(line(30, 78, 90, 78, O, 2))
    elif n == 12:  # maven hexagon
        g.append(f'<polygon points="60,18 96,39 96,81 60,102 24,81 24,39" fill="none" stroke="{T}" stroke-width="2.4"/>')
        g.append(txt(60, 66, "POM", 12, O, 700, "middle", MONO))
    elif n == 13:  # template layers
        for i, (y, w) in enumerate([(24, 72), (46, 60), (68, 48)]):
            g.append(rect(60 - w / 2, y, w, 16, "none", [O, T, T][i], 2, 2.2))
        g.append(txt(60, 96, "JdbcTemplate", 7, L, 600, "middle"))
    elif n == 14:  # datasource + cable
        g.append(f'<ellipse cx="44" cy="38" rx="20" ry="8" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(f'<path d="M24 38 v34 a20 8 0 0 0 40 0 V38" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(f'<path d="M64 56 q22 0 22 20 t22 0" fill="none" stroke="{O}" stroke-width="2.2"/>')
        g.append(rect(78, 72, 26, 16, "none", O, 2, 2))
    elif n == 15:  # bean vs pojo
        g.append(rect(16, 34, 40, 52, "none", T, 3, 2.2))
        g.append(rect(64, 26, 40, 60, "none", O, 3, 2.2))
        g.append(txt(36, 64, "POJO", 8, T, 700, "middle"))
        g.append(txt(84, 60, "BEAN", 8, O, 700, "middle"))
    elif n == 16:  # terminal
        g.append(rect(14, 26, 92, 68, "none", T, 3, 2.2))
        g.append(rect(14, 26, 92, 14, "#1b3a5c", T, 3, 2.2))
        g.append(txt(24, 52, "> javac App.java", 7, O, 400, "start", MONO))
        g.append(txt(24, 64, "> java App", 7, O, 400, "start", MONO))
        g.append(txt(24, 76, "Data inserted!", 7, T, 400, "start", MONO))
    elif n == 17:  # graduation cap
        g.append(f'<polygon points="60,26 100,44 60,62 20,44" fill="none" stroke="{O}" stroke-width="2.4"/>')
        g.append(f'<path d="M34 52 v20 c0 8 12 14 26 14 s26-6 26-14 V52" fill="none" stroke="{T}" stroke-width="2.2"/>')
        g.append(line(96, 46, 96, 76, T, 2))
    return _base("".join(g))
