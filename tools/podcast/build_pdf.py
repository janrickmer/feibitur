# -*- coding: utf-8 -*-
"""Erzeugt aus den Podcast-Quelltexten (tools/podcast/<modul>.md) schlichte, gut lesbare PDFs für NotebookLM.

Aufruf:  python3 tools/podcast/build_pdf.py            (alle vorhandenen .md)
         python3 tools/podcast/build_pdf.py q1_1 q2_3  (nur diese)
Ausgabe: tools/podcast/pdf/<Nr>_<Titel>.pdf

Erlaubtes Markdown: "# Titel", "## Kapitel", "### Abschnitt", Absätze (Leerzeile), "- " Aufzählung,
"1. " nummerierte Liste, **fett**, *kursiv*. Ein Kapitel, dessen Überschrift mit "Nur Leistungskurs" beginnt,
wird als LK-Vertiefung hervorgehoben.
"""
import os, re, sys
from reportlab import rl_config
rl_config.invariant = 1
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, KeepTogether, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pdf")
FONT_DIR = "/usr/share/fonts/truetype/liberation"
for n, f in [("Lib", "LiberationSans-Regular.ttf"), ("Lib-B", "LiberationSans-Bold.ttf"), ("Lib-I", "LiberationSans-Italic.ttf"), ("Lib-BI", "LiberationSans-BoldItalic.ttf"),
             ("Ser", "LiberationSerif-Regular.ttf"), ("Ser-B", "LiberationSerif-Bold.ttf"), ("Ser-I", "LiberationSerif-Italic.ttf"), ("Ser-BI", "LiberationSerif-BoldItalic.ttf")]:
    pdfmetrics.registerFont(TTFont(n, os.path.join(FONT_DIR, f)))
registerFontFamily("Lib", normal="Lib", bold="Lib-B", italic="Lib-I", boldItalic="Lib-BI")
registerFontFamily("Ser", normal="Ser", bold="Ser-B", italic="Ser-I", boldItalic="Ser-BI")

INK = colors.HexColor("#141618")
S = {
    "title": ParagraphStyle("title", fontName="Lib-B", fontSize=21, leading=25, textColor=INK, spaceAfter=6),
    "sub": ParagraphStyle("sub", fontName="Lib", fontSize=10.5, leading=14, textColor=colors.HexColor("#52595e"), spaceAfter=14),
    "h2": ParagraphStyle("h2", fontName="Lib-B", fontSize=15, leading=19, textColor=INK, spaceBefore=16, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName="Lib-B", fontSize=12, leading=15.5, textColor=INK, spaceBefore=10, spaceAfter=4),
    "p": ParagraphStyle("p", fontName="Ser", fontSize=11.2, leading=16, textColor=INK, spaceAfter=7),
    "li": ParagraphStyle("li", fontName="Ser", fontSize=11.2, leading=15.5, textColor=INK),
    "lk": ParagraphStyle("lk", fontName="Lib-B", fontSize=10, leading=13, textColor=colors.white),
}

def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    return t

def parse(md):
    lines = md.replace("\r", "").split("\n")
    blocks, para, lst = [], [], None
    def flush():
        nonlocal para, lst
        if para: blocks.append(("p", " ".join(para))); para = []
        if lst: blocks.append(lst); lst = None
    for ln in lines:
        s = ln.rstrip()
        if not s.strip():
            flush(); continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            flush(); blocks.append(("h%d" % len(m.group(1)), m.group(2).strip())); continue
        m = re.match(r"^\s*-\s+(.*)$", s)
        if m:
            if para: blocks.append(("p", " ".join(para))); para = []
            if not lst or lst[0] != "ul": 
                if lst: blocks.append(lst)
                lst = ("ul", [])
            lst[1].append(m.group(1)); continue
        m = re.match(r"^\s*\d+[.)]\s+(.*)$", s)
        if m:
            if para: blocks.append(("p", " ".join(para))); para = []
            if not lst or lst[0] != "ol":
                if lst: blocks.append(lst)
                lst = ("ol", [])
            lst[1].append(m.group(1)); continue
        if lst and s.startswith("  "):
            lst[1][-1] += " " + s.strip(); continue
        if lst: blocks.append(lst); lst = None
        para.append(s.strip())
    flush()
    return blocks

def build(mod):
    src = os.path.join(HERE, mod + ".md")
    md = open(src, encoding="utf-8").read()
    blocks = parse(md)
    title = next((b[1] for b in blocks if b[0] == "h1"), mod)
    nr = title.split()[0]
    safe = re.sub(r"[^A-Za-z0-9ÄÖÜäöüß]+", "_", title)[:80].strip("_")
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, safe + ".pdf")
    story, in_lk = [], False
    for kind, val in blocks:
        if kind == "h1":
            story.append(Paragraph(inline(val), S["title"]))
            story.append(Paragraph("Informationstext zum Fach Politik und Wirtschaft (gymnasiale Oberstufe, Hessen) – erstellt für Feibitur von Jan-Rickmer Feindt", S["sub"]))
        elif kind == "h2":
            if val.lower().startswith("nur leistungskurs"):
                in_lk = True
                band = Table([[Paragraph("NUR LEISTUNGSKURS – erhöhtes Anforderungsniveau", S["lk"])]], colWidths=[16.4 * cm])
                band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), INK), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
                story.append(Spacer(1, 10)); story.append(band)
            elif in_lk:
                in_lk = False
            story.append(Paragraph(inline(val), S["h2"]))
        elif kind == "h3":
            story.append(Paragraph(inline(val), S["h3"]))
        elif kind == "p":
            story.append(Paragraph(inline(val), S["p"]))
        elif kind in ("ul", "ol"):
            items = [ListItem(Paragraph(inline(x), S["li"]), leftIndent=14) for x in val]
            if kind == "ul":
                lf = ListFlowable(items, bulletType="bullet", start="•", leftIndent=14, bulletFontName="Ser", bulletFontSize=10.5, spaceAfter=6)
            else:
                lf = ListFlowable(items, bulletType="1", bulletFormat="%s.", leftIndent=16, bulletFontName="Ser", bulletFontSize=10.5, spaceAfter=6)
            story.append(lf)
            story.append(Spacer(1, 4))
    def deco(c, d):
        c.saveState(); c.setFont("Lib", 8.5); c.setFillColor(colors.HexColor("#52595e"))
        c.drawString(2.2 * cm, 1.3 * cm, title[:95])
        c.drawRightString(A4[0] - 2.2 * cm, 1.3 * cm, "Seite %d" % d.page)
        c.restoreState()
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=2.3 * cm, rightMargin=2.3 * cm, topMargin=2.1 * cm, bottomMargin=2.2 * cm,
                            title=title, author="Jan-Rickmer Feindt (Feibitur)", subject="Informationstext Politik und Wirtschaft – Quelle für einen Lern-Podcast",
                            creator="Feibitur")
    doc.build(story, onFirstPage=deco, onLaterPages=deco)
    return out, doc.page if hasattr(doc, "page") else None

if __name__ == "__main__":
    mods = sys.argv[1:] or sorted(f[:-3] for f in os.listdir(HERE) if f.endswith(".md"))
    for m in mods:
        path, _ = build(m)
        from reportlab.lib.utils import open_for_read
        import subprocess
        pages = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
        pg = re.search(r"Pages:\s+(\d+)", pages)
        print("%-6s -> %s (%s Seiten)" % (m, os.path.relpath(path), pg.group(1) if pg else "?"))
