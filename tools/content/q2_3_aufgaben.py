# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q2.3 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q2.3, insbesondere Folgen und Ursachen von Inflation und Deflation, geldpolitische Ziele und Strategien der Europäischen Zentralbank sowie Kontroversen um Mandat und Autonomie von Zentralbanken (Bezug zu Q2.1: Inflation als Problem nachfrageorientierter Politik)."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Interview „Wir dürfen die Fehler von 2022 nicht wiederholen“ (2026)",
        "absaetze": [
            "<b>Frage:</b> Die EZB hat im Juni und im September die Leitzinsen angehoben, obwohl die Wirtschaft im Euroraum nur langsam wächst. Ist das nicht widersinnig? <b>Antwort:</b> Nein. Die Inflationsrate im Euroraum ist im September auf 3,8 Prozent gestiegen, die Energiepreise lagen fast 19 Prozent über dem Vorjahr. Die EZB hat ein klares Mandat: Preisstabilität geht vor. Ihr Ziel sind 2 Prozent auf mittlere Sicht. Wenn sie jetzt nichts tut, setzt sie ihre Glaubwürdigkeit aufs Spiel.",
            "<b>Frage:</b> Aber gegen teures Öl kann eine Zentralbank doch nichts ausrichten. <b>Antwort:</b> Direkt nicht, das stimmt. Ein Energiepreisschock ist ein Angebotsschock. Die Gefahr liegt in den Folgewirkungen: Wenn Unternehmen ihre höheren Kosten weitergeben und Gewerkschaften zum Ausgleich höhere Löhne fordern, entsteht eine Lohn-Preis-Spirale. Diese Zweitrundeneffekte muss die EZB verhindern, und dafür sind die Inflationserwartungen entscheidend.",
            "<b>Frage:</b> Sie spielen auf 2022 an? <b>Antwort:</b> Genau. Damals hat die EZB den Preisanstieg zu lange für vorübergehend gehalten und die Zinsen erst im Juli 2022 erhöht, als die Inflation schon bei über acht Prozent lag. Danach musste sie umso kräftiger bremsen – bis auf einen Einlagesatz von vier Prozent. Diesmal hat sie früher reagiert, und bisher liegen die längerfristigen Inflationserwartungen bei rund zwei Prozent.",
            "<b>Frage:</b> Höhere Zinsen treffen aber Familien, die bauen wollen, Unternehmen und hoch verschuldete Staaten. <b>Antwort:</b> Das ist der Preis. Kredite werden teurer, Investitionen werden aufgeschoben, das Wachstum leidet. Genau das ist der Wirkungsmechanismus: Die Nachfrage wird gedämpft, damit der Preisauftrieb nicht auf andere Güter übergreift. Für hoch verschuldete Staaten steigen die Finanzierungskosten. Doch die EZB darf ihre Politik nicht danach ausrichten, ob sich Finanzminister günstig verschulden können – dafür gibt es das Verbot der Staatsfinanzierung. Sollten die Zinsen einzelner Länder ungerechtfertigt auseinanderlaufen, hat sie mit dem TPI ein eigenes Instrument.",
            "<b>Frage:</b> Viele Regierungen, auch die deutsche, entlasten die Bürger mit Steuersenkungen auf Kraftstoffe. Hilft das? <b>Antwort:</b> Kurzfristig senkt das die gemessene Inflation, weil die Preise an der Zapfsäule sinken. Aber es stützt die Nachfrage genau in dem Moment, in dem die EZB sie dämpfen will, und es kostet Milliarden. Besser wären gezielte Hilfen für Haushalte mit niedrigen Einkommen. Geld- und Fiskalpolitik dürfen nicht gegeneinander arbeiten.",
            "<b>Frage:</b> Kritiker sagen, die EZB würge die Erholung ab. <b>Antwort:</b> Diese Gefahr besteht, wenn sie überzieht. Deshalb entscheidet sie von Sitzung zu Sitzung anhand der Daten und hat die Zinsen im Oktober unverändert gelassen. Ein Einlagesatz von 2,5 Prozent ist auch kein Würgegriff: Bei einer Inflation von fast vier Prozent ist der reale Zins sogar negativ. Gefährlicher wäre es, wenn die Menschen das Vertrauen in einen stabilen Euro verlören.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasstes Interview mit einer fiktiven Wirtschaftswissenschaftlerin (November 2026). Die genannten Daten und Zinsentscheidungen entsprechen den Angaben der EZB und von Eurostat (Stand: 29.10.2026).",
    },
    {
        "id": "m2",
        "titel": "M2: Inflationsraten und Leitzinsen der EZB 2019–2026",
        "typ": "tabelle",
        "kopf": [
            "Jahr",
            "Inflationsrate Euroraum (HVPI, in %)",
            "Inflationsrate Deutschland (HVPI, in %)",
            "Einlagesatz der EZB zum Jahresende (in %)",
            "Hauptrefinanzierungssatz der EZB zum Jahresende (in %)",
        ],
        "zeilen": [
            ["2019", "1,2", "1,4", "−0,50", "0,00"],
            ["2020", "0,3", "0,4", "−0,50", "0,00"],
            ["2021", "2,6", "3,2", "−0,50", "0,00"],
            ["2022", "8,4", "8,7", "2,00", "2,50"],
            ["2023", "5,4", "6,0", "4,00", "4,50"],
            ["2024", "2,4", "2,5", "3,00", "3,15"],
            ["2025", "2,1", "2,3", "2,00", "2,15"],
            ["2026 (aktuell)", "3,8 (September)", "3,3 (September)", "2,50 (seit 16.09.)", "2,65 (seit 16.09.)"],
        ],
        "quelle": "Inflationsraten 2019–2025: Jahresdurchschnitte nach Eurostat (prc_hicp_aind) bzw. EZB Data Portal; 2026: Veränderung gegenüber dem Vorjahresmonat (Euroraum: EZB/Eurostat; Deutschland: Destatis, Pressemitteilung vom 13.10.2026). Leitzinsen: EZB-Leitzinstabelle, Stand nach dem Beschluss vom 29.10.2026 (Zinsen unverändert). Zum Vergleich: Höchststand der Inflation im Euroraum im Oktober 2022 mit 10,6 %.",
    },
    {
        "id": "m3",
        "titel": "M3: Kommentar „Unabhängig – aber von wem?“ (2026)",
        "absaetze": [
            "Im August 2025 versuchte der US-Präsident, die Fed-Gouverneurin Lisa Cook mit sofortiger Wirkung aus dem Amt zu entfernen. Monatelang hatte er die amerikanische Notenbank zuvor öffentlich gedrängt, die Zinsen kräftig zu senken. Erst der Supreme Court stoppte den Versuch vorläufig: Ende Juni 2026 entschied er, dass Cook vorerst im Amt bleiben darf, weil ihr der Präsident weder den Grund für die Abberufung genannt noch Gelegenheit zur Stellungnahme gegeben hatte – und dass Gerichte prüfen dürfen, ob ein „wichtiger Grund“ vorliegt. Endgültig entschieden ist der Streit noch nicht.",
            "Europäer sollten darauf nicht mit Überheblichkeit blicken. Auch die Europäische Zentralbank steht unter Druck – nur leiser. In Deutschland klagten Bürger jahrelang gegen die Anleihekäufe der EZB. 2020 erklärte das Bundesverfassungsgericht Beschlüsse zum Staatsanleihekaufprogramm PSPP für kompetenzwidrig, weil die EZB deren Verhältnismäßigkeit nicht dargelegt habe, und stellte sich damit gegen ein Urteil des Europäischen Gerichtshofs. In anderen Ländern wiederum wird der EZB vorgeworfen, mit hohen Zinsen hoch verschuldete Staaten in Bedrängnis zu bringen.",
            "Dabei gibt es gute Gründe für unabhängige Notenbanken. Regierungen sind versucht, vor Wahlen mit billigem Geld die Konjunktur anzuheizen – die Rechnung in Form von Inflation kommt später. Viele Studien zeigen, dass Länder mit unabhängigen Zentralbanken im Durchschnitt niedrigere Inflationsraten haben. Deshalb ist die Unabhängigkeit der EZB in den EU-Verträgen verankert und kann nur mit Zustimmung aller Mitgliedstaaten geändert werden.",
            "Doch Unabhängigkeit ist kein Freibrief. Die EZB trifft Entscheidungen mit enormen Verteilungswirkungen: Niedrige Zinsen und Anleihekäufe ließen in den 2010er-Jahren Aktien- und Immobilienpreise steigen, während Sparer kaum Zinsen bekamen. Hohe Zinsen verteuern heute Kredite für Familien und Unternehmen. Solche Entscheidungen trifft ein Rat aus 27 Mitgliedern, die niemand direkt gewählt hat. Je mehr die EZB tut, desto lauter wird die Frage nach ihrer demokratischen Legitimation.",
            "Hinzu kommt ein Konstruktionsproblem. Das Mandat der EZB ist eng: Vorrang hat die Preisstabilität, alles andere ist nachrangig. Die amerikanische Fed muss dagegen gleichrangig für stabile Preise und maximale Beschäftigung sorgen. In einer Lage wie der aktuellen, in der ein Energiepreisschock die Preise treibt und zugleich das Wachstum bremst, zwingt das enge Mandat die EZB, vor allem auf die Inflation zu schauen – auch wenn die Konjunktur darunter leidet.",
            "Ich plädiere deshalb für einen ehrlichen Neuanfang: Die EU sollte das Mandat der EZB um ein gleichrangiges Beschäftigungsziel erweitern und im Gegenzug die Kontrolle durch das Europäische Parlament stärken, etwa durch Anhörungen mit echten Konsequenzen. Mit dem angekündigten Rücktritt von EZB-Präsidentin Christine Lagarde im Februar 2027 ist der Zeitpunkt für diese Debatte günstig. Eine Zentralbank, die von den Bürgerinnen und Bürgern verstanden und getragen wird, ist am Ende unabhängiger als eine, die sich hinter Paragraphen versteckt.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Autors (November 2026). Die genannten Ereignisse sind real: Versuch der Abberufung von Fed-Gouverneurin Lisa Cook (August 2025), Entscheidung des US Supreme Court in Trump v. Cook (29.06.2026), Urteil des Bundesverfassungsgerichts vom 5. Mai 2020 (2 BvR 859/15 u. a.), angekündigter Rücktritt von EZB-Präsidentin Lagarde zum 7. Februar 2027 (EZB-Pressemitteilung vom 29.10.2026).",
    },
]

AUFGABEN = [
    {
        "id": "q2-3-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen der Expertin im Interview zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Interview), Titel „Wir dürfen die Fehler von 2022 nicht wiederholen“, Erscheinungsjahr (2026), Interviewte (fiktive Wirtschaftswissenschaftlerin) und Thema (Zinserhöhungen der EZB während des Energiepreisschocks 2026).",
            "punkte": [
                "Die Expertin verteidigt die Zinserhöhungen im Juni und September 2026 mit der gestiegenen Inflation (3,8 %) und dem Vorrang der Preisstabilität; Untätigkeit gefährde die Glaubwürdigkeit der EZB [1].",
                "Gegen den Energiepreisschock als Angebotsschock könne die EZB direkt nichts tun, sie müsse aber Zweitrundeneffekte und eine Lohn-Preis-Spirale verhindern; entscheidend seien die Inflationserwartungen [2].",
                "Aus 2022 habe die EZB gelernt: Damals habe sie zu spät reagiert und dann umso stärker erhöhen müssen; diesmal seien die Erwartungen bei rund 2 % verankert geblieben [3].",
                "Höhere Zinsen dämpften bewusst die Nachfrage und belasteten Kreditnehmer und Staaten; die EZB dürfe aber keine Rücksicht auf Finanzierungskosten der Staaten nehmen (Verbot der Staatsfinanzierung), für ungerechtfertigte Zinsunterschiede gebe es das TPI [4].",
                "Steuersenkungen auf Kraftstoffe senkten kurzfristig die gemessene Inflation, stützten aber die Nachfrage und seien teuer; besser seien gezielte Hilfen; Geld- und Fiskalpolitik müssten zusammenwirken [5].",
                "Die Gefahr des Abwürgens bestehe nur bei Überziehen; die EZB entscheide datenabhängig, der Realzins sei negativ; ein Vertrauensverlust in den Euro sei gefährlicher [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturiert, komprimiert, eigene Worte und indirekte Rede; keine Wertung. Die Frage-Antwort-Struktur soll nicht nacherzählt, sondern inhaltlich gebündelt werden.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen der Expertin im Ansatz korrekt und mit Einleitungssatz zusammengefasst werden.",
            "gut": "die Aussagen der Expertin weitgehend vollständig, strukturiert, in eigenen Worten und unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q2-3-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Entwicklung der Inflationsraten und der Leitzinsen der EZB von 2019 bis 2026 (M2).",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle zu Inflationsraten (HVPI) im Euroraum und in Deutschland sowie zu Einlagesatz und Hauptrefinanzierungssatz der EZB, 2019–2026; Quellen EZB, Eurostat, Destatis.",
            "punkte": [
                "2019–2020: niedrige Inflation (Euroraum 1,2 % bzw. 0,3 %), deutlich unter dem 2-%-Ziel; Einlagesatz negativ (−0,50 %), Hauptrefinanzierungssatz 0 %.",
                "2021–2022: starker Anstieg der Inflation (Euroraum 2,6 %, dann 8,4 %; Deutschland 3,2 % und 8,7 %); Leitzinsen erst 2022 angehoben (Einlagesatz Ende 2022: 2,00 %).",
                "2023: Inflation geht zurück (5,4 % bzw. 6,0 %), Leitzinsen erreichen ihren Höchststand (Einlagesatz 4,00 %, Hauptrefinanzierungssatz 4,50 %).",
                "2024–2025: Inflation nähert sich dem Ziel (2,4/2,1 % im Euroraum); Leitzinsen werden gesenkt (Einlagesatz Ende 2025: 2,00 %).",
                "2026: erneuter Inflationsanstieg (September: 3,8 % im Euroraum, 3,3 % in Deutschland) und Zinserhöhung auf 2,50 % (Einlagesatz).",
                "Vergleich: Deutschland meist leicht über dem Euroraum-Durchschnitt (Ausnahme 2026); Zinsen folgen der Inflation mit zeitlicher Verzögerung; Hinweis auf unterschiedliche Bezugsgrößen 2026 (Monatswert statt Jahresdurchschnitt).",
            ],
            "hinweis": "Beschreiben: Entwicklung strukturiert, phasenweise und mit Zahlenbelegen darstellen; Erklärungen der Ursachen gehören in AFB II. Methodische Hinweise (Jahresdurchschnitt vs. Monatswert) werten auf.",
        },
        "bewertung": {
            "ausreichend": "die Entwicklung von Inflation und Leitzinsen im Ansatz korrekt und mit einzelnen Zahlenbelegen beschrieben wird.",
            "gut": "die Entwicklung strukturiert nach Phasen, fachsprachlich präzise und mit treffenden Zahlenbelegen einschließlich des Vergleichs Deutschland – Euroraum beschrieben wird.",
        },
    },
    {
        "id": "q2-3-i3",
        "afb": "I",
        "operator": "darstellen",
        "text": "Stellen Sie ausgehend von M1 die Ziele, die geldpolitische Strategie und die Instrumente der Europäischen Zentralbank dar.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Ziel: vorrangig Preisstabilität (Art. 127 AEUV, Art. 88 GG); nachrangig Unterstützung der allgemeinen Wirtschaftspolitik der EU; Bezug M1: „Preisstabilität geht vor“ [1].",
                "Strategie: symmetrisches Inflationsziel von 2 % (HVPI) auf mittlere Sicht (Strategieüberprüfung 2021, bestätigt 2025); wirtschaftliche sowie monetäre und finanzielle Analyse; datenabhängige Entscheidungen von Sitzung zu Sitzung [6].",
                "Leitzinsen als Hauptinstrument: Einlagesatz (2,50 %), Hauptrefinanzierungssatz (2,65 %), Spitzenrefinanzierungssatz (2,90 %); Steuerung über den Einlagesatz [1], [6].",
                "Weitere Instrumente: Offenmarktgeschäfte, ständige Fazilitäten, Mindestreserve (1 %), Anleihekäufe (APP, PEPP), Transmission Protection Instrument (TPI) [4].",
                "Rahmenbedingungen: Unabhängigkeit (Art. 130 AEUV) und Verbot der monetären Staatsfinanzierung (Art. 123 AEUV) [4]; Kommunikation und Erwartungssteuerung [2], [3].",
            ],
            "hinweis": "Darstellen: Sachverhalte und ihre Zusammenhänge strukturiert aufzeigen; Materialbezüge und Fachwissen verbinden; keine Bewertung.",
        },
        "bewertung": {
            "ausreichend": "Ziele, Strategie und einige Instrumente der EZB im Ansatz korrekt dargestellt werden.",
            "gut": "Ziele, Strategie und Instrumente vollständig, strukturiert und fachsprachlich präzise dargestellt und mit dem Material verknüpft werden.",
        },
    },
    {
        "id": "q2-3-ii1",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie mögliche Ursachen und Folgen der in M2 erkennbaren Inflationsentwicklung.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "2019/2020: sehr niedrige Inflation durch schwache Nachfrage, Corona-Einbruch, sinkende Energiepreise; Gefahr der Deflation (Euroraum Ende 2020 zeitweise negativ) – Folgen: Kaufzurückhaltung, Expansionskurs der EZB (Negativzins, Anleihekäufe).",
                "2021/2022: Nachholeffekte nach der Pandemie und staatliche Stützung (Nachfrage), Lieferengpässe und Energiepreisschock nach dem russischen Angriff auf die Ukraine (Angebot/Kosten, importierte Inflation); späte Zinswende.",
                "2023–2025: Rückgang durch sinkende Energiepreise, aufgelöste Lieferengpässe und die Wirkung der Zinserhöhungen (Transmission mit Verzögerung).",
                "2026: erneuter Anstieg durch den Energiepreisschock infolge des Iran-Kriegs (Kraftstoffe, Heizöl) – Angebotsschock; Gefahr von Zweitrundeneffekten.",
                "Folgen der Inflation: Kaufkraftverlust, Umverteilung von Gläubigern/Sparern zu Schuldnern, Belastung niedriger Einkommen, Verteilungskonflikte und Lohnforderungen, Unsicherheit; Reaktion der EZB mit Zinserhöhungen und Folgen für Kredite, Investitionen und Staatsfinanzen.",
                "Belege aus M2 (z. B. Höchstwerte 2022, Zinsanstieg bis 4 % 2023, 2026 3,8 % bzw. 3,3 %).",
            ],
            "hinweis": "Erklären: Daten auf Ursachen (Nachfrage-, Kosten-, Erwartungsfaktoren) und Wirkungszusammenhänge zurückführen; Materialbelege erforderlich. Die Einordnung als Angebots- oder Nachfrageinflation darf vereinfacht erfolgen (Theorien sind LK-Stoff).",
        },
        "bewertung": {
            "ausreichend": "einzelne Ursachen und Folgen der Inflationsentwicklung ansatzweise zutreffend erklärt und mit M2 belegt werden.",
            "gut": "Ursachen und Folgen differenziert nach Phasen erklärt, fachlich korrekt auf Wirkungszusammenhänge zurückgeführt und durchgängig mit Daten aus M2 belegt werden.",
        },
    },
    {
        "id": "q2-3-ii2",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie, wie eine Leitzinserhöhung der EZB auf das Preisniveau wirken soll, und gehen Sie dabei auf die in M1 angesprochenen Zielkonflikte ein.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Zinskanal: Leitzins steigt, Geldmarkt- und Bankzinsen steigen; Kredite teurer, Sparen attraktiver; weniger Konsum und Investitionen (z. B. Wohnungsbau) [4].",
                "Weitere Kanäle: Vermögenspreise sinken, Euro wertet tendenziell auf (Importe billiger), Erwartungskanal: Glaubwürdigkeit senkt Inflationserwartungen und dämpft Lohn- und Preissetzung [2], [3].",
                "Ergebnis: sinkende Gesamtnachfrage, nachlassender Preisauftrieb; Wirkungsverzögerung von meist ein bis zwei Jahren; Realzins entscheidend (bei 2,5 % Zins und 3,8 % Inflation negativ) [6].",
                "Zielkonflikt Preisstabilität – Wachstum/Beschäftigung: Zinserhöhungen dämpfen auch Investitionen und Wachstum; Gefahr, die Erholung abzuwürgen [4], [6].",
                "Zielkonflikt bei Angebotsschocks: Die EZB kann den Ölpreis nicht beeinflussen; sie bekämpft Zweitrundeneffekte und verstärkt dabei die Wachstumsschwäche [2].",
                "Konflikt mit Fiskalpolitik und Staatsfinanzen: steigende Finanzierungskosten hoch verschuldeter Staaten, Gefahr auseinanderlaufender Zinsen (TPI); Kraftstoffsteuersenkungen stützen die Nachfrage, die die EZB dämpfen will [4], [5].",
            ],
            "hinweis": "Erläutern: Wirkungskette mit Beispielen und zusätzlichen Informationen veranschaulichen; Zielkonflikte müssen ausdrücklich mit Bezug zu M1 behandelt werden.",
        },
        "bewertung": {
            "ausreichend": "die Wirkung einer Zinserhöhung ansatzweise zutreffend erläutert und mindestens ein Zielkonflikt aus M1 aufgegriffen wird.",
            "gut": "der Transmissionsmechanismus mit mehreren Kanälen fachlich präzise erläutert und die Zielkonflikte differenziert und materialgestützt einbezogen werden.",
        },
    },
    {
        "id": "q2-3-ii3",
        "afb": "II",
        "operator": "herausarbeiten",
        "text": "Arbeiten Sie die Argumente heraus, die der Autor von M3 für und gegen die bestehende Ausgestaltung der Unabhängigkeit und des Mandats der EZB anführt.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Ausgangspunkt: Beispiel Fed – politischer Druck und Abberufungsversuch zeigen die Verwundbarkeit der Unabhängigkeit [1]; auch die EZB stehe unter Druck (PSPP-Urteil, Kritik aus hoch verschuldeten Staaten) [2].",
                "Für Unabhängigkeit: Schutz vor Missbrauch der Geldpolitik vor Wahlen, Zusammenhang zwischen Unabhängigkeit und niedriger Inflation, vertragliche Absicherung [3].",
                "Gegen die bisherige Ausgestaltung: Verteilungswirkungen der Geldpolitik (Vermögenspreise, Sparer, Kreditnehmer) und fehlende direkte demokratische Legitimation des EZB-Rats [4].",
                "Konstruktionsproblem des engen, hierarchischen Mandats im Vergleich zum dualen Mandat der Fed, besonders bei Angebotsschocks [5].",
                "Forderung: gleichrangiges Beschäftigungsziel und stärkere Kontrolle durch das Europäische Parlament; Anlass Nachfolge Lagarde [6].",
                "Nicht explizit, aber erschließbar: Der Autor verbindet Unabhängigkeit mit Akzeptanz („getragen“) und sieht Legitimation als Voraussetzung für dauerhafte Unabhängigkeit; er befürwortet Unabhängigkeit grundsätzlich, will aber das Mandat erweitern und die Kontrolle stärken.",
            ],
            "hinweis": "Herausarbeiten: auch nicht ausdrücklich genannte Zusammenhänge erschließen (z. B. die Spannung zwischen Unabhängigkeit und Legitimation, die implizite Position des Autors); Absatzbelege erforderlich.",
        },
        "bewertung": {
            "ausreichend": "zentrale Argumente des Autors für und gegen die bestehende Ausgestaltung ansatzweise zutreffend und mit Belegen herausgearbeitet werden.",
            "gut": "die Argumente vollständig, strukturiert und mit Absatzbelegen herausgearbeitet und die implizite Position des Autors schlüssig erschlossen werden.",
        },
    },
    {
        "id": "q2-3-ii4",
        "afb": "II",
        "operator": "vergleichen",
        "lk": True,
        "text": "Vergleichen Sie die Geldpolitik der Europäischen Zentralbank und der US-Notenbank Fed hinsichtlich Mandat, Strategie, Instrumenten und Unabhängigkeit. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Mandat: EZB hierarchisch (vorrangig Preisstabilität, Art. 127 AEUV) vs. Fed dual (maximale Beschäftigung und stabile Preise, Federal Reserve Act) [5].",
                "Strategie: beide 2 % Inflationsziel; EZB symmetrisch, mittelfristig, HVPI (Überprüfungen 2021/2025); Fed 2 % gemessen am PCE-Index, Strategie 2025 überarbeitet; beide inzwischen Zinssteuerung statt Geldmengenzielen (Bundesbank-Tradition, Volcker-Phase).",
                "Instrumente: EZB drei Leitzinsen (Einlagesatz 2,50 %), Offenmarktgeschäfte, Mindestreserve, APP/PEPP, TPI; Fed Zielspanne der Federal Funds Rate (3,75–4,00 %), Quantitative Easing seit 2008; beide 2026 mit Zinserhöhungen.",
                "Entscheidungsgremien: EZB-Rat (27 Mitglieder, 21 Staaten, Rotation) vs. FOMC (12 Stimmen); Rücksicht der EZB auf 21 Volkswirtschaften und Staatsanleihemärkte.",
                "Unabhängigkeit: EZB durch EU-Verträge stark geschützt (Änderung nur einstimmig), Konflikte eher juristisch (PSPP-Urteil) [2]; Fed per Gesetz geschützt, aber offener politischer Druck (Fall Cook, Supreme Court 2026) [1].",
                "Fazit: Gemeinsamkeiten (Inflationsziel, Instrumente, Unabhängigkeit) und Unterschiede (Mandat, Rechtsgrundlage, Währungsraum) begründet gegenübergestellt; Folgen für die Praxis (Fed reagiert in Krisen oft früher mit Zinssenkungen).",
            ],
            "hinweis": "Vergleichen (LK): kriteriengeleitet Gemeinsamkeiten und Unterschiede begründet darlegen; ein bloßes Nacheinander beider Zentralbanken genügt nicht für eine gute Leistung.",
        },
        "bewertung": {
            "ausreichend": "EZB und Fed anhand einzelner Kriterien ansatzweise zutreffend verglichen werden.",
            "gut": "der Vergleich anhand aller vier Kriterien fachlich präzise, mit Gemeinsamkeiten und Unterschieden sowie Material- und Aktualitätsbezug erfolgt.",
        },
    },
    {
        "id": "q2-3-ii5",
        "afb": "II",
        "operator": "anwenden",
        "lk": True,
        "text": "Wenden Sie die Theorien der Nachfrage- und der Angebotsinflation sowie die Quantitätstheorie auf die in M2 dargestellte Inflationsentwicklung von 2021 bis 2026 an.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Nachfrageinflation: Nachholkonsum nach der Pandemie, Ersparnisse und staatliche Stützungsprogramme erhöhten 2021/22 die Nachfrage bei knappen Kapazitäten; Beitrag zum Anstieg 2021 (2,6 %) und 2022.",
                "Angebotsinflation: Lieferengpässe und Energiepreisschock 2022 (Krieg gegen die Ukraine) als Kostendruck und importierte Inflation; 2026 erneuter Energiepreisschock (Iran-Krieg) mit Anstieg auf 3,8 % im September; mögliche Gewinninflation als Diskussionspunkt.",
                "Zweitrundeneffekte: Lohnforderungen 2023/24 hielten die Inflation zeitweise hoch (Kerninflation), obwohl Energiepreise sanken.",
                "Quantitätstheorie: starke Ausweitung der Geldmenge 2020/21 (Anleihekäufe, PEPP) bei gesunkener Wirtschaftsleistung – monetaristische Deutung als Vorlauf der Inflation 2022; Anwendung von M · V = P · Y.",
                "Grenzen der Quantitätstheorie: Geldmengenausweitung der 2010er-Jahre ohne Inflation (schwankende Umlaufgeschwindigkeit); 2026 kein vorheriger Geldmengenboom, sondern Kostenschock.",
                "Schlussfolgerung: Mischung der Ursachen; Konsequenzen für die Geldpolitik (bei Angebotsschocks Dilemma, Fokus auf Erwartungen; Zinserhöhungen wirken vor allem gegen Nachfrageinflation).",
            ],
            "hinweis": "Anwenden (LK): Theorien korrekt wiedergeben und begründet auf konkrete Phasen in M2 beziehen; Fachwissen über die Ereignisse 2021–2026 erforderlich.",
        },
        "bewertung": {
            "ausreichend": "mindestens zwei Theorien im Ansatz korrekt auf einzelne Phasen der Inflationsentwicklung in M2 angewendet werden.",
            "gut": "alle drei Theorien fachlich korrekt und differenziert auf die Phasen in M2 angewendet, ihre Erklärungskraft verglichen und Grenzen reflektiert werden.",
        },
    },
    {
        "id": "q2-3-iii1",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie, ob die Zinserhöhungen der EZB im Jahr 2026 eine angemessene Reaktion auf den Energiepreisschock sind. (M1, M2)",
        "material": ["m1", "m2"],
        "loesung": {
            "punkte": [
                "Kriterien: Mandatstreue (Preisstabilität, Inflationsziel), Wirksamkeit gegenüber der Art der Inflation, Nebenwirkungen (Wachstum, Beschäftigung, Staatsfinanzen), Glaubwürdigkeit und Erwartungen.",
                "Für die Zinserhöhungen: Inflation deutlich über dem Ziel (3,8 % im September, M2), Gefahr von Zweitrundeneffekten und Lohn-Preis-Spirale, Lehre aus der späten Reaktion 2022, Verankerung der Erwartungen, moderates Zinsniveau und negativer Realzins (M1 [2], [3], [6]).",
                "Gegen die Zinserhöhungen: Angebotsschock, gegen den Zinsen nicht direkt helfen; Kerninflation moderat (Deutschland Oktober 2026: 2,1 %); Wirkungsverzögerung – Schock könnte vorbei sein, bevor die Zinsen wirken; Dämpfung einer schwachen Erholung; höhere Finanzierungskosten für Staaten und Unternehmen.",
                "Zusammenspiel mit der Fiskalpolitik: breite Entlastungen (Kraftstoffsteuersenkungen) wirken gegenläufig; gezielte Hilfen würden die Geldpolitik entlasten (M1 [5]).",
                "Abwägung und begründetes Urteil (z. B. maßvolle Erhöhungen angemessen, weitere Erhöhungen nur bei Anzeichen von Zweitrundeneffekten; oder: Zinserhöhungen verfrüht).",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete Einschätzung auf Basis von Fachwissen und Materialbelegen aus M1 und M2; das Urteil kann in beide Richtungen ausfallen, muss aber begründet sein.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einzelnen Argumenten und Materialbezügen formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, fachlich fundiert (Angebotsschock, Zweitrundeneffekte, Transmission, Realzins) und schlüssig mit M1 und M2 begründet ist.",
        },
    },
    {
        "id": "q2-3-iii2",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie, ob die Unabhängigkeit der Europäischen Zentralbank demokratisch gerechtfertigt ist. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Begriffsklärung: institutionelle, personelle und finanzielle Unabhängigkeit (Art. 130 AEUV, Art. 88 GG); demokratische Legitimation über Verträge (ratifiziert von allen Parlamenten), Ernennung durch den Europäischen Rat, Berichtspflichten gegenüber dem Europäischen Parlament.",
                "Pro: Schutz vor kurzfristigen politischen Interessen (Wahlzyklen) [3]; Glaubwürdigkeit und niedrige Inflation; Selbstbindung der Demokratie (vergleichbar mit Verfassungsgerichten); Erfahrung mit politischem Druck in den USA [1]; enges Mandat begrenzt den Spielraum und damit den Legitimationsbedarf.",
                "Kontra: große Verteilungswirkungen ohne direkte Wahl [4]; Ausweitung der Aufgaben (Anleihekäufe, Krisenmanagement) über die klassische Geldpolitik hinaus; schwache Kontrolle durch das Parlament; Konflikte mit nationalem Verfassungsrecht (PSPP-Urteil) [2].",
                "Abwägung: Rechtfertigung hängt von engem Mandat, Transparenz und Rechenschaft ab; mögliche Reformen (mehr Transparenz, stärkere Anhörungen, klarere Grenzen für Anleihekäufe) [6].",
                "Begründetes eigenes Urteil.",
            ],
            "hinweis": "Erörtern: Pro- und Kontraargumente abwägen und zu einem eigenen Urteil gelangen; Bezug zu M3 und Fachwissen über Rechtsgrundlagen der EZB erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und materialbezogen ist und in ein klares, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q2-3-iii3",
        "afb": "III",
        "operator": "Stellung nehmen",
        "text": "Nehmen Sie Stellung zu der Forderung des Autors, das Mandat der EZB um ein gleichrangiges Beschäftigungsziel zu erweitern. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Klärung: Unterschied hierarchisches vs. duales Mandat; Umsetzung erfordert eine Vertragsänderung mit Zustimmung aller Mitgliedstaaten [3], [6].",
                "Pro: Geldpolitik wirkt ohnehin auf Beschäftigung; bei Angebotsschocks ausgewogenere Reaktion [5]; Vorbild Fed; größere Akzeptanz und Legitimation; Koordination mit Fiskalpolitik.",
                "Contra: Gefahr höherer Inflation und geringerer Glaubwürdigkeit; Politisierung der EZB; Beschäftigung hängt stark von Strukturfaktoren und nationalen Arbeitsmärkten ab, die eine einheitliche Geldpolitik kaum steuern kann; unterschiedliche Arbeitsmarktlagen in 21 Staaten; deutsche Stabilitätstradition; Erfahrungen mit politischem Druck auf die Fed [1].",
                "Mögliche Zwischenlösungen: stärkere Berücksichtigung im Rahmen des sekundären Mandats, mehr Transparenz und parlamentarische Kontrolle ohne Mandatserweiterung.",
                "Offenlegung der eigenen Wertmaßstäbe (z. B. Vorrang der Preisstabilität und Rechtssicherheit vs. Vorrang sozialer Ziele und demokratischer Gestaltung) und klare Position.",
            ],
            "hinweis": "Stellung nehmen: wie beurteilen, zusätzlich müssen die eigenen Wertmaßstäbe ausdrücklich begründet offengelegt werden; ohne sie ist der Operator nur teilweise erfüllt.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit erkennbaren eigenen Wertmaßstäben vorliegt.",
            "gut": "die Stellungnahme abwägend und fachlich fundiert ist, eigene Wertmaßstäbe ausdrücklich offenlegt und begründet und in eine klare Position mündet.",
        },
    },
]
