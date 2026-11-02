# -*- coding: utf-8 -*-
"""G3 Was gehört in ein Werturteil?"""

SVG_WERTE = """<svg viewBox='0 0 760 320' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' font-size='13' role='img' aria-labelledby='wkt'>
<title id='wkt'>Vom Sachurteil zum Werturteil</title>
<rect width='760' height='320' fill='#fff'/>
<text x='380' y='24' text-anchor='middle' font-weight='700' font-size='15' fill='#14213d'>Werturteil = Sachurteil + offengelegte eigene Wertmaßstäbe</text>
<rect x='30' y='50' width='300' height='150' rx='14' fill='#eef2fb' stroke='#14213d'/>
<text x='180' y='78' text-anchor='middle' font-weight='700' fill='#14213d'>Sachurteil („beurteilen“)</text>
<text x='180' y='104' text-anchor='middle' fill='#333'>Kriterien: Effektivität, Effizienz,</text>
<text x='180' y='124' text-anchor='middle' fill='#333'>Legitimität, Folgen …</text>
<text x='180' y='150' text-anchor='middle' fill='#333'>„Ein Tempolimit senkt nach</text>
<text x='180' y='170' text-anchor='middle' fill='#333'>Studien Emissionen und Unfälle.“</text>
<text x='380' y='132' text-anchor='middle' font-size='34' font-weight='700' fill='#b5302a'>+</text>
<rect x='430' y='50' width='300' height='150' rx='14' fill='#fff7e0' stroke='#d9a400'/>
<text x='580' y='78' text-anchor='middle' font-weight='700' fill='#6a4b00'>Eigene Wertmaßstäbe</text>
<text x='580' y='104' text-anchor='middle' fill='#333'>Welche Werte haben für mich</text>
<text x='580' y='124' text-anchor='middle' fill='#333'>Vorrang – und warum?</text>
<text x='580' y='150' text-anchor='middle' fill='#333'>„Für mich wiegt Sicherheit</text>
<text x='580' y='170' text-anchor='middle' fill='#333'>schwerer als Freiheit, weil …“</text>
<rect x='130' y='230' width='500' height='66' rx='14' fill='#14213d'/>
<text x='380' y='258' text-anchor='middle' font-weight='700' fill='#fff'>Werturteil („bewerten“ / „Stellung nehmen“)</text>
<text x='380' y='280' text-anchor='middle' fill='#dfe6f7'>begründete Entscheidung im Wertkonflikt, nachvollziehbar für andere</text>
</svg>"""

TOPIC = {
    "id": "g3",
    "begriffe": [],  # Grundlagen: bewusst ohne Fachbegriffe/Karteikarten
    "inhalte": [
        {"t": "text", "art": "Erklärung", "titel": "Was unterscheidet das Werturteil vom Sachurteil?",
         "html": "<p>Laut hessischer Operatorenliste bedeutet <b>„bewerten/Stellung nehmen“</b>: „wie Operator ‚beurteilen‘, aber zusätzlich die eigenen Maßstäbe begründet darlegen“. Das Werturteil <b>baut also auf dem Sachurteil auf</b>. Du prüfst zuerst die Sache (Kriterien, Fachwissen, Belege) und entscheidest dann, welcher Wert für dich Vorrang hat, und legst offen, warum.</p><p>Auch <b>„diskutieren“</b> und <b>„erörtern“</b> führen zu einer begründeten Bewertung bzw. einem eigenen Urteil; dort steht das Abwägen von Pro und Contra im Vordergrund.</p>"},
        {"t": "svg", "art": "Schaubild", "titel": "Die Formel des Werturteils", "svg": SVG_WERTE,
         "caption": "Ohne offengelegten Wertmaßstab bleibt die Aufgabe „bewerten“ nur teilweise erfüllt."},
        {"t": "table", "art": "Merke", "titel": "Wichtige Wertmaßstäbe und typische Konflikte",
         "kopf": ["Wert", "Bezug im Grundgesetz", "steht oft in Konflikt mit …", "Beispiel"],
         "zeilen": [
             ["Freiheit", "Art. 2, 5, 8, 12 GG", "Sicherheit, Gleichheit, Nachhaltigkeit", "Tempolimit, Überwachung, Klimaschutzauflagen"],
             ["Sicherheit", "Art. 2 Abs. 2 GG (Schutzpflicht)", "Freiheit, Datenschutz", "Vorratsdatenspeicherung"],
             ["Gleichheit / Gerechtigkeit", "Art. 3 GG, Sozialstaat (Art. 20)", "Freiheit, Leistungsanreize", "Erbschaftsteuer, Grundsicherung"],
             ["Solidarität", "Sozialstaatsprinzip", "Eigenverantwortung", "Rentenniveau, Gesundheitssystem"],
             ["Nachhaltigkeit", "Art. 20a GG", "kurzfristiger Wohlstand, Freiheit", "Kohleausstieg, CO<sub>2</sub>-Preis"],
             ["Demokratie / Mitbestimmung", "Art. 20 GG", "Effizienz, Schnelligkeit", "Bürgerbeteiligung bei Großprojekten"],
         ],
         "html": "<p>Der <b>Menschenwürde</b> (Art. 1 GG) kommt eine Sonderstellung zu: Sie ist der Maßstab, an dem alle anderen Abwägungen ihre Grenze finden.</p>"},
        {"t": "text", "art": "Fachtext", "titel": "Werte offenlegen – warum das in der Demokratie wichtig ist",
         "html": "<p>In einer pluralistischen Gesellschaft gibt es keinen von allen geteilten, objektiv richtigen Maßstab für politische Entscheidungen jenseits des Grundkonsenses der Verfassung. Menschen gewichten Freiheit, Sicherheit, Gerechtigkeit oder Nachhaltigkeit unterschiedlich. Politische Konflikte sind deshalb häufig <b>Wertkonflikte</b>: Die Beteiligten streiten nicht nur über Fakten, sondern darüber, was wichtiger ist.</p><p>Ein Werturteil, das seine Maßstäbe offenlegt, leistet dreierlei. Es macht erstens <b>transparent</b>, worauf die eigene Entscheidung beruht, sodass andere sie nachvollziehen und kritisieren können. Es trennt zweitens <b>Fakten von Wertungen</b>: Wer anderer Meinung ist, kann gezielt widersprechen, entweder den Fakten oder der Gewichtung der Werte. Drittens fördert es den <b>Respekt</b> vor anderen Positionen, weil sichtbar wird, dass auch abweichende Urteile auf nachvollziehbaren Werten beruhen können.</p><p>Der Beutelsbacher Konsens der politischen Bildung zieht daraus die Konsequenz, dass Lehrkräfte keine bestimmte Meinung vorgeben dürfen. Für Abiturklausuren bedeutet das: Bewertet wird nicht, <b>welche</b> Position du einnimmst, sondern <b>wie gut</b> du sie begründest. Ausnahme ist der Rahmen des Grundgesetzes. Urteile, die die Menschenwürde oder die freiheitliche demokratische Grundordnung missachten, sind keine gleichwertigen Positionen.</p>",
         "quelle": "Selbst verfasster Fachtext (Feibitur)."},
        {"t": "table", "art": "Merke", "titel": "Aufbau eines Werturteils",
         "kopf": ["Schritt", "Inhalt", "Formulierungshilfe"],
         "zeilen": [
             ["1. Frage und Wertkonflikt", "Urteilsfrage klären, betroffene Werte benennen", "„Bei der Frage nach … stehen sich die Werte … und … gegenüber.“"],
             ["2. Sachliche Grundlage", "zentrale Fakten und Argumente (kurzes Sachurteil)", "„Aus sachlicher Sicht spricht für …, dass …; dagegen …“"],
             ["3. Perspektiven", "Sicht verschiedener Betroffener und Akteure", "„Aus Sicht der … ist besonders wichtig, dass …“"],
             ["4. Eigene Maßstäbe", "eigene Wertentscheidung offenlegen und begründen", "„Für mich hat … Vorrang, weil … / Mein Maßstab ist …“"],
             ["5. Fazit", "klare Position, ggf. mit Bedingungen", "„Ich spreche mich deshalb für/gegen … aus, sofern …“"],
         ]},
        {"t": "text", "art": "Beispiel", "titel": "Schwach vs. stark: Ein Beispiel",
         "html": "<p><b>Schwach:</b> „Ich finde ein Tempolimit schlecht, weil ich gerne schnell fahre.“ → persönliche Vorliebe, keine Kriterien, kein Wertmaßstab, keine Gegenposition.</p><p><b>Stark:</b> „Sachlich spricht für ein Tempolimit, dass es nach Schätzungen des Umweltbundesamtes jährlich Millionen Tonnen CO<sub>2</sub> einsparen und die Zahl schwerer Unfälle senken könnte. Dagegen wird eingewandt, dass der Beitrag zum Klimaschutz im Verhältnis zum gesamten Verkehrssektor begrenzt sei und die individuelle Freiheit eingeschränkt werde. Mein Maßstab ist der Schutz von Leben und Gesundheit (Art. 2 Abs. 2 GG), den ich höher gewichte als die Freiheit, unbegrenzt schnell zu fahren, weil der Eingriff gering ist, während das geschützte Gut sehr hoch ist. Daher befürworte ich ein Tempolimit.“</p>"},
    ],
    "aufgaben": [
        {
            "id": "g3-a1",
            "titel": "Methodentraining Werturteil: Ein Tempolimit auf Autobahnen?",
            "kurs": "Grundkurs und Leistungskurs (Methodentraining)",
            "bezug": "Urteilskompetenz (Werturteil mit offengelegten Wertmaßstäben); inhaltlicher Bezug zu Wertkonflikten (Freiheit, Sicherheit, Nachhaltigkeit) und zum Mehrebenensystem.",
            "standards": "Urteilskompetenz: eigene Entscheidungen argumentativ begründen; sich für eine Lösungsperspektive entscheiden; Wertmaßstäbe reflektieren.",
            "aufgaben": [
                {"nr": 1, "operator": "darstellen", "afb": "I", "be": 20, "text": "Stellen Sie die im Material vertretenen Positionen dar."},
                {"nr": 2, "operator": "herausarbeiten", "afb": "II", "be": 25, "text": "Arbeiten Sie die Werte heraus, auf die sich die beiden Autoren jeweils stützen."},
                {"nr": 3, "operator": "erläutern", "afb": "II", "be": 20, "text": "Erläutern Sie den Wertkonflikt zwischen Freiheit und Sicherheit an einem weiteren politischen Beispiel Ihrer Wahl."},
                {"nr": 4, "operator": "Stellung nehmen", "afb": "III", "be": 35, "text": "Nehmen Sie Stellung zur Einführung eines allgemeinen Tempolimits von 130 km/h auf deutschen Autobahnen."},
            ],
            "material": [
                {"titel": "Material: Pro und Contra „Brauchen wir ein Tempolimit?“ (2025)",
                 "absaetze": [
                     "<b>Pro – eine Verkehrsforscherin (fiktiv):</b> Deutschland ist eines der ganz wenigen Länder der Welt ohne allgemeines Tempolimit auf Autobahnen. Dabei liegen die Vorteile auf der Hand: Wer langsamer fährt, verbraucht weniger Kraftstoff und stößt weniger CO<sub>2</sub> aus. Das Umweltbundesamt hält eine Einsparung von mehreren Millionen Tonnen pro Jahr für möglich – sofort und fast ohne Kosten.",
                     "Noch wichtiger ist mir die Sicherheit. Hohe Geschwindigkeiten machen Unfälle schwerer, und jeder Verkehrstote ist einer zu viel. Ein Tempolimit schützt nicht nur die Raser selbst, sondern alle anderen, die sich auf der Autobahn bewegen. Freiheit endet dort, wo sie das Leben anderer gefährdet. Und mal ehrlich: Wie viel Freiheit verlieren wir wirklich, wenn wir statt 180 nur 130 fahren?",
                     "<b>Contra – ein Wirtschaftsjournalist (fiktiv):</b> Die deutschen Autobahnen gehören, gemessen an der Fahrleistung, zu den sichersten Straßen des Landes. Viele Abschnitte haben bereits Tempolimits, und dort, wo frei gefahren werden darf, fahren die meisten ohnehin nicht schneller als 130. Ein generelles Verbot ist deshalb vor allem Symbolpolitik.",
                     "Mir geht es um ein Prinzip: Der Staat sollte mündigen Bürgerinnen und Bürgern nur dann Vorschriften machen, wenn es wirklich nötig ist. Eigenverantwortung ist ein Wert, den wir nicht leichtfertig aufgeben sollten. Wer Klimaschutz will, sollte auf Maßnahmen setzen, die deutlich mehr bewirken, etwa auf einen wirksamen CO<sub>2</sub>-Preis, der den Menschen die Wahl lässt, wie sie Emissionen einsparen.",
                 ],
                 "quelle": "Übungsmaterial: eigens für Feibitur verfasste Pro- und Contra-Beiträge fiktiver Autoren (2025)."},
            ],
            "loesung": [
                {"punkte": [
                    "Einleitung: Pro-und-Contra-Beiträge (2025) zur Frage eines allgemeinen Tempolimits.",
                    "Pro (Verkehrsforscherin): Deutschland als Ausnahme; Klimaschutz durch geringeren Verbrauch und CO2-Ausstoß, laut UBA Einsparung mehrerer Millionen Tonnen jährlich, sofort und kostengünstig [1]; Sicherheit: geringere Unfallschwere, Schutz Dritter; Freiheit ende bei Gefährdung anderer; geringer Freiheitsverlust [2].",
                    "Contra (Wirtschaftsjournalist): Autobahnen gemessen an Fahrleistung sicher; viele Abschnitte bereits begrenzt; viele fahren ohnehin nicht schneller – Symbolpolitik [3]; Prinzip der Eigenverantwortung und Zurückhaltung des Staates; wirksamere Klimainstrumente (CO2-Preis) mit Wahlfreiheit [4].",
                ],
                 "hinweis": "Darstellen: Positionen und ihre Bezüge/Zusammenhänge strukturiert aufzeigen, ohne zu werten."},
                {"punkte": [
                    "Pro: Sicherheit/Schutz von Leben und Gesundheit (Art. 2 Abs. 2 GG) als vorrangiger Wert („Noch wichtiger ist mir die Sicherheit“ [2]); Nachhaltigkeit/Klimaschutz (Art. 20a GG) [1]; Verständnis von Freiheit als durch die Rechte anderer begrenzte Freiheit [2]; implizit Solidarität/Rücksicht.",
                    "Contra: Freiheit und Eigenverantwortung (allgemeine Handlungsfreiheit, Art. 2 Abs. 1 GG) [4]; Verhältnismäßigkeit/Zurückhaltung des Staates (liberales Staatsverständnis) [4]; Effizienz als Sachkriterium (wirksamere Instrumente) [4]; Ablehnung von Symbolpolitik [3].",
                    "Unterscheidung von empirischen Argumenten (Unfallzahlen, Emissionen) und normativen Argumenten (Vorrang eines Wertes).",
                    "Ggf.: beide Autoren legen ihre Maßstäbe offen („Noch wichtiger ist mir…“, „Mir geht es um ein Prinzip“) – Beispiel für Werturteile.",
                ],
                 "hinweis": "Herausarbeiten: Werte erschließen und fachsprachlich benennen, mit Belegen."},
                {"punkte": [
                    "Klärung des Wertkonflikts: Mehr Sicherheit erfordert oft Eingriffe in Freiheitsrechte; Staat hat Schutzpflicht und muss zugleich Freiheitsrechte achten (Verhältnismäßigkeitsprinzip: geeignet, erforderlich, angemessen).",
                    "Mögliche Beispiele: Videoüberwachung, Vorratsdatenspeicherung/IP-Adressen-Speicherung, Corona-Maßnahmen, Waffenrecht, Messerverbotszonen, Befugnisse der Polizei, Social-Media-Regulierung, Wehrpflichtdebatte.",
                    "Darstellung der Argumente beider Seiten und der Rolle des BVerfG als Schiedsinstanz (z. B. Urteile zur Vorratsdatenspeicherung).",
                ],
                 "hinweis": "Erläutern: Wertkonflikt am gewählten Beispiel mit zusätzlichen Informationen veranschaulichen; das Beispiel muss passend und fachlich korrekt sein."},
                {"punkte": [
                    "Sachliche Grundlage (Kurz-Sachurteil): Effektivität für Klimaschutz und Sicherheit, Verhältnismäßigkeit, Akzeptanz, Durchsetzbarkeit, Alternativen (CO2-Preis), internationale Vergleiche.",
                    "Perspektiven: Pendler, Unfallopfer/Angehörige, Autoindustrie, Umweltverbände, Polizei.",
                    "Offenlegung und Begründung der eigenen Wertmaßstäbe (z. B. Vorrang von Leben/Gesundheit und Nachhaltigkeit oder Vorrang von Freiheit/Eigenverantwortung) – zwingend erforderlich.",
                    "Klare, begründete Position (Zustimmung, Ablehnung oder differenziert, z. B. variable Tempolimits); beide Ergebnisse sind gleichwertig, wenn schlüssig begründet (Beutelsbacher Konsens).",
                ],
                 "hinweis": "Stellung nehmen: Fehlt die ausdrückliche und begründete Offenlegung der eigenen Wertmaßstäbe, ist der Operator nicht vollständig erfüllt (maximal im Bereich 'ausreichend' bis 'befriedigend' für diese Teilaufgabe)."},
            ],
            "bewertung": {
                "ausreichend": ["die Positionen im Ansatz korrekt dargestellt werden,",
                                "die zugrunde liegenden Werte ansatzweise herausgearbeitet werden,",
                                "der Wertkonflikt an einem passenden Beispiel ansatzweise erläutert wird,",
                                "eine ansatzweise begründete Stellungnahme vorliegt, in der eigene Wertmaßstäbe erkennbar werden."],
                "gut": ["die Positionen strukturiert, vollständig und in ihren Zusammenhängen dargestellt werden,",
                        "die Werte differenziert, fachsprachlich präzise und mit Belegen herausgearbeitet werden (inkl. Unterscheidung empirischer und normativer Argumente),",
                        "der Wertkonflikt an einem gut gewählten Beispiel differenziert und fachlich korrekt erläutert wird,",
                        "die Stellungnahme sachlich fundiert, perspektivenreich ist, die eigenen Wertmaßstäbe ausdrücklich begründet offenlegt und in ein klares Urteil mündet."],
            },
        },
    ],
}
