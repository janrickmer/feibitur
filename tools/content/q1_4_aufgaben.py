# -*- coding: utf-8 -*-
"""Übungsaufgaben zu Q1.4 (Einzelaufgaben, je Anforderungsbereich mindestens drei).

MATERIALIEN: von mehreren Aufgaben gemeinsam genutzte Materialien (M1, M2, …)
AUFGABEN: Einzelaufgaben mit Operator, Materialbezug, Lösungshinweisen und Bewertungskriterien.
Lösungshinweise und Bewertung landen nur unsichtbar in den Korrekturdateien (PDF), nicht auf der Webseite.
"""

BEZUG = 'Q1.4, insbesondere Funktionen und Probleme klassischer Massenmedien; Chancen und Risiken neuer politischer Kommunikationsformen im Internet (insbesondere Filterblasen, Fake News).'

MATERIALIEN = [
    {
        'titel': 'M1: Gastbeitrag „Die Wahl entscheidet sich im Feed“ (2026)',
        'absaetze': [
            'Drei Tage vor einer Landtagswahl taucht ein Video auf: Die Spitzenkandidatin einer Regierungspartei sagt darin, sie werde nach der Wahl die Pendlerpauschale abschaffen. Das Video wird binnen Stunden hunderttausendfach geteilt. Erst am nächsten Tag stellt sich heraus, dass es mit künstlicher Intelligenz erzeugt wurde. Die Richtigstellung erreicht nur einen Bruchteil derer, die das Original gesehen haben.',
            'Dieses Szenario ist erfunden – aber es ist nicht unrealistisch. Mit wenigen Klicks lassen sich heute Stimmen und Gesichter täuschend echt nachahmen. Und die Plattformen, auf denen sich vor allem junge Menschen informieren, sind auf genau solche Inhalte geeicht: Was überrascht, empört oder Angst macht, wird häufiger geteilt, länger angesehen und vom Algorithmus weiter nach oben gespült.',
            'Hinzu kommt, dass viele Nutzerinnen und Nutzer gar nicht mehr merken, wie sehr ihr Feed auf sie zugeschnitten ist. Wer sich einmal für ein Thema interessiert hat, bekommt mehr davon – und immer seltener die Gegenposition. In geschlossenen Gruppen und Kanälen bestätigen sich Gleichgesinnte gegenseitig. Die gemeinsame Faktengrundlage, ohne die eine demokratische Debatte nicht funktioniert, wird brüchig.',
            'Die klassischen Medien können das nur begrenzt auffangen. Zwar prüfen Redaktionen ihre Informationen und trennen Nachricht und Meinung. Doch ihre Reichweite bei jungen Menschen sinkt, und viele Lokalzeitungen haben in den vergangenen Jahren Redaktionen geschlossen. Gleichzeitig sparen manche Plattformen an Moderation und Faktenchecks.',
            'Der Digital Services Act der EU verpflichtet große Plattformen zwar bereits, Risiken für Wahlen zu bewerten und zu verringern. Doch das reicht nicht. Ich fordere: In den vier Wochen vor einer Wahl müssen Plattformen politische Inhalte mit großer Reichweite vor ihrer weiteren Verbreitung prüfen – auf Fälschungen, auf KI-Manipulation, auf offensichtliche Falschbehauptungen. Wer das nicht leistet, muss empfindliche Strafen zahlen.',
            'Kritiker werden einwenden, das sei Zensur. Aber Meinungsfreiheit bedeutet nicht, dass gefälschte Videos ungehindert Millionen Menschen erreichen dürfen. Eine Demokratie, die ihre Wahlen nicht vor Manipulation schützt, setzt ihr Fundament aufs Spiel.',
        ],
        'quelle': 'Übungsmaterial: eigens für Feibitur verfasster Gastbeitrag einer fiktiven Medienwissenschaftlerin (2026). Das Eingangsszenario ist ausdrücklich erfunden.',
        'id': 'm1',
    },
    {
        'id': 'm2',
        'typ': 'bild',
        'titel': 'M2: Karikatur „Wohlfühlklima“ (2026)',
        'svg': "<svg viewBox='0 0 760 440' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' role='img' aria-labelledby='kkt'>\n<title id='kkt'>Karikatur Wohlfühlklima: Eine Person sitzt in einer Blase, ein Roboter namens Algorithmus pumpt sie auf, Stimmen von außen prallen ab.</title>\n<rect x='0' y='0' width='760' height='440' fill='#fffdf6'/>\n<ellipse cx='300' cy='225' rx='205' ry='185' fill='#dcefff' fill-opacity='0.55' stroke='#5b8fd1' stroke-width='3'/>\n<path d='M170 120 Q200 80 250 70' fill='none' stroke='#ffffff' stroke-width='8' stroke-linecap='round'/>\n<ellipse cx='300' cy='335' rx='80' ry='28' fill='#c0392b'/>\n<rect x='270' y='250' width='60' height='80' rx='22' fill='#2c3e50'/>\n<circle cx='300' cy='228' r='28' fill='#f2c9a0' stroke='#333' stroke-width='2'/>\n<path d='M287 236 Q300 248 313 236' fill='none' stroke='#333' stroke-width='2'/>\n<circle cx='290' cy='224' r='2.5' fill='#333'/><circle cx='310' cy='224' r='2.5' fill='#333'/>\n<path d='M272 214 Q300 186 328 214' fill='#6b4a2b'/>\n<rect x='318' y='265' width='26' height='42' rx='4' fill='#111' stroke='#555'/>\n<rect x='321' y='270' width='20' height='30' fill='#7fd3ff'/>\n<path d='M330 285 L318 300' stroke='#f2c9a0' stroke-width='9' stroke-linecap='round'/>\n<g font-size='14' fill='#14213d' font-weight='bold'>\n<rect x='140' y='140' width='120' height='34' rx='14' fill='#ffffff' stroke='#5b8fd1'/><text x='200' y='162' text-anchor='middle'>Genau so!</text>\n<rect x='330' y='130' width='140' height='34' rx='14' fill='#ffffff' stroke='#5b8fd1'/><text x='400' y='152' text-anchor='middle'>Du hast recht!</text>\n<rect x='105' y='270' width='150' height='34' rx='14' fill='#ffffff' stroke='#5b8fd1'/><text x='180' y='292' text-anchor='middle'>Sehe ich auch so!</text>\n<rect x='360' y='200' width='110' height='34' rx='14' fill='#ffffff' stroke='#5b8fd1'/><text x='415' y='222' text-anchor='middle'>100 % wahr!</text>\n</g>\n<g font-size='13' fill='#333'>\n<rect x='8' y='20' width='150' height='44' rx='12' fill='#ffffff' stroke='#999'/><text x='83' y='38' text-anchor='middle'>Laut Studie ist es</text><text x='83' y='55' text-anchor='middle'>eher umgekehrt …</text>\n<rect x='8' y='370' width='150' height='44' rx='12' fill='#ffffff' stroke='#999'/><text x='83' y='388' text-anchor='middle'>Willst du auch die</text><text x='83' y='405' text-anchor='middle'>andere Seite hören?</text>\n<rect x='400' y='395' width='210' height='34' rx='12' fill='#ffffff' stroke='#999'/><text x='505' y='417' text-anchor='middle'>Moment, das stimmt so nicht!</text>\n</g>\n<g font-size='12' fill='#b5302a' font-weight='bold'>\n<text x='150' y='88'>PLOPP!</text><text x='120' y='365'>PLOPP!</text><text x='440' y='385'>PLOPP!</text>\n</g>\n<path d='M505 225 L560 225' stroke='#777' stroke-width='10'/>\n<rect x='560' y='200' width='26' height='60' rx='6' fill='#999'/>\n<rect x='600' y='150' width='120' height='130' rx='18' fill='#b8c4d6' stroke='#4a5568' stroke-width='3'/>\n<circle cx='635' cy='190' r='12' fill='#ffffff' stroke='#4a5568' stroke-width='2'/><circle cx='685' cy='190' r='12' fill='#ffffff' stroke='#4a5568' stroke-width='2'/>\n<circle cx='635' cy='190' r='5' fill='#14213d'/><circle cx='685' cy='190' r='5' fill='#14213d'/>\n<path d='M630 225 Q660 248 690 225' fill='none' stroke='#4a5568' stroke-width='3'/>\n<path d='M660 150 L660 125' stroke='#4a5568' stroke-width='3'/><circle cx='660' cy='120' r='7' fill='#f1c40f'/>\n<rect x='608' y='250' width='104' height='22' rx='4' fill='#14213d'/><text x='660' y='266' text-anchor='middle' font-size='12' fill='#ffffff' font-weight='bold'>ALGORITHMUS</text>\n<path d='M600 230 L586 230' stroke='#4a5568' stroke-width='8'/>\n<rect x='575' y='300' width='175' height='52' rx='8' fill='#fff3cc' stroke='#d9a400'/>\n<text x='662' y='322' text-anchor='middle' font-size='13' fill='#6a4b00' font-weight='bold'>Wohlfühlklima</text>\n<text x='662' y='340' text-anchor='middle' font-size='12' fill='#6a4b00'>garantiert – rund um die Uhr!</text>\n</svg>",
        'beschreibung': "Die Karikatur zeigt in der Mitte eine große, durchsichtige Blase. Darin sitzt eine junge Person zufrieden lächelnd auf einem roten Sitzsack und schaut auf ihr Smartphone. In der Blase schweben zustimmende Sprechblasen: 'Genau so!', 'Du hast recht!', 'Sehe ich auch so!', '100 % wahr!'. Außerhalb der Blase stehen Sprechblasen mit abweichenden Stimmen ('Laut Studie ist es eher umgekehrt …', 'Willst du auch die andere Seite hören?', 'Moment, das stimmt so nicht!'); an der Blasenwand steht jeweils 'PLOPP!' – die Stimmen prallen ab. Rechts steht ein freundlich lächelnder Roboter mit der Aufschrift 'ALGORITHMUS', der die Blase über eine Pumpe aufbläst. Ein Schild darunter verspricht: 'Wohlfühlklima garantiert – rund um die Uhr!'.",
        'quelle': 'Übungsmaterial: eigene Zeichnung für Feibitur (2026).',
    },
    {
        'id': 'm3',
        'titel': 'M3: Kommentar „Wenn die Lokalzeitung stirbt“ (2025)',
        'absaetze': [
            'Als die Lokalredaktion in unserer Kreisstadt im vergangenen Jahr geschlossen wurde, gab es keinen Aufschrei. Ein paar Leserbriefe, ein Abschiedsartikel, dann war Schluss. Seitdem sitzt bei den Sitzungen des Stadtrats niemand mehr auf der Pressebank. Wer wissen will, was beschlossen wurde, muss die Protokolle selbst lesen – oder sich auf das verlassen, was in Facebook-Gruppen erzählt wird.',
            'Die Gründe für das Zeitungssterben sind bekannt. Anzeigen, mit denen Verlage früher den größten Teil ihres Geldes verdienten, sind zu großen Online-Plattformen abgewandert. Die Auflagen sinken seit Jahren, die Kosten für Papier und Zustellung steigen. Viele Verlage reagieren mit Sparprogrammen: Redaktionen werden zusammengelegt, Lokalteile ausgedünnt, Texte mehrfach verwendet.',
            'Man könnte sagen: So ist der Markt. Wer keine Zeitung mehr kauft, bekommt eben keine. Doch Lokaljournalismus ist kein beliebiges Produkt. Er kontrolliert Bürgermeister und Gemeinderäte, berichtet über Bauprojekte, Schulschließungen und Vereinsleben. Studien aus den USA deuten darauf hin, dass dort, wo Lokalzeitungen verschwinden, weniger Menschen kandidieren und wählen gehen und die Kontrolle öffentlicher Ausgaben nachlässt.',
            'Die Lücke füllen andere: Gratisblätter, die vor allem Pressemitteilungen abdrucken, oder Social-Media-Gruppen, in denen Gerüchte schneller verbreitet werden als Fakten. Für eine Demokratie, die vor Ort beginnt, ist das gefährlich.',
            'Deshalb sollte der Staat den Lokaljournalismus fördern – nicht durch Einfluss auf Inhalte, sondern durch staatsferne Modelle: Zuschüsse zur Zustellung, steuerliche Erleichterungen für gemeinnützigen Journalismus oder unabhängige Stiftungen, die Recherchen finanzieren. Wer jetzt nichts tut, wird sich in ein paar Jahren wundern, warum niemand mehr weiß, was im eigenen Rathaus passiert.',
        ],
        'quelle': 'Übungsmaterial: eigens für Feibitur verfasster Kommentar einer fiktiven Autorin (2025).',
    },
]

AUFGABEN = [
    {
        'id': 'q1-4-i1',
        'afb': 'I',
        'operator': 'zusammenfassen',
        'text': 'Fassen Sie die Aussagen des Textes zusammen. (M1)',
        'material': ['m1'],
        'loesung': {
            'vorbemerkung': 'Einleitung: Gastbeitrag einer (fiktiven) Medienwissenschaftlerin, „Die Wahl entscheidet sich im Feed“, 2026; Thema: Gefährdung von Wahlen durch KI-Fälschungen und Algorithmen, Forderung nach Vorabprüfung.',
            'punkte': [
                'Fiktives Szenario eines Deepfake-Videos kurz vor einer Wahl, schnelle Verbreitung, Richtigstellung erreicht wenige [1].',
                'Szenario sei realistisch: einfache KI-Fälschung; Plattformen belohnen Überraschung, Empörung und Angst [2].',
                'Personalisierte Feeds und geschlossene Gruppen führen zu Bestätigung eigener Meinungen; gemeinsame Faktengrundlage werde brüchig [3].',
                'Klassische Medien prüfen und trennen Nachricht und Meinung, verlieren aber Reichweite; Lokalredaktionen schließen; Plattformen sparen an Moderation [4].',
                'DSA verpflichtet zur Risikobewertung, reiche aber nicht; Forderung: Vorabprüfung reichweitenstarker politischer Inhalte vier Wochen vor Wahlen, Strafen [5].',
                'Zensur-Einwand wird zurückgewiesen; Schutz der Wahlen als Fundament der Demokratie [6].',
            ],
            'hinweis': 'Zusammenfassen: strukturiert, komprimiert, indirekte Rede, Fachsprache, keine Wertung.',
        },
        'bewertung': {
            'ausreichend': 'die Aussagen des Textes im Ansatz korrekt zusammengefasst werden',
            'gut': 'die Aussagen des Textes weitgehend korrekt, strukturiert und in eigenen Worten zusammengefasst werden',
        },
    },
    {
        'id': 'q1-4-i2',
        'afb': 'I',
        'operator': 'beschreiben',
        'material': ['m2'],
        'text': 'Beschreiben Sie die Karikatur (M2).',
        'loesung': {
            'punkte': [
                'Formale Angaben: Karikatur „Wohlfühlklima“, eigene Zeichnung, 2026.',
                'Bildmitte: große, durchsichtige Blase; darin eine junge Person auf einem Sitzsack, lächelnd, mit Smartphone.',
                'In der Blase zustimmende Sprechblasen („Genau so!“, „Du hast recht!“, „Sehe ich auch so!“, „100 % wahr!“).',
                'Außerhalb: Sprechblasen mit abweichenden Positionen und Einwänden; an der Blasenwand „PLOPP!“ – die Stimmen prallen ab.',
                'Rechts: lächelnder Roboter „ALGORITHMUS“, der die Blase mit einer Pumpe aufbläst; Schild „Wohlfühlklima garantiert – rund um die Uhr!“.',
                'Bildaufbau (Mitte–rechts–Ränder) strukturiert beschreiben.',
            ],
            'hinweis': "Beschreiben: nur das Sichtbare, noch keine Deutung (z. B. noch nicht 'Filterblase' als Erklärung verwenden, allenfalls als Benennung am Ende).",
        },
        'bewertung': {
            'ausreichend': 'die wesentlichen Bildelemente im Ansatz korrekt beschrieben werden.',
            'gut': 'die Karikatur vollständig, strukturiert (Bildaufbau) und präzise beschrieben wird, ohne vorzeitig zu deuten.',
        },
    },
    {
        'id': 'q1-4-i3',
        'afb': 'I',
        'operator': 'zusammenfassen',
        'material': ['m3'],
        'text': 'Fassen Sie den Kommentar (M3) zusammen.',
        'loesung': {
            'vorbemerkung': 'Einleitungssatz: Kommentar „Wenn die Lokalzeitung stirbt“ (2025) einer (fiktiven) Autorin über die Folgen des Zeitungssterbens.',
            'punkte': [
                'Beispiel: Schließung der Lokalredaktion ohne große Reaktion; seitdem keine Presse mehr bei Stadtratssitzungen, Information über Protokolle oder Social-Media-Gruppen [1].',
                'Ursachen: Abwanderung der Anzeigen zu Online-Plattformen, sinkende Auflagen, steigende Kosten; Sparprogramme der Verlage [2].',
                'Lokaljournalismus sei kein beliebiges Produkt: Kontrolle der Kommunalpolitik, Berichterstattung über das Gemeinwesen; US-Studien deuteten auf weniger Kandidaturen, geringere Wahlbeteiligung und schwächere Ausgabenkontrolle hin [3].',
                'Lücke werde von Gratisblättern und Gerüchten in sozialen Medien gefüllt – Gefahr für die Demokratie vor Ort [4].',
                'Forderung: staatsferne Förderung (Zustellzuschüsse, Steuererleichterungen für gemeinnützigen Journalismus, Stiftungen) [5].',
            ],
            'hinweis': 'Zusammenfassen: Einleitungssatz, Struktur, indirekte Rede, keine Wertung.',
        },
        'bewertung': {
            'ausreichend': 'die Aussagen des Kommentars im Ansatz korrekt und mit Einleitung zusammengefasst werden.',
            'gut': 'die Aussagen weitgehend vollständig, strukturiert und in eigenen Worten zusammengefasst werden.',
        },
    },
    {
        'id': 'q1-4-ii1',
        'afb': 'II',
        'operator': 'erklären',
        'text': 'Erklären Sie, wie Filterblasen und Echokammern entstehen können. (M1)',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Filterblase (Eli Pariser): algorithmische Personalisierung auf Basis von Interaktionsdaten (Likes, Verweildauer, Suchverlauf); Plattformen optimieren auf Aufmerksamkeit, um Werbeeinnahmen zu steigern.',
                'Verstärkungskreislauf: Interaktion → Profil → angepasster Feed → Bestätigung → weitere Interaktion; Gegenpositionen werden seltener angezeigt.',
                'Echokammer: Selbstselektion der Nutzer in Gruppen Gleichgesinnter, gegenseitige Bestätigung (Confirmation Bias, Gruppendruck); abweichende Informationen werden abgewertet.',
                'Rolle von Emotionalisierung, Social Bots und Desinformation als Verstärker.',
                'Differenzierung: Effektstärke empirisch umstritten; Mehrquellennutzung relativiert die Gefahr.',
                'Bezüge zum Material [2], [3].',
            ],
            'hinweis': 'Erklären: Rückführung auf Funktionsweisen (Geschäftsmodell, Algorithmus, psychologische Mechanismen).',
        },
        'bewertung': {
            'ausreichend': 'die Entstehung von Filterblasen und Echokammern ansatzweise erklärt wird',
            'gut': 'die Entstehung von Filterblasen und Echokammern differenziert und auf Funktionsmechanismen zurückgeführt erklärt wird',
        },
    },
    {
        'id': 'q1-4-ii2',
        'afb': 'II',
        'operator': 'vergleichen',
        'text': 'Vergleichen Sie klassische Massenmedien und soziale Netzwerke hinsichtlich ihrer Funktionen für die politische Öffentlichkeit.',
        'material': [],
        'loesung': {
            'punkte': [
                'Vergleichskriterien benennen (z. B. Information, Meinungsbildung/Forum, Kritik und Kontrolle, Gatekeeping/Qualitätssicherung, Zugang/Partizipation, Reichweite bei Jugendlichen, Geschäftsmodell).',
                'Klassische Massenmedien: redaktionelle Prüfung, Trennung von Nachricht und Kommentar, Pressekodex, investigativer Journalismus („vierte Gewalt“), aber Einbahnstraße, Auswahl nach Nachrichtenfaktoren, sinkende Reichweite/ökonomischer Druck.',
                'Soziale Netzwerke: niedrige Zugangshürden, Interaktivität, Partizipation, schnelle Mobilisierung, direkte Kommunikation von Politikern; aber algorithmische statt redaktioneller Auswahl, Desinformation, Hassrede, Fragmentierung.',
                'Gemeinsamkeiten (z. B. beide leisten Agenda-Setting, beide sind wirtschaftlich orientiert) und Unterschiede begründet darlegen; Fazit des Vergleichs.',
            ],
            'hinweis': "Vergleichen: kriteriengeleitet Gemeinsamkeiten UND Unterschiede; ein bloßes Nacheinander beider Seiten ohne Gegenüberstellung genügt nicht für 'gut'.",
        },
        'bewertung': {
            'ausreichend': 'klassische Medien und soziale Netzwerke ansatzweise kriteriengeleitet verglichen werden',
            'gut': 'der Vergleich kriteriengeleitet, differenziert und mit Gemeinsamkeiten und Unterschieden erfolgt',
        },
    },
    {
        'id': 'q1-4-ii3',
        'afb': 'II',
        'operator': 'analysieren',
        'material': ['m2'],
        'text': 'Analysieren Sie die Karikatur (M2) im Hinblick auf ihre Aussage über politische Kommunikation in sozialen Medien.',
        'loesung': {
            'punkte': [
                'Deutung der Blase als Filterblase/Echokammer: Nutzer erhalten vor allem bestätigende Inhalte; Gegenpositionen und Faktenchecks dringen nicht durch („PLOPP!“).',
                'Roboter „ALGORITHMUS“: Personalisierungsalgorithmen der Plattformen erzeugen und verstärken die Blase aktiv; freundliches Lächeln und Werbeschild verweisen auf das Geschäftsmodell (Aufmerksamkeitsökonomie: Wohlfühlen = Verweildauer = Werbeeinnahmen).',
                'Person: zufrieden, passiv, merkt die Abschottung nicht – Kritik an mangelnder Medienkompetenz bzw. an der Bequemlichkeit der Bestätigung (Confirmation Bias).',
                'Sprechblasen außen: Wissenschaft, Pluralität, Widerspruch – Grundlage demokratischer Öffentlichkeit, die verloren geht.',
                'Kernaussage: Algorithmen sozialer Medien gefährden eine gemeinsame, pluralistische Öffentlichkeit, indem sie Nutzer in bequeme Bestätigungsräume einschließen.',
                'Fachbegriffe: Filterblase (Pariser), Echokammer, Fragmentierung der Öffentlichkeit, Gatekeeper, Polarisierung.',
            ],
            'hinweis': 'Analysieren: Bildelemente systematisch deuten und auf Fachkonzepte beziehen; Bildbelege angeben.',
        },
        'bewertung': {
            'ausreichend': 'zentrale Bildelemente ansatzweise zutreffend gedeutet und eine Kernaussage formuliert wird.',
            'gut': 'die Bildelemente systematisch, mit Fachbegriffen und Bezug zum Geschäftsmodell der Plattformen gedeutet werden und eine präzise Kernaussage formuliert wird.',
        },
    },
    {
        'id': 'q1-4-ii4',
        'afb': 'II',
        'operator': 'erläutern',
        'material': ['m3'],
        'lk': True,
        'text': 'Erläutern Sie ausgehend von M3, inwiefern Medien als Wirtschaftsunternehmen in einem Spannungsverhältnis zu ihrer öffentlichen Aufgabe stehen.',
        'loesung': {
            'punkte': [
                'Öffentliche Aufgabe: Information, Meinungsbildung, Kritik und Kontrolle („vierte Gewalt“), Schutz durch Art. 5 GG.',
                'Wirtschaftliche Logik: Finanzierung über Werbung und Verkauf; Gewinnerwartung; Abwanderung der Werbung zu Plattformen (M3 [2]).',
                'Folgen der Spannung: Kostendruck, Stellenabbau, Zusammenlegung von Redaktionen, weniger Recherche, Boulevardisierung/Clickbait, Medienkonzentration, Verschwinden von Lokaljournalismus („News Deserts“, M3 [1], [3]).',
                'Beispiele und Gegenmodelle: öffentlich-rechtlicher Rundfunk (Beitragsfinanzierung), Stiftungs- und gemeinnütziger Journalismus, Abos/Paywalls.',
            ],
            'hinweis': 'Erläutern: Spannungsverhältnis mit Beispielen und Materialbezug veranschaulichen.',
        },
        'bewertung': {
            'ausreichend': 'das Spannungsverhältnis ansatzweise mit Beispielen erläutert wird.',
            'gut': 'das Spannungsverhältnis differenziert, mit Bezug zu M3, Fachbegriffen und Gegenmodellen erläutert wird.',
        },
    },
    {
        'id': 'q1-4-iii1',
        'afb': 'III',
        'operator': 'diskutieren',
        'text': 'Die Autorin fordert eine Pflicht für Plattformen, politische Inhalte vor Wahlen vorab zu prüfen. Diskutieren Sie diese Forderung. (M1)',
        'material': ['m1'],
        'loesung': {
            'punkte': [
                'Pro: Schutz der Integrität von Wahlen und der Chancengleichheit der Parteien; Deepfakes sind schwer rechtzeitig zu widerlegen; Plattformen tragen Verantwortung für ihre Algorithmen; Ergänzung des DSA; abschreckende Wirkung von Strafen.',
                'Contra: Gefahr der Vorzensur (Art. 5 Abs. 1 Satz 3 GG: „Eine Zensur findet nicht statt“ – wenn auch primär gegen den Staat gerichtet), Overblocking (Plattformen löschen im Zweifel zu viel), schwierige Abgrenzung von Satire, Meinung und Falschbehauptung; private Konzerne entscheiden über politische Inhalte; technische und personelle Machbarkeit; Verlagerung auf andere Kanäle (Messenger); Gefahr des Missbrauchs durch Regierungen; DSA-Pflichten bereits vorhanden.',
                'Alternativen: Kennzeichnungspflicht für KI-Inhalte, schnelle Faktenchecks, Transparenz der Algorithmen, Medienkompetenz, Stärkung von Qualitätsjournalismus.',
                'Begründete Bewertung am Ende (Abwägung Freiheit vs. Schutz der demokratischen Willensbildung).',
            ],
            'hinweis': 'Diskutieren: Argumentation mit Pro und Contra, die zu einer begründeten Bewertung führt; Bezug auf die konkrete Forderung [5] notwendig.',
        },
        'bewertung': {
            'ausreichend': 'die Diskussion ansatzweise strukturiert ist und in eine ansatzweise nachvollziehbare, begründete Bewertung mündet.',
            'gut': 'die Diskussion strukturiert und weitgehend kohärent ist und in eine weitgehend klare und schlüssig begründete Bewertung mündet.',
        },
    },
    {
        'id': 'q1-4-iii2',
        'afb': 'III',
        'operator': 'Stellung nehmen',
        'material': ['m3'],
        'text': 'Nehmen Sie Stellung zu der Forderung der Autorin, den Lokaljournalismus staatlich zu fördern (M3).',
        'loesung': {
            'punkte': [
                'Pro: Lokaljournalismus als demokratisches Gut (Kontrolle, Information, Partizipation); Marktversagen bei öffentlichen Gütern; staatsferne Modelle möglich (Zustellförderung, Gemeinnützigkeit, Stiftungen); Vorbilder in anderen Staaten.',
                'Contra: Gefahr der Abhängigkeit und Selbstzensur (Staatsferne als Verfassungsgebot aus Art. 5 GG); Verzerrung des Wettbewerbs; Subventionierung überholter Geschäftsmodelle; Frage, wer förderwürdig ist; Kosten für Steuerzahler.',
                'Alternativen/Bedingungen: unabhängige Vergabegremien, inhaltsneutrale Kriterien, Förderung digitaler Angebote, Medienkompetenz.',
                'Eigene Wertmaßstäbe offenlegen und begründen (z. B. Vorrang demokratischer Teilhabe vs. Vorrang von Staatsferne/Marktfreiheit) und klare Position.',
            ],
            'hinweis': 'Stellung nehmen: Ohne ausdrücklich begründete eigene Wertmaßstäbe ist der Operator nur teilweise erfüllt.',
        },
        'bewertung': {
            'ausreichend': 'eine ansatzweise begründete Stellungnahme mit erkennbaren eigenen Maßstäben vorliegt.',
            'gut': 'die Stellungnahme abwägend, fachlich fundiert (Art. 5 GG, Staatsferne, Medienökonomie) ist, eigene Wertmaßstäbe ausdrücklich offenlegt und in ein klares Urteil mündet.',
        },
    },
    {
        'id': 'q1-4-iii3',
        'afb': 'III',
        'operator': 'beurteilen',
        'material': ['m2'],
        'text': 'Beurteilen Sie die Aussage der Karikatur (M2) vor dem Hintergrund Ihrer Kenntnisse über die Wirkung von Algorithmen in sozialen Medien.',
        'loesung': {
            'punkte': [
                'Kriterien benennen (z. B. empirische Stichhaltigkeit, Vollständigkeit der Darstellung, Folgen für die Demokratie).',
                'Zutreffend: Personalisierung und Optimierung auf Aufmerksamkeit sind belegt; emotionale, bestätigende Inhalte werden bevorzugt; Echokammern in geschlossenen Gruppen; Gefahr von Polarisierung und Desinformation.',
                'Zugespitzt/einseitig: Forschung findet häufig schwächere Filterblaseneffekte; viele Nutzer kombinieren Quellen und begegnen auch Gegenpositionen; Selbstselektion der Nutzer spielt eine große Rolle (nicht nur der Algorithmus); Plattformen unterscheiden sich; Regulierung (DSA) und Medienkompetenz als Gegenkräfte bleiben unberücksichtigt.',
                'Begründetes Urteil (z. B. Kernaussage als Warnung berechtigt, Darstellung als totale Abschottung überzeichnet – typisch für Karikaturen).',
            ],
            'hinweis': 'Beurteilen: kriteriengeleitet, Bezug auf Forschungsstand und Bildelemente.',
        },
        'bewertung': {
            'ausreichend': 'die Aussage der Karikatur ansatzweise kriteriengeleitet beurteilt wird.',
            'gut': 'die Aussage differenziert, mit Fachwissen zum Forschungsstand und zur Funktionsweise von Algorithmen beurteilt und schlüssig begründet wird.',
        },
    },
]
