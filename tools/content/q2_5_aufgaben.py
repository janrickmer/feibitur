# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q2.5 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q2.5 (kein Schwerpunkt im Abitur 2027), insbesondere Entwicklung sozialstaatlicher Leistungen (Grundsicherung), Möglichkeiten und Grenzen steuerfinanzierter Sozialpolitik und Struktur des Bundeshaushalts; im LK Staatsverschuldung im europäischen Vergleich, nationale und europäische Schuldenregeln sowie Europäisierung der Finanzpolitik. Bezüge zu Q2.1 (Staatsverschuldung) und Q2.4 (Gerechtigkeitsbegriffe)."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Strenger ist nicht automatisch gerechter“ (2026)",
        "absaetze": [
            "Seit dem 1. Juli 2026 gibt es kein Bürgergeld mehr. Die Leistung für erwerbsfähige Menschen, die ihren Lebensunterhalt nicht selbst sichern können, heißt nun Grundsicherungsgeld. Der Bundestag hatte die Reform im März 2026 beschlossen. Die Koalition aus Union und SPD spricht von einer Rückkehr zum Grundsatz „Fördern und Fordern“, Kritiker sprechen von einer Rückkehr zu Hartz IV.",
            "Die Änderungen sind deutlich. Die Vermittlung in Arbeit hat wieder Vorrang vor Weiterbildung. Wer Pflichten verletzt, etwa eine zumutbare Arbeit ablehnt, muss mit einer Minderung des Regelbedarfs um 30 Prozent für drei Monate rechnen; wer wiederholt nicht erreichbar ist oder Arbeit verweigert, kann im Extremfall die Leistung ganz verlieren. Die einjährige Schonfrist für Erspartes entfällt, und hohe Wohnkosten werden stärker begrenzt. Am Regelbedarf selbst ändert sich nichts: Er liegt für Alleinstehende weiterhin bei 563 Euro im Monat.",
            "Für die Reform gibt es gute Gründe. Der Sozialstaat lebt von der Akzeptanz derer, die ihn mit Steuern und Beiträgen finanzieren. Viele Beschäftigte mit kleinem Einkommen fragen sich, warum sie arbeiten gehen, wenn andere ohne Gegenleistung kaum weniger haben. Wer die Hilfe der Gemeinschaft in Anspruch nimmt, darf auch zur Mitwirkung verpflichtet werden. Und angesichts des Fachkräftemangels kann es sich das Land kaum leisten, dass Menschen, die arbeiten könnten, dauerhaft ohne Job bleiben.",
            "Doch die Debatte hat eine Schieflage. Ein großer Teil der Menschen in der Grundsicherung kann gar nicht ohne Weiteres eine Vollzeitstelle antreten: Kinder, Menschen, die Angehörige pflegen oder kleine Kinder betreuen, chronisch Kranke und Erwerbstätige, deren Lohn nicht zum Leben reicht. Nur ein kleiner Teil der Leistungsberechtigten verweigert hartnäckig jede Mitwirkung. Strengere Sanktionen treffen deshalb wenige – erzeugen aber bei vielen Angst und in den Jobcentern zusätzliche Bürokratie.",
            "Hinzu kommt: Das Existenzminimum ist kein Gnadenakt, sondern ein Grundrecht. Das Bundesverfassungsgericht hat 2019 Kürzungen von mehr als 30 Prozent in der damaligen Form für unvereinbar mit dem Grundgesetz erklärt. Ob ein vollständiger Wegfall der Leistung, wie ihn das neue Gesetz in Extremfällen erlaubt, vor Gericht Bestand hat, ist unter Juristen umstritten. Und während die Regelsätze 2025 und 2026 nicht stiegen, wurde vieles im Alltag teurer – real haben die Betroffenen weniger.",
            "Wer Menschen dauerhaft in Arbeit bringen will, braucht mehr als Druck: Kinderbetreuung, Gesundheitsangebote, Sprachkurse und Weiterbildung, die zu stabilen Jobs führt, statt zur schnellen Vermittlung in den nächsten befristeten Aushilfsjob. Das kostet zunächst Geld – doch im Regierungsentwurf für den Haushalt 2027 sinken die Mittel für die Grundsicherung für Arbeitsuchende sogar leicht. Gerecht ist ein Sozialstaat, der Leistung anerkennt und zugleich niemanden fallen lässt. Strenger ist nicht automatisch gerechter.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Sozialpolitik-Redakteurin (2026). Die Angaben zur Reform (Bundestagsbeschluss vom 5.3.2026, Inkrafttreten zum 1.7.2026), zum Regelbedarf (563 Euro, Stand 2026), zum Haushaltsentwurf 2027 und zum Urteil des Bundesverfassungsgerichts vom 5.11.2019 (1 BvL 7/16) sind real.",
    },
    {
        "id": "m2",
        "titel": "M2: Bundeshaushalt 2025–2027: ausgewählte Kennzahlen (in Mrd. Euro)",
        "typ": "tabelle",
        "kopf": ["Kennzahl", "2025 (Soll)", "2026 (Soll)", "2027 (Regierungsentwurf)"],
        "zeilen": [
            ["Ausgaben insgesamt", "502,6", "524,5", "555,4"],
            ["darunter: Arbeit und Soziales (Einzelplan 11)", "190,3", "197,3", "201,5"],
            ["– davon Leistungen an die Rentenversicherung", "122,5", "127,4", "132,0"],
            ["– davon Grundsicherung für Arbeitsuchende", "52,0", "51,0", "50,8"],
            ["darunter: Verteidigung (Einzelplan 14)", "62,3", "82,7", "109,7"],
            ["darunter: Zinsausgaben", "–", "rund 30", "41,9"],
            ["Investitionen (Kernhaushalt)", "62,7", "58,3", "56,3"],
            ["Steuereinnahmen", "386,8", "387,2", "394,7"],
            ["Nettokreditaufnahme (Kernhaushalt)", "81,8", "98,0", "118,7"],
            ["– davon im Rahmen der regulären Schuldenregel", "–", "40,4", "33,4"],
            ["– davon über die Bereichsausnahme (Verteidigung u. a.)", "–", "57,6", "85,4"],
        ],
        "quelle": "Eigene Zusammenstellung nach Angaben des Deutschen Bundestages (Textarchiv): Beschluss des Haushaltsgesetzes 2026 am 28.11.2025 (Werte 2025 und 2026: Soll) sowie erste Lesung des Haushaltsentwurfs 2027 vom 8. bis 11.9.2026 (Regierungsentwurf, Kabinettsbeschluss vom 6.7.2026; Beratungen im Bundestag bei Redaktionsschluss im November 2026 noch nicht abgeschlossen). Werte gerundet; „–“ = hier nicht ausgewiesen. Nicht enthalten sind die Kredite der Sondervermögen (2026: Bundeswehr 25,5 Mrd. Euro, Infrastruktur und Klimaneutralität 58,1 Mrd. Euro).",
    },
    {
        "id": "m3",
        "titel": "M3: Staatsverschuldung und Haushaltssalden ausgewählter EU-Staaten (in % des BIP)",
        "typ": "tabelle",
        "kopf": ["Staat", "Schuldenquote 2022", "Schuldenquote 2025", "Saldo 2024", "Saldo 2025"],
        "zeilen": [
            ["EU (27 Staaten)", "82,3", "81,5", "−3,1", "−3,1"],
            ["Euroraum (20 Staaten)", "89,2", "87,7", "−3,0", "−3,0"],
            ["Deutschland", "64,1", "62,8", "−2,7", "−2,9"],
            ["Frankreich", "111,4", "115,7", "−5,8", "−5,1"],
            ["Italien", "138,4", "136,7", "−3,4", "−3,1"],
            ["Griechenland", "177,8", "145,4", "+1,4", "+2,0"],
            ["Spanien", "109,3", "100,5", "−3,2", "−2,4"],
            ["Portugal", "111,2", "89,2", "+0,7", "+0,7"],
            ["Belgien", "103,3", "108,1", "−4,4", "−5,2"],
            ["Österreich", "78,1", "80,7", "−4,6", "−4,1"],
            ["Finnland", "74,1", "88,4", "−4,4", "−3,8"],
            ["Niederlande", "48,4", "44,7", "−0,7", "−1,6"],
            ["Polen", "48,8", "59,6", "−6,4", "−7,2"],
            ["Dänemark", "33,4", "27,2", "+4,1", "+2,9"],
        ],
        "quelle": "Eurostat, Euro-Indikatoren vom 21.10.2026 (zweite Meldung 2026 im Verfahren bei einem übermäßigen Defizit; Daten 2022–2025). Saldo = Finanzierungsdefizit (−) bzw. -überschuss (+) des Gesamtstaates. Euroraum in der Abgrenzung von 2025 (ohne Bulgarien, das den Euro seit 1.1.2026 verwendet). Referenzwerte des Stabilitäts- und Wachstumspakts: Defizit höchstens 3 %, Schuldenstand höchstens 60 % des BIP.",
    },
]

AUFGABEN = [
    {
        "id": "q2-5-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung: Kommentar einer (fiktiven) Sozialpolitik-Redakteurin, „Strenger ist nicht automatisch gerechter“, 2026; Thema: Bewertung der Neuen Grundsicherung (Grundsicherungsgeld).",
            "punkte": [
                "Seit 1. Juli 2026 ersetze das Grundsicherungsgeld das Bürgergeld; Bundestagsbeschluss im März 2026; Koalition sieht Rückkehr zu „Fördern und Fordern“, Kritiker zu Hartz IV [1].",
                "Inhalte: Vorrang der Vermittlung, Minderung um 30 % für drei Monate bei Pflichtverletzungen, im Extremfall vollständiger Wegfall, Wegfall der Schonfrist für Vermögen, Begrenzung der Wohnkosten; Regelbedarf unverändert 563 Euro [2].",
                "Argumente für die Reform: Akzeptanz bei Steuer- und Beitragszahlern, Lohnabstand, Mitwirkungspflicht als Gegenleistung, Fachkräftemangel [3].",
                "Kritik: Viele Leistungsberechtigte könnten nicht ohne Weiteres arbeiten (Kinder, Pflegende, Kranke, Aufstocker); nur wenige verweigerten die Mitwirkung; Sanktionen erzeugten Angst und Bürokratie [4].",
                "Existenzminimum als Grundrecht; BVerfG 2019; verfassungsrechtliche Zweifel an der Vollsanktion; realer Kaufkraftverlust durch Nullrunden [5].",
                "Forderung nach Förderung (Betreuung, Gesundheit, Sprache, Weiterbildung) statt bloßem Druck; Kritik an sinkenden Mitteln im Entwurf 2027; Fazit: Gerechtigkeit verlange Anerkennung von Leistung und Schutz aller [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache, keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen weitgehend vollständig, strukturiert, in eigenen Worten und unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q2-5-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Entwicklung zentraler Einnahmen und Ausgaben des Bundeshaushalts von 2025 bis 2027. (M2)",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle mit ausgewählten Kennzahlen des Bundeshaushalts (Soll 2025 und 2026, Regierungsentwurf 2027) in Mrd. Euro, eigene Zusammenstellung nach Angaben des Deutschen Bundestages.",
            "punkte": [
                "Gesamtausgaben steigen von 502,6 über 524,5 auf 555,4 Mrd. Euro (rund +10 % in zwei Jahren).",
                "Arbeit und Soziales bleibt größter Einzelplan (190,3 auf 201,5 Mrd.), sein Anteil sinkt aber leicht (von knapp 38 % auf gut 36 %); Leistungen an die Rentenversicherung steigen (122,5 auf 132,0 Mrd.), die Grundsicherung für Arbeitsuchende sinkt leicht (52,0 auf 50,8 Mrd.).",
                "Verteidigung wächst am stärksten (62,3 auf 109,7 Mrd., rund +76 %); Zinsausgaben steigen von rund 30 auf 41,9 Mrd. Euro.",
                "Investitionen im Kernhaushalt sinken (62,7 auf 56,3 Mrd.).",
                "Steuereinnahmen stagnieren nahezu (386,8 auf 394,7 Mrd., rund +2 %); ihr Deckungsanteil an den Ausgaben sinkt von rund 77 % auf rund 71 %.",
                "Nettokreditaufnahme steigt von 81,8 über 98,0 auf 118,7 Mrd.; der Anteil über die Bereichsausnahme wächst (57,6 auf 85,4 Mrd.), während der Spielraum der regulären Schuldenregel sinkt (40,4 auf 33,4 Mrd.).",
                "Hinweis auf Datenlage: 2027 nur Regierungsentwurf; Sondervermögen nicht enthalten.",
            ],
            "hinweis": "Beschreiben: Entwicklungen strukturiert und fachsprachlich darlegen, mit genauen Zahlenbelegen; Tendenzen (steigend, sinkend, stagnierend) benennen, aber noch nicht erklären oder bewerten. Einfache Rechenschritte (Veränderungsraten, Anteile) sind erwünscht.",
        },
        "bewertung": {
            "ausreichend": "die wichtigsten Entwicklungen im Ansatz korrekt und mit einzelnen Zahlenbelegen beschrieben werden.",
            "gut": "die Entwicklungen strukturiert, vollständig und mit präzisen Zahlenbelegen (einschließlich Anteilen bzw. Veränderungsraten) beschrieben werden.",
        },
    },
    {
        "id": "q2-5-i3",
        "afb": "I",
        "operator": "darstellen",
        "text": "Stellen Sie die Gestaltungsprinzipien der sozialen Sicherung in Deutschland (Versicherungs-, Versorgungs- und Fürsorgeprinzip) sowie das Solidaritäts- und das Subsidiaritätsprinzip dar.",
        "material": [],
        "loesung": {
            "punkte": [
                "Versicherungsprinzip: Leistungen aufgrund vorheriger Beiträge, Rechtsanspruch ohne Bedürftigkeitsprüfung; Finanzierung durch Beiträge von Beschäftigten und Arbeitgebern (plus Bundeszuschüsse); Beispiele: fünf Zweige der Sozialversicherung; ggf. Äquivalenzprinzip in der Rentenversicherung.",
                "Versorgungsprinzip: steuerfinanzierte Leistungen ohne eigene Beiträge für besondere Dienste oder Opfer für die Gemeinschaft; Beispiele: Beamtenversorgung, Soziale Entschädigung.",
                "Fürsorgeprinzip: steuerfinanzierte Hilfe bei individueller Bedürftigkeit nach Prüfung von Einkommen und Vermögen, nachrangig; Beispiele: Grundsicherungsgeld, Sozialhilfe, Grundsicherung im Alter.",
                "Solidaritätsprinzip: gemeinsame Tragung von Risiken, Umverteilung von Starken zu Schwachen (z. B. GKV: Beitrag nach Einkommen, Leistung nach Bedarf; beitragsfreie Familienversicherung).",
                "Subsidiaritätsprinzip: Vorrang der Eigenverantwortung und kleinerer Gemeinschaften, Staat hilft nachrangig; Bedeutung für Nachrang der Fürsorge und Rolle der Wohlfahrtsverbände.",
                "Zusammenhang: Prinzipien ergänzen sich und werden in vielen Leistungen kombiniert; verfassungsrechtliche Grundlage im Sozialstaatsprinzip (Art. 20 Abs. 1 GG).",
            ],
            "hinweis": "Darstellen: Sachverhalte und ihre Zusammenhänge aufzeigen; Beispiele und Fachbegriffe werden erwartet, eine Bewertung nicht.",
        },
        "bewertung": {
            "ausreichend": "die Prinzipien im Ansatz zutreffend und mit einzelnen Beispielen dargestellt werden.",
            "gut": "alle Prinzipien fachlich präzise, mit passenden Beispielen und unter Herausarbeitung ihrer Zusammenhänge dargestellt werden.",
        },
    },
    {
        "id": "q2-5-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 die Neuregelung der Grundsicherung im Spannungsfeld von Bedarfs- und Leistungsgerechtigkeit.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Begriffsklärung: Bedarfsgerechtigkeit (jeder erhält, was er für ein menschenwürdiges Leben braucht; Existenzminimum, Art. 1 i. V. m. Art. 20 GG) vs. Leistungsgerechtigkeit (Gegenleistung und Lohnabstand; wer arbeitet, soll mehr haben).",
                "Elemente der Reform mit Leistungsgerechtigkeits-Logik: Vermittlungsvorrang, Mitwirkungspflichten, 30-%-Minderung, Vollsanktion in Extremfällen, Wegfall der Vermögens-Karenzzeit [2], [3].",
                "Begründungen: Akzeptanz des Sozialstaats bei Steuer- und Beitragszahlern, Lohnabstand, Arbeitsanreize angesichts des Fachkräftemangels [3].",
                "Bedarfsgerechtigkeits-Einwände: Existenzminimum als Grundrecht, BVerfG 2019 (mehr als 30 % in damaliger Form unvereinbar), Betroffenheit von Kindern und Nicht-Erwerbsfähigen bzw. eingeschränkt Erwerbsfähigen, realer Kaufkraftverlust durch Nullrunden [4], [5].",
                "Beispielhafte Veranschaulichung, z. B. Alleinerziehende mit Kleinkind (Zumutbarkeit ab dem 14. Lebensmonat des Kindes) oder Aufstocker im Niedriglohnbereich.",
                "Ggf. Chancengerechtigkeit als vermittelnder Maßstab (Förderung durch Qualifizierung, Kinderbetreuung) [6].",
            ],
            "hinweis": "Erläutern: Zusammenhang zwischen Reformelementen und Gerechtigkeitsbegriffen mit zusätzlichen Informationen und Beispielen veranschaulichen; Materialbelege erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Neuregelung ansatzweise den Gerechtigkeitsbegriffen zugeordnet und mit einem Beispiel erläutert wird.",
            "gut": "die Neuregelung differenziert, mit präzisen Begriffen, Materialbezügen und anschaulichen Beispielen im Spannungsfeld beider Gerechtigkeitsvorstellungen erläutert wird.",
        },
    },
    {
        "id": "q2-5-ii2",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie M2 im Hinblick auf Möglichkeiten und Grenzen steuerfinanzierter Sozialpolitik.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Sozialausgaben als größter Block: Arbeit und Soziales über ein Drittel des Haushalts; hoher Anteil steuerfinanzierter Leistungen an die Rentenversicherung (u. a. für versicherungsfremde Leistungen) und für die Grundsicherung.",
                "Möglichkeiten: Bund stabilisiert über Zuschüsse die Rentenversicherung (Entlastung der Beitragssätze, Generationenvertrag), finanziert die Grundsicherung unabhängig von Beiträgen (Bedarfsgerechtigkeit).",
                "Grenze Einnahmeseite: Steuereinnahmen stagnieren nahezu, während die Ausgaben deutlich steigen; wachsende Lücke wird über Kredite geschlossen.",
                "Grenze Konkurrenz im Haushalt: stark steigende Verteidigungs- und Zinsausgaben, sinkende Investitionen im Kernhaushalt; Leistungen an die Rentenversicherung wachsen demografiebedingt automatisch (gebundene Ausgaben).",
                "Grenze Schuldenbremse: regulärer Kreditspielraum sinkt (40,4 auf 33,4 Mrd.); die Bereichsausnahme gilt nur für Verteidigung u. a., nicht für Sozialausgaben – Sozialpolitik muss sich im Rahmen der regulären Regel finanzieren.",
                "Folgerungen: Druck auf Leistungen (leichte Kürzung bei der Grundsicherung), Debatten über Steuererhöhungen, Umschichtungen oder Reformen der Sozialversicherungen.",
            ],
            "hinweis": "Analysieren: Daten kriteriengeleitet (Möglichkeiten/Grenzen) erschließen und mit Zahlenbelegen versehen; Fachwissen zu Schuldenbremse, Bundeszuschüssen und demografischem Wandel einbeziehen.",
        },
        "bewertung": {
            "ausreichend": "die Tabelle ansatzweise im Hinblick auf Möglichkeiten und Grenzen steuerfinanzierter Sozialpolitik ausgewertet und mit einzelnen Zahlen belegt wird.",
            "gut": "die Tabelle kriteriengeleitet, mit präzisen Zahlenbelegen und unter Einbezug von Fachwissen (Schuldenbremse, gebundene Ausgaben, Demografie) analysiert wird.",
        },
    },
    {
        "id": "q2-5-ii3",
        "afb": "II",
        "operator": "auswerten",
        "text": "Werten Sie die Tabelle (M3) im Hinblick auf die Staatsverschuldung Deutschlands im europäischen Vergleich aus.",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle nach Eurostat (Oktober 2026) zu Schuldenquoten 2022 und 2025 sowie Haushaltssalden 2024 und 2025 ausgewählter EU-Staaten in % des BIP.",
            "punkte": [
                "Deutschland: Schuldenquote sinkt von 64,1 % auf 62,8 %, liegt damit deutlich unter EU (81,5 %) und Euroraum (87,7 %), aber über dem Referenzwert von 60 %; Defizit steigt von 2,7 % auf 2,9 % und liegt knapp unter 3 %.",
                "Hochverschuldete Staaten: Griechenland (145,4 %), Italien (136,7 %), Frankreich (115,7 %), Belgien (108,1 %), Spanien (100,5 %).",
                "Unterschiedliche Trends: deutlicher Abbau in Griechenland (−32,4 Prozentpunkte, mit Überschüssen) und Portugal (−22,0 Punkte, Überschüsse); Anstieg in Frankreich, Belgien, Finnland, Österreich und Polen bei hohen Defiziten (z. B. Polen −7,2 %, Belgien −5,2 %, Frankreich −5,1 %).",
                "Niedrig verschuldete Staaten: Dänemark (27,2 %, Überschuss), Niederlande (44,7 %).",
                "EU und Euroraum insgesamt mit Defiziten von etwa 3 % und Schuldenquoten weit über 60 %: Referenzwerte werden im Durchschnitt verfehlt.",
                "Gesamtaussage: Deutschland gehört zu den solideren Staaten mit vergleichsweise niedriger, leicht sinkender Schuldenquote, nähert sich beim Defizit aber der 3-%-Grenze; angesichts der stark steigenden Kreditaufnahme des Bundes ab 2026 (Bereichsausnahme, Sondervermögen) dürfte sich die Quote künftig erhöhen.",
            ],
            "hinweis": "Auswerten: Daten zu einer Gesamtaussage zusammenführen; Vergleich mit Referenzwerten und anderen Staaten sowie Unterscheidung von Bestands- (Schuldenquote) und Stromgröße (Saldo) erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Daten ansatzweise zutreffend ausgewertet werden und eine einfache Gesamtaussage zu Deutschland formuliert wird.",
            "gut": "die Daten differenziert und mit präzisen Belegen ausgewertet werden (Referenzwerte, Trends, Bestands- und Stromgrößen) und in eine schlüssige Gesamtaussage münden.",
        },
    },
    {
        "id": "q2-5-ii4",
        "afb": "II",
        "operator": "erläutern",
        "lk": True,
        "text": "Erläutern Sie die nationalen und europäischen Regeln zur Begrenzung der Staatsverschuldung und ordnen Sie die Daten aus M3 in diesen Rahmen ein.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Schuldenbremse (Art. 109, 115 GG, seit 2009): strukturelle Neuverschuldung des Bundes höchstens 0,35 % des BIP, Konjunkturkomponente, Notlagenklausel mit Tilgungsplan.",
                "Reform 2025: Bereichsausnahme für Verteidigungs- und bestimmte Sicherheitsausgaben oberhalb von 1 % des BIP; Sondervermögen Infrastruktur und Klimaneutralität bis 500 Mrd. Euro (Art. 143h GG); Kreditspielraum der Länder von zusammen 0,35 % des BIP.",
                "Stabilitäts- und Wachstumspakt: Referenzwerte 3 % Defizit und 60 % Schuldenstand; Defizitverfahren.",
                "Reform 2024: mittelfristige Pläne mit Nettoausgabenpfad, Anpassungszeitraum vier (bis sieben) Jahre, Mindestabbau der Schuldenquote (1 bzw. 0,5 Prozentpunkte pro Jahr), Ziel strukturelles Defizit 1,5 %; nationale Ausweichklausel für Verteidigung (bis 1,5 % des BIP).",
                "Einordnung M3: Deutschland erfüllt das Defizitkriterium knapp (−2,9 %), verfehlt das Schuldenstandskriterium leicht (62,8 %) und müsste nach den neuen Regeln die Quote moderat senken; Frankreich, Belgien, Polen, Österreich, Finnland verletzen das Defizitkriterium, Griechenland, Italien, Frankreich, Belgien, Spanien liegen über 90 % (strengere Mindestabbau-Vorgabe).",
                "Spannung: höhere Verteidigungsausgaben und Sondervermögen erhöhen künftig die Verschuldung; nationale und europäische Regeln sind nicht deckungsgleich.",
            ],
            "hinweis": "Erläutern: Regeln mit konkreten Zahlen und Beispielen veranschaulichen; die Einordnung der Daten muss nachvollziehbar und materialgestützt erfolgen.",
        },
        "bewertung": {
            "ausreichend": "nationale und europäische Schuldenregeln in Grundzügen zutreffend erläutert und einzelne Daten aus M3 eingeordnet werden.",
            "gut": "beide Regelwerke einschließlich der Reformen 2024 und 2025 präzise erläutert und die Daten aus M3 differenziert und zutreffend eingeordnet werden.",
        },
    },
    {
        "id": "q2-5-iii1",
        "afb": "III",
        "operator": "Stellung nehmen",
        "text": "Nehmen Sie Stellung zur These der Autorin, strengere Regeln machten die Grundsicherung nicht automatisch gerechter. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klärung der These und der Position der Autorin: Anerkennung berechtigter Reformgründe, aber Vorrang von Förderung und Existenzsicherung [3]–[6].",
                "Argumente für die These: Grundrecht auf Existenzminimum, verfassungsrechtliche Risiken der Vollsanktion; Sanktionen treffen wenige, belasten viele; Betroffenheit von Kindern; Kaufkraftverlust; Nachhaltigkeit der Integration durch Qualifizierung statt schneller Vermittlung.",
                "Argumente gegen die These: Leistungsgerechtigkeit und Lohnabstand; Akzeptanz des Sozialstaats; Mitwirkung als legitime Gegenleistung; Signalwirkung von Pflichten; Fachkräftemangel; Missbrauchsvermeidung und Fairness gegenüber Geringverdienern.",
                "Ggf. Differenzierung: Gerechtigkeit hängt von der Ausgestaltung ab (Härtefallregeln, Schutz psychisch Erkrankter, Förderangebote, Kinderbetreuung).",
                "Offenlegung eigener Wertmaßstäbe (z. B. Vorrang der Bedarfs- oder der Leistungsgerechtigkeit, Eigenverantwortung vs. Solidarität) und klare, begründete Position.",
            ],
            "hinweis": "Stellung nehmen: wie beurteilen, zusätzlich müssen die eigenen Wertmaßstäbe ausdrücklich dargelegt werden. Bezug zu den Gerechtigkeitsbegriffen (Q2.4) und zum Material ist zu erwarten.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit erkennbaren eigenen Maßstäben und Bezug zum Material vorliegt.",
            "gut": "die Stellungnahme Pro- und Contra-Argumente fachlich fundiert abwägt, die eigenen Wertmaßstäbe ausdrücklich offenlegt und in ein klares, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q2-5-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie, ob die in M2 erkennbare Haushaltsentwicklung dem Ziel der Generationengerechtigkeit entspricht.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien klären, z. B. Lastenverteilung zwischen Generationen (Schulden, Zinsen), Zukunftsvorsorge (Investitionen, Bildung, Klimaschutz), Sicherheit als Vorleistung für künftige Generationen, Tragfähigkeit der Sozialsysteme.",
                "Gegen Generationengerechtigkeit: stark steigende Nettokreditaufnahme (81,8 auf 118,7 Mrd.) und Zinsausgaben (rund 30 auf 41,9 Mrd.) engen künftige Spielräume ein; Investitionen im Kernhaushalt sinken; wachsende Rentenzuschüsse begünstigen Ältere, Lasten tragen Jüngere.",
                "Für Generationengerechtigkeit (bzw. relativierend): Verteidigungsausgaben sichern Freiheit und Sicherheit auch künftiger Generationen; Investitionen laufen zusätzlich über das Sondervermögen (nicht in M2 enthalten); Schuldenquote Deutschlands im europäischen Vergleich niedrig; unterlassene Investitionen wären ebenfalls eine Last.",
                "Berücksichtigung der Datenlage: 2027 nur Entwurf, Sondervermögen außerhalb des Kernhaushalts.",
                "Kriteriengeleitetes, begründetes Gesamturteil.",
            ],
            "hinweis": "Beurteilen: Sachurteil auf Basis ausdrücklich genannter Kriterien und präziser Zahlenbelege aus M2; Fachwissen (Schuldenbremse, Sondervermögen, demografischer Wandel) einbeziehen.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einzelnen Zahlenbelegen formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, mit präzisen Belegen und unter Einbezug von Fachwissen schlüssig begründet wird.",
        },
    },
    {
        "id": "q2-5-iii3",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie die These, der Sozialstaat in Deutschland stoße an die Grenzen seiner Finanzierbarkeit. (M1, M2)",
        "material": ["m1", "m2"],
        "loesung": {
            "punkte": [
                "Klärung: Finanzierbarkeit ökonomisch (Einnahmen, Schulden, Demografie) und politisch (Akzeptanz, Prioritäten) verstehen.",
                "Pro: Sozialleistungsquote rund 32 % des BIP (2025); Arbeit und Soziales über ein Drittel des Bundeshaushalts; demografisch bedingt steigende Rentenzuschüsse (M2); stagnierende Steuereinnahmen, wachsende Kredite und Zinsen; steigende Beitragssätze (z. B. Zusatzbeiträge der Krankenkassen); Konkurrenz mit Verteidigung und Investitionen; Akzeptanzprobleme (M1 [3]).",
                "Contra: Finanzierbarkeit ist eine politische Prioritätenfrage; Spielräume über Steuerpolitik (z. B. Vermögen, Erbschaften), Bürgerversicherung, Effizienzgewinne (z. B. Bündelung von Leistungen, Bürokratieabbau), höhere Erwerbsbeteiligung; Grundsicherung ist im Gesamtbudget ein vergleichsweise kleiner Posten und sinkt sogar leicht (M2, M1 [6]); Sozialstaat als Stabilisator und Standortfaktor.",
                "Abwägung nach Kriterien (z. B. Nachhaltigkeit, Gerechtigkeit, wirtschaftliche Effekte) mit Bezug auf beide Materialien.",
                "Eigenes, begründetes Urteil (auch differenzierte Positionen, z. B. Reformbedarf ohne grundsätzliche Unfinanzierbarkeit).",
            ],
            "hinweis": "Erörtern: These unter Abwägen von Pro- und Kontraargumenten hinterfragen und zu einem eigenen Urteil gelangen; Belege aus M1 und M2 sowie Fachwissen erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist, Argumente beider Seiten enthält und in ein nachvollziehbares Urteil mündet.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und materialgestützt ist und in ein klares, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q2-5-iii4",
        "afb": "III",
        "operator": "diskutieren",
        "lk": True,
        "text": "Diskutieren Sie, ob die Europäische Union nach dem Vorbild von NextGenerationEU dauerhaft gemeinsame Schulden aufnehmen sollte, etwa für Verteidigung und Klimaschutz. Beziehen Sie M3 ein.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Klärung: NextGenerationEU (2020, bis zu 750 Mrd. Euro in Preisen von 2018, Zuschüsse und Kredite, Rückzahlung bis 2058) und SAFE (2025, bis 150 Mrd. Euro Kredite für Rüstungsbeschaffung) als Präzedenzfälle; bisher befristet und zweckgebunden.",
                "Pro: europäische öffentliche Güter (Verteidigung, Klimaschutz, Netze) effizienter gemeinsam finanzierbar; günstige Finanzierungsbedingungen der EU; Entlastung hochverschuldeter Staaten (M3: Italien, Frankreich, Griechenland) ohne Gefährdung ihrer Tragfähigkeit; Stabilisierung des Euroraums und Solidarität in Krisen; Stärkung der Handlungsfähigkeit der EU.",
                "Contra: Haftungs- und Transferunion, Moral Hazard (Staaten mit hohen Defiziten in M3 hätten geringeren Konsolidierungsdruck); No-bail-out-Klausel (Art. 125 AEUV) und Kompetenzgrenzen; Budgetrecht der nationalen Parlamente, BVerfG-Maßstäbe (Urteil 2022); fehlende eigene Steuerquellen für die Rückzahlung; Deutschland mit vergleichsweise niedriger Schuldenquote (62,8 %) trüge hohe Lasten.",
                "Abwägung mit Kriterien (Effektivität, Legitimität, Solidarität, Stabilität) und mögliche Zwischenlösungen (zweckgebunden, befristet, mit Konditionalität und eigenen Einnahmequellen).",
                "Begründete Bewertung.",
            ],
            "hinweis": "Diskutieren: Argumentation entwickeln, die zu einer begründeten Bewertung führt; Bezug zu den Daten in M3 und zur Europäisierung der Finanzpolitik erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Diskussion ansatzweise strukturiert ist, Argumente beider Seiten nennt und in eine nachvollziehbare Bewertung mündet.",
            "gut": "die Diskussion fachlich fundiert, materialgestützt und abwägend ist und in eine klare, schlüssig begründete Bewertung mündet.",
        },
    },
]
