# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q3.5 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q3.5, insbesondere internationale Umweltpolitik im Spannungsfeld von Kooperation und Verteilungskonflikten (Kollektivgutproblem, Klimarahmenkonvention, Kyoto-Protokoll, Pariser Abkommen, Klimakonferenzen) sowie Ziele, Interessen und Strategien staatlicher und privater Akteure; Bezug zu Q4.3 (Europas Beitrag zu einer globalen Klimapolitik)."

_WELLE = "M0 352 " + " ".join("Q%d %d %d 352" % (x + 20, 344 if (x // 40) % 2 == 0 else 360, x + 40) for x in range(0, 760, 40)) + " L760 460 L0 460 Z"

SVG_KARIKATUR = """<svg viewBox='0 0 760 460' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='kkk'>
<title id='kkk'>Karikatur Einstimmig beschlossen: Delegierte an einem Konferenztisch über steigendem Wasser, ein Ölstaat hält ein Veto-Schild hoch, ein Inselstaat steht auf einer fast überfluteten Insel.</title>
<rect x='0' y='0' width='760' height='460' fill='#fffdf6'/>
<rect x='170' y='10' width='420' height='58' rx='8' fill='#14213d'/>
<text x='380' y='34' text-anchor='middle' font-size='17' font-weight='bold' fill='#ffffff'>WELTKLIMAKONFERENZ</text>
<text x='380' y='56' text-anchor='middle' font-size='13' fill='#dfe6f7'>Beschlüsse nur im Konsens</text>
<rect x='12' y='80' width='322' height='62' rx='14' fill='#ffffff' stroke='#333' stroke-width='1.5'/>
<polygon points='86,141 110,141 100,190' fill='#ffffff' stroke='#333' stroke-width='1.5'/>
<rect x='88' y='138' width='20' height='5' fill='#ffffff'/>
<text x='173' y='105' text-anchor='middle' font-size='14' font-weight='bold' fill='#14213d'>Einstimmig beschlossen:</text>
<text x='173' y='128' text-anchor='middle' font-size='14' fill='#14213d'>Wir verhandeln nächstes Jahr weiter!</text>
<rect x='500' y='80' width='250' height='62' rx='14' fill='#ffffff' stroke='#333' stroke-width='1.5'/>
<polygon points='600,141 622,141 628,250' fill='#ffffff' stroke='#333' stroke-width='1.5'/>
<rect x='602' y='138' width='18' height='5' fill='#ffffff'/>
<text x='625' y='105' text-anchor='middle' font-size='14' font-weight='bold' fill='#b5302a'>Wir können nicht</text>
<text x='625' y='128' text-anchor='middle' font-size='14' font-weight='bold' fill='#b5302a'>bis nächstes Jahr warten!</text>
<rect x='258' y='152' width='176' height='42' rx='12' fill='#ffffff' stroke='#333' stroke-width='1.2'/>
<polygon points='328,193 344,193 336,204' fill='#ffffff' stroke='#333' stroke-width='1.2'/>
<rect x='330' y='190' width='12' height='4' fill='#ffffff'/>
<text x='346' y='169' text-anchor='middle' font-size='13' fill='#333'>Erst zahlt ihr –</text>
<text x='346' y='187' text-anchor='middle' font-size='13' fill='#333'>ihr habt angefangen!</text>
<rect x='165' y='310' width='12' height='70' fill='#6b4423'/>
<rect x='493' y='310' width='12' height='70' fill='#6b4423'/>
<rect x='60' y='292' width='82' height='90' fill='#c9b38a' stroke='#6b4423'/>
<text x='101' y='318' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>VORSITZ</text>
<rect x='79' y='232' width='44' height='60' rx='6' fill='#555555'/>
<circle cx='101' cy='214' r='18' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<circle cx='95' cy='211' r='2.2' fill='#333'/><circle cx='107' cy='211' r='2.2' fill='#333'/>
<path d='M93 221 Q101 227 109 221' fill='none' stroke='#333' stroke-width='1.6'/>
<path d='M123 246 L146 230' stroke='#555555' stroke-width='7' stroke-linecap='round'/>
<rect x='140' y='220' width='22' height='10' rx='2' fill='#6b4423'/>
<rect x='191' y='239' width='48' height='26' rx='6' fill='#22355e'/>
<circle cx='215' cy='222' r='17' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<circle cx='209' cy='219' r='2.2' fill='#333'/><circle cx='221' cy='219' r='2.2' fill='#333'/>
<path d='M207 228 Q215 233 223 228' fill='none' stroke='#333' stroke-width='1.6'/>
<rect x='311' y='239' width='48' height='26' rx='6' fill='#4a7c59'/>
<circle cx='335' cy='222' r='17' fill='#e0b48a' stroke='#333' stroke-width='1.5'/>
<circle cx='329' cy='219' r='2.2' fill='#333'/><circle cx='341' cy='219' r='2.2' fill='#333'/>
<path d='M328 230 L342 230' stroke='#333' stroke-width='1.6'/>
<rect x='431' y='239' width='48' height='26' rx='6' fill='#7a4b2a'/>
<circle cx='455' cy='222' r='17' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<circle cx='449' cy='219' r='2.2' fill='#333'/><circle cx='461' cy='219' r='2.2' fill='#333'/>
<path d='M445 227 Q455 236 465 227' fill='none' stroke='#333' stroke-width='1.6'/>
<path d='M474 250 L494 188' stroke='#555555' stroke-width='4'/>
<rect x='452' y='150' width='88' height='38' rx='4' fill='#b5302a'/>
<text x='496' y='176' text-anchor='middle' font-size='18' font-weight='bold' fill='#ffffff'>VETO</text>
<rect x='150' y='262' width='370' height='14' fill='#8b5a2b'/>
<rect x='150' y='276' width='370' height='40' fill='#a86b3c'/>
<rect x='488' y='238' width='24' height='26' rx='3' fill='#333333'/>
<rect x='488' y='245' width='24' height='3' fill='#888888'/>
<rect x='488' y='255' width='24' height='3' fill='#888888'/>
<rect x='160' y='284' width='110' height='24' rx='3' fill='#ffffff'/>
<text x='215' y='301' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>Industriestaaten</text>
<rect x='280' y='284' width='110' height='24' rx='3' fill='#ffffff'/>
<text x='335' y='301' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>Schwellenländer</text>
<rect x='400' y='284' width='110' height='24' rx='3' fill='#ffffff'/>
<text x='455' y='301' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>Ölstaaten</text>
<rect x='541' y='300' width='8' height='120' fill='#ffffff' stroke='#333'/>
<rect x='541' y='310' width='8' height='10' fill='#b5302a'/>
<rect x='541' y='330' width='8' height='10' fill='#b5302a'/>
<rect x='541' y='350' width='8' height='10' fill='#b5302a'/>
<text x='545' y='294' text-anchor='middle' font-size='12' fill='#333'>Pegel</text>
<path d='WELLE' fill='#9fc5e8'/>
<ellipse cx='650' cy='356' rx='72' ry='12' fill='#e8d9a8'/>
<path d='M716 356 Q722 318 712 292' fill='none' stroke='#7a5230' stroke-width='6'/>
<path d='M712 292 Q690 278 676 292' fill='none' stroke='#3f7f3f' stroke-width='5'/>
<path d='M712 292 Q734 278 748 292' fill='none' stroke='#3f7f3f' stroke-width='5'/>
<path d='M712 292 Q700 270 688 272' fill='none' stroke='#3f7f3f' stroke-width='5'/>
<path d='M712 292 Q726 270 740 272' fill='none' stroke='#3f7f3f' stroke-width='5'/>
<rect x='620' y='334' width='8' height='22' fill='#2c3e50'/>
<rect x='634' y='334' width='8' height='22' fill='#2c3e50'/>
<rect x='618' y='288' width='26' height='48' rx='6' fill='#2c7a7b'/>
<circle cx='631' cy='271' r='16' fill='#c68e5e' stroke='#333' stroke-width='1.5'/>
<circle cx='625' cy='268' r='2.2' fill='#333'/><circle cx='637' cy='268' r='2.2' fill='#333'/>
<path d='M624 280 Q631 275 638 280' fill='none' stroke='#333' stroke-width='1.6'/>
<path d='M644 300 L684 238' stroke='#555555' stroke-width='4'/>
<rect x='656' y='198' width='90' height='40' rx='4' fill='#ffffff' stroke='#b5302a' stroke-width='3'/>
<text x='701' y='225' text-anchor='middle' font-size='17' font-weight='bold' fill='#b5302a'>1,5 °C!</text>
<rect x='560' y='348' width='200' height='16' fill='#9fc5e8' fill-opacity='0.85'/>
<rect x='576' y='384' width='110' height='24' rx='3' fill='#ffffff' stroke='#14213d'/>
<text x='631' y='401' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>Inselstaaten</text>
</svg>""".replace("WELLE", _WELLE)

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Schluss mit dem Konsens-Theater?“ (2026)",
        "absaetze": [
            "Jedes Jahr im November dasselbe Bild: Zehntausende Delegierte, Lobbyisten und Aktivistinnen reisen zur Weltklimakonferenz, verhandeln zwei Wochen lang bis tief in die Nacht – und am Ende steht ein Beschluss, den alle mittragen können, weil er niemandem wehtut. Im November 2025 in Belém war es wieder so. Mehr als 80 Staaten wollten einen Fahrplan für die Abkehr von Kohle, Öl und Gas. Im Abschlusstext steht davon nichts.",
            "Das liegt an einer Besonderheit der Klimadiplomatie: Seit Jahrzehnten können sich die Vertragsstaaten nicht auf Abstimmungsregeln einigen. Deshalb gilt faktisch das Konsensprinzip. Jeder einzelne Staat kann Formulierungen blockieren, die seinen Interessen widersprechen. Wer vom Verkauf fossiler Rohstoffe lebt, hat einen starken Anreiz, genau das zu tun.",
            "Hinzu kommt das alte Problem des Trittbrettfahrens. Klimaschutz kostet heute Geld, der Nutzen verteilt sich auf alle Staaten und zeigt sich oft erst in Jahrzehnten. Das Pariser Abkommen hat versucht, dieses Problem mit Freiwilligkeit und Transparenz zu lösen: Jeder Staat legt seine eigenen Ziele fest. Doch die Summe dieser Ziele reicht nicht. Nach Berechnungen des UN-Umweltprogramms führen selbst vollständig umgesetzte Zusagen zu einer Erwärmung von 2,3 bis 2,5 Grad. Und wer gar nicht mitmachen will, tritt einfach aus – wie die USA, die das Pariser Abkommen im Januar 2026 verlassen haben.",
            "Trotzdem wäre es falsch, die Klimakonferenzen für nutzlos zu erklären. Ohne sie gäbe es kein 1,5-Grad-Ziel, keine regelmäßige Überprüfung der nationalen Ziele, keinen Fonds für Verluste und Schäden und kein Forum, in dem Tuvalu dieselbe Stimme hat wie China. Vor dem Pariser Abkommen rechneten Fachleute mit einer weit stärkeren Erwärmung als heute, und erneuerbare Energien sind in vielen Ländern inzwischen die günstigste Stromquelle.",
            "Ich schlage deshalb einen doppelten Weg vor. Erstens sollten die Vertragsstaaten endlich Mehrheitsentscheidungen ermöglichen – etwa mit einer Dreiviertelmehrheit, die kleinen wie großen Staaten Gewicht gibt. Zweitens sollten die EU und andere ehrgeizige Staaten einen Klimaclub bilden: mit einem gemeinsamen CO2-Mindestpreis, Grenzausgleichsabgaben auf Importe aus Ländern ohne vergleichbaren Klimaschutz und großzügiger finanzieller Hilfe für ärmere Mitglieder.",
            "Die Einwände liegen auf der Hand: Mehrheitsentscheidungen könnten große Emittenten aus dem Prozess treiben, ein Klimaclub könnte als Handelsprotektionismus wahrgenommen werden. Doch die Alternative ist, weiter auf den Langsamsten zu warten. Das kann sich angesichts steigender Meeresspiegel niemand leisten – am wenigsten diejenigen, die am wenigsten zum Problem beigetragen haben.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Politikwissenschaftlers (2026). Die genannten Fakten beruhen auf dem Emissions Gap Report 2025 des UN-Umweltprogramms (UNEP) und auf Berichten über die COP30 in Belém (November 2025).",
    },
    {
        "id": "m2",
        "titel": "M2: CO2-Emissionen ausgewählter Staaten und Staatengruppen (2024)",
        "typ": "tabelle",
        "kopf": ["Staat / Staatengruppe", "CO2-Emissionen 2024 (Mio. t)", "Anteil an den weltweiten Emissionen 2024 (%)", "Emissionen pro Kopf 2024 (t)", "Anteil an den kumulierten Emissionen 1750–2024 (%)"],
        "zeilen": [
            ["China", "12.289", "31,8", "8,7", "15,4"],
            ["USA", "4.904", "12,7", "14,2", "23,5"],
            ["Indien", "3.193", "8,3", "2,2", "3,6"],
            ["EU (27 Staaten)", "2.426", "6,3", "5,4", "16,3"],
            ["darunter Deutschland", "572", "1,5", "6,8", "5,1"],
            ["Russland", "1.781", "4,6", "12,3", "6,6"],
            ["Japan", "962", "2,5", "7,8", "3,8"],
            ["Saudi-Arabien", "692", "1,8", "20,4", "1,0"],
            ["Nigeria", "136", "0,4", "0,6", "0,3"],
            ["Bangladesch", "108", "0,3", "0,6", "0,1"],
            ["Afrika (gesamt)", "1.502", "3,9", "1,0", "2,9"],
            ["Staaten mit hohem Einkommen", "13.868", "35,9", "9,8", "62,3"],
            ["Staaten mit niedrigem Einkommen", "211", "0,5", "0,3", "0,6"],
            ["Welt", "38.599", "100", "4,7", "100"],
        ],
        "quelle": "Global Carbon Project, Global Carbon Budget 2025 (fossile CO2-Emissionen einschließlich Zement, ohne Landnutzungsänderungen), aufbereitet von Our World in Data (CO2-Datensatz, abgerufen am 2.11.2026); Werte gerundet. Einkommensgruppen nach Klassifikation der Weltbank. Der Weltwert schließt den internationalen Flug- und Schiffsverkehr ein.",
    },
    {
        "id": "m3",
        "typ": "bild",
        "titel": "M3: Karikatur „Einstimmig beschlossen“ (2026)",
        "svg": SVG_KARIKATUR,
        "beschreibung": "Die Karikatur zeigt oben ein dunkelblaues Banner mit der Aufschrift 'WELTKLIMAKONFERENZ' und darunter 'Beschlüsse nur im Konsens'. In der Bildmitte steht ein langer, brauner Konferenztisch auf Stelzen; darunter steigt von unten hellblaues, welliges Wasser auf, die Tischbeine stehen bereits im Wasser. Hinter dem Tisch sitzen drei Delegierte mit Namensschildern: 'Industriestaaten' (zufrieden lächelnd), 'Schwellenländer' (mit ernstem Gesicht) und 'Ölstaaten'. Der Delegierte der Ölstaaten grinst und hält ein großes rotes Schild mit der Aufschrift 'VETO' hoch; neben ihm steht ein schwarzes Ölfass auf dem Tisch. Über dem Delegierten der Schwellenländer steht die Sprechblase 'Erst zahlt ihr – ihr habt angefangen!'. Links steht die Konferenzleitung auf einem Podest mit der Aufschrift 'VORSITZ', hält einen Hammer und verkündet in einer Sprechblase: 'Einstimmig beschlossen: Wir verhandeln nächstes Jahr weiter!'. Rechts steht eine kleine Figur auf einer winzigen, fast überfluteten Sandinsel mit einer Palme; das Wasser reicht ihr bis an die Knöchel, im Wasser schwimmt ein Schild 'Inselstaaten'. Sie hält ein Schild '1,5 °C!' hoch und ruft in einer Sprechblase: 'Wir können nicht bis nächstes Jahr warten!'. Zwischen Tisch und Insel ragt ein rot-weiß markierter Pegel mit der Beschriftung 'Pegel' aus dem Wasser.",
        "quelle": "Übungsmaterial: eigene Zeichnung für Feibitur (2026).",
    },
]

AUFGABEN = [
    {
        "id": "q3-5-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Kommentar), Titel, Erscheinungsjahr (2026), Thema (Leistungsfähigkeit der Weltklimakonferenzen und Reformvorschläge) und Hinweis auf einen (fiktiven) Politikwissenschaftler als Autor.",
            "punkte": [
                "Der Autor kritisiert, dass Klimakonferenzen trotz großen Aufwands nur Beschlüsse hervorbrächten, die niemandem wehtun; Beispiel Belém 2025: Fahrplan zur Abkehr von fossilen Energien trotz Unterstützung von über 80 Staaten nicht im Abschlusstext [1].",
                "Ursache sei das faktische Konsensprinzip, das jedem Staat – insbesondere Förderstaaten fossiler Rohstoffe – eine Blockade ermögliche [2].",
                "Hinzu komme das Trittbrettfahrerproblem; die freiwilligen Ziele des Pariser Abkommens reichten nicht (2,3–2,5 °C laut UNEP), und Staaten könnten austreten wie die USA im Januar 2026 [3].",
                "Zugleich würdigt er Erfolge: 1,5-Grad-Ziel, Überprüfungsmechanismus, Fonds für Verluste und Schäden, gleiche Stimme kleiner Staaten, geringere Erwärmungsprognosen als vor Paris, günstige erneuerbare Energien [4].",
                "Er schlägt Mehrheitsentscheidungen (z. B. Dreiviertelmehrheit) und einen Klimaclub der EU mit anderen ehrgeizigen Staaten vor (CO2-Mindestpreis, Grenzausgleich, Hilfe für ärmere Mitglieder) [5].",
                "Einwände (Austritt großer Emittenten, Protektionismus) hält er für weniger gewichtig als die Kosten weiteren Abwartens, besonders für die Hauptbetroffenen [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache, keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen des Kommentars weitgehend vollständig, strukturiert, komprimiert und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q3-5-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die in M2 dargestellten Daten zu den CO2-Emissionen.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle nach Daten des Global Carbon Project (Global Carbon Budget 2025) zu den fossilen CO2-Emissionen ausgewählter Staaten und Staatengruppen im Jahr 2024 – absolut, als Anteil, pro Kopf und kumuliert seit 1750.",
            "punkte": [
                "Weltweit wurden 2024 rund 38,6 Mrd. t CO2 ausgestoßen, durchschnittlich 4,7 t pro Kopf.",
                "Größter Emittent ist China mit rund 12,3 Mrd. t (31,8 %), gefolgt von den USA (12,7 %), Indien (8,3 %), der EU (6,3 %) und Russland (4,6 %).",
                "Pro Kopf liegen Saudi-Arabien (20,4 t), die USA (14,2 t) und Russland (12,3 t) weit vorn; China (8,7 t) liegt über, Indien (2,2 t), Afrika (1,0 t), Nigeria und Bangladesch (je 0,6 t) weit unter dem Weltdurchschnitt; die EU liegt mit 5,4 t leicht darüber.",
                "Bei den kumulierten Emissionen seit 1750 führen die USA (23,5 %) vor der EU (16,3 %) und China (15,4 %); Deutschland allein hat 5,1 % verursacht, Afrika insgesamt nur 2,9 %.",
                "Staaten mit hohem Einkommen verursachten 2024 rund 36 % der Emissionen und 62,3 % der kumulierten Emissionen; Staaten mit niedrigem Einkommen nur 0,5 % bzw. 0,6 % bei 0,3 t pro Kopf.",
            ],
            "hinweis": "Beschreiben: Daten strukturiert und fachsprachlich darlegen (Thema, Quelle, Kategorien, zentrale Werte, Auffälligkeiten); noch keine Erklärung oder Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die zentralen Werte der Tabelle im Ansatz korrekt und strukturiert beschrieben werden.",
            "gut": "die Daten vollständig, strukturiert und fachsprachlich präzise beschrieben werden, wobei die Unterschiede zwischen absoluten, Pro-Kopf- und kumulierten Werten herausgestellt werden.",
        },
    },
    {
        "id": "q3-5-i3",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Karikatur (M3).",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Formale Angaben: Karikatur „Einstimmig beschlossen“, eigene Zeichnung, 2026.",
                "Oben ein Banner „WELTKLIMAKONFERENZ – Beschlüsse nur im Konsens“; in der Mitte ein Konferenztisch auf Stelzen über steigendem Wasser.",
                "Hinter dem Tisch drei Delegierte mit Namensschildern „Industriestaaten“, „Schwellenländer“ und „Ölstaaten“; der Ölstaaten-Delegierte grinst, hält ein rotes Schild „VETO“ hoch, neben ihm ein Ölfass; Sprechblase der Schwellenländer: „Erst zahlt ihr – ihr habt angefangen!“.",
                "Links die Konferenzleitung auf einem Podest „VORSITZ“ mit Hammer und der Sprechblase „Einstimmig beschlossen: Wir verhandeln nächstes Jahr weiter!“.",
                "Rechts eine kleine Figur („Inselstaaten“) auf einer fast überfluteten Sandinsel mit Palme, Wasser bis an die Knöchel, Schild „1,5 °C!“, Sprechblase „Wir können nicht bis nächstes Jahr warten!“; dazwischen ein Pegel im Wasser.",
                "Strukturierte Beschreibung des Bildaufbaus (oben – Mitte – links – rechts).",
            ],
            "hinweis": "Beschreiben: nur das Sichtbare strukturiert und präzise darlegen; noch keine Deutung (z. B. „Konsensprinzip blockiert“ gehört in die Analyse).",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Bildelemente im Ansatz korrekt beschrieben werden.",
            "gut": "die Karikatur vollständig, strukturiert (Bildaufbau) und präzise beschrieben wird, ohne vorzeitig zu deuten.",
        },
    },
    {
        "id": "q3-5-ii1",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie ausgehend von M1, warum internationale Klimapolitik als Kollektivgutproblem gilt und weshalb Kooperation zwischen Staaten so schwierig ist.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klima als globales Kollektivgut: Nicht-Ausschließbarkeit vom Nutzen eines stabilen Klimas; Atmosphäre als übernutzte Allmende (Tragik der Allmende, Hardin).",
                "Asymmetrie von Kosten und Nutzen: Kosten der Minderung national und sofort, Nutzen global und zeitverzögert [3].",
                "Trittbrettfahrerproblem/Gefangenendilemma: Für jeden Staat ist Nichthandeln individuell rational, kollektiv führt es zum schlechtesten Ergebnis; Freiwilligkeit des Pariser Abkommens reicht deshalb nicht (2,3–2,5 °C) [3].",
                "Institutionelle Verstärker: Konsensprinzip erlaubt Blockaden durch Staaten mit fossilen Interessen [1], [2]; keine Sanktionen, Austrittsmöglichkeit (USA 2026) [3].",
                "Verteilungskonflikte: unterschiedliche Verantwortung und Betroffenheit (Industrie-, Schwellen-, Inselstaaten), Streit um Finanzierung und Lastenteilung.",
                "Bedingungen für Kooperation: Transparenz, Vertrauen durch wiederholte Verhandlungen, Anreize/Sanktionen (Klimaclub), Beispiel Montreal-Protokoll [4], [5].",
            ],
            "hinweis": "Erklären: Rückführung auf ökonomische und politikwissenschaftliche Modelle (Kollektivgut, Gefangenendilemma, Allmende); Materialbezug erforderlich.",
        },
        "bewertung": {
            "ausreichend": "das Kollektivgutproblem und die Schwierigkeit der Kooperation im Ansatz zutreffend erklärt und auf das Material bezogen werden.",
            "gut": "das Kollektivgutproblem modellgestützt, fachsprachlich präzise und differenziert erklärt und durchgängig mit Belegen aus M1 verknüpft wird.",
        },
    },
    {
        "id": "q3-5-ii2",
        "afb": "II",
        "operator": "auswerten",
        "text": "Werten Sie M2 im Hinblick auf Verteilungskonflikte in der internationalen Klimapolitik aus.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Heutige Emissionen: China ist mit Abstand größter Emittent; ohne Schwellenländer (China, Indien) ist das Klimaziel nicht erreichbar – Argument der Industriestaaten für Pflichten aller.",
                "Historische Verantwortung: USA und EU verursachten zusammen fast 40 % der kumulierten Emissionen, Staaten mit hohem Einkommen über 60 %; Afrika nur 2,9 % – Grundlage für das Verursacherprinzip und die Forderung nach Klimafinanzierung und Ausgleich für Verluste und Schäden.",
                "Pro-Kopf-Perspektive: Indien, Nigeria, Bangladesch weit unter dem Weltdurchschnitt; Saudi-Arabien, USA, Russland weit darüber – Gleichheitsprinzip und Recht auf Entwicklung als Argumente der Schwellen- und Entwicklungsländer.",
                "Sonderfälle: China mit hohen absoluten und inzwischen über dem EU-Wert liegenden Pro-Kopf-Emissionen, aber Status als Entwicklungsland; reiche Ölstaaten mit sehr hohen Pro-Kopf-Werten – Streit über die Einteilung der Konvention von 1992.",
                "Staaten mit niedrigem Einkommen (0,5 % der Emissionen) sind kaum verantwortlich, aber oft besonders betroffen – Kern der Forderung nach Klimagerechtigkeit.",
                "Gesamtaussage: Je nach Maßstab (absolut, pro Kopf, historisch, Leistungsfähigkeit) ergibt sich eine andere „gerechte“ Lastenverteilung; dies erklärt die Konfliktlinien auf Klimakonferenzen und das Prinzip gemeinsamer, aber unterschiedlicher Verantwortlichkeiten.",
            ],
            "hinweis": "Auswerten: Einzeldaten unter der Leitfrage zu einer Gesamtaussage zusammenführen; Bezug auf Gerechtigkeitsmaßstäbe und Akteursgruppen erwartet; bloßes Wiederholen der Zahlen genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "die Daten ansatzweise im Hinblick auf Verteilungskonflikte ausgewertet werden und eine nachvollziehbare Gesamtaussage vorliegt.",
            "gut": "die Daten differenziert nach absoluten, Pro-Kopf- und kumulierten Werten ausgewertet, den Positionen der Staatengruppen zugeordnet und zu einer schlüssigen Gesamtaussage zusammengeführt werden.",
        },
    },
    {
        "id": "q3-5-ii3",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Karikatur (M3) im Hinblick auf ihre Aussage über die internationale Klimapolitik.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Banner und Vorsitz: Kritik am Konsensprinzip der COP – „einstimmige“ Beschlüsse bestehen im Vertagen; Ergebnis als kleinster gemeinsamer Nenner.",
                "Ölstaaten mit Veto-Schild und Ölfass: Förderstaaten fossiler Rohstoffe nutzen die Blockademöglichkeit zum Schutz ihrer Einnahmen (Bezug: fehlender Fossil-Fahrplan in Belém 2025).",
                "Schwellenländer („Erst zahlt ihr – ihr habt angefangen!“): Verweis auf historische Verantwortung und Finanzierungsforderungen; zugleich Andeutung gegenseitiger Schuldzuweisungen (Trittbrettfahrerlogik).",
                "Industriestaaten zufrieden, trocken am Tisch: geringe Betroffenheit und mangelnder Handlungsdruck der Verursacher.",
                "Inselstaat auf überfluteter Insel mit „1,5 °C!“ und Pegel: existenzielle Bedrohung der Hauptbetroffenen, Zeitdruck, Klimagerechtigkeit; steigendes Wasser auch unter dem Tisch als Hinweis, dass die Folgen am Ende alle treffen.",
                "Kernaussage: Die internationale Klimapolitik scheitert an Interessengegensätzen und am Konsensprinzip, während die Zeit für die Verwundbarsten abläuft; Fachbegriffe: Konsensprinzip, Kollektivgut, Trittbrettfahrer, Klimagerechtigkeit, AOSIS.",
            ],
            "hinweis": "Analysieren: Bildelemente systematisch deuten und auf Fachkonzepte beziehen; Kernaussage präzise formulieren; Bildbelege angeben.",
        },
        "bewertung": {
            "ausreichend": "zentrale Bildelemente ansatzweise zutreffend gedeutet werden und eine Kernaussage formuliert wird.",
            "gut": "die Bildelemente systematisch und mit Fachbegriffen gedeutet, auf Akteursinteressen und das Konsensprinzip bezogen werden und eine präzise Kernaussage formuliert wird.",
        },
    },
    {
        "id": "q3-5-ii4",
        "afb": "II",
        "operator": "vergleichen",
        "text": "Vergleichen Sie das Kyoto-Protokoll und das Pariser Klimaabkommen hinsichtlich ihrer Ziele, der Verpflichtungen der Staaten und ihrer Wirksamkeit.",
        "material": [],
        "loesung": {
            "punkte": [
                "Vergleichskriterien benennen (z. B. Ziel, Ansatz, Verpflichtete, Verbindlichkeit, Überprüfung/Sanktionen, Beteiligung, Wirksamkeit).",
                "Gemeinsamkeiten: beide unter dem Dach der Klimarahmenkonvention, Ziel der Emissionsminderung, Prinzip gemeinsamer, aber unterschiedlicher Verantwortlichkeiten, Berichtspflichten, Marktmechanismen (Kyoto: Emissionshandel/CDM; Paris: Art. 6).",
                "Kyoto (1997, in Kraft 2005): Top-down, verbindliche Reduktionsziele nur für Industriestaaten (insgesamt rund 5 % unter 1990 in 2008–2012), keine Pflichten für China oder Indien, USA nicht beigetreten, Kanada ausgetreten – geringe Abdeckung der Weltemissionen.",
                "Paris (2015, in Kraft 2016): Bottom-up, alle Staaten legen NDCs vor, Temperaturziel deutlich unter 2 °C/1,5 °C, Fortschreibung alle fünf Jahre, globale Bestandsaufnahme, keine verbindlichen Zielhöhen und keine Sanktionen; nahezu universelle Beteiligung, aber Austritt der USA 2026.",
                "Wirksamkeit: Paris erreicht breite Beteiligung und hat Erwärmungsprognosen gesenkt, die NDCs reichen aber nicht (UNEP: 2,3–2,5 °C); Kyoto war verbindlicher, aber zu eng; Fazit des Vergleichs (Zielkonflikt Verbindlichkeit vs. Beteiligung).",
            ],
            "hinweis": "Vergleichen: kriteriengeleitet Gemeinsamkeiten und Unterschiede begründet darlegen; ein bloßes Nacheinander beider Abkommen ohne Gegenüberstellung genügt nicht für „gut“.",
        },
        "bewertung": {
            "ausreichend": "die beiden Abkommen ansatzweise kriteriengeleitet verglichen werden.",
            "gut": "der Vergleich kriteriengeleitet, fachlich präzise und mit Gemeinsamkeiten und Unterschieden erfolgt und in ein begründetes Fazit mündet.",
        },
    },
    {
        "id": "q3-5-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie die Vorschläge des Autors, auf Weltklimakonferenzen Mehrheitsentscheidungen einzuführen und einen Klimaclub zu bilden. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Kriterien klären, z. B. Effektivität (Emissionsminderung), Legitimität und Beteiligung, Gerechtigkeit gegenüber ärmeren Staaten, Vereinbarkeit mit Handelsregeln, politische Durchsetzbarkeit.",
                "Pro Mehrheitsentscheidungen: Ende der Blockade durch Einzelstaaten [2]; schnellere, ambitioniertere Beschlüsse; demokratischere Logik; Belém-Beispiel [1].",
                "Contra Mehrheitsentscheidungen: Einführung selbst bräuchte Konsens; große Emittenten könnten überstimmt werden und austreten (USA als Beispiel) [6]; Beschlüsse bleiben ohne Sanktionen; Souveränität; Gefahr, dass kleine Staaten ihr faktisches Vetorecht verlieren [4].",
                "Pro Klimaclub: löst Trittbrettfahrerproblem durch Anreize/Sanktionen (Nordhaus); schützt vor Carbon Leakage; EU hat mit CBAM bereits ein Instrument; Hilfe für ärmere Mitglieder fördert Beitritt [5].",
                "Contra Klimaclub: Handelskonflikte und Protektionismusvorwurf (WTO-Konformität), Spaltung der Staatenwelt, Belastung ärmerer Exportländer, Gegenmaßnahmen großer Handelspartner; ohne große Emittenten begrenzte Wirkung.",
                "Abwägung und begründetes Urteil (z. B. Klimaclub als Ergänzung zum UN-Prozess sinnvoll, Mehrheitsprinzip politisch kaum durchsetzbar).",
            ],
            "hinweis": "Erörtern: beide Vorschläge unter Abwägen von Pro- und Kontraargumenten hinterfragen und zu einem eigenen Urteil gelangen; Bezug zu [5] und [6] sowie Fachwissen zu Konsensprinzip und Kollektivgutproblem erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist, Pro- und Kontraargumente zu beiden Vorschlägen enthält und in ein ansatzweise nachvollziehbares Urteil mündet.",
            "gut": "die Erörterung strukturiert, kriteriengeleitet und fachlich fundiert ist und in ein weitgehend klares und schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q3-5-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie, inwieweit die Karikatur (M3) die Ergebnisse der jüngsten Weltklimakonferenzen zutreffend darstellt.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Kriterien benennen (z. B. Übereinstimmung mit den tatsächlichen Konferenzergebnissen, Vollständigkeit der Akteursdarstellung, Angemessenheit der Zuspitzung).",
                "Zutreffend: Konsensprinzip begünstigt Blockaden; in Belém 2025 kein Fahrplan zum Ausstieg aus fossilen Energien im Beschlusstext; Finanzstreit (Baku 2024: 300 Mrd. US-Dollar, viele Entwicklungsländer unzufrieden); NDCs reichen nicht (UNEP: 2,3–2,5 °C); Inselstaaten existenziell bedroht.",
                "Überzeichnet/einseitig: Konferenzen brachten auch Fortschritte – Fonds für Verluste und Schäden (2022/2023), Aufruf zur Abkehr von fossilen Brennstoffen (Dubai 2023), neues Finanzziel (Baku), Verdreifachung der Anpassungsfinanzierung (Belém), Tropenwaldfonds; Industriestaaten wie die EU treiben Klimaschutz voran, während die USA ausgetreten sind – „die Industriestaaten“ sind keine einheitliche Gruppe; Schwellenländer wie China investieren massiv in erneuerbare Energien.",
                "Einordnung: Zuspitzung ist Stilmittel der Karikatur; Kernkritik an Tempo und Verfahren bleibt berechtigt.",
                "Begründetes Urteil (z. B. im Kern zutreffend, in der Pauschalität überzeichnet).",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete Einschätzung auf Basis von Fachwissen zu konkreten Konferenzergebnissen; Bezug auf Bildelemente erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Darstellung der Karikatur ansatzweise kriteriengeleitet und mit einzelnen zutreffenden Konferenzergebnissen beurteilt wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend und mit präzisem Fachwissen zu mehreren Klimakonferenzen begründet wird und die Zuspitzung der Karikatur reflektiert.",
        },
    },
    {
        "id": "q3-5-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Entwerfen Sie eine Rede, die eine Vertreterin der Allianz der kleinen Inselstaaten (AOSIS) auf der Weltklimakonferenz hält und in der sie ihre Forderungen an Industrie- und Schwellenländer begründet. Nutzen Sie dazu M2.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Produktorientierte Aufgabe: Erwartet wird eine adressatengerechte Rede (Anrede, Einstieg, Argumentation, Appell, Schluss) aus der Perspektive der AOSIS.",
            "punkte": [
                "Situationsbezug und Betroffenheit: Meeresspiegelanstieg, Stürme, Versalzung, Existenzbedrohung kleiner Inselstaaten; Verweis auf das 1,5-Grad-Ziel des Pariser Abkommens.",
                "Datengestützte Begründung mit M2: historische Verantwortung (USA und EU fast 40 % der kumulierten Emissionen, Staaten mit hohem Einkommen über 60 %), hohe Pro-Kopf-Emissionen (USA, Saudi-Arabien, Russland), heutige Hauptemittenten (China über 30 %); eigener Beitrag der Inselstaaten verschwindend gering.",
                "Forderungen an Industriestaaten: schnellere Emissionsminderung, Erfüllung und Ausbau der Klimafinanzierung (300-Mrd.-Ziel, Verdreifachung der Anpassungsfinanzierung), Einzahlung in den Fonds für Verluste und Schäden.",
                "Forderungen an Schwellenländer und Ölstaaten: ehrgeizigere NDCs, Abkehr von fossilen Energien, Beitrag zur Finanzierung nach Leistungsfähigkeit; Kritik an Blockaden im Konsensverfahren.",
                "Rhetorische Mittel: Appelle, Bilder, Bezug zu Gerechtigkeit (Verursacher-, Leistungsfähigkeitsprinzip), ggf. Bezug zum IGH-Gutachten 2025.",
                "Fachliche Richtigkeit und schlüssige Argumentation; Perspektive konsequent eingehalten.",
            ],
            "hinweis": "Gestalten/entwerfen: kreative, produktorientierte Umsetzung; bewertet werden Adressaten- und Situationsbezug, fachliche Fundierung (Daten aus M2, Kenntnisse zu Verhandlungen und Finanzierung) und Überzeugungskraft der Argumentation.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise adressatengerechte Rede vorliegt, die Forderungen der AOSIS nennt und mit einzelnen Daten aus M2 begründet.",
            "gut": "die Rede adressaten- und situationsgerecht gestaltet ist, die Perspektive der AOSIS konsequent einnimmt, ihre Forderungen differenziert an verschiedene Staatengruppen richtet und fachlich fundiert sowie überzeugend mit M2 begründet.",
        },
    },
    {
        "id": "q3-5-iii4",
        "afb": "III",
        "operator": "diskutieren",
        "lk": True,
        "text": "Diskutieren Sie, ob Industriestaaten verpflichtet werden sollten, ärmeren Staaten Ausgleich für klimabedingte Verluste und Schäden zu leisten.",
        "material": [],
        "loesung": {
            "punkte": [
                "Klärung: Loss and Damage als dritte Säule neben Minderung und Anpassung; Art. 8 Pariser Abkommen ohne Haftungsgrundlage (Entscheidung 2015); Fonds seit COP27/COP28 mit knapp 800 Mio. US-Dollar Zusagen (Ende 2025), erste Förderrunde 250 Mio. US-Dollar.",
                "Pro: Verursacherprinzip und historische Verantwortung; Leistungsfähigkeitsprinzip; ärmste Staaten kaum Verursacher, aber stark betroffen; IGH-Gutachten 2025 (Pflicht zur Schadensvermeidung, mögliche Wiedergutmachung); Glaubwürdigkeit und Vertrauen als Voraussetzung für Kooperation im Kollektivgutproblem.",
                "Contra: Schwierigkeit, einzelne Schäden kausal bestimmten Emittenten zuzurechnen; lange Unkenntnis über die Schädlichkeit von CO2; heutige Generationen haften für frühere; Schwellenländer (China) und Ölstaaten tragen heute große Verantwortung, sind aber keine Geber; Gefahr unbegrenzter Haftungsforderungen, die Kooperation gefährden; Vorrang von Minderung und Anpassung.",
                "Zielkonflikte und institutionelle Schwierigkeiten: Konsensprinzip, fehlende Durchsetzung, knappe Finanzmittel, Austritt der USA.",
                "Differenzierte Lösungen: freiwillige Solidarfonds statt Haftung, Beiträge nach Leistungsfähigkeit unter Einbeziehung reicher Schwellenländer, innovative Finanzierungsquellen (z. B. Abgaben auf Luft- und Schiffsverkehr).",
                "Begründete Bewertung am Ende.",
            ],
            "hinweis": "Diskutieren (LK): Argumentation entwickeln, die zu einer begründeten Bewertung führt; Bezug zu Gerechtigkeitsprinzipien, zu Zielkonflikten und institutionellen Schwierigkeiten globaler Umweltpolitik erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Diskussion ansatzweise strukturiert ist, Argumente beider Seiten enthält und in eine ansatzweise nachvollziehbare Bewertung mündet.",
            "gut": "die Diskussion strukturiert, theoriegeleitet (Klimagerechtigkeit, Kollektivgutproblem) und fachlich fundiert ist, institutionelle Schwierigkeiten einbezieht und in eine schlüssig begründete Bewertung mündet.",
        },
    },
]
