---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["assets/css/style.css","assets/js/app.js","assets/js/tools.js"]
---

# Surface brief: Feibitur PoWi (ganze Fachwelt inkl. Lerntools, Startseite als Verbindung, Fachbegriffe-Memory)

Scope and visitor mode: read (Fachwelt PoWi: Themenseiten, Lerntools); das Memory ist ein Spielmoment innerhalb dieser Welt.
Audience/job: Q-Phase Hessen, GK/LK, lernt am Handy (abends), Laptop (Schreibtisch), Tablet. Findet Thema, Bereich, Lernstand sofort; liest lange Texte mühelos; kommt gern wieder.
Constraints: alles selbst gehostet (Schriften als Dateien im Repo), keine Fremdressourcen; kein Sound; Aufbau aus dem Auftrag bleibt (Unterthemen-Liste links, drei Bereiche, 2/3 Inhalt + Chatbot rechts, grüner Korrektur-Knopf, 3-Schritte-Anleitung); politische Neutralität (keine einzelne Parteifarbe als Markenfarbe); Religion bekommt später eine eigene Welt.
Memorable moment: das Unterthema öffnet als Plakat, das an den Mast geklebt wird; im Memory fliegen gefundene Paare auf den Stapel des Spielers.
Unresolved: keine.

## Direction contract

THESIS: PoWi lernt man an der Plakatwand im Wahlkampf. Jedes Halbjahr ist ein Plakat in eigener Farbe, jedes Unterthema öffnet als Plakat mit seinem Titel in Plakatschrift, festgezurrt mit Kabelbindern. Verweigert wird das Standard-Lernapp-Raster (gleich große Icon-Karten, Pastell, Fortschrittsringe) ebenso wie der Behörden-Look.

OWN-WORLD: Grund = Straßenseite der Plakatwand (kühles Betongrau, feine Kleister-Körnung), Plakatpapier strahlend weiß, Druckschwarz; vier Halbjahresfarben, die immer gemeinsam auftreten: Q1 Zinnober, Q2 Kobalt, Q3 Petrol, Q4 Goldgelb; Grundlagen Schwarz. Blueback-Graublau als Rückseite gerissener Papiere. Plakatschrift: Archivo in extra-condensed, Gewicht 800–900, Versalien, Durchschuss 0.9. Lesetext: Source Serif 4. Signaturen: Kabelbinder-Laschen, diagonaler Störer „NUR LK“, Ausverkauft-Streifen „ERLEDIGT“, Laternenmast als Navigationsschiene.

STORY: Schüler erkennen sofort ihr Halbjahr an der Plakatfarbe, sehen am Mast, wo sie zuletzt waren, lesen in ruhiger Spalte, markieren Lernstand mit Zeichen statt nur Farbe und spielen das Memory am edlen Holztisch gegeneinander.

FIRST VIEWPORT: Oben Feibitur-Kopfzeile mit Kurswahl GK/LK und Lerntools. Darunter die Halbjahres-Plakatbahn (Grundlagen, Q1–Q4 als nebeneinander geklebte Plakatstreifen, aktives Plakat vollfarbig und größer). Links der Laternenmast mit Unterthemen-Schildern (aktiv vollfarbig, Flagge „zuletzt hier“). Rechts das Themenplakat: Nummer riesig, Titel in Plakatschrift über ganze Breite, Kabelbinder oben, darunter Bereichsumschalter Fachbegriffe · Inhalte · Übungsaufgaben und die Lesespalte (~68 Zeichen) auf weißem Papier. Auf dem Handy: Plakatbahn horizontal scrollbar, Mast wird zur Schild-Leiste über dem Plakat.

FORM: Wahlkampf-Plakatwand (Laternenmast, Litfaßsäule, Störer), Position 6 der eigenen Liste; seed:94c8f7e53f6c4f97. Signature interaction: Plakat-Ankleben (380 ms, leichtes Überschwingen, Rotation setzt sich auf 0) beim Öffnen eines Unterthemas; Memory: Austeilen, 3D-Wenden, Paar fliegt zum Spielerstapel. Motion grammar: eine Konstante (380 ms, cubic-bezier(.2,1.3,.4,1)) für alles Klebende; Ausblenden exponentiell (220 ms). Raises: (Schneidetisch) Zustand ist ein Zeichen, kein Farbton; die Stelle, an der du aufgehört hast, wird gemerkt und beim Wiederkommen markiert. (Belichtungsprotokoll) neutrale Töne nur aus einer festen 7-stufigen Betongrau-Leiter. (Zyklorama) Farbe ist nie das einzige Signal, jeder Zustand hat Text oder Muster. (Zoo-Karte) eine einzige Bewegungskonstante für alles. (Wolkensteinbruch) Abschnitte als einzelne geklebte Bögen mit sichtbarer Wand dazwischen.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
