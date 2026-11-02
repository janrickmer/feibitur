# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q2.2 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q2.2, insbesondere Bedeutung und Bestimmungsfaktoren des Wirtschaftswachstums, neoklassische Konzeption und Gestaltung von Angebotsbedingungen sowie Ziele, Prinzipien, Probleme und Kontroversen angebotsorientierter Wirtschaftspolitik; im LK zusätzlich EU-Wettbewerbspolitik und Soziale Marktwirtschaft in Abgrenzung zur freien Marktwirtschaft."

KARIKATUR_SVG = """<svg viewBox='0 0 760 440' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='cht'>
<title id='cht'>Karikatur Der Champagnerturm: Aus einer Flasche mit der Aufschrift Steuersenkungen fließt Champagner in das oberste Glas einer Glaspyramide; die unteren Gläser bleiben fast leer. Ein Mann im Anzug verspricht, es laufe nach unten über; zwei Menschen mit leeren Gläsern warten.</title>
<rect x='0' y='0' width='760' height='440' fill='#fffdf6'/>
<text x='20' y='34' font-size='16' font-weight='bold' fill='#14213d'>Der Champagnerturm</text>
<line x1='0' y1='432' x2='760' y2='432' stroke='#bbbbbb' stroke-width='2'/>
<rect x='220' y='395' width='320' height='10' fill='#8a6d3b'/>
<rect x='232' y='405' width='10' height='27' fill='#8a6d3b'/>
<rect x='518' y='405' width='10' height='27' fill='#8a6d3b'/>
<g stroke='#5b6b7f' stroke-width='2'>
<path d='M245 333 Q275 381 305 333 Z' fill='#f4f8fc'/><path d='M315 333 Q345 381 375 333 Z' fill='#f4f8fc'/>
<path d='M385 333 Q415 381 445 333 Z' fill='#f4f8fc'/><path d='M455 333 Q485 381 515 333 Z' fill='#f4f8fc'/>
<path d='M280 271 Q310 319 340 271 Z' fill='#f4f8fc'/><path d='M350 271 Q380 319 410 271 Z' fill='#f4f8fc'/>
<path d='M420 271 Q450 319 480 271 Z' fill='#f4f8fc'/>
<path d='M315 209 Q345 257 375 209 Z' fill='#f4f8fc'/><path d='M385 209 Q415 257 445 209 Z' fill='#f4f8fc'/>
<path d='M350 147 Q380 195 410 147 Z' fill='#f3d36b'/>
</g>
<g fill='#f3d36b'>
<path d='M327 221 Q345 245 363 221 Z'/><path d='M397 221 Q415 245 433 221 Z'/>
<ellipse cx='310' cy='292' rx='6' ry='2.5'/><ellipse cx='380' cy='292' rx='6' ry='2.5'/><ellipse cx='450' cy='292' rx='6' ry='2.5'/>
</g>
<g stroke='#5b6b7f' stroke-width='3'>
<line x1='275' y1='357' x2='275' y2='391'/><line x1='345' y1='357' x2='345' y2='391'/><line x1='415' y1='357' x2='415' y2='391'/><line x1='485' y1='357' x2='485' y2='391'/>
<line x1='310' y1='295' x2='310' y2='329'/><line x1='380' y1='295' x2='380' y2='329'/><line x1='450' y1='295' x2='450' y2='329'/>
<line x1='345' y1='233' x2='345' y2='267'/><line x1='415' y1='233' x2='415' y2='267'/>
<line x1='380' y1='171' x2='380' y2='205'/>
</g>
<g fill='#5b6b7f'>
<ellipse cx='275' cy='392' rx='14' ry='3'/><ellipse cx='345' cy='392' rx='14' ry='3'/><ellipse cx='415' cy='392' rx='14' ry='3'/><ellipse cx='485' cy='392' rx='14' ry='3'/>
<ellipse cx='310' cy='330' rx='14' ry='3'/><ellipse cx='380' cy='330' rx='14' ry='3'/><ellipse cx='450' cy='330' rx='14' ry='3'/>
<ellipse cx='345' cy='268' rx='14' ry='3'/><ellipse cx='415' cy='268' rx='14' ry='3'/>
<ellipse cx='380' cy='206' rx='14' ry='3'/>
</g>
<g stroke='#e2b93b' stroke-width='3'>
<line x1='352' y1='149' x2='352' y2='212'/><line x1='408' y1='149' x2='408' y2='212'/>
</g>
<polygon points='440,95 470,125 530,65 500,35' fill='#2e6b3a' stroke='#1d4526' stroke-width='2'/>
<polygon points='450,105 460,115 440,135 430,125' fill='#2e6b3a' stroke='#1d4526' stroke-width='2'/>
<path d='M435 132 Q405 138 385 152' fill='none' stroke='#e2b93b' stroke-width='5'/>
<line x1='532' y1='62' x2='545' y2='62' stroke='#999999' stroke-width='2'/>
<rect x='545' y='40' width='200' height='50' rx='8' fill='#fff3cc' stroke='#d9a400'/>
<text x='645' y='61' text-anchor='middle' font-size='13' font-weight='bold' fill='#6a4b00'>STEUERSENKUNGEN</text>
<text x='645' y='79' text-anchor='middle' font-size='12' fill='#6a4b00'>für Firmen und Topverdiener</text>
<text x='330' y='182' text-anchor='end' font-size='12' font-style='italic' fill='#555555'>oben</text>
<text x='235' y='372' text-anchor='end' font-size='12' font-style='italic' fill='#555555'>unten</text>
<circle cx='115' cy='300' r='16' fill='#f2c9a0' stroke='#333333' stroke-width='1.5'/>
<rect x='97' y='317' width='36' height='70' rx='6' fill='#14213d'/>
<polygon points='115,319 110,332 115,350 120,332' fill='#b5302a'/>
<rect x='100' y='387' width='12' height='45' fill='#22355e'/><rect x='118' y='387' width='12' height='45' fill='#22355e'/>
<line x1='133' y1='330' x2='166' y2='287' stroke='#14213d' stroke-width='8' stroke-linecap='round'/>
<circle cx='168' cy='284' r='5' fill='#f2c9a0'/>
<rect x='20' y='180' width='230' height='70' rx='12' fill='#ffffff' stroke='#999999'/>
<polygon points='104,249 124,249 114,282' fill='#ffffff' stroke='#999999'/>
<rect x='105' y='246' width='18' height='5' fill='#ffffff'/>
<text x='135' y='204' text-anchor='middle' font-size='13' fill='#333333'>Nur Geduld! Wenn oben alles</text>
<text x='135' y='222' text-anchor='middle' font-size='13' fill='#333333'>voll ist, läuft es nach</text>
<text x='135' y='240' text-anchor='middle' font-size='13' fill='#333333'>unten über.</text>
<circle cx='610' cy='338' r='15' fill='#e0b48a' stroke='#333333' stroke-width='1.5'/>
<rect x='595' y='354' width='30' height='58' rx='5' fill='#7a8b99'/>
<rect x='597' y='412' width='10' height='20' fill='#4a5568'/><rect x='613' y='412' width='10' height='20' fill='#4a5568'/>
<line x1='625' y1='368' x2='640' y2='366' stroke='#7a8b99' stroke-width='6' stroke-linecap='round'/>
<path d='M632 350 Q645 366 658 350 Z' fill='#f4f8fc' stroke='#5b6b7f' stroke-width='2'/>
<line x1='645' y1='358' x2='645' y2='372' stroke='#5b6b7f' stroke-width='2'/>
<ellipse cx='645' cy='373' rx='7' ry='2' fill='#5b6b7f'/>
<circle cx='690' cy='341' r='14' fill='#c68e6b' stroke='#333333' stroke-width='1.5'/>
<rect x='676' y='356' width='28' height='56' rx='5' fill='#b5302a'/>
<rect x='678' y='412' width='10' height='20' fill='#4a5568'/><rect x='692' y='412' width='10' height='20' fill='#4a5568'/>
<line x1='704' y1='370' x2='716' y2='368' stroke='#b5302a' stroke-width='6' stroke-linecap='round'/>
<path d='M710 352 Q722 368 734 352 Z' fill='#f4f8fc' stroke='#5b6b7f' stroke-width='2'/>
<line x1='722' y1='360' x2='722' y2='374' stroke='#5b6b7f' stroke-width='2'/>
<ellipse cx='722' cy='375' rx='7' ry='2' fill='#5b6b7f'/>
<rect x='560' y='235' width='190' height='70' rx='12' fill='#ffffff' stroke='#999999'/>
<polygon points='625,304 645,304 618,322' fill='#ffffff' stroke='#999999'/>
<rect x='626' y='301' width='18' height='5' fill='#ffffff'/>
<text x='655' y='259' text-anchor='middle' font-size='13' fill='#333333'>Bei uns ist in all</text>
<text x='655' y='277' text-anchor='middle' font-size='13' fill='#333333'>den Jahren kaum etwas</text>
<text x='655' y='295' text-anchor='middle' font-size='13' fill='#333333'>angekommen …</text>
</svg>"""

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Gastbeitrag „Wachstum entsteht nicht im Finanzministerium“ (2026)",
        "absaetze": [
            "Drei Jahre ohne nennenswertes Wachstum: Nach Angaben des Statistischen Bundesamtes schrumpfte die deutsche Wirtschaft 2023 um 0,9 Prozent und 2024 um 0,5 Prozent, 2025 wuchs sie gerade einmal um 0,2 Prozent. Zwar zeichnet sich 2026 eine leichte Erholung ab. Doch wer glaubt, das Problem sei damit erledigt, irrt. Deutschland leidet nicht an einer vorübergehenden Konjunkturdelle, sondern an einer Wachstumsschwäche, die tief in seinen Strukturen sitzt.",
            "Langfristiges Wachstum entsteht, wenn mehr gearbeitet wird, mehr investiert wird und die Produktivität steigt. Bei allen drei Faktoren sieht es schlecht aus. Die geburtenstarken Jahrgänge gehen in Rente, und schon heute fehlen in vielen Branchen Fachkräfte. Die Unternehmen investieren zu wenig, weil Energie teuer ist, Genehmigungen Jahre dauern und die Steuerbelastung auf Gewinne im internationalen Vergleich hoch ist. Und die Produktivität wächst seit Jahren kaum noch.",
            "Die Politik antwortet darauf vor allem mit Geld. Mit dem Sondervermögen für Infrastruktur und Klimaneutralität und der Ausnahme von der Schuldenbremse für Verteidigungsausgaben nimmt der Bund Kredite in Rekordhöhe auf. Investitionen in Brücken und Schienen sind sinnvoll. Aber ein Staat, der mit Schulden Nachfrage erzeugt, ersetzt keine Unternehmen, die hier investieren wollen. Schulden von heute sind die Steuern von morgen – und das wissen auch die Investoren.",
            "Was wir brauchen, ist ein Angebotsschock. Erstens müssen die Steuern auf Unternehmensgewinne schneller sinken als geplant: Die beschlossene Senkung der Körperschaftsteuer ab 2028 ist richtig, kommt aber zu spät. Zweitens brauchen wir einen radikalen Bürokratieabbau: Für jede neue Vorschrift sollten zwei alte wegfallen. Drittens muss sich Arbeit mehr lohnen – durch niedrigere Abgaben auf Arbeitseinkommen und Anreize, länger und mehr zu arbeiten.",
            "Die Erfahrung gibt dieser Politik recht. Als Deutschland Anfang der 2000er-Jahre als „kranker Mann Europas“ galt, brachte die Agenda 2010 die Wende: Flexiblere Arbeitsmärkte und das Prinzip des Förderns und Forderns trugen dazu bei, dass die Arbeitslosigkeit in den folgenden Jahren stark sank. Großbritannien und die USA haben in den 1980er-Jahren gezeigt, dass Steuersenkungen und Deregulierung eine erstarrte Wirtschaft beleben können.",
            "Natürlich profitieren von niedrigeren Unternehmensteuern zunächst die Unternehmen. Aber wer daraus eine Gerechtigkeitsfrage macht, übersieht: Arbeitsplätze und steigende Löhne entstehen nur dort, wo investiert wird. Die beste Sozialpolitik ist ein wettbewerbsfähiger Standort. Wer Wohlstand verteilen will, muss ihn zuerst erwirtschaften.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Gastbeitrag einer fiktiven Wirtschaftswissenschaftlerin (2026). Die Wachstumszahlen stammen vom Statistischen Bundesamt (Pressemitteilung Januar 2026); die schrittweise Senkung der Körperschaftsteuer ab 2028 wurde 2025 mit dem steuerlichen Investitionssofortprogramm beschlossen.",
    },
    {
        "id": "m2",
        "typ": "bild",
        "titel": "M2: Karikatur „Der Champagnerturm“ (2026)",
        "svg": KARIKATUR_SVG,
        "beschreibung": "Die Karikatur trägt oben links den Titel 'Der Champagnerturm'. In der Bildmitte steht auf einem Tisch eine Pyramide aus zehn Sektschalen: unten vier, darüber drei, dann zwei und ganz oben eine. Neben dem obersten Glas steht klein 'oben', neben der untersten Reihe 'unten'. Von rechts oben gießt eine schräg gehaltene grüne Champagnerflasche einen goldenen Strahl in das oberste Glas; ein Schild an der Flasche trägt die Aufschrift 'STEUERSENKUNGEN für Firmen und Topverdiener'. Das oberste Glas ist randvoll, an seinen Rändern laufen dünne Rinnsale in die beiden Gläser der zweiten Reihe, die etwa halb gefüllt sind. In den drei Gläsern der dritten Reihe sind nur noch einzelne Tropfen, die vier Gläser der untersten Reihe sind leer. Links neben dem Tisch steht ein Mann im dunklen Anzug mit roter Krawatte, der mit erhobenem Arm nach oben zeigt und sagt: 'Nur Geduld! Wenn oben alles voll ist, läuft es nach unten über.' Rechts stehen zwei einfach gekleidete Menschen, die jeweils eine leere Sektschale in der Hand halten; einer von ihnen sagt: 'Bei uns ist in all den Jahren kaum etwas angekommen …'.",
        "quelle": "Übungsmaterial: eigene Zeichnung für Feibitur (2026).",
    },
    {
        "id": "m3",
        "titel": "M3: Kommentar „Wer zahlt die Zeche?“ (2026)",
        "absaetze": [
            "Wenn die Wirtschaft schwächelt, ist die Antwort mancher Ökonominnen und Ökonomen immer dieselbe: Steuern runter für Unternehmen, Regeln weg, Sozialleistungen kürzen. Das Rezept ist über 40 Jahre alt – und seine Bilanz ist durchwachsen.",
            "In den USA versprach Ronald Reagan in den 1980er-Jahren, dass sich Steuersenkungen durch mehr Wachstum selbst finanzieren würden. Tatsächlich stiegen Haushaltsdefizite und Staatsschulden stark an, und die Einkommen der Reichsten wuchsen viel schneller als die der Mittelschicht. Der Wohlstand ist nicht nach unten durchgesickert, er ist oben hängen geblieben.",
            "Auch die Erfolgsgeschichte der Agenda 2010 ist nur die halbe Wahrheit. Ja, die Arbeitslosigkeit sank nach 2005 deutlich. Aber dazu trugen auch die gute Weltkonjunktur und jahrelange Lohnzurückhaltung bei. Gleichzeitig wuchs ein großer Niedriglohnsektor. Viele Menschen arbeiteten in Minijobs oder Leiharbeit, ohne Aussicht auf Aufstieg. Erst der gesetzliche Mindestlohn hat 2015 eine Untergrenze gezogen.",
            "Heute investieren Unternehmen nicht vor allem deshalb zu wenig, weil die Steuern zu hoch sind, sondern weil sie unsicher sind, ob sich ihre Produkte verkaufen lassen: Die Exporte leiden unter Zöllen und der Konkurrenz aus China, und die Verbraucher halten sich zurück. Hinzu kommt ein jahrzehntelanger Investitionsstau bei Schulen, Schienen, Brücken und Netzen. Hier liegt die eigentliche Wachstumsbremse – und hier muss der Staat handeln. Das Sondervermögen ist dafür ein richtiger, wenn auch später Schritt.",
            "Pauschale Steuersenkungen für Unternehmen kosten den Staat Milliarden, die dann bei Bildung, Pflege oder Klimaschutz fehlen. Davon profitieren vor allem Aktionäre und Spitzenverdiener. Wer gleichzeitig bei Sozialleistungen kürzt, verschärft die Ungleichheit und schwächt die Kaufkraft breiter Schichten – also genau die Nachfrage, die die Unternehmen brauchen.",
            "Und noch etwas fehlt in der Debatte: Wachstum ist kein Wert an sich. Ein Wachstum, das die Klimakrise verschärft und die Gesellschaft spaltet, macht uns nicht reicher. Wir sollten Erfolg nicht allein am Bruttoinlandsprodukt messen, sondern daran, ob Arbeit gut bezahlt ist, die Umwelt geschützt wird und alle am Wohlstand teilhaben. Nachhaltiges Wachstum braucht einen aktiven Staat, keinen Nachtwächter.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Ökonomen eines gewerkschaftsnahen Instituts (2026). Die Angaben zu Reaganomics, Agenda 2010 und Mindestlohn (seit 2015) beziehen sich auf reale Entwicklungen.",
    },
]

AUFGABEN = [
    {
        "id": "q2-2-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Gastbeitrags zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung: Gastbeitrag einer (fiktiven) Wirtschaftswissenschaftlerin, „Wachstum entsteht nicht im Finanzministerium“, 2026; Thema: Ursachen der deutschen Wachstumsschwäche und Forderung nach angebotsorientierten Reformen.",
            "punkte": [
                "Die Autorin stellt fest, Deutschland sei 2023 und 2024 geschrumpft und 2025 kaum gewachsen; trotz leichter Erholung 2026 handle es sich um eine strukturelle, nicht um eine konjunkturelle Schwäche [1].",
                "Wachstum hänge von Arbeit, Kapital/Investitionen und Produktivität ab; bei allen drei Faktoren gebe es Probleme (Demografie, Fachkräftemangel, Energiepreise, lange Genehmigungen, hohe Unternehmensteuern, schwache Produktivität) [2].",
                "Die Politik setze vor allem auf kreditfinanzierte Ausgaben (Sondervermögen, Ausnahme für Verteidigung); staatlich erzeugte Nachfrage ersetze aber keine privaten Investitionen, Schulden bedeuteten künftige Steuern [3].",
                "Gefordert wird ein „Angebotsschock“: schnellere Senkung der Unternehmensteuern, radikaler Bürokratieabbau, niedrigere Abgaben und stärkere Arbeitsanreize [4].",
                "Als Belege verweist sie auf die Agenda 2010 sowie auf Großbritannien und die USA in den 1980er-Jahren [5].",
                "Den Gerechtigkeitseinwand weist sie zurück: Arbeitsplätze und Löhne entstünden nur durch Investitionen, die beste Sozialpolitik sei ein wettbewerbsfähiger Standort [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache (z. B. Produktionsfaktoren, Angebotsbedingungen), keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Gastbeitrags im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen weitgehend vollständig, strukturiert, in eigenen Worten und unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q2-2-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Karikatur (M2).",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Formale Angaben: Karikatur „Der Champagnerturm“, eigene Zeichnung, 2026.",
                "Bildmitte: Pyramide aus zehn Sektschalen auf einem Tisch (vier, drei, zwei, eine), Markierungen „oben“ und „unten“.",
                "Rechts oben: Champagnerflasche mit dem Schild „STEUERSENKUNGEN für Firmen und Topverdiener“, die in das oberste Glas gießt.",
                "Füllstand: oberstes Glas randvoll, zweite Reihe halb gefüllt durch dünne Rinnsale, dritte Reihe nur Tropfen, unterste Reihe leer.",
                "Links: Mann im Anzug mit roter Krawatte, zeigt nach oben, Sprechblase „Nur Geduld! Wenn oben alles voll ist, läuft es nach unten über.“",
                "Rechts: zwei einfach gekleidete Personen mit leeren Gläsern, Sprechblase „Bei uns ist in all den Jahren kaum etwas angekommen …“.",
            ],
            "hinweis": "Beschreiben: nur das Sichtbare strukturiert (z. B. Mitte – rechts oben – links – rechts unten) wiedergeben; Deutung (Trickle-down) gehört noch nicht hierher.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Bildelemente im Ansatz korrekt beschrieben werden.",
            "gut": "die Karikatur vollständig, strukturiert und präzise beschrieben wird, ohne vorzeitig zu deuten.",
        },
    },
    {
        "id": "q2-2-i3",
        "afb": "I",
        "operator": "wiedergeben",
        "text": "Geben Sie die Kritik des Autors an der angebotsorientierten Wirtschaftspolitik wieder. (M3)",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitungssatz: Kommentar „Wer zahlt die Zeche?“ (2026) eines (fiktiven) Ökonomen eines gewerkschaftsnahen Instituts zur Kritik angebotsorientierter Wirtschaftspolitik.",
            "punkte": [
                "Das angebotspolitische Rezept (Steuersenkungen, Deregulierung, Sozialkürzungen) sei alt und habe eine durchwachsene Bilanz [1].",
                "Reaganomics: Steuersenkungen hätten sich nicht selbst finanziert, Defizite und Schulden seien gestiegen, die Einkommen der Reichsten schneller gewachsen; kein Trickle-down [2].",
                "Agenda 2010: Rückgang der Arbeitslosigkeit auch durch Weltkonjunktur und Lohnzurückhaltung; Entstehung eines großen Niedriglohnsektors, erst der Mindestlohn 2015 habe eine Untergrenze gezogen [3].",
                "Die heutige Investitionsschwäche beruhe vor allem auf Absatzunsicherheit (Zölle, China, Konsumzurückhaltung) und öffentlichem Investitionsstau; der Staat müsse investieren [4].",
                "Steuersenkungen kosteten Milliarden, begünstigten Aktionäre und Spitzenverdiener; Sozialkürzungen verschärften Ungleichheit und schwächten die Nachfrage [5].",
                "Wachstum sei kein Selbstzweck; Erfolg solle an guter Arbeit, Umweltschutz und Teilhabe gemessen werden – nachhaltiges Wachstum brauche einen aktiven Staat [6].",
            ],
            "hinweis": "Wiedergeben: ausgehend von einem Einleitungssatz die Informationen des Materials in eigenen Worten und fachsprachlich ausdrücken (indirekte Rede); keine eigene Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die Kritik des Autors im Ansatz korrekt und mit Einleitungssatz wiedergegeben wird.",
            "gut": "die Kritikpunkte weitgehend vollständig, strukturiert, fachsprachlich und in eigenen Worten wiedergegeben werden.",
        },
    },
    {
        "id": "q2-2-ii1",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie ausgehend von M1 die Bestimmungsfaktoren mittel- und langfristigen Wirtschaftswachstums aus Sicht der neoklassischen Konzeption.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Grundannahmen der Neoklassik: flexible Preise, Löhne und Zinsen, Selbstheilungskräfte der Märkte, Say'sches Theorem – langfristiges Wachstum wird von der Angebotsseite bestimmt.",
                "Produktionsfaktor Arbeit: Zahl der Erwerbstätigen, Arbeitsvolumen, Qualifikation; in M1 Demografie und Fachkräftemangel als Bremse [2].",
                "Produktionsfaktor Kapital: Investitionen erhöhen den Kapitalstock; abhängig von Rentabilität (Steuern, Energiekosten, Bürokratie) [2], [4]; abnehmende Grenzerträge des Kapitals (Solow-Modell).",
                "Technischer Fortschritt/Produktivität als entscheidende Quelle dauerhaften Pro-Kopf-Wachstums (totale Faktorproduktivität); in M1 schwaches Produktivitätswachstum [2].",
                "Rolle des Staates: Gestaltung der Angebotsbedingungen (Steuern, Regulierung, Arbeitsanreize, solide Finanzen) statt Nachfragesteuerung; Kritik an kreditfinanzierter Nachfrage und Crowding-out-/Erwartungseffekten („Schulden von heute sind die Steuern von morgen“) [3].",
                "Abgrenzung zur keynesianischen Sicht (Nachfrage als Engpass) zur Verdeutlichung.",
            ],
            "hinweis": "Erklären: Rückführung auf das neoklassische Modell (Produktionsfunktion, Faktoren, Angebotsbedingungen); Materialbezüge erforderlich. Eine reine Aufzählung von Faktoren ohne Begründungszusammenhang genügt nicht für „gut“.",
        },
        "bewertung": {
            "ausreichend": "die Bestimmungsfaktoren des Wachstums im Ansatz zutreffend erklärt und auf die neoklassische Sicht bezogen werden.",
            "gut": "die Bestimmungsfaktoren differenziert, modellgestützt (Produktionsfunktion, abnehmende Grenzerträge, technischer Fortschritt) und mit Materialbezug erklärt werden.",
        },
    },
    {
        "id": "q2-2-ii2",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Karikatur (M2) im Hinblick auf ihre Aussage zu den Verteilungswirkungen angebotsorientierter Wirtschaftspolitik.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Champagnerturm als Bild der Einkommens- und Vermögensverteilung bzw. der gesellschaftlichen Hierarchie („oben“ – „unten“).",
                "Flasche „Steuersenkungen für Firmen und Topverdiener“: angebotsorientierte Entlastungen setzen oben an (Unternehmensteuern, Spitzensteuersatz).",
                "Mann im Anzug verkörpert die Trickle-down-These (Befürworter angebotsorientierter Politik): Wohlstand laufe von oben nach unten über (Investitionen, Arbeitsplätze, Löhne).",
                "Füllstände: Der Nutzen bleibt weitgehend oben, nach unten kommen nur Tropfen – Kritik, dass die Durchsickerwirkung gering ist und Ungleichheit wächst.",
                "Wartende Personen mit leeren Gläsern („in all den Jahren“): Verweis auf jahrzehntelange Erfahrungen (z. B. Reaganomics, Niedriglohnsektor) und auf enttäuschte Erwartungen unterer Einkommensgruppen.",
                "Kernaussage: Angebotsorientierte Steuerpolitik begünstige vor allem Wohlhabende; das Versprechen eines allgemeinen Wohlstandsgewinns erweise sich als unzutreffend. Fachbegriffe: Trickle-down, Verteilungswirkung, Ungleichheit.",
            ],
            "hinweis": "Analysieren: Bildelemente systematisch deuten und auf Fachkonzepte beziehen; Bildbelege angeben; klare Kernaussage formulieren.",
        },
        "bewertung": {
            "ausreichend": "zentrale Bildelemente ansatzweise zutreffend gedeutet werden und eine Kernaussage formuliert wird.",
            "gut": "die Bildelemente systematisch, mit Fachbegriffen (Trickle-down, Verteilungswirkungen) gedeutet werden und eine präzise Kernaussage formuliert wird.",
        },
    },
    {
        "id": "q2-2-ii3",
        "afb": "II",
        "operator": "vergleichen",
        "text": "Vergleichen Sie die Positionen der Autorin (M1) und des Autors (M3) hinsichtlich der Ursachen der Wachstumsschwäche, der Rolle des Staates und der Verteilungswirkungen.",
        "material": ["m1", "m3"],
        "loesung": {
            "punkte": [
                "Gemeinsamkeiten: Beide sehen eine ernsthafte Wachstums- bzw. Investitionsschwäche; beide halten öffentliche Investitionen in Infrastruktur grundsätzlich für sinnvoll (M1 [3], M3 [4]); beide beziehen sich auf die Agenda 2010 und die 1980er-Jahre.",
                "Ursachen: M1 – strukturelle Angebotsprobleme (Demografie, Kosten, Bürokratie, Steuern, Produktivität) [2]; M3 – Nachfrageschwäche (Absatzunsicherheit, Zölle, Konsumzurückhaltung) und öffentlicher Investitionsstau [4].",
                "Rolle des Staates: M1 – Angebotsbedingungen verbessern, Steuern senken, deregulieren, Schulden begrenzen (neoklassisch-angebotsorientiert) [3], [4]; M3 – aktiver Staat, öffentliche Investitionen, Nachfrage stärken, Sozialleistungen erhalten (keynesianisch geprägt) [4]–[6].",
                "Verteilung: M1 – Gerechtigkeitseinwand nachrangig, Wohlstand müsse erst erwirtschaftet werden, Investitionen schaffen Jobs [6]; M3 – Steuersenkungen begünstigen Aktionäre und Spitzenverdiener, Sozialkürzungen verschärfen Ungleichheit [2], [5].",
                "Bewertung historischer Erfahrungen: M1 deutet Agenda 2010 und Reagan/Thatcher als Erfolge [5]; M3 relativiert (Weltkonjunktur, Niedriglohnsektor, Defizite) [2], [3].",
                "Zusätzlich M3: Kritik am BIP als Erfolgsmaß, Forderung nach nachhaltigem Wachstum [6] – in M1 nicht thematisiert.",
            ],
            "hinweis": "Vergleichen: kriteriengeleitete Gegenüberstellung von Gemeinsamkeiten UND Unterschieden mit Belegen; ein bloßes Nacheinander beider Positionen genügt nicht für „gut“. Zuordnung zu den wirtschaftspolitischen Konzeptionen wird erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Positionen ansatzweise kriteriengeleitet verglichen und mit einzelnen Belegen gestützt werden.",
            "gut": "die Positionen entlang aller drei Kriterien differenziert, mit Gemeinsamkeiten und Unterschieden, Belegen und Zuordnung zu den Konzeptionen verglichen werden.",
        },
    },
    {
        "id": "q2-2-ii4",
        "afb": "II",
        "operator": "erläutern",
        "lk": True,
        "text": "Erläutern Sie, mit welchen Instrumenten die Europäische Union auf Konzentrationsprozesse und Marktmacht reagiert, insbesondere auf digitalen Märkten.",
        "material": [],
        "loesung": {
            "punkte": [
                "Ausgangsproblem: Konzentration (horizontal, vertikal, konglomerat) und Marktformen mit wenigen Anbietern (Oligopol, Monopol) führen zu Marktmacht; digitale Plattformen neigen wegen Netzwerk- und Dateneffekten besonders zur Konzentration.",
                "Kartellverbot (Art. 101 AEUV): Verbot wettbewerbsbeschränkender Absprachen, Bußgelder, Kronzeugenregelung; Beispiel Lkw-Kartell 2016.",
                "Missbrauchsaufsicht (Art. 102 AEUV): Marktbeherrschung erlaubt, Missbrauch verboten; Beispiel Google Shopping (2017 verhängt, 2024 vom EuGH bestätigt) oder Adtech-Verfahren 2025.",
                "Fusionskontrolle (Fusionskontrollverordnung): Anmeldung oberhalb von Umsatzschwellen, Untersagung oder Auflagen; Beispiel Siemens/Alstom 2019.",
                "Beihilfekontrolle (Art. 107 AEUV) gegen wettbewerbsverzerrende Subventionen.",
                "Digital Markets Act: Ex-ante-Pflichten für benannte Gatekeeper (z. B. Verbot der Selbstbevorzugung, Öffnung für alternative Vertriebs- und Bezahlwege); erste Bußgelder 2025 gegen Apple und Meta; ergänzend in Deutschland § 19a GWB.",
                "Ggf. Hinweis auf Kontroverse („europäische Champions“, Draghi-Bericht 2024) und auf Kritik aus den USA.",
            ],
            "hinweis": "Erläutern: Instrumente mit zusätzlichen Informationen und konkreten Beispielen veranschaulichen; die Besonderheit digitaler Märkte (ex ante statt ex post) sollte deutlich werden.",
        },
        "bewertung": {
            "ausreichend": "zentrale Instrumente der EU-Wettbewerbspolitik ansatzweise zutreffend und mit mindestens einem Beispiel erläutert werden.",
            "gut": "die Instrumente differenziert, mit Rechtsgrundlagen und passenden Beispielen erläutert werden und die Besonderheit des Digital Markets Act überzeugend herausgestellt wird.",
        },
    },
    {
        "id": "q2-2-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Die Autorin fordert einen „Angebotsschock“ mit schnelleren Steuersenkungen für Unternehmen, radikalem Bürokratieabbau und stärkeren Arbeitsanreizen. Erörtern Sie diese Forderung. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klärung: Forderung entspricht den Prinzipien angebotsorientierter Politik (Steuersenkung, Deregulierung, Flexibilisierung) [4]; Bezug zur aktuellen Lage (Stagnation 2023–2025, Investitionsschwäche).",
                "Pro: höhere Nettorenditen stärken Investitionen; internationale Steuerwettbewerbsfähigkeit; Bürokratieabbau senkt Kosten ohne Haushaltsbelastung; Arbeitsanreize erhöhen das Arbeitsangebot angesichts von Demografie und Fachkräftemangel; Erfahrungen mit der Agenda 2010 [5].",
                "Contra: Steuersenkungen ohne Gegenfinanzierung belasten den Haushalt (Schuldenbremse, Zinslasten) und können Investitionen in Bildung und Infrastruktur verdrängen; Mitnahmeeffekte; Investitionen hängen auch von Absatzerwartungen ab (Nachfrageseite); Verteilungswirkungen zugunsten von Kapitaleinkommen; Bürokratieabbau kann Schutzstandards senken; Erfahrungen der 1980er-Jahre (Defizite, Ungleichheit).",
                "Abwägung, z. B. nach Kriterien Effektivität (Wachstumswirkung), Finanzierbarkeit, Verteilungsgerechtigkeit, Zeithorizont; differenzierte Lösungen möglich (z. B. gezielte Investitionsanreize, Abbau von Genehmigungshürden, Policy-Mix mit öffentlichen Investitionen).",
                "Eigenes, begründetes Urteil.",
            ],
            "hinweis": "Erörtern: Pro- und Kontraargumente abwägen und zu einem eigenen Urteil gelangen; Bezug auf die konkreten Forderungen in M1 [4] und auf Fachwissen (angebots- vs. nachfrageorientierte Konzeption) erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und weitgehend kohärent ist und in ein klares, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q2-2-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie die Aussage der Karikatur (M2) vor dem Hintergrund der Erfahrungen mit angebotsorientierter Wirtschaftspolitik.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien benennen, z. B. empirische Stichhaltigkeit, Vollständigkeit der Darstellung, Berücksichtigung von Wirkungszusammenhängen.",
                "Stützend: Reaganomics – Steuersenkungen finanzierten sich nicht selbst, Ungleichheit nahm zu; Thatcherismus – steigende Arbeitslosigkeit und regionale Verarmung; Agenda 2010 – wachsender Niedriglohnsektor; Gewinne können ausgeschüttet oder im Ausland investiert werden.",
                "Relativierend: Angebotspolitik zielt auch auf Beschäftigung (Rückgang der Arbeitslosigkeit nach 2005), Investitionen und Produktivität, wovon auch Beschäftigte profitieren können; Wirkung oft verzögert; nicht jede Angebotspolitik setzt oben an (Bürokratieabbau, Bildung, Infrastruktur, Fachkräfte); Verteilungsergebnisse hängen auch von Tarifpolitik und Sozialstaat ab.",
                "Karikatur als bewusste Zuspitzung: Sie blendet Wachstums- und Beschäftigungseffekte aus und stellt Verteilung als Nullsummenspiel dar.",
                "Begründetes Gesamturteil (z. B. Kritik an pauschalen Steuersenkungen für Spitzeneinkommen berechtigt, als Urteil über Angebotspolitik insgesamt verkürzt).",
            ],
            "hinweis": "Beurteilen: kriteriengeleitetes Sachurteil auf Basis von Fachwissen und historischen Beispielen; Bezug zu konkreten Bildelementen erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Aussage der Karikatur ansatzweise kriteriengeleitet und mit einzelnen Beispielen beurteilt wird.",
            "gut": "die Aussage differenziert, mit Bezug zu mehreren historischen Erfahrungen und Wirkungszusammenhängen beurteilt und schlüssig begründet wird.",
        },
    },
    {
        "id": "q2-2-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Entwerfen Sie eine Rede für eine Podiumsdiskussion des Schülerparlaments zum Thema „Wie schafft Deutschland wieder nachhaltiges Wachstum?“, in der Sie eine eigene wachstumspolitische Strategie begründen. Berücksichtigen Sie dabei Argumente aus M1 und M3 sowie das Ziel nachhaltigen Wachstums.",
        "material": ["m1", "m3"],
        "loesung": {
            "punkte": [
                "Adressaten- und situationsgerechte Gestaltung: Anrede, Einstieg (z. B. aktuelle Wachstumszahlen), klare Gliederung, rhetorische Mittel, Appell bzw. Schluss.",
                "Problemdiagnose mit Fachbegriffen: Wachstumsschwäche 2023–2025, strukturelle Faktoren (Demografie, Produktivität, Investitionen, Energiekosten) und ggf. Nachfrageschwäche.",
                "Eigene Strategie mit begründeten Maßnahmen, z. B. angebotsseitig (Genehmigungen beschleunigen, Fachkräfte gewinnen, gezielte Investitionsanreize), nachfrage- bzw. staatsseitig (öffentliche Investitionen in Infrastruktur, Bildung, Netze) und nachhaltigkeitsbezogen (Klimaschutzinvestitionen, Entkopplung, Wohlfahrtsindikatoren).",
                "Auseinandersetzung mit Gegenargumenten aus M1 (Schulden als künftige Steuern, Angebotsschock) und M3 (Verteilungswirkungen, aktiver Staat).",
                "Berücksichtigung von Finanzierung (Schuldenbremse, Sondervermögen) und Verteilungsgerechtigkeit.",
                "Schlüssige Verknüpfung zu einem Gesamtkonzept (z. B. Policy-Mix) mit erkennbarer eigener Position.",
            ],
            "hinweis": "Entwerfen (gestalten): produktorientierte Bearbeitung; neben fachlicher Fundierung zählen Textsortenmerkmale der Rede und die Kohärenz der Strategie. Jede schlüssig begründete Strategie ist anzuerkennen.",
        },
        "bewertung": {
            "ausreichend": "eine Rede mit erkennbarer Strategie vorliegt, die einige fachlich zutreffende Argumente aus M1 und M3 aufgreift.",
            "gut": "die Rede adressatengerecht gestaltet ist und eine fachlich fundierte, in sich schlüssige Strategie entwickelt, die Gegenargumente und das Ziel nachhaltigen Wachstums überzeugend einbezieht.",
        },
    },
    {
        "id": "q2-2-iii4",
        "afb": "III",
        "operator": "Stellung nehmen",
        "lk": True,
        "text": "Nehmen Sie ausgehend von M1 und M3 Stellung zu der These, die Soziale Marktwirtschaft werde heute eher durch zu viel Staat als durch zu viel Markt gefährdet.",
        "material": ["m1", "m3"],
        "loesung": {
            "punkte": [
                "Klärung der Konzeption: Soziale Marktwirtschaft als Verbindung von Marktfreiheit und sozialem Ausgleich (Müller-Armack), ordoliberale Wurzeln (Eucken: konstituierende und regulierende Prinzipien), Abgrenzung zur freien Marktwirtschaft und zur Zentralverwaltungswirtschaft.",
                "Argumente für die These (Nähe zu M1): hohe Steuer- und Abgabenlast, Regulierungsdichte und Bürokratie, kreditfinanzierte Staatsausgaben, Verstoß gegen Euckens Prinzip der Konstanz und solider Finanzen; Gefahr für Investitionen und Wettbewerbsfähigkeit.",
                "Argumente gegen die These (Nähe zu M3): Ungleichheit, Niedriglohnsektor, Marktmacht großer (Digital-)Konzerne als Gefahr für Wettbewerb (Eucken: Monopolkontrolle), Investitionsstau durch zu wenig Staat, ökologische Externalitäten als Marktversagen.",
                "Differenzierung: „Staat“ ist nicht gleich „Staat“ – ordnungspolitische Eingriffe (Wettbewerbsschutz) vs. prozesspolitische Eingriffe; Frage nach Qualität statt Quantität staatlichen Handelns.",
                "Offenlegung eigener Wertmaßstäbe (z. B. Vorrang von Freiheit/Eigenverantwortung vs. sozialer Gerechtigkeit/Teilhabe) und klare, begründete Position.",
            ],
            "hinweis": "Stellung nehmen: wie beurteilen, zusätzlich müssen die eigenen Wertmaßstäbe ausdrücklich dargelegt werden. Ohne Rückbindung an die Konzeption der Sozialen Marktwirtschaft und ohne Materialbezug ist eine gute Leistung nicht möglich.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit Bezug zur Sozialen Marktwirtschaft und erkennbaren eigenen Maßstäben vorliegt.",
            "gut": "die Stellungnahme die Konzeption der Sozialen Marktwirtschaft fachlich fundiert einbezieht, Argumente aus M1 und M3 abwägt, eigene Wertmaßstäbe ausdrücklich offenlegt und in ein klares Urteil mündet.",
        },
    },
]
