# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q1.3 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = 'Q1.3: Rechtssetzung im politischen Mehrebenensystem Europas; Vergemeinschaftung und Souveränitätsverlagerung; (LK) Debatte über das Demokratiedefizit. Zugleich Q1.1: europäische Institutionen im Gesetzgebungsprozess.'

MATERIALIEN = [
    {
        'titel': 'M1: Bericht „Ein Gesetz auf der Zielgeraden – und dann?“ (2025)',
        'absaetze': [
            'Eigentlich schien alles entschieden. Im Juli 2021 hatte die Europäische Kommission vorgeschlagen, ab 2035 nur noch Neuwagen zuzulassen, die kein CO<sub>2</sub> ausstoßen. Das Europäische Parlament und die Mitgliedstaaten im Rat legten ihre Positionen fest, im Oktober 2022 einigten sich die Unterhändler beider Seiten unter Vermittlung der Kommission. Im Februar 2023 stimmte das Parlament in Straßburg zu.',
            'Die Abstimmung im Rat der EU galt als Formsache. Doch dann meldete sich Berlin: Der damalige Bundesverkehrsminister von der FDP erklärte, Deutschland könne nur zustimmen, wenn Autos, die ausschließlich mit synthetischen, klimaneutralen Kraftstoffen (E-Fuels) fahren, auch nach 2035 zugelassen werden dürften. Weil auch andere Staaten zögerten, war die qualifizierte Mehrheit plötzlich in Gefahr.',
            'In Brüssel war man verärgert. Diplomaten anderer Staaten sprachen von einem Vertrauensbruch: Wer nach einer Einigung im Trilog noch einmal nachverhandle, stelle das ganze Verfahren infrage. Abgeordnete des Europäischen Parlaments beklagten, ihr Votum werde von einer nationalen Koalitionsdebatte überlagert.',
            'Nach wochenlangen Gesprächen sagte die Kommission zu, einen Vorschlag für die Zulassung reiner E-Fuel-Fahrzeuge vorzulegen. Im März 2023 stimmte der Rat der Verordnung zu. Die Bundesregierung sprach von einem Erfolg für die Technologieoffenheit, Umweltverbände von einem Schlupfloch.',
            'Der Streit um den Verbrennungsmotor ist damit nicht beendet. Autoindustrie und mehrere Regierungen fordern seitdem, die Regeln zu lockern; andere warnen, dass Europa so seine Klimaziele verfehle. Der Fall zeigt, wie eng in Europa Klimapolitik, Industrieinteressen und nationale Politik miteinander verflochten sind – und wie schwer es ist, zu sagen, wer am Ende eigentlich entschieden hat.',
        ],
        'quelle': 'Übungsmaterial: eigens für Feibitur verfasster Bericht (2025) auf Grundlage des öffentlich dokumentierten Verfahrens zur Verordnung (EU) 2023/851.',
        'id': 'm1',
    },
    {
        'id': 'm2',
        'titel': 'M2: Vertrag über die Europäische Union (EUV), Art. 5 (Auszug)',
        'absaetze': [
            '(1) Für die Abgrenzung der Zuständigkeiten der Union gilt der Grundsatz der begrenzten Einzelermächtigung. Für die Ausübung der Zuständigkeiten der Union gelten die Grundsätze der Subsidiarität und der Verhältnismäßigkeit.',
            '(2) Nach dem Grundsatz der begrenzten Einzelermächtigung wird die Union nur innerhalb der Grenzen der Zuständigkeiten tätig, die die Mitgliedstaaten ihr in den Verträgen zur Verwirklichung der darin niedergelegten Ziele übertragen haben. Alle der Union nicht in den Verträgen übertragenen Zuständigkeiten verbleiben bei den Mitgliedstaaten.',
            '(3) Nach dem Subsidiaritätsprinzip wird die Union in den Bereichen, die nicht in ihre ausschließliche Zuständigkeit fallen, nur tätig, sofern und soweit die Ziele der in Betracht gezogenen Maßnahmen von den Mitgliedstaaten weder auf zentraler noch auf regionaler oder lokaler Ebene ausreichend verwirklicht werden können, sondern vielmehr wegen ihres Umfangs oder ihrer Wirkungen auf Unionsebene besser zu verwirklichen sind. […] Die nationalen Parlamente achten auf die Einhaltung des Subsidiaritätsprinzips […].',
            '(4) Nach dem Grundsatz der Verhältnismäßigkeit gehen die Maßnahmen der Union inhaltlich wie formal nicht über das zur Erreichung der Ziele der Verträge erforderliche Maß hinaus. […]',
        ],
        'quelle': 'Vertrag über die Europäische Union in der Fassung des Vertrags von Lissabon, Art. 5 (Auszug).',
    },
    {
        'id': 'm3',
        'titel': 'M3: Sitzverteilung im Europäischen Parlament 2024–2029 (Auswahl)',
        'typ': 'tabelle',
        'kopf': [
            'Mitgliedstaat',
            'Sitze',
            'Einwohner (gerundet, in Mio.)',
            'Einwohner je Sitz (gerundet)',
        ],
        'zeilen': [
            [
                'Deutschland',
                '96',
                '83,4',
                'rund 869.000',
            ],
            [
                'Frankreich',
                '81',
                '68,4',
                'rund 844.000',
            ],
            [
                'Italien',
                '76',
                '58,9',
                'rund 775.000',
            ],
            [
                'Spanien',
                '61',
                '48,6',
                'rund 797.000',
            ],
            [
                'Polen',
                '53',
                '36,6',
                'rund 691.000',
            ],
            [
                'Niederlande',
                '31',
                '17,9',
                'rund 577.000',
            ],
            [
                'Luxemburg',
                '6',
                '0,67',
                'rund 112.000',
            ],
            ['Malta', '6', '0,56', 'rund 93.000'],
            [
                '<b>EU gesamt</b>',
                '<b>720</b>',
                '<b>ca. 449</b>',
                '<b>rund 624.000</b>',
            ],
        ],
        'quelle': 'Sitzzahlen: Beschluss des Europäischen Rates zur Zusammensetzung des Europäischen Parlaments für die Wahlperiode 2024–2029. Einwohnerzahlen: Eurostat, Stand 1.1.2024 (gerundet). Einwohner je Sitz: eigene Berechnung.',
    },
]

AUFGABEN = [
    {
        'id': 'q1-3-i1',
        'afb': 'I',
        'operator': 'beschreiben',
        'text': 'Beschreiben Sie den in M1 dargestellten Entscheidungsprozess.',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Einleitung: Bericht (2025) über das Gesetzgebungsverfahren zu den CO2-Flottengrenzwerten (sog. Verbrenner-Aus).',
                'Vorschlag der Kommission 2021 (Null-Emission für Neuwagen ab 2035) [1].',
                'Festlegung der Positionen von Parlament und Rat, Einigung im Trilog im Oktober 2022, Zustimmung des EP im Februar 2023 [1].',
                'Deutsche Bundesregierung (FDP-Verkehrsminister) verlangt Ausnahme für E-Fuels; qualifizierte Mehrheit im Rat gefährdet [2].',
                'Kritik anderer Staaten und von EP-Abgeordneten (Vertrauensbruch, Überlagerung durch nationale Koalitionsdebatte) [3].',
                'Kompromiss: Zusage der Kommission, Zustimmung des Rates im März 2023; unterschiedliche Bewertungen [4].',
                'Fortdauernder Streit um Lockerung, Verflechtung von Klima-, Industrie- und nationaler Politik [5].',
            ],
            'hinweis': 'Beschreiben: strukturiert, chronologisch nachvollziehbar, fachsprachlich (Kommission, Rat, Trilog, qualifizierte Mehrheit); keine Bewertung.',
        },
        'bewertung': {
            'ausreichend': 'der Entscheidungsprozess im Ansatz korrekt und nachvollziehbar beschrieben wird',
            'gut': 'der Entscheidungsprozess weitgehend vollständig, strukturiert und fachsprachlich korrekt beschrieben wird',
        },
    },
    {
        'id': 'q1-3-i2',
        'afb': 'I',
        'operator': 'beschreiben',
        'material': ['m3'],
        'text': 'Beschreiben Sie die Tabelle (M3).',
        'loesung': {
            'punkte': [
                'Formal: Tabelle zur Sitzverteilung im Europäischen Parlament 2024–2029 (Auswahl von acht Mitgliedstaaten), Sitze, Einwohner in Mio., Einwohner je Sitz; Quellen: Europäischer Rat, Eurostat (2024), eigene Berechnung.',
                'Deutschland hat mit 96 Sitzen die meisten Sitze, Luxemburg und Malta mit je 6 die wenigsten der Auswahl; insgesamt 720 Sitze für ca. 449 Mio. Einwohner.',
                'Einwohner je Sitz: Deutschland rund 869.000 (höchster Wert), Malta rund 93.000 (niedrigster Wert); große Staaten liegen über, kleine deutlich unter dem EU-Durchschnitt von rund 624.000.',
                'Die Sitzzahl wächst mit der Einwohnerzahl, aber unterproportional.',
            ],
            'hinweis': "Beschreiben: formal und inhaltlich, Extremwerte und Tendenzen nennen, ohne Interpretation (z. B. ohne Begriff 'ungerecht').",
        },
        'bewertung': {
            'ausreichend': 'die Tabelle im Ansatz formal und inhaltlich korrekt beschrieben wird.',
            'gut': 'die Tabelle vollständig, strukturiert und mit den wichtigsten Werten, Extremwerten und Tendenzen beschrieben wird.',
        },
    },
    {
        'id': 'q1-3-i3',
        'afb': 'I',
        'operator': 'wiedergeben',
        'material': ['m2'],
        'text': 'Geben Sie die in M2 genannten Grundsätze zur Abgrenzung und Ausübung der Zuständigkeiten der EU wieder.',
        'loesung': {
            'vorbemerkung': 'Einleitungssatz: Art. 5 EUV regelt die Zuständigkeiten der Union.',
            'punkte': [
                'Abgrenzung nach dem Grundsatz der begrenzten Einzelermächtigung; Ausübung nach Subsidiarität und Verhältnismäßigkeit [1].',
                'Begrenzte Einzelermächtigung: Die EU handelt nur in den Bereichen, die ihr die Mitgliedstaaten in den Verträgen übertragen haben; alles andere bleibt bei den Staaten [2].',
                'Subsidiarität: Außerhalb ausschließlicher Zuständigkeiten handelt die EU nur, wenn Ziele von den Staaten (zentral, regional, lokal) nicht ausreichend und auf EU-Ebene besser erreicht werden können; nationale Parlamente wachen darüber [3].',
                'Verhältnismäßigkeit: EU-Maßnahmen dürfen nicht über das Erforderliche hinausgehen [4].',
            ],
            'hinweis': 'Wiedergeben: in eigenen Worten, unter Verwendung der Fachsprache, ohne Wertung.',
        },
        'bewertung': {
            'ausreichend': 'die Grundsätze im Ansatz korrekt in eigenen Worten wiedergegeben werden.',
            'gut': 'alle drei Grundsätze präzise, strukturiert und in eigenen Worten fachsprachlich korrekt wiedergegeben werden.',
        },
    },
    {
        'id': 'q1-3-ii1',
        'afb': 'II',
        'operator': 'erklären',
        'text': 'Erklären Sie anhand des Fallbeispiels die Rollen von Kommission, Europäischem Parlament und Rat der EU im ordentlichen Gesetzgebungsverfahren. (M1)',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Kommission: Initiativmonopol (Vorschlag 2021 im Rahmen von „Fit for 55“), vertritt das Gemeinschaftsinteresse, vermittelt im Trilog, macht im Konflikt Zusagen (E-Fuel-Vorschlag) – Agenda-Setter und Vermittlerin.',
                'Europäisches Parlament: direkt gewählt, Mitgesetzgeber, legt Position fest, verhandelt im Trilog, stimmt zu (Februar 2023); kein Initiativrecht; im Fall: Votum durch nationale Blockade unter Druck.',
                'Rat der EU: Fachminister der Mitgliedstaaten, vertritt nationale Interessen, Mitgesetzgeber, Entscheidung mit qualifizierter Mehrheit (55 % der Staaten, 65 % der Bevölkerung) – Erklärung, warum Deutschland (bevölkerungsreichster Staat) mit anderen Zögernden die Mehrheit gefährden kann.',
                'Ordentliches Gesetzgebungsverfahren (Art. 294 AEUV): Gleichberechtigung von EP und Rat, beide müssen zustimmen; Trilog als informelles Verhandlungsforum.',
                'Rückwirkung nationaler Politik (Koalitionskonflikt in Berlin) auf die EU-Ebene; Verhältnis supranational vs. intergouvernemental.',
            ],
            'hinweis': "Erklären: Rollen müssen auf Regeln/Funktionszusammenhänge zurückgeführt und mit dem Fall verknüpft werden; reine Institutionenkunde ohne Fallbezug reicht nicht für 'gut'.",
        },
        'bewertung': {
            'ausreichend': 'die Rollen der Institutionen ansatzweise mit Bezug zum Fall erklärt werden',
            'gut': 'die Rollen der Institutionen differenziert, regelbezogen und durchgängig am Fall erklärt werden',
        },
    },
    {
        'id': 'q1-3-ii2',
        'afb': 'II',
        'operator': 'erläutern',
        'text': 'Erläutern Sie, warum es im europäischen Mehrebenensystem zu Konflikten um Kompetenzen kommt.',
        'material': [],
        'loesung': {
            'punkte': [
                'Prinzip der begrenzten Einzelermächtigung; Zuständigkeitsarten (ausschließlich, geteilt, unterstützend).',
                'Subsidiarität und Verhältnismäßigkeit als Auslegungsfragen: Wann ist eine EU-Regelung „besser“?',
                'Vergemeinschaftung = Souveränitätsverlagerung; Spannungsverhältnis zwischen Effizienz/gemeinsamer Handlungsfähigkeit und nationaler Selbstbestimmung bzw. Länderinteressen.',
                'Unterschiedliche Interessen der Ebenen und Akteure (Kommission/EP vs. nationale Regierungen, Industriestandorte, Parteien).',
                'Beispiele: Verbrenner-Aus (Industrie- vs. Klimapolitik), Datenschutz, Asyl/Migration, Ultra-vires-Konflikt BVerfG–EuGH (PSPP 2020), Subsidiaritätsrügen.',
            ],
            'hinweis': 'Erläutern: mit Beispielen veranschaulichen.',
        },
        'bewertung': {
            'ausreichend': 'Ursachen von Kompetenzkonflikten ansatzweise erläutert werden',
            'gut': 'Kompetenzkonflikte differenziert und mit passenden Beispielen erläutert werden',
        },
    },
    {
        'id': 'q1-3-ii3',
        'afb': 'II',
        'operator': 'auswerten',
        'material': ['m3'],
        'text': 'Werten Sie M3 im Hinblick auf die Frage aus, inwieweit die Wahl zum Europäischen Parlament dem Grundsatz der Wahlgleichheit entspricht.',
        'loesung': {
            'punkte': [
                'Wahlgleichheit: gleicher Zählwert und (bei Verhältniswahl) möglichst gleicher Erfolgswert jeder Stimme („one person, one vote“).',
                'Auswertung: Erfolgswert unterscheidet sich stark – eine Stimme aus Malta hat etwa das Neunfache (869.000 : 93.000 ≈ 9,3) des Gewichts einer Stimme aus Deutschland; Luxemburg ca. Faktor 8.',
                'Prinzip der degressiven Proportionalität: große Staaten mehr Sitze, kleine Staaten mehr Sitze je Einwohner; Mindestzahl 6, Höchstzahl 96 Sitze pro Staat.',
                'Gesamtaussage: Die Sitzverteilung weicht bewusst von strikter Wahlgleichheit ab, um kleinen Staaten eine Vertretung (Meinungsvielfalt, mehrere Parteien) zu sichern.',
                'Ggf. Fachwissen: BVerfG sieht darin einen Grund, das EP nicht als Parlament eines Bundesstaats zu verstehen (Lissabon-Urteil 2009); Bezug zur Debatte um das Demokratiedefizit.',
            ],
            'hinweis': 'Auswerten: Einzelwerte zu einer Gesamtaussage zusammenführen; Rechenbeispiele sind erwünscht.',
        },
        'bewertung': {
            'ausreichend': 'die Daten ansatzweise zu einer Aussage über die Wahlgleichheit zusammengeführt werden.',
            'gut': 'die Daten mit Rechenbeispielen und dem Prinzip der degressiven Proportionalität zu einer schlüssigen Gesamtaussage zusammengeführt werden.',
        },
    },
    {
        'id': 'q1-3-ii4',
        'afb': 'II',
        'operator': 'erläutern',
        'material': [],
        'lk': True,
        'text': 'Erläutern Sie unterschiedliche Zielvorstellungen der europäischen Integration zwischen Staatenbund und Bundesstaat.',
        'loesung': {
            'punkte': [
                'Staatenbund: souveräne Staaten, intergouvernementale Zusammenarbeit, Einstimmigkeit („Europa der Vaterländer“, de Gaulle); Befürworter betonen nationale Identität und Souveränität.',
                'Bundesstaat („Vereinigte Staaten von Europa“): eigene Verfassung, europäische Regierung, Parlament mit vollen Rechten, eigene Steuern/Armee; Befürworter betonen Handlungsfähigkeit und Demokratisierung.',
                'Status quo: Staatenverbund (BVerfG) mit supranationalen (Binnenmarkt, Handel, Wettbewerb) und intergouvernementalen Elementen (GASP, Steuern).',
                'Weitere Modelle: Europa der verschiedenen Geschwindigkeiten / differenzierte Integration, Kerneuropa.',
                'Beispiele: Euro, Schengen (differenzierte Integration), Debatten über Mehrheitsentscheidungen in der Außenpolitik, Grenzen durch das Grundgesetz (Art. 23, 79 Abs. 3, 146).',
            ],
            'hinweis': 'Erläutern: Modelle mit Beispielen und Argumenten veranschaulichen.',
        },
        'bewertung': {
            'ausreichend': 'mindestens zwei Zielvorstellungen ansatzweise erläutert werden.',
            'gut': 'die Zielvorstellungen differenziert, mit Beispielen und Bezug zum heutigen Staatenverbund erläutert werden.',
        },
    },
    {
        'id': 'q1-3-iii1',
        'afb': 'III',
        'operator': 'Stellung nehmen',
        'text': '„Die EU ist eine Demokratie der Regierungen, nicht der Bürger.“ Nehmen Sie Stellung zu dieser Aussage. Beziehen Sie das Fallbeispiel (M1) ein.',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Argumente für die Aussage: Rat (Regierungen) als Mitgesetzgeber und Europäischer Rat als Agenda-Setter; Regierungen können blockieren (Fallbeispiel); Trilog intransparent; EP ohne Initiativrecht; fehlende europäische Öffentlichkeit, Europawahlen als Nebenwahlen; Spitzenkandidatenprinzip 2019 nicht beachtet.',
                'Gegenargumente: EP gleichberechtigter Gesetzgeber und hat im Fall zugestimmt; doppelte Legitimation (auch Regierungen sind demokratisch gewählt und dem nationalen Parlament verantwortlich); Bürgerinitiative; Wahlbeteiligung zuletzt über 50 %; Kontrolle durch EuGH; Mitwirkung nationaler Parlamente (Art. 23 GG, Subsidiaritätsrüge).',
                'Ggf. Reformvorschläge (Initiativrecht für EP, mehr Transparenz im Trilog, Mehrheitsentscheidungen, transnationale Listen).',
                'Stellung nehmen: begründetes Urteil auf Basis von Kriterien UND ausdrückliche Offenlegung der eigenen Wertmaßstäbe (z. B. Vorrang von Bürgerbeteiligung/Wahlgleichheit vs. Handlungsfähigkeit/Effizienz).',
            ],
            'hinweis': "Bei 'Stellung nehmen/bewerten' müssen die eigenen Maßstäbe begründet dargelegt werden; fehlt dies, ist der Operator nur teilweise erfüllt.",
        },
        'bewertung': {
            'ausreichend': 'eine ansatzweise strukturierte Stellungnahme mit erkennbaren eigenen Maßstäben vorliegt.',
            'gut': 'die Stellungnahme differenziert abwägt, die eigenen Wertmaßstäbe offenlegt und in ein schlüssig begründetes Urteil mündet.',
        },
    },
    {
        'id': 'q1-3-iii2',
        'afb': 'III',
        'operator': 'beurteilen',
        'material': ['m2'],
        'text': 'Beurteilen Sie, ob das Subsidiaritätsprinzip (M2) die Mitgliedstaaten wirksam vor einer zu starken Zentralisierung in der EU schützt.',
        'loesung': {
            'punkte': [
                'Kriterien benennen (z. B. Wirksamkeit, Justiziabilität, Legitimität, Praxis).',
                'Für Wirksamkeit: verbindlicher Vertragsgrundsatz; Pflicht der Kommission zur Begründung; Subsidiaritätsrüge nationaler Parlamente (Frühwarnsystem, gelbe/orange Karte); Subsidiaritätsklage beim EuGH; Mitwirkung von Bundestag und Bundesrat (Art. 23 GG); Ultra-vires-Kontrolle des BVerfG.',
                'Gegen Wirksamkeit: unbestimmter Begriff („besser“) mit großem Auslegungsspielraum; Rügen erreichen selten die nötigen Quoren und binden die Kommission nicht endgültig; EuGH prüft zurückhaltend; Binnenmarktkompetenz wirkt weit; politische Dynamik von Krisen.',
                'Abwägung und begründetes Urteil (z. B. eher politisches als rechtlich scharfes Schutzinstrument).',
            ],
            'hinweis': 'Beurteilen: kriteriengeleitet mit Fachwissen; Bezug zum Vertragstext M2.',
        },
        'bewertung': {
            'ausreichend': 'ein ansatzweise kriteriengeleitetes, nachvollziehbares Urteil formuliert wird.',
            'gut': 'das Urteil kriteriengeleitet, abwägend und mit Fachwissen zu den Kontrollinstrumenten schlüssig begründet ist.',
        },
    },
    {
        'id': 'q1-3-iii3',
        'afb': 'III',
        'operator': 'diskutieren',
        'material': ['m3'],
        'text': 'Diskutieren Sie, ob die Sitzverteilung im Europäischen Parlament (M3) gerecht ist.',
        'loesung': {
            'punkte': [
                'Klärung des Gerechtigkeitsmaßstabs: Gleichheit der Bürger (Wahlgleichheit) vs. Gleichheit der Staaten (Föderalismus).',
                'Pro (gerecht): Schutz kleiner Staaten vor Dominanz der großen; Mindestvertretung für politische Vielfalt aus jedem Staat; Vergleich mit Bundesstaaten (Bundesrat, US-Senat); Rat vertritt die Staaten, EP die Bürger – Ausgleich im Gesamtsystem; doppelte Mehrheit im Rat berücksichtigt Bevölkerung.',
                'Contra: Verstoß gegen „one person, one vote“; Stimmen aus Deutschland zählen deutlich weniger; schwächt die demokratische Legitimation des EP (Demokratiedefizit); Alternativen (transnationale Listen, Zweikammersystem).',
                'Begründete Bewertung.',
            ],
            'hinweis': 'Diskutieren: Argumentation mit Pro und Contra, Bezug zu den Daten in M3, begründete Bewertung.',
        },
        'bewertung': {
            'ausreichend': 'Argumente für und gegen die Gerechtigkeit der Sitzverteilung ansatzweise abgewogen werden und eine Bewertung vorliegt.',
            'gut': 'die Diskussion strukturiert, mit klarem Gerechtigkeitsmaßstab, Bezug zu M3 und Fachwissen zum institutionellen Gefüge geführt wird und in eine schlüssige Bewertung mündet.',
        },
    },
]
