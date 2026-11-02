# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q4.1 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q4.1: Chancen und Risiken möglicher zukünftiger EU-Erweiterungen; Zielvorstellungen der Integration zwischen Staatenbund und Bundesstaat (Vertiefung und Erweiterung); Chancen und Grenzen des europäischen Parlamentarismus und zivilgesellschaftlicher Demokratie; (LK) Integrationstheorien. Kein Erlass-Schwerpunkt 2027, aber Bezüge zu Q1.1, Q1.2 und Q4.3."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Rede „Erweiterung braucht Reform – und zwar jetzt“ (2026)",
        "absaetze": [
            "Frau Präsidentin, liebe Kolleginnen und Kollegen, in diesem Jahr hat sich in der Erweiterungspolitik mehr bewegt als im ganzen Jahrzehnt davor. Im Juni wurde mit der Ukraine und der Republik Moldau endlich das erste Verhandlungscluster eröffnet, bis Mitte Oktober folgten drei weitere. Montenegro hat inzwischen 21 seiner 33 Verhandlungskapitel vorläufig abgeschlossen und will die Verhandlungen bis zum Jahresende beenden; auch Albanien kommt voran. Nach Jahren des Stillstands ist die Erweiterung wieder ein Versprechen, das die Union einlösen kann.",
            "Aber wir sollten ehrlich sein, warum es so lange gedauert hat. Zwei Jahre lang hat eine einzige Regierung die Öffnung der Cluster mit der Ukraine verhindert. Erst nach dem Regierungswechsel in Ungarn kam Bewegung in die Sache – und selbst danach knüpfte Budapest seine Zustimmung an eine bilaterale Minderheitenfrage. Im Fall Serbiens wiederum stellen sich mehrere Mitgliedstaaten quer. Wer so verhandelt, macht den Beitrittsprozess zur Geisel nationaler Einzelinteressen.",
            "Deshalb sage ich: Erweiterung und Vertiefung gehören zusammen. Eine Union mit mehr als 30 Mitgliedern kann nicht nach Regeln funktionieren, die einst für sechs Staaten geschrieben wurden. Die Kommission hat Anfang Oktober vorgeschlagen, über die Eröffnung von Verhandlungsclustern künftig mit qualifizierter Mehrheit zu entscheiden und mithilfe der Brückenklauseln der Verträge in ausgewählten Bereichen wie Sanktionen vom Einstimmigkeitsprinzip abzurücken. Das ist richtig, aber es reicht nicht. Auch in der Außen- und Sicherheitspolitik brauchen wir Mehrheitsentscheidungen, bevor neue Staaten beitreten – sonst vervielfachen wir die Zahl der Vetos.",
            "Zweitens müssen wir unsere Werte auch nach einem Beitritt besser schützen können. Die Erfahrung lehrt: Der Einfluss der Union ist vor dem Beitritt am größten. Das Verfahren nach Artikel 7 gegen Ungarn läuft seit 2018, ohne dass es je zu Sanktionen kam. Künftige Beitrittsverträge brauchen daher klare Schutzklauseln – bis hin zur Aussetzung von Stimmrechten, wenn ein neues Mitglied bei Demokratie und Rechtsstaatlichkeit zurückfällt.",
            "Drittens dürfen wir die Menschen in den Kandidatenländern nicht bis zum letzten Tag vor der Tür warten lassen. Wer Reformen umsetzt, soll schon vorher schrittweise am Binnenmarkt und an der Zusammenarbeit bei Energie, Verkehr und Verteidigung teilhaben. Das schafft sichtbare Vorteile und hält den Reformwillen wach.",
            "Mir ist bewusst, dass es Sorgen gibt – um die Agrarmittel, um die Kohäsionspolitik, um den Haushalt. Ein Beitritt der Ukraine würde die Verteilung der EU-Gelder grundlegend verändern. Diese Fragen müssen wir offen beantworten, und zwar im nächsten mehrjährigen Finanzrahmen ab 2028, nicht erst am Tag des Beitritts. Wer aber glaubt, eine Union ohne Erweiterung sei billiger, irrt: Instabilität an unseren Grenzen kostet am Ende mehr.",
            "Die Erweiterung ist unsere geopolitische Antwort auf den russischen Angriffskrieg. Aber sie ist kein Gnadenakt, sondern ein Leistungsversprechen in beide Richtungen: Die Kandidaten erfüllen die Kriterien – und wir machen die Union fit für ihre Aufnahme. Beides zusammen, und zwar jetzt.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasste Rede einer fiktiven Europaabgeordneten im Europäischen Parlament (Oktober 2026). Die genannten Ereignisse sind real (Stand: Oktober 2026): Eröffnung der Cluster 1, 6, 2 und 3 mit der Ukraine und Moldau am 15. Juni, 14. Juli und 13. Oktober 2026; Stand Montenegro am 12. Oktober 2026; Mitteilung der Europäischen Kommission „Preparing for a wider Union“ vom 6. Oktober 2026.",
    },
    {
        "id": "m2",
        "titel": "M2: Stand der Beitrittsprozesse ausgewählter Kandidatenländer (Ende Oktober 2026)",
        "typ": "tabelle",
        "kopf": ["Land", "Beitrittsantrag", "Kandidatenstatus", "Beginn der Verhandlungen", "Stand der Verhandlungen"],
        "zeilen": [
            ["Montenegro", "2008", "2010", "2012", "alle 33 Kapitel eröffnet, 21 vorläufig geschlossen; Entwurf des Beitrittsvertrags in Arbeit"],
            ["Albanien", "2009", "2014", "2022", "alle 33 Kapitel eröffnet, 4 vorläufig geschlossen"],
            ["Serbien", "2009", "2012", "2014", "22 von 35 Kapiteln eröffnet, 2 vorläufig geschlossen; seit 2021 kein neues Cluster eröffnet"],
            ["Ukraine", "2022", "2022", "2024", "4 von 6 Clustern eröffnet (alle im Jahr 2026)"],
            ["Republik Moldau", "2022", "2022", "2024", "4 von 6 Clustern eröffnet (alle im Jahr 2026)"],
            ["Nordmazedonien", "2004", "2005", "2022", "kein Cluster eröffnet (Streit um Verfassungsänderung zugunsten der bulgarischen Minderheit)"],
            ["Bosnien und Herzegowina", "2016", "2022", "Grundsatzbeschluss 2024", "noch keine erste Regierungskonferenz"],
            ["Georgien", "2022", "2023", "–", "Prozess laut Europäischem Rat seit 2024 „de facto gestoppt“"],
            ["Türkei", "1987", "1999", "2005", "16 Kapitel eröffnet, 1 vorläufig geschlossen; seit 2018 Stillstand"],
        ],
        "quelle": "Eigene Zusammenstellung nach Angaben der Europäischen Kommission (Generaldirektion Erweiterung und Östliche Nachbarschaft), des Rates der EU und der Regierungen der Kandidatenländer; Stand: Ende Oktober 2026. Potenzieller Kandidat (nicht aufgeführt): Kosovo (Antrag 2022).",
    },
    {
        "id": "m3",
        "titel": "M3: Interview „Ein Parlament mit angezogener Handbremse?“ (2026)",
        "absaetze": [
            "<b>Frau Dr. Brandt, bei der Europawahl 2024 lag die Wahlbeteiligung EU-weit bei gut 50 Prozent. Ist das ein Erfolg?</b> Im Vergleich zu 2014, als nicht einmal 43 Prozent wählen gingen, schon. In Deutschland waren es fast 65 Prozent, auch weil erstmals 16-Jährige wählen durften. Aber in vielen Staaten bleibt die Europawahl eine Nebenwahl: Die Parteien führen nationale Wahlkämpfe, und viele Wählerinnen und Wähler nutzen die Wahl, um ihrer Regierung einen Denkzettel zu verpassen.",
            "<b>Mit dem Spitzenkandidatenprinzip sollte die Wahl doch europäischer werden.</b> Die Idee ist gut: Wer die Wahl gewinnt, soll die Kommission führen – ähnlich wie bei uns die Kanzlerkandidaten. 2014 hat das mit Jean-Claude Juncker funktioniert. 2019 haben die Staats- und Regierungschefs dann aber Ursula von der Leyen vorgeschlagen, die gar nicht angetreten war. 2024 war sie Spitzenkandidatin der Europäischen Volkspartei und wurde mit 401 Stimmen wiedergewählt. Rechtlich verbindlich ist das Prinzip bis heute nicht; der Europäische Rat muss das Wahlergebnis nur ‚berücksichtigen‘.",
            "<b>Was fehlt dem Europäischen Parlament zu einem ‚richtigen‘ Parlament?</b> Vor allem das Recht, selbst Gesetze vorzuschlagen. Das Initiativrecht liegt bei der Kommission; das Parlament kann sie nur auffordern, einen Vorschlag vorzulegen. 2026 hat das Parlament eine überarbeitete Rahmenvereinbarung mit der Kommission gebilligt, die solchen Aufforderungen mehr Gewicht geben soll. Ein echtes Initiativrecht würde aber eine Vertragsänderung erfordern. Außerdem fehlt die vertraute Logik von Regierung und Opposition: Die Kommission stützt sich nicht auf eine feste Koalition, Mehrheiten bilden sich von Fall zu Fall.",
            "<b>Und die Bürgerinnen und Bürger – können sie mehr tun als wählen?</b> Es gibt die Europäische Bürgerinitiative: Mit einer Million Unterschriften aus mindestens sieben Mitgliedstaaten kann man die Kommission auffordern, tätig zu werden. Bis heute haben 14 Initiativen diese Hürde genommen und eine Antwort der Kommission erhalten, zuletzt im Juni 2026 die Initiative „Stop Destroying Videogames“. Das Problem: Die Kommission muss antworten, aber nichts umsetzen. Viele Initiatoren sind am Ende enttäuscht.",
            "<b>Die Konferenz zur Zukunft Europas galt als großes Demokratieexperiment. Was ist daraus geworden?</b> Zwischen Mai 2021 und Mai 2022 haben 800 zufällig ausgewählte Bürgerinnen und Bürger in vier europäischen Bürgerforen beraten; am Ende standen 49 Vorschläge mit über 300 Maßnahmen. Einiges wurde aufgegriffen, und die Kommission lädt seither regelmäßig ausgeloste Bürgerforen zu einzelnen Vorhaben ein. Die weitreichenden Vorschläge aber – etwa mehr Mehrheitsentscheidungen oder ein Initiativrecht für das Parlament – würden Vertragsänderungen erfordern. Die hat es bislang nicht gegeben.",
            "<b>Was würden Sie ändern?</b> Drei Dinge: erstens transnationale Listen, damit einige Abgeordnete von allen Europäerinnen und Europäern gewählt werden können; zweitens ein Initiativrecht für das Parlament; drittens ein verbindliches Spitzenkandidatenprinzip. Ich gebe zu: Viele Regierungen wollen das nicht, weil sie Macht abgeben müssten. Und solange es keine gemeinsame europäische Öffentlichkeit gibt, werden auch die besten Regeln nicht alle Probleme lösen.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasstes Interview mit einer fiktiven Politikwissenschaftlerin (2026). Zahlen und Ereignisse sind real: Wahlbeteiligung laut Europäischem Parlament (EU 2024: 50,74 %, Deutschland: 64,74 %, 2014: 42,61 %); Konferenz zur Zukunft Europas (Abschlussbericht 9. Mai 2022); Europäische Bürgerinitiative (Stand: Oktober 2026).",
    },
]

AUFGABEN = [
    {
        "id": "q4-1-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Rede der Europaabgeordneten zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung: Rede einer (fiktiven) Europaabgeordneten im Europäischen Parlament, „Erweiterung braucht Reform – und zwar jetzt“, Oktober 2026; Thema: Verhältnis von Erweiterung und Reform (Vertiefung) der EU.",
            "punkte": [
                "Die Rednerin stellt fest, dass 2026 in der Erweiterungspolitik viel erreicht worden sei: Eröffnung erster Cluster mit der Ukraine und Moldau, Fortschritte Montenegros (21 von 33 Kapiteln) und Albaniens [1].",
                "Ursache der langen Verzögerung sei die Blockade durch eine einzige Regierung (Ungarn) gewesen, die selbst nach dem Regierungswechsel Bedingungen gestellt habe; auch bei Serbien blockierten mehrere Staaten; der Beitrittsprozess werde so zur Geisel nationaler Interessen [2].",
                "Erweiterung und Vertiefung gehörten zusammen; sie unterstützt den Kommissionsvorschlag zu Mehrheitsentscheidungen bei der Clustereröffnung und zu Brückenklauseln, fordert aber zusätzlich Mehrheitsentscheidungen in der Außen- und Sicherheitspolitik vor weiteren Beitritten [3].",
                "Die Werte müssten auch nach einem Beitritt geschützt werden; das Art.-7-Verfahren gegen Ungarn sei wirkungslos geblieben; sie verlangt Schutzklauseln bis zur Aussetzung von Stimmrechten [4].",
                "Kandidaten sollten schon vor dem Beitritt schrittweise in Binnenmarkt und Zusammenarbeit eingebunden werden, um Reformanreize zu erhalten [5].",
                "Sorgen um Agrar-, Kohäsions- und Haushaltsmittel seien berechtigt und im Finanzrahmen ab 2028 zu klären; Nicht-Erweiterung sei wegen Instabilität teurer [6].",
                "Fazit: Erweiterung als geopolitische Antwort auf Russlands Krieg und als beidseitiges Leistungsversprechen [7].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache (Cluster, Einstimmigkeit, qualifizierte Mehrheit, Art. 7 EUV), keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die zentralen Aussagen der Rede im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen der Rede weitgehend vollständig, strukturiert, fachsprachlich korrekt und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q4-1-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie den in M2 dargestellten Stand der Beitrittsprozesse.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Formale Angaben: Tabelle zum Stand der Beitrittsprozesse von neun Kandidatenländern (Antrag, Kandidatenstatus, Verhandlungsbeginn, Verhandlungsstand), eigene Zusammenstellung nach Angaben von Kommission, Rat und Regierungen, Stand Ende Oktober 2026.",
                "Am weitesten fortgeschritten: Montenegro (alle 33 Kapitel eröffnet, 21 vorläufig geschlossen, Beitrittsvertrag in Arbeit) und Albanien (alle Kapitel eröffnet, 4 geschlossen).",
                "Mittleres Stadium: Ukraine und Moldau (Antrag und Kandidatenstatus 2022, Verhandlungen seit 2024, 4 von 6 Clustern erst 2026 eröffnet); Serbien (22 von 35 Kapiteln eröffnet, 2 geschlossen, seit 2021 kein neues Cluster).",
                "Stockende Prozesse: Nordmazedonien (Antrag schon 2004, Verhandlungen seit 2022, aber kein Cluster eröffnet), Bosnien und Herzegowina (noch keine Regierungskonferenz), Georgien (Prozess „de facto gestoppt“), Türkei (Antrag 1987, Verhandlungen seit 2005, seit 2018 Stillstand).",
                "Auffällig: sehr unterschiedliche Dauer – teils Jahrzehnte zwischen Antrag und heutigem Stand (Türkei, Nordmazedonien), bei Ukraine und Moldau Antrag und Kandidatenstatus im selben Jahr; noch kein Land hat die Verhandlungen abgeschlossen.",
            ],
            "hinweis": "Beschreiben: formale Angaben, strukturierte Darstellung (z. B. nach Fortschritt gruppiert), zentrale Werte und Auffälligkeiten nennen, ohne Ursachen zu erklären oder zu bewerten.",
        },
        "bewertung": {
            "ausreichend": "die Tabelle im Ansatz formal und inhaltlich korrekt beschrieben wird.",
            "gut": "die Tabelle formal vollständig, inhaltlich strukturiert (z. B. nach Stand der Verhandlungen) und mit den wichtigsten Werten und Auffälligkeiten beschrieben wird.",
        },
    },
    {
        "id": "q4-1-i3",
        "afb": "I",
        "operator": "wiedergeben",
        "text": "Geben Sie die Aussagen der Politikwissenschaftlerin zu Stärken und Schwächen der europäischen Demokratie wieder. (M3)",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitungssatz: Interview mit einer (fiktiven) Politikwissenschaftlerin, „Ein Parlament mit angezogener Handbremse?“ (2026), über Europawahl, Europäisches Parlament und Bürgerbeteiligung.",
            "punkte": [
                "Wahlbeteiligung 2024 (gut 50 %, Deutschland fast 65 %, erstmals ab 16) sei im Vergleich zu 2014 ein Erfolg, die Europawahl bleibe aber vielerorts eine national geprägte Nebenwahl [1].",
                "Spitzenkandidatenprinzip: gute Idee, 2014 erfolgreich (Juncker), 2019 missachtet (von der Leyen ohne Kandidatur), 2024 wieder angewandt; rechtlich unverbindlich, da der Europäische Rat das Ergebnis nur berücksichtigen müsse [2].",
                "Dem EP fehle das Initiativrecht (nur Aufforderung an die Kommission; 2026 überarbeitete Rahmenvereinbarung, echtes Recht nur per Vertragsänderung) sowie die Logik von Regierung und Opposition [3].",
                "Europäische Bürgerinitiative: 1 Mio. Unterschriften aus sieben Staaten, 14 erfolgreiche Initiativen; Kommission müsse antworten, aber nichts umsetzen [4].",
                "Konferenz zur Zukunft Europas: 800 ausgeloste Bürger, 49 Vorschläge; Bürgerforen als Folge, weitreichende Vorschläge mangels Vertragsänderung nicht umgesetzt [5].",
                "Reformforderungen: transnationale Listen, Initiativrecht, verbindliches Spitzenkandidatenprinzip; Widerstand der Regierungen und fehlende europäische Öffentlichkeit als Grenzen [6].",
            ],
            "hinweis": "Wiedergeben: ausgehend von einem Einleitungssatz in eigenen Worten und mit Fachsprache, indirekte Rede, keine eigene Wertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen der Politikwissenschaftlerin im Ansatz korrekt und in eigenen Worten wiedergegeben werden.",
            "gut": "die Aussagen strukturiert nach Stärken, Schwächen und Reformvorschlägen, fachsprachlich präzise und in indirekter Rede wiedergegeben werden.",
        },
    },
    {
        "id": "q4-1-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M2 das Beitrittsverfahren der EU und die Bedeutung der Kopenhagener Kriterien.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Rechtsgrundlage Art. 49 EUV: europäischer Staat, der die Werte nach Art. 2 EUV achtet und fördert; Antrag an den Rat; Entscheidung einstimmig nach Anhörung der Kommission und Zustimmung des EP; Ratifikation durch alle Vertragsstaaten.",
                "Schritte: Antrag → Stellungnahme der Kommission → Kandidatenstatus → Verhandlungsrahmen und Regierungskonferenz → Screening → Verhandlungen in 6 Clustern/33 Kapiteln → Beitrittsvertrag → Ratifikation; Belege aus M2 (z. B. Ukraine: Antrag und Status 2022, Verhandlungen seit 2024, Cluster 2026; Montenegro: Beitrittsvertrag in Arbeit).",
                "Kopenhagener Kriterien (1993): politische (Demokratie, Rechtsstaat, Menschen- und Minderheitenrechte), wirtschaftliche (funktionsfähige Marktwirtschaft, Wettbewerbsfähigkeit) und Acquis-Kriterium; dazu Aufnahmefähigkeit der EU.",
                "Bedeutung: Maßstab für jeden Schritt; Methodik seit 2020 „Grundlagen zuerst“ (Cluster 1 zuerst geöffnet, zuletzt geschlossen); Rückschritte bei politischen Kriterien bremsen oder stoppen den Prozess (Georgien, Türkei, Serbien Cluster 3).",
                "Einstimmigkeit als Vetopunkt: Prozesse können auch aus bilateralen oder politischen Gründen blockiert werden (Nordmazedonien – Bulgarien, Ukraine – Ungarn bis 2026), daher große Unterschiede in der Dauer (M2).",
            ],
            "hinweis": "Erläutern: Verfahren und Kriterien mit zusätzlichen Informationen und Beispielen aus M2 veranschaulichen; eine bloße Aufzählung der Schritte ohne Materialbezug reicht nicht für eine gute Leistung.",
        },
        "bewertung": {
            "ausreichend": "das Beitrittsverfahren und die Kopenhagener Kriterien ansatzweise zutreffend und mit einzelnen Beispielen aus M2 erläutert werden.",
            "gut": "das Verfahren und die Kriterien fachlich präzise, in ihrem Zusammenhang und durchgängig mit Beispielen aus M2 erläutert werden.",
        },
    },
    {
        "id": "q4-1-ii2",
        "afb": "II",
        "operator": "einordnen",
        "text": "Ordnen Sie die Position der Rednerin (M1) in die Debatte über Vertiefung und Erweiterung sowie über Zielvorstellungen der Integration zwischen Staatenbund und Bundesstaat ein.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Debattenpositionen darstellen: „erst vertiefen, dann erweitern“; Erweiterung ohne Reform (intergouvernemental, Veto bleibt); parallele Vertiefung und Erweiterung; differenzierte Integration.",
                "Rednerin vertritt die These, dass Erweiterung und Vertiefung gleichzeitig erfolgen müssen („Beides zusammen“) [3], [7]; sie lehnt eine Verschiebung der Erweiterung ab [1], [6].",
                "Ihre Forderungen (Mehrheitsentscheidungen bei Clustern, Brückenklauseln, auch in der GASP) [3] und stärkerer Werteschutz mit Aussetzung von Stimmrechten [4] zielen auf mehr Supranationalität – Richtung föderalistisches Leitbild.",
                "Schrittweise Teilhabe an Binnenmarkt und Kooperationen [5] entspricht Elementen differenzierter Integration (gestufte Mitgliedschaft, konzentrische Kreise).",
                "Einordnung zwischen den Polen: keine Forderung nach einem europäischen Bundesstaat (keine europäische Regierung, keine Verfassung), sondern Weiterentwicklung des Staatenverbunds mit weniger Vetos; Gegensatz zu souveränistischen Positionen, die Einstimmigkeit als Schutz nationaler Souveränität verteidigen.",
                "Bezug zur aktuellen Debatte: Nähe zur Kommissionsmitteilung vom Oktober 2026, geht aber in der GASP darüber hinaus.",
            ],
            "hinweis": "Einordnen: Position begründet unter Verwendung von Vorwissen in den genannten Zusammenhang stellen; Belege aus M1 mit Absatzangaben erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Position der Rednerin ansatzweise zutreffend in die Debatte eingeordnet und mit einzelnen Textbelegen gestützt wird.",
            "gut": "die Position differenziert, mit Fachbegriffen (Vertiefung, Supranationalität, Staatenverbund, differenzierte Integration) und durchgängigen Textbelegen eingeordnet wird.",
        },
    },
    {
        "id": "q4-1-ii3",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie ausgehend von M3, warum das Europäische Parlament trotz seines Machtzuwachses nicht wie ein nationales Parlament in einem parlamentarischen Regierungssystem funktioniert.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Machtzuwachs: Direktwahl seit 1979; Mitentscheidung seit Maastricht, ordentliches Gesetzgebungsverfahren als Regelfall seit Lissabon; Haushaltsrecht, Zustimmungsrechte, Wahl der Kommissionsspitze, Misstrauensantrag.",
                "Parlamentarisches Regierungssystem (Q1.1): Parlamentsmehrheit wählt und trägt die Regierung, Gesetzesinitiative auch aus dem Parlament, Dualismus Regierung/Mehrheit vs. Opposition.",
                "In der EU fehlt dieser Zusammenhang: Kommissionsspitze wird vom Europäischen Rat vorgeschlagen (Art. 17 Abs. 7 EUV, Wahlergebnis nur „berücksichtigen“), Spitzenkandidatenprinzip unverbindlich (2019) [2]; keine feste Koalition, wechselnde Mehrheiten [3].",
                "Kein formelles Initiativrecht (Art. 225 AEUV nur Aufforderung; Rahmenvereinbarung 2026) [3]; Rat als zweiter Gesetzgeber mit Regierungsvertretern; Einstimmigkeit in Bereichen wie GASP ohne EP-Entscheidungsrecht.",
                "Strukturelle Ursachen: Nebenwahlcharakter und nationale Wahlkämpfe [1], fehlende europäische Öffentlichkeit [6], Staatenverbund mit doppelter Legitimation über EP und Rat statt Bundesstaat.",
            ],
            "hinweis": "Erklären: Unterschiede auf Funktionsprinzipien (parlamentarisches Regierungssystem, Institutionengefüge der EU, Art. 17 EUV, Art. 225 AEUV) zurückführen; Materialbezug erforderlich.",
        },
        "bewertung": {
            "ausreichend": "einige Unterschiede zum nationalen Parlamentarismus ansatzweise zutreffend erklärt und auf M3 bezogen werden.",
            "gut": "die Unterschiede differenziert auf die Funktionslogik des parlamentarischen Regierungssystems und das Institutionengefüge der EU zurückgeführt und durchgängig mit M3 verknüpft werden.",
        },
    },
    {
        "id": "q4-1-ii4",
        "afb": "II",
        "operator": "anwenden",
        "lk": True,
        "text": "Wenden Sie den liberalen Intergouvernementalismus und den konstruktivistischen Postfunktionalismus auf die in M1 und M2 dargestellte Erweiterungspolitik an.",
        "material": ["m1", "m2"],
        "loesung": {
            "punkte": [
                "Kernaussagen: Liberaler Intergouvernementalismus (Moravcsik): innerstaatliche Präferenzbildung, zwischenstaatliche Verhandlungen nach Verhandlungsmacht (asymmetrische Interdependenz), Delegation zur glaubwürdigen Selbstbindung. Postfunktionalismus (Hooghe/Marks): Politisierung, beschränkender Dissens, Bedeutung exklusiver nationaler Identitäten.",
                "LI angewendet: Präferenzen der Mitglieder (Sicherheit gegenüber Russland, Marktinteressen, Sorgen von Landwirten und Nettoempfängern) [M1: 6, 7]; Vetos als Verhandlungsmacht (Ungarns Bedingung zur Minderheitenfrage, Serbien) [M1: 2; M2]; Kandidaten als schwächere Verhandlungsseite müssen Kriterien, Schutzklauseln und Übergangsregeln akzeptieren [M1: 4, 5].",
                "LI zur Reform: Übergang zu Mehrheitsentscheidungen und Schutzklauseln als institutionelle Wahl, um Zusagen glaubwürdig zu machen und Blockaden zu verhindern [M1: 3, 4].",
                "Postfunktionalismus angewendet: Erweiterung als Identitätsfrage; Blockaden aus innenpolitischer Mobilisierung (ungarische Regierungspolitik bis zum Regierungswechsel 2026) und Identitätskonflikten (Nordmazedonien – Bulgarien, Serbien – Kosovo) [M2]; Haushaltsängste und Referendumsvorbehalte als beschränkender Dissens; Stillstand Türkei/Georgien auch als Frage von Zugehörigkeit und Werten.",
                "Vergleich der Erklärungskraft: LI erklärt Verhandlungsverläufe und Konditionen gut, Postfunktionalismus besser die Politisierung und die lange Dauer; beide erklären nur teilweise die Beschleunigung 2026 (Geopolitik, Regierungswechsel).",
            ],
            "hinweis": "Anwenden: Theorien nicht nur darstellen, sondern ihre Mechanismen ausdrücklich auf konkrete Befunde aus M1 und M2 beziehen; ein abschließender Vergleich der Erklärungskraft ist für eine gute Leistung erforderlich.",
        },
        "bewertung": {
            "ausreichend": "beide Theorien in Grundzügen zutreffend dargestellt und ansatzweise auf Befunde aus M1 und M2 angewendet werden.",
            "gut": "beide Theorien präzise dargestellt, systematisch auf mehrere Befunde aus M1 und M2 angewendet und in ihrer Erklärungskraft verglichen werden.",
        },
    },
    {
        "id": "q4-1-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Die Rednerin fordert, vor weiteren Beitritten im Beitrittsprozess und in der Außen- und Sicherheitspolitik vom Einstimmigkeitsprinzip zu Mehrheitsentscheidungen überzugehen. Erörtern Sie diese Forderung. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klärung: Einstimmigkeit in GASP und Erweiterung; Wege zum Wechsel (Passerelle-Klauseln Art. 48 Abs. 7 und Art. 31 Abs. 3 EUV – selbst einstimmig, in Deutschland mit Gesetz; Vertragsänderung); Kommissionsvorschlag Oktober 2026 (QMV für Zwischenschritte, Brückenklauseln z. B. bei Sanktionen).",
                "Pro: Handlungsfähigkeit bei 30+ Mitgliedern; Schutz vor Erpressung durch Einzelstaaten und vor sachfremden bilateralen Blockaden (Ungarn – Ukraine, Bulgarien – Nordmazedonien) [2]; schnellere Reaktion in Krisen (Sanktionen); Glaubwürdigkeit des Beitrittsversprechens; qualifizierte Mehrheit schützt über doppelte Mehrheit auch kleinere Staaten.",
                "Contra: Souveränitätsverlust in Kernbereichen (Krieg und Frieden); Gefahr, dass große Staaten dominieren; schwächere Akzeptanz überstimmter Staaten, mögliche Politisierung und EU-Skepsis (Postfunktionalismus); Einstimmigkeit erzwingt breite Kompromisse; Beitritt als Vertrag bleibt ohnehin ratifikationspflichtig; Alternativen wie konstruktive Enthaltung oder Koalitionen der Willigen.",
                "Differenzierte Lösungen: QMV nur für Zwischenschritte, Notbremsen für vitale nationale Interessen, schrittweiser Übergang, Schutzklauseln.",
                "Abwägung nach Kriterien (Effektivität, Legitimität, Schutz kleiner Staaten, Souveränität) und eigenes begründetes Urteil; unterschiedliche Ergebnisse sind möglich.",
            ],
            "hinweis": "Erörtern: Pro- und Contra-Argumente abwägen und zu einem eigenen Urteil gelangen; Bezug auf die konkrete Forderung in M1 [3] und auf die rechtlichen Wege (Passerelle, Vertragsänderung) erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, fachlich fundiert (Rechtsgrundlagen, Beispiele) und abwägend ist und in ein klares, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q4-1-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie Chancen und Risiken einer Aufnahme der Ukraine und der Republik Moldau in die EU. Beziehen Sie M2 ein.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien benennen, z. B. Sicherheit/Frieden, wirtschaftliche Folgen, Haushalt, Demokratie und Rechtsstaat, Handlungsfähigkeit der EU, Akzeptanz.",
                "Chancen: Stabilisierung und Verankerung im Westen, Schließen geopolitischer Grauzonen gegenüber Russland; Reformanreize durch Kopenhagener Kriterien (Cluster „Grundlagen“ 2026 eröffnet, M2); größerer Binnenmarkt, Agrarpotenzial, Arbeitskräfte; Glaubwürdigkeit der EU nach dem Kandidatenstatus 2022.",
                "Risiken: anhaltender Krieg und russische Besetzung, Transnistrien in Moldau, Fragen der Beistandsklausel (Art. 42 Abs. 7 EUV); Verschiebungen bei Agrar- und Kohäsionsmitteln, Konkurrenz für Landwirte; Korruption und Rechtsstaatsdefizite; Gefahr von Rückschritten nach dem Beitritt; Einstimmigkeit und Institutionen bei mehr als 30 Mitgliedern; Akzeptanz in der Bevölkerung.",
                "Auswertung M2: Verhandlungen erst seit 2024, 4 von 6 Clustern erst 2026 geöffnet, schwierigste Cluster (u. a. Landwirtschaft) noch zu – ein Beitritt ist noch nicht absehbar; Vergleich mit Montenegro (seit 2012) zeigt die übliche Dauer.",
                "Abwägung und begründetes Urteil (z. B. Chancen überwiegen langfristig unter Bedingungen wie Reformen der EU, Schutzklauseln, schrittweiser Integration; oder Risiken überwiegen derzeit).",
            ],
            "hinweis": "Beurteilen: Einschätzung auf Basis erkennbarer Kriterien und Fachwissen; Materialbezug zu M2 notwendig. Die Differenzierung zwischen Ukraine und Moldau (Größe, Krieg, Agrarsektor) ist für eine gute Leistung wünschenswert.",
        },
        "bewertung": {
            "ausreichend": "Chancen und Risiken ansatzweise kriteriengeleitet gegenübergestellt werden und ein nachvollziehbares Urteil mit Bezug zu M2 vorliegt.",
            "gut": "das Urteil kriteriengeleitet, differenziert (auch zwischen beiden Ländern), fachlich fundiert und mit Auswertung von M2 schlüssig begründet ist.",
        },
    },
    {
        "id": "q4-1-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Sie nehmen an einem Europäischen Bürgerforum zur Zukunft der europäischen Demokratie teil. Entwerfen Sie einen Redebeitrag, in dem Sie einen der in M3 genannten Reformvorschläge auswählen und begründet für oder gegen seine Umsetzung werben.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Form: Redebeitrag mit Anrede, klarer These, Begründung, Auseinandersetzung mit einem Gegenargument und Schlussappell; adressatengerechte Sprache für ein Bürgerforum.",
                "Transnationale Listen – pro: Europäisierung der Wahl, Stärkung europäischer Parteien und Öffentlichkeit [6]; contra: Dominanz großer Staaten, Entfremdung von Wahlkreisen, Komplexität, fehlende Einigung im Rat.",
                "Initiativrecht für das EP – pro: einzige direkt gewählte Institution, Abbau des Demokratiedefizits [3]; contra: Kommission als neutrale Hüterin des Gemeinschaftsinteresses, Rat bleibt Mitgesetzgeber, Vertragsänderung nötig, indirektes Initiativrecht (Art. 225 AEUV, Rahmenvereinbarung 2026) als Alternative.",
                "Verbindliches Spitzenkandidatenprinzip – pro: Wahl entscheidet über die Kommissionsspitze, Personalisierung erhöht Beteiligung [2]; contra: Kandidaten in vielen Staaten unbekannt, Europäischer Rat verliert Gestaltungsspielraum, Kommission wird parteipolitischer.",
                "Fachliche Fundierung mit Bezug auf M3 (z. B. Nebenwahl, Wahlbeteiligung, Erfahrungen 2014/2019/2024, Konferenz zur Zukunft Europas) und auf das Demokratiedefizit (Q1.3).",
                "Eigene, begründete Position mit offengelegten Maßstäben (z. B. Input-Legitimation vs. Handlungsfähigkeit).",
            ],
            "hinweis": "Gestalten/Entwerfen: produktorientierte Umsetzung in eine Rede; bewertet werden fachliche Richtigkeit, Schlüssigkeit der Argumentation, Material- und Adressatenbezug sowie die Textsortenmerkmale.",
        },
        "bewertung": {
            "ausreichend": "ein Redebeitrag mit erkennbarer Position und einigen fachlich zutreffenden Argumenten mit Bezug zu M3 vorliegt.",
            "gut": "der Redebeitrag adressatengerecht und rhetorisch überzeugend gestaltet ist, eine klare Position fachlich fundiert begründet, ein Gegenargument entkräftet und durchgängig auf M3 Bezug nimmt.",
        },
    },
    {
        "id": "q4-1-iii4",
        "afb": "III",
        "operator": "überprüfen",
        "lk": True,
        "text": "Überprüfen Sie die These, die Entwicklung der europäischen Integration lasse sich am besten neofunktionalistisch als Abfolge von Spillover-Effekten erklären.",
        "material": [],
        "loesung": {
            "punkte": [
                "Klärung: Neofunktionalismus (Haas), Spillover-Arten (funktional, politisch, kultiviert), Rolle supranationaler Akteure; Supranationalismus als Weiterentwicklung.",
                "Belege für die These: EGKS → EWG → Binnenmarkt → Euro (funktionaler Spillover); Schengen → gemeinsamer Außengrenzschutz und Asylpolitik; Rolle von Kommission und EuGH (Vorrang des EU-Rechts, Costa/ENEL); Bankenunion als Reaktion auf die Euro-Krise.",
                "Gegenbelege: Politik des leeren Stuhls 1965/66 und Luxemburger Kompromiss; Intergouvernementalität der GASP und Einstimmigkeit (Hoffmann); große Vertragsreformen als Regierungsverhandlungen (Moravcsik); gescheiterter Verfassungsvertrag 2005 und Brexit als Spillback; Blockaden der Erweiterung 2024–2026 durch Einzelstaaten.",
                "Alternative Erklärungen: liberaler Intergouvernementalismus (Interessen und Verhandlungsmacht), Postfunktionalismus (Politisierung, beschränkender Dissens seit Maastricht), konstruktivistische Ansätze (rhetorische Selbstverpflichtung bei der Osterweiterung).",
                "Begründetes Fazit: These nur teilweise haltbar – Spillover erklärt v. a. wirtschaftliche Integrationsschritte und langfristige Dynamik, weniger Krisen, Stillstand und Rückschritte; Theorienpluralismus als angemessene Sicht.",
            ],
            "hinweis": "Überprüfen: die These auf Grundlage von Fachkenntnissen kritisch hinterfragen und ihre Angemessenheit begründet einschätzen; mehrere historische Belege und mindestens eine alternative Theorie werden erwartet.",
        },
        "bewertung": {
            "ausreichend": "die These ansatzweise anhand einzelner Belege und Gegenbelege überprüft und ein nachvollziehbares Fazit gezogen wird.",
            "gut": "die These theoriegeleitet, mit mehreren historischen Belegen und Gegenbelegen sowie alternativen Integrationstheorien überprüft wird und in ein differenziertes, schlüssiges Fazit mündet.",
        },
    },
]
