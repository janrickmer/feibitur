# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q3.4 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q3.4, insbesondere Dimensionen und Folgen der Entgrenzung nationalstaatlicher Demokratien (Legislative, Exekutive, Judikative), Demokratie jenseits des Nationalstaates, globales Regieren zwischen Institutionalisierung (UN) und Informalisierung (G7/G20) sowie Spannungsverhältnis von wirtschaftlicher und politischer Liberalisierung; erhöhtes Niveau: Universalität der Menschenrechte und internationale Strafgerichtsbarkeit. Kein Schwerpunkt im Abiturerlass 2027."

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Die Demokratie hat ihre Adresse verloren“ (2026)",
        "absaetze": [
            "Ende Juni 2025 verständigten sich die G7-Staaten unter kanadischer Präsidentschaft darauf, Konzerne mit Sitz in den USA von zentralen Regeln der globalen Mindeststeuer weitgehend auszunehmen. Im Januar 2026 setzte das Inclusive Framework der OECD, in dem weit über hundert Staaten zusammenarbeiten, diese Linie in ein Regelpaket um. Für die nationalen Parlamente bleibt bei solchen Absprachen meist nur die Rolle des Notars: Sie können das Ergebnis umsetzen oder das ganze Paket gefährden. Gestalten können sie kaum.",
            "Das ist kein Einzelfall. Ein erheblicher Teil der Gesetze, die der Bundestag beschließt, setzt Vorgaben der Europäischen Union um. Handelsabkommen werden über Jahre zwischen Regierungen und Kommission verhandelt und den Parlamenten am Ende zur Ratifikation vorgelegt – Ja oder Nein, Änderungen sind nicht vorgesehen. Wer gewählt wird, entscheidet immer weniger; wer entscheidet, wird immer seltener gewählt.",
            "Auch die Rechtsprechung wirkt längst über Grenzen hinweg. Der Europäische Gerichtshof für Menschenrechte stärkt Bürgerinnen und Bürger gegenüber ihren eigenen Staaten – das ist ein Gewinn. Doch daneben gibt es Schiedsgerichte, vor denen ausländische Investoren Staaten verklagen können. Als der Energiekonzern Vattenfall Deutschland wegen des Atomausstiegs vor ein Schiedsgericht in Washington zog, stand ein demokratisch beschlossenes Gesetz plötzlich vor einem Gremium, das keiner Wählerschaft verantwortlich ist. 2021 einigten sich Bund und Energiekonzerne auf Entschädigungen von insgesamt rund 2,4 Milliarden Euro; im Gegenzug wurde das Verfahren beendet.",
            "Der Ökonom Dani Rodrik hat das Dilemma auf den Punkt gebracht: Tiefe wirtschaftliche Integration, nationale Souveränität und Demokratie lassen sich nicht gleichzeitig vollständig verwirklichen. In den vergangenen Jahrzehnten wurde im Zweifel die Demokratie zurückgestellt. Dass populistische Bewegungen mit Parolen wie „Take back control“ Erfolg haben, ist auch eine Reaktion auf dieses Gefühl des Kontrollverlusts.",
            "Die Antwort kann trotzdem nicht der Rückzug in die Nation sein. Klimawandel, Steueroasen, Pandemien und Cyberkriminalität lassen sich nicht im nationalen Alleingang bewältigen. Die Europäische Union zeigt, dass Demokratie jenseits des Staates möglich ist: mit einem direkt gewählten Parlament, mit Bürgerrechten, die in 27 Staaten gelten, und mit Gerichten, die diese Rechte schützen.",
            "Zwei Schritte wären sofort möglich. Erstens sollte die Bundesregierung vor jedem G7- oder G20-Gipfel ihre Verhandlungsziele im Bundestag vorstellen und darüber abstimmen lassen; Zusagen ohne parlamentarisches Mandat sollte es nicht mehr geben. Zweitens sollte sich Deutschland für eine Parlamentarische Versammlung bei den Vereinten Nationen einsetzen – als Keimzelle eines Weltparlaments. Wer Weltpolitik demokratisieren will, muss irgendwo anfangen.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Politikwissenschaftlerin (2026). Reale Hintergründe: G7-Erklärung zur globalen Mindeststeuer (Juni 2025); „Side-by-Side“-Paket des OECD/G20 Inclusive Framework (Januar 2026); Einigung zwischen Bund und Energiekonzernen zum Atomausstieg (2021).",
    },
    {
        "id": "m2",
        "titel": "M2: Globales Regieren im Vergleich – Vereinte Nationen, G7 und G20",
        "typ": "tabelle",
        "kopf": ["Merkmal", "Vereinte Nationen (UN)", "G7", "G20"],
        "zeilen": [
            ["Gründung", "1945 (UN-Charta, in Kraft seit 24.10.1945)", "1975 als Weltwirtschaftsgipfel (zunächst sechs Staaten), seit 1976 G7", "1999 als Treffen der Finanzminister und Notenbankchefs; Gipfel der Staats- und Regierungschefs seit 2008"],
            ["Mitglieder", "193 Staaten", "Deutschland, Frankreich, Italien, Japan, Kanada, USA, Vereinigtes Königreich; die EU nimmt teil", "19 Staaten (u. a. die G7-Staaten, China, Indien, Brasilien, Russland, Saudi-Arabien, Südafrika) sowie die EU und (seit 2023) die Afrikanische Union"],
            ["Rechtsgrundlage", "völkerrechtlicher Vertrag (UN-Charta)", "keine – informelles Forum", "keine – informelles Forum"],
            ["Organisation", "Generalversammlung, Sicherheitsrat, Sekretariat, Internationaler Gerichtshof u. a.; Sonderorganisationen (z. B. WHO)", "kein ständiges Sekretariat; jährlich wechselnde Präsidentschaft", "kein ständiges Sekretariat; jährlich wechselnde Präsidentschaft"],
            ["Entscheidungen", "Generalversammlung: ein Staat – eine Stimme, meist Empfehlungen; Sicherheitsrat: bindende Beschlüsse (Art. 25), Veto der fünf ständigen Mitglieder", "Konsens; politische Erklärungen ohne Rechtsbindung", "Konsens; politische Erklärungen ohne Rechtsbindung"],
            ["Aktuelle Entwicklungen", "regulärer Haushalt 2026 auf 3,45 Mrd. US-$ gekürzt, rund 19 % weniger Stellen (Reforminitiative „UN80“); USA kündigen im Januar 2026 den Rückzug aus 31 UN-Einrichtungen an", "Gipfel in Évian (Juni 2026): u. a. weitere Unterstützung der Ukraine, Allianz für kritische Rohstoffe", "Präsidentschaft 2026: USA; Gipfel in Miami (Dezember 2026) ohne Einladung an Südafrika"],
        ],
        "quelle": "Zusammenstellung für Feibitur nach Angaben der Vereinten Nationen (UN-Charta; Haushaltsbeschluss der Generalversammlung vom 30.12.2025), des Weißen Hauses (Memorandum vom 7.1.2026), der G7-Präsidentschaft Frankreich 2026 und der G20-Präsidentschaft USA 2026. Stand: Oktober 2026.",
    },
    {
        "id": "m3",
        "titel": "M3: Rede „Handel ohne Wandel?“ (2026)",
        "absaetze": [
            "Herr Präsident, liebe Kolleginnen und Kollegen, als China im Dezember 2001 der Welthandelsorganisation beitrat, waren sich viele im Westen sicher: Wer Handel treibt, öffnet sich. Mit dem Wohlstand würden eine Mittelschicht, freie Medien und am Ende auch freie Wahlen kommen. Wandel durch Handel – so lautete das Versprechen.",
            "Ein Teil dieses Versprechens hat sich erfüllt. Hunderte Millionen Menschen in China und anderen Schwellenländern sind der extremen Armut entkommen, auch dank offener Märkte. Doch der politische Wandel blieb aus. Das UN-Menschenrechtsbüro sprach 2022 von schweren Menschenrechtsverletzungen in der Region Xinjiang, die möglicherweise Verbrechen gegen die Menschlichkeit darstellen; die chinesische Regierung weist das zurück. Und Russland, mit dem Europa jahrzehntelang Gas gegen Geld tauschte, hat 2022 die Ukraine überfallen.",
            "Wir erleben keinen Siegeszug der Freiheit, sondern ihren Rückzug. Freedom House zählt für 2025 das 20. Jahr in Folge, in dem die Freiheit weltweit abgenommen hat. Nur noch rund ein Fünftel der Menschheit lebt in Ländern, die als frei gelten. Wirtschaftliche Öffnung und politische Freiheit gehen offensichtlich nicht automatisch Hand in Hand.",
            "Wenn wir das ansprechen, hören wir aus Peking und anderen Hauptstädten stets ähnliche Antworten: Menschenrechte seien eine innere Angelegenheit. Jede Kultur habe ihr eigenes Verständnis von Freiheit; Stabilität, Gemeinschaft und das Recht auf Entwicklung hätten Vorrang vor individuellen Freiheiten. Und überhaupt: Wer selbst mit doppelten Standards messe, solle nicht belehren. Den letzten Punkt sollten wir ernst nehmen. Aber die Allgemeine Erklärung der Menschenrechte wurde 1948 nicht für Europa, sondern für alle Menschen verkündet.",
            "Gleichzeitig müssen wir vor der eigenen Tür kehren. Investoren können ihre Rechte vor internationalen Schiedsgerichten einklagen, Arbeiterinnen in den Zulieferbetrieben unserer Konzerne ihre Rechte dagegen kaum. Bei der europäischen Lieferkettenrichtlinie haben sich Parlament und Rat im Dezember 2025 darauf verständigt, sie stark abzuschwächen: Sie soll nur noch für sehr große Unternehmen gelten und erst ab 2029 angewendet werden. Immerhin dürfen ab Dezember 2027 Produkte aus Zwangsarbeit in der EU nicht mehr verkauft werden.",
            "Deshalb fordere ich: Jedes neue Handelsabkommen der EU muss verbindliche Menschenrechts- und Arbeitsrechtsklauseln enthalten, deren Verletzung zur Aussetzung von Zollvorteilen führt – überprüft von einem unabhängigen Gremium, in dem auch Gewerkschaften und Nichtregierungsorganisationen sitzen. Handel ist kein Selbstzweck. Er muss der Freiheit dienen, nicht nur dem Gewinn.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasste Rede eines fiktiven Mitglieds des Europäischen Parlaments (2026). Reale Fakten: WTO-Beitritt Chinas (11.12.2001); Bewertung des UN-Hochkommissariats für Menschenrechte zu Xinjiang (31.8.2022); Freedom House, Freedom in the World 2026; vorläufige Einigung zum „Omnibus“-Paket (Dezember 2025); Verordnung (EU) 2024/3015.",
    },
]

AUFGABEN = [
    {
        "id": "q3-4-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung: Kommentar „Die Demokratie hat ihre Adresse verloren“ einer (fiktiven) Politikwissenschaftlerin aus dem Jahr 2026; Thema: Entgrenzung nationalstaatlicher Demokratie und Vorschläge zu ihrer Demokratisierung.",
            "punkte": [
                "Am Beispiel der globalen Mindeststeuer (G7-Absprache 2025, OECD-Paket 2026) zeige sich, dass Parlamente bei internationalen Absprachen nur noch zustimmen oder ablehnen, aber kaum gestalten könnten [1].",
                "Ein großer Teil der Gesetze setze EU-Vorgaben um; Handelsabkommen würden von Exekutiven verhandelt und Parlamenten nur zur Ratifikation vorgelegt; Gewählte entschieden immer weniger [2].",
                "Grenzüberschreitende Gerichte wirkten ambivalent: Der EGMR stärke Bürgerrechte, Investor-Staat-Schiedsgerichte (Beispiel Vattenfall, Einigung 2021 über rund 2,4 Mrd. Euro) stellten demokratische Gesetze vor nicht verantwortliche Gremien [3].",
                "Nach Rodriks Trilemma sei die Demokratie zugunsten wirtschaftlicher Integration zurückgestellt worden; der Erfolg populistischer Parolen sei auch eine Reaktion auf Kontrollverlust [4].",
                "Renationalisierung sei keine Lösung, weil globale Probleme Kooperation erforderten; die EU beweise, dass Demokratie jenseits des Staates möglich sei [5].",
                "Forderungen: Mandat des Bundestages vor G7/G20-Gipfeln und deutscher Einsatz für eine Parlamentarische Versammlung bei den UN als Keimzelle eines Weltparlaments [6].",
            ],
            "hinweis": "Zusammenfassen: Einleitungssatz, strukturierte und komprimierte Wiedergabe in eigenen Worten, indirekte Rede, Fachsprache, keine Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen des Kommentars weitgehend vollständig, strukturiert, komprimiert und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q3-4-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie anhand von M2 Merkmale und aktuelle Entwicklungen der Vereinten Nationen, der G7 und der G20.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: tabellarische Zusammenstellung zu UN, G7 und G20 nach Gründung, Mitgliedern, Rechtsgrundlage, Organisation, Entscheidungsverfahren und aktuellen Entwicklungen (Stand Oktober 2026).",
            "punkte": [
                "UN: 1945 gegründet, 193 Mitgliedstaaten, völkerrechtlicher Vertrag (UN-Charta), feste Organe und Sonderorganisationen; Generalversammlung nach dem Prinzip „ein Staat – eine Stimme“ mit Empfehlungen, Sicherheitsrat mit bindenden Beschlüssen und Vetorecht der fünf ständigen Mitglieder.",
                "G7: 1975 entstanden, sieben Industriestaaten plus EU, keine Rechtsgrundlage und kein Sekretariat, wechselnde Präsidentschaft, Konsensentscheidungen ohne Rechtsbindung.",
                "G20: 1999 auf Ebene der Finanzminister gegründet, seit 2008 Gipfel; 19 Staaten einschließlich großer Schwellenländer sowie EU und Afrikanische Union; ebenfalls informell und konsensbasiert.",
                "Aktuelle Entwicklungen: Haushaltskürzungen und Stellenabbau bei den UN (UN80), Rückzug der USA aus 31 UN-Einrichtungen; G7-Gipfel in Évian mit Beschlüssen zur Ukraine und zu kritischen Rohstoffen; US-Präsidentschaft der G20 ohne Einladung Südafrikas zum Gipfel in Miami.",
                "Strukturierte Darstellung nach Kriterien (z. B. Mitgliedschaft, Verbindlichkeit, Organisation) statt bloßer Aufzählung der Zellen.",
            ],
            "hinweis": "Beschreiben: Informationen aus M2 strukturiert, fachsprachlich und in eigenen Worten darlegen; noch kein Vergleich im Sinne einer Bewertung und keine Erklärung.",
        },
        "bewertung": {
            "ausreichend": "zentrale Merkmale der drei Foren ansatzweise korrekt und mit Bezug zu M2 beschrieben werden.",
            "gut": "Merkmale und aktuelle Entwicklungen aller drei Foren strukturiert, präzise und fachsprachlich beschrieben werden.",
        },
    },
    {
        "id": "q3-4-i3",
        "afb": "I",
        "operator": "wiedergeben",
        "text": "Geben Sie die Position des Redners zum Verhältnis von Handel und Menschenrechten wieder. (M3)",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitung: Rede „Handel ohne Wandel?“ eines (fiktiven) Mitglieds des Europäischen Parlaments (2026) zum Verhältnis von Handelspolitik und Menschenrechten.",
            "punkte": [
                "Mit Chinas WTO-Beitritt 2001 sei die Erwartung verbunden gewesen, wirtschaftliche Öffnung führe zu Demokratie („Wandel durch Handel“) [1].",
                "Die Armutsminderung sei gelungen, der politische Wandel aber ausgeblieben (Xinjiang-Bewertung des UN-Menschenrechtsbüros 2022, chinesische Zurückweisung; Russlands Angriff auf die Ukraine trotz Energiehandel) [2].",
                "Weltweit gehe die Freiheit laut Freedom House seit 20 Jahren zurück; wirtschaftliche und politische Liberalisierung gingen nicht automatisch zusammen [3].",
                "Kulturrelativistische Gegenargumente autoritärer Regierungen (innere Angelegenheit, eigenes Freiheitsverständnis, Vorrang von Stabilität und Entwicklung, Vorwurf der Doppelstandards) weist der Redner unter Verweis auf den universellen Anspruch der AEMR zurück; den Vorwurf der Doppelstandards nimmt er teilweise ernst [4].",
                "Selbstkritik: Investorenrechte seien besser geschützt als Arbeitnehmerrechte; Abschwächung der EU-Lieferkettenrichtlinie; positiv: Verbot von Produkten aus Zwangsarbeit ab Dezember 2027 [5].",
                "Forderung: verbindliche, sanktionsbewehrte Menschenrechts- und Arbeitsrechtsklauseln in allen neuen EU-Handelsabkommen mit unabhängiger Überprüfung unter Beteiligung von Gewerkschaften und NGOs [6].",
            ],
            "hinweis": "Wiedergeben: ausgehend von einem Einleitungssatz die Position in eigenen Worten und mit Fachsprache darstellen (indirekte Rede), ohne Bewertung.",
        },
        "bewertung": {
            "ausreichend": "die Position des Redners im Ansatz korrekt und mit Einleitung wiedergegeben wird.",
            "gut": "die Position des Redners strukturiert, vollständig, fachsprachlich und in eigenen Worten unter Verwendung der indirekten Rede wiedergegeben wird.",
        },
    },
    {
        "id": "q3-4-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 die Entgrenzung nationalstaatlicher Demokratie in den Dimensionen Legislative, Exekutive und Judikative.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Grundgedanke: Kongruenz von Entscheidenden und Betroffenen als Voraussetzung nationaler Demokratie; Denationalisierung/Globalisierung löst sie auf (Kongruenzproblem, „postnationale Konstellation“).",
                "Legislative: Rechtsetzung verlagert sich auf die EU (Richtlinien, Verordnungen) und in internationale Verträge; Parlamente werden zu „Ratifikationsparlamenten“ (M1 [1], [2]); Beispiel Mindeststeuer (OECD/G20-Einigung 2021, EU-Richtlinie, nationales Gesetz; Ausnahme für US-Konzerne 2025/26); Gegengewichte: Art. 23 GG, Subsidiaritätsrüge, Europäisches Parlament.",
                "Exekutive: Regierungen handeln in Gipfeln und Clubs (G7/G20), im Rat der EU, in Expertennetzwerken; Informationsvorsprung und Vertraulichkeit; Ergebnisse als „Sachzwang“ [1], [2].",
                "Judikative: EGMR stärkt Individualrechte (positiv) [3]; Investor-Staat-Schiedsverfahren (Vattenfall) begrenzen demokratischen Gestaltungsspielraum; weitere Beispiele: EuGH und Konflikt mit dem BVerfG (PSPP-Urteil 2020), WTO-Streitschlichtung (Berufungsinstanz seit 2019 blockiert), IStGH.",
                "Folgen: Input-Legitimationsprobleme, Gefühl des Kontrollverlusts, Populismus und Renationalisierungsforderungen (Rodrik-Trilemma, M1 [4]); zugleich Output-Gewinne durch gemeinsame Problemlösung [5].",
            ],
            "hinweis": "Erläutern: alle drei Dimensionen mit Beispielen und zusätzlichen Informationen veranschaulichen; Materialbezüge zu M1 und darüber hinausgehendes Fachwissen erwartet.",
        },
        "bewertung": {
            "ausreichend": "die Entgrenzung in mindestens zwei Dimensionen ansatzweise mit Beispielen und Bezug zu M1 erläutert wird.",
            "gut": "die Entgrenzung in allen drei Dimensionen differenziert, mit passenden Beispielen aus M1 und Fachwissen sowie mit Blick auf demokratische Folgen erläutert wird.",
        },
    },
    {
        "id": "q3-4-ii2",
        "afb": "II",
        "operator": "vergleichen",
        "text": "Vergleichen Sie die Vereinten Nationen mit den Clubs G7 und G20 als Formen globalen Regierens zwischen Institutionalisierung und Informalisierung. (M2)",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Vergleichskriterien benennen, z. B. Mitgliedschaft/Inklusivität, Rechtsgrundlage, Organisation, Verbindlichkeit der Entscheidungen, Handlungsfähigkeit, Legitimität.",
                "Gemeinsamkeiten: Foren zwischenstaatlicher Kooperation zur Bearbeitung globaler Probleme; Entscheidungen hängen vom Willen der Staaten, besonders der Großmächte, ab (Veto im Sicherheitsrat bzw. Konsens in G7/G20); USA prägen alle drei stark (Rückzug aus UN-Einrichtungen, G20-Präsidentschaft 2026).",
                "Unterschiede: UN universell (193 Staaten) und vertraglich institutionalisiert mit festen Organen und teils bindenden Beschlüssen; G7/G20 exklusiv, ohne Vertrag und Sekretariat, nur politische Erklärungen (Informalisierung).",
                "G7 und G20 untereinander: G7 kleine, relativ homogene Gruppe westlicher Industriedemokratien; G20 breiter, bezieht Schwellenländer, EU und Afrikanische Union ein, ist heterogener und damit konfliktträchtiger (Ausschluss Südafrikas 2026).",
                "Folgerung: Institutionalisierung bringt Legitimität und Verbindlichkeit, aber Schwerfälligkeit (Haushaltskrise, Blockaden); Informalisierung bringt Tempo und Flexibilität, aber Legitimations- und Verbindlichkeitsdefizite.",
            ],
            "hinweis": "Vergleichen: Gemeinsamkeiten UND Unterschiede kriteriengeleitet und begründet darlegen; ein bloßes Nacheinander der Spalten aus M2 genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "UN und Clubs ansatzweise kriteriengeleitet verglichen und einige Gemeinsamkeiten und Unterschiede benannt werden.",
            "gut": "der Vergleich kriteriengeleitet, differenziert und mit den Fachbegriffen Institutionalisierung und Informalisierung erfolgt und zu einem begründeten Fazit führt.",
        },
    },
    {
        "id": "q3-4-ii3",
        "afb": "II",
        "operator": "erklären",
        "text": "Erklären Sie ausgehend von M3 das Spannungsverhältnis von wirtschaftlicher und politischer Liberalisierung im Globalisierungsprozess.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Begriffe: wirtschaftliche Liberalisierung (Abbau von Handels- und Kapitalschranken, Schutz von Eigentum und Investitionen) vs. politische Liberalisierung (Demokratie, Menschenrechte, Rechtsstaat).",
                "Erwartung der Modernisierungstheorie (Lipset): Wohlstand und Mittelschicht führen zu Demokratie („Wandel durch Handel“, M3 [1]); Belege dafür: Südkorea, Taiwan.",
                "Empirischer Befund: Armutsminderung ohne Demokratisierung in China, Rückgang der Freiheit weltweit (Freedom House) [2], [3] – autoritärer Kapitalismus.",
                "Gründe der Spannung: asymmetrische institutionelle Garantien (Investorenrechte durch Schiedsgerichte und WTO durchsetzbar, Arbeits- und Menschenrechte kaum, M3 [5]); Legitimation autoritärer Regime durch Wachstum; Standortwettbewerb begrenzt demokratische Gestaltungsspielräume (Rodrik-Trilemma); Interdependenz als Druckmittel (Russland/Gas, M3 [2]); Globalisierungsverlierer und Populismus in Demokratien.",
                "Politische Steuerungsversuche: Menschenrechtsklauseln, Lieferkettensorgfaltspflichten (abgeschwächt), Verbot von Produkten aus Zwangsarbeit ab Dezember 2027 [5], [6].",
            ],
            "hinweis": "Erklären: Spannungsverhältnis auf Theorien (Modernisierungstheorie, Trilemma) und Funktionszusammenhänge zurückführen; Materialbezüge erforderlich.",
        },
        "bewertung": {
            "ausreichend": "das Spannungsverhältnis ansatzweise erklärt und mit Beispielen aus M3 belegt wird.",
            "gut": "das Spannungsverhältnis differenziert auf theoretische Annahmen und Funktionszusammenhänge zurückgeführt und durchgängig mit M3 und Fachwissen belegt wird.",
        },
    },
    {
        "id": "q3-4-ii4",
        "afb": "II",
        "operator": "erläutern",
        "lk": True,
        "text": "Erläutern Sie ausgehend von M3 (Absatz 4) die Kontroverse zwischen einem universalistischen und einem kulturrelativistischen Verständnis der Menschenrechte.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Universalismus: Menschenrechte gelten für alle Menschen aufgrund ihrer Würde (AEMR 1948, Art. 1; Wiener Erklärung 1993: universell, unteilbar, interdependent); Mitwirkung nichtwestlicher Autoren an der AEMR; Schutz Einzelner und von Minderheiten vor Staat und Mehrheit.",
                "Kulturrelativismus: Werte kulturell gebunden; Vorrang von Gemeinschaft, Stabilität, Recht auf Entwicklung (Debatte um „asiatische Werte“, Bangkok-Erklärung 1993; Kairoer Erklärung 1990 mit Scharia-Vorbehalt); Menschenrechte als innere Angelegenheit und Nichteinmischung (M3 [4]).",
                "Machtpolitische Dimension: Kulturrelativistische Argumente dienen autoritären Regierungen auch zur Abwehr von Kritik (Xinjiang, M3 [2]); umgekehrt Vorwurf westlicher Doppelstandards [4].",
                "Vermittelnde Positionen: nicht verhandelbarer universeller Kern (Folterverbot, Sklavereiverbot), Spielräume bei der Umsetzung (Beurteilungsspielraum des EGMR); Doppelstandards widerlegen nicht den Geltungsanspruch, sondern fordern konsequente Anwendung.",
                "Bezug zur Globalisierung: Konflikt um Menschenrechtsklauseln in Handelsabkommen und Lieferketten (M3 [5], [6]).",
            ],
            "hinweis": "Erläutern auf erhöhtem Niveau: beide Positionen mit Beispielen und Dokumenten veranschaulichen und die Kontroverse strukturiert entfalten; Bezug zu M3 [4] erforderlich.",
        },
        "bewertung": {
            "ausreichend": "beide Positionen ansatzweise zutreffend mit Beispielen und Bezug zu M3 erläutert werden.",
            "gut": "die Kontroverse differenziert, mit Bezug auf zentrale Dokumente (AEMR, Wiener Erklärung, Bangkok- und Kairoer Erklärung), auf M3 und auf die machtpolitische Dimension erläutert wird.",
        },
    },
    {
        "id": "q3-4-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie die Forderungen der Autorin, Zusagen der Bundesregierung bei G7- und G20-Gipfeln an ein vorheriges Mandat des Bundestages zu binden und eine Parlamentarische Versammlung bei den Vereinten Nationen zu schaffen. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Pro Parlamentsmandat: Stärkung der Input-Legitimation und der Kontrollfunktion des Parlaments; mehr Transparenz und Öffentlichkeit; Gegengewicht zur Exekutivlastigkeit (M1 [1], [2]); Vorbilder (Mitwirkungsrechte nach Art. 23 GG in EU-Angelegenheiten, Parlamentsvorbehalt bei Auslandseinsätzen).",
                "Contra Parlamentsmandat: Einschränkung der Verhandlungsflexibilität der Regierung; Clubs leben von vertraulichen Kompromissen; andere Staaten binden ihre Regierungen nicht; Gefahr von Blockaden und Zeitverlust in Krisen; ohnehin politische Verantwortung der Regierung gegenüber dem Parlament.",
                "Pro UN-Parlamentsversammlung: Beitrag zu globaler Input-Legitimation, Stimme der Bürger statt nur der Regierungen, Keimzelle kosmopolitischer Demokratie [6]; Unterstützung durch Teile der Zivilgesellschaft.",
                "Contra UN-Parlamentsversammlung: kein globales „Volk“ und keine gemeinsame Öffentlichkeit; Problem der Sitzverteilung (Bevölkerungsgröße vs. Staatengleichheit); autoritäre Staaten würden keine frei gewählten Abgeordneten entsenden; ohne Kompetenzen bloß symbolisch; Charta-Änderung kaum durchsetzbar.",
                "Abwägung nach Kriterien (Legitimität, Effektivität, Realisierbarkeit) und begründetes eigenes Urteil; differenzierte Ergebnisse (z. B. Informationspflicht statt Zustimmungsvorbehalt) sind möglich.",
            ],
            "hinweis": "Erörtern: beide Forderungen [6] unter Abwägen von Pro- und Contra-Argumenten prüfen und zu einem eigenen, begründeten Urteil gelangen; Fachbegriffe wie Input-/Output-Legitimation und kosmopolitische Demokratie stärken die Leistung.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist, Pro- und Contra-Argumente enthält und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, kriteriengeleitet und weitgehend kohärent ist, beide Forderungen fachlich fundiert prüft und in ein schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q3-4-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie, ob informelle Clubs wie G7 und G20 die Vereinten Nationen als Forum globalen Regierens sinnvoll ergänzen. (M2)",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien benennen, z. B. Handlungsfähigkeit/Effektivität, Legitimität/Inklusivität, Verbindlichkeit, Folgen für die multilaterale Ordnung.",
                "Für eine sinnvolle Ergänzung: Tempo und Flexibilität (Finanzkrise 2008/09), Vorreiterrolle mit späterer Ausweitung (Mindeststeuer), G20 bindet Schwellenländer und Afrikanische Union ein; UN sind durch Veto, Haushaltskrise und Rückzug der USA geschwächt (M2).",
                "Gegen eine sinnvolle Ergänzung: fehlende Input-Legitimation (die Mehrheit der Staaten bleibt außen vor), keine Rechtsbindung und Kontrolle, Gefahr der Verdrängung universeller Institutionen und der Blockbildung (G7 vs. BRICS), Abhängigkeit von der Präsidentschaft (Ausschluss Südafrikas 2026).",
                "Differenzierung: Ergänzung gelingt dort, wo Clubs Vorarbeiten leisten, die in universellen Institutionen beschlossen werden; problematisch, wo sie diese ersetzen.",
                "Begründetes Urteil auf Grundlage der Kriterien und der Daten aus M2.",
            ],
            "hinweis": "Beurteilen: kriteriengeleitete, begründete Einschätzung unter Verwendung von Fachwissen und Materialbezügen; ein Urteil ohne Kriterien genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einzelnen Belegen aus M2 und Fachwissen formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, fachlich fundiert und mit gezielten Bezügen zu M2 schlüssig begründet wird.",
        },
    },
    {
        "id": "q3-4-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Entwerfen Sie eine Erwiderung auf die Rede (M3) aus der Sicht einer Abgeordneten, die verbindliche, sanktionsbewehrte Menschenrechtsklauseln in allen EU-Handelsabkommen für den falschen Weg hält.",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Produktorientierte Aufgabe: Erwartet wird eine adressatengerechte Rede (Anrede, Bezug auf den Vorredner, Argumentationsgang, Schluss mit eigenem Vorschlag), die die Gegenposition schlüssig und sachlich vertritt.",
            "punkte": [
                "Anknüpfung an die Rede: Anerkennung der Ziele (Menschenrechte, Kritik an Zwangsarbeit), aber Widerspruch zum Instrument [6].",
                "Wirtschaftliche Argumente: Wettbewerbsnachteile und Bürokratiekosten für europäische Unternehmen; Partnerstaaten könnten auf Abkommen mit weniger anspruchsvollen Partnern ausweichen (z. B. China), wodurch Europa Einfluss verliert; Handel bleibt Grundlage für Wohlstand und Armutsminderung [2].",
                "Entwicklungspolitische Argumente: Zollsanktionen treffen oft Arbeiterinnen und Arbeiter in ärmeren Ländern statt Regierungen; Vorwurf des Protektionismus und Paternalismus aus dem Globalen Süden.",
                "Politische Argumente: Handel als Kanal für Dialog und Einfluss; Gefahr von Doppelstandards (M3 [4]); Wirksamkeit von Sanktionsklauseln empirisch umstritten.",
                "Alternativvorschläge: gezielte Instrumente wie das Zwangsarbeitsverbot ab 2027 [5], Kooperation und Kapazitätsaufbau, Anreize (Zollpräferenzen) statt Sanktionen, multilaterale Lösungen über ILO und WTO.",
                "Sprachlich-formale Gestaltung: rhetorische Mittel, klare Struktur, sachlicher Ton.",
            ],
            "hinweis": "Gestalten/entwerfen: kreative, produktorientierte Umsetzung; bewertet werden Schlüssigkeit, fachliche Fundierung, Bezug auf M3 und Textsortenadäquatheit. Die vertretene Position muss nicht der eigenen Meinung entsprechen.",
        },
        "bewertung": {
            "ausreichend": "eine erkennbare Rede mit einigen schlüssigen Gegenargumenten und Bezug zu M3 vorliegt.",
            "gut": "die Rede adressatengerecht und strukturiert ist, fachlich fundierte wirtschafts-, entwicklungs- und menschenrechtspolitische Argumente entfaltet, sich präzise auf M3 bezieht und einen eigenen Alternativvorschlag entwickelt.",
        },
    },
    {
        "id": "q3-4-iii4",
        "afb": "III",
        "operator": "erörtern",
        "lk": True,
        "text": "Erörtern Sie Chancen und Grenzen einer internationalen Strafgerichtsbarkeit am Beispiel des Internationalen Strafgerichtshofs.",
        "material": [],
        "loesung": {
            "punkte": [
                "Grundlagen: Römisches Statut (1998, in Kraft 2002), 125 Vertragsstaaten, vier Kernverbrechen, Komplementarität, Zuständigkeit über Territorium, Staatsangehörigkeit oder Überweisung durch den Sicherheitsrat; keine Immunität für Amtsträger.",
                "Chancen: Ende der Straflosigkeit, individuelle Verantwortung auch von Staatschefs, Abschreckung, Opferbeteiligung und Wiedergutmachung, gerichtsfeste Dokumentation; Beispiele: Verurteilung eines Dschandschawid-Führers (Darfur) 2025, Überstellung Dutertes 2025 und Prozessbeginn im November 2026, Haftbefehle gegen Putin (2023) und Netanjahu/Gallant (2024); Ergänzung durch nationale Gerichte (Weltrechtsprinzip, OLG Koblenz 2022).",
                "Grenzen: keine eigene Polizei, Abhängigkeit von Kooperation (Putin in der Mongolei 2024, Netanjahu in Ungarn 2025 ohne Festnahme); Großmächte nicht Vertragsstaaten (USA, Russland, China, Indien), Sicherheitsrat mit Veto; Vorwurf der Selektivität und Afrika-Fokus; Austrittserklärungen 2026 (Burkina Faso, Mali, Niger, Venezuela, Tschad) vs. Rücknahme des ungarischen Austritts; US-Sanktionen bis hin zur Präsidentin des Gerichts (August 2026); Absetzung des Chefanklägers Khan (Juli 2026) als Vertrauenskrise; lange, teure Verfahren.",
                "Grundsatzkonflikt Frieden vs. Gerechtigkeit (Haftbefehle und Verhandlungen) sowie Souveränität vs. universelle Verantwortung.",
                "Abwägung und eigenes begründetes Urteil, z. B.: unverzichtbar als Norm und Instrument, aber nur so stark wie der politische Wille der Staaten; Reformvorschläge (mehr Vertragsstaaten, Kooperationspflichten, Schutz vor Sanktionen).",
            ],
            "hinweis": "Erörtern auf erhöhtem Niveau: Pro und Contra abwägen, aktuelle Beispiele korrekt einordnen und zu einem eigenen, begründeten Urteil kommen. Exakte Daten sind nicht zwingend, Fakten müssen aber zutreffen.",
        },
        "bewertung": {
            "ausreichend": "Chancen und Grenzen ansatzweise mit zutreffenden Beispielen abgewogen werden und ein nachvollziehbares Urteil vorliegt.",
            "gut": "die Erörterung strukturiert, fachlich fundiert (Römisches Statut, Komplementarität, aktuelle Fälle und Konflikte) und abwägend ist und in ein schlüssig begründetes Urteil mündet.",
        },
    },
]
