---
name: Feibitur
description: Abiturvorbereitung PoWi Hessen 2027 – gelernt an der Plakatwand im Wahlkampf.
colors:
  paper: "#ffffff"
  g1: "#f1f3f4"
  g2: "#e1e4e6"
  g3: "#c7ccd0"
  g4: "#868d92"
  g5: "#52595e"
  g6: "#2a2f33"
  ink: "#141618"
  q1: "#D23A1F"
  q2: "#2340C8"
  q3: "#0A6E72"
  q4: "#F2B300"
  gl: "#141618"
  go: "#1B6E3E"
  go-tint: "#e6f2ea"
  go-deep: "#0f4527"
  stop: "#B3261E"
  stop-tint: "#fbe9e7"
  stop-deep: "#7a1a14"
  blueback: "#9fb1c2"
  walnut: "#3b2014"
  card-stock: "#fffdf8"
  card-edge: "#d8d1c2"
  def-stripe: "#6f87a0"
typography:
  display:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(4.4rem, 19vw, 12rem)"
    fontWeight: 850
    lineHeight: 0.82
    letterSpacing: "-0.005em"
    fontVariation: "'wdth' 66"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 8.5vw, 6.2rem)"
    fontWeight: 850
    lineHeight: 0.84
    letterSpacing: "-0.005em"
    fontVariation: "'wdth' 66"
  poster-number:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(3.6rem, 9vw, 6.4rem)"
    fontWeight: 850
    lineHeight: 0.8
    fontVariation: "'wdth' 66"
  headline-poster:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 5.2vw, 4.6rem)"
    fontWeight: 850
    lineHeight: 0.9
    letterSpacing: "-0.005em"
    fontVariation: "'wdth' 66"
  title-poster:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.7rem"
    fontWeight: 850
    lineHeight: 1
    fontVariation: "'wdth' 66"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.32rem"
    fontWeight: 800
    lineHeight: 1.18
    letterSpacing: "-0.005em"
    fontVariation: "'wdth' 90"
  body:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.62
  body-ui:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
  button:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "0.01em"
    fontVariation: "'wdth' 92"
  section-tab:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.02rem"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "0.02em"
    fontVariation: "'wdth' 85"
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "0.04em"
    fontVariation: "'wdth' 88"
  stamp:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.82rem"
    fontWeight: 850
    lineHeight: 1
    letterSpacing: "0.08em"
    fontVariation: "'wdth' 75"
rounded:
  none: "0px"
  control: "2px"
  tie: "3px"
  card: "7px"
  card-zoom: "12px"
  round: "50%"
spacing:
  gutter: "16px"
  gutter-tight: "10px"
  wall-gap: "10px"
  mast-step: "12px"
  stack: "1.1rem"
  sheet: "1.35rem 1.6rem 1.45rem"
  sheet-compact: "1.05rem 0.95rem 1.15rem"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.55rem 1.1rem"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.g6}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.55rem 1.1rem"
    height: "44px"
  button-secondary-hover:
    backgroundColor: "{colors.g1}"
  button-korrektur:
    backgroundColor: "{colors.go}"
    textColor: "{colors.paper}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.55rem 1.1rem"
    height: "50px"
  button-korrektur-hover:
    backgroundColor: "#155a32"
  button-tools:
    backgroundColor: "{colors.q4}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.35rem 0.8rem"
    height: "38px"
  button-tools-hover:
    backgroundColor: "#ffc61a"
  kurswahl-segment:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0.5rem 0.95rem"
    height: "40px"
  kurswahl-segment-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  input-field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0.75rem 0.9rem"
  kopfzeile:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    padding: "0.55rem 16px"
  halbjahresplakat:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "1.15rem 0.9rem 0.9rem"
    height: "112px"
  halbjahresplakat-active-q1:
    backgroundColor: "{colors.q1}"
    textColor: "{colors.paper}"
  halbjahresplakat-active-q4:
    backgroundColor: "{colors.q4}"
    textColor: "{colors.ink}"
  mast-schild:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.75rem 0.85rem 0.8rem"
  themenplakat-kopf-q2:
    backgroundColor: "{colors.q2}"
    textColor: "{colors.paper}"
    typography: "{typography.headline-poster}"
    rounded: "{rounded.none}"
    padding: "1.6rem 1.6rem 1.4rem"
  bereichsschalter:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.section-tab}"
    rounded: "{rounded.none}"
    height: "54px"
  bereichsschalter-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  bogen:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: "{spacing.sheet}"
  bogen-merke:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  bogen-gesetz:
    backgroundColor: "{colors.g1}"
  stoerer-nur-lk:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.stamp}"
    width: "170px"
  streifen-erledigt:
    backgroundColor: "{colors.go}"
    textColor: "{colors.paper}"
    typography: "{typography.stamp}"
    width: "150px"
  fahne-zuletzt:
    backgroundColor: "{colors.q4}"
    textColor: "{colors.ink}"
    padding: "0.3rem 0.45rem"
  memory-karte-ruecken:
    backgroundColor: "{colors.blueback}"
    textColor: "{colors.paper}"
    rounded: "{rounded.card}"
  memory-karte-vorderseite:
    backgroundColor: "{colors.card-stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
---

# Design System: Feibitur

## Overview

**Creative North Star: "Die Plakatwand im Wahlkampf"**

Politik und Wirtschaft lernt man an der Plakatwand. Die Seite ist eine Straßenwand aus kühlem Betongrau mit feiner Kleister-Körnung, auf die strahlend weiße Bögen geklebt sind. Jedes Kurshalbjahr ist ein Plakat in eigener Farbe (Grundlagen Schwarz, Q1 Zinnober, Q2 Kobalt, Q3 Petrol, Q4 Goldgelb), jedes Unterthema öffnet als Themenplakat mit riesiger Nummer und Titel in Plakatschrift, festgezurrt mit Kabelbindern. Links steht der Laternenmast mit den Unterthemen-Schildern; darunter wird in einer ruhigen Serifenspalte gelesen. Zustände sind Zeichen auf der Wand: der diagonale Störer „Nur LK“, der Streifen „Erledigt“, das gelbe Fähnchen „Zuletzt hier“.

Die Dichte ist die einer echten Wand: großflächig und laut in den Köpfen, still und weiß dort, wo gelesen wird. Plakatschrift (Archivo, extra-schmal, 850, Versalien) spricht kurz und groß; Source Serif 4 trägt jeden Satz, der gelesen werden muss. Verworfen sind das Standard-Lernapp-Raster (gleich große Icon-Kacheln, Pastell, Fortschrittsringe) und der Behörden-Look. Innerhalb der Fachwelt gibt es einen eigenen Raum: das Fachbegriffe-Memory spielt an einem warm beleuchteten Holztisch, auf dem dieselben Plakatfarben als Kartenrücken-Streifen wiederkehren.

Geltungsbereich: Diese Datei beschreibt die PoWi-Welt „Plakatwand“ (Fachseite, Lerntools, Memory) und die fachübergreifenden Elemente Startseite, Kopfzeile, Passwortseite und Rechtsseiten, die heute in derselben Sprache gebaut sind. Jedes künftige Fach bekommt eine **eigene visuelle Welt**; ev. Religion übernimmt weder Halbjahresfarben noch Mast, Störer, Kabelbinder oder Holztisch. Was an Startseite und Kopfzeile fachneutral bleibt, wird festgelegt, wenn die zweite Welt entsteht. Bewusste Abweichungen vom Richtungsvertrag: Die Kurswahl GK/LK sitzt im PoWi-Kopf statt in der schwarzen Kopfzeile; der Holztisch ist ein CC0-Foto (Poly Haven „Wood Table 001“) statt einer generierten Textur; die Litfaßsäule wird (noch) nicht als Motiv genutzt.

**Key Characteristics:**
- Betongrau-Wand mit Körnung als Grund, weiße Bögen ohne Rundung als einzige Lesefläche.
- Fünf Halbjahresfarben als Orientierungscode, nie als Dekor; sie fließen über ein einziges Token-Paar (`--hj` / `--hj-ink`).
- Zwei Stimmen: Plakatschrift für Nummern und Titel, Source Serif 4 für alles Lesbare (höchstens 68 Zeichen).
- Zustand als Zeichen mit Wort: Störer, Erledigt-Streifen, Zuletzt-Fähnchen.
- Kabelbinder-Laschen und Laternenmast als wiederkehrende Signaturen.
- Bewegung heißt Kleben: 380 ms mit leichtem Überschwingen, sonst kurze, ruhige Rückmeldung.
- Alles selbst gehostet: Schriften als OFL-Dateien im Repo, Bilder mit Herkunftsnachweis.

## Colors

Druckschwarz auf Plakatweiß vor kühlem Betongrau, dazu fünf satte Halbjahresfarben und zwei Signalfarben; jede Farbe hat eine Aufgabe.

### Primary
- **Druckschwarz Grundlagen** (#141618, `gl`): Halbjahresplakat „G“ und Themenplakate der Grundlagen; auf Schwarz werden die Kabelbinder zu Grau (`g5`), damit sie sichtbar bleiben.
- **Zinnober Q1** (#D23A1F, `q1`): Plakat Q1 mit weißer Schrift. Zusätzlich als Stempelfarbe der Serie im Memory („Serie“).
- **Kobalt Q2** (#2340C8, `q2`): Plakat Q2 mit weißer Schrift.
- **Petrol Q3** (#0A6E72, `q3`): Plakat Q3 mit weißer Schrift.
- **Goldgelb Q4** (#F2B300, `q4`): Plakat Q4, immer mit Druckschwarz als Schrift. Zugleich der Textmarker der Wand (siehe Markierer-Regel).

### Secondary
- **Kontrollgrün** (#1B6E3E, `go`): Knopf „Korrekturdatei herunterladen“, Streifen „Erledigt“, „gut“-Bewertung, Fortschrittsbalken, Trefferring im Memory.
- **Kontrollgrün hell** (#e6f2ea, `go-tint`) mit **Kontrollgrün tief** (#0f4527, `go-deep`): Fläche und Schrift für bestätigte Zustände (Erledigt-Häkchen, richtige Antwort).
- **Warnrot** (#B3261E, `stop`): Fehlermeldungen, „noch nicht“-Bewertung, abgelaufene Zeit in der Abi-Simulation.
- **Warnrot hell** (#fbe9e7, `stop-tint`) mit **Warnrot tief** (#7a1a14, `stop-deep`): Fläche und Schrift für Warnungen (Chat-Hinweis, falsche Antwort).

### Tertiary
Materialfarben. Sie beschreiben Gegenstände, nicht Oberflächen, und bleiben in ihrem Objekt. Außer `blueback` stehen sie im CSS als Literale im Memory-Block.
- **Blueback-Graublau** (#9fb1c2, `blueback`): Rückseite von Plakatpapier. Bildet als Verlauf (#b2c1cf → #8fa3b6) mit Körnung den Rücken der Memory-Karten.
- **Nussbaum** (#3b2014, `walnut`): Grundton des Holztischs unter dem Foto.
- **Kartenkarton** (#fffdf8, `card-stock`): warmweiße Vorderseite der Memory-Karten, Lernstreifen und Zoomkarte. Nur am Tisch; an der Wand ist Papier reinweiß.
- **Kartenkante** (#d8d1c2, `card-edge`): Stapelkante unter Karten und Spielbogen.
- **Beschreibungsband** (#6f87a0, `def-stripe`): Kopfband der Beschreibungskarten im Memory (Begriffskarten tragen ein schwarzes Band).

### Neutral
Die Betongrau-Leiter, kühl (Farbton um 240°), vom Papier bis zum Druckschwarz:
- **Plakatweiß** (#ffffff, `paper`): jeder Bogen, jedes Plakat, jedes Schild, jedes Eingabefeld.
- **Beton hell** (#f1f3f4, `g1`): Hover auf Weiß, Gesetzestext-Bögen, Operator-Kasten, Tabellen-Zebra, Religion-Platzhalter.
- **Beton** (#e1e4e6, `g2`): die Wand selbst (`body`, mit `--grain`), leere Fortschrittsbalken.
- **Beton mittel** (#c7ccd0, `g3`): Haarlinien in Tabellen, Listen und Chat.
- **Fuge** (#868d92, `g4`): 2px-Rahmen von Eingabefeldern und Pillen, Link-Unterstreichung. Die hellste Linie; nie Textfarbe (3,4:1 auf Weiß).
- **Schiefer** (#52595e, `g5`): Sekundärtext, Quellen, Hinweise (7,1:1 auf Weiß).
- **Asphalt** (#2a2f33, `g6`): Untertitel in Serif, Hover des schwarzen Knopfs.
- **Druckschwarz** (#141618, `ink`): Text, Kopfzeile, Merke-Bögen, Tabellenköpfe, Rahmen der Bedienelemente, Kabelbinder.

### Named Rules
**The Halbjahr-Code Rule.** Eine Farbfläche in Halbjahresfarbe heißt immer „hier bist du“: aktives Halbjahresplakat, aktives Mast-Schild, Themenplakat-Kopf, Kopfband der Karteikarte, Schrittziffern. Sie kommt ausschließlich über `data-hj` → `--hj` / `--hj-ink`; Q4 trägt Druckschwarz, alle anderen Weiß.

**The Vierer Rule.** Wo Feibitur als Ganzes auftritt (Favicon, Passwortbogen, PoWi-Karte der Startseite, Memory-Kartenrücken, Konfetti), stehen die Halbjahresfarben gemeinsam in fester Reihenfolge Q1 · Q2 · Q3 · Q4, wo das ganze Kursraster gemeint ist mit Grundlagen-Schwarz davor. Keine einzelne Halbjahresfarbe wird zur Markenfarbe; das wahrt die politische Neutralität.

**The Betongrau-Leiter Rule.** Text, Flächen und Linien nehmen Neutrale nur aus `paper`, `g1`–`g6`, `ink`. Materialdarstellungen (Mastmetall, Holz, Kartenkante) sind keine Neutralen und verlassen ihr Objekt nicht.

**The Markierer Rule.** Goldgelb ist auch der Textmarker der Wand: Fokusring auf dunklem Grund, Textauswahl, Fokus-Halo der Eingabefelder, Fähnchen „Zuletzt hier“, Zettel „Weiter, wo du aufgehört hast“, Abitur-Aushang, Lerntools-Knopf. Als Schriftfarbe nur auf Druckschwarz oder dem Holztisch, nie auf Weiß.

## Typography

**Display Font:** Archivo, variabel in Breite (62–125 %) und Gewicht (100–900) (mit Helvetica Neue, Arial)
**Body Font:** Source Serif 4, variabel 200–900, aufrecht und kursiv (mit Georgia, Times New Roman)

**Character:** Archivo in 66 % Breite und Gewicht 850 ist die Plakatschrift: schmal, schwer, in Versalien, mit Durchschuss unter 1 wie gedruckte Wahlplakate. Source Serif 4 ist die ruhige Lesestimme daneben. Beide liegen als WOFF2 (latin und latin-ext, SIL OFL) in `assets/fonts`; der lateinische Archivo-Schnitt wird vorgeladen.

### Hierarchy
- **Display** (850, clamp(4.4rem, 19vw, 12rem), 0.82, Breite 66 %, Versalien): nur die Wortmarke „Feibitur“ auf Start- und Passwortseite.
- **Headline** (850, clamp(2.6rem, 8.5vw, 6.2rem), 0.84, Breite 66 %, Versalien): Seitentitel der Fachwelt und der Lerntools.
- **Poster-Nummer** (850, clamp(3.6rem, 9vw, 6.4rem), 0.8): die Unterthemen-Nummer („Q2.3“) im Themenplakat. Halbjahresplakate tragen ihre Kennung in 2.3rem, Mast-Schilder in 1.5rem, Aufgaben ihre Nummer in 1.9rem, alle im selben Schnitt.
- **Headline-Poster** (850, clamp(2rem, 5.2vw, 4.6rem), 0.9, Breite 66 %, Versalien, Silbentrennung): Titel des Unterthemas über die volle Plakatbreite.
- **Title-Poster** (850, 1.7rem, 1, Breite 66 %, Versalien): Abschnittstitel auf Bögen (Anleitung, Glossar, Kann-Listen, Simulation; 1.5–2rem).
- **Title** (800, 1.32rem, 1.18, Breite 90 %, gemischt): Überschrift eines Inhaltsbogens. Gemischte Schreibung, weil Fachtitel lang sind.
- **Body** (Source Serif 4, 400, 1.0625rem, 1.62): Lesetext in Bögen, höchstens 68ch, Silbentrennung an, `text-wrap: pretty`. Fachtexte 1.09rem. Definitionen, Aufgabenstellungen, Materialien, Untertitel ebenfalls in Serif.
- **Body-UI** (Archivo, 400, 16px, 1.55): Bedienung, Tabellen (0.93rem, Ziffern tabellarisch), Chat-Eingaben.
- **Button** (700, 0.95rem, 1.15, Breite 92 %, +0.01em): alle Knöpfe und das Kurswahl-Segment.
- **Section-Tab** (800, 1.02rem, Breite 85 %, Versalien, +0.02em): Bereichsschalter Fachbegriffe · Inhalte · Übungsaufgaben.
- **Label** (700, 0.7rem, Breite 88 %, Versalien, +0.04em bis +0.08em): Abzeichen („Abi 2027: Schwerpunkt“) und Bogen-Art („Merke“), immer mit 1,5px-Rahmen.
- **Stamp** (850, 0.82rem, Breite 75 %, Versalien, +0.08em): Störer „Nur LK“, Streifen „Erledigt“, Memory-Serie.

### Named Rules
**The Plakatschrift Rule.** Archivo 66 % / 850 / Versalien / Durchschuss ≤ 0.9 gilt für Nummern, Titel, Wortmarke und Stempel; nie für Sätze, die gelesen werden müssen.

**The Ruhige-Spalte Rule.** Alles, was gelesen wird, steht in Source Serif 4 auf Weiß, höchstens 68 Zeichen breit, ohne Bewegung und ohne Schräglage.

## Layout

Die Wand ist der Raum, die Bögen sind die Inhalte. Zwischen zwei Bögen bleibt immer Wand sichtbar (`wall-gap` 10px in der Plakatbahn, `stack` 1.1rem zwischen Inhaltsbögen). Seitliche Rinne 16px (`gutter`), in der Fachwelt unter 560px 10px (`gutter-tight`).

- **Startseite** (max. 1180px): Wortmarke in Display-Größe (bis 12rem), darunter ein asymmetrisches Raster 1.55fr / 1fr. Die PoWi-Karte überspannt zwei Zeilen (min. 340px) und trägt unten die Halbjahresleiste randabfallend; rechts gestapelt Lerntools (schwarz) und ev. Religion (`g1`, Platzhalter). Darunter der gelbe Weiter-Zettel. Unter 860px einspaltig.
- **Fachwelt PoWi** (max. 1400px): Kopf mit Titel links und Kurswahl rechts, darunter der Abitur-Aushang, dann die Halbjahres-Plakatbahn (fünf gleiche Spalten, Abstand 10px, aktives Plakat 10px angehoben). Darunter Mast (300px, ab 1100px 250px, klebt oben mit 0.8rem) und Plakatfläche. Inhalte stehen 2fr / 1fr mit dem klebenden Chat rechts; unter 1024px darunter (max. 560px hoch).
- **Mobil** (≤ 860px): Die Plakatbahn wird ein waagerecht scrollbarer Streifen aus 150px breiten Plakaten mit Scroll-Snap. Ist ein Unterthema offen, wird der Mast zur waagerechten Schild-Leiste über dem Plakat: eine 6px-Metallstange quer, Schilder nur mit Nummer, ohne Kabelbinder.
- **Lerntools** (max. 1100px): Gruppen als schwarzer Plakatkopf mit einem Bogen darunter; jedes Werkzeug ist eine Zeile (Titel 15rem · Beschreibung · Pfeil), keine Kacheln.
- **Rechtsseiten** (max. 820px) und Religion-Platzhalter (max. 900px): ein einzelner Bogen mittig.
- **Umbrüche:** 1100, 1024, 860, 760, 640 (Memory), 560, 360px. Lesbar ab 320px.

## Elevation & Depth

Die Wand ist flach; Tiefe entsteht nur dort, wo Papier auf Papier liegt. Jeder Bogen trägt dieselbe Klebeschatten-Kombination aus 1px-Kontakt und weichem, kurzem Fall (`--sheet-shadow`). Bedienelemente haben keinen Schatten, sondern einen 2px-Rahmen. Der Holztisch des Memory hat ein eigenes Tiefenvokabular: Karten und Spielbogen zeigen ihre Kartonstärke als gestapelte Kante plus tiefen, weichen Schlagschatten unter warmem Lampenlicht.

### Shadow Vocabulary
- **Kleister** (`box-shadow: 0 1px 1px rgba(20,22,24,.08), 0 8px 18px -10px rgba(20,22,24,.35)`): jeder Bogen, jedes Plakat, Schild, Zettel und Abschnitt an der Wand.
- **Angehoben** (`box-shadow: 0 14px 26px -12px rgba(20,22,24,.55)`): nur das aktive Halbjahresplakat, zusammen mit `translateY(-10px)`.
- **Karteikarte** (`box-shadow: 0 1px 1px rgba(20,22,24,.1), 0 18px 34px -16px rgba(20,22,24,.55)`): die wendbare Lernkartei-Karte.
- **Stempel** (`box-shadow: 0 2px 6px rgba(20,22,24,.3)`): Störer und Erledigt-Streifen, die auf dem Bogen liegen; das Zuletzt-Fähnchen mit `0 2px 4px rgba(20,22,24,.25)`.
- **Kartenstärke am Tisch** (`box-shadow: 0 1px 0 #e6e1d6, 0 2px 0 #d8d1c2, 0 3px 0 #c9c1b0, 0 12px 18px -8px rgba(0,0,0,.7)`): Memory-Vorderseiten; Rücken mit blaugrauen Kanten (#6d8193, #5e7183, #50606f).
- **Spielbogen am Tisch** (`box-shadow: 0 2px 0 #e6e1d6, 0 4px 0 #d8d1c2, 0 26px 50px -18px rgba(0,0,0,.75)`): Einstellungen und Siegerehrung.

### Named Rules
**The Kleister Rule.** An der Wand klebt alles flach mit demselben Klebeschatten; nur das aktive Halbjahresplakat hebt sich ab. Knöpfe, Felder und Segmente bekommen Rahmen statt Schatten.

## Shapes

Papier hat Ecken: Bögen, Plakate, Schilder, Tabellen und Abschnittsschalter stehen mit 0px. Bedienelemente sind fast eckig (2px) mit 2px Druckschwarz-Rahmen. Gerundet sind nur Gegenstände: Kabelbinder-Laschen (3px), der Mast (8px breit, 4px rund, Metallverlauf #8f9492 → #c8ccca → #7d8280), Memory-Karten (7px, Format 3:4), die Zoomkarte (12px) sowie runde Schließknöpfe am Tisch (44px). Schräge Formen gibt es zwei: diagonale 45°-Streifen in der rechten oberen Bogenecke (Störer, Erledigt) und leicht verdrehte aufgeklebte Einzelobjekte (Passwortbogen −0.8°, Weiter-Zettel −0.6°, Zuletzt-Fähnchen 2.5°, Spielbogen −0.7°, Memory-Karten zufällig ±2.5°, Serien-Stempel −4°). Symbole sind Inline-SVG-Linien (24er Raster, Strich 2–2.6, runde Enden, `currentColor`), 18–22px.

## Components

### Buttons
Eckig, kräftig, gedruckt.
- **Shape:** fast eckig (2px), 2px Rahmen in Druckschwarz, mindestens 44px hoch.
- **Primary:** Druckschwarz mit Weiß (`button-primary`), Polster 0.55rem 1.1rem, Schrift Button-Stil. Hover Asphalt (`g6`).
- **Secondary:** Weiß mit Druckschwarz-Rahmen; Hover `g1`. Ghost-Variante transparent. Klein: 38px, 0.88rem.
- **Korrekturdatei:** Kontrollgrün mit Weiß, 50px hoch, Download-Symbol; Hover #155a32. Der einzige grüne Knopf der Seite und fest im Auftrag verankert.
- **Lerntools in der Kopfzeile:** Goldgelb mit Druckschwarz; Hover #ffc61a.
- **Hover / Focus / Active:** Hover nur bei Zeiger-Geräten; Druck `scale(.97)` in 160ms `--ease-out`; Fokus 3px Druckschwarz-Umriss mit 2px Abstand, auf dunklem Grund Goldgelb.
- **Memory-Knopf:** Der Einstieg ins Memory ist ein Holzknopf (Verlauf #8a5629 → #6b3f1c, Rahmen #5a3418, innere Lichtkante) und kündigt den Tisch schon an der Wand an.

### Kurswahl-Segment
- **Style:** Weißes Segment mit 2px Druckschwarz-Rahmen, Trennstriche innen; gewählter Kurs Druckschwarz mit Weiß (`aria-pressed`). Sitzt rechts im PoWi-Kopf mit dem Vorsatz „Mein Kurs:“. Solange nichts gewählt ist, steht darunter ein Hinweis mit goldgelbem Quadrat.

### Abzeichen
- **Style:** Label-Schrift mit 1,5px-Rahmen in Textfarbe. „Abi 2027: Schwerpunkt“ und „LK-Niveau“ gefüllt Druckschwarz; „kein Schwerpunkt 2027“ nur Rahmen in Schiefer. Im Themenplakat invertiert in `--hj-ink` / `--hj`. Operator-Abzeichen in Aufgaben ebenso, mit Rahmen in Druckschwarz.

### Cards / Containers (Bögen)
- **Corner Style:** 0px.
- **Background:** Plakatweiß; Merke-Bogen Druckschwarz mit Weiß (Tabellenkopf dort Goldgelb); Gesetzestext-Bogen `g1`.
- **Shadow Strategy:** Kleister (siehe Elevation & Depth).
- **Border:** keiner; nur Abbildungen und Materialtexte erhalten eine 1px-Haarlinie `g3`.
- **Internal Padding:** `sheet` (1.35rem 1.6rem 1.45rem), unter 560px `sheet-compact`.
- **Kopf:** Titel im Title-Stil, rechts daneben die Bogen-Art (Label mit Rahmen) und der Vorlese-Knopf (38px). Die Bogen-Art steht neben, nie über dem Titel.
- **Tabellen:** Kopf Druckschwarz mit Weiß, Zebra `g1`, Haarlinien `g3`, Archivo 0.93rem, waagerecht scrollbar statt gestaucht.
- **Schaubilder:** Inline-SVG auf Weiß mit Haarlinie; beim Build passt `plakat_svg` sie an die Welt an (Farben auf Druckschwarz, Zinnober, Kobalt, Goldgelb, Archivo statt Systemschrift, eckige Kästen). Materialien zu Aufgaben bleiben im Original.

### Inputs / Fields
- **Style:** Weiß, 2px Rahmen `g4`, 2px Rundung, Schrift erbt.
- **Focus:** Rahmen Druckschwarz plus 3px goldgelber Halo, kein Browser-Umriss.
- **Error:** Text in Warnrot, fett, darunter (Passwortseite); Auswahl falsch: Rahmen Warnrot auf `stop-tint`, richtig: Kontrollgrün auf `go-tint`. Checkboxen und Radios in Druckschwarz, 18px.

### Navigation
- **Kopfzeile:** Druckschwarz, Wortmarke links in Plakatschrift (1.75rem, mobil 1.5rem), rechts kleine Knöpfe mit halbtransparent weißem Rahmen; Lerntools goldgelb. Unter 760px nur das Werkzeug-Symbol.
- **Halbjahres-Plakatbahn:** fünf weiße Plakate mit 12px-Oberkante in ihrer Halbjahresfarbe, Kennung in Plakatschrift (2.3rem), Langtitel darunter (600, 0.86rem). Das aktive Plakat ist vollflächig in seiner Farbe und 10px angehoben; Hover hebt inaktive um 4px.
- **Laternenmast:** senkrechte Metallstange links, Überschrift „Unterthemen“; jedes Unterthema ist ein weißes Schild, mit zwei Kabelbindern (40 × 7px) an die Stange gebunden: Nummer in Plakatschrift, Titel, Abzeichen. Aktiv vollfarbig in `--hj`. Hover schiebt das Schild 3px nach rechts.
- **Bereichsschalter:** drei gleich breite weiße Felder (54px) mit Symbol und Versalien; aktiv Druckschwarz mit Weiß. Unter 560px Symbol über Text.

### Themenplakat (Signatur)
Kopf vollflächig in der Halbjahresfarbe, zwei Kabelbinder-Laschen (34 × 13px, Druckschwarz, innere Lichtkante) bei 12 % von links und rechts an der Oberkante. Zeile mit riesiger Nummer und Schwerpunkt-Abzeichen, darunter der Titel über die volle Breite, dann Erlass-Hinweis in Serif und die aufklappbaren Kerncurriculum-Stichworte. Beim Öffnen eines neuen Unterthemas wird das Plakat angeklebt: 380ms `--ease-paste`, von −14px, −1.4° und 102 % auf null, Drehpunkt oben Mitte.

### Störer, Erledigt-Streifen, Zuletzt-Fähnchen (Signatur)
- **Störer „Nur LK“:** 170px breiter Diagonalstreifen (45°) über der rechten oberen Ecke eines LK-Bogens, Druckschwarz mit Weiß, Stamp-Stil; auf dem schwarzen Merke-Bogen Goldgelb mit Druckschwarz.
- **Erledigt-Streifen:** 150px, Kontrollgrün mit Weiß, Wort „Erledigt“, über der Ecke einer bearbeiteten Aufgabe; für Screenreader zusätzlich „bearbeitet“.
- **Zuletzt-Fähnchen:** Goldgelber Zettel „Zuletzt hier“ (0.68rem, Versalien), 2.5° gedreht, oben rechts am zuletzt besuchten Mast-Schild. Auf der Startseite entspricht ihm der Weiter-Zettel.

### Passwortseite
Ein einzelner weißer Bogen (max. 420px) mittig auf der Wand, −0.8° gedreht, mit zwei Kabelbindern; Wortmarke, Satz in Schiefer, Feld, schwarzer Knopf, unten randabfallend die fünf Halbjahresstreifen (14px).

### Fachbegriffe-Memory: der Holztisch (Signatur)
Ein Vollbild-Raum innerhalb der Fachwelt. Grund ist das Holzfoto (`assets/img/holztisch.webp`, CC0, Kachel 760px) über Nussbaum, mit dunkler Vignette, schwachem Lichtstreif und warmem Lampenkegel von oben. Spielbogen (Einstellungen, Siegerehrung) sind weiße Bögen (max. 540px, −0.7°) mit Kartenstärke.
- **Kartenrücken:** Blueback-Verlauf mit Körnung, 5px weißer Innenrahmen, Aufdruck „FEIBITUR“ gesperrt oben, großes „F“ in Plakatschrift, unten die vier Q-Streifen.
- **Vorderseite:** Kartenkarton; Begriffskarten mit schwarzem Kopfband und Begriff in Plakatschrift (72 %), Beschreibungskarten mit Beschreibungsband und Text in Serif. Keine Beschriftung der Kartenart.
- **Spieler:** Namensschilder links und rechts mit eigenem Kartenstapel und Punktzahl in Goldgelb (Plakatschrift); wer dran ist, bekommt goldgelben Rahmen und „ist dran“.
- **Bewegung:** Austeilen gestaffelt, Wenden 3D in 460ms `--ease-io`, Treffer mit 5px grünem Ring und Anheben, Fehlgriff als kurzes Rütteln, gefundenes Paar fliegt in 640ms zum Stapel des Spielers. Siegerehrung mit Podest (Sieger Goldgelb, Zweiter Schiefer) und Konfetti in den Halbjahresfarben plus Weiß. Ohne Ton.

### Lerntools
Schwarzer Gruppenkopf in Plakatschrift, darunter ein Bogen mit Werkzeug-Zeilen, getrennt durch Haarlinien; Hover `g1` und Pfeil 4px nach rechts. Der Countdown ist ein schwarzer Bogen mit goldgelber Zahl in Plakatschrift; die Abi-Simulation hat eine klebende schwarze Zeitleiste.

## Do's and Don'ts

### Do:
- **Do** die Halbjahresfarbe nur über `data-hj` → `--hj` / `--hj-ink` setzen; Q4 Goldgelb trägt Druckschwarz, alle anderen Halbjahresfarben Weiß.
- **Do** jeden Inhaltsabschnitt als eigenen weißen Bogen kleben (`--paper`, Ecken 0, `--sheet-shadow`) und zwischen den Bögen die Betongrau-Wand sichtbar lassen (mindestens 10px, im Lesefluss 1.1rem).
- **Do** Nummern, Titel und Stempel in Plakatschrift setzen (Archivo, `--poster-stretch` 66 %, 850, Versalien, Durchschuss 0.8–0.9) und alles Lesbare in Source Serif 4 (1.0625rem / 1.62, höchstens 68ch).
- **Do** jeden Zustand mit Zeichen und Wort markieren: Störer „Nur LK“, Streifen „Erledigt“, Fähnchen „Zuletzt hier“, Halbjahreskennung im Plakat.
- **Do** für alles Klebende `--t-paste` (380ms) mit `--ease-paste` nutzen, für Rückmeldungen 150–220ms `--ease-out`, für Wenden `--ease-io`, und unter `prefers-reduced-motion` darauf verzichten.
- **Do** Bedienelemente mindestens 44px hoch, fast eckig (2px) und mit 2px Druckschwarz-Rahmen bauen.
- **Do** jedes Inhalts-Schaubild durch `plakat_svg` schicken (Archivo, eckige Kästen, Weltfarben); Aufgabenmaterialien bleiben im Original.
- **Do** Schriften und Bilder nur aus dem Repo laden (`assets/fonts`, `assets/img`) und neben jedes Rasterbild eine Herkunftsdatei (`*.json`) legen.

### Don't:
- **Don't** Raster aus gleich großen Icon-Kacheln, Pastellflächen oder Fortschrittsringe bauen; Lerntools stehen als Zeilen auf einem Bogen.
- **Don't** eine einzelne Halbjahresfarbe zur Markenfarbe machen; wo Feibitur als Ganzes erscheint, stehen alle Halbjahresfarben gemeinsam.
- **Don't** Grautöne außerhalb der Betongrau-Leiter für Text, Flächen oder Linien verwenden; `g4` ist die hellste Linie, Text beginnt bei `g5`.
- **Don't** Papier runden: Bögen, Plakate, Schilder und Tabellen haben Ecken 0; Rundung gehört nur Gegenständen (Kabelbinder 3px, Memory-Karten 7px).
- **Don't** Lesetexte, Tabellen oder Aufgaben schräg stellen; Drehung gibt es nur für einzeln aufgeklebte Objekte (bis 2.5°) und Stempel (−4°).
- **Don't** Spitzmarken oder Etiketten über Überschriften oder auf Memory-Kartenflächen setzen; Begriff und Beschreibung unterscheiden sich durch Kopfband und Schrift.
- **Don't** Goldgelb als Schriftfarbe auf Weiß einsetzen.
- **Don't** die Plakatwand in ein anderes Fach übernehmen; ev. Religion bekommt eine eigene Welt.
