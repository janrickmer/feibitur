# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q4.3 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = "Q4.3, insbesondere die EU als Akteur kollektiver Konfliktbearbeitung und Friedenssicherung (GASP/GSVP, Einstimmigkeit, Sanktionen, Friedensfazilität, Verhältnis zur NATO) und Europas Beitrag zu einer globalen Klimapolitik; im LK zusätzlich die außenpolitischen Beziehungen Europas zu den USA, China und Russland."

SVG_KARIKATUR = """<svg viewBox='0 0 760 460' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='q43kk'>
<title id='q43kk'>Karikatur Mir nach: Ein Radfahrer im EU-Trikot zieht bergauf einen schweren Anhänger mit der Fahne Green Deal und ruft Mir nach, niemand folgt ihm. Ein Mann mit der Aufschrift Omnibus zieht eine Kiste Berichtspflichten vom Anhänger, eine Figur USA geht zu einem Schild Exit Paris, ein rotes Elektroauto CN fährt unten auf einer Schnellstraße vorbei.</title>
<rect x='0' y='0' width='760' height='460' fill='#fffdf6'/>
<circle cx='70' cy='62' r='28' fill='#fff3cc' stroke='#d9a400' stroke-width='2'/>
<polygon points='0,460 0,410 760,160 760,460' fill='#e7eedb'/>
<line x1='0' y1='410' x2='760' y2='160' stroke='#9a9a9a' stroke-width='14'/>
<line x1='0' y1='448' x2='560' y2='448' stroke='#9a9a9a' stroke-width='10'/>
<line x1='675' y1='118' x2='675' y2='184' stroke='#555' stroke-width='4'/>
<rect x='600' y='70' width='150' height='48' rx='6' fill='#14213d'/>
<text x='675' y='90' text-anchor='middle' font-size='13' font-weight='bold' fill='#ffffff'>Ziel: klimaneutral</text>
<text x='675' y='109' text-anchor='middle' font-size='13' font-weight='bold' fill='#d9a400'>bis 2050</text>
<line x1='318' y1='292' x2='345' y2='272' stroke='#333' stroke-width='3'/>
<rect x='192' y='288' width='128' height='9' fill='#6b4a2b'/>
<circle cx='255' cy='311' r='16' fill='#333'/>
<circle cx='255' cy='311' r='6' fill='#bbbbbb'/>
<rect x='196' y='252' width='58' height='36' fill='#eef2fb' stroke='#14213d' stroke-width='1.5'/>
<text x='225' y='275' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>ETS 2</text>
<rect x='258' y='252' width='58' height='36' fill='#eef2fb' stroke='#14213d' stroke-width='1.5'/>
<text x='287' y='275' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>CBAM</text>
<rect x='204' y='216' width='104' height='36' fill='#fff7e0' stroke='#d9a400' stroke-width='1.5'/>
<text x='256' y='239' text-anchor='middle' font-size='13' font-weight='bold' fill='#6a4b00'>2040: –90 %</text>
<line x1='210' y1='216' x2='210' y2='164' stroke='#333' stroke-width='3'/>
<rect x='210' y='164' width='92' height='24' fill='#2f6b3a'/>
<text x='256' y='181' text-anchor='middle' font-size='12' font-weight='bold' fill='#ffffff'>GREEN DEAL</text>
<circle cx='345' cy='274' r='22' fill='none' stroke='#333' stroke-width='3'/>
<circle cx='418' cy='250' r='22' fill='none' stroke='#333' stroke-width='3'/>
<polygon points='345,274 378,266 370,236' fill='none' stroke='#333' stroke-width='3'/>
<polyline points='370,236 404,228 378,266' fill='none' stroke='#333' stroke-width='3'/>
<line x1='404' y1='228' x2='418' y2='250' stroke='#333' stroke-width='3'/>
<polyline points='404,228 410,216 420,216' fill='none' stroke='#333' stroke-width='3'/>
<rect x='362' y='230' width='16' height='5' fill='#333'/>
<line x1='370' y1='234' x2='388' y2='252' stroke='#333' stroke-width='6'/>
<line x1='388' y1='252' x2='380' y2='268' stroke='#333' stroke-width='5'/>
<polygon points='360,230 378,236 402,208 386,198' fill='#22355e'/>
<line x1='394' y1='206' x2='416' y2='216' stroke='#22355e' stroke-width='6'/>
<text x='381' y='224' text-anchor='middle' font-size='12' font-weight='bold' fill='#d9a400'>EU</text>
<circle cx='400' cy='188' r='12' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<path d='M388 186 Q400 168 413 184 Z' fill='#d9a400' stroke='#333' stroke-width='1'/>
<path d='M418 172 Q422 179 418 182 Q414 179 418 172 Z' fill='#5b8fd1'/>
<path d='M424 186 Q428 193 424 196 Q420 193 424 186 Z' fill='#5b8fd1'/>
<polygon points='444,158 462,158 412,180' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<rect x='424' y='108' width='170' height='52' rx='14' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<text x='509' y='130' text-anchor='middle' font-size='14' font-weight='bold' fill='#14213d'>Mir nach – wir sind</text>
<text x='509' y='150' text-anchor='middle' font-size='14' font-weight='bold' fill='#14213d'>die Vorreiter!</text>
<path d='M132 214 L140 204 M150 214 L156 204 M168 214 L172 204' stroke='#555' stroke-width='2'/>
<rect x='126' y='222' width='74' height='38' fill='#ffffff' stroke='#555' stroke-width='1.5'/>
<text x='163' y='238' text-anchor='middle' font-size='12' fill='#333'>Berichts-</text>
<text x='163' y='253' text-anchor='middle' font-size='12' fill='#333'>pflichten</text>
<circle cx='162' cy='292' r='11' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<path d='M151 289 Q162 276 173 289 Z' fill='#555'/>
<rect x='152' y='303' width='20' height='34' rx='4' fill='#333'/>
<polygon points='160,305 164,305 162,318' fill='#b5302a'/>
<line x1='157' y1='337' x2='154' y2='357' stroke='#333' stroke-width='5'/>
<line x1='167' y1='337' x2='171' y2='352' stroke='#333' stroke-width='5'/>
<line x1='170' y1='308' x2='182' y2='262' stroke='#333' stroke-width='5'/>
<line x1='154' y1='308' x2='146' y2='326' stroke='#333' stroke-width='5'/>
<text x='116' y='348' text-anchor='middle' font-size='13' font-weight='bold' fill='#b5302a'>„Omnibus“</text>
<polygon points='138,276 138,292 151,290' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<rect x='10' y='262' width='130' height='44' rx='12' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<text x='75' y='280' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>Weniger Ballast,</text>
<text x='75' y='298' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>mehr Tempo!</text>
<path d='M210 410 L240 410 M200 420 L240 420 M215 430 L240 430' stroke='#555' stroke-width='2'/>
<rect x='292' y='376' width='58' height='8' fill='#22355e'/>
<path d='M306 376 L306 384 M321 376 L321 384 M336 376 L336 384' stroke='#dfe6f7' stroke-width='1'/>
<polygon points='274,404 290,384 352,384 368,404' fill='#b5302a'/>
<polygon points='282,402 294,388 318,388 318,402' fill='#dfe6f7'/>
<polygon points='324,402 324,388 348,388 360,402' fill='#dfe6f7'/>
<rect x='250' y='404' width='140' height='32' rx='8' fill='#b5302a'/>
<text x='320' y='426' text-anchor='middle' font-size='14' font-weight='bold' fill='#ffffff'>CN</text>
<circle cx='278' cy='438' r='11' fill='#333'/>
<circle cx='362' cy='438' r='11' fill='#333'/>
<polygon points='420,412 440,412 370,396' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<rect x='404' y='366' width='216' height='50' rx='14' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<text x='512' y='386' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>Solarmodule und E-Autos?</text>
<text x='512' y='405' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>Liefern wir euch gern!</text>
<line x1='712' y1='290' x2='712' y2='370' stroke='#555' stroke-width='4'/>
<rect x='668' y='250' width='88' height='40' rx='4' fill='#22355e'/>
<text x='712' y='267' text-anchor='middle' font-size='13' font-weight='bold' fill='#ffffff'>EXIT Paris</text>
<text x='712' y='283' text-anchor='middle' font-size='12' font-weight='bold' fill='#d9a400'>Öl &amp; Gas</text>
<rect x='632' y='280' width='16' height='11' rx='3' fill='#6b4a2b'/>
<ellipse cx='640' cy='291' rx='16' ry='3.5' fill='#6b4a2b'/>
<circle cx='640' cy='301' r='10' fill='#f2c9a0' stroke='#333' stroke-width='1.5'/>
<line x1='640' y1='311' x2='640' y2='340' stroke='#14213d' stroke-width='8'/>
<line x1='640' y1='340' x2='632' y2='364' stroke='#333' stroke-width='5'/>
<line x1='640' y1='340' x2='652' y2='362' stroke='#333' stroke-width='5'/>
<line x1='640' y1='318' x2='656' y2='330' stroke='#14213d' stroke-width='5'/>
<rect x='654' y='324' width='16' height='20' rx='2' fill='#333'/>
<text x='622' y='332' text-anchor='end' font-size='13' font-weight='bold' fill='#14213d'>USA</text>
<polygon points='600,286 614,286 632,296' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<rect x='530' y='256' width='96' height='30' rx='12' fill='#ffffff' stroke='#14213d' stroke-width='1.5'/>
<text x='578' y='276' text-anchor='middle' font-size='13' font-weight='bold' fill='#14213d'>Ohne mich!</text>
</svg>"""

MATERIALIEN = [
    {
        "id": "m1",
        "titel": "M1: Kommentar „Einstimmig in die Ohnmacht?“ (2026)",
        "absaetze": [
            "Wer wissen will, wie weit die Europäische Union als sicherheitspolitischer Akteur gekommen ist, muss nur auf die vergangenen vier Jahre schauen. Vor 2022 hätte kaum jemand geglaubt, dass die EU gemeinsam Waffen für ein Land im Krieg finanziert, Russland mit 21 Sanktionspaketen belegt, russisches Zentralbankvermögen in dreistelliger Milliardenhöhe unbefristet festsetzt und Kredite über 150 Milliarden Euro für Rüstungsprojekte vergibt. Die einstige „Zivilmacht“ hat gelernt, die Sprache der Macht zumindest zu buchstabieren.",
            "Doch jeder dieser Schritte war ein Kraftakt – und manche gelangen nur auf Umwegen. Über zwei Jahre lang blockierte Ungarn Erstattungen von 6,6 Milliarden Euro aus der Europäischen Friedensfazilität; erst nach dem Regierungswechsel in Budapest kam 2026 Bewegung in die Sache. Das 20. Sanktionspaket verzögerte sich um Wochen, weil Ungarn und die Slowakei ihre Zustimmung an einen Streit über russische Öllieferungen knüpften. Und das Darlehen von 90 Milliarden Euro für die Ukraine konnte nur im Wege der verstärkten Zusammenarbeit von 24 Staaten beschlossen werden.",
            "Der Grund für diese Mühen ist das Einstimmigkeitsprinzip. In der Gemeinsamen Außen- und Sicherheitspolitik kann jeder der 27 Mitgliedstaaten einen Beschluss verhindern. Was als Schutz der nationalen Souveränität gedacht war, ist zur Einladung zur Erpressung geworden: Wer ein Veto einlegt, kann dafür Zugeständnisse in ganz anderen Fragen verlangen – und Moskau weiß das.",
            "Zugleich wächst der Druck von außen. Die USA, über Jahrzehnte Garant der europäischen Sicherheit, drohten im Januar 2026 sogar Verbündeten mit Strafzöllen, weil diese sich Washingtons Ansprüchen auf Grönland widersetzten. Die NATO bleibt das Fundament der Verteidigung, so steht es auch im EU-Vertrag. Aber wer sich darauf verlässt, dass im Ernstfall andere für Europa entscheiden, handelt fahrlässig.",
            "Deshalb muss die EU die Einstimmigkeit in der Außenpolitik überwinden. Der Vertrag bietet dafür einen Weg: Über die sogenannte Brückenklausel kann der Europäische Rat beschließen, dass der Rat künftig etwa bei Sanktionen oder Menschenrechtserklärungen mit qualifizierter Mehrheit entscheidet. Militärische Einsätze sollen ausgenommen bleiben – niemand soll gegen seinen Willen Soldatinnen und Soldaten schicken müssen.",
            "Die Einwände sind bekannt: Kleine Staaten fürchten, von den großen überstimmt zu werden, und Mehrheitsentscheidungen könnten die Union eher spalten als einen. Doch ein Europa, das in der Weltpolitik nur so schnell ist wie sein langsamstes Mitglied, wird zum Zuschauer – in der Ukraine, im Nahen Osten und gegenüber Peking und Washington. Wer weltpolitikfähig sein will, muss bereit sein, auch einmal überstimmt zu werden.",
        ],
        "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Politikwissenschaftlerin (2026). Die genannten Ereignisse sind real (Stand: Oktober 2026): u. a. 20. und 21. Sanktionspaket (23.4. und 23.7.2026), unbefristete Festsetzung des russischen Zentralbankvermögens (Dezember 2025), SAFE-Verordnung (Mai 2025), Ukraine-Unterstützungsdarlehen (23.4.2026), Einigung über die Freigabe von 6,6 Mrd. Euro aus der Europäischen Friedensfazilität (September 2026), US-Zolldrohung im Grönland-Streit (Januar 2026).",
    },
    {
        "id": "m2",
        "typ": "bild",
        "titel": "M2: Karikatur „Mir nach!“ (2026)",
        "svg": SVG_KARIKATUR,
        "beschreibung": "Die Karikatur zeigt eine Straße, die von links unten steil nach rechts oben ansteigt. Rechts oben steht ein dunkelblaues Schild mit der Aufschrift 'Ziel: klimaneutral bis 2050'. In der Mitte fährt ein Radfahrer mit dunkelblauem Trikot, auf dem in Gelb 'EU' steht, bergauf; er trägt einen gelben Helm und schwitzt. Hinter sich zieht er einen schwer beladenen Anhänger: Unten stehen zwei Kisten mit den Aufschriften 'ETS 2' und 'CBAM', darauf eine Kiste '2040: –90 %'; an einer Stange weht eine grüne Fahne mit der Aufschrift 'GREEN DEAL'. Der Radfahrer ruft in einer Sprechblase: 'Mir nach – wir sind die Vorreiter!' Niemand folgt ihm. Links hinter dem Anhänger steht ein Mann im dunklen Anzug mit roter Krawatte, unter ihm steht in roter Schrift '„Omnibus“'. Er zieht eine Kiste mit der Aufschrift 'Berichtspflichten' vom Anhänger, die herunterfällt; in seiner Sprechblase steht: 'Weniger Ballast, mehr Tempo!' Rechts unten, abseits der Straße, geht eine Figur mit Cowboyhut und der Beschriftung 'USA', die ein dunkles Fass trägt, auf ein Schild 'EXIT Paris – Öl & Gas' zu und sagt: 'Ohne mich!' Unten links fährt auf einer eigenen, flachen Schnellstraße schnell ein rotes Elektroauto mit der Aufschrift 'CN' und Solarmodulen auf dem Dach vorbei (Geschwindigkeitsstriche); aus ihm kommt die Sprechblase: 'Solarmodule und E-Autos? Liefern wir euch gern!' Oben links scheint eine Sonne.",
        "quelle": "Übungsmaterial: eigene Zeichnung für Feibitur (2026).",
    },
    {
        "id": "m3",
        "titel": "M3: Warenhandel der EU mit den USA, China und Russland (in Mrd. Euro)",
        "typ": "tabelle",
        "kopf": ["Handelspartner und Jahr", "EU-Exporte", "EU-Importe", "Saldo", "Anmerkungen"],
        "zeilen": [
            ["USA 2025", "554,9", "355,5", "+199,4*", "wichtigstes Abnehmerland (21,0 % der EU-Exporte), zweitwichtigstes Lieferland (14,1 % der EU-Importe); Exporte +3,6 % gegenüber 2024"],
            ["China 2025", "199,6", "559,4", "–359,8", "wichtigstes Lieferland (22,3 % der EU-Importe); Exporte –6,5 %, Importe +6,4 % gegenüber 2024"],
            ["Russland 2025", "30,2", "27,9", "+2,3*", "Importe zu 71,8 % mineralische Brennstoffe; Handel insgesamt 58,1"],
            ["Russland 2021", "99,0", "158,5*", "–59,5*", "Jahr vor dem Großangriff auf die Ukraine; Handel insgesamt 257,5"],
        ],
        "quelle": "Eurostat, „EU trade in goods surplus down to €128 billion in 2025“ (26.3.2026; Werte für die USA) und „Trade in goods with China in 2025“ (10.4.2026); Europäische Kommission (Generaldirektion Handel), „EU trade relations with Russia“ (Werte für Russland; abgerufen am 2.11.2026). Warenhandel ohne Dienstleistungen, Werte gerundet und teilweise vorläufig. * eigene Berechnung aus den Angaben der Quellen. Der Überschuss der EU im gesamten Warenhandel lag 2025 bei 128 Mrd. Euro.",
    },
]

AUFGABEN = [
    {
        "id": "q4-3-i1",
        "afb": "I",
        "operator": "zusammenfassen",
        "text": "Fassen Sie die Aussagen des Kommentars zusammen. (M1)",
        "material": ["m1"],
        "loesung": {
            "vorbemerkung": "Einleitung mit Textsorte (Kommentar), Titel („Einstimmig in die Ohnmacht?“), Erscheinungsjahr (2026), Verfasserin (fiktive Politikwissenschaftlerin) und Thema (Handlungsfähigkeit der EU in der Außen- und Sicherheitspolitik, Forderung nach Mehrheitsentscheidungen).",
            "punkte": [
                "Die Autorin stellt fest, die EU habe seit 2022 sicherheitspolitisch bisher Undenkbares getan: gemeinsame Finanzierung von Waffen, 21 Sanktionspakete, unbefristete Festsetzung russischen Zentralbankvermögens, Rüstungskredite über 150 Mrd. Euro; die Zivilmacht lerne die Sprache der Macht [1].",
                "Jeder Schritt sei jedoch mühsam gewesen: ungarische Blockade von 6,6 Mrd. Euro aus der Friedensfazilität über zwei Jahre, Verzögerung des 20. Sanktionspakets durch Ungarn und die Slowakei, 90-Mrd.-Darlehen nur über verstärkte Zusammenarbeit von 24 Staaten [2].",
                "Ursache sei das Einstimmigkeitsprinzip in der GASP, das jedem Staat ein Veto gebe und zur Erpressung einlade – was auch Russland ausnutzen könne [3].",
                "Der Druck von außen wachse, da selbst die USA Verbündeten im Grönland-Streit mit Zöllen gedroht hätten; die NATO bleibe zwar Fundament, sich allein auf andere zu verlassen, sei aber fahrlässig [4].",
                "Forderung: Einstimmigkeit überwinden, indem der Europäische Rat über die Brückenklausel Mehrheitsentscheidungen etwa bei Sanktionen und Menschenrechtserklärungen ermögliche; militärische Einsätze sollten ausgenommen bleiben [5].",
                "Die Einwände (Überstimmung kleiner Staaten, Gefahr der Spaltung) würden genannt, aber zurückgewiesen: Ohne Mehrheitsentscheidungen werde Europa zum Zuschauer; Weltpolitikfähigkeit setze die Bereitschaft voraus, überstimmt zu werden [6].",
            ],
            "hinweis": "Zusammenfassen: strukturiert, komprimiert, in eigenen Worten und in indirekter Rede; keine eigene Wertung. Die Argumentationsstruktur (Bilanz – Problem – Ursache – Druck von außen – Forderung – Umgang mit Einwänden) sollte erkennbar werden.",
        },
        "bewertung": {
            "ausreichend": "die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.",
            "gut": "die Aussagen des Kommentars weitgehend vollständig, strukturiert, fachsprachlich und in eigenen Worten unter Verwendung der indirekten Rede zusammengefasst werden.",
        },
    },
    {
        "id": "q4-3-i2",
        "afb": "I",
        "operator": "beschreiben",
        "text": "Beschreiben Sie die Karikatur (M2).",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Formale Angaben: Karikatur „Mir nach!“, eigene Zeichnung, 2026; Thema: Klimapolitik der EU.",
                "Bildmitte: Radfahrer im EU-Trikot fährt eine steile Straße hinauf, schwitzt; er zieht einen schweren Anhänger mit den Kisten „ETS 2“, „CBAM“ und „2040: –90 %“ sowie einer grünen Fahne „GREEN DEAL“; Sprechblase „Mir nach – wir sind die Vorreiter!“; niemand folgt ihm.",
                "Oben rechts: Zielschild „Ziel: klimaneutral bis 2050“ am Ende der Steigung.",
                "Links: Mann im Anzug („Omnibus“) zieht die Kiste „Berichtspflichten“ vom Anhänger; Sprechblase „Weniger Ballast, mehr Tempo!“.",
                "Rechts unten: Figur mit Cowboyhut („USA“) mit einem Fass geht abseits der Straße auf ein Schild „EXIT Paris – Öl & Gas“ zu und sagt „Ohne mich!“.",
                "Unten links: rotes Elektroauto „CN“ mit Solarmodulen fährt schnell auf einer flachen Schnellstraße vorbei; Sprechblase „Solarmodule und E-Autos? Liefern wir euch gern!“.",
            ],
            "hinweis": "Beschreiben: nur das Sichtbare, strukturiert nach Bildaufbau (z. B. Mitte – oben – links – rechts – unten), noch keine Deutung. Begriffe wie „Trittbrettfahrer“ gehören in die Analyse.",
        },
        "bewertung": {
            "ausreichend": "die wesentlichen Bildelemente im Ansatz korrekt beschrieben werden.",
            "gut": "die Karikatur vollständig, strukturiert nach dem Bildaufbau und präzise beschrieben wird, ohne vorzeitig zu deuten.",
        },
    },
    {
        "id": "q4-3-i3",
        "afb": "I",
        "operator": "darstellen",
        "text": "Stellen Sie die Ziele und zentralen Instrumente der Klimapolitik der Europäischen Union dar.",
        "material": [],
        "loesung": {
            "punkte": [
                "Leitbild und Rahmen: Europäischer Grüner Deal (2019), Klimaneutralität bis 2050; Vorreiterrolle als Anspruch, ökologische Modernisierung als Wachstumsstrategie.",
                "Rechtsverbindliche Ziele: Europäisches Klimagesetz (2021) mit mindestens –55 % bis 2030 gegenüber 1990, seit 2026 –90 % bis 2040 (mit Flexibilitäten, z. B. bis zu 5 % internationale Gutschriften ab 2036); NDC für 2035: –66,25 bis –72,5 %.",
                "Marktinstrumente: EU-Emissionshandel seit 2005 (Cap and Trade für Kraftwerke, Industrie, Luftverkehr in Europa, Schifffahrt), ETS 2 für Gebäude und Straßenverkehr ab 2028, Klima-Sozialfonds als sozialer Ausgleich.",
                "Ordnungsrecht und Ziele für einzelne Bereiche (Paket „Fit for 55“): nationale Minderungsziele für Nicht-ETS-Sektoren, CO2-Flottengrenzwerte für Pkw, Ziele für erneuerbare Energien und Energieeffizienz.",
                "Außenwirtschaftliche Instrumente: CO2-Grenzausgleich (CBAM, endgültige Phase seit 2026) gegen Carbon Leakage.",
                "Klimaaußenpolitik: Verhandlungen auf den COPs als Block, Allianzen, Klimafinanzierung (2025: 32,3 Mrd. Euro öffentlich), Partnerschaften für eine gerechte Energiewende.",
                "Zusammenhänge darstellen: Ziele im Klimagesetz → Umsetzung über Instrumente → Glaubwürdigkeit und Hebelwirkung nach außen.",
            ],
            "hinweis": "Darstellen verlangt, Sachverhalte und ihre Bezüge aufzuzeigen – nicht nur aufzuzählen. Exakte Prozentzahlen sind nachrangig; entscheidend sind die Systematik (Ziele – Instrumente – Außenwirkung) und fachlich korrekte Begriffe.",
        },
        "bewertung": {
            "ausreichend": "zentrale Ziele und einige Instrumente der EU-Klimapolitik im Ansatz zutreffend dargestellt werden.",
            "gut": "Ziele und Instrumente fachlich präzise, systematisch und in ihren Zusammenhängen dargestellt werden, einschließlich der außenpolitischen Dimension.",
        },
    },
    {
        "id": "q4-3-ii1",
        "afb": "II",
        "operator": "erläutern",
        "text": "Erläutern Sie ausgehend von M1 die Entscheidungsverfahren und Instrumente, mit denen die EU zur kollektiven Konfliktbearbeitung und Friedenssicherung beiträgt.",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Entscheidungsverfahren der GASP: intergouvernemental; Europäischer Rat legt Leitlinien fest, Rat „Auswärtige Angelegenheiten“ beschließt grundsätzlich einstimmig (Art. 24, 31 EUV); Hohe Vertreterin (Kaja Kallas) und EAD bereiten vor und setzen um; Kommission wirkt bei Sanktionen und Handel mit; Parlament nur mit Informations- und Haushaltsrechten.",
                "Auswege aus der Einstimmigkeit mit Beispielen: konstruktive Enthaltung (z. B. Irland, Österreich bei Waffenfinanzierung über die EFF), Mehrheit bei Durchführungsbeschlüssen, Brückenklausel (Art. 31 Abs. 3, selbst einstimmig zu beschließen, nicht für militärische Fragen, M1 [5]), verstärkte Zusammenarbeit (90-Mrd.-Darlehen, M1 [2]), andere Rechtsgrundlagen (Art. 122 AEUV für das russische Vermögen).",
                "Instrument Sanktionen: einstimmiger Ratsbeschluss, 21 Pakete gegen Russland bis Juli 2026, Ziel: Kosten des Krieges erhöhen; Grenzen: Umgehung, Blockaden (M1 [1]–[3]).",
                "Instrument Europäische Friedensfazilität: außerhalb des Haushalts (Art. 41 Abs. 2 EUV), finanziert Militärhilfe und Einsätze; für die Ukraine rund 10,8 Mrd. Euro; ungarische Blockade der 6,6 Mrd. Euro (M1 [2]).",
                "GSVP-Missionen: zivile und militärische Einsätze (21 laufende, rund 4.000 Kräfte, z. B. EUMAM Ukraine, Atalanta, Aspides); Personal von den Mitgliedstaaten; schnelle Eingreifkapazität (Strategischer Kompass).",
                "Weitere Instrumente: Diplomatie und Vermittlung, Finanzhilfen, Erweiterung als Sicherheitspolitik, Rüstungsförderung (SAFE, M1 [1]); Beistandsklausel Art. 42 Abs. 7 EUV und Verhältnis zur NATO (M1 [4]).",
            ],
            "hinweis": "Erläutern verlangt, Verfahren und Instrumente mit zusätzlichen Informationen und Beispielen zu veranschaulichen. Materialbezüge zu M1 sind zu erwarten; eine reine Aufzählung ohne Erklärung des Einstimmigkeitsprinzips genügt nicht für eine gute Leistung.",
        },
        "bewertung": {
            "ausreichend": "Entscheidungsverfahren und einige Instrumente der GASP/GSVP im Ansatz zutreffend und mit Materialbezug erläutert werden.",
            "gut": "Entscheidungsverfahren und Instrumente differenziert, mit treffenden Beispielen und durchgängigem Bezug zu M1 erläutert und ihre Grenzen deutlich werden.",
        },
    },
    {
        "id": "q4-3-ii2",
        "afb": "II",
        "operator": "analysieren",
        "text": "Analysieren Sie die Karikatur (M2) im Hinblick auf ihre Aussage über die Rolle der EU in der globalen Klimapolitik.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Steile Straße zum Ziel „klimaneutral bis 2050“: Klimaneutralität als langer, anstrengender Weg (Klimagesetz, Zwischenziele).",
                "Radfahrer „EU“ mit Anhänger: EU als selbst ernannte Vorreiterin, die die Last ehrgeiziger Instrumente (ETS 2, CBAM, 2040-Ziel, Green Deal) allein trägt; Schweiß verweist auf Kosten für Wirtschaft und Haushalte.",
                "„Mir nach!“ ohne Nachfolger: Strategie des Vorbilds (Leadership by example) greift nicht; Bezug zum Kollektivgut- und Trittbrettfahrerproblem (vgl. Q3.5).",
                "Figur „USA“ auf dem Weg zum „EXIT Paris – Öl & Gas“: Austritt der USA aus dem Pariser Abkommen (wirksam seit 27.1.2026) und Vorrang fossiler Energien; Ausfall eines zentralen Partners.",
                "Rotes E-Auto „CN“ auf eigener Schnellstraße: China als größter Emittent, der zugleich bei Solar, Batterien und E-Autos dominiert und an der europäischen Nachfrage verdient; EU in Abhängigkeit bei grüner Technologie (Wettbewerbsproblem).",
                "Mann „Omnibus“ wirft „Berichtspflichten“ ab: Vereinfachungs- und Deregulierungspolitik der EU (Omnibus-I-Paket, CBAM-Ausnahmen) als Reaktion auf Wettbewerbsdruck – ambivalent zwischen Entlastung und Abschwächung.",
                "Kernaussage: Die EU beansprucht die Führungsrolle im Klimaschutz, steht aber weitgehend allein, trägt hohe Lasten, während andere aussteigen oder wirtschaftlich profitieren, und gerät intern unter Druck, ihre Ambition zu verringern.",
            ],
            "hinweis": "Analysieren: Bildelemente systematisch deuten, mit Fachbegriffen (Vorreiterrolle, Trittbrettfahrer, Carbon Leakage, Wettbewerbsfähigkeit, Omnibus) und Fachwissen verknüpfen und eine Kernaussage formulieren. Auch Einordnungen wie die Frage, ob die Karikatur den Green Deal eher als Last oder als Chance zeigt, sind zu würdigen.",
        },
        "bewertung": {
            "ausreichend": "zentrale Bildelemente ansatzweise zutreffend gedeutet und eine Kernaussage formuliert wird.",
            "gut": "die Bildelemente systematisch, mit Fachbegriffen und aktuellem Fachwissen gedeutet werden und eine präzise, gut begründete Kernaussage formuliert wird.",
        },
    },
    {
        "id": "q4-3-ii3",
        "afb": "II",
        "operator": "auswerten",
        "text": "Werten Sie M3 im Hinblick auf die Wirkung der europäischen Sanktions- und Energiepolitik gegenüber Russland sowie auf die wirtschaftlichen Abhängigkeiten der EU aus.",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Russland: Der Warenhandel sank von 257,5 Mrd. Euro (2021) auf 58,1 Mrd. Euro (2025), also um rund 77 %; die Importe aus Russland fielen von 158,5 auf 27,9 Mrd. Euro (rund –82 %), die Exporte von 99,0 auf 30,2 Mrd. Euro (rund –70 %); erstmals leichter Überschuss der EU.",
                "Deutung: Sanktionen (Ein- und Ausfuhrverbote) und der Ausstieg aus russischer Energie haben die wirtschaftliche Verflechtung drastisch reduziert; die verbleibenden Importe bestehen aber zu 71,8 % aus mineralischen Brennstoffen – die Energieabhängigkeit ist noch nicht beendet (Gasausstieg erst bis 2027).",
                "Grenzen der Aussagekraft: Die Daten zeigen nur den Handel mit der EU, nicht, ob Russland ausweicht (z. B. Exporte nach China und Indien, Umgehung über Drittstaaten) oder ob die Sanktionen die Kriegsführung tatsächlich einschränken; Werte sind nominal und von Energiepreisen beeinflusst.",
                "USA: wichtigster Absatzmarkt (21,0 % der EU-Exporte), Überschuss von rund 199 Mrd. Euro – hohe Exportabhängigkeit und Verwundbarkeit gegenüber US-Zöllen; der Überschuss dient der US-Regierung als Argument für Zölle.",
                "China: wichtigstes Lieferland (22,3 % der Importe), Defizit von 359,8 Mrd. Euro, Importe steigend, Exporte sinkend – Importabhängigkeit (z. B. Elektronik, Batterien, Vorprodukte) und Wettbewerbsdruck; Anlass für De-Risking.",
                "Gesamtaussage: Gegenüber Russland hat die EU ihre Abhängigkeit unter hohen Kosten weitgehend abgebaut; gegenüber den USA (Absatz) und China (Bezug) bestehen erhebliche Abhängigkeiten, die ihren außenpolitischen Handlungsspielraum begrenzen.",
            ],
            "hinweis": "Auswerten verlangt, die Daten zu einer Gesamtaussage zusammenzuführen; Berechnungen (Veränderungsraten, Salden) sowie eine Reflexion der Aussagekraft der Statistik werden erwartet. Ungefähre Prozentwerte genügen.",
        },
        "bewertung": {
            "ausreichend": "die Daten im Ansatz korrekt erfasst und zu einer ansatzweise begründeten Aussage über Sanktionswirkung und Abhängigkeiten zusammengeführt werden.",
            "gut": "die Daten präzise und rechnerisch belegt ausgewertet, mit Fachwissen zu Sanktionen und Abhängigkeiten verknüpft, in ihrer Aussagekraft reflektiert und zu einer schlüssigen Gesamtaussage zusammengeführt werden.",
        },
    },
    {
        "id": "q4-3-ii4",
        "afb": "II",
        "operator": "vergleichen",
        "lk": True,
        "text": "Vergleichen Sie die Beziehungen der EU zu den USA und zu China unter wirtschaftlichen und politischen Gesichtspunkten. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Vergleichskriterien benennen, z. B. wirtschaftliche Verflechtung, Sicherheit, Werte und Systemfrage, Konfliktfelder, Instrumente der EU, Einigkeit der Mitgliedstaaten.",
                "Wirtschaft (M3): USA wichtigster Absatzmarkt mit EU-Überschuss (rund 199 Mrd. Euro) – Exportabhängigkeit; China wichtigstes Lieferland mit EU-Defizit (359,8 Mrd. Euro) – Importabhängigkeit, Überkapazitäten, sinkende EU-Exporte.",
                "Sicherheit: USA Verbündeter in der NATO und Garant nuklearer Abschreckung, aber mit Forderungen nach Lastenteilung und Zweifeln an der Verlässlichkeit (Grönland, Sicherheitsstrategie 2025); China kein Bündnispartner, enge Partnerschaft mit Russland, EU-Sanktionen gegen chinesische Firmen.",
                "Werte und System: USA demokratischer Partner trotz Spannungen (Kritik der US-Regierung an Europa, Digitalregulierung); China „systemischer Rivale“ mit autoritärem Modell, Menschenrechtskonflikte.",
                "Instrumente der EU: gegenüber den USA Verhandlungen und Zugeständnisse (Turnberry: 15-%-Obergrenze, Zollabbau der EU) mit Gegenmaßnahmen in Reserve; gegenüber China De-Risking, Ausgleichszölle auf E-Autos, Mindestpreiszusagen, Investitionsprüfung, Dialog beim Klimaschutz.",
                "Gemeinsamkeiten: Beide Mächte nutzen wirtschaftliche Verflechtung als Druckmittel (US-Zölle, chinesische Exportkontrollen für seltene Erden); in beiden Fällen sind die Mitgliedstaaten uneinig (z. B. Exportinteressen der Autoindustrie).",
                "Fazit: unterschiedliche Grundmuster (Verbündeter unter Vorbehalt vs. Partner, Wettbewerber und Rivale), aber ähnliche Herausforderung: die Abwägung zwischen wirtschaftlichen Interessen und strategischer Selbstbehauptung.",
            ],
            "hinweis": "Vergleichen verlangt kriteriengeleitet Gemeinsamkeiten und Unterschiede; ein bloßes Nacheinander beider Beziehungen ohne Gegenüberstellung genügt nicht für eine gute Leistung. Materialbezug zu M3 wird erwartet (LK-Niveau).",
        },
        "bewertung": {
            "ausreichend": "die Beziehungen zu den USA und zu China ansatzweise kriteriengeleitet und mit Materialbezug verglichen werden.",
            "gut": "der Vergleich kriteriengeleitet, differenziert, mit Gemeinsamkeiten und Unterschieden, aktuellen Belegen und einem begründeten Fazit erfolgt.",
        },
    },
    {
        "id": "q4-3-iii1",
        "afb": "III",
        "operator": "erörtern",
        "text": "Die Autorin fordert, in der Gemeinsamen Außen- und Sicherheitspolitik Mehrheitsentscheidungen einzuführen. Erörtern Sie diese Forderung. (M1)",
        "material": ["m1"],
        "loesung": {
            "punkte": [
                "Pro: schnellere und verlässlichere Handlungsfähigkeit; Ende von Blockaden und Erpressung durch Einzelstaaten (Beispiele aus M1 [2]); höhere Glaubwürdigkeit gegenüber Russland, China und den USA; in anderen Politikfeldern (Handel, Binnenmarkt) funktioniert die qualifizierte Mehrheit; konstruktive Enthaltung reicht in der Praxis nicht aus; die Brückenklausel erlaubt den Schritt ohne Vertragsänderung; militärische Einsätze bleiben ausgenommen.",
                "Kontra: Außen- und Sicherheitspolitik als Kern staatlicher Souveränität; demokratische Legitimation (Verantwortung nationaler Parlamente, in Deutschland Art. 23 GG); kleine Staaten könnten von großen überstimmt werden; überstimmte Staaten müssten Sanktionen dennoch umsetzen – Gefahr von Spaltung und Legitimitätsverlust; die Brückenklausel muss selbst einstimmig beschlossen werden und ist politisch kaum durchsetzbar.",
                "Differenzierung: Probleme sind teils politisch statt institutionell (Lösung der EFF-Blockade nach dem Regierungswechsel in Ungarn); Ausweichwege (verstärkte Zusammenarbeit, Koalitionen der Willigen, andere Rechtsgrundlagen mit Mehrheit) zeigen Handlungsfähigkeit, sind aber rechtlich umstritten (Klagen Ungarns und der Slowakei).",
                "Mögliche Zwischenlösungen: Mehrheit zunächst nur bei Menschenrechtserklärungen und Sanktionen, Schutzklausel für vitale nationale Interessen, Ausbau der konstruktiven Enthaltung.",
                "Abwägung nach Kriterien (z. B. Effektivität, Legitimität, Zusammenhalt der Union) und begründetes eigenes Urteil; beide Ergebnisse sind möglich, wenn schlüssig begründet.",
            ],
            "hinweis": "Erörtern verlangt eine Abwägung von Pro- und Kontraargumenten und ein eigenes, begründetes Urteil. Ein Urteil ohne Gegenargumente oder ohne Bezug zur Forderung in M1 [5]–[6] kann nicht als gut bewertet werden.",
        },
        "bewertung": {
            "ausreichend": "die Erörterung ansatzweise strukturiert ist und in ein ansatzweise nachvollziehbares, begründetes Urteil mündet.",
            "gut": "die Erörterung strukturiert, fachlich fundiert (Verfahren der GASP, aktuelle Beispiele) und weitgehend kohärent ist und in ein klares, schlüssig begründetes Urteil mündet.",
        },
    },
    {
        "id": "q4-3-iii2",
        "afb": "III",
        "operator": "beurteilen",
        "text": "Beurteilen Sie ausgehend von der Karikatur (M2), ob die EU ihrem Anspruch gerecht wird, Vorreiterin einer globalen Klimapolitik zu sein.",
        "material": ["m2"],
        "loesung": {
            "punkte": [
                "Kriterien benennen, z. B. Ehrgeiz der Ziele, tatsächliche Wirkung (Emissionsminderung), Glaubwürdigkeit und Beständigkeit, Einfluss auf andere Staaten, Gerechtigkeit gegenüber ärmeren Ländern.",
                "Für die Vorreiterrolle: rechtsverbindliche Ziele (–55 % 2030, –90 % 2040, Klimaneutralität 2050); Emissionen 2024 rund 37 % unter 1990 (in der Abgrenzung des 2030-Ziels); Halbierung der Emissionen im Emissionshandel seit 2005; innovative Instrumente (ETS 2, CBAM); NDC 2035; Klimafinanzierung von 32,3 Mrd. Euro (2025); Allianzen auf den COPs (z. B. Fahrplan zum Ausstieg aus fossilen Energien in Belém mit über 80 Staaten); Brüssel-Effekt.",
                "Gegen die Vorreiterrolle: Flexibilitäten und Verschiebungen (internationale Gutschriften ab 2036, ETS 2 erst 2028), Omnibus-Abschwächungen, Vorschlag zur Lockerung des Verbrenner-Aus – Glaubwürdigkeitsverlust; Projektion verfehlt das 2030-Ziel knapp; steigende Verkehrsemissionen; geringer Anteil an den globalen Emissionen (rund 6 %); in Belém kein Fahrplan durchgesetzt; Kritik des globalen Südens am CBAM; Abhängigkeit von chinesischer Klimatechnik.",
                "Bezug zur Karikatur: Sie trifft die Einsamkeit der Vorreiterrolle und den internen Druck (USA-Austritt, Chinas wirtschaftlicher Vorteil, Omnibus), blendet aber Erfolge und Kooperationen aus (z. B. Klimaerklärung mit China, Partnerschaften, Allianzen mit Inselstaaten) – typisch zugespitzt.",
                "Begründetes Urteil, z. B.: Vorreiterin bei Zielen und Instrumenten, aber mit nachlassender Konsequenz und begrenzter Gefolgschaft; ihre Rolle hängt davon ab, ob sie zeigt, dass Klimaschutz und Wettbewerbsfähigkeit vereinbar sind.",
            ],
            "hinweis": "Beurteilen verlangt ein kriteriengeleitetes, auf Fachwissen gestütztes Sachurteil; die Karikatur ist Ausgangspunkt, die Beurteilung muss aber über sie hinausgehen. Aktuelle Belege mit Stand sind zu würdigen.",
        },
        "bewertung": {
            "ausreichend": "ein ansatzweise kriteriengeleitetes Urteil mit einigen zutreffenden Belegen zur EU-Klimapolitik formuliert wird.",
            "gut": "das Urteil kriteriengeleitet, abwägend, mit aktuellen Belegen und Bezug zur Karikatur fundiert und schlüssig begründet ist.",
        },
    },
    {
        "id": "q4-3-iii3",
        "afb": "III",
        "operator": "entwerfen",
        "text": "Entwerfen Sie eine Rede, die eine Abgeordnete des Europäischen Parlaments in einer Plenardebatte zum Thema „Braucht Europa eine Verteidigungsunion neben der NATO?“ halten könnte.",
        "material": [],
        "loesung": {
            "vorbemerkung": "Produktorientierte Aufgabe: Bewertet werden fachliche Fundierung, klare Position, Adressatenbezug (Plenum des EP) und die Merkmale einer Rede (Anrede, Einstieg, Argumentationsgang, Umgang mit Gegenargumenten, Appell). Beide Grundpositionen sind zulässig.",
            "punkte": [
                "Redeform: Anrede („Frau Präsidentin, liebe Kolleginnen und Kollegen …“), anschaulicher Einstieg (z. B. Drohnen über der Ostflanke, Grönland-Streit), klare These, Schluss mit Appell.",
                "Lagebeschreibung: Russlands Angriffskrieg und hybride Angriffe; Zweifel an der Verlässlichkeit der USA (Forderung nach 5 % des BIP, Sicherheitsstrategie 2025, Zolldrohung 2026); Fragmentierung der europäischen Rüstung.",
                "Vorhandene EU-Instrumente einordnen: Strategischer Kompass und schnelle Eingreifkapazität, SSZ/PESCO, Europäischer Verteidigungsfonds, EDIP, ReArm Europe/SAFE (150 Mrd. Euro), Beistandsklausel Art. 42 Abs. 7 EUV.",
                "Verhältnis zur NATO: 23 gemeinsame Mitglieder, NATO als Fundament der kollektiven Verteidigung; Verteidigungsunion als „europäischer Pfeiler“ oder als Schritt zur strategischen Autonomie; Risiko von Doppelstrukturen.",
                "Gegenargumente aufgreifen und entkräften oder gewichten: Kosten und gemeinsame Schulden, nationale Souveränität und Parlamentsvorbehalt, neutrale Staaten, Sicherheitsdilemma, Abhängigkeit von US-Fähigkeiten.",
                "Konkrete Forderungen, z. B. gemeinsame Beschaffung, Luftverteidigung, militärische Mobilität, Stärkung der Rüstungsindustrie, Mehrheitsentscheidungen in Teilbereichen – oder umgekehrt Konzentration auf die NATO und nationale Fähigkeiten.",
            ],
            "hinweis": "Entwerfen verlangt ein eigenständiges, kreatives Produkt auf fachlicher Grundlage. Eine bloße Erörterung ohne Redeform oder eine Rede ohne fachliche Substanz erfüllt den Operator nur teilweise.",
        },
        "bewertung": {
            "ausreichend": "eine erkennbar als Rede gestaltete Stellungnahme mit einer Position und einigen fachlich zutreffenden Argumenten vorliegt.",
            "gut": "die Rede adressatengerecht und überzeugend gestaltet ist, eine klare Position fachlich fundiert entwickelt, Gegenargumente aufgreift und mit konkreten Forderungen schließt.",
        },
    },
    {
        "id": "q4-3-iii4",
        "afb": "III",
        "operator": "Stellung nehmen",
        "lk": True,
        "text": "„Europa muss lernen, zwischen Washington, Peking und Moskau als eigenständige Macht zu bestehen.“ Nehmen Sie Stellung zu dieser These. (M3)",
        "material": ["m3"],
        "loesung": {
            "punkte": [
                "Klärung: eigenständige Macht im Sinne strategischer Autonomie bzw. Souveränität; Abgrenzung zum „europäischen Pfeiler“ im westlichen Bündnis; Bezug zu den drei Beziehungsmustern (Verbündeter unter Vorbehalt, Partner–Wettbewerber–Rivale, Bedrohung).",
                "Für die These: Unberechenbarkeit der US-Politik (Zölle, Grönland, Sicherheitsstrategie); systemische Rivalität und Erpressungspotenzial Chinas (seltene Erden, Defizit, M3); militärische Bedrohung durch Russland; wirtschaftliches Gewicht der EU als Grundlage (Binnenmarkt, Brüssel-Effekt, Handelsvolumina in M3); Instrumente wie das Instrument gegen Zwangsmaßnahmen, De-Risking, Aufrüstung.",
                "Gegen die These bzw. Einschränkungen: militärische und nukleare Abhängigkeit von den USA; hohe wirtschaftliche Abhängigkeit vom US-Absatzmarkt und von chinesischen Importen (M3); Uneinigkeit der Mitgliedstaaten und Einstimmigkeit in der GASP; Kosten und Zeitbedarf; Risiko, die USA zusätzlich zu entfremden; Gefahr einer Äquidistanz zwischen Demokratie und autoritären Mächten.",
                "Theoriebezug: Realismus (Machtbalance, Selbsthilfe), Liberalismus/Institutionalismus (Interdependenz, Regeln, Bündnisse), ggf. Konstruktivismus (Identität als Zivil- oder Friedensmacht).",
                "Eigene Wertmaßstäbe offenlegen (z. B. Sicherheit, Freiheit, Wohlstand, Regelbindung) und eine klare, begründete Position entwickeln, ggf. differenziert (z. B. Selbstbehauptung ja, Abkehr vom transatlantischen Bündnis nein).",
            ],
            "hinweis": "Stellung nehmen verlangt wie „beurteilen“ eine kriteriengeleitete Einschätzung, zusätzlich aber die ausdrückliche Offenlegung und Begründung eigener Wertmaßstäbe. LK-Niveau: Theoriebezug und Differenzierung zwischen den drei Mächten werden erwartet.",
        },
        "bewertung": {
            "ausreichend": "eine ansatzweise begründete Stellungnahme mit erkennbaren eigenen Maßstäben und einigen Belegen vorliegt.",
            "gut": "die Stellungnahme abwägend, theoriegeleitet und mit Bezug zu M3 sowie zu allen drei Mächten fundiert ist, eigene Wertmaßstäbe ausdrücklich offenlegt und in ein klares Urteil mündet.",
        },
    },
]
