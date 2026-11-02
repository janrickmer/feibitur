# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q3.1 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

SVG_KARIKATUR = """<svg viewBox='0 0 760 460' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='q31kk'>
<title id='q31kk'>Karikatur Bitte warten: Vor einer Tür mit der Aufschrift Kapitel VII hängen fünf Vorhängeschlösser mit den Kürzeln CN, FR, RU, UK und US. Ein Mann mit der Aufschrift UN versucht schwitzend, sie mit einem Schlüssel zu öffnen. Links warten Menschen mit Schildern Ukraine, Sudan, Gaza und Syrien.</title>
<rect x='0' y='0' width='760' height='460' fill='#fffdf6'/>
<line x1='0' y1='400' x2='760' y2='400' stroke='#999' stroke-width='2'/>
<rect x='250' y='80' width='150' height='30' rx='4' fill='#eeeeee' stroke='#999'/>
<text x='325' y='100' text-anchor='middle' font-size='12' fill='#333'>In Betrieb seit 1945</text>
<rect x='40' y='150' width='150' height='34' rx='6' fill='#fff7e0' stroke='#d9a400'/>
<text x='115' y='172' text-anchor='middle' font-size='13' font-weight='bold' fill='#6a4b00'>WARTEBEREICH</text>
<rect x='430' y='60' width='240' height='340' fill='#8c7a5b'/>
<rect x='440' y='70' width='220' height='330' fill='#dfe6f7' stroke='#14213d' stroke-width='2'/>
<rect x='465' y='82' width='170' height='64' rx='6' fill='#14213d'/>
<text x='550' y='103' text-anchor='middle' font-size='15' font-weight='bold' fill='#ffffff'>KAPITEL VII</text>
<text x='550' y='121' text-anchor='middle' font-size='12' fill='#ffffff'>Maßnahmen bei Bedrohung</text>
<text x='550' y='137' text-anchor='middle' font-size='12' fill='#ffffff'>des Friedens</text>
<circle cx='462' cy='240' r='7' fill='#d9a400' stroke='#6a4b00'/>
<g fill='none' stroke='#555' stroke-width='4'>
<path d='M538 165 L538 159 Q550 147 562 159 L562 165'/>
<path d='M538 213 L538 207 Q550 195 562 207 L562 213'/>
<path d='M538 261 L538 255 Q550 243 562 255 L562 261'/>
<path d='M538 309 L538 303 Q550 291 562 303 L562 309'/>
<path d='M538 357 L538 351 Q550 339 562 351 L562 357'/>
</g>
<g fill='#d9a400' stroke='#6a4b00' stroke-width='1.5'>
<rect x='528' y='165' width='44' height='32' rx='4'/>
<rect x='528' y='213' width='44' height='32' rx='4'/>
<rect x='528' y='261' width='44' height='32' rx='4'/>
<rect x='528' y='309' width='44' height='32' rx='4'/>
<rect x='528' y='357' width='44' height='32' rx='4'/>
</g>
<g font-size='13' font-weight='bold' fill='#14213d' text-anchor='middle'>
<text x='550' y='186'>CN</text>
<text x='550' y='234'>FR</text>
<text x='550' y='282'>RU</text>
<text x='550' y='330'>UK</text>
<text x='550' y='378'>US</text>
</g>
<circle cx='715' cy='120' r='26' fill='#ffffff' stroke='#333' stroke-width='2'/>
<line x1='715' y1='120' x2='715' y2='102' stroke='#333' stroke-width='2'/>
<line x1='715' y1='120' x2='729' y2='126' stroke='#333' stroke-width='2'/>
<circle cx='370' cy='252' r='16' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<ellipse cx='392' cy='238' rx='3' ry='5' fill='#7fb8e6'/>
<ellipse cx='397' cy='252' rx='3' ry='5' fill='#7fb8e6'/>
<rect x='352' y='270' width='36' height='70' rx='6' fill='#4a6fa5' stroke='#14213d'/>
<text x='370' y='312' text-anchor='middle' font-size='13' font-weight='bold' fill='#ffffff'>UN</text>
<line x1='362' y1='340' x2='358' y2='396' stroke='#14213d' stroke-width='5'/>
<line x1='378' y1='340' x2='384' y2='396' stroke='#14213d' stroke-width='5'/>
<line x1='352' y1='285' x2='336' y2='315' stroke='#4a6fa5' stroke-width='6'/>
<line x1='388' y1='282' x2='426' y2='262' stroke='#4a6fa5' stroke-width='6'/>
<circle cx='433' cy='262' r='9' fill='none' stroke='#d9a400' stroke-width='3'/>
<line x1='439' y1='268' x2='449' y2='282' stroke='#d9a400' stroke-width='3'/>
<rect x='230' y='160' width='190' height='50' rx='12' fill='#ffffff' stroke='#555'/>
<polygon points='340,209 362,209 362,232' fill='#ffffff' stroke='#555'/>
<line x1='341' y1='209' x2='361' y2='209' stroke='#ffffff' stroke-width='2'/>
<text x='325' y='181' text-anchor='middle' font-size='13' fill='#333'>Einer sagt immer</text>
<text x='325' y='199' text-anchor='middle' font-size='13' fill='#333'>Nein …</text>
<g stroke='#333' stroke-width='3' fill='none'>
<line x1='66' y1='246' x2='66' y2='330'/><line x1='50' y1='297' x2='50' y2='345'/><line x1='50' y1='308' x2='66' y2='302'/><line x1='50' y1='308' x2='38' y2='338'/><line x1='50' y1='345' x2='40' y2='396'/><line x1='50' y1='345' x2='60' y2='396'/>
<line x1='131' y1='246' x2='131' y2='330'/><line x1='115' y1='297' x2='115' y2='345'/><line x1='115' y1='308' x2='131' y2='302'/><line x1='115' y1='308' x2='103' y2='338'/><line x1='115' y1='345' x2='105' y2='396'/><line x1='115' y1='345' x2='125' y2='396'/>
<line x1='196' y1='246' x2='196' y2='330'/><line x1='180' y1='297' x2='180' y2='345'/><line x1='180' y1='308' x2='196' y2='302'/><line x1='180' y1='308' x2='168' y2='338'/><line x1='180' y1='345' x2='170' y2='396'/><line x1='180' y1='345' x2='190' y2='396'/>
<line x1='261' y1='246' x2='261' y2='330'/><line x1='245' y1='297' x2='245' y2='345'/><line x1='245' y1='308' x2='261' y2='302'/><line x1='245' y1='308' x2='233' y2='338'/><line x1='245' y1='345' x2='235' y2='396'/><line x1='245' y1='345' x2='255' y2='396'/>
</g>
<g fill='#f2c9a0' stroke='#333' stroke-width='1.5'>
<circle cx='50' cy='285' r='12'/><circle cx='115' cy='285' r='12'/><circle cx='180' cy='285' r='12'/><circle cx='245' cy='285' r='12'/>
</g>
<g fill='#ffffff' stroke='#333' stroke-width='1.5'>
<rect x='36' y='222' width='60' height='24' rx='3'/><rect x='101' y='222' width='60' height='24' rx='3'/><rect x='166' y='222' width='60' height='24' rx='3'/><rect x='231' y='222' width='60' height='24' rx='3'/>
</g>
<g font-size='12' font-weight='bold' fill='#b5302a' text-anchor='middle'>
<text x='66' y='239'>Ukraine</text><text x='131' y='239'>Sudan</text><text x='196' y='239'>Gaza</text><text x='261' y='239'>Syrien</text>
</g>
<rect x='20' y='408' width='420' height='44' rx='6' fill='#ffffff' stroke='#b5302a' stroke-width='2'/>
<text x='230' y='426' text-anchor='middle' font-size='13' fill='#333'>Bitte warten! Ihr Anliegen wird bearbeitet,</text>
<text x='230' y='444' text-anchor='middle' font-size='13' fill='#333'>sobald alle fünf Schlösser offen sind.</text>
<text x='740' y='450' text-anchor='end' font-size='12' fill='#999999'>Feibitur 2026</text>
</svg>"""

BEZUG = "Q3.1, insbesondere Analyse eines aktuellen Konflikts vor dem Hintergrund einer differenzierten Staatenwelt und unterschiedlicher Konfliktarten (Bürgerkrieg, zwischenstaatlicher Krieg, Terrorismus und hybride Kriegsführung) samt Folgen; Ziele und Strategien deutscher Außen- und Sicherheitspolitik; kollektive Konfliktbearbeitung (UN inkl. UN-Charta, NATO)."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Krieg ohne Kriegserklärung“ (2026)",
        "absaetze": [
            "Im August 2024 wurde die Deutsche Flugsicherung Ziel eines Cyberangriffs. Kaum jemand nahm davon Notiz. Erst im Dezember 2025 erklärte die Bundesregierung, der Angriff gehe auf das Konto der Hackergruppe APT28, hinter der sie den russischen Militärgeheimdienst GRU sieht. Zugleich ordnete sie eine Desinformationskampagne namens „Storm-1516“, mit der die Bundestagswahl im Februar 2025 beeinflusst werden sollte, russischen Akteuren zu. Der russische Botschafter wurde einbestellt. Sechzehn Monate von der Tat bis zur Zuordnung – das allein zeigt, wie dieser Konflikt funktioniert.",
            "Wir befinden uns nicht im Krieg mit Russland. Aber Russland führt gegen uns einen Konflikt, der kein Krieg sein soll: Cyberangriffe, gefälschte Nachrichtenseiten, Drohnenflüge über Kasernen und Industrieanlagen, Sabotageversuche und Spionage. In der Ostsee wurden wiederholt Unterseekabel beschädigt; Ermittler verdächtigen Schiffe der sogenannten Schattenflotte, beweisen lässt sich wenig. Das ist kein Zufall, sondern Methode: Jede einzelne Tat bleibt so klein und so schwer zuzuordnen, dass niemand den Bündnisfall ausrufen kann.",
            "Im September 2025 wurde diese Grauzone für alle sichtbar. Fast zwanzig russische Drohnen drangen in den polnischen Luftraum ein, NATO-Kampfflugzeuge schossen einige von ihnen ab. Polen beantragte Konsultationen nach Artikel 4 des NATO-Vertrags, gut eine Woche später auch Estland, nachdem russische Kampfjets seinen Luftraum verletzt hatten. Die NATO reagierte mit der Operation „Eastern Sentry“ und verstärkte ihre Luftverteidigung im Osten. Den Bündnisfall nach Artikel 5 rief niemand aus – und genau darauf setzt Moskau.",
            "Unser Völkerrecht und unsere Bündnisverträge kennen im Kern zwei Zustände: Frieden oder bewaffneter Angriff. Die hybride Kriegsführung lebt davon, dass sie dazwischen operiert. Sie nutzt die Stärken offener Gesellschaften – freie Medien, offene Netze, einen Rechtsstaat, der Beweise verlangt – als Schwachstellen. Wer in jedem Fall erst nach gerichtsfesten Beweisen reagiert, reagiert zu spät.",
            "Deutschland hat inzwischen einiges getan. Der Nationale Sicherheitsrat, den die Bundesregierung 2025 eingerichtet hat, beschloss einen Aktionsplan gegen hybride Bedrohungen; kritische Infrastruktur soll besser geschützt, die Bundeswehr personell verstärkt werden. Doch Widerstandsfähigkeit allein reicht nicht. Wer sich nur verteidigt, lädt den Angreifer ein, es immer wieder zu versuchen.",
            "Ich plädiere deshalb für zwei Schritte. Erstens muss die NATO öffentlich festlegen, ab welcher Schwelle hybride Angriffe – etwa die Lahmlegung eines Stromnetzes oder Sabotage mit Todesopfern – als bewaffneter Angriff im Sinne von Artikel 5 gelten. Zweitens muss Deutschland die rechtlichen und technischen Voraussetzungen schaffen, um auf schwere Cyberangriffe auch mit eigenen offensiven Gegenmaßnahmen zu antworten, statt nur Botschafter einzubestellen. Abschreckung entsteht nur, wenn der Angreifer einen Preis zahlt.",
            "Natürlich birgt das Risiken. Russland ist eine Atommacht, und jede Eskalation muss bedacht sein. Aber die größere Gefahr liegt darin, dass wir uns an den Dauerzustand gewöhnen – und erst merken, dass wir in einem Konflikt stehen, wenn er längst entschieden ist.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Sicherheitsexperten (2026). Die genannten Ereignisse sind real: Auswärtiges Amt, Regierungspressekonferenz vom 12.12.2025 (Attribution); NATO, Operation Eastern Sentry (September 2025).",
    },
    {
        "id": "m2",
        "titel": "M2: Militärausgaben ausgewählter Staaten 2025",
        "typ": "tabelle",
        "kopf": ["Staat (Rang 2025)", "Ausgaben 2025 in Mrd. US-$", "Veränderung 2024–2025 (real, in %)", "Anteil am BIP 2016 (in %)", "Anteil am BIP 2025 (in %)"],
        "zeilen": [
            ["USA (1)", "954", "–7,5", "3,4", "3,1"],
            ["China (2)", "[336]", "+7,4", "[1,7]", "[1,7]"],
            ["Russland (3)", "[190]", "+5,9", "[5,4]", "[7,5]"],
            ["Deutschland (4)", "114", "+24", "1,1", "2,3"],
            ["Vereinigtes Königreich (6)", "89,0", "–2,0", "2,0", "2,4"],
            ["Ukraine (7)", "[84,1]", "+20", "[3,7]", "[40]"],
            ["Frankreich (9)", "68,0", "+1,5", "1,9", "2,0"],
            ["Polen (14)", "46,8", "+23", "1,9", "4,5"],
            ["Welt insgesamt", "2.887", "+2,9", "2,2", "2,5"],
        ],
        "quelle": "Quelle: SIPRI Fact Sheet „Trends in World Military Expenditure, 2025“ (April 2026), Tabelle 1. [ ] = Schätzung von SIPRI; Ausgaben in laufenden US-Dollar, Veränderung inflationsbereinigt. Zum Vergleich: Beim NATO-Gipfel in Den Haag (Juni 2025) vereinbarten die Verbündeten, bis 2035 jährlich 5 % des BIP für Verteidigung und Sicherheit aufzuwenden, davon mindestens 3,5 % für die Kernverteidigung; Deutschland strebt 3,5 % bereits bis 2029 an.",
    },
    {
        "id": "m3",
        "typ": "bild",
        "titel": "M3: Karikatur „Bitte warten“ (2026)",
        "svg": SVG_KARIKATUR,
        "beschreibung": "Die Karikatur zeigt rechts eine große, verschlossene Tür in einem braunen Rahmen. Auf einem dunkelblauen Schild an der Tür steht 'KAPITEL VII – Maßnahmen bei Bedrohung des Friedens'. Untereinander hängen an der Tür fünf goldene Vorhängeschlösser mit den Aufschriften 'CN', 'FR', 'RU', 'UK' und 'US'. Rechts oben hängt eine Wanduhr. Vor der Tür steht ein Mann im blauen Anzug mit der Aufschrift 'UN' auf der Brust; er hält einen Schlüsselbund an die Tür und schwitzt (Schweißtropfen an der Stirn). In einer Sprechblase sagt er: 'Einer sagt immer Nein …'. Links unter dem Schild 'WARTEBEREICH' stehen vier Menschen in einer Reihe und halten Schilder mit den Aufschriften 'Ukraine', 'Sudan', 'Gaza' und 'Syrien' hoch. An der Wand hängt eine Plakette 'In Betrieb seit 1945'. Unten links steht auf einem rot umrandeten Hinweisschild: 'Bitte warten! Ihr Anliegen wird bearbeitet, sobald alle fünf Schlösser offen sind.'",
        "quelle": "Übungsmaterial: eigene Zeichnung für Feibitur (2026).",
    },
]

AUFGABEN = [
    {
        "id": "q3-1-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung: Kommentar „Krieg ohne Kriegserklärung“ eines (fiktiven) Sicherheitsexperten aus dem Jahr 2026; Thema: hybride Angriffe Russlands auf Deutschland und Europa und die Frage nach einer angemessenen Reaktion.",
            "punkte": [
                "Der Cyberangriff auf die Deutsche Flugsicherung (August 2024) und die Desinformationskampagne „Storm-1516“ zur Bundestagswahl 2025 seien erst im Dezember 2025 von der Bundesregierung Russland (APT28/GRU) zugeordnet worden; der Botschafter sei einbestellt worden. Die lange Zeit bis zur Zuordnung zeige die Funktionsweise des Konflikts [1].",
                "Russland führe einen Konflikt unterhalb der Kriegsschwelle (Cyberangriffe, gefälschte Nachrichtenseiten, Drohnen, Sabotage, Spionage, beschädigte Ostseekabel); die einzelnen Taten blieben bewusst klein und schwer zuzuordnen, damit kein Bündnisfall ausgerufen werde [2].",
                "Im September 2025 seien Drohnen in den polnischen und Kampfjets in den estnischen Luftraum eingedrungen; beide Staaten hätten Konsultationen nach Art. 4 beantragt, die NATO habe „Eastern Sentry“ gestartet, den Bündnisfall aber nicht ausgerufen [3].",
                "Hybride Kriegsführung operiere zwischen Frieden und bewaffnetem Angriff und nutze die Stärken offener Gesellschaften als Schwachstellen; wer erst nach gerichtsfesten Beweisen reagiere, reagiere zu spät [4].",
                "Deutsche Maßnahmen (Nationaler Sicherheitsrat, Aktionsplan, Schutz kritischer Infrastruktur, mehr Personal für die Bundeswehr) reichten nicht aus, weil bloße Verteidigung den Angreifer ermutige [5].",
                "Forderungen: Die NATO solle eine Schwelle festlegen, ab der hybride Angriffe als bewaffneter Angriff nach Art. 5 gelten; Deutschland solle offensive Gegenmaßnahmen gegen schwere Cyberangriffe ermöglichen [6]. Das Eskalationsrisiko gegenüber einer Atommacht wird eingeräumt, die Gewöhnung an den Dauerzustand aber als größere Gefahr bezeichnet [7].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache, keine Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen des Kommentars weitgehend vollständig, strukturiert, komprimiert und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q3-1-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Karikatur. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Formale Angaben: Karikatur „Bitte warten“, eigene Zeichnung für Feibitur, 2026.",
                "Rechts: große, verschlossene Tür mit dem Schild „KAPITEL VII – Maßnahmen bei Bedrohung des Friedens“; daran fünf Vorhängeschlösser mit den Kürzeln CN, FR, RU, UK und US; Wanduhr rechts oben.",
                "Vor der Tür: schwitzender Mann mit der Aufschrift „UN“, der mit einem Schlüssel versucht, die Tür zu öffnen; Sprechblase „Einer sagt immer Nein …“.",
                "Links: Schild „WARTEBEREICH“; vier wartende Menschen mit Schildern „Ukraine“, „Sudan“, „Gaza“ und „Syrien“.",
                "Plakette „In Betrieb seit 1945“; Hinweisschild unten: „Bitte warten! Ihr Anliegen wird bearbeitet, sobald alle fünf Schlösser offen sind.“",
                "Strukturierte Beschreibung des Bildaufbaus (z. B. von rechts nach links oder vom Zentrum zu den Rändern).",
            ],
            "hinweis": "Beschreiben: nur das Sichtbare strukturiert und fachsprachlich darlegen, noch keine Deutung (z. B. die Kürzel noch nicht ausführlich als Vetomächte interpretieren; eine kurze Benennung ist zulässig).",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Bildelemente im Ansatz korrekt beschrieben werden.",
            "gut": "die Karikatur vollständig, strukturiert und präzise beschrieben wird, ohne vorzeitig zu deuten.",
        },
    },
    {
        "id": "q3-1-i3",
        "afb": "I",
        "operator": "darstellen",
        "text": "Stellen Sie die in M2 aufgeführten Militärausgaben ausgewählter Staaten dar.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle mit Daten des Stockholmer Friedensforschungsinstituts SIPRI (Fact Sheet April 2026) zu Militärausgaben 2025, ihrer Veränderung gegenüber 2024 und ihrem Anteil am BIP (2016 und 2025); einige Werte sind Schätzungen.",
            "punkte": [
                "Weltweit stiegen die Militärausgaben 2025 real um 2,9 % auf 2.887 Mrd. US-$; der Anteil am Welt-BIP wuchs von 2,2 % (2016) auf 2,5 %.",
                "Die USA geben mit 954 Mrd. US-$ mit Abstand am meisten aus, ihre Ausgaben sanken aber um 7,5 %; ihr BIP-Anteil fiel von 3,4 % auf 3,1 %. China folgt mit geschätzt 336 Mrd. US-$ (+7,4 %, konstant rund 1,7 % des BIP).",
                "Russland steigerte seine Ausgaben auf geschätzt 190 Mrd. US-$ (+5,9 %); der BIP-Anteil stieg von 5,4 % auf 7,5 %. Die Ukraine gibt geschätzt 84,1 Mrd. US-$ aus (+20 %) – rund 40 % ihres BIP gegenüber 3,7 % im Jahr 2016.",
                "Deutschland liegt mit 114 Mrd. US-$ auf Rang 4; die Ausgaben stiegen um 24 %, der BIP-Anteil von 1,1 % auf 2,3 %.",
                "Weitere europäische Staaten: Polen mit dem höchsten Zuwachs unter den aufgeführten NATO-Staaten (+23 %, 4,5 % des BIP), Frankreich (+1,5 %, 2,0 %), Vereinigtes Königreich (–2,0 %, 2,4 %).",
                "Einordnung der Bezugsgröße: NATO-Ziel von Den Haag (5 % bis 2035, davon mindestens 3,5 % Kernverteidigung) laut Quellenangabe.",
            ],
            "hinweis": "Darstellen: Daten strukturiert und mit Bezügen (z. B. Rangfolge, Entwicklung, BIP-Anteile) aufzeigen, korrekte Einheiten verwenden; Schätzwerte als solche kennzeichnen; noch keine Erklärung oder Bewertung.",
        },
        "bewertung": {
            "ausreichend": "zentrale Daten ansatzweise zutreffend und mit Bezug zu M2 dargestellt werden.",
            "gut": "die Daten strukturiert, präzise (Einheiten, Schätzwerte, Zeitvergleich) und mit Blick auf zentrale Zusammenhänge dargestellt werden.",
        },
    },
    {
        "id": "q3-1-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 Merkmale und Ziele hybrider Kriegsführung sowie die Schwierigkeiten der NATO, darauf zu reagieren.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Begriff: Kombination militärischer und nichtmilitärischer Mittel, häufig verdeckt und unterhalb der Schwelle eines bewaffneten Angriffs; Verschwimmen der Grenze zwischen Krieg und Frieden.",
                "Instrumente mit Beispielen aus M1 und Fachwissen: Cyberangriffe (Deutsche Flugsicherung 2024), Desinformation („Storm-1516“ zur Bundestagswahl 2025), Drohnenflüge, Sabotage und Spionage, beschädigte Unterseekabel [1]–[3]; weitere Beispiele etwa Soldaten ohne Hoheitsabzeichen auf der Krim 2014 oder die Instrumentalisierung von Migration durch Belarus 2021.",
                "Ziele: Verunsicherung und Spaltung der Gesellschaft, Schwächung des Vertrauens in Institutionen und Wahlen, Schwächung der Unterstützung für die Ukraine, Austesten der Reaktionsfähigkeit von NATO und EU, Kosten verursachen bei geringem eigenem Risiko.",
                "Logik der Grauzone: Abstreitbarkeit, schwierige Attribution (16 Monate im Fall der Flugsicherung), Ausnutzung offener Gesellschaften [4].",
                "Schwierigkeiten der NATO: Art. 5 setzt einen „bewaffneten Angriff“ voraus; Feststellung des Bündnisfalls im Konsens; jeder Staat entscheidet selbst über Art des Beistands; Art. 4 nur Konsultation [3]. Die NATO erklärte 2016/2018, dass auch hybride Angriffe den Bündnisfall auslösen können, ließ die Schwelle aber offen.",
                "Dilemma: Überreaktion birgt Eskalationsrisiko gegenüber einer Atommacht, Unterreaktion schwächt die Abschreckung; Antworten bisher v. a. Resilienz (Eastern Sentry, Baltic Sentry, Schutz kritischer Infrastruktur, Aktionsplan des Nationalen Sicherheitsrats) [3], [5].",
            ],
            "hinweis": "Erläutern verlangt Veranschaulichung durch zusätzliche Informationen und Beispiele; bloßes Wiedergeben von M1 genügt nicht. Bezug zum Erlass-Schwerpunkt „hybride Kriegsführung“ und zu Art. 4/5 NATO-Vertrag erwartet.",
        },
        "bewertung": {
            "ausreichend": "Merkmale und Ziele hybrider Kriegsführung sowie Reaktionsprobleme der NATO ansatzweise erläutert und mit Beispielen belegt werden.",
            "gut": "Merkmale, Ziele und Reaktionsprobleme differenziert, mit Bezug auf Art. 4/5 NATO-Vertrag, Attributionsproblematik und passenden Beispielen aus M1 und Fachwissen erläutert werden.",
        },
    },
    {
        "id": "q3-1-ii2",
        "afb": "II",
        "operator": "anwenden",
        "text": "Wenden Sie das Modell der Konfliktanalyse auf den Bürgerkrieg im Sudan an.",
        "material": [],
        "loesung": {
            "vorbemerkung": "Erwartet wird eine kategoriengeleitete Analyse; die Kategorien können auch anders benannt werden, wenn sie gleichwertig sind.",
            "punkte": [
                "Konfliktgegenstand und Ursachen: Machtkampf um die Kontrolle des Staates, um Ressourcen (u. a. Gold) und Einfluss; Hintergrund: gescheiterter Übergang nach dem Sturz al-Baschirs (2019), gemeinsamer Putsch von Armee und RSF 2021, Streit über die Eingliederung der RSF in die Armee; Kriegsbeginn am 15. April 2023.",
                "Akteure: sudanesische Armee (SAF, General al-Burhan) und Rapid Support Forces (RSF, Daglo/„Hemeti“) mit verbündeten Milizen; externe Unterstützer beider Seiten laut UN-Berichten und Medien (Vorwürfe teils bestritten); Vermittler (u. a. „Quad“ aus USA, Saudi-Arabien, VAE, Ägypten; Afrikanische Union); UN-Hilfsorganisationen.",
                "Konfliktart und Staatenwelt: innerstaatlicher, zunehmend internationalisierter Bürgerkrieg; Sudan als failing state mit zwei rivalisierenden Machtzentren (Regierung in Port Sudan, von der RSF-Allianz ausgerufene Gegenregierung in Nyala); Merkmale „neuer Kriege“ (Milizen, Kriegsökonomie, Gewalt gegen Zivilisten).",
                "Verlauf und Intensität: Krieg höchster Intensität seit 2023; Eroberung El Faschers durch die RSF im Oktober 2025 nach 18-monatiger Belagerung; Waffenruhen bislang gescheitert.",
                "Folgen: laut UNHCR Ende 2025 9,1 Mio. Binnenvertriebene (weltweit höchste Zahl) und 2,8 Mio. Flüchtlinge (v. a. Tschad, Südsudan, Libyen, Ägypten); Hunger, Massengewalt in Darfur; Destabilisierung der Nachbarstaaten.",
                "Konfliktbearbeitung: Vermittlungsinitiativen ohne Durchbruch; Sicherheitsrat blockiert (russisches Veto gegen Waffenruhe-Resolution im November 2024); humanitäre Hilfe unterfinanziert; Strafverfolgung durch den IStGH (Darfur-Situation; Verurteilung eines früheren Milizenführers 2025).",
                "Bewertung/Perspektiven: geringe internationale Aufmerksamkeit („vergessene Krise“), Interessen externer Akteure, Fragmentierung des Staates erschweren eine Lösung.",
            ],
            "hinweis": "Anwenden: Das bekannte Analysemodell muss erkennbar auf den neuen Fall übertragen werden. Konkrete Fakten (mit ungefährer Zeitangabe) sind zu erwarten; exakte Zahlen sind nicht zwingend, Größenordnungen sollten stimmen.",
        },
        "bewertung": {
            "ausreichend": "das Modell ansatzweise auf den Sudan-Konflikt angewendet wird und einige Kategorien mit zutreffenden Fakten gefüllt werden.",
            "gut": "das Modell vollständig, kategoriengeleitet und mit präzisen Fakten (Akteure, Konfliktart, Staatszerfall, Folgen wie Flucht und Vertreibung, Bearbeitung) auf den Sudan-Konflikt angewendet wird.",
        },
    },
    {
        "id": "q3-1-ii3",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Karikatur (M3) im Hinblick auf ihre Aussage zu den Möglichkeiten und Grenzen kollektiver Konfliktbearbeitung durch die Vereinten Nationen.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Tür „Kapitel VII“: Zwangsmaßnahmen der UN (Art. 39, 41, 42 UN-Charta) als schärfstes Instrument kollektiver Sicherheit; nur der Sicherheitsrat kann sie verbindlich beschließen (Art. 24, 25).",
                "Fünf Schlösser CN, FR, RU, UK, US: die ständigen Mitglieder mit Vetorecht (Art. 23, Art. 27 Abs. 3); jedes kann die Tür allein verschlossen halten – Sprechblase „Einer sagt immer Nein …“.",
                "Schwitzende UN-Figur mit Schlüssel: Generalsekretär bzw. UN als Organisation, die handeln will, aber von den Mitgliedstaaten abhängt; keine eigene Macht, keine eigenen Truppen.",
                "Wartende mit Schildern: Konflikte, in denen der Sicherheitsrat blockiert war oder ist – Ukraine (russisches Veto 2022), Sudan (russisches Veto 2024), Gaza (mehrere US-Vetos), Syrien (zahlreiche russische und chinesische Vetos); Hinweis, dass Vetos von verschiedenen Großmächten ausgehen.",
                "„In Betrieb seit 1945“, Uhr, „Wartebereich“: veraltete Struktur, Zeitverlust, Ohnmacht der Betroffenen; Kritik an mangelnder Reformfähigkeit.",
                "Kernaussage: Das System kollektiver Sicherheit ist durch das Veto der Großmächte strukturell blockiert, gerade wenn deren Interessen berührt sind. Ausgeblendet werden Möglichkeiten wie Generalversammlung („Uniting for Peace“, Veto-Initiative 2022), humanitäre Hilfe, Vermittlung und erfolgreiche Missionen.",
            ],
            "hinweis": "Analysieren: Bildelemente systematisch deuten, mit Fachwissen (UN-Charta-Artikel, Beispiele) verknüpfen und eine Kernaussage formulieren; Bildbelege angeben.",
        },
        "bewertung": {
            "ausreichend": "zentrale Bildelemente ansatzweise zutreffend gedeutet und eine Kernaussage formuliert wird.",
            "gut": "die Bildelemente systematisch und mit Bezug auf die UN-Charta sowie konkrete Konflikte gedeutet werden und eine präzise Kernaussage einschließlich ausgeblendeter Aspekte formuliert wird.",
        },
    },
    {
        "id": "q3-1-ii4",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M2 Ziele und Strategien der deutschen Außen- und Sicherheitspolitik seit der „Zeitenwende“.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Ausgangspunkt M2: deutliche Steigerung der deutschen Militärausgaben (+24 % 2025, BIP-Anteil von 1,1 % 2016 auf 2,3 % 2025) im Kontext russischer Aufrüstung (7,5 % des BIP) und des Krieges gegen die Ukraine.",
                "Zeitenwende (Rede von Olaf Scholz am 27.2.2022): Sondervermögen Bundeswehr bis zu 100 Mrd. Euro (Art. 87a Abs. 1a GG); Grundgesetzänderung 2025: Verteidigungsausgaben über 1 % des BIP von der Schuldenbremse ausgenommen (Art. 115 Abs. 2 GG); Ziel 3,5 % des BIP bis 2029, NATO-Ziel 5 % bis 2035.",
                "Ziele laut Nationaler Sicherheitsstrategie 2023 (integrierte Sicherheit): wehrhaft (Landes- und Bündnisverteidigung, Abschreckung Russlands), resilient (Schutz vor hybriden Bedrohungen, kritische Infrastruktur, Energieunabhängigkeit), nachhaltig (Klima, Ernährung, Gesundheit).",
                "Strategien/Instrumente: Stärkung der NATO-Ostflanke (Brigade in Litauen), Unterstützung der Ukraine (Waffen, Finanzhilfe, Sanktionen im EU-Rahmen, Aufnahme Geflüchteter), neuer Wehrdienst seit 1.1.2026, Nationaler Sicherheitsrat; daneben zivile Instrumente (Diplomatie, Krisenprävention, Entwicklungszusammenarbeit, humanitäre Hilfe).",
                "Rahmenbedingungen: Multilateralismus und Einbindung (UN, NATO, EU), Parlamentsarmee, Art. 26 GG; Wandel vom Selbstverständnis als „Zivilmacht“ zur stärkeren Betonung militärischer Fähigkeiten; Unsicherheit über die Verlässlichkeit der USA.",
            ],
            "hinweis": "Erläutern: Ziele und Strategien mit Beispielen und zusätzlichen Informationen veranschaulichen; Materialbezug zu M2 ist erforderlich, ebenso Fachwissen über die Daten hinaus.",
        },
        "bewertung": {
            "ausreichend": "einige Ziele und Strategien deutscher Sicherheitspolitik ansatzweise mit Beispielen und Bezug zu M2 erläutert werden.",
            "gut": "Ziele und Strategien differenziert, fachlich präzise (Nationale Sicherheitsstrategie, Sondervermögen, Grundgesetzänderung, Bündnisverpflichtungen) und mit durchgängigem Bezug zu M2 erläutert werden.",
        },
    },
    {
        "id": "q3-1-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie die Forderungen des Autors, für hybride Angriffe eine klare Bündnisfall-Schwelle festzulegen und auf schwere Cyberangriffe mit eigenen offensiven Gegenmaßnahmen zu antworten. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Pro: Abschreckung durch klare rote Linien und Kosten für den Angreifer; Schließen der Grauzone, die der Angreifer bewusst nutzt [2]–[4]; Stärkung der Glaubwürdigkeit der NATO; Schutz kritischer Infrastruktur und demokratischer Wahlen; bloße Resilienz und Einbestellungen wirken kaum [5], [6].",
                "Contra Schwelle: Eine öffentliche Schwelle lädt dazu ein, knapp darunter zu bleiben; strategische Mehrdeutigkeit kann abschreckender sein; Gefahr eines Automatismus und der Eskalation mit einer Atommacht [7]; Konsensprinzip in der NATO; Attribution bleibt schwierig.",
                "Contra offensive Gegenmaßnahmen: völker- und verfassungsrechtliche Fragen (Gewaltverbot, Verhältnismäßigkeit, Parlamentsvorbehalt, Zuständigkeiten), Gefahr von Fehlzuordnung und Kollateralschäden in zivilen Netzen, Eskalationsspirale, Legitimitätsverlust des Rechtsstaats.",
                "Alternativen/Differenzierungen: schnellere und öffentliche Attribution, gezielte EU-Sanktionen, Ausweisung von Agenten, Stärkung der Cyberabwehr, gemeinsame NATO-Reaktionsoptionen unterhalb von Art. 5, Medienkompetenz.",
                "Abwägung nach Kriterien (Sicherheit/Abschreckung, Rechtmäßigkeit, Eskalationsrisiko, Wirksamkeit) und begründetes eigenes Urteil; beide Ergebnisse oder ein differenziertes Urteil (z. B. ja zu besserer Attribution und Sanktionen, nein zu einer starren Schwelle) sind möglich.",
            ],
            "hinweis": "Erörtern verlangt das Abwägen von Pro- und Contra-Argumenten zu beiden Forderungen [6] und ein eigenes, begründetes Urteil. Fachbezüge zu Art. 51 UN-Charta und Art. 4/5 NATO-Vertrag stärken die Leistung.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist, Pro- und Contra-Argumente enthält und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, kriteriengeleitet und weitgehend kohärent ist, beide Forderungen fachlich fundiert prüft und in ein schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q3-1-iii2",
        "afb": "III",
        "operator": "Stellung nehmen",
        "text": "Nehmen Sie Stellung zu der Frage, ob Deutschland seine Verteidigungsausgaben – wie von der Bundesregierung angestrebt – bis 2029 auf 3,5 % des BIP erhöhen sollte. (M2)",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Pro: Bedrohung durch Russland (Militärausgaben 7,5 % des BIP, Angriffskrieg, hybride Angriffe); Bündnisverpflichtungen (NATO-Ziel Den Haag); Nachholbedarf nach Jahrzehnten niedriger Ausgaben (1,1 % 2016); unsichere Verlässlichkeit der USA; Unterstützung der Ukraine; Abschreckung verhindert Krieg; Vorbilder wie Polen (4,5 %).",
                "Contra: Opportunitätskosten (Bildung, Soziales, Klimaschutz, Entwicklung); steigende Schulden durch Ausnahme von der Schuldenbremse; Effizienz der Beschaffung fraglich (Geld allein schafft keine Fähigkeiten); Gefahr eines Rüstungswettlaufs (Sicherheitsdilemma); europäische Staaten geben zusammen bereits deutlich mehr aus als Russland; Vorrang für Diplomatie und Rüstungskontrolle.",
                "Differenzierungen: BIP-Quote als Maßstab umstritten (Input statt Fähigkeiten); Unterscheidung Kernverteidigung/sicherheitsrelevante Ausgaben (Infrastruktur, Cyber, Zivilschutz); europäische Kooperation bei der Beschaffung.",
                "Offenlegung der eigenen Wertmaßstäbe (z. B. Vorrang von Sicherheit und Bündnissolidarität oder von sozialer Gerechtigkeit und Generationengerechtigkeit) und begründetes eigenes Urteil.",
            ],
            "hinweis": "Stellung nehmen: wie beurteilen, aber die eigenen Wertmaßstäbe müssen ausdrücklich begründet dargelegt werden. Die Daten aus M2 sollten als Belege genutzt werden.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit erkennbaren eigenen Maßstäben und einzelnen Belegen aus M2 vorliegt.",
            "gut": "die Stellungnahme abwägend und fachlich fundiert ist, Daten aus M2 gezielt nutzt, eigene Wertmaßstäbe ausdrücklich offenlegt und in ein klares, schlüssiges Urteil mündet.",
        },
    },
    {
        "id": "q3-1-iii3",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie ausgehend von M3 Vorschläge zur Reform des UN-Sicherheitsrats.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Kriterien benennen, z. B. Handlungsfähigkeit/Effektivität, Legitimität und Repräsentativität, Realisierbarkeit.",
                "Reformvorschläge: Abschaffung oder Einschränkung des Vetos (z. B. Verzicht bei Massenverbrechen, wie von Frankreich und Mexiko vorgeschlagen; Veto nur gemeinsam mit einem zweiten ständigen Mitglied); Erweiterung um neue ständige Mitglieder (G4: Deutschland, Japan, Indien, Brasilien; afrikanische Staaten) oder um langfristige, wiederwählbare Sitze; Stärkung der Generalversammlung (Veto-Initiative 2022, „Uniting for Peace“).",
                "Für Reformen spricht: Blockaden in zentralen Konflikten (Ukraine, Sudan, Gaza, Syrien – M3); Zusammensetzung von 1945 („In Betrieb seit 1945“); Legitimitätsdefizit, besonders aus Sicht Afrikas und des Globalen Südens.",
                "Gegen bzw. Grenzen: Charta-Änderung braucht nach Art. 108 die Ratifikation durch alle ständigen Mitglieder – diese müssten auf Macht verzichten; mehr Mitglieder können neue Blockaden erzeugen; ohne Großmächte keine Durchsetzung (Veto als „Sicherheitsventil“, das deren Verbleib in der UN sichert); regionale Rivalitäten (z. B. um einen deutschen Sitz – Wahlniederlage Deutschlands für 2027/28 im Juni 2026).",
                "Begründetes Urteil, z. B.: Reform notwendig, aber kurzfristig unrealistisch; realistischer sind Selbstbeschränkungen beim Veto und eine Aufwertung der Generalversammlung.",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete, begründete Einschätzung auf Basis von Fachwissen; Bezug zur Aussage der Karikatur erwartet. Die Kenntnis von Art. 108 ist ein Plus, aber nicht zwingend.",
        },
        "bewertung": {
            "ausreichend": "mindestens ein Reformvorschlag ansatzweise kriteriengeleitet beurteilt und ein nachvollziehbares Urteil formuliert wird.",
            "gut": "mehrere Reformvorschläge kriteriengeleitet, fachlich fundiert (UN-Charta, aktuelle Beispiele) und mit Bezug zu M3 beurteilt werden und ein schlüssig begründetes Urteil vorliegt.",
        },
    },
    {
        "id": "q3-1-iii4",
        "afb": "III",
        "operator": "überprüfen",
        "lk": True,
        "text": "Überprüfen Sie, inwieweit der Realismus und der Institutionalismus die in M2 dokumentierte Entwicklung der Militärausgaben erklären können.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Realismus/Neorealismus: Anarchie, Selbsthilfe, Machtgleichgewicht; Aufrüstung Russlands und Reaktion der europäischen Staaten (Deutschland +24 %, Polen +23 %, BIP-Anteile steigen) als Balancing und Sicherheitsdilemma; Ukraine (40 % des BIP) als Existenzkampf; Wirkung von Machtverschiebungen (China +7,4 %).",
                "Grenzen des Realismus: Rückgang der US-Ausgaben (–7,5 %) trotz Großmachtkonkurrenz erklärt er nur bedingt (innenpolitische Entscheidungen, Wegfall von Ukraine-Hilfen); Rolle von Bündnisverpflichtungen und Normen wird unterschätzt.",
                "Institutionalismus: NATO als Institution koordiniert die Aufrüstung (5-%-Ziel von Den Haag, Fähigkeitsziele), schafft Transparenz und Lastenteilung; Ausgabensteigerung als Erfüllung institutioneller Verpflichtungen; Europa reagiert gemeinsam statt nur national.",
                "Grenzen des Institutionalismus: Institutionen (Budapester Memorandum, OSZE, Rüstungskontrollverträge) haben den Krieg nicht verhindert; Spanien und andere erfüllen Ziele zögerlich; Aufrüstung zeigt eher das Versagen kooperativer Sicherheit mit Russland.",
                "Vergleichendes Fazit, z. B.: Der Realismus erklärt das Motiv (Bedrohungswahrnehmung), der Institutionalismus die Form (koordinierte Ziele im Bündnis); ggf. Ergänzung durch Liberalismus/Konstruktivismus (Innenpolitik, Bedrohungswahrnehmung).",
            ],
            "hinweis": "Überprüfen: die Erklärungskraft beider Theorien anhand der Daten aus M2 kritisch hinterfragen und begründet einschätzen; eine bloße Darstellung der Theorien genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "beide Theorien ansatzweise zutreffend auf Daten aus M2 bezogen werden und eine nachvollziehbare Einschätzung ihrer Erklärungskraft vorliegt.",
            "gut": "beide Theorien präzise auf die Daten aus M2 angewendet, Stärken und Grenzen ihrer Erklärungskraft abgewogen und ein schlüssig begründetes Fazit gezogen wird.",
        },
    },
]
