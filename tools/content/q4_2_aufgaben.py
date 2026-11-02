# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q4.2 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q4.2 (kein Schwerpunkt im Landesabitur 2027), insbesondere Freiheiten und Schranken des europäischen Binnenmarktes, Grenzen staatlicher Souveränität in Fiskal-, Wirtschafts- und Umweltpolitik sowie Krisen als Herausforderungen europäischer Politik; LK: Außenwirtschaftsbeziehungen und Außenwirtschaftspolitik der EU (Zoll- und Währungspolitik). Bezüge zu den Schwerpunkten Q2.1 (Staatsverschuldung), Q3.2 (Binnenmärkte, Handelskonflikte) und Q4.3."

SVG_KARIKATUR = """<svg viewBox='0 0 760 460' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='q42kt'>
<title id='q42kt'>Karikatur Balanceakt: Europa balanciert auf einer Wippe; links ziehen die Gewichte Energiepreise und Arbeitsplätze nach unten, auf die ein Ölfass mit der Aufschrift Iran-Krieg 2026 fällt; rechts schwebt das Gewicht Klimaziel 2040 nach oben; ein Industrievertreter fordert die Aussetzung des Emissionshandels, eine Klimaaktivistin warnt vor den Folgen.</title>
<rect x='0' y='0' width='760' height='460' fill='#fffdf6'/>
<rect x='0' y='372' width='760' height='30' fill='#c8c8c8'/>
<polygon points='380,290 342,372 418,372' fill='#22355e'/>
<polygon points='120,318 640,258 640,270 120,330' fill='#8c8c8c' stroke='#555555' stroke-width='2'/>
<polygon points='150,314 245,303 245,258 150,269' fill='#14213d'/>
<text x='197' y='283' text-anchor='middle' font-size='12' font-weight='bold' fill='#ffffff'>ENERGIE-</text>
<text x='197' y='297' text-anchor='middle' font-size='12' font-weight='bold' fill='#ffffff'>PREISE</text>
<polygon points='252,302 330,293 330,250 252,259' fill='#b5302a'/>
<text x='291' y='276' text-anchor='middle' font-size='12' font-weight='bold' fill='#ffffff'>ARBEITS-</text>
<text x='291' y='290' text-anchor='middle' font-size='12' font-weight='bold' fill='#ffffff'>PLÄTZE</text>
<polygon points='470,277 590,263 590,221 470,235' fill='#eef2fb' stroke='#14213d' stroke-width='2'/>
<text x='530' y='248' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>KLIMAZIEL</text>
<text x='530' y='264' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>2040: -90 %</text>
<rect x='175' y='118' width='90' height='76' rx='6' fill='#333333'/>
<ellipse cx='220' cy='118' rx='45' ry='9' fill='#555555'/>
<text x='220' y='148' text-anchor='middle' font-size='13' font-weight='bold' fill='#ffffff'>ÖL &amp; GAS</text>
<text x='220' y='166' text-anchor='middle' font-size='12' fill='#fff7e0'>Iran-Krieg</text>
<text x='220' y='184' text-anchor='middle' font-size='12' fill='#fff7e0'>2026</text>
<line x1='214' y1='196' x2='204' y2='244' stroke='#b5302a' stroke-width='4'/>
<polygon points='195,242 212,246 201,260' fill='#b5302a'/>
<polygon points='364,218 396,218 408,286 352,286' fill='#22355e'/>
<text x='380' y='262' text-anchor='middle' font-size='14' font-weight='bold' fill='#ffffff'>EU</text>
<line x1='290' y1='212' x2='470' y2='210' stroke='#555555' stroke-width='4'/>
<line x1='366' y1='226' x2='326' y2='213' stroke='#f2c9a0' stroke-width='6' stroke-linecap='round'/>
<line x1='394' y1='226' x2='434' y2='212' stroke='#f2c9a0' stroke-width='6' stroke-linecap='round'/>
<circle cx='380' cy='202' r='16' fill='#f2c9a0' stroke='#333333' stroke-width='2'/>
<circle cx='374' cy='199' r='2' fill='#333333'/><circle cx='386' cy='199' r='2' fill='#333333'/>
<path d='M372 210 Q376 207 380 210 Q384 213 388 210' fill='none' stroke='#333333' stroke-width='2'/>
<g fill='#d9a400'>
<circle cx='364' cy='181' r='3'/><circle cx='372' cy='177' r='3'/><circle cx='380' cy='175' r='3'/><circle cx='388' cy='177' r='3'/><circle cx='396' cy='181' r='3'/>
</g>
<path d='M406 188 Q410 195 406 198 Q402 195 406 188 Z' fill='#3b5592'/>
<path d='M354 190 Q358 197 354 200 Q350 197 354 190 Z' fill='#3b5592'/>
<polygon points='40,90 62,90 50,276' fill='#ffffff' stroke='#14213d'/>
<rect x='15' y='30' width='230' height='62' rx='14' fill='#ffffff' stroke='#14213d'/>
<text x='130' y='56' text-anchor='middle' font-size='13' fill='#14213d'>Emissionshandel aussetzen –</text>
<text x='130' y='78' text-anchor='middle' font-size='13' fill='#14213d'>sonst wandern wir ab!</text>
<polygon points='371,90 389,90 380,166' fill='#ffffff' stroke='#14213d'/>
<rect x='265' y='30' width='230' height='62' rx='14' fill='#ffffff' stroke='#14213d'/>
<text x='380' y='56' text-anchor='middle' font-size='13' fill='#14213d'>Ich halte die Balance …</text>
<text x='380' y='78' text-anchor='middle' font-size='13' fill='#14213d'>irgendwie!</text>
<polygon points='688,90 708,90 700,194' fill='#ffffff' stroke='#14213d'/>
<rect x='515' y='30' width='230' height='62' rx='14' fill='#ffffff' stroke='#14213d'/>
<text x='630' y='56' text-anchor='middle' font-size='13' fill='#14213d'>Wer jetzt bremst, zahlt</text>
<text x='630' y='78' text-anchor='middle' font-size='13' fill='#14213d'>später doppelt!</text>
<line x1='50' y1='306' x2='50' y2='345' stroke='#14213d' stroke-width='5'/>
<line x1='50' y1='345' x2='40' y2='372' stroke='#14213d' stroke-width='4'/>
<line x1='50' y1='345' x2='60' y2='372' stroke='#14213d' stroke-width='4'/>
<line x1='50' y1='318' x2='30' y2='334' stroke='#f2c9a0' stroke-width='4' stroke-linecap='round'/>
<line x1='50' y1='318' x2='84' y2='306' stroke='#f2c9a0' stroke-width='4' stroke-linecap='round'/>
<circle cx='50' cy='292' r='14' fill='#f2c9a0' stroke='#333333' stroke-width='2'/>
<path d='M35 289 Q50 266 65 289 Z' fill='#d9a400' stroke='#6a4b00'/>
<circle cx='45' cy='293' r='2' fill='#333333'/><circle cx='55' cy='293' r='2' fill='#333333'/>
<path d='M44 301 Q50 297 56 301' fill='none' stroke='#333333' stroke-width='2'/>
<line x1='705' y1='306' x2='705' y2='345' stroke='#b5302a' stroke-width='5'/>
<line x1='705' y1='345' x2='695' y2='372' stroke='#14213d' stroke-width='4'/>
<line x1='705' y1='345' x2='715' y2='372' stroke='#14213d' stroke-width='4'/>
<line x1='705' y1='314' x2='680' y2='240' stroke='#f2c9a0' stroke-width='4' stroke-linecap='round'/>
<line x1='705' y1='314' x2='730' y2='240' stroke='#f2c9a0' stroke-width='4' stroke-linecap='round'/>
<rect x='652' y='196' width='96' height='44' fill='#ffffff' stroke='#b5302a' stroke-width='2'/>
<text x='700' y='214' text-anchor='middle' font-size='13' font-weight='bold' fill='#b5302a'>KLIMA-</text>
<text x='700' y='232' text-anchor='middle' font-size='13' font-weight='bold' fill='#b5302a'>SCHUTZ!</text>
<circle cx='705' cy='292' r='14' fill='#f2c9a0' stroke='#333333' stroke-width='2'/>
<circle cx='700' cy='290' r='2' fill='#333333'/><circle cx='710' cy='290' r='2' fill='#333333'/>
<line x1='699' y1='299' x2='711' y2='299' stroke='#333333' stroke-width='2'/>
<text x='50' y='392' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>Industrie</text>
<text x='700' y='392' text-anchor='middle' font-size='12' font-weight='bold' fill='#14213d'>Klimabewegung</text>
<text x='380' y='438' text-anchor='middle' font-size='17' font-weight='bold' fill='#14213d'>„Balanceakt“</text>
</svg>"""

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Freier Markt, kontrollierte Grenzen?“ (2026)",
        "absaetze": [
            "Wer morgens aus dem saarländischen Perl über die Mosel nach Luxemburg zur Arbeit pendelt, kennt das Bild inzwischen: Polizeifahrzeuge am Straßenrand, Absperrkegel auf der Fahrbahn, ein prüfender Blick ins Auto. Und das nur wenige Kilometer von dem Ort entfernt, der dem Schengener Abkommen seinen Namen gab. Seit dem 16. September 2024 kontrolliert die Bundespolizei an allen deutschen Landgrenzen. Was als befristete Maßnahme begann, ist mehrfach verlängert worden; im August 2026 meldete die Bundesregierung in Brüssel eine weitere Verlängerung bis März 2027 an. Für viele Menschen in den Grenzregionen ist der Schlagbaum zurückgekehrt – zumindest im Kopf.",
            "Dabei ist der europäische Binnenmarkt eine Erfolgsgeschichte. Seit 1993 können sich Waren, Dienstleistungen, Kapital und Menschen zwischen den Mitgliedstaaten frei bewegen. Ein Likör, der in Frankreich rechtmäßig verkauft wird, darf grundsätzlich auch in Hessen ins Regal – das hat der Europäische Gerichtshof schon 1979 im berühmten Cassis-de-Dijon-Urteil klargestellt. Für die deutsche Exportwirtschaft ist der Binnenmarkt mit rund 450 Millionen Menschen wichtiger als jeder andere Absatzmarkt: Mehr als die Hälfte ihrer Warenexporte geht in andere EU-Staaten.",
            "Doch fertig ist dieser Markt noch lange nicht. Der Internationale Währungsfonds hat 2024 errechnet, dass die verbliebenen Hürden zwischen den EU-Staaten für Industriegüter wie ein Zoll von rund 44 Prozent wirken, bei manchen Dienstleistungen sogar wie einer von 110 Prozent. Wer als Handwerksbetrieb im Nachbarland arbeiten will, kämpft mit Meldepflichten, Formularen und der Anerkennung von Berufsabschlüssen. Die EU-Kommission hat 2025 die zehn schädlichsten Hindernisse benannt, die sogenannten „Terrible Ten“. Abgebaut sind sie bis heute nicht.",
            "Natürlich darf ein Staat die Grundfreiheiten beschränken, wenn wichtige Gemeinwohlgründe es verlangen: zum Schutz der Gesundheit, der öffentlichen Sicherheit oder der Beschäftigten. Dass entsandte Bauarbeiter seit der Reform der Entsenderichtlinie nach dem Grundsatz „gleicher Lohn für gleiche Arbeit am gleichen Ort“ bezahlt werden müssen, ist eine solche sinnvolle Schranke. Sie schützt vor Lohndumping, ohne den Markt zu schließen. Grenzkontrollen sind etwas anderes. Der Schengener Grenzkodex erlaubt sie nur ausnahmsweise und befristet, bei einer ernsthaften Bedrohung der öffentlichen Ordnung oder der inneren Sicherheit. Das Verwaltungsgericht Koblenz hat im April 2026 eine Kontrolle an der luxemburgischen Grenze für rechtswidrig erklärt, weil die Verlängerung nicht ausreichend begründet worden sei. Der Bund will dagegen in Berufung gehen.",
            "Die Bundesregierung hält die Kontrollen für notwendig, um irreguläre Migration zu begrenzen und Schleuser zu fassen. Das ist ein legitimes Anliegen. Aber der Preis ist hoch: Lastwagen stehen im Stau, Lieferungen verzögern sich, Tausende Polizistinnen und Polizisten sind gebunden, und Nachbarländer antworten mit eigenen Kontrollen – Polen etwa kontrolliert seit Juli 2025 an der Grenze zu Deutschland. Zudem gilt seit Juni 2026 die Reform des Gemeinsamen Europäischen Asylsystems, die die Außengrenzen stärker sichern soll. Wenn die Außengrenzen funktionieren, braucht es keine Schlagbäume im Inneren.",
            "Deutschland sollte die Kontrollen deshalb beenden und durch gemeinsame Streifen mit der Polizei der Nachbarländer und gezielte Kontrollen im Hinterland der Grenze ersetzen. Und Europa sollte den Binnenmarkt endlich vollenden – vor allem bei Dienstleistungen, Energie und Kapital. Wer im Wettbewerb mit den USA und China bestehen will, kann sich keine Grenzen im Inneren leisten, weder auf der Straße noch in den Amtsstuben.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Wirtschaftsjournalistin (2026). Die genannten Ereignisse und Zahlen sind real (Stand: Oktober 2026): IWF, Regional Economic Outlook Europe (Oktober 2024); VG Koblenz, Urteil vom 27.04.2026 (nicht rechtskräftig); Anmeldung der Verlängerung der Binnengrenzkontrollen bis 15.03.2027 (August 2026).",
    },
    {
        "id": "m2",
        "titel": "M2: Haushaltsdefizite und Staatsschulden ausgewählter EU-Staaten 2024 und 2025 (in % des BIP)",
        "typ": "tabelle",
        "kopf": ["Staat", "Finanzierungssaldo 2024", "Finanzierungssaldo 2025", "Schuldenstand 2024", "Schuldenstand 2025", "Defizitverfahren (Stand: Juli 2026)"],
        "zeilen": [
            ["Deutschland", "−2,7", "−2,9", "61,4", "62,8", "nein"],
            ["Frankreich", "−5,8", "−5,1", "112,6", "115,7", "ja (seit 2024)"],
            ["Italien", "−3,4", "−3,1", "134,3", "136,7", "ja (seit 2024)"],
            ["Griechenland", "+1,4", "+2,0", "153,5", "145,4", "nein"],
            ["Spanien", "−3,2", "−2,4", "101,4", "100,5", "nein"],
            ["Belgien", "−4,4", "−5,2", "104,0", "108,1", "ja (seit 2024)"],
            ["Österreich", "−4,6", "−4,1", "79,0", "80,7", "ja (seit 2025)"],
            ["Finnland", "−4,4", "−3,8", "82,5", "88,4", "ja (seit 2026)"],
            ["Polen", "−6,4", "−7,2", "54,8", "59,6", "ja (seit 2024)"],
            ["Niederlande", "−0,7", "−1,6", "44,0", "44,7", "nein"],
            ["Irland", "+4,2", "+1,8", "38,4", "34,8", "nein"],
            ["Euroraum (20 Staaten)", "−3,0", "−3,0", "86,6", "87,7", "–"],
            ["EU (27 Staaten)", "−3,1", "−3,1", "80,3", "81,5", "–"],
            ["Referenzwerte des Stabilitäts- und Wachstumspakts", "−3,0", "−3,0", "60,0", "60,0", "–"],
        ],
        "quelle": "Eurostat, Euro-Indikatoren vom 21. Oktober 2026 (Daten der zweiten Meldung 2026, gerundet). Finanzierungssaldo: negativer Wert = Defizit, positiver Wert = Überschuss. Euroraum ohne das 2026 beigetretene Bulgarien. Defizitverfahren: Beschlüsse des Rates der EU vom 26.07.2024, 08.07.2025 und 20.01.2026; außerdem liefen im Juli 2026 Verfahren gegen Bulgarien, Rumänien, die Slowakei und Ungarn, das Verfahren gegen Malta wurde im Juni 2026 eingestellt.",
    },
    {
        "id": "m3",
        "typ": "bild",
        "titel": "M3: Karikatur „Balanceakt“ (2026)",
        "svg": SVG_KARIKATUR,
        "beschreibung": "Die Karikatur zeigt eine große Wippe aus einem grauen Brett, das auf einem dunkelblauen Dreieck in der Bildmitte liegt. Die linke Seite der Wippe ist nach unten gedrückt, die rechte Seite ragt nach oben. Auf der linken, tiefer liegenden Seite stehen zwei schwere Gewichte: ein dunkelblaues mit der Aufschrift 'ENERGIEPREISE' und ein rotes mit der Aufschrift 'ARBEITSPLÄTZE'. Darüber schwebt ein schwarzes Ölfass mit der Aufschrift 'ÖL & GAS – Iran-Krieg 2026'; ein roter Pfeil zeigt vom Fass nach unten auf das Gewicht 'Energiepreise'. Auf der rechten, hochgehobenen Seite der Wippe liegt ein hellblaues, leichteres Gewicht mit der Aufschrift 'KLIMAZIEL 2040: -90 %'. Genau über dem Drehpunkt steht eine Frauenfigur in einem dunkelblauen Kleid mit der Aufschrift 'EU'; über ihrem Kopf schweben fünf goldene Sterne wie eine Krone. Sie hält mit ausgestreckten Armen eine lange Balancierstange, schaut besorgt und hat Schweißtropfen auf der Stirn. Ihre Sprechblase lautet: 'Ich halte die Balance … irgendwie!'. Ganz links neben dem tiefen Ende der Wippe steht ein Mann mit gelbem Schutzhelm, beschriftet als 'Industrie'. Er zeigt auf die Wippe; seine Sprechblase lautet: 'Emissionshandel aussetzen – sonst wandern wir ab!'. Ganz rechts steht eine junge Person in rotem Oberteil, beschriftet als 'Klimabewegung', die ein Schild mit der Aufschrift 'KLIMASCHUTZ!' hochhält. Ihre Sprechblase lautet: 'Wer jetzt bremst, zahlt später doppelt!'. Unter dem Bild steht der Titel 'Balanceakt'.",
        "quelle": "Übungsmaterial: eigene Zeichnung für Feibitur (2026).",
    },
]

AUFGABEN = [
    {
        "id": "q4-2-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Kommentar), Titel „Freier Markt, kontrollierte Grenzen?“, Erscheinungsjahr (2026), Autorin (fiktive Wirtschaftsjournalistin) und Thema (Binnenmarkt zwischen Grundfreiheiten und Binnengrenzkontrollen; Forderung nach Ende der Kontrollen und Vollendung des Binnenmarktes).",
            "punkte": [
                "Die Autorin beschreibt die seit dem 16. September 2024 an allen deutschen Landgrenzen durchgeführten Kontrollen, die mehrfach verlängert und im August 2026 bis März 2027 angemeldet worden seien; für Pendlerinnen und Pendler in den Grenzregionen sei der „Schlagbaum“ zurückgekehrt, ausgerechnet nahe dem Ort Schengen [1].",
                "Der Binnenmarkt sei eine Erfolgsgeschichte: seit 1993 freier Verkehr von Waren, Dienstleistungen, Kapital und Personen; das Cassis-de-Dijon-Urteil (1979) habe festgelegt, dass in einem Mitgliedstaat rechtmäßig verkaufte Produkte grundsätzlich überall verkauft werden dürfen; für die deutsche Exportwirtschaft sei er der wichtigste Absatzmarkt (rund 450 Mio. Menschen, mehr als die Hälfte der Warenexporte) [2].",
                "Der Binnenmarkt sei aber unvollendet: Nach dem IWF wirkten die Hürden wie ein Zoll von rund 44 % bei Industriegütern und bis zu 110 % bei manchen Dienstleistungen; Betriebe kämpften mit Meldepflichten und der Anerkennung von Abschlüssen; die 2025 benannten „Terrible Ten“ seien nicht abgebaut [3].",
                "Beschränkungen der Grundfreiheiten aus Gemeinwohlgründen seien legitim, etwa die reformierte Entsenderichtlinie („gleicher Lohn für gleiche Arbeit am gleichen Ort“) gegen Lohndumping; Grenzkontrollen erlaube der Schengener Grenzkodex dagegen nur ausnahmsweise und befristet; das VG Koblenz habe eine Kontrolle im April 2026 wegen unzureichender Begründung für rechtswidrig erklärt, der Bund wolle in Berufung gehen [4].",
                "Das Ziel der Bundesregierung, irreguläre Migration zu begrenzen, sei legitim, die Kosten aber hoch: Staus, Lieferverzögerungen, gebundene Polizeikräfte, Gegenreaktionen der Nachbarn (Polen seit Juli 2025); die seit Juni 2026 geltende GEAS-Reform sichere die Außengrenzen, sodass Binnenkontrollen überflüssig würden [5].",
                "Die Autorin fordert, die Kontrollen durch gemeinsame Streifen und gezielte Kontrollen im Hinterland zu ersetzen und den Binnenmarkt bei Dienstleistungen, Energie und Kapital zu vollenden, um im Wettbewerb mit den USA und China zu bestehen [6].",
            ],
            "hinweis": "Zusammenfassen verlangt einen Einleitungssatz sowie eine strukturierte, komprimierte Wiedergabe in eigenen Worten und in indirekter Rede, ohne eigene Wertung. Die Argumentationsstruktur (Problemaufriss – Erfolg des Binnenmarktes – Defizite – legitime und illegitime Schranken – Gegenposition – Forderung) sollte erkennbar werden; Fachbegriffe (Grundfreiheiten, Schengener Grenzkodex, Entsenderichtlinie) sind korrekt zu verwenden.",
        },
        "bewertung": {
            "ausreichend": "die zentralen Aussagen des Kommentars im Ansatz korrekt und mit Einleitungssatz zusammengefasst werden.",
            "gut": "die Aussagen weitgehend vollständig, strukturiert, fachsprachlich präzise und in indirekter Rede zusammengefasst werden und die Argumentationsstruktur des Kommentars deutlich wird.",
        },
    },
    {
        "id": "q4-2-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die in M2 dargestellte Haushaltslage ausgewählter EU-Staaten.",
        "material": ["m2"],
        "loesung": {
            "vorbemerkung": "Einleitung: Tabelle nach Eurostat (Euro-Indikatoren vom 21.10.2026) zu Finanzierungssaldo und Schuldenstand 2024 und 2025 in % des BIP für elf EU-Staaten, den Euroraum (20 Staaten) und die EU sowie zum Stand der Defizitverfahren (Juli 2026); Referenzwerte des Stabilitäts- und Wachstumspakts zum Vergleich.",
            "punkte": [
                "Gesamtbild: Der Euroraum weist 2024 und 2025 ein Defizit von 3,0 % auf, also genau den Referenzwert, die EU von 3,1 %; die Schuldenquoten steigen (Euroraum von 86,6 auf 87,7 %, EU von 80,3 auf 81,5 %) und liegen deutlich über 60 %.",
                "Hohe Defizite haben 2025 vor allem Polen (−7,2 %, steigend), Belgien (−5,2 %, steigend), Frankreich (−5,1 %, sinkend) und Österreich (−4,1 %); Finnland liegt mit −3,8 % ebenfalls darüber, Italien mit −3,1 % knapp.",
                "Überschüsse erzielen Griechenland (+1,4 auf +2,0 %) und Irland (+4,2 auf +1,8 %); unter 3 % bleiben außerdem Deutschland (−2,9 %, leicht steigend), Spanien (−2,4 %, sinkend) und die Niederlande (−1,6 %).",
                "Schuldenstände über 100 % des BIP: Griechenland (145,4 %, deutlich sinkend von 153,5 %), Italien (136,7 %), Frankreich (115,7 %), Belgien (108,1 %) und Spanien (100,5 %); unter 60 % liegen Polen (59,6 %, stark steigend), die Niederlande (44,7 %) und Irland (34,8 %); Deutschland liegt mit 62,8 % knapp darüber.",
                "Ein Defizitverfahren läuft gegen Frankreich, Italien, Belgien und Polen (seit 2024), Österreich (seit 2025) und Finnland (seit 2026), nicht dagegen gegen Deutschland, Griechenland, Spanien, die Niederlande und Irland.",
            ],
            "hinweis": "Beschreiben verlangt eine strukturierte, fachsprachliche Darstellung mit Zahlenbelegen (Gesamtbild, Auffälligkeiten, Entwicklungen). Defizit (Stromgröße eines Jahres) und Schuldenstand (Bestandsgröße) sind sauber zu unterscheiden. Erklärungen und Bewertungen gehören nicht in diese Aufgabe.",
        },
        "bewertung": {
            "ausreichend": "zentrale Daten zu Defiziten, Schuldenständen und Defizitverfahren im Ansatz korrekt und mit einigen Zahlenbelegen beschrieben werden.",
            "gut": "die Haushaltslage strukturiert, fachsprachlich präzise und mit treffenden Zahlenbelegen beschrieben wird, wobei Gesamtbild, Extremwerte und Entwicklungen zwischen 2024 und 2025 deutlich werden.",
        },
    },
    {
        "id": "q4-2-i3",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Karikatur (M3).",
        "material": ["m3"],
        "loesung": {
            "vorbemerkung": "Einleitung: Karikatur „Balanceakt“ (2026, eigene Zeichnung), Thema: Spannungsverhältnis zwischen Energiepreisen bzw. Wirtschaft und Klimaschutz in der EU während des Energiepreisschocks 2026.",
            "punkte": [
                "Bildmitte: Wippe auf einem Drehpunkt; darauf balanciert eine Frauenfigur mit EU-Aufschrift und goldenen Sternen über dem Kopf, mit Balancierstange, besorgtem Gesicht und Schweißtropfen; Sprechblase „Ich halte die Balance … irgendwie!“.",
                "Linke Seite der Wippe nach unten gedrückt durch die Gewichte „Energiepreise“ und „Arbeitsplätze“; darüber ein Ölfass „Öl & Gas – Iran-Krieg 2026“, von dem ein roter Pfeil auf das Gewicht „Energiepreise“ zeigt.",
                "Rechte Seite der Wippe angehoben, darauf ein leichteres Gewicht „Klimaziel 2040: −90 %“.",
                "Links ein Mann mit Schutzhelm („Industrie“) mit der Forderung „Emissionshandel aussetzen – sonst wandern wir ab!“.",
                "Rechts eine junge Person („Klimabewegung“) mit dem Schild „Klimaschutz!“ und der Aussage „Wer jetzt bremst, zahlt später doppelt!“; Titel „Balanceakt“.",
            ],
            "hinweis": "Beschreiben einer Karikatur: Einleitung sowie präzise, geordnete Wiedergabe der Bildelemente (Figuren, Gegenstände, Beschriftungen, Anordnung, Sprechblasen) ohne Deutung. Eine Gliederung vom Zentrum nach außen oder von links nach rechts erleichtert die Struktur.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Bildelemente und Beschriftungen im Ansatz korrekt und geordnet beschrieben werden.",
            "gut": "alle wesentlichen Bildelemente, ihre Anordnung und die Beschriftungen präzise, strukturiert und ohne vorgreifende Deutung beschrieben werden.",
        },
    },
    {
        "id": "q4-2-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 die Schranken der Grundfreiheiten im europäischen Binnenmarkt sowie die Strategien der Harmonisierung und der gegenseitigen Anerkennung.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Grundfreiheiten (Art. 26 und 28 ff. AEUV): freier Verkehr von Waren, Personen, Dienstleistungen und Kapital; verboten sind Zölle, mengenmäßige Beschränkungen und Maßnahmen gleicher Wirkung (Dassonville-Formel) sowie Diskriminierungen und ungerechtfertigte Beschränkungen [2], [3].",
                "Geschriebene Rechtfertigungsgründe: z. B. Art. 36 AEUV (öffentliche Sittlichkeit, Ordnung, Sicherheit, Schutz der Gesundheit, Kulturgut), Art. 45 Abs. 3 und 4 (öffentliche Ordnung, Sicherheit, Gesundheit; öffentliche Verwaltung), Art. 52, Art. 65 AEUV; ungeschriebene „zwingende Erfordernisse“ des Allgemeininteresses seit Cassis (Verbraucher-, Umwelt-, Arbeitnehmerschutz, Lauterkeit des Handels), grundsätzlich nur für unterschiedslos geltende Regeln.",
                "Verhältnismäßigkeit als Schranken-Schranke: geeignet, erforderlich, angemessen; keine willkürliche Diskriminierung oder verschleierte Handelsbeschränkung.",
                "Beispiele aus M1: Entsenderichtlinie als gerechtfertigte Schranke der Dienstleistungsfreiheit zum Schutz der Beschäftigten [4]; Binnengrenzkontrollen als Beschränkung des freien Personenverkehrs, nach dem Schengener Grenzkodex nur ausnahmsweise, befristet und bei ernsthafter Bedrohung zulässig; das VG Koblenz sah die Begründung als unzureichend an [1], [4], [5].",
                "Gegenseitige Anerkennung: Cassis-de-Dijon-Urteil 1979 – deutsches Mindestalkoholgebot unverhältnismäßig, Etikettierung als milderes Mittel; Grundsatz, dass rechtmäßig in einem Mitgliedstaat vertriebene Waren grundsätzlich überall vertrieben werden dürfen (auch Reinheitsgebot-Urteil 1987); Vorteile (schnell, Vielfalt) und Risiken (Unterbietung von Standards, Inländerdiskriminierung) [2].",
                "Harmonisierung: gemeinsame EU-Regeln nach Art. 114 AEUV, Neue Konzeption mit grundlegenden Anforderungen, europäischen Normen und CE-Kennzeichen, Beispiel USB-C-Ladekabel; einheitliches Schutzniveau, aber langwierig und mit Souveränitätsverlust verbunden; beide Strategien ergänzen sich und sollen die in [3] genannten Hürden (IWF-Schätzung, „Terrible Ten“) abbauen.",
            ],
            "hinweis": "Erläutern verlangt, die Schranken und Strategien mit zusätzlichen Informationen und Beispielen zu veranschaulichen. Erwartet werden Materialbezüge (v. a. [2]–[5]) und Fachwissen über das Material hinaus (Rechtfertigungsgründe, Verhältnismäßigkeit, Cassis-Fall). Eine bloße Aufzählung der Grundfreiheiten genügt nicht.",
        },
        "bewertung": {
            "ausreichend": "Schranken der Grundfreiheiten sowie Harmonisierung und gegenseitige Anerkennung im Ansatz zutreffend und mit Bezug zu M1 erläutert werden.",
            "gut": "Rechtfertigungsgründe, Verhältnismäßigkeit und beide Strategien differenziert, fachlich präzise und mit treffenden Beispielen aus M1 und darüber hinaus erläutert werden.",
        },
    },
    {
        "id": "q4-2-ii2",
        "afb": "II",
        "operator": "auswerten",
        "text": "Werten Sie M2 im Hinblick auf die Frage aus, inwieweit die EU-Staaten die europäischen Fiskalregeln einhalten.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Maßstab: Referenzwerte des Stabilitäts- und Wachstumspakts (Defizit höchstens 3 %, Schuldenstand höchstens 60 % des BIP oder hinreichend rückläufig); seit der Reform 2024 länderspezifische Nettoausgabenpfade; das Defizitverfahren knüpft in der Praxis vor allem am Defizitkriterium an.",
                "Gesamtaussage: Die Regeln werden von vielen Staaten nicht eingehalten – im Durchschnitt liegt der Euroraum genau an der Defizitgrenze (3,0 %) und mit fast 88 % Schuldenquote weit über dem Schuldenkriterium; sechs der elf aufgeführten Staaten befinden sich im Defizitverfahren.",
                "Gruppenbildung: (a) Staaten mit klarer Überschreitung des Defizitkriteriums und Verfahren (Polen, Belgien, Frankreich, Österreich, Finnland; Italien knapp); (b) hoch verschuldete Staaten, die konsolidieren (Griechenland mit Überschüssen und sinkender Quote, Spanien, Italien mit sinkendem Defizit); (c) Staaten innerhalb oder nahe der Regeln (Niederlande, Irland, Deutschland).",
                "Auffälligkeiten: Griechenland verfehlt das Schuldenkriterium deutlich, ist aber wegen seiner Überschüsse nicht im Verfahren – das Schuldenkriterium wirkt weniger bindend; Spanien lag 2024 knapp über 3 % ohne Verfahren (nur geringfügige, vorübergehende Überschreitung); Polen verschlechtert sich stark (u. a. hohe Verteidigungsausgaben; Bezug zur nationalen Ausweichklausel möglich).",
                "Deutschland hält das Defizitkriterium knapp ein (2,9 %), überschreitet aber den Schuldenreferenzwert leicht und steigend – trotz Lockerung der Schuldenbremse 2025 Spielraum vor allem über die Ausweichklausel für Verteidigung (Bezug Q2.1/Q2.5).",
                "Fazit: Die Regeln wirken eher als Orientierungsrahmen mit Korrekturpfaden als als harte Grenze; Durchsetzung über Verfahren und Empfehlungen, Geldbußen wurden nie verhängt; Flexibilität durch Ausweichklauseln (Verteidigung, seit 2026 Energiesicherheit).",
            ],
            "hinweis": "Auswerten verlangt, die Daten zu einer begründeten Gesamtaussage zusammenzuführen. Erwartet werden der ausdrückliche Bezug auf die Referenzwerte, die Bildung von Ländergruppen, der Abgleich mit dem Status der Defizitverfahren und präzise Zahlenbelege. Eine bloße Wiederholung der Beschreibung aus AFB I reicht nicht aus.",
        },
        "bewertung": {
            "ausreichend": "die Daten im Ansatz mit den Referenzwerten abgeglichen und zu einer nachvollziehbaren Gesamtaussage geführt werden.",
            "gut": "die Daten kriteriengeleitet, mit Ländergruppen, Auffälligkeiten und Zahlenbelegen ausgewertet werden und in eine differenzierte, schlüssige Gesamtaussage über die Wirksamkeit der Fiskalregeln münden.",
        },
    },
    {
        "id": "q4-2-ii3",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Karikatur (M3) im Hinblick auf das Spannungsverhältnis zwischen Wirtschafts- und Umweltpolitik in der Energiepreiskrise 2026.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Deutung der Bildelemente: Wippe als Metapher für einen Zielkonflikt; Europa/EU als überforderte Akteurin, die zwei Ziele zugleich halten will (Schweißtropfen, „irgendwie“); Gewichte „Energiepreise“ und „Arbeitsplätze“ für Wettbewerbsfähigkeit und soziale Folgen; „Klimaziel 2040: −90 %“ als leichteres, nach oben gedrücktes Gewicht; Ölfass als externer Schock, der das Gleichgewicht verschiebt.",
                "Kontext: Iran-Krieg seit Ende Februar 2026, Störung der Schifffahrt durch die Straße von Hormus, stark steigende Öl- und Gaspreise, Inflation im Euroraum 3,8 % im September 2026; EU-Antworten: AccelerateEU (April 2026), befristeter Beihilferahmen, Ausweichklausel für Energiesicherheit (August 2026).",
                "Spannungsverhältnis: Wirtschaftspolitik (Kostenentlastung, Wettbewerbsfähigkeit, Arbeitsplätze, Gefahr der Abwanderung/Carbon Leakage) gegen Umweltpolitik (Klimaziel 2040 von −90 %, beschlossen im März 2026; Emissionshandel als Kerninstrument; ETS2 ab 2028).",
                "Akteure und Interessen: Industrie (Forderung nach Aussetzung des ETS, Brief von zehn Mitgliedstaaten im März 2026, Italien forderte eine Aussetzung), Klimabewegung und Umweltverbände (Kosten späteren Handelns, Glaubwürdigkeit, Generationengerechtigkeit), Kommission/EU (Ausgleich durch ETS-Reformvorschlag vom Juli 2026, Entlastungen, Ausbau erneuerbarer Energien).",
                "Gestaltungsmittel: Gewichtung und Neigung der Wippe, Zuspitzung durch Sprechblasen, Ironie in der Aussage der EU-Figur, Farbsymbolik (Rot für Arbeitsplätze und Klimaschutz-Schild als Warnsignale).",
                "Aussage/Intention: skeptisch-ironische Sicht auf die Fähigkeit der EU, Klimaschutz und Wettbewerbsfähigkeit gleichzeitig zu sichern; der äußere Schock droht die Balance zulasten des Klimaschutzes zu kippen; zugleich Hinweis, dass ein Aufschieben teurer werden könnte – die Karikatur ergreift nicht eindeutig Partei.",
            ],
            "hinweis": "Analysieren verlangt eine kriteriengeleitete Erschließung: Deutung der Bildelemente, Einordnung in den politischen Kontext, Benennung des Spannungsverhältnisses zweier Politikfelder und Herausarbeitung der Aussage. Kontextwissen zum Energiepreisschock 2026 und zum Emissionshandel ist erforderlich.",
        },
        "bewertung": {
            "ausreichend": "die Karikatur ansatzweise gedeutet und das Spannungsverhältnis zwischen Wirtschafts- und Umweltpolitik im Ansatz zutreffend herausgestellt wird.",
            "gut": "die Bildelemente schlüssig gedeutet, in den Kontext des Energiepreisschocks 2026 eingeordnet und Akteure, Zielkonflikt sowie Aussage der Karikatur differenziert analysiert werden.",
        },
    },
    {
        "id": "q4-2-ii4",
        "afb": "II",
        "operator": "erläutern",
        "lk": True,
        "text": "Erläutern Sie Ziele und Instrumente der Außenwirtschaftspolitik der EU (Zoll- und Handelspolitik sowie Währungspolitik) am Beispiel der Handelsbeziehungen zu den USA und zum Mercosur seit 2025.",
        "material": [],
        "loesung": {
            "punkte": [
                "Zuständigkeit und Verfahren: Zollunion und gemeinsame Handelspolitik als ausschließliche Zuständigkeiten (Art. 3 Abs. 1, Art. 207 AEUV); Mandat des Rates, Verhandlung durch die Kommission, Beschluss des Rates (meist qualifizierte Mehrheit), Zustimmung des Europäischen Parlaments; gemischte Abkommen nach dem Gutachten 2/15 und daraus folgende Aufteilung der Abkommen.",
                "Ziele: Marktzugang und Wohlstand für eine exportstarke Union, Diversifizierung der Handelspartner, Schutz vor unfairen Praktiken und Erpressung (strategische Autonomie), Durchsetzung eigener Standards.",
                "Zollpolitik: Gemeinsamer Zolltarif, Zolleinnahmen als EU-Eigenmittel; aktuelle Beispiele: Abschaffung der Zollfreigrenze von 150 € für Kleinsendungen (pauschal 3 € seit Juli 2026), Abschaffung der Zölle auf US-Industriegüter seit 1. Juli 2026 mit Aussetzungsklausel und Befristung bis Ende 2029.",
                "Handelsbeziehungen zu den USA: Handelsvolumen bei Waren 910,6 Mrd. € (2025) mit EU-Überschuss, Defizit bei Dienstleistungen; Turnberry-Vereinbarung (Juli 2025) mit US-Zollobergrenze von 15 %; Grönland-Drohung im Januar 2026, Stopp der Umsetzung durch das Parlament, Debatte über das Anti-Coercion-Instrument; vorbereitete, aber ausgesetzte Gegenzölle als Druckmittel; seit Juli 2026 neue US-Zölle nach Section 301 mit Obergrenze von 10 % für die meisten EU-Waren (Sonderzölle auf Stahl, Aluminium, Autos bleiben).",
                "Mercosur: Freihandelsabkommen mit Zollabbau für über 90 % des Handels; Ratsbeschluss mit qualifizierter Mehrheit gegen fünf Staaten (u. a. Frankreich) im Januar 2026; Prüfung durch den EuGH auf Antrag des Parlaments; vorläufige Anwendung des Handelsteils seit 1. Mai 2026; Schutzklauseln für die Landwirtschaft – Diversifizierung als Antwort auf den Konflikt mit den USA.",
                "Weitere Instrumente: Handelsschutz (Antidumping- und Ausgleichszölle, z. B. auf chinesische Elektroautos seit 2024), Anti-Coercion-Instrument (2023, bisher nicht angewandt).",
                "Währungspolitik: Euro als zweitwichtigste Reservewährung (rund 20 % gegenüber knapp 57 % für den Dollar, Ende 2025) und Fakturierungswährung (60 % der Warenexporte aus dem Euroraum in Drittstaaten 2025) mindert Wechselkursrisiken im Handelskonflikt; Wechselkurspolitik nach Art. 219 AEUV ohne Wechselkursziele, EZB vorrangig der Preisstabilität verpflichtet; eine Aufwertung des Euro kann Exporte zusätzlich belasten; digitaler Euro und Kapitalmarktunion als Bausteine strategischer Autonomie.",
            ],
            "hinweis": "Erläutern auf LK-Niveau verlangt, Ziele und Instrumente systematisch darzustellen und an den Beispielen USA und Mercosur zu veranschaulichen. Erwartet wird, dass der Zusammenhang zwischen Zuständigkeitsordnung und Handlungsfähigkeit der EU deutlich wird. Exakte Zahlen sind nicht zwingend, die Größenordnungen und Abläufe sollten stimmen.",
        },
        "bewertung": {
            "ausreichend": "zentrale Ziele und Instrumente der EU-Außenwirtschaftspolitik im Ansatz zutreffend erläutert und auf mindestens eines der Beispiele bezogen werden.",
            "gut": "Zuständigkeiten, Ziele sowie zoll-, handels- und währungspolitische Instrumente differenziert, fachlich präzise und an beiden Beispielen veranschaulicht erläutert werden.",
        },
    },
    {
        "id": "q4-2-iii1",
        "afb": "III",
        "operator": "Stellung nehmen",
        "text": "Nehmen Sie Stellung zu der Forderung der Autorin, die Kontrollen an den deutschen Binnengrenzen zu beenden (M1).",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Klärung der Forderung [6] und des Rahmens: Personenfreizügigkeit und Schengen-Besitzstand; Binnengrenzkontrollen nach dem Schengener Grenzkodex nur als letztes Mittel, befristet und verhältnismäßig (Reform 2024 mit Höchstfristen); Offenlegung eigener Wertmaßstäbe, z. B. Freiheit, Sicherheit, Rechtsstaatlichkeit, wirtschaftliche Effizienz, europäische Solidarität.",
                "Argumente für ein Ende: Symbol und Kern der Integration (Schengen) [1]; wirtschaftliche Kosten für Pendler, Logistik und Lieferketten [5]; Zweifel an der Rechtmäßigkeit (VG Koblenz April 2026, VG Berlin 2025 zu Zurückweisungen) [4]; Dominoeffekt durch Gegenkontrollen (Polen) [5]; gebundene Polizeikräfte; GEAS-Reform seit Juni 2026 stärkt die Außengrenzen [5]; Alternativen wie gemeinsame Streifen und Kontrollen im Hinterland [6].",
                "Argumente für eine Fortsetzung: Steuerung irregulärer Migration und Bekämpfung von Schleuserkriminalität; Sicherheitslage (Terrorgefahr); Wirksamkeit der GEAS-Reform noch nicht erwiesen; Kontrollen sind stichprobenartig und keine Grenzschließung; Rechtslage nicht abschließend geklärt (erstinstanzliches Urteil, Berufung); politische Akzeptanz und Vertrauen in staatliche Handlungsfähigkeit.",
                "Abwägung: Verhältnis von Nutzen (Aufgriffe, Signalwirkung) und Kosten (Wirtschaft, Grundfreiheiten, Vertrauen der Nachbarn); Bedeutung der europäischen Rechtsordnung; Möglichkeit von Zwischenlösungen (schrittweiser Abbau, Evaluation, gezielte statt flächendeckender Kontrollen, enge Abstimmung mit Nachbarstaaten).",
                "Begründetes eigenes Urteil mit ausdrücklich benannten Maßstäben; beide Ergebnisse sind möglich, wenn schlüssig begründet.",
            ],
            "hinweis": "Stellung nehmen verlangt wie Beurteilen eine kriteriengeleitete, begründete Einschätzung, zusätzlich aber die Darlegung der eigenen Wertmaßstäbe. Materialbezüge (v. a. [1], [4]–[6]) und Fachwissen zum Schengen-Raum und zu den Grundfreiheiten sind zu erwarten. Gemäß Beutelsbacher Konsens ist keine bestimmte Position vorgegeben.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Position mit einigen Pro- und Kontra-Argumenten und erkennbaren Maßstäben formuliert wird.",
            "gut": "die Stellungnahme abwägend, fachlich fundiert und materialgestützt ist, die eigenen Wertmaßstäbe offengelegt werden und das Urteil schlüssig aus der Abwägung folgt.",
        },
    },
    {
        "id": "q4-2-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie, ob die europäischen Fiskalregeln die finanzpolitische Souveränität der Mitgliedstaaten zu stark einschränken. (M2)",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien, z. B. demokratische Legitimation (Budgetrecht als „Königsrecht“ der Parlamente), Stabilität der Währungsunion, Handlungsfähigkeit in Krisen und bei Investitionen, Generationengerechtigkeit.",
                "Für eine zu starke Einschränkung: Kommission und Rat überwachen Haushalte (Europäisches Semester, Nettoausgabenpfade, Defizitverfahren); Sparvorgaben können prozyklisch wirken (Erfahrung der Eurokrise); großer Investitionsbedarf (Klima, Verteidigung, Infrastruktur); Referenzwerte 3 % und 60 % gelten als ökonomisch willkürlich; viele Staaten verfehlen sie (M2), was gegen ihre Realitätsnähe spricht.",
                "Gegen eine zu starke Einschränkung: In der Währungsunion haben unsolide Staatsfinanzen Folgen für alle (Zinsen, Ansteckung, Rettungsdruck trotz No-bail-out-Klausel); die Staaten haben die Regeln selbst beschlossen (gebündelte statt verlorene Souveränität); die Regeln wurden 2024 flexibilisiert (länderspezifische Pfade über vier bis sieben Jahre) und durch Ausweichklauseln für Verteidigung und Energie ergänzt; Geldbußen wurden nie verhängt; M2 zeigt große faktische Spielräume (Frankreich mit 5,1 % Defizit und 115,7 % Schulden, Polen mit 7,2 %).",
                "Materialbelege aus M2: Durchschnitt des Euroraums genau an der Defizitgrenze und weit über dem Schuldenkriterium; Konsolidierungserfolg Griechenlands; Deutschland innerhalb des Defizitkriteriums.",
                "Bezug zu Q2.1: Kontroverse um Staatsverschuldung (Zinslast, Crowding-out, Inflationsgefahr gegenüber keynesianischer Stabilisierung und investitionsorientierter „goldener Regel“).",
                "Begründetes Urteil, z. B.: formal deutliche Bindung, faktisch eher schwache Durchsetzung; Problem eher die Glaubwürdigkeit als ein Übermaß an Kontrolle – oder umgekehrt.",
            ],
            "hinweis": "Beurteilen verlangt eine kriteriengeleitete, begründete Einschätzung auf Basis von Fachwissen und Material. Erwartet werden explizite Kriterien, eine Abwägung mit Materialbelegen aus M2 und ein klares Urteil. Bezüge zur Staatsverschuldungsdebatte (Q2.1) sind erwünscht.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einigen zutreffenden Argumenten und Bezügen zu M2 formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, fachlich fundiert und durch Belege aus M2 gestützt ist und schlüssig begründet wird.",
        },
    },
    {
        "id": "q4-2-iii3",
        "afb": "III",
        "operator": "erörtern",
        "text": "Erörtern Sie, ob die EU in Energiepreiskrisen ihre Klimaschutzinstrumente, insbesondere den Emissionshandel, lockern sollte. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Problemstellung: Spannungsverhältnis zwischen Wirtschafts- und Sozialpolitik (Energiepreise, Arbeitsplätze, Wettbewerbsfähigkeit) und Umweltpolitik (Klimaziele 2030/2040, Emissionshandel) im Energiepreisschock 2026, wie in M3 zugespitzt.",
                "Pro Lockerung: Entlastung von Unternehmen und Haushalten; Schutz vor Abwanderung (Carbon Leakage) und Arbeitsplatzverlusten; Wettbewerbsfähigkeit gegenüber den USA und China (Draghi-Bericht); soziale Akzeptanz der Klimapolitik, besonders mit Blick auf das ETS2 ab 2028; Ziele bleiben bestehen, nur der Pfad wird flexibler (Reformvorschlag Juli 2026); Forderungen mehrerer Mitgliedstaaten.",
                "Contra Lockerung: Glaubwürdigkeit und Planungssicherheit für klimafreundliche Investitionen; die Abhängigkeit von fossilen Importen ist Ursache der Krise – Elektrifizierung und erneuerbare Energien senken langfristig Preise und Erpressbarkeit (AccelerateEU); Kosten des Klimawandels und zusätzlicher Emissionen (Schätzungen von Umweltverbänden); ETS-Einnahmen können zur gezielten Entlastung genutzt werden; ungezielte Hilfen heizen Inflation an (Mahnung der EZB); Vorreiterrolle der EU in der internationalen Klimapolitik (Bezug Q4.3).",
                "Differenzierte Lösungen: Preisstabilisierungsmechanismen (Marktstabilitätsreserve, Freigabe zusätzlicher Zertifikate bei hohen ETS2-Preisen), Klima-Sozialfonds und Rückverteilung, Strompreiskompensation und befristete, zielgenaue Beihilfen statt Aussetzung des Systems.",
                "Abwägung nach Kriterien (Effektivität, Effizienz, soziale Gerechtigkeit, Generationengerechtigkeit, Legitimität) und eigenes, begründetes Urteil.",
            ],
            "hinweis": "Erörtern verlangt, die Problemstellung unter Abwägung von Pro- und Kontra-Argumenten zu hinterfragen und zu einem eigenen Urteil zu gelangen. Der Bezug zu M3 (Spannungsverhältnis, Akteure) und Fachwissen zum Emissionshandel und zum Energiepreisschock 2026 sind zu erwarten. Gemäß Beutelsbacher Konsens sind unterschiedliche Urteile möglich.",
        },
        "bewertung": {
            "ausreichend": "Pro- und Kontra-Argumente ansatzweise strukturiert abgewogen werden und ein nachvollziehbares Urteil vorliegt.",
            "gut": "die Erörterung strukturiert, fachlich fundiert und kriteriengeleitet ist, differenzierte Lösungsansätze einbezieht und in ein schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q4-2-iii4",
        "afb": "III",
        "operator": "entwerfen",
        "lk": True,
        "text": "Entwerfen Sie eine Rede einer Abgeordneten des Europäischen Parlaments, in der sie begründet darlegt, wie die EU auf künftige Zolldrohungen der USA reagieren sollte.",
        "material": [],
        "loesung": {
            "punkte": [
                "Formale Anforderungen: Redeform mit Anrede, Einstieg (z. B. Bezug auf den Grönland-Streit im Januar 2026), klarer These, Argumentation, Schluss mit Appell; adressatengerechte Sprache (Plenum, Öffentlichkeit), rhetorische Mittel.",
                "Sachliche Grundlage: Bedeutung der Handelsbeziehungen (Warenhandel 910,6 Mrd. € 2025, EU-Überschuss bei Waren, Defizit bei Dienstleistungen); Verlauf des Konflikts (US-Zölle 2025, Turnberry-Vereinbarung mit 15-%-Obergrenze, Zollsenkung der EU seit Juli 2026 mit Aussetzungsklausel, Befristung bis 2029; neue US-Zölle seit Juli 2026 und laufende US-Untersuchung zu Überkapazitäten); Zuständigkeit der EU für Handelspolitik.",
                "Handlungsoptionen: Verhandlungen und Deals (Stabilität, Sicherheitsabhängigkeit von den USA, Interessen exportstarker Branchen); Gegenzölle (vorbereitet, ausgesetzt); Anti-Coercion-Instrument (Abschreckung, Glaubwürdigkeit, Schutz der Souveränität; Entscheidung des Rates mit qualifizierter Mehrheit); WTO-Weg (wegen blockierter Berufungsinstanz begrenzt, Bezug Q3.2); Diversifizierung über Abkommen (Mercosur, Indien); Stärkung von Binnenmarkt und internationaler Rolle des Euro.",
                "Abwägung von Risiken: Eskalation und Zollspirale, Inflation, Arbeitsplätze, Spaltung der Mitgliedstaaten, Glaubwürdigkeit der EU als regelbasierter Akteur.",
                "Eigene, begründete Position mit konkreten Vorschlägen (z. B. abgestufte Reaktion: Verhandlungsangebot plus glaubwürdige Abschreckung, klare rote Linien, Einbindung der Mitgliedstaaten).",
            ],
            "hinweis": "Gestalten/Entwerfen ist eine produktorientierte Aufgabe: Bewertet werden Sachrichtigkeit, Schlüssigkeit der Argumentation, Abwägung von Optionen, Adressatenbezug und Einhaltung der Textsorte. Unterschiedliche Positionen sind zulässig, wenn sie sachlich fundiert und begründet sind.",
        },
        "bewertung": {
            "ausreichend": "eine erkennbare Rede mit einer begründeten Position und einigen sachlich zutreffenden Argumenten und Handlungsoptionen entworfen wird.",
            "gut": "die Rede adressatengerecht und rhetorisch gestaltet ist, mehrere Handlungsoptionen sachkundig abwägt und eine schlüssig begründete Position mit konkreten Vorschlägen entwickelt.",
        },
    },
]
