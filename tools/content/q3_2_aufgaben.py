# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q3.2 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q3.2, insbesondere Verflechtung von Volkswirtschaften (Außenhandel, Freihandelszonen, Binnenmärkte, Arbeit) mit Chancen und Risiken, Globalisierung von Unternehmen (Arbeitsteilung, Lieferkettenproblematik, Standortfaktoren) sowie – laut Erlass 2027 auch im Grundkurs – die Kontroverse um die Handelspolitik der WTO zwischen Liberalisierung und Regulierung; LK: Außenwirtschaftstheorien (absolute und komparative Kostenvorteile, Faktor-Proportionen-Theorem)."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Schiedsrichter ohne Pfeife“ (2026)",
        "absaetze": [
            "Als die US-Regierung am 2. April 2025 ihre „reziproken Zölle“ verkündete, sprach sie von einem „Befreiungstag“. Für die Welthandelsorganisation war es eher ein Offenbarungseid. Ein Land, das die Regeln des Welthandels nach 1945 maßgeblich mitgeschrieben hatte, setzte sich offen über deren Kern hinweg: Gleiche Zölle für alle Mitglieder – die Meistbegünstigung – galten plötzlich nicht mehr. Jeder Handelspartner erhielt seinen eigenen Satz, je nachdem, wie hoch das Defizit der USA im Handel mit ihm war und wie viel er in Verhandlungen zu bieten bereit war.",
            "Ökonominnen und Ökonomen sind sich seit David Ricardo weitgehend einig, dass solche Zölle vor allem den Verbrauchern und Unternehmen im eigenen Land schaden und am Ende den Wohlstand aller Beteiligten senken. Doch ökonomische Argumente prallten ab. Selbst als der Oberste Gerichtshof der USA im Februar 2026 die auf ein Notstandsgesetz gestützten Zölle für unzulässig erklärte, fand Washington binnen Tagen neue Rechtsgrundlagen. Seit Juli 2026 heißen die Zölle nicht mehr „reziprok“, sondern sollen Zwangsarbeit bekämpfen – an ihrer Höhe hat sich für viele Länder wenig geändert.",
            "Und die WTO? Sie schaute zu. China und Kanada leiteten 2025 zwar Streitverfahren ein, doch die USA erklärten, Fragen der nationalen Sicherheit gingen die WTO nichts an. Selbst ein Sieg vor einem Streitschlichtungspanel wäre wertlos gewesen: Weil Washington seit Jahren die Neubesetzung des Berufungsgremiums blockiert, ist die zweite Instanz seit Dezember 2019 handlungsunfähig. Wer verliert, legt einfach Berufung ein – ins Leere. Ein Schiedsrichter ohne Pfeife ist kein Schiedsrichter.",
            "Es wäre jedoch zu einfach, die Schuld allein den USA zu geben. China hat seinen Status als Entwicklungsland lange genutzt und mit massiven Staatssubventionen Überkapazitäten aufgebaut, gegen die die WTO-Regeln kaum etwas ausrichten. Die EU wiederum erhebt seit 2026 einen CO₂-Grenzausgleich auf Stahl, Zement oder Dünger und verlangt von Unternehmen Sorgfalt in ihren Lieferketten – aus Sicht vieler Länder des Globalen Südens „grüner Protektionismus“. Die Doha-Runde, die den Entwicklungsländern faire Chancen bringen sollte, ist seit Langem gescheitert. Und die Ministerkonferenz im kamerunischen Yaoundé endete im März 2026 ohne gemeinsame Abschlusserklärung.",
            "Was folgt daraus? Die Zeit, in der sich über 160 Staaten im Konsens auf immer weitere Zollsenkungen einigten, ist vorbei – und sie kommt nicht wieder. Statt einer Liberalisierungsmaschine braucht die Welt eine WTO, die Regeln für fairen Handel setzt: für Subventionen, für Klimaschutz an der Grenze, für Mindeststandards bei der Arbeit. Wo nicht alle mitziehen, müssen Koalitionen der Willigen vorangehen. Dass 62 Mitglieder mit einer Ersatz-Berufungsinstanz arbeiten und 66 Mitglieder ein Abkommen zum elektronischen Handel vorgelegt haben, zeigt, dass das möglich ist. Auch die neuen Abkommen der EU mit dem Mercosur und mit Indien gehören in dieses Bild.",
            "Wer an der alten WTO festhält, verteidigt eine Ordnung, die es so nicht mehr gibt. Wer sie aber ganz aufgibt, überlässt den Welthandel dem Recht des Stärkeren. Die Europäische Union sollte deshalb vorangehen und die WTO vom Motor der Liberalisierung zu einem Regelwerk für fairen, nachhaltigen Handel umbauen – notfalls zunächst ohne die USA.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Handelsökonomin (2026). Die genannten Ereignisse sind real (Stand: Oktober 2026); die Zahl der MPIA-Teilnehmer beruht auf Angaben der EU-Kommission vom 9. September 2026, die Angabe zum E-Commerce-Abkommen auf Berichten zur 14. WTO-Ministerkonferenz (März 2026).",
    },
    {
        "id": "m2",
        "titel": "M2: Deutschlands wichtigste Handelspartner im Warenhandel 2025",
        "typ": "tabelle",
        "kopf": ["Handelspartner", "Außenhandelsumsatz 2025 in Mrd. Euro (Rang)", "Exporte 2025 in Mrd. Euro (Rang)", "Exporte: Veränderung zu 2024", "Importe 2025 in Mrd. Euro (Rang)", "Importe: Veränderung zu 2024", "Saldo 2025 in Mrd. Euro", "Saldo 2024 in Mrd. Euro"],
        "zeilen": [
            ["China", "251,8 (1)", "81,3 (6)", "−9,7 %", "170,6 (1)", "+8,8 %", "−89,3", "−66,9"],
            ["USA", "240,5 (2)", "146,2 (1)", "−9,4 %", "94,3 (3)", "+2,7 %", "+51,9", "+69,6"],
            ["Niederlande", "209,1 (3)", "112,5 (3)", "+2,9 %", "96,7 (2)", "+3,9 %", "+15,8*", "k. A."],
            ["Alle Länder insgesamt", "2.925,5*", "1.563,0", "+0,9 %", "1.362,5", "+4,3 %", "+200,5", "+242,9"],
            ["darunter: Kraftwagen und Kraftwagenteile, Export in die USA", "–", "28,5", "−17,8 %", "–", "–", "–", "–"],
            ["darunter: Datenverarbeitungsgeräte, elektronische und optische Erzeugnisse, Import aus China", "–", "–", "–", "50,9", "+4,9 %", "–", "–"],
        ],
        "quelle": "Statistisches Bundesamt (Destatis), Pressemitteilung Nr. 056 vom 20. Februar 2026 (vorläufige Ergebnisse, Werte gerundet). Außenhandelsumsatz = Exporte + Importe. * eigene Berechnung aus den Export- und Importwerten; k. A. = in der Quelle nicht ausgewiesen. Zweitwichtigstes Exportziel 2025 war Frankreich (117,4 Mrd. Euro).",
    },
    {
        "id": "m3",
        "titel": "M3: Interview „Just in time war gestern“ (2026)",
        "absaetze": [
            "<b>Frau K., Ihr Unternehmen verkauft Outdoor-Bekleidung. Wo entstehen Ihre Produkte?</b> Entworfen wird bei uns in Hessen, wo wir 350 Beschäftigte haben. Die Stoffe kaufen wir vor allem in China und der Türkei, genäht wird in Vietnam und Bangladesch. Dort sind die Lohnkosten ein Bruchteil der deutschen, und die Fabriken haben über Jahrzehnte enormes Know-how aufgebaut. Ohne diese Arbeitsteilung könnten wir eine gute Regenjacke nicht für unter 200 Euro anbieten.",
            "<b>Wie haben Sie die vergangenen Jahre erlebt?</b> Als Dauerkrise. In der Pandemie standen Fabriken still, Container waren kaum zu bekommen, die Frachtraten vervielfachten sich. Kaum hatte sich das normalisiert, griffen ab Ende 2023 Huthi-Milizen Schiffe im Roten Meer an. Unsere Ware fährt seitdem oft um die Südspitze Afrikas – das dauert rund zwei Wochen länger. Und seit 2025 wissen wir bei Lieferungen in die USA nie genau, welcher Zollsatz im nächsten Quartal gilt.",
            "<b>Was haben Sie geändert?</b> „Just in time“ war gestern. Wir halten heute deutlich mehr Ware auf Lager und haben für jedes Produkt mindestens zwei Lieferanten in verschiedenen Ländern. Einen Teil der Produktion haben wir in die Türkei verlagert. Das ist teurer, aber die Ware ist in einer Woche per Lkw bei uns. Diese Sicherheit kostet uns ein paar Prozentpunkte Gewinnmarge – mehr bezahlen will die Kundschaft dafür nur begrenzt.",
            "<b>Unter das Lieferkettengesetz fallen Sie mit 350 Beschäftigten gar nicht. Spielt es für Sie eine Rolle?</b> Und ob. Unsere großen Handelskunden fallen darunter und geben die Anforderungen an uns weiter. Wir füllen Fragebögen aus, lassen Fabriken prüfen und haben ein Beschwerdesystem für die Näherinnen eingerichtet. Seit dem Einsturz von Rana Plaza 2013 weiß jeder in der Branche, was auf dem Spiel steht. Ich halte die Grundidee für richtig: Wer an billiger Produktion verdient, trägt Verantwortung für die Bedingungen, unter denen sie entsteht.",
            "<b>Die EU hat ihre Lieferkettenrichtlinie 2026 stark abgeschwächt, die Bundesregierung will die Berichtspflicht streichen. Freut Sie das?</b> Gemischt. Die Bürokratie war teilweise absurd – dieselben Fragen in zehn verschiedenen Formularen. Aber wir haben investiert, weil man uns gesagt hat, die Regeln kommen. Jetzt sollen nur noch sehr große Konzerne erfasst sein. Wer sich bemüht hat, steht als der Dumme da, und wer weiter auf die billigste Fabrik setzt, hat einen Kostenvorteil. Ein faires Spielfeld sieht anders aus.",
            "<b>Ist die Globalisierung am Ende?</b> Nein, aber sie verändert sich. Sie wird regionaler, vorsichtiger und teurer. Für Länder wie Bangladesch, die vom Export leben, ist das eine echte Gefahr. Wenn sich alle aus Angst zurückziehen, verlieren gerade die Näherinnen ihre Jobs, denen wir eigentlich helfen wollten.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasstes Interview mit einer fiktiven Unternehmerin (2026). Die genannten Ereignisse und Regelungen sind real (Stand: Oktober 2026).",
    },
]

AUFGABEN = [
    {
        "id": "q3-2-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Kommentar), Titel „Schiedsrichter ohne Pfeife“, Erscheinungsjahr (2026), Thema (Krise der WTO angesichts der US-Zollpolitik und Forderung nach ihrem Umbau) und – da fiktiv – Hinweis auf eine ungenannte Autorin (Handelsökonomin).",
            "punkte": [
                "Die US-Zölle vom April 2025 hätten das Meistbegünstigungsprinzip offen missachtet; Zollsätze seien je Land nach Handelsdefizit und Verhandlungsbereitschaft festgelegt worden [1].",
                "Zölle schadeten nach weitgehend einhelliger ökonomischer Einschätzung vor allem dem eigenen Land und dem Wohlstand aller; trotz des Urteils des Supreme Court (Februar 2026) hätten die USA neue Rechtsgrundlagen gefunden und begründeten die Zölle seit Juli 2026 mit Zwangsarbeit – bei für viele Länder ähnlicher Höhe [2].",
                "Die WTO sei machtlos gewesen: Klagen Chinas und Kanadas, Verweis der USA auf nationale Sicherheit, seit Dezember 2019 handlungsunfähiges Berufungsgremium, Berufung „ins Leere“ [3].",
                "Mitverantwortung anderer: chinesische Subventionen und Überkapazitäten, CO₂-Grenzausgleich und Sorgfaltspflichten der EU als „grüner Protektionismus“ aus Sicht des Globalen Südens, gescheiterte Doha-Runde, ergebnislose Ministerkonferenz 2026 [4].",
                "Die Ära multilateraler Zollsenkungen im Konsens sei vorbei; nötig sei eine WTO, die Regeln für fairen Handel setze (Subventionen, Klimaschutz, Arbeitsstandards); Koalitionen der Willigen (MPIA, E-Commerce-Abkommen, EU-Abkommen mit Mercosur und Indien) zeigten, dass dies möglich sei [5].",
                "Fazit: weder Festhalten an der alten WTO noch Aufgabe; die EU solle den Umbau zu einem Regelwerk für fairen, nachhaltigen Handel anführen, notfalls zunächst ohne die USA [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache (Meistbegünstigung, Berufungsgremium, plurilateral), keine eigene Wertung. Die Argumentationsstruktur (Diagnose – Mitverantwortung – Forderung) sollte erkennbar werden.",
        },
        "bewertung": {
            "ausreichend": "die zentralen Aussagen des Kommentars im Ansatz korrekt und mit Einleitungssatz zusammengefasst werden.",
            "gut": "die Aussagen weitgehend vollständig, strukturiert, fachsprachlich präzise und in indirekter Rede zusammengefasst werden und die Argumentationsstruktur des Kommentars deutlich wird.",
        },
    },
    {
        "id": "q3-2-i2",
        "afb": "I",
        "operator": "darstellen",
        "text": "Stellen Sie die Grundprinzipien der Welthandelsorganisation (WTO) sowie die Funktionsweise ihres Streitbeilegungsverfahrens dar.",
        "material": [],
        "loesung": {
            "punkte": [
                "Ziel und Entstehung: 1995 aus dem GATT (1947) hervorgegangen, Sitz Genf, über 160 Mitglieder; Ziel eines offenen, regelbasierten und nicht diskriminierenden Welthandels; Aufgaben: Verhandlungsforum, Überwachung der Handelspolitik, Streitbeilegung; Entscheidungen im Konsens.",
                "Meistbegünstigung (Art. I GATT): Handelsvorteile für ein Mitglied gelten für alle Mitglieder; Ausnahmen für Freihandelszonen und Zollunionen (Art. XXIV) sowie Präferenzen für Entwicklungsländer.",
                "Inländerbehandlung (Art. III GATT): Eingeführte Waren dürfen nach der Verzollung nicht schlechter behandelt werden als heimische (z. B. bei Steuern oder Vorschriften).",
                "Weitere Grundsätze: Gegenseitigkeit von Zugeständnissen, Transparenz, gebundene Höchstzölle; Ausnahmen zum Schutz von Gesundheit, Umwelt und Ressourcen (Art. XX) und wesentlicher Sicherheitsinteressen (Art. XXI); Sonder- und Vorzugsbehandlung von Entwicklungsländern.",
                "Streitbeilegung: Konsultationen – Einsetzung eines Panels (Bericht) – Berufung beim Berufungsgremium – Annahme durch das Streitbeilegungsgremium im negativen Konsens – Umsetzung oder genehmigte Gegenmaßnahmen.",
                "Aktuelle Lage: Berufungsgremium seit Dezember 2019 handlungsunfähig, weil die USA Neubesetzungen blockieren; Berufung „ins Leere“ möglich; Ersatz-Schiedsverfahren MPIA (62 Mitglieder, Stand September 2026; USA nicht beteiligt).",
            ],
            "hinweis": "Darstellen: Sachverhalte und ihre Zusammenhänge strukturiert aufzeigen. Die Prinzipien sollten mit Beispielen veranschaulicht werden; eine Bewertung ist nicht verlangt. Genaue Artikelangaben sind nicht zwingend.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Prinzipien der WTO und der Ablauf der Streitbeilegung in Grundzügen zutreffend dargestellt werden.",
            "gut": "Prinzipien, Ausnahmen und Streitbeilegung strukturiert, fachsprachlich präzise und mit Bezug zur Blockade des Berufungsgremiums dargestellt werden.",
        },
    },
    {
        "id": "q3-2-i3",
        "afb": "I",
        "operator": "wiedergeben",
        "text": "Geben Sie die Erfahrungen und Positionen der Unternehmerin wieder. (M3)",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitungssatz: Interview „Just in time war gestern“ (2026) mit der (fiktiven) Geschäftsführerin eines mittelständischen hessischen Bekleidungsunternehmens über globale Lieferketten und Sorgfaltspflichten.",
            "punkte": [
                "Arbeitsteilung: Design in Hessen (350 Beschäftigte), Stoffe aus China und der Türkei, Nähen in Vietnam und Bangladesch; Gründe: niedrige Lohnkosten und Know-how der Fabriken; nur so seien günstige Preise möglich [1].",
                "Störungen: Pandemie (Stillstand, Containermangel, stark gestiegene Frachtraten), Angriffe im Roten Meer seit Ende 2023 (Umweg um Afrika, rund zwei Wochen länger), Unsicherheit über US-Zölle seit 2025 [2].",
                "Anpassungen: mehr Lagerhaltung, mindestens zwei Lieferanten je Produkt, teilweise Verlagerung in die Türkei (Nearshoring) – teurer, aber schneller; geringere Gewinnmarge [3].",
                "Sorgfaltspflichten: Das Unternehmen falle nicht unter das LkSG, große Kunden gäben die Anforderungen aber weiter (Fragebögen, Prüfungen, Beschwerdesystem); Rana Plaza als Wendepunkt; Verantwortung für Produktionsbedingungen sei grundsätzlich richtig [4].",
                "Abschwächung von CSDDD und LkSG: Bürokratieabbau teils berechtigt, aber Verlust an Planungssicherheit, Benachteiligung engagierter Unternehmen, kein faires Spielfeld [5].",
                "Die Globalisierung ende nicht, werde aber regionaler, vorsichtiger und teurer; Gefahr für Exportländer wie Bangladesch und deren Beschäftigte [6].",
            ],
            "hinweis": "Wiedergeben: ausgehend von einem Einleitungssatz die Informationen in eigenen Worten und unter Verwendung von Fachbegriffen (z. B. Nearshoring, Diversifizierung, Sorgfaltspflichten) ausdrücken; indirekte Rede; keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die Erfahrungen und Positionen der Unternehmerin im Ansatz korrekt und mit Einleitungssatz wiedergegeben werden.",
            "gut": "die Erfahrungen und Positionen weitgehend vollständig, strukturiert, fachsprachlich und in indirekter Rede wiedergegeben werden.",
        },
    },
    {
        "id": "q3-2-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1, inwiefern die US-Zollpolitik seit 2025 und die Blockade der WTO-Streitbeilegung die regelbasierte Welthandelsordnung infrage stellen.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Regelbasierte Ordnung: gleiche, vorhersehbare Regeln für alle, Nichtdiskriminierung, gebundene Zölle und Durchsetzung durch unabhängige Streitbeilegung; Schutz kleinerer Staaten vor Machtpolitik.",
                "Meistbegünstigung: länderspezifische „reziproke“ Zölle (April 2025), unterschiedliche Sätze der Section-301-Zölle (Juli 2026) und bilaterale Deals (z. B. Turnberry-Vereinbarung EU–USA mit 15 %-Obergrenze) differenzieren nach Partnern statt einheitlicher Zölle [1], [2].",
                "Rechtfertigung: Berufung auf nationale Sicherheit (Art. XXI GATT) bzw. Notstands- und nationale Handelsgesetze – Gefahr, dass Ausnahmen zur Regel werden und jedes Mitglied sie für sich beansprucht [2], [3].",
                "Durchsetzung: Klagen Chinas und Kanadas (2025) laufen faktisch ins Leere, weil das Berufungsgremium seit Dezember 2019 nicht besetzt ist; die MPIA gilt nur zwischen Teilnehmern, die USA sind nicht dabei [3], [5].",
                "Folgewirkungen: Gegenzölle und Zollspirale, Rechtsunsicherheit für Unternehmen, Nachahmungseffekte, Ausweichen auf bilaterale und plurilaterale Abkommen (EU–Mercosur, EU–Indien) und damit Zersplitterung der Handelsordnung [5].",
                "Ergänzung: Innenpolitische Grenzen (Urteil des Supreme Court im Februar 2026) zeigen, dass Rechtsstaatlichkeit auch national wirkt – die Regierung fand aber neue Rechtsgrundlagen [2].",
            ],
            "hinweis": "Erläutern: Sachverhalte mit zusätzlichen Informationen und Beispielen veranschaulichen. Erwartet wird die Verknüpfung der WTO-Prinzipien mit konkreten Maßnahmen; bloßes Nacherzählen von M1 genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "ansatzweise erläutert wird, gegen welche Prinzipien die US-Zollpolitik verstößt und warum die blockierte Streitbeilegung die Durchsetzung der Regeln schwächt.",
            "gut": "differenziert und mit passenden Beispielen erläutert wird, wie Zollpolitik und blockierte Streitbeilegung Nichtdiskriminierung, Rechtssicherheit und Durchsetzbarkeit der Welthandelsordnung untergraben, und Materialbezüge durchgängig hergestellt werden.",
        },
    },
    {
        "id": "q3-2-ii2",
        "afb": "II",
        "operator": "auswerten",
        "text": "Werten Sie M2 im Hinblick auf die außenwirtschaftliche Verflechtung Deutschlands und die damit verbundenen Risiken aus.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Formales: Tabelle des Statistischen Bundesamtes, vorläufige Ergebnisse für 2025 mit Vorjahresvergleich; nur Warenhandel; Kategorien Umsatz, Exporte, Importe, Salden.",
                "Hohe Verflechtung insgesamt: Exporte 1.563 Mrd. Euro, Importe 1.362,5 Mrd. Euro, Überschuss 200,5 Mrd. Euro (2024: 242,9 Mrd.); Exporte stagnieren (+0,9 %), Importe wachsen stärker (+4,3 %).",
                "USA: wichtigstes Exportziel (146,2 Mrd. Euro), aber Exporte −9,4 % und Rückgang des Überschusses von 69,6 auf 51,9 Mrd. Euro; Kfz-Exporte −17,8 % – Zusammenhang mit den US-Zöllen (u. a. auf Autos) plausibel.",
                "China: wichtigster Handelspartner nach Umsatz, aber stark asymmetrisch: Importe 170,6 Mrd. Euro (+8,8 %), Exporte nur 81,3 Mrd. Euro (−9,7 %); Defizit wächst auf 89,3 Mrd. Euro; hohe Importe bei Elektronik (50,9 Mrd. Euro) deuten auf Abhängigkeit bei wichtigen Vorprodukten hin; deutsche Exporteure verlieren in China an Boden.",
                "EU-Partner (Niederlande) mit moderatem Wachstum in beide Richtungen – der Binnenmarkt wirkt stabilisierend.",
                "Gesamtaussage: Deutschland ist stark und zugleich einseitig verflochten – Absatzrisiko gegenüber den USA (Zölle), Beschaffungsrisiko gegenüber China (Abhängigkeit, Exportkontrollen); Gefahren für Arbeitsplätze in Exportbranchen, v. a. der Autoindustrie. Grenzen der Aussagekraft: vorläufige Daten, nur Warenhandel, Ursachen nicht direkt ablesbar.",
            ],
            "hinweis": "Auswerten: Daten zu einer Gesamtaussage zusammenführen. Erwartet werden korrekte Zahlenbezüge, Vergleiche (absolute Werte, Veränderungen, Salden) und eine begründete Gesamtaussage zu Verflechtung und Risiken; reine Zahlenwiedergabe genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "zentrale Daten korrekt aufgegriffen und ansatzweise zu einer Aussage über Verflechtung und Risiken zusammengeführt werden.",
            "gut": "die Daten differenziert verglichen, Zusammenhänge (z. B. US-Zölle, Abhängigkeit von China) plausibel hergestellt und in eine schlüssige Gesamtaussage mit Hinweis auf die Grenzen der Daten überführt werden.",
        },
    },
    {
        "id": "q3-2-ii3",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie ausgehend von M3, warum Unternehmen ihre Produktion international aufteilen und weshalb globale Lieferketten störanfällig sind.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Internationale Arbeitsteilung: Zerlegung der Wertschöpfung in einzelne Schritte (Design in Deutschland, Stoffe aus China und der Türkei, Nähen in Vietnam und Bangladesch) [1]; Rückführung auf Kostenvorteile und Spezialisierung (Lohnstückkosten, Know-how, Größenvorteile der Zulieferer).",
                "Standortfaktoren: harte Faktoren (Lohnkosten, Transportkosten und -zeiten, Zölle, Infrastruktur) und weiche Faktoren (Rechtssicherheit, politische Stabilität); Abwägung zwischen Kosten und Lieferzeit, z. B. bei der Verlagerung in die Türkei [1], [3].",
                "Voraussetzungen: niedrige Transportkosten (Container), Digitalisierung, Handelsliberalisierung und Zollpräferenzen für Produktionsländer.",
                "Störanfälligkeit: lange Transportwege mit wenigen Engpässen (Suezkanal, Rotes Meer), Just-in-time-Produktion ohne Puffer, Konzentration auf wenige Lieferländer, geopolitische Risiken (Zölle, Exportkontrollen), Pandemien [2].",
                "Zielkonflikt Effizienz vs. Resilienz: Diversifizierung, Lagerhaltung und Nearshoring erhöhen die Sicherheit, aber auch die Kosten und senken die Marge [3].",
            ],
            "hinweis": "Erklären: Rückführung auf ökonomische Grundprinzipien (Arbeitsteilung, Kostenvorteile, Standortfaktoren, Risiko). Materialbezüge zu [1]–[3] sind erforderlich.",
        },
        "bewertung": {
            "ausreichend": "Gründe für die internationale Arbeitsteilung und für die Störanfälligkeit von Lieferketten im Ansatz zutreffend erklärt und auf M3 bezogen werden.",
            "gut": "Arbeitsteilung und Störanfälligkeit schlüssig auf Kostenvorteile, Standortfaktoren und Risiken zurückgeführt werden und der Zielkonflikt zwischen Effizienz und Resilienz mit Materialbezug deutlich wird.",
        },
    },
    {
        "id": "q3-2-ii4",
        "afb": "II",
        "operator": "anwenden",
        "lk": True,
        "text": "Wenden Sie die Theorie der komparativen Kostenvorteile auf das folgende Beispiel (fiktive Zahlen) an und leiten Sie daraus wirtschaftspolitische Folgerungen ab: Deutschland benötigt für eine Maschine 20 und für einen Ballen Textilien 4 Arbeitsstunden, Vietnam für eine Maschine 60 und für einen Ballen Textilien 6 Arbeitsstunden. Deutschland stehen 120, Vietnam 240 Arbeitsstunden zur Verfügung. Ohne Handel stellt Deutschland 3 Maschinen und 15 Ballen her, Vietnam 2 Maschinen und 20 Ballen.",
        "material": [],
        "loesung": {
            "punkte": [
                "Absolute Kostenvorteile: Deutschland ist bei beiden Gütern absolut überlegen (20 statt 60 Stunden je Maschine, 4 statt 6 Stunden je Ballen) – nach Smith ließe sich Handel nicht begründen.",
                "Opportunitätskosten: Deutschland 1 Maschine = 5 Ballen (20 : 4), 1 Ballen = 0,2 Maschinen; Vietnam 1 Maschine = 10 Ballen (60 : 6), 1 Ballen = 0,1 Maschinen. Komparativer Vorteil Deutschlands bei Maschinen, Vietnams bei Textilien.",
                "Spezialisierung: Deutschland 120 : 20 = 6 Maschinen, Vietnam 240 : 6 = 40 Ballen. Gesamtproduktion 6 Maschinen und 40 Ballen statt 5 Maschinen und 35 Ballen – ein Mehr von 1 Maschine und 5 Ballen bei gleichem Arbeitseinsatz.",
                "Tauschverhältnis zwischen 5 und 10 Ballen je Maschine, z. B. 1 : 7. Beispiel: Deutschland tauscht 2 Maschinen gegen 14 Ballen; Deutschland verfügt dann über 4 Maschinen und 14 Ballen (statt 3 und 15), Vietnam über 2 Maschinen und 26 Ballen (statt 2 und 20) – beide Länder stellen sich besser.",
                "Wirtschaftspolitische Folgerungen: Abbau von Zöllen und Handelshemmnissen, Spezialisierung nach komparativen Vorteilen; Handel lohnt sich auch für das „unterlegene“ Land; Zölle (z. B. Vietnams auf Maschinen) würden die Wohlstandsgewinne verringern.",
                "Grenzen: Modellannahmen (keine Transportkosten, Vollbeschäftigung, unbewegliche Produktionsfaktoren, konstante Kosten), Verteilungsfolgen innerhalb der Länder (Stolper-Samuelson), Abhängigkeits- und Sicherheitsfragen, dynamische Effekte (Erziehungszoll-Argument nach List).",
            ],
            "hinweis": "Anwenden: Die Theorie wird auf das neue Beispiel übertragen; die Rechenschritte müssen nachvollziehbar dokumentiert sein. Andere korrekte Tauschverhältnisse zwischen 5 und 10 Ballen je Maschine sind gleichwertig.",
        },
        "bewertung": {
            "ausreichend": "die Opportunitätskosten im Wesentlichen korrekt berechnet, die komparativen Vorteile richtig zugeordnet und ein Spezialisierungsgewinn ansatzweise gezeigt werden.",
            "gut": "Rechnung, Spezialisierungsgewinn und ein geeignetes Tauschverhältnis vollständig und nachvollziehbar dargelegt und daraus begründete wirtschaftspolitische Folgerungen samt Grenzen des Modells abgeleitet werden.",
        },
    },
    {
        "id": "q3-2-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie die Forderung der Autorin, die WTO müsse von einem Motor der Liberalisierung zu einem Regelwerk für fairen, nachhaltigen Handel umgebaut werden – notfalls zunächst ohne die USA. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klärung: Liberalisierung (Zollabbau, Marktöffnung) vs. Regulierung (Regeln zu Subventionen, Umwelt- und Sozialstandards); plurilaterale „Koalitionen der Willigen“ statt Konsens aller [5], [6].",
                "Pro: Konsensprinzip und gescheiterte Doha-Runde zeigen die Grenzen weiterer Liberalisierung; neue Probleme (Staatssubventionen, Klimaschutz, Arbeitsstandards) brauchen Regeln; plurilaterale Lösungen sind handlungsfähig (MPIA, E-Commerce-Abkommen, Fischereiabkommen 2025); Handel wird in der Bevölkerung eher akzeptiert, wenn er als fair gilt; die EU hat als großer Binnenmarkt Gewicht.",
                "Kontra: Regulierung kann zu verstecktem („grünem“) Protektionismus werden und Entwicklungsländer benachteiligen [4]; Standards sind kaum konsensfähig; ohne die USA als größte Volkswirtschaft bleibt jede Reform lückenhaft und riskiert weitere Konfrontation; Clubs zersplittern den Welthandel und schließen ärmere Länder aus; Liberalisierung hat nachweislich Wohlstand geschaffen (Ricardo, Aufstieg Asiens).",
                "Differenzierungen: Kombination möglich (Marktöffnung für Entwicklungsländer plus Mindeststandards), Reform der Streitbeilegung als Voraussetzung, Einbindung des Globalen Südens (Übergangsfristen, Unterstützung, Sonderbehandlung).",
                "Begründetes eigenes Urteil nach Kriterien (z. B. Wohlstand und Effizienz, Gerechtigkeit, Nachhaltigkeit, Legitimität, Durchsetzbarkeit); verschiedene Ergebnisse sind möglich, wenn sie schlüssig begründet sind.",
            ],
            "hinweis": "Erörtern: Pro- und Kontra-Argumente abwägen und zu einem eigenen Urteil gelangen. Der Bezug zur Kontroverse Liberalisierung vs. Regulierung (Erlass-Schwerpunkt 2027) und Materialbezüge zu [4]–[6] sind zu erwarten.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist, Argumente beider Seiten enthält und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und abwägend ist, die Kontroverse Liberalisierung vs. Regulierung klar herausarbeitet und in ein schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q3-2-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie, ob gesetzliche Sorgfaltspflichten für Unternehmen ein geeignetes Mittel sind, um Menschenrechte und Umwelt in globalen Lieferketten zu schützen. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Kriterien: Wirksamkeit (Schutz der Betroffenen), Verhältnismäßigkeit und Kosten (Bürokratie, Wettbewerbsfähigkeit), Gerechtigkeit (faires Spielfeld), Durchsetzbarkeit.",
                "Sachlage: LkSG (seit 2023, ab 1.000 Beschäftigten; Risikoanalyse, Prävention, Abhilfe, Beschwerdeverfahren; Kontrolle durch das BAFA); CSDDD nach Omnibus I nur für Unternehmen mit mehr als 5.000 Beschäftigten und 1,5 Mrd. Euro Umsatz, ab 2029; geplante Entlastungen beim LkSG (Stand Oktober 2026).",
                "Für die Eignung: Freiwillige Selbstverpflichtungen reichten nicht (Rana Plaza 2013); Pflichten wirken über die Kunden auch auf kleinere Zulieferer [4]; Beschwerdesysteme geben Beschäftigten eine Stimme; einheitliche Regeln schaffen ein faires Spielfeld gegenüber Billiganbietern [5].",
                "Gegen die Eignung bzw. Grenzen: Bürokratie und Formularflut [5]; Kosten vor allem für den Mittelstand durch Weitergabe der Pflichten; Kontrolle tief in der Kette schwierig, Prüfberichte manipulierbar; Gefahr des Rückzugs aus Risikoländern zulasten der dortigen Beschäftigten [6]; Abschwächung 2025/26 und hohe Schwellen begrenzen die Reichweite; keine EU-weite zivilrechtliche Haftung.",
                "Ergänzungen und Alternativen: Branchenabkommen (International Accord), Stärkung von Gewerkschaften und Arbeitsrecht in Produktionsländern, Sozialkapitel in Handelsabkommen, Siegel (z. B. Grüner Knopf), Verbraucherverhalten.",
                "Begründetes Urteil, z. B.: grundsätzlich geeignet, aber nur bei praxistauglicher Ausgestaltung und in Kombination mit anderen Instrumenten wirksam.",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete, begründete Einschätzung auf Basis von Fachwissen. Der aktuelle Stand (Abschwächung von CSDDD und LkSG) sollte einbezogen und auf M3 bezogen werden.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einigen zutreffenden Argumenten und Bezügen zu M3 formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, fachlich fundiert (Regelungen, aktuelle Änderungen, Grenzen) und schlüssig begründet ist.",
        },
    },
    {
        "id": "q3-2-iii3",
        "afb": "III",
        "operator": "Stellung nehmen",
        "text": "Nehmen Sie ausgehend von M2 Stellung zu der Forderung, Deutschland solle seine wirtschaftlichen Abhängigkeiten von China und den USA durch eine konsequente De-Risking-Strategie deutlich verringern.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Ausgangslage aus M2: Beschaffungsabhängigkeit von China (Importe 170,6 Mrd. Euro, Elektronik 50,9 Mrd. Euro, Defizit 89,3 Mrd. Euro) und Absatzabhängigkeit von den USA (Exporte 146,2 Mrd. Euro, Rückgang um 9,4 %, Kfz −17,8 %).",
                "Klärung: De-Risking (gezielte Verringerung riskanter Abhängigkeiten) vs. Decoupling (Entkopplung); Instrumente: Diversifizierung, Lagerhaltung, Rohstoffpartnerschaften, EU-Gesetz über kritische Rohstoffe, Investitionsprüfungen, neue Freihandelsabkommen (Mercosur, Indien), Vertiefung des Binnenmarkts.",
                "Pro: Erpressbarkeit (Gas 2022, seltene Erden 2025), Versorgungssicherheit, Schutz vor Zollschocks, geopolitische Rivalität, europäische Handlungsfähigkeit.",
                "Kontra: höhere Kosten und Preise (Resilienz ist teuer), Verlust von Marktanteilen in großen Märkten, mögliche Gegenmaßnahmen, Effizienzverluste im Sinne der Außenhandelstheorie, kurzfristig begrenzte Alternativen; Unternehmen entscheiden selbst, der Staat kann nur Anreize und Regeln setzen.",
                "Offenlegung der eigenen Wertmaßstäbe (z. B. Sicherheit vs. Wohlstand, Freiheit des Handels vs. staatliche Steuerung) und begründete Stellungnahme; differenzierte Positionen (gezieltes De-Risking bei kritischen Gütern statt allgemeiner Abkopplung) sind möglich.",
            ],
            "hinweis": "Stellung nehmen: wie beurteilen, zusätzlich müssen die eigenen Wertmaßstäbe begründet offengelegt werden. Zahlenbezüge aus M2 sind erforderlich.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit einzelnen Bezügen zu M2 vorliegt und eigene Maßstäbe zumindest erkennbar werden.",
            "gut": "die Stellungnahme abwägend und fachlich fundiert ist, Daten aus M2 gezielt nutzt, die eigenen Wertmaßstäbe ausdrücklich offenlegt und schlüssig zu einem Ergebnis führt.",
        },
    },
    {
        "id": "q3-2-iii4",
        "afb": "III",
        "operator": "überprüfen",
        "lk": True,
        "text": "Überprüfen Sie unter Rückgriff auf Außenwirtschaftstheorien die Aussage der Autorin, Zölle schadeten vor allem dem eigenen Land und senkten am Ende den Wohlstand aller Beteiligten. (M1, Absatz [2])",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Theoretische Stütze: Nach Smith und Ricardo verhindern Zölle die Spezialisierung nach Kostenvorteilen; Folgen sind Wohlfahrtsverluste durch höhere Preise, weniger Wettbewerb und ineffiziente Produktion; Zölle wirken wie eine Steuer auf die eigenen Verbraucher und auf Unternehmen, die Vorprodukte importieren; Vergeltungszölle vergrößern die Verluste (Zollspirale der 1930er-Jahre).",
                "Heckscher-Ohlin bzw. Stolper-Samuelson: Freihandel nützt dem reichlich vorhandenen Faktor; Zölle können den knappen Faktor (z. B. gering qualifizierte Industriearbeit in den USA) kurzfristig schützen – nicht alle verlieren gleichermaßen (Verteilungsargument).",
                "Gegenargumente: Ein großes Land kann mit einem „Optimalzoll“ einen Teil der Last auf ausländische Exporteure abwälzen; Erziehungszoll-Argument (List); Sicherheits- und Resilienzargumente; Zölle als Verhandlungsdruck.",
                "Empirie: Studien zu den US-Zöllen von 2018/2019 fanden, dass die Kosten überwiegend von US-Importeuren und Verbrauchern getragen wurden – das stützt eher die Autorin.",
                "Grenzen der Theorien: statische Modelle, Vollbeschäftigung, keine Macht- und Sicherheitspolitik; der Gesamtwohlstand verdeckt Verteilungsfragen.",
                "Ergebnis: Die Aussage ist theoretisch und empirisch gut gestützt, aber zu pauschal – Verteilungseffekte, strategische Zölle und nichtökonomische Ziele müssen differenziert betrachtet werden.",
            ],
            "hinweis": "Überprüfen: die Aussage auf Grundlage von Fachkenntnissen kritisch hinterfragen und begründet einschätzen. Mindestens zwei Theorien (z. B. Ricardo, Heckscher-Ohlin) sollen sachgerecht angewendet werden.",
        },
        "bewertung": {
            "ausreichend": "die Aussage mithilfe mindestens einer Außenwirtschaftstheorie ansatzweise zutreffend überprüft und eine begründete Einschätzung formuliert wird.",
            "gut": "die Aussage mit mehreren Theorien fachlich korrekt überprüft, Gegenargumente und Grenzen der Theorien einbezogen und eine differenzierte, schlüssig begründete Einschätzung formuliert wird.",
        },
    },
]
