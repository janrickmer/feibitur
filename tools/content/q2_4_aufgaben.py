# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q2.4 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q2.4, insbesondere Entwicklung von Beschäftigung (Fachkräftemangel) und Beschäftigungsstrukturen, Wirkung arbeitsmarktpolitischer Instrumente, Tarifvertragsparteien, Tarifpolitik und Tarifautonomie sowie konkurrierende Gerechtigkeitsbegriffe (Bedarfs- und Leistungsgerechtigkeit, Chancengleichheit, Diskriminierung)."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Fachkräfte gesucht – trotz fast drei Millionen Arbeitslosen“ (2026)",
        "absaetze": [
            "Es klingt wie ein Widerspruch: Im Oktober 2026 waren in Deutschland 2,955 Millionen Menschen arbeitslos gemeldet, die Arbeitslosenquote lag bei 6,3 Prozent. Gleichzeitig finden Pflegeheime keine Pflegefachkräfte, Kitas keine Erzieherinnen und Handwerksbetriebe keine Elektroniker. Die Bundesagentur für Arbeit zählte 2025 nicht weniger als 157 Berufe, in denen Fachkräfte knapp sind.",
            "Der Widerspruch löst sich auf, wenn man genauer hinsieht. Die Industrie baut seit Monaten Stellen ab, besonders in der Auto- und Zulieferbranche, während Gesundheitswesen, Kitas und Handwerk händeringend suchen. Wer zwanzig Jahre am Band gestanden hat, wird nicht über Nacht Pflegefachkraft. Und eine freie Stelle in Oberbayern hilft einem Arbeitslosen in Vorpommern nur, wenn er umziehen kann und will. Laut Bundesagentur suchte 2025 nur etwa jede fünfte arbeitslose Fachkraft überhaupt eine Stelle in einem Engpassberuf.",
            "Dahinter steht eine Entwicklung, die sich nicht wegverhandeln lässt: Die geburtenstarken Jahrgänge gehen in Rente, und es rücken deutlich weniger Junge nach. 2025 ist die Zahl der Erwerbstätigen erstmals seit 2020 gesunken – nicht nur wegen der schwachen Konjunktur, sondern auch wegen der Demografie. Ohne Zuwanderung und ohne mehr erwerbstätige Frauen und Ältere wäre der Rückgang deutlich größer ausgefallen. In den Engpassberufen hat sich der Anteil ausländischer Beschäftigter seit 2014 auf rund 14 Prozent verdoppelt.",
            "Die Politik hat einiges getan: Die Chancenkarte erleichtert seit 2024 die Einreise zur Jobsuche, die Aktivrente macht seit Januar 2026 Arbeit nach dem Erreichen der Regelaltersgrenze steuerlich attraktiver, und Kurzarbeitergeld kann 2026 bis zu 24 Monate gezahlt werden. Doch vieles passt nicht zusammen. Visa- und Anerkennungsverfahren dauern oft viele Monate. Und wer Beschäftigte zwei Jahre lang in Kurzarbeit hält, obwohl ihr Arbeitsplatz absehbar nicht zurückkommt, verschiebt das Problem nur.",
            "Ich plädiere deshalb für einen Kurswechsel. Erstens sollte es Kurzarbeitergeld in Branchen im Strukturwandel nur noch geben, wenn die ausgefallene Arbeitszeit verbindlich für Weiterbildung genutzt wird – am besten für Berufe, in denen Fachkräfte fehlen. Zweitens sollten Arbeitslose ohne Aussicht auf eine Stelle in ihrem alten Beruf stärker in Umschulungen für Engpassberufe gelenkt werden, notfalls mit Verpflichtung, aber verbunden mit einem spürbaren finanziellen Bonus. Drittens gehören die Einwanderungsverfahren in eine zentrale, digitale Stelle statt in Hunderte Ausländerbehörden. Die Bundesregierung hat im November 2025 Eckpunkte für eine solche „Work-and-Stay-Agentur“ beschlossen – sie muss schnell Wirklichkeit werden.",
            "Kritiker werden einwenden, der Staat solle Menschen nicht in bestimmte Berufe drängen, und Weiterbildung lasse sich nicht erzwingen. Doch die Alternative ist teurer: Wenn wir Arbeitslosigkeit finanzieren, während Pflegebetten leer bleiben, weil das Personal fehlt, verlieren alle – die Arbeitslosen, die Betriebe und eine Gesellschaft, die auf diese Arbeit angewiesen ist.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Arbeitsmarktforscherin (2026). Die genannten Zahlen stammen von der Bundesagentur für Arbeit (Oktober 2026; Engpassanalyse 2025, Presseinfo vom 2.9.2026) und von Destatis (Januar 2026).",
    },
    {
        "id": "m2",
        "titel": "M2: Verdienstabstand zwischen Frauen und Männern in Deutschland (2025)",
        "typ": "tabelle",
        "kopf": ["Merkmal", "Wert 2025", "Anteil an der Verdienstlücke"],
        "zeilen": [
            ["Durchschnittlicher Bruttostundenverdienst der Frauen", "22,81 €", "–"],
            ["Durchschnittlicher Bruttostundenverdienst der Männer", "27,05 €", "–"],
            ["Verdienstabstand (unbereinigter Gender Pay Gap)", "4,24 € bzw. 16 %", "100 %"],
            ["davon statistisch erklärbar durch: höheren Teilzeitanteil der Frauen", "0,81 €", "19 %"],
            ["… häufigere Tätigkeit in Branchen und Berufen mit niedrigerer Bezahlung", "0,75 €", "18 %"],
            ["… geringeres Anforderungsniveau der ausgeübten Tätigkeit", "0,55 €", "13 %"],
            ["… weitere erfasste Merkmale (nicht einzeln ausgewiesen)", "0,42 €", "10 %"],
            ["Nicht erklärter Teil (bereinigter Gender Pay Gap)", "1,71 € bzw. 6 %", "40 %"],
            ["Unbereinigter Gender Pay Gap West / Ost", "17 % / 5 %", "–"],
            ["Bereinigter Gender Pay Gap West / Ost", "6 % / 9 %", "–"],
            ["Gender Gap Arbeitsmarkt (Verdienst, bezahlte Arbeitsstunden und Erwerbsbeteiligung zusammen)", "37 %", "–"],
        ],
        "quelle": "Statistisches Bundesamt (Destatis): Pressemitteilung Nr. 453 vom 16. Dezember 2025 (Verdiensterhebung, Berichtsmonat April 2025) und Angaben zum Equal Pay Day am 27. Februar 2026 (Gender Gap Arbeitsmarkt). Die Zeile „weitere erfasste Merkmale“ ist rechnerisch aus der Differenz ermittelt. Laut Destatis ist der bereinigte Wert als Obergrenze für Verdienstdiskriminierung zu verstehen, da z. B. Erwerbsunterbrechungen nicht erfasst werden.",
    },
    {
        "id": "m3",
        "titel": "M3: Bericht „Verhandeln, streiken, schlichten – hat das Tarifmodell Zukunft?“ (2026)",
        "absaetze": [
            "Seit dem 1. November 2026 wird in der Metall- und Elektroindustrie wieder gestreikt. Die IG Metall fordert fünf Prozent mehr Geld, eine tarifliche Sicherung der Beschäftigung und eine Gewinnbeteiligung in Unternehmen, denen es wirtschaftlich gut geht. Die Arbeitgeber hatten in der zweiten Verhandlungsrunde 1,3 Prozent mehr Geld angeboten – allerdings erst ab Juli 2028. Die Gewerkschaft nannte das „eine Provokation“ und rief mit dem Ende der Friedenspflicht am 31. Oktober zu Warnstreiks auf.",
            "Für die Sprecherin eines regionalen Arbeitgeberverbandes ist die Forderung realitätsfern: „Viele unserer Betriebe kämpfen mit hohen Energiepreisen, schwachen Exporten und dem Umbruch in der Autoindustrie. Wer jetzt fünf Prozent fordert, gefährdet Arbeitsplätze.“ Ein Gewerkschaftssekretär hält dagegen: „Die Beschäftigten haben in der Inflation 2022 real verloren. Und ohne Druck hat es noch nie faire Löhne gegeben.“",
            "Hinter dem Konflikt steht eine grundsätzlichere Frage. Nach dem IAB-Betriebspanel arbeiteten 2025 nur noch 42 Prozent der Beschäftigten in einem Betrieb mit Branchentarifvertrag; 1996 waren es 67 Prozent. Besonders niedrig ist die Tarifbindung im Handel, im Gastgewerbe und in der IT-Branche. Viele Unternehmen sind aus ihren Verbänden ausgetreten oder haben in eine Mitgliedschaft ohne Tarifbindung gewechselt.",
            "Der Staat versucht gegenzusteuern. Seit Mai 2026 müssen Unternehmen, die Bau- oder Dienstleistungsaufträge des Bundes ab 50.000 Euro erhalten, ihren Beschäftigten tarifliche Arbeitsbedingungen gewähren. Der Mindestlohn steigt nach einem Beschluss der Mindestlohnkommission 2027 auf 14,60 Euro. Der Vertreter eines Mittelstandsverbandes kritisiert: „Der Staat untergräbt die Tarifautonomie, wenn er Tarifbindung erzwingt.“ Eine Betriebsrätin entgegnet: „Ohne starke Tarifverträge entscheidet am Ende der Gesetzgeber über die Löhne – das kann eigentlich niemand wollen.“",
            "Zugleich wird über die Grenzen des Streikrechts gestritten. Nach mehreren langen Arbeitskämpfen bei Bahn und Flughäfen in den vergangenen Jahren fordert der Präsident eines Wirtschaftsverbandes ein Gesetz für die kritische Infrastruktur: Streiks sollen dort mindestens vier Tage vorher angekündigt werden, ein Notbetrieb soll garantiert sein, und vor jedem Streik soll eine Schlichtung stattfinden müssen. „Das Streikrecht ist ein Grundrecht, aber kein Recht, ein ganzes Land lahmzulegen“, sagt er.",
            "Die Gewerkschaften lehnen das ab. Eine Arbeitsrechtlerin gibt zu bedenken, Art. 9 Abs. 3 GG schütze auch den Arbeitskampf, und die Gerichte prüften schon heute, ob ein Streik verhältnismäßig sei. Eine Pflicht zur Schlichtung würde das Gleichgewicht zwischen den Tarifparteien zugunsten der Arbeitgeber verschieben: „Tarifverhandlungen ohne glaubwürdige Streikdrohung sind, wie das Bundesarbeitsgericht einmal sinngemäß gesagt hat, kollektives Betteln.“",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Bericht (2026). Die zitierten Verbandsvertreter, die Betriebsrätin und die Arbeitsrechtlerin sind fiktiv. Angaben zur Metall-Tarifrunde: IG Metall (Stand: 2. November 2026); Tarifbindung: IAB-Betriebspanel 2025 (WSI-Mitteilungen 4/2026); Bundestariftreuegesetz in Kraft seit 1. Mai 2026.",
    },
]

AUFGABEN = [
    {
        "id": "q2-4-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Kommentar), Titel, Erscheinungsjahr (2026), Thema (Fachkräftemangel trotz hoher Arbeitslosigkeit, Vorschläge zur Arbeitsmarktpolitik) und Hinweis auf eine (fiktive) Arbeitsmarktforscherin als Autorin.",
            "punkte": [
                "Die Autorin beschreibt einen scheinbaren Widerspruch: 2,955 Mio. Arbeitslose (Quote 6,3 %, Oktober 2026) bei gleichzeitigem Personalmangel in Pflege, Kitas und Handwerk; 157 Engpassberufe laut BA [1].",
                "Sie erklärt den Widerspruch mit Stellenabbau in der Industrie bei Bedarf in anderen Bereichen, fehlender Qualifikation und regionaler Distanz; nur etwa jede fünfte arbeitslose Fachkraft suche in einem Engpassberuf [2].",
                "Als grundlegende Ursache nennt sie den demografischen Wandel; 2025 sei die Erwerbstätigenzahl erstmals seit 2020 gesunken; Zuwanderung sowie Frauen und Ältere hätten Schlimmeres verhindert; Anteil ausländischer Beschäftigter in Engpassberufen rund 14 % [3].",
                "Sie würdigt Maßnahmen (Chancenkarte, Aktivrente, verlängertes Kurzarbeitergeld), kritisiert aber lange Verfahren und eine Kurzarbeit, die Strukturprobleme nur verschiebe [4].",
                "Sie fordert Kurzarbeitergeld im Strukturwandel nur bei verbindlicher Weiterbildung, eine stärkere – notfalls verpflichtende – Lenkung Arbeitsloser in Umschulungen für Engpassberufe mit finanziellem Bonus sowie eine zentrale digitale Einwanderungsstelle (Work-and-Stay-Agentur) [5].",
                "Den Einwand staatlicher Bevormundung weist sie mit dem Argument zurück, dass Untätigkeit für alle teurer sei [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache, keine Wertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen des Kommentars weitgehend vollständig, strukturiert, komprimiert und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q2-4-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die in M2 dargestellten Daten zum Verdienstabstand zwischen Frauen und Männern.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle des Statistischen Bundesamts zum Gender Pay Gap im Jahr 2025 (Bruttostundenverdienste, Zerlegung der Lücke, regionale Unterschiede).",
            "punkte": [
                "Frauen verdienten 2025 durchschnittlich 22,81 € brutto pro Stunde, Männer 27,05 €; der Abstand beträgt 4,24 € bzw. 16 % (unbereinigter Gender Pay Gap).",
                "Rund 60 % der Lücke (2,53 €) sind statistisch erklärbar: Teilzeit 19 %, Branchen und Berufe mit niedrigerer Bezahlung 18 %, Anforderungsniveau 13 %, weitere Merkmale 10 %.",
                "40 % der Lücke (1,71 €) bleiben unerklärt; dies entspricht dem bereinigten Gender Pay Gap von 6 %.",
                "Regionale Unterschiede: unbereinigt Westdeutschland 17 %, Ostdeutschland 5 %; bereinigt dagegen West 6 %, Ost 9 %.",
                "Der Gender Gap Arbeitsmarkt, der zusätzlich Arbeitszeit und Erwerbsbeteiligung berücksichtigt, liegt mit 37 % deutlich höher.",
                "Quellenkritische Angabe: Destatis versteht den bereinigten Wert als Obergrenze möglicher Diskriminierung, da Erwerbsunterbrechungen nicht erfasst sind.",
            ],
            "hinweis": "Beschreiben: Daten strukturiert und fachsprachlich in eigenen Worten darlegen (Überblick, zentrale Werte, Auffälligkeiten); noch keine Deutung oder Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die zentralen Werte der Tabelle im Ansatz korrekt und strukturiert beschrieben werden.",
            "gut": "die Daten vollständig, strukturiert, fachsprachlich präzise (unbereinigter/bereinigter Gender Pay Gap, erklärte Anteile, regionale Unterschiede) und ohne vorzeitige Wertung beschrieben werden.",
        },
    },
    {
        "id": "q2-4-i3",
        "afb": "I",
        "operator": "wiedergeben",
        "text": "Geben Sie die in M3 dargestellten Positionen zur Tarifpolitik und zum Streikrecht wieder.",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitungssatz: Bericht „Verhandeln, streiken, schlichten – hat das Tarifmodell Zukunft?“ (2026) über die Metall-Tarifrunde 2026, die sinkende Tarifbindung und die Debatte um das Streikrecht.",
            "punkte": [
                "Ausgangslage: Warnstreiks in der Metall- und Elektroindustrie seit dem 1. November 2026; Forderung der IG Metall (5 %, Beschäftigungssicherung, Gewinnbeteiligung) vs. Angebot der Arbeitgeber (1,3 % ab Juli 2028) [1].",
                "Arbeitgeberseite: Forderung sei angesichts von Energiepreisen, Exportschwäche und Umbruch der Autoindustrie arbeitsplatzgefährdend; Gewerkschaftsseite: Reallohnverluste 2022, faire Löhne nur durch Druck [2].",
                "Sinkende Tarifbindung (42 % Branchentarif 2025 gegenüber 67 % 1996), besonders niedrig in Handel, Gastgewerbe und IT; Verbandsflucht und OT-Mitgliedschaften [3].",
                "Staatliche Maßnahmen (Bundestariftreuegesetz, Mindestlohnerhöhung) und Kontroverse: Mittelstandsvertreter sieht Untergrabung der Tarifautonomie, Betriebsrätin sieht in starken Tarifverträgen die Alternative zu staatlicher Lohnsetzung [4].",
                "Forderung eines Wirtschaftsverbandes nach gesetzlichen Regeln für Streiks in der kritischen Infrastruktur (Ankündigungsfrist von vier Tagen, Notbetrieb, Schlichtungspflicht) [5].",
                "Gegenposition: Gewerkschaften und Arbeitsrechtlerin verweisen auf Art. 9 Abs. 3 GG, bestehende gerichtliche Verhältnismäßigkeitskontrolle und die Gefahr eines Ungleichgewichts zulasten der Gewerkschaften [6].",
            ],
            "hinweis": "Wiedergeben: ausgehend von einem Einleitungssatz die Positionen in eigenen Worten und mit Fachsprache ausdrücken; Positionen den jeweiligen Akteuren zuordnen; keine eigene Stellungnahme.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Positionen im Ansatz korrekt und den Akteuren zugeordnet wiedergegeben werden.",
            "gut": "die Positionen vollständig, strukturiert, in eigenen Worten und mit korrekter Zuordnung zu den Akteuren wiedergegeben werden.",
        },
    },
    {
        "id": "q2-4-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 die Ursachen des Fachkräftemangels in Deutschland.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Begriffsklärung: dauerhaft unbesetzte Stellen für qualifizierte Arbeitskräfte in bestimmten Berufen/Regionen; Messung über die Engpassanalyse der BA (2025: 157 Engpassberufe) [1].",
                "Demografischer Wandel: Renteneintritt der Babyboomer, schwächere Nachwuchsjahrgänge, sinkendes Erwerbspersonenpotenzial (IAB-Projektion: ohne Zuwanderung bis 2035 gut 7 Mio. weniger); Erwerbstätigenzahl 2025 erstmals gesunken [3].",
                "Mismatch: qualifikatorisch (Industriebeschäftigte vs. Pflege-/Kitaberufe), berufsfachlich und regional (Oberbayern vs. Vorpommern); nur jede fünfte arbeitslose Fachkraft sucht in Engpassberufen [2].",
                "Strukturwandel: Stellenabbau in Industrie (Auto/Zulieferer), Wachstum in Gesundheit, Erziehung, Handwerk; neue Anforderungen durch Digitalisierung und Energiewende [2].",
                "Arbeitsbedingungen und Attraktivität von Berufen (Belastung, Bezahlung in Pflege und Kitas), hohe Teilzeitquote insbesondere von Frauen, begrenzte Kinderbetreuung.",
                "Institutionelle Hürden: lange Visa- und Anerkennungsverfahren bremsen Zuwanderung; Kurzarbeit kann Beschäftigte in schrumpfenden Branchen halten [4].",
            ],
            "hinweis": "Erläutern: Ursachen mit zusätzlichen Informationen und Beispielen veranschaulichen; Materialbezug und Fachbegriffe (Mismatch, Erwerbspersonenpotenzial, Strukturwandel) werden erwartet. Eine bloße Aufzählung ohne Veranschaulichung genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "mehrere Ursachen des Fachkräftemangels ansatzweise zutreffend und mit Materialbezug erläutert werden.",
            "gut": "die Ursachen differenziert (Demografie, Mismatch, Strukturwandel, Arbeitsbedingungen, institutionelle Hürden), fachsprachlich präzise und mit Beispielen und Materialbelegen erläutert werden.",
        },
    },
    {
        "id": "q2-4-ii2",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie ausgehend von M3 die Tarifautonomie sowie den Ablauf von Tarifverhandlungen einschließlich Arbeitskampf und Schlichtung.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Grundlage: Koalitionsfreiheit nach Art. 9 Abs. 3 GG; Tarifautonomie als Recht der Tarifvertragsparteien (Gewerkschaften, Arbeitgeberverbände, einzelne Arbeitgeber, § 2 TVG), Arbeitsbedingungen ohne staatliche Einmischung zu regeln; Staat setzt nur den Rahmen (TVG).",
                "Begründung: Sachnähe der Sozialpartner, Kräftegleichgewicht, Funktionen des Flächentarifvertrags (Schutz-, Kartell-, Ordnungs-, Friedensfunktion); Wirkung des Tarifvertrags unmittelbar und zwingend für Tarifgebundene (§§ 3, 4 TVG), Günstigkeitsprinzip.",
                "Ablauf: Auslaufen/Kündigung des Tarifvertrags, Forderung und Angebot (Beispiel Metall 2026: 5 % vs. 1,3 % ab 2028), Verhandlungen; nach Ende der Friedenspflicht Warnstreiks (seit 1.11.2026) [1].",
                "Bei Scheitern: Schlichtung nur, wenn vereinbart (keine Zwangsschlichtung); Urabstimmung (meist 75 % laut Gewerkschaftssatzung), Streik, ggf. Aussperrung; Einigung, zweite Urabstimmung, neuer Tarifvertrag mit Friedenspflicht.",
                "Rechtliche Grenzen des Arbeitskampfs: Richterrecht des BAG – tariflich regelbares Ziel, gewerkschaftliche Trägerschaft, Verhältnismäßigkeit/ultima ratio; keine politischen Streiks [5], [6].",
                "Bezug zur aktuellen Lage: sinkende Tarifbindung (42 % Branchentarif 2025) schwächt die Reichweite des Modells; staatliche Stützen (Tariftreuegesetz, Mindestlohn) [3], [4].",
            ],
            "hinweis": "Erklären: Rückführung auf Grundprinzipien (Art. 9 Abs. 3 GG, TVG, Kräftegleichgewicht) und Funktionszusammenhänge; der Ablauf ist logisch zu begründen, nicht nur aufzuzählen; Materialbezug erforderlich.",
        },
        "bewertung": {
            "ausreichend": "Tarifautonomie und Ablauf von Tarifverhandlungen im Ansatz zutreffend erklärt und auf das Material bezogen werden.",
            "gut": "Tarifautonomie und Tarifrunde differenziert auf ihre rechtlichen Grundlagen und Funktionslogik zurückgeführt und durchgängig mit dem Fallbeispiel in M3 verknüpft werden.",
        },
    },
    {
        "id": "q2-4-ii3",
        "afb": "II",
        "operator": "auswerten",
        "text": "Werten Sie M2 im Hinblick auf die Frage aus, inwieweit der Verdienstabstand zwischen Frauen und Männern auf Diskriminierung zurückzuführen ist.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Unterscheidung: Der unbereinigte Gender Pay Gap (16 %) misst den Durchschnittsabstand, nicht gleiche Bezahlung für gleiche Arbeit; er ist kein direktes Maß für Diskriminierung.",
                "60 % der Lücke sind strukturell erklärbar (Teilzeit, Branchen/Berufe, Anforderungsniveau) – das bedeutet aber nicht automatisch Diskriminierungsfreiheit: Hinter Teilzeit und Berufswahl können ungleiche Sorgearbeit, Rollenbilder, fehlende Kinderbetreuung und eine geringere Bewertung typischer „Frauenberufe“ stehen (strukturelle bzw. mittelbare Benachteiligung).",
                "Der bereinigte Wert (6 %) ist laut Destatis eine Obergrenze für unmittelbare Verdienstdiskriminierung, weil z. B. Erwerbsunterbrechungen nicht erfasst sind; tatsächliche Diskriminierung kann also geringer sein, ist aber nicht ausgeschlossen.",
                "Ost-West-Vergleich: niedrigerer unbereinigter Wert im Osten (5 %), aber höherer bereinigter Wert (9 %) – Hinweis darauf, dass Strukturunterschiede (z. B. höhere Vollzeitquote, andere Branchenstruktur) und unerklärte Unterschiede unabhängig voneinander variieren.",
                "Gender Gap Arbeitsmarkt (37 %) zeigt, dass die Einkommensungleichheit weit über die Stundenlöhne hinausgeht (Arbeitszeit, Erwerbsbeteiligung) – relevant für Chancengleichheit und Alterssicherung.",
                "Gesamtaussage: Direkte Lohndiskriminierung erklärt höchstens einen kleineren Teil; der größere Teil beruht auf strukturellen Faktoren, deren Bewertung (freie Entscheidung oder strukturelle Benachteiligung) umstritten ist.",
            ],
            "hinweis": "Auswerten: Einzelwerte zu einer abschließenden Gesamtaussage zusammenführen; Unterscheidung unbereinigt/bereinigt und unmittelbare/mittelbare Diskriminierung erwartet; reine Wiederholung der Zahlen genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "die Daten ansatzweise im Hinblick auf die Fragestellung ausgewertet werden und eine nachvollziehbare Gesamtaussage formuliert wird.",
            "gut": "die Daten differenziert und fachlich präzise (bereinigt/unbereinigt, strukturelle vs. unmittelbare Diskriminierung, Grenzen der Statistik) ausgewertet werden und in eine schlüssige Gesamtaussage münden.",
        },
    },
    {
        "id": "q2-4-ii4",
        "afb": "II",
        "operator": "erläutern",
        "lk": True,
        "text": "Erläutern Sie ausgehend von M1 die Bestimmungsgründe von Arbeitsangebot und Arbeitsnachfrage in Deutschland sowie Möglichkeiten ihrer politischen Steuerung.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Modellrahmen: neoklassischer Arbeitsmarkt mit Arbeitsangebot (Haushalte) und Arbeitsnachfrage (Unternehmen), Reallohn als Preis; Grenzen des Modells (Mismatch, Marktmacht, Monopson, Kaufkrafteffekt).",
                "Bestimmungsgründe des Angebots: Demografie (Babyboomer, M1 [3]), Erwerbsbeteiligung von Frauen und Älteren, Teilzeit, Zuwanderung (Anteil ausländischer Beschäftigter in Engpassberufen), Qualifikation, Lohnhöhe sowie Steuern und Abgaben.",
                "Bestimmungsgründe der Nachfrage: abgeleitete Nachfrage aus Güternachfrage (Konjunkturschwäche, Industrieabbau, M1 [2]), Lohnstückkosten, technischer Fortschritt (Automatisierung, KI), Strukturwandel (Auto/Zulieferer vs. Gesundheit/Erziehung), Energiepreise und Standortbedingungen.",
                "Steuerung des Angebots: Fachkräfteeinwanderungsgesetz/Chancenkarte und Work-and-Stay-Agentur, Aktivrente, Kinderbetreuung, Weiterbildung und Umschulung, Anreize zur Ausweitung von Teilzeit [4], [5].",
                "Steuerung der Nachfrage: Kurzarbeitergeld, Lohnkostenzuschüsse, Konjunktur- und Investitionspolitik, Senkung der Lohnnebenkosten; Mindestlohn als Regulierung mit umstrittener Wirkung auf die Nachfrage.",
                "Einordnung: angebotsorientierte (Q2.2) vs. nachfrageorientierte (Q2.1) Steuerungslogik.",
            ],
            "hinweis": "Erläutern (LK): Bestimmungsgründe modellgestützt und mit Beispielen aus M1 veranschaulichen; Unterscheidung von Angebots- und Nachfrageseite muss klar erkennbar sein.",
        },
        "bewertung": {
            "ausreichend": "zentrale Bestimmungsgründe von Arbeitsangebot und -nachfrage und einzelne Steuerungsmöglichkeiten ansatzweise zutreffend erläutert werden.",
            "gut": "die Bestimmungsgründe modellgestützt, systematisch nach Angebot und Nachfrage getrennt, mit Materialbezug erläutert und passende Steuerungsinstrumente differenziert zugeordnet werden.",
        },
    },
    {
        "id": "q2-4-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Die Autorin fordert, Kurzarbeitergeld in Branchen im Strukturwandel nur noch bei verbindlicher Weiterbildung zu zahlen und Arbeitslose stärker in Umschulungen für Engpassberufe zu lenken. Erörtern Sie diese Forderung. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klärung: Kurzarbeitergeld als Instrument zur Überbrückung vorübergehender Arbeitsausfälle (2026 bis zu 24 Monate); aktive Arbeitsmarktpolitik durch Weiterbildung/Umschulung; Kriterien z. B. Effektivität gegen Fachkräftemangel, Kosten, Freiheit der Berufswahl (Art. 12 GG), soziale Gerechtigkeit.",
                "Pro: Kurzarbeit im Strukturwandel kann nicht zukunftsfähige Arbeitsplätze konservieren (Lock-in) [4]; Ausfallzeit sinnvoll für Qualifizierung nutzbar; Abbau von Mismatch [2]; Arbeitskräfte für Pflege, Kitas, Handwerk; geringere Kosten für Arbeitslosigkeit [6]; finanzieller Bonus erhöht Akzeptanz [5].",
                "Contra: Unterscheidung zwischen konjunkturellen und strukturellen Ausfällen in der Praxis schwierig; Betriebe könnten auf Kurzarbeit verzichten und entlassen; Weiterbildung braucht Motivation und Eignung – Zwang senkt Erfolgschancen; nicht jede/r ist für Pflege oder Erziehung geeignet; Eingriff in Berufsfreiheit; Kapazitäten bei Bildungsträgern und Ausbildungsbetrieben; Umschulungen dauern Jahre; Ursachen wie Bezahlung und Arbeitsbedingungen in Engpassberufen bleiben unberührt.",
                "Alternativen/Ergänzungen: Anreize statt Zwang (Weiterbildungsgeld, Qualifizierungsförderung im Betrieb), bessere Arbeitsbedingungen, schnellere Anerkennung ausländischer Abschlüsse, Kinderbetreuung zur Ausweitung von Teilzeit.",
                "Abwägung und begründetes eigenes Urteil (z. B. Kopplung von Kurzarbeit an Qualifizierung in Strukturbranchen sinnvoll, Zwang bei Umschulungen problematisch).",
            ],
            "hinweis": "Erörtern: Pro- und Kontraargumente abwägen und zu einem eigenen, begründeten Urteil gelangen; Bezug zur konkreten Forderung in [5] und Fachwissen zu Kurzarbeit und aktiver Arbeitsmarktpolitik erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist, Pro- und Kontraargumente enthält und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, kriteriengeleitet und fachlich fundiert ist und in ein weitgehend klares und schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q2-4-iii2",
        "afb": "III",
        "operator": "Stellung nehmen",
        "text": "Nehmen Sie unter Bezug auf konkurrierende Gerechtigkeitsbegriffe Stellung zu der Frage, ob der Verdienstabstand zwischen Frauen und Männern politisch korrigiert werden sollte. (M2)",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Leistungsgerechtigkeit: Lohnunterschiede bei unterschiedlicher Arbeitszeit, Verantwortung oder Qualifikation gelten als gerechtfertigt; Eingriffe in Lohnfindung (Tarifautonomie, Vertragsfreiheit) problematisch; aber: gleiche Leistung muss gleich bezahlt werden (unerklärter Rest von bis zu 6 %).",
                "Chancengleichheit: Teilzeit, Berufswahl und Erwerbsunterbrechungen sind nicht nur freie Entscheidungen, sondern hängen von Kinderbetreuung, Pflegeverantwortung, Rollenbildern und steuerlichen Anreizen ab; strukturelle Ungleichheit (Gender Gap Arbeitsmarkt 37 %) schränkt Chancen ein.",
                "Bedarfsgerechtigkeit: geringere Erwerbseinkommen führen zu geringeren Renten und höherem Armutsrisiko (z. B. Alleinerziehende); Folgen für soziale Sicherung.",
                "Diskriminierungsfreiheit: Art. 3 Abs. 2 GG, AGG, Entgelttransparenzgesetz; EU-Entgelttransparenzrichtlinie (Umsetzungsfrist 7.6.2026 verpasst).",
                "Mögliche Maßnahmen und ihre Bewertung: Lohntransparenz, Aufwertung sozialer Berufe (Tarifpolitik), Ausbau der Kinderbetreuung, Reform steuerlicher Anreize, Partnermonate beim Elterngeld; Gegenargumente: Bürokratie, Eingriff in Tarifautonomie, Kosten, Respekt vor individuellen Lebensentscheidungen.",
                "Eigene Wertmaßstäbe ausdrücklich offenlegen (z. B. Vorrang der Chancengleichheit vs. Vorrang der Vertragsfreiheit) und begründete Position formulieren.",
            ],
            "hinweis": "Stellung nehmen: wie beurteilen, zusätzlich müssen die eigenen Wertmaßstäbe begründet dargelegt werden. Mindestens zwei Gerechtigkeitsbegriffe sind fachlich korrekt anzuwenden; Bezug zu den Daten in M2 erforderlich.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit Bezug zu mindestens zwei Gerechtigkeitsbegriffen und erkennbaren eigenen Maßstäben vorliegt.",
            "gut": "die Stellungnahme abwägend, fachlich fundiert und datengestützt ist, die konkurrierenden Gerechtigkeitsbegriffe präzise anwendet, eigene Wertmaßstäbe ausdrücklich offenlegt und in ein klares Urteil mündet.",
        },
    },
    {
        "id": "q2-4-iii3",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie die in M3 erhobene Forderung nach gesetzlichen Regeln für Streiks in der kritischen Infrastruktur.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Kriterien benennen, z. B. Vereinbarkeit mit Art. 9 Abs. 3 GG, Kräftegleichgewicht der Tarifparteien, Schutz der Allgemeinheit/Daseinsvorsorge, Wirksamkeit, Rechtssicherheit.",
                "Für die Forderung: Streiks bei Bahn, Flughäfen, Energie oder Kliniken treffen Unbeteiligte stark [5]; Ankündigungsfristen und Notdienste ermöglichen Planung; Schlichtung kann Konflikte ohne Streik lösen; klare gesetzliche Regeln statt Richterrecht schaffen Rechtssicherheit; Vergleich mit anderen Staaten mit Regeln für Daseinsvorsorge.",
                "Gegen die Forderung: Arbeitskampf ist durch Art. 9 Abs. 3 GG geschützt; Gerichte prüfen bereits die Verhältnismäßigkeit [6]; Pflichtschlichtung und lange Fristen schwächen die Streikdrohung und verschieben das Gleichgewicht zugunsten der Arbeitgeber („kollektives Betteln“); Abgrenzung kritischer Infrastruktur schwierig; Notdienste werden oft schon heute vereinbart; Gefahr einer schleichenden Aushöhlung der Tarifautonomie bei ohnehin sinkender Tarifbindung [3].",
                "Differenzierte Lösungen möglich: freiwillige Schlichtungsvereinbarungen der Tarifparteien, Notdienstvereinbarungen, Ankündigungsfristen ohne Schlichtungszwang.",
                "Begründetes Urteil unter Gewichtung der Kriterien.",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete, begründete Einschätzung mit Fachwissen zu Koalitionsfreiheit, Arbeitskampfrecht und Tarifautonomie; Materialbezug auf [5] und [6] erwartet.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einigen zutreffenden Argumenten und Materialbezug formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, verfassungsrechtlich und fachlich fundiert (Art. 9 Abs. 3 GG, Richterrecht, Kräftegleichgewicht) und schlüssig begründet ist.",
        },
    },
    {
        "id": "q2-4-iii4",
        "afb": "III",
        "operator": "diskutieren",
        "lk": True,
        "text": "Diskutieren Sie, ob der Staat der Entwicklung der Einkommens- und Vermögensverteilung in Deutschland stärker entgegenwirken sollte.",
        "material": [],
        "loesung": {
            "punkte": [
                "Sachgrundlage: Gini verfügbare Äquivalenzeinkommen rund 0,30 (EU-SILC 2025: 0,301, nahe EU-Durchschnitt), deutlich ungleichere Markteinkommen; Gini Nettovermögen 0,724 (Bundesbank 2023), reichste 10 % besitzen gut die Hälfte; Armutsgefährdungsquote 16,1 % (2025).",
                "Für stärkeres Gegensteuern: Chancengleichheit (Vererbung von Vermögen, Herkunftsabhängigkeit der Bildung), Bedarfsgerechtigkeit (Armutsrisiko von Arbeitslosen und Alleinerziehenden), sozialer Zusammenhalt und Demokratievertrauen, Kaufkraftargument, Stärkung von Tarifbindung und Mindestlohn (Primärverteilung), Erbschaft- und Vermögensbesteuerung.",
                "Gegen stärkeres Gegensteuern: Leistungsgerechtigkeit und Leistungsanreize, bereits starke Umverteilung durch Steuern und Transfers (Einkommensungleichheit im EU-Mittelfeld), Kapitalflucht und Belastung von Betriebsvermögen/Mittelstand, verfassungsrechtliche und administrative Probleme einer Vermögensteuer, Eigentumsschutz (Art. 14 GG).",
                "Differenzierung nach Instrumenten (Primärverteilung über Tarifpolitik vs. Sekundärverteilung über Steuern/Transfers) und nach Einkommen vs. Vermögen.",
                "Begründete Bewertung am Ende.",
            ],
            "hinweis": "Diskutieren (LK): Argumentation entwickeln, die zu einer begründeten Bewertung führt; Bezug zu konkurrierenden Gerechtigkeitsbegriffen und zu empirischen Kennzahlen (Gini, Vermögenskonzentration) wird erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Diskussion ansatzweise strukturiert ist, auf Verteilungsdaten Bezug nimmt und in eine ansatzweise nachvollziehbare Bewertung mündet.",
            "gut": "die Diskussion strukturiert, empirisch fundiert und theoriegeleitet (Gerechtigkeitsbegriffe, Primär-/Sekundärverteilung) ist und in eine schlüssig begründete Bewertung mündet.",
        },
    },
]
