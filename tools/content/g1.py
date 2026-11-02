# -*- coding: utf-8 -*-
"""G1 Wie analysiere ich vorliegendes Material tiefgründig?"""

SVG_ACHSE = """<svg viewBox='0 0 760 300' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' font-size='13' role='img' aria-labelledby='act'>
<title id='act'>Gleiche Daten, unterschiedliche Wirkung: abgeschnittene y-Achse</title>
<rect width='760' height='300' fill='#fff'/>
<text x='380' y='22' text-anchor='middle' font-weight='700' font-size='15' fill='#14213d'>Gleiche (fiktive) Daten – unterschiedliche Wirkung</text>
<text x='190' y='48' text-anchor='middle' font-weight='700' fill='#333'>Achse beginnt bei 0</text>
<line x1='60' y1='250' x2='330' y2='250' stroke='#888'/><line x1='60' y1='60' x2='60' y2='250' stroke='#888'/>
<text x='52' y='254' text-anchor='end' fill='#666' font-size='11'>0</text><text x='52' y='160' text-anchor='end' fill='#666' font-size='11'>25</text><text x='52' y='66' text-anchor='end' fill='#666' font-size='11'>50</text>
<rect x='95' y='99' width='70' height='151' fill='#5b77b5'/><rect x='215' y='92' width='70' height='158' fill='#14213d'/>
<text x='130' y='92' text-anchor='middle' font-weight='700' fill='#333'>40 %</text><text x='250' y='85' text-anchor='middle' font-weight='700' fill='#333'>42 %</text>
<text x='130' y='270' text-anchor='middle' fill='#333'>2024</text><text x='250' y='270' text-anchor='middle' fill='#333'>2025</text>
<text x='570' y='48' text-anchor='middle' font-weight='700' fill='#b5302a'>Achse beginnt bei 39</text>
<line x1='440' y1='250' x2='710' y2='250' stroke='#888'/><line x1='440' y1='60' x2='440' y2='250' stroke='#888'/>
<text x='432' y='254' text-anchor='end' fill='#666' font-size='11'>39</text><text x='432' y='160' text-anchor='end' fill='#666' font-size='11'>40,5</text><text x='432' y='66' text-anchor='end' fill='#666' font-size='11'>42</text>
<path d='M436 238 l8 -6 M436 244 l8 -6' stroke='#b5302a' stroke-width='1.5'/>
<rect x='475' y='187' width='70' height='63' fill='#5b77b5'/><rect x='595' y='63' width='70' height='187' fill='#14213d'/>
<text x='510' y='180' text-anchor='middle' font-weight='700' fill='#333'>40 %</text><text x='630' y='56' text-anchor='middle' font-weight='700' fill='#333'>42 %</text>
<text x='510' y='270' text-anchor='middle' fill='#333'>2024</text><text x='630' y='270' text-anchor='middle' fill='#333'>2025</text>
<text x='380' y='292' text-anchor='middle' fill='#555' font-size='12'>Ein Anstieg um 2 Prozentpunkte wirkt rechts wie eine Verdreifachung. Prüfe deshalb immer die Achsenbeschriftung!</text>
</svg>"""

TOPIC = {
    "id": "g1",
    "begriffe": [
        {"b": "Einleitungssatz", "kurz": "erster Satz einer Analyse/Zusammenfassung mit Autor, Titel, Textsorte, Quelle, Erscheinungsjahr und Thema.",
         "lang": "Der <b>Einleitungssatz</b> ist Pflicht bei „zusammenfassen“ und „wiedergeben“: Er nennt <b>Autor/in, Titel, Textsorte, Quelle, Erscheinungsdatum und Thema</b> (ggf. Adressat). Beispiel: „In dem Kommentar ‚…‘ von …, erschienen am … in …, setzt sich der Autor mit … auseinander.“ Die Lösungshinweise im Landesabitur fordern ihn ausdrücklich."},
        {"b": "Textsorte", "kurz": "Art eines Textes, z. B. Bericht, Kommentar, Interview, Rede, Leitartikel, wissenschaftlicher Fachtext.",
         "lang": "Die <b>Textsorte</b> verrät dir die Absicht: Ein <b>Bericht</b> informiert möglichst sachlich, ein <b>Kommentar</b> oder Leitartikel bezieht Position, eine <b>Rede</b> will überzeugen und mobilisieren, ein <b>Interview</b> gibt die Sicht der befragten Person wieder, ein <b>Fachtext</b> erklärt wissenschaftlich."},
        {"b": "Intention", "kurz": "Absicht, die ein Autor mit seinem Text verfolgt (z. B. informieren, überzeugen, appellieren, kritisieren).",
         "lang": "Die <b>Intention</b> ist das Ziel des Textes: Will der Autor informieren, überzeugen, warnen, zum Handeln aufrufen oder eine Position diskreditieren? Hinweise geben Textsorte, Adressat, Schlussforderung und sprachliche Mittel. Die Intention musst du belegen, nicht nur behaupten."},
        {"b": "Position", "kurz": "die Haltung des Autors zum Thema, z. B. befürwortend, ablehnend, differenziert.",
         "lang": "Die <b>Position</b> beschreibt, wie der Autor zum Thema steht. Formuliere sie präzise, z. B.: „Der Autor lehnt eine Einschränkung der Normenkontrolle ab, räumt aber ein, dass …“. Oft steht die Position im ersten oder letzten Absatz."},
        {"b": "These", "kurz": "zentrale Behauptung, die mit Argumenten begründet wird.",
         "lang": "Eine <b>These</b> ist eine Behauptung, deren Richtigkeit erst bewiesen bzw. begründet werden muss, z. B. „Die Fünf-Prozent-Hürde schadet der Demokratie.“ Zu einer guten Analyse gehört, die <b>Hauptthese</b> von Nebenthesen zu unterscheiden."},
        {"b": "Argument", "kurz": "Begründung, die eine These stützt; besteht aus Behauptung, Begründung und Beleg/Beispiel.",
         "lang": "Ein vollständiges <b>Argument</b> hat drei Teile: <b>Behauptung</b> (These), <b>Begründung</b> (warum?) und <b>Beleg/Beispiel</b> (Fakten, Zahlen, Expertenaussagen, Erfahrungen). Merkhilfe: „BBB“. Prüfe in der Analyse, ob Belege fehlen oder einseitig sind."},
        {"b": "Argumentationsstruktur", "kurz": "Aufbau einer Argumentation, z. B. steigernd, dialektisch (Pro und Contra) oder linear.",
         "lang": "Die <b>Argumentationsstruktur</b> beschreibt, wie ein Text aufgebaut ist: <b>linear</b> (Argumente in eine Richtung, oft steigernd), <b>dialektisch</b> (Pro und Contra mit Abwägung) oder mit <b>Einwandvorwegnahme</b> (Gegenargument nennen und entkräften). Achte auf Signalwörter wie „zwar … aber“, „hinzu kommt“, „deshalb“."},
        {"b": "Indirekte Rede", "kurz": "Wiedergabe fremder Aussagen im Konjunktiv I („Der Autor meint, die Politik sei …“).",
         "lang": "In Zusammenfassungen und Wiedergaben machst du mit der <b>indirekten Rede</b> (Konjunktiv I) deutlich, dass es nicht deine Meinung ist: „Der Autor behauptet, das Gericht <i>habe</i> zu viel Macht.“ Ist der Konjunktiv I gleich dem Indikativ, nimm Konjunktiv II („sie hätten“)."},
        {"b": "Materialbeleg", "kurz": "Angabe der Fundstelle im Material (Zeile/Absatz), die eine Aussage stützt.",
         "lang": "Ab Anforderungsbereich II verlangt die Operatorenliste <b>Belege sowie Text- oder Materialbezüge</b>. Gib Fundstellen an, z. B. „(Z. 12 ff.)“ oder „(M1, Abs. 3)“. Belege machen deine Analyse überprüfbar und unterscheiden sie von bloßen Behauptungen."},
        {"b": "Absolute Zahl", "kurz": "konkrete Anzahl oder Menge (z. B. 2,9 Millionen Arbeitslose).",
         "lang": "<b>Absolute Zahlen</b> geben eine Menge an (z. B. Personen, Euro, Tonnen). Sie sagen ohne Bezugsgröße wenig: 1 Million Menschen ist in Deutschland viel weniger als in Luxemburg. Deshalb ergänzt man sie oft um <b>relative Zahlen</b>."},
        {"b": "Relative Zahl", "kurz": "Anteil im Verhältnis zu einer Bezugsgröße, meist in Prozent.",
         "lang": "<b>Relative Zahlen</b> (Prozent, Quoten, je 1.000 Einwohner) setzen Werte ins Verhältnis und machen Vergleiche möglich. Prüfe immer: <b>Prozent wovon?</b> – z. B. von allen Wahlberechtigten oder nur von den gültigen Stimmen?"},
        {"b": "Prozentpunkt", "kurz": "Differenz zwischen zwei Prozentwerten (von 40 % auf 42 % = +2 Prozentpunkte = +5 Prozent).",
         "lang": "Steigt ein Wert von 40 % auf 42 %, ist das ein Plus von <b>2 Prozentpunkten</b>, aber ein Anstieg um <b>5 Prozent</b> (2 von 40). Verwechslungen sind ein häufiger Fehler – und ein beliebter Trick, um Veränderungen größer oder kleiner wirken zu lassen."},
        {"b": "Indexwert", "kurz": "Darstellung einer Entwicklung relativ zu einem Basisjahr, das auf 100 gesetzt wird.",
         "lang": "Bei einem <b>Index</b> wird ein <b>Basisjahr = 100</b> gesetzt. Ein Wert von 112 bedeutet: 12 % mehr als im Basisjahr. Indizes (z. B. Verbraucherpreisindex) zeigen Entwicklungen gut, verraten aber nichts über das absolute Niveau. Achte darauf, welches Basisjahr gewählt wurde."},
        {"b": "Statistikanalyse", "kurz": "methodische Untersuchung einer Statistik in den Schritten: formale Beschreibung, inhaltliche Beschreibung, Auswertung/Interpretation, Kritik.",
         "lang": "Eine <b>Statistikanalyse</b> folgt meist vier Schritten: 1. <b>formal</b> (Titel, Quelle, Jahr, Darstellungsform, Einheiten), 2. <b>inhaltlich beschreiben</b> (wichtigste Werte, Entwicklungen, Extremwerte), 3. <b>auswerten/interpretieren</b> (Zusammenhänge, Ursachen, Fachwissen), 4. <b>kritisch prüfen</b> (Aussagekraft, fehlende Daten, Darstellungstricks)."},
        {"b": "Karikatur", "kurz": "zeichnerische Darstellung, die politische Sachverhalte überspitzt, kritisiert und kommentiert.",
         "lang": "Eine <b>Karikatur</b> ist ein gezeichneter Kommentar. Sie arbeitet mit <b>Übertreibung, Symbolen und Ironie</b>. Analyse in drei Schritten: <b>beschreiben</b> (was sehe ich?), <b>deuten</b> (wofür stehen Personen, Symbole, Text?), <b>beurteilen</b> (Ist die Kritik berechtigt? Was wird ausgeblendet?)."},
        {"b": "Symbol", "kurz": "Bildelement, das für etwas anderes steht (z. B. Waage = Gerechtigkeit, Michel mit Zipfelmütze = deutsches Volk).",
         "lang": "<b>Symbole</b> verdichten Bedeutung: Die <b>Waage</b> steht für Justiz, der <b>deutsche Michel</b> mit Zipfelmütze für das (oft naive) deutsche Volk, der <b>Bär</b> für Russland, der <b>Adler</b> für Deutschland oder die USA, <b>Sterne im Kreis</b> für die EU. In der Analyse musst du ihre Bedeutung erklären."},
        {"b": "Quellenkritik", "kurz": "Prüfung, wer ein Material erstellt hat, mit welcher Absicht und wie verlässlich es ist.",
         "lang": "<b>Quellenkritik</b> fragt: <b>Wer</b> ist Urheber (Ministerium, Verband, Partei, Forschungsinstitut, Zeitung)? Welche <b>Interessen</b> könnten dahinterstehen? Wann und für wen wurde das Material erstellt? Ist die Darstellung vollständig? Gerade bei Verbandsstudien und Parteimaterial ist das wichtig."},
        {"b": "Adressat", "kurz": "Zielgruppe, an die sich ein Text oder eine Rede richtet.",
         "lang": "Der <b>Adressat</b> beeinflusst Sprache und Inhalt: Eine Rede auf einem Parteitag richtet sich an Mitglieder, ein Gastbeitrag in einer Tageszeitung an die breite Öffentlichkeit, ein Fachtext an Experten. Benenne den Adressaten, wenn er erkennbar ist – er hilft, die Intention zu erklären."},
    ],
    "inhalte": [
        {"t": "text", "art": "Erklärung", "titel": "Warum Materialanalyse so wichtig ist",
         "html": "<p>Fast jede Abituraufgabe in Politik und Wirtschaft beginnt mit Material: einem Zeitungsartikel, einem Interview, einer Rede, einer Statistik oder einer Karikatur. Die erste Teilaufgabe (Anforderungsbereich I) verlangt meist, das Material <b>zusammenzufassen, wiederzugeben oder zu beschreiben</b>. Spätere Aufgaben verlangen <b>Analysen</b>, für die du das Material mit deinem Fachwissen verknüpfst.</p><p>„Tiefgründig“ heißt: nicht nur sagen, <b>was</b> drinsteht, sondern auch <b>wie</b> und <b>warum</b> – Wer spricht? Mit welcher Absicht? Mit welchen Argumenten und Belegen? Was fehlt?</p>"},
        {"t": "table", "art": "Merke", "titel": "Textanalyse in fünf Schritten",
         "kopf": ["Schritt", "Leitfrage", "Tipp"],
         "zeilen": [
             ["1. Erschließen", "Worum geht es? Wer schreibt wann, wo, für wen?", "Zweimal lesen; beim zweiten Mal Schlüsselbegriffe markieren und Absätze mit Stichworten versehen."],
             ["2. Einleitung", "Autor, Titel, Textsorte, Quelle, Datum, Thema", "Bei Interviews beide Personen nennen; Hinweise unter dem Text (z. B. zur Person des Autors) nutzen."],
             ["3. Inhalt und Struktur", "Welche Hauptthese? Welche Argumente in welcher Reihenfolge?", "Sinnabschnitte bilden, nicht Absatz für Absatz nacherzählen. Konjunktiv I verwenden."],
             ["4. Argumentation und Sprache", "Wie überzeugt der Autor? Belege, Beispiele, rhetorische Mittel?", "Nur Auffälligkeiten mit Funktion nennen („Die Metapher ‚Kartell‘ soll … diskreditieren“)."],
             ["5. Position und Intention", "Was will der Autor erreichen? Wo steht er politisch?", "Einordnung mit Fachwissen (z. B. Theorie, Partei, Interessengruppe) – immer belegen."],
         ]},
        {"t": "text", "art": "Beispiel", "titel": "Musterformulierungen",
         "html": "<ul><li><b>Einleitung:</b> „In dem Kommentar ‚Regiert Karlsruhe mit?‘, erschienen 2025, setzt sich der Autor kritisch mit der Rolle des Bundesverfassungsgerichts im politischen Prozess auseinander.“</li><li><b>Überleitungen:</b> „Zunächst stellt der Autor fest, … / Im Anschluss daran führt er aus, … / Abschließend fordert er, …“</li><li><b>Indirekte Rede:</b> „Er kritisiert, die Opposition <i>nutze</i> das Gericht als Verlängerung der Politik.“</li><li><b>Analyse:</b> „Durch die rhetorische Frage (Z. 14) unterstreicht die Autorin …“ / „Die Gegenüberstellung von ‚wir‘ und ‚die da oben‘ (Abs. 2) zeigt das populistische Muster …“</li><li><b>Intention:</b> „Der Autor möchte die Leserschaft davon überzeugen, dass …, und richtet sich dabei vor allem an …“</li></ul>"},
        {"t": "text", "art": "Fachtext", "titel": "Statistiken richtig lesen",
         "html": "<p>Statistiken wirken objektiv, sind aber immer das Ergebnis von Entscheidungen: Welche Daten werden erhoben, wie werden sie zusammengefasst, und wie werden sie dargestellt? Eine gründliche Analyse beginnt deshalb mit der <b>formalen Beschreibung</b>: Titel, Quelle (Herausgeber, Erhebungsinstitut), Erhebungszeitraum, Darstellungsform (Tabelle, Säulen-, Linien-, Kreisdiagramm), Einheiten (absolut, Prozent, Index) und Bezugsgröße.</p><p>Danach folgt die <b>inhaltliche Beschreibung</b>. Hier werden die wichtigsten Werte, Höchst- und Tiefstwerte sowie Entwicklungen genannt, ohne dass schon interpretiert wird. Erst im dritten Schritt, der <b>Auswertung</b>, werden die Einzelergebnisse zu einer Gesamtaussage zusammengeführt und mit Fachwissen erklärt, etwa mit möglichen Ursachen und Folgen.</p><p>Den Abschluss bildet die <b>kritische Prüfung</b>. Welche Aussagen lässt die Statistik nicht zu? Fehlen Vergleichswerte oder Zeiträume? Wurde eine Achse abgeschnitten, um Unterschiede größer erscheinen zu lassen? Wer ist der Herausgeber, und könnte er ein Interesse an einer bestimmten Darstellung haben? Häufige Fehler sind die Verwechslung von <b>Prozent und Prozentpunkten</b>, von <b>Korrelation und Kausalität</b> (zwei Dinge treten gemeinsam auf, aber das eine verursacht nicht das andere) sowie die Gleichsetzung von Indexwerten mit absoluten Niveaus.</p>",
         "quelle": "Selbst verfasster Fachtext (Feibitur)."},
        {"t": "svg", "art": "Grafik", "titel": "Achtung, Darstellungstrick: die abgeschnittene Achse", "svg": SVG_ACHSE,
         "caption": "Beide Diagramme zeigen dieselben (fiktiven) Werte. Rechts beginnt die y-Achse nicht bei 0 – der Unterschied wirkt dadurch dramatisch größer."},
        {"t": "table", "art": "Merke", "titel": "Karikaturanalyse in drei Schritten",
         "kopf": ["Schritt", "Was tust du?", "Formulierungshilfe"],
         "zeilen": [
             ["1. Beschreiben", "Zeichner/in, Titel, Quelle, Jahr; Personen, Gegenstände, Texte, Bildaufbau (Vorder-/Hintergrund, Größenverhältnisse)", "„Im Vordergrund ist … zu sehen, der …“"],
             ["2. Deuten", "Bedeutung von Symbolen und Personen; politischer Kontext; Kernaussage", "„Die übergroße Figur symbolisiert … Der Zeichner kritisiert damit …“"],
             ["3. Beurteilen", "Ist die Kritik berechtigt? Was wird zugespitzt oder ausgeblendet?", "„Die Karikatur trifft insofern zu, als …, blendet jedoch aus, dass …“"],
         ]},
        {"t": "text", "art": "Merke", "titel": "Die häufigsten Fehler – und wie du sie vermeidest",
         "html": "<ul><li><b>Nacherzählen statt strukturieren:</b> Fasse Sinnabschnitte zusammen, nicht jeden Absatz einzeln.</li><li><b>Eigene Meinung im AFB I:</b> In Zusammenfassung und Wiedergabe wird nicht bewertet.</li><li><b>Zitieren statt eigene Worte:</b> Die Operatorenliste verlangt grundsätzlich eigene Worte.</li><li><b>Behauptungen ohne Beleg:</b> Ab AFB II immer Material- bzw. Zeilenbezüge.</li><li><b>Fachwissen fehlt:</b> „Analysieren“ heißt erschließen <i>mit</i> Fachkategorien, nicht nur Material wiederholen.</li></ul>"},
    ],
    "aufgaben": [
        {
            "id": "g1-a1",
            "titel": "Methodentraining: Statistik und Kommentar zur Bundestagswahl 2025",
            "kurs": "Grundkurs und Leistungskurs (Methodentraining)",
            "bezug": "Methodenkompetenz (Statistik- und Textanalyse) mit Inhaltsbezug zu Q1.2 (Nationale Wahlen, Parteiensystem).",
            "standards": "Methodenkompetenz: Materialien kriteriengeleitet erschließen, Statistiken auswerten, Argumentationsstrukturen analysieren. Urteilskompetenz: Aussagen auf ihre Angemessenheit hin überprüfen.",
            "aufgaben": [
                {"nr": 1, "operator": "beschreiben", "afb": "I", "be": 25, "text": "Beschreiben Sie die Tabelle (Material 1) formal und inhaltlich."},
                {"nr": 2, "operator": "auswerten", "afb": "II", "be": 25, "text": "Werten Sie Material 1 im Hinblick auf das Verhältnis von Zweitstimmen- und Sitzanteilen aus."},
                {"nr": 3, "operator": "analysieren", "afb": "II", "be": 25, "text": "Analysieren Sie den Kommentar (Material 2) hinsichtlich Position, Argumentationsstruktur und Intention des Autors."},
                {"nr": 4, "operator": "überprüfen", "afb": "III", "be": 25, "text": "Überprüfen Sie die Aussage des Autors, die Fünf-Prozent-Hürde habe „Millionen Wählerinnen und Wähler stummgeschaltet“, unter Einbeziehung von Material 1."},
            ],
            "material": [
                {"titel": "Material 1: Ergebnis der Bundestagswahl vom 23. Februar 2025 (Zweitstimmen und Sitze)", "typ": "tabelle",
                 "kopf": ["Partei", "Zweitstimmen in %", "Sitze", "Sitzanteil in %"],
                 "zeilen": [["CDU/CSU", "28,5", "208", "33,0"], ["AfD", "20,8", "152", "24,1"], ["SPD", "16,4", "120", "19,0"],
                            ["Bündnis 90/Die Grünen", "11,6", "85", "13,5"], ["Die Linke", "8,8", "64", "10,2"], ["SSW", "0,2", "1", "0,2"],
                            ["BSW", "4,98", "0", "0"], ["FDP", "4,3", "0", "0"], ["Sonstige", "4,4", "0", "0"], ["<b>Gesamt</b>", "100", "630", "100"]],
                 "quelle": "Zusammenstellung nach den Angaben der Bundeswahlleiterin zur Bundestagswahl 2025; Werte gerundet, Sitzanteile selbst berechnet. Wahlbeteiligung: 82,5 %. Der SSW ist als Partei der dänischen Minderheit von der Sperrklausel befreit."},
                {"titel": "Material 2: Kommentar „Die stumme Minderheit“ (2025)",
                 "absaetze": [
                     "Fast jede siebte Stimme bei der letzten Bundestagswahl ist im Papierkorb gelandet. Wer BSW, FDP oder eine der vielen Kleinparteien gewählt hat, ist im Parlament nicht vertreten. Millionen Wählerinnen und Wähler hat die Fünf-Prozent-Hürde einfach stummgeschaltet.",
                     "Natürlich: Die Sperrklausel hat eine Geschichte. Nach den Erfahrungen der Weimarer Republik wollte man ein zersplittertes Parlament verhindern. Doch die Bundesrepublik von heute ist eine stabile Demokratie. Andere Länder kommen mit niedrigeren Hürden aus, ohne im Chaos zu versinken.",
                     "Zudem verzerrt die Hürde den Wettbewerb. Wer kleine Parteien wählen möchte, überlegt es sich zweimal, weil er fürchtet, seine Stimme zu verschenken. So schützt die Hürde vor allem die etablierten Parteien vor neuer Konkurrenz.",
                     "Man wird einwenden, dass Koalitionsbildungen schwieriger würden, wenn mehr Parteien im Bundestag säßen. Das mag sein. Aber Demokratie ist kein Effizienzwettbewerb. Ein Parlament soll den Willen der Wählerinnen und Wähler abbilden – und zwar möglichst vollständig.",
                     "Der Bundestag sollte die Hürde deshalb auf drei Prozent senken und eine Ersatzstimme einführen: Wer eine Partei wählt, die an der Hürde scheitert, könnte dann eine zweite Präferenz angeben. Keine Stimme ginge mehr verloren.",
                 ],
                 "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Autors (2025)."},
            ],
            "loesung": [
                {"punkte": [
                    "Formal: Tabelle zum Ergebnis der Bundestagswahl vom 23.02.2025; Quelle: Bundeswahlleiterin (Zusammenstellung), Werte gerundet; Spalten: Zweitstimmenanteil in %, absolute Sitzzahl, Sitzanteil in %; Gesamtzahl 630 Sitze; Hinweis zu Wahlbeteiligung (82,5 %) und SSW-Ausnahme.",
                    "Inhaltlich: CDU/CSU stärkste Kraft (28,5 %, 208 Sitze), AfD zweitstärkste (20,8 %, 152), SPD (16,4 %, 120), Grüne (11,6 %, 85), Linke (8,8 %, 64), SSW 1 Sitz; BSW (4,98 %) und FDP (4,3 %) sowie Sonstige (4,4 %) ohne Sitze.",
                    "Struktur der Beschreibung: vom Wichtigsten zum Speziellen, keine Interpretation.",
                ],
                 "hinweis": "Beschreiben: strukturiert, fachsprachlich (z. B. Prozent vs. Prozentpunkte korrekt), ohne Interpretation."},
                {"punkte": [
                    "Gesamtaussage: Alle im Bundestag vertretenen Parteien erhalten einen höheren Sitzanteil als ihren Zweitstimmenanteil.",
                    "Ursache: Rund 13–14 % der Zweitstimmen (BSW 4,98 + FDP 4,3 + Sonstige 4,4) bleiben wegen der Sperrklausel unberücksichtigt; die Sitze werden auf die übrigen Parteien verteilt (z. B. CDU/CSU +4,5 Prozentpunkte, AfD +3,3 Prozentpunkte).",
                    "Bei 630 Sitzen und Verhältnisausgleich: Die Parteien über 5 % teilen sich 100 % der Sitze mit ca. 86 % der Stimmen.",
                    "Besonderheit: BSW scheiterte äußerst knapp; SSW durch Minderheitenregel vertreten.",
                    "Fachwissen: Verhältniswahl nach Zweitstimmen, Sperrklausel/Grundmandatsklausel, Wahlrecht 2023 (feste Größe 630, Zweitstimmendeckung).",
                    "Ggf. Folgen: Mehrheit für Koalitionen leichter (CDU/CSU + SPD mit ca. 45 % der Stimmen erreichen 328 von 630 Sitzen, also eine absolute Mehrheit).",
                ],
                 "hinweis": "Auswerten: Einzelergebnisse zu einer Gesamtaussage zusammenführen; Prozentpunkte korrekt verwenden; Rechenschritte nachvollziehbar."},
                {"punkte": [
                    "Position: Ablehnung der Fünf-Prozent-Hürde in ihrer jetzigen Form; Forderung nach 3 %-Hürde und Ersatzstimme [5].",
                    "Struktur: Einstieg mit zugespitzter Problembeschreibung („jede siebte Stimme im Papierkorb“, „stummgeschaltet“) [1]; Einräumen des historischen Arguments (Weimar) und Entkräftung durch Stabilität der heutigen Demokratie und Ländervergleich [2]; weiteres Argument: Wettbewerbsverzerrung/Schutz etablierter Parteien [3]; Einwandvorwegnahme (Koalitionsbildung) und Entkräftung mit Wertargument („kein Effizienzwettbewerb“, Repräsentation) [4]; konkrete Forderung [5]. Insgesamt linear-steigernde Argumentation mit Einwandvorwegnahme.",
                    "Sprachliche Mittel mit Funktion: Metaphern („Papierkorb“, „stummgeschaltet“) zur Dramatisierung; Konzessivstruktur („Natürlich…“, „Das mag sein. Aber…“) zur Stärkung der Glaubwürdigkeit.",
                    "Belege: teils vorhanden (Anteil der Stimmen), teils pauschal („andere Länder“ ohne Nennung).",
                    "Intention: Leserschaft von einer Wahlrechtsreform überzeugen; Appell an den Bundestag; Wertmaßstab: möglichst vollständige Repräsentation.",
                ],
                 "hinweis": "Analysieren: Position, Struktur und Intention müssen mit Belegen erschlossen werden; eine reine Zusammenfassung genügt nicht."},
                {"punkte": [
                    "Rechnerische Prüfung: ca. 13,7 % nicht im Bundestag vertretene Zweitstimmen; bei ca. 49–50 Mio. gültigen Zweitstimmen etwa 6–7 Mio. Stimmen; „fast jede siebte Stimme“ (1/7 ≈ 14,3 %) ist annähernd zutreffend; „Millionen“ ist sachlich korrekt.",
                    "Kritische Einordnung von „stummgeschaltet“: Diese Wähler haben gewählt und ihre Stimme wurde gezählt; sie beeinflusst Parteienfinanzierung (Wahlkampfkostenerstattung ab 0,5 %) und politische Signalwirkung; die Wähler sind über Wahlkreisabgeordnete und das freie Mandat (Art. 38 GG: Vertreter des ganzen Volkes) dennoch repräsentiert.",
                    "Gegenargumente zur Sperrklausel-Kritik: Funktionsfähigkeit des Parlaments und Regierungsbildung; BVerfG hält die Hürde auf Bundesebene für verfassungsgemäß (anders als bei Europawahlen); Grundmandatsklausel als Ausnahme; strategisches Wählen ist auch Ausdruck von Wahlfreiheit.",
                    "Stützende Aspekte: hoher Anteil 2025 im historischen Vergleich; knapp gescheiterte Parteien; Erfolgswertgleichheit eingeschränkt.",
                    "Begründetes Ergebnis: Aussage quantitativ weitgehend zutreffend, aber sprachlich zugespitzt und normativ einseitig.",
                ],
                 "hinweis": "Überprüfen: Aussage auf Grundlage von Fachkenntnissen kritisch hinterfragen und auf Angemessenheit hin begründet einschätzen; sowohl Rechnung als auch Wertung sind gefragt."},
            ],
            "bewertung": {
                "ausreichend": ["die Tabelle ansatzweise formal und inhaltlich korrekt beschrieben wird,",
                                "das Verhältnis von Stimmen- und Sitzanteilen ansatzweise ausgewertet wird,",
                                "Position und Intention des Autors ansatzweise mit Belegen analysiert werden,",
                                "die Aussage ansatzweise rechnerisch und inhaltlich überprüft und begründet eingeschätzt wird."],
                "gut": ["die Tabelle vollständig, strukturiert und fachsprachlich korrekt beschrieben wird,",
                        "die Auswertung zu einer schlüssigen Gesamtaussage gelangt und mit Fachwissen zum Wahlsystem verknüpft wird,",
                        "Position, Argumentationsstruktur (inkl. Einwandvorwegnahme) und Intention differenziert und belegt analysiert werden,",
                        "die Aussage differenziert, rechnerisch nachvollziehbar und mit Fachwissen überprüft und schlüssig eingeschätzt wird."],
            },
        },
    ],
}
