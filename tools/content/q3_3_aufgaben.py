# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q3.3 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q3.3, insbesondere Fallstudie zu Entwicklungsproblemen (Wirtschaft, Gesellschaft, Politik, Ökologie) am Beispiel Bangladeschs, Beitrag staatlicher und nichtstaatlicher Akteure zu nachhaltiger Entwicklung sowie Fragen nachhaltiger Entwicklungspolitik (Zielkonflikte, Strategien, Mittel); LK: Dimensionen von Unterentwicklung und multikausale Erklärungsansätze. Q3.3 ist kein Schwerpunkt im Abiturerlass 2027; Bezüge bestehen zu Q3.2 (Lieferketten, Standortwettbewerb, WTO)."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Bericht „Der lange Weg aus dem Nadelöhr“ (2026)",
        "absaetze": [
            "Gazipur, nördlich von Dhaka, kurz nach acht Uhr morgens. Hunderte Frauen strömen durch das Tor einer Bekleidungsfabrik. Eine von ihnen ist die 24-jährige Rina, die seit sechs Jahren an einer Nähmaschine arbeitet. Sie verdient etwas mehr als den gesetzlichen Mindestlohn der Branche von 12.500 Taka im Monat, der seit Dezember 2023 gilt. „Davon kann ich die Miete zahlen und meinen Eltern im Dorf etwas schicken“, sagt sie. Die Gewerkschaften fordern eine deutliche Erhöhung; über eine Neufestsetzung wird verhandelt.",
            "Fabriken wie diese haben Bangladesch verändert. Als das Land 1971 unabhängig wurde, galt es als hoffnungsloser Fall. Heute stammen über 80 Prozent seiner Warenexporte aus der Bekleidungsindustrie – im Fiskaljahr 2024/25 rund 39 von 48 Milliarden US-Dollar. Die Lebenserwartung liegt bei fast 75 Jahren, der Anteil der extrem Armen ist laut Weltbank auf unter sechs Prozent gesunken. Mikrokredite der Grameen Bank und Programme großer NGOs wie BRAC haben dazu ebenso beigetragen wie Milliarden an Rücküberweisungen von Menschen aus Bangladesch, die in den Golfstaaten oder in Malaysia arbeiten.",
            "Doch der Erfolg hat Schattenseiten. Am 24. April 2013 stürzte das Fabrikgebäude Rana Plaza ein; mehr als 1.100 Menschen starben. Seitdem sind viele Fabriken sicherer geworden – auch dank eines verbindlichen Abkommens zwischen internationalen Modemarken und Gewerkschaften. Aber die Löhne bleiben niedrig, Überstunden sind die Regel, und Gewerkschaftsarbeit wird vielerorts behindert. Zudem hängt das Land am seidenen Faden einer einzigen Branche: Als die USA 2025 hohe Zölle verhängten, zitterten die Fabrikbesitzer um ihre Aufträge.",
            "Auch politisch ist das Land im Umbruch. Im Sommer 2024 stürzten Studierendenproteste, bei denen nach Schätzungen der Vereinten Nationen bis zu 1.400 Menschen getötet wurden, die seit 2009 regierende Premierministerin Sheikh Hasina. Nach einer Übergangszeit unter Muhammad Yunus gewann im Februar 2026 die Bangladesh Nationalist Party (BNP) die Parlamentswahl. „Die Menschen erwarten, dass die Korruption endlich bekämpft wird“, sagt ein Politikwissenschaftler der Universität Dhaka. „Ob die neuen Machthaber anders sind als die alten, muss sich erst zeigen.“",
            "Über allem schwebt der Klimawandel. Große Teile des Landes liegen nur wenige Meter über dem Meeresspiegel. Wirbelstürme, Überschwemmungen und die Versalzung der Böden im Süden vertreiben jedes Jahr Menschen aus ihren Dörfern – viele landen in den Armenvierteln von Dhaka und suchen Arbeit in den Fabriken. Gleichzeitig färben Abwässer der Textilfärbereien die Flüsse rund um die Hauptstadt.",
            "Eigentlich sollte Bangladesch am 24. November 2026 die Gruppe der am wenigsten entwickelten Länder (LDC) verlassen – ein Erfolg, der zugleich Risiken birgt. Denn mit dem Status entfallen nach einer Übergangsfrist Vorteile wie der zollfreie Zugang zum EU-Markt. Die neue Regierung beantragte deshalb einen Aufschub; Ende Oktober 2026 stimmte die UN-Generalversammlung zu: Der Austritt erfolgt nun am 24. November 2029. Wirtschaftsverbände begrüßen die Atempause. Kritische Ökonominnen und Ökonomen warnen dagegen, das Land verschiebe nur notwendige Reformen: höhere Produktivität, neue Exportbranchen, bessere Arbeitsbedingungen.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Bericht einer fiktiven Reporterin (2026); die zitierten Personen sind erfunden. Daten und Ereignisse sind real (Stand: Oktober 2026), u. a. nach Angaben des Export Promotion Bureau Bangladesh (Fiskaljahr 2024/25), der Weltbank, des UN-Menschenrechtsbüros und Berichten über den Beschluss der UN-Generalversammlung.",
    },
    {
        "id": "m2",
        "titel": "M2: Entwicklungsindikatoren ausgewählter Länder im Vergleich",
        "typ": "tabelle",
        "kopf": ["Land (Einwohner 2025)", "HDI 2023 (Rang von 193)", "Lebenserwartung 2023 in Jahren", "Schuljahre im Durchschnitt 2023", "BNE pro Kopf 2025 in US-$ (Einkommensgruppe)", "Extreme Armut in % (Jahr)", "Beschäftigte in der Landwirtschaft 2025 in %", "Verarbeitendes Gewerbe 2025 in % des BIP"],
        "zeilen": [
            ["Bangladesch (175,7\u00a0Mio.)", "0,685\u00a0(130)", "74,7", "6,8", "2.840 (untere mittlere)", "5,9\u00a0(2022)", "44,3", "22,4"],
            ["Vietnam (101,6\u00a0Mio.)", "0,766\u00a0(93)", "74,6", "9,0", "4.970 (obere mittlere)", "1,6\u00a0(2022)", "25,0", "24,5"],
            ["Äthiopien (135,5\u00a0Mio.)", "0,497\u00a0(180)", "67,3", "2,4", "1.110 (niedrige)", "38,6\u00a0(2021)", "60,1", "4,2"],
            ["Niger (27,9\u00a0Mio.)", "0,419\u00a0(188)", "61,2", "1,4", "750 (niedrige)", "60,5\u00a0(2021)", "73,0", "7,0\u00a0(2024)"],
            ["Deutschland (83,5\u00a0Mio.)", "0,959\u00a0(5)", "81,4", "14,3", "60.200 (hohe)", "0,7\u00a0(2022)", "1,1", "17,6"],
        ],
        "quelle": "Extreme Armut = Anteil der Bevölkerung mit weniger als 3,00 US-$ pro Tag (Kaufkraftparitäten 2021); Einkommensgruppen nach der Weltbank-Klassifikation ab 1. Juli 2026. Quellen: UNDP, Human Development Report 2025, Statistik-Tabelle 1 (Daten für 2023); Weltbank, World Development Indicators (Datenstand 8. Oktober 2026, abgerufen am 2. November 2026): Bevölkerung, BNE pro Kopf (Atlas-Methode), Armutsquote bei 3,00 US-$ pro Tag (Kaufkraftparitäten 2021), Beschäftigte in der Landwirtschaft (modellierte ILO-Schätzung), Wertschöpfung des Verarbeitenden Gewerbes. Werte gerundet.",
    },
    {
        "id": "m3",
        "titel": "M3: Kommentar „Mehr Handel, weniger Hilfe“ (2026)",
        "absaetze": [
            "2025 war ein Schockjahr für die Entwicklungszusammenarbeit. Nach vorläufigen Zahlen der OECD sanken die öffentlichen Entwicklungsleistungen der Geberländer um 23,1 Prozent – so stark wie nie zuvor. Die USA lösten ihre Entwicklungsagentur USAID auf, auch Deutschland kürzte und verfehlt das vor mehr als 50 Jahren vereinbarte Ziel, 0,7 Prozent des Bruttonationaleinkommens bereitzustellen, inzwischen deutlich. Hilfsorganisationen sprechen von einer Katastrophe. Ich halte die Krise für eine Chance.",
            "Denn seit Jahrzehnten fließen Milliarden in die ärmsten Länder, ohne dass sich viele von ihnen nachhaltig entwickelt hätten. Hilfe hat Regierungen bequem gemacht: Wer seinen Haushalt zu großen Teilen aus dem Ausland finanziert, muss sich weniger vor den eigenen Bürgerinnen und Bürgern verantworten und keine Steuern eintreiben. Projekte werden nach den Vorlieben der Geber ausgewählt, oft mit Aufträgen für deren eigene Unternehmen. Und in Ländern mit korrupten Eliten versickert ein Teil des Geldes.",
            "Die Länder, die den Sprung geschafft haben, verdanken das nicht in erster Linie Hilfsprogrammen, sondern dem Handel: Südkorea, China, Vietnam – und Bangladesch. Dessen Exporterlöse aus Bekleidung lagen zuletzt bei fast 40 Milliarden US-Dollar im Jahr, hinzu kamen Rücküberweisungen von über 30 Milliarden. Damit können Entwicklungsgelder nicht annähernd mithalten. Die Jobs in den Fabriken haben Millionen Frauen ein eigenes Einkommen verschafft – das hätte kein Projekt geschafft.",
            "Was ist also zu tun? Erstens müssen die reichen Länder ihre Märkte öffnen – auch für verarbeitete Produkte und Agrargüter – und dürfen Fortschritte nicht bestrafen, indem sie Handelsvorteile nach dem Aufstieg eines Landes rasch streichen. Zweitens müssen private Investitionen in Fabriken, Energie und Infrastruktur abgesichert und gefördert werden. Drittens sollte sich staatliche Hilfe auf Nothilfe und auf globale Gemeinschaftsgüter wie Impfstoffe und Klimaanpassung konzentrieren.",
            "Natürlich hat auch der Handel Schattenseiten, wie Rana Plaza gezeigt hat. Aber höhere Standards entstehen nicht durch Projekte aus Berlin oder Washington, sondern durch Wachstum, das Arbeitskräfte knapper und Gewerkschaften stärker macht. Wer heute gegen Fabriken in Bangladesch protestiert, sollte sich fragen, welche Alternativen die Näherinnen hätten: die Reisfelder ihrer Eltern oder die Armenviertel von Dhaka.",
            "Die Kürzungen schmerzen, gerade in akuten Krisen. Doch statt sie nur zu beklagen, sollten wir die Gelegenheit nutzen, die Entwicklungspolitik vom Kopf auf die Füße zu stellen: Handel statt Hilfe, Investitionen statt Almosen, Eigenverantwortung statt Abhängigkeit.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Wirtschaftsjournalisten (2026). Zahlen: OECD, vorläufige ODA-Daten 2025 (April 2026); Export Promotion Bureau und Bangladesh Bank (Fiskaljahr 2024/25). Zum Vergleich: Die öffentlichen Entwicklungsleistungen an Bangladesch betrugen laut Weltbank 2023 netto rund 5,7 Mrd. US-Dollar.",
    },
]

AUFGABEN = [
    {
        "id": "q3-3-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie den Bericht zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Bericht), Titel „Der lange Weg aus dem Nadelöhr“, Erscheinungsjahr (2026) und Thema (Entwicklung Bangladeschs zwischen Exporterfolg, Schattenseiten und dem verschobenen Austritt aus der LDC-Gruppe); fiktive Reporterin.",
            "punkte": [
                "Alltag einer Textilarbeiterin in Gazipur: Lohn knapp über dem Mindestlohn von 12.500 Taka (seit Dezember 2023), Unterstützung der Familie, Forderungen der Gewerkschaften nach einer Erhöhung [1].",
                "Aufstieg vom „hoffnungslosen Fall“ (1971) zum Exportland: über 80 % der Warenexporte aus Bekleidung (rund 39 von 48 Mrd. US-Dollar, 2024/25), Lebenserwartung fast 75 Jahre, extreme Armut unter 6 %; Beiträge von Mikrokrediten, NGOs und Rücküberweisungen [2].",
                "Schattenseiten: Einsturz von Rana Plaza 2013 (über 1.100 Tote), seitdem sicherere Fabriken durch ein Abkommen, aber niedrige Löhne, Überstunden, Behinderung von Gewerkschaften; Abhängigkeit von einer Branche, Sorge wegen der US-Zölle 2025 [3].",
                "Politischer Umbruch: Sturz Hasinas 2024 nach Protesten mit bis zu 1.400 Toten, Übergangsregierung unter Yunus, Wahlsieg der BNP im Februar 2026; Erwartung an Korruptionsbekämpfung, offene Zukunft [4].",
                "Klimawandel: niedrige Lage, Wirbelstürme, Fluten, Versalzung; Landflucht in die Armenviertel und Fabriken; Wasserverschmutzung durch Färbereien [5].",
                "LDC-Austritt: ursprünglich für November 2026 geplant, auf Antrag auf den 24. November 2029 verschoben; Wegfall von Präferenzen nach einer Übergangsfrist; Zustimmung der Wirtschaft vs. Warnung vor aufgeschobenen Reformen [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache, keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Aussagen des Berichts im Ansatz korrekt und mit Einleitungssatz zusammengefasst werden.",
            "gut": "die Aussagen weitgehend vollständig, strukturiert, komprimiert und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q3-3-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie den Entwicklungsstand Bangladeschs im Vergleich zu den anderen in M2 aufgeführten Ländern.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Formales: Tabelle mit Daten von UNDP (2023) und Weltbank (2021–2025); fünf Länder aus unterschiedlichen Einkommensgruppen; Indikatoren zu Gesundheit, Bildung, Einkommen, Armut und Wirtschaftsstruktur.",
                "HDI: Bangladesch 0,685 (Rang 130) – deutlich vor Äthiopien (0,497) und Niger (0,419), hinter Vietnam (0,766) und weit hinter Deutschland (0,959).",
                "Gesundheit und Bildung: Lebenserwartung 74,7 Jahre – fast gleichauf mit Vietnam (74,6), deutlich höher als in Äthiopien (67,3) und Niger (61,2); Schulbesuchsdauer 6,8 Jahre – mehr als in Äthiopien und Niger, aber weniger als in Vietnam (9,0) und Deutschland (14,3).",
                "Einkommen und Armut: BNE pro Kopf 2.840 US-Dollar (unteres mittleres Einkommen), knapp 60 % des vietnamesischen Werts, aber mehr als das Doppelte Äthiopiens; extreme Armut 5,9 % gegenüber 38,6 % (Äthiopien) und 60,5 % (Niger).",
                "Wirtschaftsstruktur: 44,3 % der Beschäftigten arbeiten in der Landwirtschaft; das Verarbeitende Gewerbe erwirtschaftet 22,4 % des BIP – ähnlich wie in Vietnam (24,5 %) und mehr als in Deutschland (17,6 %).",
                "Gesamteindruck: Bangladesch liegt bei fast allen Indikatoren zwischen den ärmsten Ländern (Äthiopien, Niger) und dem Aufsteiger Vietnam.",
            ],
            "hinweis": "Beschreiben: strukturiert und fachsprachlich in eigenen Worten; Zahlen korrekt mit Einheit und Jahr wiedergeben. Ursachen müssen nicht erklärt, Befunde nicht bewertet werden.",
        },
        "bewertung": {
            "ausreichend": "zentrale Indikatoren Bangladeschs im Ansatz korrekt beschrieben und mit einzelnen anderen Ländern verglichen werden.",
            "gut": "der Entwicklungsstand Bangladeschs strukturiert, mit korrekten Zahlenangaben und durchgängig im Vergleich zu den anderen Ländern beschrieben wird.",
        },
    },
    {
        "id": "q3-3-i3",
        "afb": "I",
        "operator": "darstellen",
        "text": "Stellen Sie die Agenda 2030 sowie die wichtigsten Mittel der staatlichen Entwicklungszusammenarbeit dar.",
        "material": [],
        "loesung": {
            "punkte": [
                "Agenda 2030: 2015 von allen UN-Mitgliedstaaten beschlossen; 17 Ziele für nachhaltige Entwicklung (SDGs) mit 169 Unterzielen bis 2030; universeller Anspruch (auch für Industrieländer); Leitprinzip „Niemanden zurücklassen“; Verbindung ökonomischer, sozialer und ökologischer Dimensionen.",
                "Beispiele für Ziele: keine Armut, kein Hunger, hochwertige Bildung, Geschlechtergleichheit, menschenwürdige Arbeit und Wirtschaftswachstum, Klimaschutz, Partnerschaften.",
                "Stand: Laut SDG-Bericht 2026 sind nur 36 % der messbaren Unterziele auf Kurs oder machen moderate Fortschritte, 15 % haben sich gegenüber 2015 verschlechtert (Detailkenntnis nicht zwingend).",
                "Bilaterale Mittel: Finanzielle Zusammenarbeit (über die KfW: Zuschüsse, zinsgünstige Kredite, z. B. für Infrastruktur), Technische Zusammenarbeit (über die GIZ: Beratung, Ausbildung, Aufbau von Institutionen), personelle Zusammenarbeit.",
                "Multilaterale Mittel: Beiträge an Weltbank, Vereinte Nationen, EU und globale Fonds.",
                "Weitere Instrumente: Budgethilfe, Schuldenerlass, Handelspräferenzen (z. B. „Alles außer Waffen“), Klimapartnerschaften, humanitäre Hilfe; Finanzierungsziel 0,7 % des Bruttonationaleinkommens (ODA-Quote).",
            ],
            "hinweis": "Darstellen: Sachverhalte und Zusammenhänge strukturiert aufzeigen; Fachbegriffe korrekt verwenden; keine Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die Agenda 2030 und einige Mittel der staatlichen EZ in Grundzügen zutreffend dargestellt werden.",
            "gut": "Agenda 2030 und Mittel der staatlichen EZ strukturiert, fachsprachlich präzise und mit Beispielen dargestellt werden.",
        },
    },
    {
        "id": "q3-3-ii1",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Entwicklungsprobleme Bangladeschs in den Dimensionen Wirtschaft, Gesellschaft, Politik und Ökologie. (M1, M2)",
        "material": ["m1", "m2"],
        "loesung": {
            "punkte": [
                "Wirtschaft: einseitige Exportstruktur (über 80 % Bekleidung) [2], [3]; Abhängigkeit von Abnehmern in EU und USA, von Zöllen und Handelspräferenzen [3], [6]; großer Agrarsektor (44,3 % der Beschäftigten, M2); niedrige Produktivität; Abhängigkeit von Rücküberweisungen [2].",
                "Gesellschaft: niedrige Löhne, lange Arbeitszeiten, eingeschränkte Gewerkschaftsrechte [1], [3]; geringe Schulbildung (6,8 Jahre, M2); Arbeitssicherheit (Rana Plaza) [3]; als Gegenbefund Fortschritte bei Lebenserwartung und Armut (M2, [2]).",
                "Politik: Korruption, autoritäre Herrschaft bis 2024, Gewalt gegen Protestierende, ungewisse Reformperspektive nach dem Machtwechsel 2026 [4].",
                "Ökologie: hohe Verwundbarkeit durch den Klimawandel (Wirbelstürme, Fluten, Versalzung) und Umweltverschmutzung durch die Textilindustrie [5].",
                "Wechselwirkungen: Klimafolgen führen zu Landflucht und vergrößern das Angebot billiger Arbeitskräfte für die Fabriken [5]; schwache Institutionen erschweren die Durchsetzung von Arbeits- und Umweltrecht [3], [4]; Exportabhängigkeit erhöht den Druck auf Löhne im Standortwettbewerb.",
                "Fazit: Bangladesch ist ein Aufsteiger mit erheblichen strukturellen Risiken; seine Entwicklungsprobleme sind mehrdimensional und verstärken sich gegenseitig.",
            ],
            "hinweis": "Analysieren: kriteriengeleitete Erschließung entlang der vier vorgegebenen Dimensionen mit Belegen aus M1 und M2. Das Herausarbeiten von Wechselwirkungen zwischen den Dimensionen kennzeichnet eine gute Leistung.",
        },
        "bewertung": {
            "ausreichend": "Entwicklungsprobleme in mehreren Dimensionen im Ansatz zutreffend und mit einzelnen Materialbelegen analysiert werden.",
            "gut": "alle vier Dimensionen strukturiert, mit Belegen aus M1 und M2 analysiert und Wechselwirkungen zwischen ihnen schlüssig herausgearbeitet werden.",
        },
    },
    {
        "id": "q3-3-ii2",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie am Beispiel Bangladeschs den Beitrag staatlicher und nichtstaatlicher Akteure zu einer nachhaltigen Entwicklung. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Staat Bangladesch: Mindestlohn [1], Wahlen und Reformvorhaben [4], Antrag auf Aufschub des LDC-Austritts [6]; Aufgaben: Rechtsstaat, Durchsetzung von Arbeits- und Umweltrecht, Bildung, Klimaanpassung.",
                "Internationale staatliche Akteure: UN (LDC-Status, Beschluss der Generalversammlung) [6]; EU (zollfreier Marktzugang „Alles außer Waffen“) [6]; USA mit Zöllen als Gegenbeispiel [3]; Weltbank und IWF (Kredite, Reformauflagen); bilaterale EZ, z. B. deutsche Unterstützung bei Sozial- und Umweltstandards in der Textilindustrie.",
                "Nichtstaatliche Akteure: NGOs wie BRAC und die Grameen Bank (Mikrokredite, Gesundheit, Bildung) [2]; Gewerkschaften (Lohnforderungen, Abkommen) [1], [3]; internationale Modemarken (Abkommen zur Gebäudesicherheit nach Rana Plaza) [3]; Arbeitsmigrantinnen und -migranten (Rücküberweisungen) [2].",
                "Beitrag nach Nachhaltigkeitsdimensionen: ökonomisch (Jobs, Marktzugang, Devisen), sozial (Sicherheit, Armutsminderung, Frauenerwerbstätigkeit), ökologisch bislang gering (Abwasserprobleme [5]).",
                "Grenzen: Abhängigkeit von Geberinteressen, begrenzte Reichweite von NGOs, Freiwilligkeit vieler Unternehmensinitiativen, Korruption und schwache Institutionen.",
            ],
            "hinweis": "Erläutern: Beiträge der Akteure mit Beispielen aus M1 und zusätzlichem Fachwissen veranschaulichen; die Unterscheidung staatlich/nichtstaatlich sowie national/international sollte erkennbar sein.",
        },
        "bewertung": {
            "ausreichend": "Beiträge einiger staatlicher und nichtstaatlicher Akteure im Ansatz zutreffend und mit Bezug zu M1 erläutert werden.",
            "gut": "die Beiträge verschiedener Akteursgruppen differenziert, mit Beispielen aus M1 und Fachwissen erläutert und auf die Dimensionen nachhaltiger Entwicklung bezogen werden, einschließlich ihrer Grenzen.",
        },
    },
    {
        "id": "q3-3-ii3",
        "afb": "II",
        "operator": "herausarbeiten",
        "text": "Arbeiten Sie die entwicklungspolitischen Annahmen heraus, die der Argumentation des Kommentars zugrunde liegen. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Entwicklung entstehe vor allem durch Marktintegration, Handel und private Investitionen (exportorientierte Industrialisierung) [3], [4] – Nähe zur Modernisierungstheorie bzw. zur liberalen Außenhandelstheorie.",
                "Die Ursachen von Unterentwicklung lägen wesentlich in den Ländern selbst (Korruption, fehlende Rechenschaft, fehlende Steuererhebung) [2] – Betonung endogener Faktoren und der Regierungsführung.",
                "Entwicklungshilfe könne schaden (Abhängigkeit, Fehlanreize, Geberinteressen) [2], [6]; die Rolle des Staates solle sich auf Nothilfe und globale Gemeinschaftsgüter beschränken [4].",
                "Wachstum führe gleichsam automatisch zu besseren Arbeitsstandards (Knappheit von Arbeitskräften, stärkere Gewerkschaften) [5].",
                "Die Erfahrungen erfolgreicher Länder (Südkorea, China, Vietnam, Bangladesch) seien übertragbar [3]; nicht thematisiert werden die aktive Rolle des Staates in diesen Ländern und die besonderen Bedingungen ärmster Länder (Binnenlage, Konflikte, fehlende Industrie).",
                "Wertorientierung: Eigenverantwortung und Marktfreiheit als Leitwerte [6].",
            ],
            "hinweis": "Herausarbeiten: aus dem Material nicht explizit genannte Sachverhalte erschließen; die bloße Wiedergabe der Forderungen reicht nicht. Bezüge zu Erklärungsansätzen sind auch im Grundkurs als Vertiefung willkommen.",
        },
        "bewertung": {
            "ausreichend": "einige zugrunde liegende Annahmen zutreffend erschlossen und am Text belegt werden.",
            "gut": "die zentralen Annahmen über Ursachen von Entwicklung, Rolle von Staat und Markt und Wirkungen von Hilfe differenziert erschlossen, belegt und auch Leerstellen der Argumentation benannt werden.",
        },
    },
    {
        "id": "q3-3-ii4",
        "afb": "II",
        "operator": "erklären",
        "lk": True,
        "text": "Erklären Sie die Entwicklung Bangladeschs seit 1971 mithilfe der Modernisierungstheorie und der Dependenztheorie. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Modernisierungstheorie: Ausgangspunkt traditionelle Agrargesellschaft mit Kapitalmangel; Industrialisierung durch die Exportindustrie, Kapital und Know-how ausländischer Abnehmer, Urbanisierung, Frauenerwerbstätigkeit als Modernisierung [2]; „Take-off“ im Sinne Rostows; LDC-Aufstieg als Beleg [6].",
                "Grenzen dieser Erklärung: weiterhin großer Agrarsektor und geringe Bildung, einseitige Abhängigkeit von einer Branche, politische Instabilität [3], [4].",
                "Dependenztheorie: Einbindung als Niedriglohnstandort in Wertschöpfungsketten, die von Marken des Nordens gesteuert werden; geringer Anteil an der Wertschöpfung, niedrige Löhne, Abhängigkeit von Abnehmern, Präferenzen und Zöllen der Zentren [3], [6]; historisch: Ausbeutung als Rohstofflieferant (Jute) in der Kolonialzeit und als Teil Pakistans (1947–1971).",
                "Grenzen der Dependenztheorie: Bangladesch hat sich gerade durch Weltmarktintegration entwickelt (Rückgang der Armut, steigende Lebenserwartung [2]) – das widerspricht der Abkopplungsstrategie.",
                "Fazit: Beide Theorien erklären Teilaspekte; eine multikausale Erklärung, die endogene (Regierungsführung, NGOs) und exogene Faktoren (Präferenzen, Zölle, Klimawandel) einbezieht, ist überzeugender.",
            ],
            "hinweis": "Erklären: die Entwicklung auf Annahmen und Wirkungszusammenhänge der beiden Theorien zurückführen; Materialbezüge sind erforderlich. Theoriegeleitete Grenzen kennzeichnen eine gute Leistung.",
        },
        "bewertung": {
            "ausreichend": "die Entwicklung Bangladeschs mit Grundannahmen beider Theorien im Ansatz zutreffend erklärt wird.",
            "gut": "beide Theorien sachgerecht auf die Entwicklung Bangladeschs angewendet, mit Materialbelegen verknüpft und in ihrer Erklärungskraft begrenzt werden.",
        },
    },
    {
        "id": "q3-3-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie die These des Autors, Entwicklungsländern helfe „Handel statt Hilfe“ mehr als staatliche Entwicklungszusammenarbeit. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Pro: Erfolgsbeispiele Ostasiens und Bangladeschs (Exporterlöse, Jobs und Rücküberweisungen übertreffen die Entwicklungsgelder deutlich) [3]; Fehlanreize und Abhängigkeit durch Hilfe, Korruption, Geberinteressen [2]; Marktöffnung (z. B. „Alles außer Waffen“) als wirksames Instrument; Stärkung der Eigenverantwortung.",
                "Kontra: Die ärmsten Länder (z. B. Niger, Äthiopien) haben kaum wettbewerbsfähige Exportsektoren, oft Binnenlage und Konflikte – Handel allein reicht nicht; Gesundheit, Bildung und Infrastruktur entstehen oft erst durch öffentliche Investitionen und Hilfe (auch Bangladesch profitierte von NGOs und Weltbank); Handel ohne Standards kann zu Ausbeutung führen (Rana Plaza), Wachstum verbessert Standards nicht automatisch [5]; globale Herausforderungen (Klima, Pandemien) erfordern öffentliche Gelder; Kürzungen treffen akut Bedürftige (humanitäre Hilfe 2025 laut OECD um über ein Drittel gesunken).",
                "Abwägung: Handel und Hilfe als Ergänzung („Aid for Trade“), Qualität statt Quantität der EZ, Kohärenz von Handels-, Agrar- und Entwicklungspolitik.",
                "Begründetes eigenes Urteil nach Kriterien (z. B. Wirksamkeit, Gerechtigkeit, Nachhaltigkeit, Eigenverantwortung); unterschiedliche Ergebnisse sind möglich, wenn sie schlüssig begründet werden.",
            ],
            "hinweis": "Erörtern: Pro und Kontra abwägen und zu einem eigenen Urteil gelangen; Materialbezüge zu M3 sowie gern Belege aus der Fallstudie Bangladesch.",
        },
        "bewertung": {
            "ausreichend": "Argumente für und gegen die These ansatzweise strukturiert abgewogen werden und ein nachvollziehbares Urteil vorliegt.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und abwägend ist, unterschiedliche Ländergruppen differenziert betrachtet und in ein schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q3-3-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie die Entscheidung, Bangladeschs Austritt aus der Gruppe der am wenigsten entwickelten Länder (LDC) auf das Jahr 2029 zu verschieben. (M1, M2)",
        "material": ["m1", "m2"],
        "loesung": {
            "punkte": [
                "Kriterien: wirtschaftliche Stabilität, soziale Folgen, Anreize für Reformen, Gerechtigkeit gegenüber anderen armen Ländern.",
                "Sachlage: LDC-Kriterien erfüllt (Einkommen, Humanvermögen, Verwundbarkeit); Austritt ursprünglich zum 24. November 2026, Aufschub auf den 24. November 2029; Präferenzen wie der zollfreie EU-Zugang entfallen erst nach einer Übergangsfrist; zusätzlicher Druck durch US-Zölle seit 2025 [3], [6].",
                "Für den Aufschub: Die einseitige Exportstruktur (über 80 % Bekleidung) [2] macht den Verlust der Zollfreiheit riskant, vor allem für Arbeitsplätze von Frauen [1]; politischer Umbruch und neue Regierung brauchen Zeit [4]; Klimarisiken [5]; Strukturschwächen laut M2 (6,8 Schuljahre, 44,3 % in der Landwirtschaft).",
                "Gegen den Aufschub: Der Reformdruck sinkt, Diversifizierung und Produktivitätssteigerung werden verschoben [6]; die Indikatoren (HDI, Armut, BNE; M2) zeigen, dass Bangladesch deutlich vor den ärmsten Ländern liegt; Vorteile sollten den Ärmsten (z. B. Niger, Äthiopien) zugutekommen; Signalwirkung für andere Länder.",
                "Begründetes Urteil, z. B.: Aufschub vertretbar, wenn er mit konkreten Reformschritten und einer Strategie für den Übergang (z. B. zu APS+) verbunden wird.",
            ],
            "hinweis": "Beurteilen: kriteriengeleitetes, begründetes Sachurteil auf Basis von Fachwissen mit Bezügen zu M1 und M2.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einzelnen Argumenten und Bezügen zu M1 oder M2 formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, mit Belegen aus M1 und M2 fachlich fundiert und schlüssig begründet ist.",
        },
    },
    {
        "id": "q3-3-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Entwerfen Sie ein Positionspapier (ca. eine Seite) einer Nichtregierungsorganisation, das Vorschläge für eine nachhaltige deutsche Entwicklungspolitik gegenüber Bangladesch macht und dabei Zielkonflikte offenlegt. (M1, M3)",
        "material": ["m1", "m3"],
        "loesung": {
            "punkte": [
                "Form: Adressat (z. B. BMZ, Bundestagsausschuss, Öffentlichkeit), Titel, klare Gliederung (Ausgangslage – Ziele – Forderungen – Begründung), sachlich-appellativer Stil; die NGO-Perspektive ist erkennbar.",
                "Ausgangslage: Fortschritte und Probleme Bangladeschs (M1), Kürzungen der Entwicklungsgelder (M3), Aufschub des LDC-Austritts bis 2029 [6].",
                "Mögliche Forderungen: Unterstützung bei Löhnen, Arbeitsstandards, Gewerkschaftsrechten und Gebäudesicherheit; Klimaanpassung und erneuerbare Energien; Bildung und Berufsbildung zur Diversifizierung der Wirtschaft; faire Handelsbedingungen und begleiteter Übergang nach dem LDC-Austritt (z. B. APS+); wirksame Lieferkettengesetze; Stärkung der lokalen Zivilgesellschaft; keine weiteren Kürzungen bzw. Rückkehr zum 0,7-%-Ziel.",
                "Zielkonflikte offenlegen: Löhne vs. Wettbewerbsfähigkeit, Wachstum vs. Klima- und Umweltschutz, Standards vs. Rückzug von Unternehmen, Konditionalität vs. Souveränität, Hilfe vs. Eigenverantwortung (Auseinandersetzung mit der Position in M3).",
                "Begründung der Forderungen mit Fachwissen (SDGs, Dimensionen der Nachhaltigkeit, Akteure und Mittel) und Bezügen zu M1 und M3.",
            ],
            "hinweis": "Gestalten/entwerfen: produktorientierte Aufgabe. Bewertet werden fachliche Fundierung, Adressatenbezug, Merkmale der Textsorte, Kohärenz und die ausdrückliche Thematisierung von Zielkonflikten.",
        },
        "bewertung": {
            "ausreichend": "ein erkennbares Positionspapier mit einigen fachlich zutreffenden Vorschlägen vorliegt und mindestens ein Zielkonflikt benannt wird.",
            "gut": "das Positionspapier adressatengerecht und schlüssig aufgebaut ist, fachlich fundierte Vorschläge mit Material- und Fachbezug begründet und mehrere Zielkonflikte reflektiert.",
        },
    },
    {
        "id": "q3-3-iii4",
        "afb": "III",
        "operator": "überprüfen",
        "lk": True,
        "text": "Überprüfen Sie die These, Unterentwicklung sei vor allem auf endogene Faktoren wie schlechte Regierungsführung zurückzuführen. (M1, M2)",
        "material": ["m1", "m2"],
        "loesung": {
            "punkte": [
                "Klärung: endogene vs. exogene Faktoren; die These entspricht Modernisierungs- und Institutionenansätzen (Good Governance, Acemoglu/Robinson).",
                "Stützende Belege: Korruption und autoritäre Herrschaft in Bangladesch [4]; Unterschiede zwischen Ländern mit ähnlichen äußeren Bedingungen (z. B. Vietnam vs. Bangladesch, M2); Ressourcenfluch zeigt die Bedeutung von Institutionen (Botswana vs. andere Rohstoffländer); der Erfolg Bangladeschs beruht auch auf eigenen Akteuren (NGOs, Unternehmer) [2].",
                "Gegenbelege (exogen): Klimawandel als vor allem von Industrieländern verursachte Belastung [5]; Abhängigkeit von Weltmarktnachfrage, Zöllen und Präferenzen [3], [6]; koloniales Erbe; geografische Nachteile und Schulden (z. B. Niger als Binnenland mit sehr niedrigen Werten, M2); sinkende Entwicklungsgelder.",
                "Wechselwirkungen: Exogene Schocks schwächen Institutionen, schwache Institutionen erhöhen die Verwundbarkeit gegenüber Schocks (Teufelskreis).",
                "Ergebnis: Die These ist zu einseitig; eine multikausale Erklärung ist angemessener, wobei endogene Faktoren für die Frage, warum manche Länder aufholen und andere nicht, besonderes Gewicht haben können.",
            ],
            "hinweis": "Überprüfen: die These auf Grundlage von Fachkenntnissen (Erklärungsansätze) kritisch hinterfragen und begründet einschätzen; Material- und Länderbelege sind erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die These mit einzelnen endogenen und exogenen Faktoren ansatzweise überprüft und eine begründete Einschätzung formuliert wird.",
            "gut": "die These theoriegeleitet, mit Belegen aus M1 und M2 und unter Berücksichtigung von Wechselwirkungen differenziert überprüft und schlüssig eingeschätzt wird.",
        },
    },
]
