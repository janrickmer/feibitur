# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q1.2 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = 'Q1.2, insbesondere Funktionen von Parteien und Populismus (Erlass 2027), alternative Beteiligungsformen, Extremismus als Gefährdung der Demokratie.'

MATERIALIEN = [
    {
        'titel': 'M1: Rede des Vorsitzenden der (fiktiven) Partei „Stimme des Volkes“ auf einer Kundgebung (2026)',
        'absaetze': [
            'Liebe Freunde, liebe Bürgerinnen und Bürger! Schaut euch um: Hier stehen die Menschen, die dieses Land jeden Morgen am Laufen halten. Die Krankenpflegerin, der Handwerker, die Rentnerin, die jeden Euro zweimal umdrehen muss. Und was macht die Politik in Berlin? Sie redet über euch, aber sie redet nicht mit euch!',
            'Die sogenannten etablierten Parteien haben sich den Staat zur Beute gemacht. Sie verteilen Posten unter sich, sie finanzieren sich mit unserem Steuergeld, und vor jeder Wahl erzählen sie euch das Gleiche. Ob ihr nun die eine oder die andere Partei wählt: Am Ende regieren sie doch zusammen. Das ist keine Demokratie, das ist ein Kartell!',
            'Und die Medien? Die sitzen mit am Tisch. Wer die Wahrheit ausspricht, wird in die rechte Ecke gestellt oder gleich ganz totgeschwiegen. Deshalb sprechen wir direkt mit euch – auf der Straße und im Netz. Über eine Million Menschen folgen uns inzwischen. Das ist die echte Stimme des Volkes, nicht das, was in den Talkshows erzählt wird.',
            'Wir sagen: Schluss damit! Die Probleme in unserem Land sind nicht kompliziert, sie werden nur kompliziert gemacht. Wir wissen, was die Menschen wollen. Sie wollen sichere Straßen, bezahlbare Energie, und sie wollen, dass ihr hart verdientes Geld bei ihnen bleibt und nicht in Brüssel versickert.',
            'Deshalb fordern wir: Die großen Fragen dieses Landes – Zuwanderung, Energie, Europa – müssen künftig in bundesweiten Volksentscheiden entschieden werden. Nicht die Funktionäre, sondern ihr sollt bestimmen! Dann wird man sehen, dass wir die Mehrheit sind. Wer gegen Volksentscheide ist, der hat Angst vor dem Volk.',
            'Wir sind keine Partei wie die anderen. Wir sind eine Bewegung. Und diese Bewegung wird nicht aufhören, bis dieses Land wieder denen gehört, denen es gehört: euch, dem Volk!',
        ],
        'quelle': 'Übungsmaterial: eigens für Feibitur verfasste Rede einer fiktiven Partei. Ähnlichkeiten mit realen Personen oder Parteien sind nicht beabsichtigt; die Rede dient ausschließlich der Analyse populistischer Kommunikationsmuster.',
        'id': 'm1',
    },
    {
        'id': 'm2',
        'titel': 'M2: Ergebnisse ausgewählter Bundestagswahlen 1972–2025',
        'typ': 'tabelle',
        'kopf': [
            'Wahljahr',
            'CDU/CSU (Zweitstimmen in %)',
            'SPD (Zweitstimmen in %)',
            'CDU/CSU und SPD zusammen (in %)',
            'Wahlbeteiligung (in %)',
            'Fraktionen im Bundestag',
        ],
        'zeilen': [
            ['1972', '44,9', '45,8', '90,7', '91,1', '3'],
            ['1983', '48,8', '38,2', '87,0', '89,1', '4'],
            ['1998', '35,1', '40,9', '76,0', '82,2', '5'],
            ['2009', '33,8', '23,0', '56,8', '70,8', '5'],
            ['2017', '32,9', '20,5', '53,4', '76,2', '6'],
            ['2021', '24,1', '25,7', '49,8', '76,6', '6'],
            ['2025', '28,5', '16,4', '44,9', '82,5', '5'],
        ],
        'quelle': 'Eigene Zusammenstellung nach Angaben der Bundeswahlleiterin (Werte gerundet). CDU und CSU bilden im Bundestag eine gemeinsame Fraktion. 2025 zusätzlich ein Abgeordneter des SSW (keine Fraktion).',
    },
    {
        'id': 'm3',
        'titel': 'M3: Bericht „Radikal in 60 Sekunden“ (2025)',
        'absaetze': [
            'Der Clip dauert keine Minute. Ein junger Mann mit Bart und ruhiger Stimme erklärt, warum Musik, Freundschaften mit „Ungläubigen“ und Demokratie nicht zum wahren Glauben passten. Darunter: Zehntausende Likes. Ein paar Swipes weiter singt ein anderer junger Mann über ein „Volk“, das sich gegen „Überfremdung“ wehren müsse, untermalt mit Bildern von Fackeln und Fahnen. Auch hier: Tausende Kommentare, viele von Jugendlichen.',
            'Sicherheitsbehörden in Bund und Ländern warnen seit einiger Zeit, dass sich Menschen immer jünger und immer schneller radikalisieren. Eine wichtige Rolle spielen kurze Videos in sozialen Netzwerken. Sie greifen Alltagsfragen auf – Identität, Zugehörigkeit, Ungerechtigkeit, Einsamkeit – und bieten einfache Antworten und klare Feindbilder.',
            'Islamistische und rechtsextremistische Akteure unterscheiden sich in ihren Zielen grundlegend: Die einen wollen eine Ordnung, die sich auf ihre Auslegung religiöser Gebote stützt, die anderen eine ethnisch definierte „Volksgemeinschaft“. Doch ihre Methoden ähneln sich: ein Denken in „Wir“ und „Die“, das Versprechen von Stärke und Gemeinschaft, die Abwertung anderer Menschen und die Ablehnung der Demokratie als schwach und verlogen.',
            'Gegenmaßnahmen sind umstritten. Die einen fordern, die Plattformen schärfer zu regulieren und extremistische Konten schneller zu sperren. Andere setzen auf Prävention: Medienbildung in Schulen, Beratungsstellen für Angehörige und Aussteigerprogramme. Wieder andere verlangen mehr Befugnisse für Polizei und Verfassungsschutz, etwa bei der Überwachung von Messengerdiensten. Kritiker warnen dabei vor zu weitreichenden Eingriffen in die Grundrechte.',
            'Eine Sozialarbeiterin, die mit gefährdeten Jugendlichen arbeitet, sagt: „Verbote allein helfen nicht. Die Jugendlichen suchen Halt und Anerkennung. Wenn wir ihnen das nicht geben, tun es andere.“',
        ],
        'quelle': 'Übungsmaterial: eigens für Feibitur verfasster Bericht (2025). Die beschriebenen Videos und die zitierte Sozialarbeiterin sind fiktiv; die Warnungen vor einer Radikalisierung immer jüngerer Menschen entsprechen Einschätzungen der Verfassungsschutzbehörden.',
    },
]

AUFGABEN = [
    {
        'id': 'q1-2-i1',
        'afb': 'I',
        'operator': 'wiedergeben',
        'text': 'Geben Sie die Aussagen der Rede wieder. (M1)',
        'material': ['m1'],
        'loesung': {
            'vorbemerkung': 'Einleitungssatz: Rede des Vorsitzenden der fiktiven Partei „Stimme des Volkes“ auf einer Kundgebung 2026, Thema: Kritik an etablierten Parteien und Medien, Forderung nach Volksentscheiden.',
            'punkte': [
                'Der Redner spricht „normale“ Bürger (Pflegerin, Handwerker, Rentnerin) an und wirft der Politik vor, über statt mit ihnen zu reden [1].',
                'Die etablierten Parteien hätten sich den Staat zur Beute gemacht, verteilten Posten, finanzierten sich mit Steuergeld und regierten ohnehin zusammen – es handle sich um ein Kartell [2].',
                'Die Medien seien Teil dieses Systems und grenzten Kritiker aus; deshalb kommuniziere die Partei direkt (Straße, Internet) und sei die „echte Stimme des Volkes“ [3].',
                'Probleme seien einfach; die Partei wisse, was die Menschen wollten (Sicherheit, bezahlbare Energie, kein Geld für Brüssel) [4].',
                'Forderung: bundesweite Volksentscheide über Zuwanderung, Energie und Europa; wer dagegen sei, habe Angst vor dem Volk [5].',
                'Selbstdarstellung als Bewegung, die das Land „dem Volk“ zurückgeben wolle [6].',
            ],
            'hinweis': 'Wiedergeben: in eigenen Worten, indirekte Rede, ohne Wertung, mit Einleitungssatz.',
        },
        'bewertung': {
            'ausreichend': 'die Aussagen der Rede im Ansatz korrekt wiedergegeben werden',
            'gut': 'die Aussagen der Rede weitgehend korrekt, strukturiert und in eigenen Worten wiedergegeben werden',
        },
    },
    {
        'id': 'q1-2-i2',
        'afb': 'I',
        'operator': 'beschreiben',
        'material': ['m2'],
        'text': 'Beschreiben Sie die in M2 dargestellte Entwicklung.',
        'loesung': {
            'punkte': [
                'Formal: Tabelle mit ausgewählten Bundestagswahlen 1972–2025; Zweitstimmenanteile von CDU/CSU und SPD, gemeinsamer Anteil, Wahlbeteiligung, Zahl der Fraktionen; Quelle: Bundeswahlleiterin, gerundet.',
                'Gemeinsamer Anteil von CDU/CSU und SPD sinkt von 90,7 % (1972) auf 44,9 % (2025), also um rund 46 Prozentpunkte; stärkster Rückgang zwischen 1998 und 2009.',
                'SPD: von 45,8 % (1972) auf 16,4 % (2025); CDU/CSU: Höchstwert 48,8 % (1983), Tiefstwert 24,1 % (2021), 2025 wieder 28,5 %.',
                'Wahlbeteiligung: Höchstwert 91,1 % (1972), Tiefstwert 70,8 % (2009), Anstieg auf 82,5 % (2025).',
                'Zahl der Fraktionen steigt von 3 (1972) auf 6 (2017, 2021); 2025 sind es 5.',
            ],
            'hinweis': 'Beschreiben: Werte korrekt (Prozent vs. Prozentpunkte), strukturiert, ohne Interpretation.',
        },
        'bewertung': {
            'ausreichend': 'die wesentlichen Entwicklungen im Ansatz korrekt beschrieben werden.',
            'gut': 'die Tabelle formal und inhaltlich vollständig, strukturiert und mit korrekter Verwendung von Prozent und Prozentpunkten beschrieben wird.',
        },
    },
    {
        'id': 'q1-2-i3',
        'afb': 'I',
        'operator': 'wiedergeben',
        'material': ['m3'],
        'text': 'Geben Sie die Aussagen des Berichts (M3) wieder.',
        'loesung': {
            'vorbemerkung': 'Einleitungssatz: Bericht „Radikal in 60 Sekunden“ (2025) über Radikalisierung Jugendlicher über soziale Medien.',
            'punkte': [
                'Beispiele für kurze islamistische und rechtsextremistische Videos mit großer Reichweite unter Jugendlichen [1].',
                'Sicherheitsbehörden warnen vor schnellerer Radikalisierung immer jüngerer Menschen; Kurzvideos greifen Alltagsfragen auf und bieten einfache Antworten und Feindbilder [2].',
                'Ziele unterscheiden sich (religiös begründete Ordnung vs. ethnische „Volksgemeinschaft“), Methoden ähneln sich (Wir-Die-Denken, Stärke und Gemeinschaft, Abwertung, Demokratiefeindlichkeit) [3].',
                'Umstrittene Gegenmaßnahmen: Plattformregulierung, Prävention, mehr Befugnisse für Sicherheitsbehörden; Warnung vor Grundrechtseingriffen [4].',
                'Sozialarbeiterin: Verbote allein reichten nicht, Jugendliche suchten Halt und Anerkennung [5].',
            ],
            'hinweis': 'Wiedergeben: eigene Worte, indirekte Rede, Einleitungssatz, keine Wertung.',
        },
        'bewertung': {
            'ausreichend': 'die Aussagen des Berichts im Ansatz korrekt wiedergegeben werden.',
            'gut': 'die Aussagen weitgehend vollständig, strukturiert und in eigenen Worten mit Einleitungssatz wiedergegeben werden.',
        },
    },
    {
        'id': 'q1-2-ii1',
        'afb': 'II',
        'operator': 'analysieren',
        'text': 'Analysieren Sie die Rede im Hinblick auf Merkmale populistischer Kommunikation. (M1)',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Volk-Elite-Gegensatz / Anti-Elitarismus: „die Menschen, die dieses Land am Laufen halten“ vs. „die Politik in Berlin“, „Funktionäre“ [1], [5].',
                'Antipluralismus und moralischer Alleinvertretungsanspruch: „echte Stimme des Volkes“ [3], „wir wissen, was die Menschen wollen“ [4], „dass wir die Mehrheit sind“ [5]; Gegner werden delegitimiert („Angst vor dem Volk“).',
                'Pauschale Diskreditierung von Institutionen: Parteien als „Kartell“, Staat als „Beute“ [2]; Medien als Teil des Systems [3] – Anknüpfung an Kartellpartei-These, aber verzerrt.',
                'Vereinfachung komplexer Probleme: „nicht kompliziert, nur kompliziert gemacht“ [4]; keine konkreten Lösungswege.',
                'Emotionalisierung und Identifikationsangebote: direkte Anrede („liebe Freunde“, „ihr“), Alltagsfiguren, Ausrufe, Wir-gegen-sie-Rhetorik [1], [6].',
                'Feindbilder: „Brüssel“, Medien, etablierte Parteien; implizit Zuwanderung als Problem [4], [5].',
                'Direkte Kommunikation über soziale Medien unter Umgehung journalistischer Gatekeeper [3] (Bezug Q1.4).',
                'Selbstinszenierung als „Bewegung“ statt Partei [6] – Distanz zum Parteiensystem.',
                'Ggf. Einordnung: Merkmale nach Jan-Werner Müller (antielitär + antipluralistisch); nicht automatisch extremistisch, aber in Spannung zur FdGO.',
            ],
            'hinweis': 'Analysieren: aspektgeleitet mit Fachkategorien und konsequenten Materialbelegen. Eine bloße Liste von Merkmalen ohne Belege aus der Rede genügt nicht.',
        },
        'bewertung': {
            'ausreichend': 'einige Merkmale populistischer Kommunikation ansatzweise mit Materialbezug analysiert werden',
            'gut': 'die Merkmale populistischer Kommunikation differenziert, fachsprachlich präzise und mit durchgängigen Materialbelegen analysiert werden',
        },
    },
    {
        'id': 'q1-2-ii2',
        'afb': 'II',
        'operator': 'erläutern',
        'text': 'Erläutern Sie, welche Funktionen politische Parteien in der repräsentativen Demokratie erfüllen sollen.',
        'material': [],
        'loesung': {
            'punkte': [
                'Verfassungsgrundlage: Art. 21 GG – Parteien wirken bei der politischen Willensbildung mit; Parteiengesetz.',
                'Artikulation und Aggregation: gesellschaftliche Interessen aufgreifen und zu Programmen bündeln.',
                'Partizipation und Integration: Möglichkeit zur Mitarbeit, Einbindung unterschiedlicher Gruppen, Kompromissbildung.',
                'Rekrutierung/Elitenauswahl: Aufstellung von Kandidierenden, Besetzung politischer Ämter.',
                'Legitimation und Regierungsbildung: Strukturierung von Wahlen, Koalitionsbildung, Regierungs- bzw. Oppositionsfunktion, Kontrolle.',
                'Vermittlungsfunktion zwischen Gesellschaft und Staat; Beispiele (Koalitionsvertrag, Parteiprogramme, Jugendorganisationen, Kandidatenaufstellung).',
                'Optional: Probleme der Funktionserfüllung (Mitgliederschwund, Repräsentationslücken), die Populisten aufgreifen.',
            ],
            'hinweis': 'Erläutern: Funktionen müssen mit Beispielen veranschaulicht werden.',
        },
        'bewertung': {
            'ausreichend': 'die Funktionen von Parteien ansatzweise erläutert werden',
            'gut': 'die Funktionen von Parteien differenziert und mit passenden Beispielen erläutert werden',
        },
    },
    {
        'id': 'q1-2-ii3',
        'afb': 'II',
        'operator': 'erklären',
        'material': ['m2'],
        'text': 'Erklären Sie mögliche Ursachen für die in M2 dargestellte Entwicklung des Parteiensystems.',
        'loesung': {
            'punkte': [
                'Auflösung sozialer Milieus (Arbeitermilieu, katholisch-kirchliches Milieu) und abnehmende Parteibindung (Dealignment), mehr Wechselwähler (Volatilität).',
                'Individualisierung und Pluralisierung der Lebensstile; Volksparteien können immer weniger Gruppen integrieren.',
                'Neue Konfliktlinien (Ökologie seit den 1980ern → Grüne; Ost-West → PDS/Linke; Migration, Globalisierung, EU, kosmopolitisch vs. kommunitaristisch → AfD, BSW).',
                'Unzufriedenheit mit Großen Koalitionen, programmatische Annäherung der großen Parteien, Repräsentationslücken, Krisen (Agenda 2010, Finanzkrise, Migration 2015, Pandemie, Energiekrise).',
                'Wandel der Mediennutzung und Personalisierung; neue Parteien können sich über soziale Medien schnell bekannt machen.',
                'Bezug zu M2: Rückgang des Anteils der Volksparteien, Zunahme der Fraktionen, schwankende Wahlbeteiligung.',
            ],
            'hinweis': 'Erklären: Ursachen auf fachliche Modelle zurückführen (Milieu, Cleavages, Dealignment); Daten aus M2 einbeziehen.',
        },
        'bewertung': {
            'ausreichend': 'einige zutreffende Ursachen ansatzweise erklärt und auf M2 bezogen werden.',
            'gut': 'mehrere Ursachen differenziert, fachsprachlich präzise und mit Bezug auf Modelle der Parteienforschung und die Daten in M2 erklärt werden.',
        },
    },
    {
        'id': 'q1-2-ii4',
        'afb': 'II',
        'operator': 'vergleichen',
        'material': ['m3'],
        'text': 'Vergleichen Sie Rechtsextremismus (insbesondere völkischen Nationalismus) und Islamismus hinsichtlich ihrer Ziele, ihres Menschenbildes und ihres Verhältnisses zur freiheitlichen demokratischen Grundordnung. (M3)',
        'loesung': {
            'punkte': [
                'Vergleichskriterien ausdrücklich benennen (Ziele, Menschenbild, Verhältnis zur FdGO, ggf. Methoden/Zielgruppen).',
                'Ziele: völkischer Nationalismus – ethnisch homogene „Volksgemeinschaft“, autoritärer Staat; Islamismus – Staats- und Gesellschaftsordnung nach eigener Auslegung religiöser Normen (Scharia, Kalifat).',
                'Menschenbild: beide ungleichwertig – Abwertung nach Abstammung/Herkunft bzw. nach Glauben und Geschlecht; Verstoß gegen die gleiche Menschenwürde (Art. 1 GG).',
                'Verhältnis zur FdGO: beide lehnen Volkssouveränität, Pluralismus, Gleichberechtigung und Minderheitenschutz ab; Gewalt wird teilweise legitimiert (Rechtsterrorismus, Dschihadismus); es gibt jeweils legalistische und gewaltorientierte Strömungen.',
                'Gemeinsamkeiten (M3 [3]): Freund-Feind-Denken, Absolutheitsanspruch, Gemeinschaftsversprechen, Demokratieverachtung, Ansprache Jugendlicher über soziale Medien [2].',
                'Unterschiede: Begründung (ethnisch-national vs. religiös), Bezugsgemeinschaft (Nation vs. Umma), teilweise gegenseitige Feindbilder.',
                'Fazit des Vergleichs.',
            ],
            'hinweis': 'Vergleichen: Gemeinsamkeiten UND Unterschiede kriteriengeleitet und begründet darlegen; Unterscheidung zwischen Islam (Religion, Art. 4 GG) und Islamismus (Ideologie) muss deutlich werden.',
        },
        'bewertung': {
            'ausreichend': 'beide Formen des Extremismus ansatzweise kriteriengeleitet verglichen werden.',
            'gut': 'der Vergleich kriteriengeleitet, differenziert, fachlich korrekt (Islam vs. Islamismus, FdGO) und mit Gemeinsamkeiten und Unterschieden erfolgt.',
        },
    },
    {
        'id': 'q1-2-ii5',
        'afb': 'II',
        'operator': 'einordnen',
        'material': ['m1'],
        'lk': True,
        'text': 'Ordnen Sie das in der Rede (M1) erkennbare Demokratieverständnis in die Theorie der identitären Demokratie ein.',
        'loesung': {
            'punkte': [
                'Identitäre Demokratie (Rousseau): vorgegebener, homogener Gemeinwille (volonté générale), Identität von Regierenden und Regierten, Skepsis gegenüber Repräsentation und intermediären Organisationen; Gemeinwohl a priori.',
                'Belege in M1: Behauptung eines einheitlichen Volkswillens („Wir wissen, was die Menschen wollen“ [4]), Abwertung von Parteien und Medien als Störfaktoren [2], [3], Forderung nach Volksentscheiden über alle großen Fragen [5], Selbstverständnis als „Bewegung“ statt Partei [6].',
                'Gegenmodell: repräsentative/pluralistische Demokratie (Fraenkel): Gemeinwohl a posteriori, Legitimität von Interessenvielfalt, Parteien und Kompromissen.',
                'Einordnung: Rede weist zentrale Merkmale identitären Denkens auf; populistische Verknüpfung (Antipluralismus); Gefahren für Minderheiten.',
            ],
            'hinweis': 'Einordnen: Theorie korrekt darstellen und die Position begründet mit Belegen zuordnen.',
        },
        'bewertung': {
            'ausreichend': 'die identitäre Demokratietheorie ansatzweise korrekt dargestellt und die Rede mit einzelnen Belegen zugeordnet wird.',
            'gut': 'die Theorie differenziert dargestellt, die Rede mit mehreren Belegen begründet eingeordnet und vom pluralistischen Modell abgegrenzt wird.',
        },
    },
    {
        'id': 'q1-2-iii1',
        'afb': 'III',
        'operator': 'beurteilen',
        'text': 'Beurteilen Sie die in der Rede erhobene Forderung, wichtige politische Fragen künftig grundsätzlich durch bundesweite Volksentscheide zu entscheiden. (M1)',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Pro: höhere Legitimation und Akzeptanz; unmittelbare Beteiligung, Antwort auf Repräsentationslücken; Korrektiv zwischen Wahlen; Beispiele aus Ländern/Kommunen oder der Schweiz; Förderung politischer Debatte.',
                'Contra: GG sieht auf Bundesebene grundsätzlich die repräsentative Demokratie vor (Volksentscheid nur Art. 29; Einführung bräuchte Verfassungsänderung); komplexe Fragen (Zuwanderung, Energie, Europa) werden auf Ja/Nein verkürzt; Gefahr von Kampagnen und Desinformation; Minderheitenrechte und Grundrechte (z. B. Asylrecht, Menschenwürde) dürfen nicht zur Abstimmung stehen; europarechtliche Bindungen; Verantwortlichkeit unklar; geringe Beteiligung.',
                'Einordnung der Forderung als Teil populistischer Strategie: Volksentscheid als Mittel, den angeblich homogenen Volkswillen gegen Institutionen auszuspielen (identitäres Demokratieverständnis); Delegitimierung von Gegnern („Angst vor dem Volk“).',
                'Mögliche differenzierte Lösungsperspektive: ergänzende Beteiligungsformen (Bürgerräte, Volksinitiativen mit Quoren, Ausschluss von Grundrechtsfragen) statt grundsätzlicher Entscheidung aller großen Fragen.',
                'Begründetes Urteil auf Basis expliziter Kriterien (z. B. Legitimität, Effizienz, Minderheitenschutz, Verfassungskonformität).',
            ],
            'hinweis': "Beurteilen: Kriterien müssen erkennbar sein, das Urteil muss begründet sein; eigene Wertmaßstäbe müssen hier nicht explizit offengelegt werden (anders als bei 'bewerten').",
        },
        'bewertung': {
            'ausreichend': 'ein ansatzweise kriterienorientiertes und nachvollziehbar begründetes Urteil formuliert wird.',
            'gut': 'die Forderung strukturiert, kriterienorientiert und weitgehend kohärent beurteilt wird und in ein schlüssig begründetes Urteil mündet.',
        },
    },
    {
        'id': 'q1-2-iii2',
        'afb': 'III',
        'operator': 'diskutieren',
        'material': ['m2'],
        'text': 'Diskutieren Sie, ob die in M2 erkennbare Fragmentierung des Parteiensystems die Stabilität der Demokratie in Deutschland gefährdet.',
        'loesung': {
            'punkte': [
                'Gefährdung: schwierigere Regierungsbildung, Dreierkoalitionen mit hohem Konfliktpotenzial (z. B. Ampel bis 2024), weniger Auswahl an Mehrheiten, Stärkung extremer Ränder, Polarisierung, vorgezogene Neuwahlen, Kanzlerwahl 2025 erst im zweiten Wahlgang.',
                'Keine Gefährdung: bessere Abbildung gesellschaftlicher Vielfalt (Repräsentation), stabile Institutionen (konstruktives Misstrauensvotum, Sperrklausel), hohe Wahlbeteiligung 2025 als Zeichen von Mobilisierung, Fragmentierung ist in vielen europäischen Demokratien normal, Koalitionsfähigkeit demokratischer Parteien.',
                'Differenzierung: Problem liegt weniger in der Zahl der Parteien als in der Stärke antidemokratischer Kräfte und der Bereitschaft zu Kompromissen.',
                'Begründete Bewertung am Ende.',
            ],
            'hinweis': 'Diskutieren: Argumentation mit Pro und Contra, die zu einer begründeten Bewertung führt; Bezug zu den Daten in M2.',
        },
        'bewertung': {
            'ausreichend': 'die Diskussion ansatzweise strukturiert ist und in eine nachvollziehbare Bewertung mündet.',
            'gut': 'die Diskussion strukturiert, fachlich fundiert, mit Bezug zu M2 und weitgehend kohärent ist und in eine schlüssig begründete Bewertung mündet.',
        },
    },
    {
        'id': 'q1-2-iii3',
        'afb': 'III',
        'operator': 'beurteilen',
        'material': ['m3'],
        'text': 'Beurteilen Sie die in M3 genannten Maßnahmen gegen die Radikalisierung junger Menschen im Internet.',
        'loesung': {
            'punkte': [
                'Kriterien benennen (z. B. Effektivität, Verhältnismäßigkeit/Grundrechtsschutz, Durchsetzbarkeit, langfristige Wirkung).',
                'Plattformregulierung/Sperrungen: schnell wirksam, rechtliche Grundlage (Digital Services Act, Strafrecht), aber Ausweichen auf andere Plattformen/Messenger, Abgrenzung legal/illegal, Gefahr von Overblocking, Grenzen der Meinungsfreiheit (Art. 5 GG).',
                'Prävention (Medienbildung, Beratung, Aussteigerprogramme): setzt an Ursachen an (Identität, Zugehörigkeit – M3 [5]), langfristig wirksam, aber langsam, abhängig von Finanzierung und Personal.',
                'Mehr Befugnisse für Sicherheitsbehörden: Gefahrenabwehr bei Anschlagsplänen, aber Grundrechtseingriffe (Fernmeldegeheimnis Art. 10 GG, informationelle Selbstbestimmung), Verhältnismäßigkeit, Kontrolle durch Gerichte.',
                'Abwägung und begründetes Urteil, z. B. Kombination der Maßnahmen mit Vorrang der Prävention.',
            ],
            'hinweis': 'Beurteilen: kriteriengeleitet; wehrhafte Demokratie und Grundrechte sollten einbezogen werden.',
        },
        'bewertung': {
            'ausreichend': 'die Maßnahmen ansatzweise kriteriengeleitet beurteilt werden und ein nachvollziehbares Urteil vorliegt.',
            'gut': 'die Maßnahmen differenziert anhand ausdrücklicher Kriterien, mit Fachwissen (Grundrechte, DSA, Prävention) beurteilt werden und ein schlüssiges Urteil vorliegt.',
        },
    },
]
