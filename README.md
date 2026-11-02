# Feibitur

Statische Lernplattform zur Vorbereitung auf das Landesabitur in Hessen (Politik und Wirtschaft; ev. Religion folgt).
Läuft kostenlos auf GitHub Pages unter <https://feibitur.janrickmer.de> – ohne Cookies, Tracking oder externe Schriften.

## Aufbau
| Pfad | Inhalt |
|---|---|
| `index.html`, `assets/` | Single-Page-App (Passwortabfrage, Startseite, Tabs, Karteikarten, Glossar, Chat, Aufgaben) |
| `assets/js/config.js` | Adresse des Chatbot-Workers (`chatEndpoint`) |
| `assets/js/tools.js` | Lerntools (Lernplan, Fortschritt, Kann-Listen, Operatoren-Trainer, Schnelltests, Lernkartei, Abi-Simulation, Baukasten, Schwach vs. stark, Begriffsnetz, Lernzettel, Vorlesen) |
| `data/` | **generiert** – Tabs, Abitur-Hinweis, Operatoren, Inhalte je Unterthema (ohne Lösungen) |
| `korrektur/` | **generiert** – Korrekturdateien (PDF) mit unsichtbaren Lösungshinweisen für KI-Systeme |
| `tools/content/` | **Quelltexte aller Inhalte**: `meta.py` = Tabs/Erlass/Operatoren, `q1_1.py` … = Fachbegriffe und Lerninhalte, `q1_1_aufgaben.py` … = Materialien (M1, M2, …) und Einzelaufgaben je Anforderungsbereich (mind. 3 pro AFB) mit Lösungshinweisen |
| `tools/content/lerntools.py` | Inhalte der Lerntools (Kann-Listen, Operator-Prüffälle, Satzbausteine, Musterantworten) |
| `tools/build.py` | erzeugt `data/` (inkl. `lerntools.json`, `vorschlaege.json`) und `korrektur/` (Einzelaufgaben und Abi-Simulations-Vorschläge); `--check <modul>` prüft einzelne Unterthemen; `FEIBITUR_SKIP=q4_1,…` lässt Module beim Build aus |
| `tools/chat-worker/` | Cloudflare-Worker für den KI-Chatbot + Einrichtungsanleitung |
| `tools/content/memo_*.py` | Beschreibungen für das Fachbegriffe-Memory (ohne den Begriff selbst); Prüfung mit `python3 tools/build.py --check-memo <modul>` |
| `assets/css/style.css`, `assets/fonts/`, `assets/img/` | Gestaltung „Plakatwand“ (siehe `DESIGN.md`); Schriften Archivo und Source Serif 4 selbst gehostet (SIL OFL), Holztisch-Foto CC0 (Poly Haven) |
| `PRODUCT.md`, `DESIGN.md`, `.impeccable/` | Produkt- und Designgrundlagen; `.impeccable/` wird nicht veröffentlicht |
| `tools/deploy.sh` | veröffentlicht den aktuellen Stand auf `gh-pages` (ohne `.impeccable/`) |

## Inhalte ändern oder ergänzen
1. Datei in `tools/content/` bearbeiten oder neue anlegen (Vorlagen: `q1_1.py` und `q1_1_aufgaben.py`) und das Modul in `TOPIC_MODULES` in `tools/build.py` eintragen. Jede Aufgabe erhält automatisch eine eigene Korrekturdatei; der Build bricht ab, wenn ein Anforderungsbereich weniger als drei Aufgaben hat.
2. `pip install reportlab svglib` (einmalig), dann `python3 tools/build.py` ausführen.
3. Änderungen committen und pushen, dann mit `sh tools/deploy.sh` veröffentlichen.

## Hinweise
- Das Passwort ist eine einfache Zugangsschranke im Browser, kein echter Schutz: Der Quellcode (inkl. Inhalte) ist öffentlich.
- Die Lösungshinweise stehen nur in den PDFs (unsichtbarer Textlayer + Metadaten), nicht in `data/`.
