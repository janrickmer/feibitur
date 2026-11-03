# -*- coding: utf-8 -*-
"""Prüft Podcast-Quelltexte: Umfang, Pflichtkapitel, verbotene Jahrgangsbezüge, Markdown-Regeln.
Aufruf: python3 tools/podcast/check.py q1_1 [q1_2 ...]"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
VERBOTEN = [r"Abitur\w*\s*20\d\d", r"Abiturerlass", r"Landesabitur\s*20\d\d", r"Prüfungsschwerpunkt", r"Schwerpunktthem", r"Abiturjahrgang\s*20\d\d",
            r"Prüfungsjahr", r"kein Schwerpunkt", r"\bErlass\b", r"Jahrgang 20\d\d", r"\bFeibitur\b"]
def check(mod):
    p = os.path.join(HERE, mod + ".md")
    if not os.path.exists(p): return ["Datei fehlt: " + p], 0
    t = open(p, encoding="utf-8").read(); err = []
    words = len(re.findall(r"\w+", re.sub(r"[#*\-]", " ", t)))
    if words < 7000: err.append("zu kurz: %d Wörter (Ziel 7500–9500)" % words)
    if words > 10500: err.append("zu lang: %d Wörter (Ziel 7500–9500)" % words)
    h1 = re.findall(r"^# (.+)$", t, re.M)
    if len(h1) != 1: err.append("genau eine Titelzeile '# …' nötig")
    h2 = re.findall(r"^## (.+)$", t, re.M)
    if not any(h.startswith("Nur Leistungskurs") for h in h2): err.append("Kapitel '## Nur Leistungskurs: …' fehlt")
    if not any(h.startswith("Im Abitur") for h in h2): err.append("Kapitel '## Im Abitur: …' fehlt")
    if not any(h.startswith("Quellen") for h in h2): err.append("Kapitel '## Quellen' fehlt")
    if len(h2) < 8: err.append("zu wenige Kapitel (%d, mind. 8)" % len(h2))
    for v in VERBOTEN:
        for m in re.finditer(v, t): err.append("verboten: „%s“ (…%s…)" % (m.group(0), t[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
    if re.search(r"^\|", t, re.M): err.append("keine Tabellen (|) verwenden")
    if re.search(r"<[a-z/][^>]*>", t): err.append("kein HTML verwenden")
    if re.search(r"https?://", t) and not re.search(r"^## Quellen", t, re.M): err.append("Links nur im Quellenkapitel")
    return err, words
if __name__ == "__main__":
    bad = 0
    for m in sys.argv[1:]:
        e, w = check(m)
        print(("[OK] " if not e else "[FEHLER] ") + "%s: %d Wörter" % (m, w))
        for x in e: print("   - " + x)
        bad += bool(e)
    sys.exit(1 if bad else 0)
