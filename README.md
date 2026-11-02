# Feibitur

Statische Lernplattform zur Vorbereitung auf das Landesabitur in Hessen (Politik und Wirtschaft; ev. Religion folgt).
Läuft kostenlos auf GitHub Pages unter <https://feibitur.janrickmer.de> – ohne Cookies, Tracking oder externe Schriften.

## Aufbau
| Pfad | Inhalt |
|---|---|
| `index.html`, `assets/` | Single-Page-App (Passwortabfrage, Startseite, Tabs, Karteikarten, Glossar, Chat, Aufgaben) |
| `assets/js/config.js` | Adresse des Chatbot-Workers (`chatEndpoint`) |
| `data/` | **generiert** – Tabs, Abitur-Hinweis, Operatoren, Inhalte je Unterthema (ohne Lösungen) |
| `korrektur/` | **generiert** – Korrekturdateien (PDF) mit unsichtbaren Lösungshinweisen für KI-Systeme |
| `tools/content/` | **Quelltexte aller Inhalte** (`meta.py` = Tabs/Erlass/Operatoren, `q1_1.py` … = Unterthemen) |
| `tools/build.py` | erzeugt `data/` und `korrektur/` aus `tools/content/` |
| `tools/chat-worker/` | Cloudflare-Worker für den KI-Chatbot + Einrichtungsanleitung |

## Inhalte ändern oder ergänzen
1. Datei in `tools/content/` bearbeiten oder neue anlegen (Vorlage: `q1_1.py`) und in `TOPIC_MODULES` in `tools/build.py` eintragen.
2. `pip install reportlab` (einmalig), dann `python3 tools/build.py` ausführen.
3. Änderungen committen und pushen.

## Hinweise
- Das Passwort ist eine einfache Zugangsschranke im Browser, kein echter Schutz: Der Quellcode (inkl. Inhalte) ist öffentlich.
- Die Lösungshinweise stehen nur in den PDFs (unsichtbarer Textlayer + Metadaten), nicht in `data/`.
