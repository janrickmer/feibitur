# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q2.1 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q2.1, insbesondere Grundlagen der keynesianischen Konzeption (Krisenanalyse, effektive Gesamtnachfrage, Rolle des Staates, Multiplikatoreffekt), Analyse der Konjunktur mit Konjunkturindikatoren sowie Probleme und Kontroversen nachfrageorientierter Fiskalpolitik (insbesondere Inflation sowie Staatsverschuldung)."

SVG_KARIKATUR = """<svg viewBox='0 0 760 440' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='q21kt'>
<title id='q21kt'>Karikatur Gas und Bremse zugleich: Ein Auto namens Konjunktur mit einem Anhänger voller Staatsschulden; der Staat gibt Gas, die EZB zieht die Handbremse, vorne steht ein Warnschild Inflation.</title>
<rect x='0' y='0' width='760' height='440' fill='#fffdf6'/>
<rect x='0' y='345' width='760' height='50' fill='#c8c8c8'/>
<line x1='0' y1='370' x2='760' y2='370' stroke='#ffffff' stroke-width='4' stroke-dasharray='24 16'/>
<rect x='55' y='214' width='55' height='34' fill='#d9a400' stroke='#6a4b00'/>
<rect x='118' y='214' width='55' height='34' fill='#d9a400' stroke='#6a4b00'/>
<rect x='181' y='214' width='55' height='34' fill='#d9a400' stroke='#6a4b00'/>
<g font-size='12' font-weight='bold' fill='#3a2a00' text-anchor='middle'>
<text x='82' y='236'>Kredit</text><text x='145' y='236'>Kredit</text><text x='208' y='236'>Kredit</text>
</g>
<rect x='40' y='248' width='210' height='70' rx='6' fill='#b5302a'/>
<text x='145' y='280' text-anchor='middle' font-size='15' font-weight='bold' fill='#ffffff'>STAATSSCHULDEN</text>
<text x='145' y='303' text-anchor='middle' font-size='13' fill='#ffe9e6'>+ Zinslast</text>
<circle cx='145' cy='330' r='22' fill='#333333'/><circle cx='145' cy='330' r='8' fill='#999999'/>
<line x1='250' y1='300' x2='282' y2='300' stroke='#333333' stroke-width='6'/>
<path d='M332 255 L372 195 L500 195 L542 255 Z' fill='#3b5592'/>
<rect x='280' y='255' width='300' height='72' rx='16' fill='#22355e'/>
<polygon points='346,250 378,203 432,203 432,250' fill='#dfe9f7'/>
<polygon points='442,250 442,203 496,203 528,250' fill='#dfe9f7'/>
<circle cx='408' cy='228' r='14' fill='#f2c9a0' stroke='#333333' stroke-width='2'/>
<circle cx='403' cy='224' r='2' fill='#333333'/><circle cx='413' cy='224' r='2' fill='#333333'/>
<path d='M401 236 Q408 230 415 236' fill='none' stroke='#333333' stroke-width='2'/>
<circle cx='470' cy='228' r='14' fill='#f2c9a0' stroke='#333333' stroke-width='2'/>
<circle cx='465' cy='224' r='2' fill='#333333'/><circle cx='475' cy='224' r='2' fill='#333333'/>
<path d='M462 232 Q470 241 478 232' fill='none' stroke='#333333' stroke-width='2'/>
<text x='430' y='300' text-anchor='middle' font-size='18' font-weight='bold' fill='#ffffff'>KONJUNKTUR</text>
<circle cx='574' cy='275' r='6' fill='#fff7e0'/>
<circle cx='340' cy='330' r='27' fill='#333333'/><circle cx='340' cy='330' r='10' fill='#aaaaaa'/>
<circle cx='520' cy='330' r='27' fill='#333333'/><circle cx='520' cy='330' r='10' fill='#aaaaaa'/>
<line x1='398' y1='236' x2='372' y2='212' stroke='#f2c9a0' stroke-width='6' stroke-linecap='round'/>
<line x1='395' y1='240' x2='330' y2='160' stroke='#b5302a' stroke-width='7' stroke-linecap='round'/>
<circle cx='330' cy='160' r='9' fill='#b5302a'/>
<rect x='160' y='146' width='150' height='28' rx='6' fill='#ffffff' stroke='#b5302a'/>
<text x='235' y='165' text-anchor='middle' font-size='12' font-weight='bold' fill='#b5302a'>Handbremse: Leitzins</text>
<line x1='478' y1='240' x2='566' y2='306' stroke='#14213d' stroke-width='6' stroke-linecap='round'/>
<polygon points='556,308 590,296 597,310 563,322' fill='#d9a400' stroke='#6a4b00'/>
<line x1='580' y1='318' x2='595' y2='358' stroke='#6a4b00' stroke-width='1.5'/>
<rect x='470' y='358' width='250' height='30' rx='6' fill='#ffffff' stroke='#d9a400'/>
<text x='595' y='378' text-anchor='middle' font-size='12' font-weight='bold' fill='#6a4b00'>Gaspedal: Kredite, Sondervermögen</text>
<rect x='686' y='228' width='8' height='118' fill='#777777'/>
<polygon points='690,140 748,232 632,232' fill='#fff7e0' stroke='#b5302a' stroke-width='5'/>
<text x='690' y='196' text-anchor='middle' font-size='26' font-weight='bold' fill='#b5302a'>!</text>
<text x='690' y='222' text-anchor='middle' font-size='12' font-weight='bold' fill='#b5302a'>INFLATION</text>
<rect x='140' y='60' width='250' height='62' rx='14' fill='#ffffff' stroke='#14213d'/>
<polygon points='330,121 352,121 402,212' fill='#ffffff' stroke='#14213d'/>
<text x='265' y='85' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>EZB: Bremsen!</text>
<text x='265' y='107' text-anchor='middle' font-size='13' fill='#14213d'>Die Preise steigen zu stark!</text>
<rect x='420' y='60' width='250' height='62' rx='14' fill='#ffffff' stroke='#14213d'/>
<polygon points='470,121 492,121 472,212' fill='#ffffff' stroke='#14213d'/>
<text x='545' y='85' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>Staat: Vollgas!</text>
<text x='545' y='107' text-anchor='middle' font-size='13' fill='#14213d'>Wir investieren aus der Krise!</text>
<text x='380' y='426' text-anchor='middle' font-size='16' font-weight='bold' fill='#14213d'>„Gas und Bremse zugleich“</text>
</svg>"""

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Wer jetzt bremst, verliert“ (2026)",
        "absaetze": [
            "Endlich wächst die deutsche Wirtschaft wieder. Nach dem Schrumpfen im Jahr 2023, der Stagnation 2024 und einem mageren Plus von 0,2 Prozent im Jahr 2025 lag das Bruttoinlandsprodukt im dritten Quartal 2026 um 1,3 Prozent über dem Vorjahresniveau. Doch zum Jubeln besteht kein Anlass: Im Sommer gingen die Investitionen schon wieder zurück, die Exporte verloren an Schwung, und noch immer sind fast drei Millionen Menschen arbeitslos. Der Energiepreisschock infolge des Kriegs im Nahen Osten belastet Haushalte und Unternehmen.",
            "In dieser Lage ist die Debatte, die in Berlin schon wieder geführt wird, gefährlich. Kaum sind die Kredite für das Sondervermögen Infrastruktur und die höheren Verteidigungsausgaben angelaufen, mehren sich die Stimmen, die eine Rückkehr zu einer strengen Schuldenbremse fordern. Die Geschichte lehrt das Gegenteil: Wer in einer schwachen Konjunktur spart, verschärft die Krise. Reichskanzler Brüning hat das Anfang der 1930er-Jahre vorgeführt, und auch in den USA führte ein zu früher Sparkurs 1937 zurück in die Rezession.",
            "Die Logik ist einfach. Wenn Verbraucher wegen hoher Energiepreise verunsichert sind und Unternehmen ihre Investitionen zurückstellen, fehlt Nachfrage. Diese Lücke kann nur der Staat schließen. Jeder Euro, der in eine sanierte Brücke, ein neues Stromnetz oder eine modernisierte Schule fließt, wird zum Einkommen von Bauarbeiterinnen, Ingenieuren und Zulieferern – und von diesen wieder ausgegeben. So entsteht aus einem Euro staatlicher Investition mehr als ein Euro Wirtschaftsleistung. Zugleich wächst das Produktionspotenzial des Landes.",
            "Die Inflationsangst halte ich für übertrieben. Ja, die Teuerung ist im September auf 3,3 Prozent gestiegen. Aber das liegt an Öl und Gas, deren Preise auf dem Weltmarkt bestimmt werden, nicht an zu viel Nachfrage im Inland. Die Inflationsrate ohne Energie und Nahrungsmittel lag im Oktober bei 2,1 Prozent. Gegen den Preisschock an der Zapfsäule helfen keine Sparhaushalte, sondern Investitionen in erneuerbare Energien und Netze, die uns unabhängiger machen.",
            "Auch das Schuldenargument trägt nicht weit. Die Schuldenstandsquote Deutschlands liegt mit knapp 63 Prozent des Bruttoinlandsprodukts deutlich unter dem Durchschnitt des Euroraums und weit unter dem Niveau von 2010. Gewiss: Die Zinsausgaben des Bundes sollen laut Finanzplan bis 2030 auf rund 80 Milliarden Euro steigen. Doch marode Brücken, langsame Züge und fehlende Netze sind ebenfalls Schulden – nur stehen sie in keinem Haushaltsplan. Wer künftigen Generationen ein funktionierendes Land hinterlassen will, muss heute investieren.",
            "Das eigentliche Problem ist nicht zu viel Geld, sondern zu wenig Tempo. Planungsverfahren dauern Jahre, Baufirmen und Fachkräfte sind knapp, viele bewilligte Mittel fließen nicht ab. Wir brauchen deshalb schnellere Genehmigungen und eine verlässliche Investitionsplanung über 2030 hinaus. Teure Entlastungen mit der Gießkanne wie die erneute Steuersenkung auf Benzin und Diesel sind dagegen ein Strohfeuer. Die Bundesregierung sollte die Schuldenbremse nicht wieder verschärfen, sondern dauerhaft eine Ausnahme für öffentliche Investitionen schaffen.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Wirtschaftswissenschaftlerin (November 2026). Die genannten Daten stammen vom Statistischen Bundesamt, von Eurostat, der Bundesagentur für Arbeit und aus dem Finanzplan des Bundes 2026–2030 (Stand: Oktober 2026).",
    },
    {
        "id": "m2",
        "titel": "M2: Konjunktur- und Finanzdaten Deutschlands in ausgewählten Jahren",
        "typ": "tabelle",
        "kopf": [
            "Jahr",
            "Wachstum des realen BIP (in %)",
            "Inflationsrate (HVPI, in %)",
            "Finanzierungssaldo des Staates (in % des BIP)",
            "Schuldenstand des Staates (in % des BIP)",
        ],
        "zeilen": [
            ["2008", "0,9", "2,8", "−0,3", "65,2"],
            ["2009", "−5,6", "0,2", "−3,2", "72,4"],
            ["2010", "4,1", "1,1", "−4,4", "81,0"],
            ["2019", "1,1", "1,4", "1,3", "58,3"],
            ["2020", "−4,0", "0,4", "−4,3", "67,5"],
            ["2021", "4,0", "3,2", "−3,2", "67,4"],
            ["2022", "1,9", "8,7", "−1,9", "64,1"],
            ["2023", "−1,0", "6,0", "−2,2", "61,8"],
            ["2024", "0,0", "2,5", "−2,7", "61,4"],
            ["2025", "0,2", "2,3", "−2,9", "62,8"],
        ],
        "quelle": "Eurostat (Datenbanken nama_10_gdp, prc_hicp_aind, gov_10dd_edpt1; Datenstand 21./22.10.2026). Finanzierungssaldo: negativer Wert = Defizit. Frühere Veröffentlichungen können wegen Revisionen abweichen. Zum Vergleich 2026: BIP im 3. Quartal +1,3 % gegenüber dem Vorjahresquartal, Inflationsrate (HVPI) im Oktober 2,8 % (vorläufig, Destatis); Schuldenstand im Euroraum 2025: 87,7 % des BIP.",
    },
    {
        "id": "m3",
        "typ": "bild",
        "titel": "M3: Karikatur „Gas und Bremse zugleich“ (2026)",
        "svg": SVG_KARIKATUR,
        "beschreibung": "Die Karikatur zeigt auf einer Straße ein dunkelblaues Auto, auf dessen Karosserie in großen Buchstaben 'KONJUNKTUR' steht. Im Auto sitzen zwei Figuren. Die vordere Figur (Fahrer) grinst und tritt mit dem Bein auf ein gelbes Pedal, das aus dem Auto ragt; ein Schild darunter erklärt: 'Gaspedal: Kredite, Sondervermögen'. Ihre Sprechblase lautet: 'Staat: Vollgas! Wir investieren aus der Krise!'. Die hintere Figur schaut besorgt und zieht an einem großen roten Hebel, der aus dem Dach ragt; das Schild daneben lautet 'Handbremse: Leitzins'. Ihre Sprechblase lautet: 'EZB: Bremsen! Die Preise steigen zu stark!'. Hinten am Auto hängt ein schwerer roter Anhänger mit der Aufschrift 'STAATSSCHULDEN + Zinslast', auf dem drei gelbe Säcke mit der Aufschrift 'Kredit' liegen. Vor dem Auto steht am Straßenrand ein dreieckiges Warnschild mit Ausrufezeichen und der Aufschrift 'INFLATION'. Unter dem Bild steht der Titel 'Gas und Bremse zugleich'.",
        "quelle": "Übungsmaterial: eigene Zeichnung für Feibitur (2026).",
    },
]

AUFGABEN = [
    {
        "id": "q2-1-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Kommentar), Titel „Wer jetzt bremst, verliert“, Erscheinungsjahr (2026), Autorin (fiktive Wirtschaftswissenschaftlerin) und Thema (Fortsetzung kreditfinanzierter Investitionen statt Rückkehr zu einer strengen Schuldenbremse).",
            "punkte": [
                "Die Autorin stellt fest, dass die Wirtschaft nach Schrumpfung (2023), Stagnation (2024) und schwachem Wachstum (2025) wieder wachse (3. Quartal 2026: +1,3 % zum Vorjahr), die Lage aber fragil sei: rückläufige Investitionen, schwächere Exporte, fast drei Millionen Arbeitslose, Energiepreisschock [1].",
                "Forderungen nach einer Rückkehr zu einer strengen Schuldenbremse hält sie für gefährlich; mit Verweis auf Brüning und die US-Rezession 1937 warnt sie vor Sparen in der Schwäche [2].",
                "Sie begründet staatliche Investitionen mit fehlender privater Nachfrage und einem Multiplikatoreffekt; zugleich steige das Produktionspotenzial [3].",
                "Die Inflation sei energiepreisbedingt und nicht nachfragegetrieben (Kerninflation 2,1 %); helfen würden Investitionen in Energie und Netze [4].",
                "Die Schuldenquote (knapp 63 %) sei vergleichsweise niedrig; trotz steigender Zinsausgaben seien unterlassene Investitionen ebenfalls eine Last für künftige Generationen [5].",
                "Das Hauptproblem sei langsame Umsetzung (Planung, Kapazitäten, Fachkräfte); die Kraftstoffsteuersenkung sei ein Strohfeuer; sie fordert eine dauerhafte Ausnahme von der Schuldenbremse für öffentliche Investitionen [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturiert, komprimiert, in eigenen Worten und indirekter Rede; keine eigene Wertung. Zahlen nur, soweit sie die Argumentation tragen.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitungssatz zusammengefasst werden.",
            "gut": "die Aussagen des Kommentars weitgehend vollständig, strukturiert, in eigenen Worten und unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q2-1-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Entwicklung von Wirtschaftswachstum, Inflation und Staatsfinanzen in Deutschland anhand von M2.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle mit Daten von Eurostat zu realem BIP-Wachstum, Inflationsrate (HVPI), Finanzierungssaldo und Schuldenstand des Staates in ausgewählten Jahren 2008–2025.",
            "punkte": [
                "Wachstum: starker Einbruch 2009 (−5,6 %) und 2020 (−4,0 %), jeweils kräftige Erholung im Folgejahr (2010: +4,1 %, 2021: +4,0 %); seit 2023 Schwächephase mit Schrumpfung (−1,0 %), Stagnation (2024: 0,0 %) und geringem Wachstum (2025: +0,2 %).",
                "Inflation: meist zwischen 0 und 3 %; 2009 und 2020 nahe null, deutlicher Anstieg 2021 (3,2 %) mit Höhepunkt 2022 (8,7 %) und 2023 (6,0 %); danach Rückgang auf 2,5 % (2024) und 2,3 % (2025).",
                "Finanzierungssaldo: in Krisenjahren hohe Defizite (2010: −4,4 %, 2020: −4,3 %), 2019 Überschuss (+1,3 %); seit 2022 wieder wachsende Defizite (−1,9 % bis −2,9 %).",
                "Schuldenstand: Anstieg von 65,2 % (2008) auf 81,0 % (2010), Rückgang bis 2019 auf 58,3 %, sprunghafter Anstieg 2020 auf 67,5 %, danach Rückgang auf 61,4 % (2024) und leichter Anstieg auf 62,8 % (2025).",
                "Zusammenhang erkennbar: Krisenjahre gehen mit Defiziten und steigendem Schuldenstand einher; Datenlücke 2011–2018 und Revisionsvorbehalt beachten.",
            ],
            "hinweis": "Beschreiben: Entwicklung strukturiert und fachsprachlich mit konkreten Zahlenbelegen darstellen (Höchst- und Tiefstwerte, Trends); noch keine Erklärung der Ursachen. Methodische Hinweise (Auswahljahre, HVPI statt VPI, Revisionen) werten auf.",
        },
        "bewertung": {
            "ausreichend": "die Entwicklung der vier Größen im Ansatz korrekt und mit einigen Zahlenbelegen beschrieben wird.",
            "gut": "die Entwicklung aller Größen strukturiert, fachsprachlich präzise und mit treffenden Zahlenbelegen (Trends, Extremwerte) beschrieben wird.",
        },
    },
    {
        "id": "q2-1-i3",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Karikatur (M3).",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Formale Angaben: Karikatur „Gas und Bremse zugleich“, eigene Zeichnung für Feibitur, 2026.",
                "Bildmitte: Auto mit der Aufschrift „KONJUNKTUR“ auf einer Straße; zwei Insassen.",
                "Fahrer (Staat): grinst, tritt auf ein Pedal mit der Erläuterung „Gaspedal: Kredite, Sondervermögen“; Sprechblase „Staat: Vollgas! Wir investieren aus der Krise!“.",
                "Beifahrer (EZB): schaut besorgt, zieht einen roten Hebel „Handbremse: Leitzins“; Sprechblase „EZB: Bremsen! Die Preise steigen zu stark!“.",
                "Hinten: schwerer roter Anhänger „STAATSSCHULDEN + Zinslast“ mit drei Säcken „Kredit“; vorne am Straßenrand: Warnschild mit Ausrufezeichen und „INFLATION“.",
                "Strukturierte Beschreibung des Bildaufbaus (Mitte, hinten, vorne, Sprechblasen, Titel).",
            ],
            "hinweis": "Beschreiben: nur das Sichtbare strukturiert wiedergeben; Deutungen (z. B. Zielkonflikt zwischen Fiskal- und Geldpolitik) gehören in die Analyse.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Bildelemente im Ansatz korrekt beschrieben werden.",
            "gut": "die Karikatur vollständig, strukturiert nach Bildaufbau und präzise beschrieben wird, ohne vorzeitig zu deuten.",
        },
    },
    {
        "id": "q2-1-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 die keynesianische Krisenanalyse und die Bedeutung des Multiplikatoreffekts.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Ausgangspunkt: Kritik am Sayschen Theorem; nach Keynes bestimmt die effektive Gesamtnachfrage (C + I + G + X − M) Produktion und Beschäftigung; Gleichgewicht bei Unterbeschäftigung möglich.",
                "Krisenanalyse: Sparen bei steigendem Einkommen, unsichere Erwartungen der Unternehmen (animal spirits), Investitionsschwäche; Abwärtsspirale aus sinkenden Investitionen, Einkommen und Konsum; Lohnsenkungen verschärfen die Nachfrageschwäche; Grenzen der Geldpolitik (Liquiditätsfalle).",
                "Bezug M1: Verunsicherung der Verbraucher durch Energiepreise, zurückgestellte Investitionen, fehlende Nachfrage [1], [3].",
                "Rolle des Staates: antizyklische Fiskalpolitik, Deficit Spending, Schließen der Nachfragelücke; Gegenbeispiel Brüning als prozyklische Sparpolitik [2].",
                "Multiplikator: Ausgaben werden zu Einkommen, die teilweise wieder ausgegeben werden; k = 1/(1 − c), Beispiel mit c = 0,8; Bezug zur Kette Brücke – Bauarbeiter – Zulieferer in M1 [3].",
                "Einschränkung: Sickerverluste (Sparen, Steuern, Importe), Crowding-out und Zeitverzögerungen machen den Multiplikator in der Realität kleiner.",
            ],
            "hinweis": "Erläutern: Theorie mit zusätzlichen Informationen und Beispielen veranschaulichen; Materialbezug notwendig. Eine Rechnung oder ein Zahlenbeispiel zum Multiplikator wertet die Leistung auf.",
        },
        "bewertung": {
            "ausreichend": "die keynesianische Krisenanalyse und der Multiplikatoreffekt im Ansatz zutreffend und mit Bezug zu M1 erläutert werden.",
            "gut": "Krisenanalyse und Multiplikatoreffekt fachlich präzise, mit Beispielen, Grenzen des Multiplikators und durchgängigem Materialbezug erläutert werden.",
        },
    },
    {
        "id": "q2-1-ii2",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie mithilfe von M2 den Zusammenhang zwischen Konjunkturverlauf und Staatsfinanzen.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Automatische Stabilisatoren: In Rezessionen sinken Steuereinnahmen und steigen Ausgaben (Arbeitslosen-, Kurzarbeitergeld) – Defizite 2009/10 und 2020/21; im Aufschwung umgekehrt (Überschuss 2019).",
                "Diskretionäre Maßnahmen: Konjunkturpakete I und II 2008/09, Corona-Hilfen und Konjunkturpaket 2020, Energiepreisbremsen 2022 erhöhen Defizit und Schuldenstand.",
                "Nenner-Effekt: Die Schuldenstandsquote steigt in Rezessionen auch, weil das BIP sinkt (2009, 2020), und sinkt bei Wachstum und Inflation, weil das nominale BIP steigt (2022/23: Quote sinkt trotz Defiziten).",
                "Wirkung der Schuldenbremse (ab 2009/2016) und guter Konjunktur auf den Schuldenabbau bis 2019 (58,3 %).",
                "Seit 2023: Defizite trotz fehlender tiefer Rezession – Hinweis auf strukturelle Ursachen (Verteidigung, Investitionen, Zinsen) bzw. Ratchet-Effekt; Bezug zur Reform 2025.",
                "Rückwirkung: höhere Schulden bedeuten höhere Zinsausgaben und geringeren künftigen Spielraum.",
            ],
            "hinweis": "Erklären: Daten auf Funktionszusammenhänge (automatische Stabilisatoren, diskretionäre Fiskalpolitik, Quotenberechnung) zurückführen; konkrete Belege aus M2 erforderlich.",
        },
        "bewertung": {
            "ausreichend": "der Zusammenhang zwischen Konjunktur und Staatsfinanzen ansatzweise zutreffend erklärt und mit einzelnen Daten aus M2 belegt wird.",
            "gut": "der Zusammenhang differenziert (automatische Stabilisatoren, Konjunkturprogramme, Nenner-Effekt der Quote) erklärt und durchgängig mit Daten aus M2 belegt wird.",
        },
    },
    {
        "id": "q2-1-ii3",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Karikatur (M3) im Hinblick auf Probleme nachfrageorientierter Fiskalpolitik.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Auto „Konjunktur“: die Volkswirtschaft, die in Fahrt gebracht werden soll; der Staat als Fahrer steht für expansive, kreditfinanzierte Fiskalpolitik (Sondervermögen, Kredite) im Sinne von Keynes.",
                "EZB als Beifahrerin mit der Handbremse „Leitzins“: restriktive Geldpolitik zur Sicherung der Preisniveaustabilität (vorrangiges Mandat); Bezug zu den Zinserhöhungen 2026.",
                "Kernaussage 1 – fehlende Koordination (Policy-Mix): Fiskal- und Geldpolitik arbeiten gegeneinander, die Wirkung beider Instrumente wird geschwächt; Ressourcenverschwendung und Unsicherheit.",
                "Kernaussage 2 – Inflation: Das Warnschild verweist auf das Risiko, dass zusätzliche Nachfrage bei knappen Kapazitäten die Preise treibt (Nachfrageinflation); Zielkonflikt im magischen Viereck.",
                "Kernaussage 3 – Staatsverschuldung: Der schwere Anhänger „Staatsschulden + Zinslast“ bremst die Fahrt; steigende Zinsausgaben verringern künftige Spielräume (Ratchet-Effekt, Crowding-out über höhere Zinsen).",
                "Gesamtaussage: Nachfrageorientierte Fiskalpolitik kann unter den Bedingungen von Inflation, Zinserhöhungen und hoher Verschuldung ins Leere laufen oder schaden; die Karikatur ist eher kritisch gegenüber der expansiven Fiskalpolitik.",
            ],
            "hinweis": "Analysieren: Bildelemente systematisch deuten, auf Fachkonzepte beziehen (Policy-Mix, Inflation, Staatsverschuldung, Crowding-out) und eine Gesamtaussage formulieren; Bildbelege angeben.",
        },
        "bewertung": {
            "ausreichend": "zentrale Bildelemente ansatzweise zutreffend gedeutet werden und eine Kernaussage formuliert wird.",
            "gut": "die Bildelemente systematisch und fachsprachlich gedeutet, auf die Probleme Inflation und Staatsverschuldung sowie auf das Zusammenspiel von Fiskal- und Geldpolitik bezogen und zu einer präzisen Gesamtaussage verdichtet werden.",
        },
    },
    {
        "id": "q2-1-ii4",
        "afb": "II",
        "operator": "erklären",
        "lk": True,
        "text": "Erklären Sie die in M2 erkennbaren Konjunkturschwankungen mithilfe eines güterwirtschaftlichen und eines monetären Erklärungsmodells.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Unterscheidung: güterwirtschaftliche Modelle (Ursachen im realen Bereich: Nachfrage, Investitionen, Lager, Innovationen, Schocks) vs. monetäre Modelle (Ursachen in Geldmenge, Zins, Kredit).",
                "Güterwirtschaftlich, z. B. Multiplikator-Akzelerator-Modell: Nachfrageeinbruch 2009 (Exporte) führt über den Akzelerator zu überproportionalem Investitionsrückgang und über den Multiplikator zu weiterem Einkommensrückgang; Erholung 2010 als Umkehrung.",
                "Alternativ Schockmodell: Corona 2020 (Angebots- und Nachfrageschock) und Energiepreisschock 2022 bzw. 2026 als exogene Störungen; Inflationsanstieg 2022 und Schwäche 2023.",
                "Monetär, z. B. Finanzielle Instabilität (Minsky) oder Überinvestitionstheorie (Hayek): Kreditboom und Immobilienblase in den USA vor 2008, Platzen der Blase, Bankenkrise, Kreditklemme als Auslöser der Rezession 2009.",
                "Monetär auch: Zinswende der EZB 2022/23 (Einlagesatz bis 4 %) dämpft Investitionen und Bau – Beitrag zur Schwäche 2023/24; Monetarismus: Geldmengenausweitung 2020/21 als möglicher Beitrag zur Inflation 2022.",
                "Fazit: Die Schwankungen lassen sich meist nur durch das Zusammenwirken mehrerer Ursachen erklären; unterschiedliche Modelle führen zu unterschiedlichen Politikempfehlungen.",
            ],
            "hinweis": "Erklären (LK): zwei Modelle korrekt darstellen und schlüssig auf konkrete Phasen in M2 anwenden; reines Referieren der Modelle ohne Datenbezug genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "ein güterwirtschaftliches und ein monetäres Modell im Ansatz zutreffend dargestellt und auf einzelne Phasen in M2 bezogen werden.",
            "gut": "beide Modelle fachlich präzise erklärt, schlüssig auf mehrere Phasen in M2 angewendet und ihr Erklärungswert reflektiert wird.",
        },
    },
    {
        "id": "q2-1-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Die Autorin fordert, die Schuldenbremse nicht wieder zu verschärfen, sondern dauerhaft eine Ausnahme für öffentliche Investitionen zu schaffen. Erörtern Sie diese Forderung unter besonderer Berücksichtigung der Probleme Inflation und Staatsverschuldung. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Einordnung: Forderung entspricht der „goldenen Regel“ der Finanzpolitik (Kreditfinanzierung von Nettoinvestitionen); Bezug zur Reform 2025 (Sondervermögen, Bereichsausnahme) und zu Art. 115 GG [6].",
                "Pro: Investitionsstau, Wachstumswirkung und höheres Produktionspotenzial; Multiplikator in schwacher Konjunktur [3]; Generationengerechtigkeit, weil künftige Generationen von Infrastruktur profitieren [5]; vergleichsweise niedrige Schuldenquote; Planungssicherheit für Bauwirtschaft.",
                "Contra Staatsverschuldung: steigende Zinsausgaben (bis 2030 rund 80 Mrd. Euro) engen Spielräume ein [5]; Ratchet-Effekt; Abgrenzungsprobleme, was als Investition gilt (Umetikettierung); EU-Fiskalregeln; Risiko steigender Zinsen und Vertrauensverlust.",
                "Contra Inflation: zusätzliche Nachfrage bei knappen Kapazitäten (Bau, Fachkräfte – von der Autorin selbst genannt [6]) treibt Preise; Konflikt mit der EZB, die 2026 die Zinsen erhöhte; Gegenargument der Autorin: Inflation energiegetrieben, Kerninflation moderat [4].",
                "Abwägung: z. B. Bedeutung der Lage (Unterauslastung vs. Kapazitätsgrenze), Umsetzungsprobleme (Mittelabfluss), alternative Finanzierung (Umschichtungen, Abbau von Subventionen), Verbindung mit Angebotsreformen (Planungsbeschleunigung).",
                "Begründetes eigenes Urteil nach Kriterien (Wirksamkeit, Preisniveaustabilität, Tragfähigkeit, Generationengerechtigkeit); beide Ergebnisse möglich, differenzierte Lösungen (z. B. befristete, eng definierte Ausnahme) ebenso.",
            ],
            "hinweis": "Erörtern: Pro- und Kontraargumente abwägen und zu einem eigenen Urteil gelangen. Die Erlass-Schwerpunkte Inflation und Staatsverschuldung müssen ausdrücklich behandelt werden; Bezug auf die Forderung in [6] und die Argumente in [4], [5] erwartet.",
        },
        "bewertung": {
            "ausreichend": "Pro- und Kontraargumente unter Berücksichtigung von Inflation und Staatsverschuldung ansatzweise abgewogen werden und ein nachvollziehbares Urteil vorliegt.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und materialbezogen ist, Inflation und Staatsverschuldung differenziert gewichtet und in ein kriteriengeleitetes, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q2-1-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie auf der Grundlage von M2, ob die deutsche Fiskalpolitik in den Krisen 2008/09 und 2020 dem keynesianischen Anspruch einer antizyklischen Politik gerecht geworden ist.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien klären: rechtzeitiges und ausreichendes Gegensteuern in der Krise, Wirksamkeit (Erholung, Beschäftigung), Symmetrie (Konsolidierung im Aufschwung), Nebenwirkungen (Inflation, Schulden).",
                "2008/09: Konjunkturpakete I und II, Kurzarbeit, Umweltprämie; Defizit 2009/10 (−3,2 % / −4,4 %), rasche Erholung 2010 (+4,1 %) – spricht für antizyklisches Handeln; aber zeitliche Verzögerung (Teile wirkten erst 2010), Mitnahmeeffekte.",
                "Konsolidierung danach: Schuldenstand von 81,0 % (2010) auf 58,3 % (2019), Überschuss 2019 – antizyklische Symmetrie weitgehend erfüllt (unterstützt durch Schuldenbremse und Niedrigzinsen).",
                "2020: Notlagenausnahme, Hilfen und Konjunkturpaket, Defizit −4,3 %; Erholung 2021 (+4,0 %), Massenarbeitslosigkeit verhindert – antizyklisch.",
                "Kritische Punkte: Fortsetzung hoher Defizite 2021–2025 trotz Erholung bzw. bei hoher Inflation (2022: 8,7 %) – teils prozyklische Wirkung, Ratchet-Effekt; Energiepreisbremsen eher Angebots-/Verteilungsfrage; Haushaltsurteil 2023.",
                "Begründetes Gesamturteil (z. B. in der akuten Krise weitgehend antizyklisch, bei der Rückführung nach 2020 nur eingeschränkt).",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete, mit Fachwissen und Daten aus M2 belegte Einschätzung; Kenntnisse über die Maßnahmen beider Krisen werden erwartet.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil zu beiden Krisen mit einzelnen Belegen aus M2 formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, differenziert nach Krise und Phase (Krise, Konsolidierung), fachlich fundiert und schlüssig mit Daten aus M2 begründet ist.",
        },
    },
    {
        "id": "q2-1-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Entwerfen Sie eine Rede für die Haushaltsdebatte im Deutschen Bundestag, in der Sie als Abgeordnete bzw. Abgeordneter begründet Position zu der Frage beziehen, ob der Bund seine Kreditaufnahme zur Stützung der Konjunktur weiter ausweiten sollte. Setzen Sie sich dabei mit den Risiken Inflation und Staatsverschuldung auseinander. (M1, M3)",
        "material": ["m1", "m3"],
        "loesung": {
            "punkte": [
                "Adressatengerechte Redeform: Anrede (Frau Präsidentin/Herr Präsident, meine Damen und Herren), klare These, Gliederung, rhetorische Mittel, Appell bzw. Schluss.",
                "Lagebeschreibung mit Fakten: schwaches Wachstum seit 2023, Erholung 2026, knapp drei Millionen Arbeitslose, Energiepreisschock, Reform 2025 und Haushalt 2026 (Nettokreditaufnahme rund 98 Mrd. Euro) (M1 [1], [2]).",
                "Argumentation aus der gewählten Position: z. B. keynesianisch (Nachfragelücke, Multiplikator, Investitionsstau, Brüning als Warnung) oder konsolidierungsorientiert (Zinslast, Ratchet-Effekt, Crowding-out, Kapazitätsgrenzen, Angebotsreformen).",
                "Auseinandersetzung mit Inflation: Unterscheidung Energie- vs. Nachfrageinflation, Kerninflation, Konflikt mit der EZB („Gas und Bremse“, M3), Zweitrundeneffekte.",
                "Auseinandersetzung mit Staatsverschuldung: Schuldenquote, Zinsausgaben laut Finanzplan, Generationengerechtigkeit, Investitionen vs. konsumtive Ausgaben (z. B. Kraftstoffsteuersenkung, M1 [6]).",
                "Konkrete Vorschläge (z. B. Investitionen beschleunigen, zielgenaue statt Gießkannen-Entlastungen, Koordination mit der Geldpolitik, Konsolidierungspfad) und schlüssiges Fazit.",
            ],
            "hinweis": "Gestalten/entwerfen: produktorientierte Aufgabe; bewertet werden fachliche Richtigkeit, Schlüssigkeit der Position, Auseinandersetzung mit Gegenargumenten (Inflation, Staatsverschuldung) und Adressaten- bzw. Textsortengerechtigkeit. Die Position ist frei wählbar.",
        },
        "bewertung": {
            "ausreichend": "eine erkennbare Rede mit nachvollziehbarer Position vorliegt, die die Risiken Inflation und Staatsverschuldung zumindest ansatzweise aufgreift.",
            "gut": "die Rede textsortengerecht, adressatenbezogen und fachlich fundiert ist, Materialbezüge nutzt, sich differenziert mit Inflation und Staatsverschuldung auseinandersetzt und in ein überzeugendes Fazit mündet.",
        },
    },
    {
        "id": "q2-1-iii4",
        "afb": "III",
        "operator": "beurteilen",
        "lk": True,
        "text": "Beurteilen Sie, welche Lehren sich aus historischen Erfahrungen mit fiskalpolitischen Interventionen (z. B. 1930er-Jahre, 1970er-Jahre, 2008/09, 2020) für die heutige Konjunkturpolitik ziehen lassen.",
        "material": [],
        "loesung": {
            "punkte": [
                "Kriterien: Art der Krise (Nachfrage- vs. Angebotsschock), Zeitpunkt und Dosierung, Koordination mit der Geldpolitik, Nebenwirkungen (Inflation, Schulden), politische Umsetzbarkeit.",
                "1930er: Brünings prozyklische Sparpolitik verschärfte die Krise; New Deal mit Erholung, Rückfall 1937/38 nach zu früher Straffung – Lehre: in tiefen Nachfragekrisen nicht prozyklisch sparen.",
                "1970er: Konjunkturprogramme bei Ölpreisschocks führten zu Stagflation und Schuldenanstieg – Lehre: Nachfragepolitik hilft kaum gegen Angebotsschocks; Gefahr für die Preisniveaustabilität.",
                "2008/09: schnelle, international abgestimmte Programme und Kurzarbeit stabilisierten Beschäftigung – Erfolg bei Nachfrageschock; aber Mitnahmeeffekte und Schuldenanstieg, danach Konsolidierung.",
                "2020–2022: massive Stützung verhinderte Massenarbeitslosigkeit; anschließende Inflation und Debatte über Überstimulierung; Notlagenkredite und Haushaltsurteil 2023 zeigen rechtliche Grenzen.",
                "Übertragung auf heute (Energiepreisschock 2026, Sondervermögen, Zinserhöhungen der EZB): eher zielgenaue, befristete Hilfen und investive statt konsumtive Ausgaben; Abstimmung mit der EZB; begründetes Gesamturteil, das auch Grenzen der Übertragbarkeit (andere Ausgangslagen, Euro, Globalisierung) reflektiert.",
            ],
            "hinweis": "Beurteilen (LK): historische Fälle müssen fachlich korrekt und vergleichend genutzt werden; das Urteil braucht erkennbare Kriterien und einen Gegenwartsbezug.",
        },
        "bewertung": {
            "ausreichend": "mehrere historische Beispiele im Ansatz korrekt herangezogen und zu einem ansatzweise begründeten Urteil über Lehren für heute verdichtet werden.",
            "gut": "die historischen Erfahrungen kriteriengeleitet verglichen, fachlich präzise dargestellt und in ein differenziertes, schlüssig begründetes Urteil mit klarem Gegenwartsbezug überführt werden.",
        },
    },
]
