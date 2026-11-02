# -*- coding: utf-8 -*-
"""G2 Was gehört in ein Sachurteil?"""

SVG_URTEIL = """<svg viewBox='0 0 760 300' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' font-size='13' role='img' aria-labelledby='urt'>
<title id='urt'>Aufbau eines Sachurteils</title>
<defs><marker id='a5' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' orient='auto'><path d='M0 0L10 5L0 10z' fill='#14213d'/></marker></defs>
<rect width='760' height='300' fill='#fff'/>
<text x='380' y='24' text-anchor='middle' font-weight='700' font-size='15' fill='#14213d'>Aufbau eines Sachurteils („beurteilen“)</text>
<g text-anchor='middle'>
<rect x='15' y='60' width='130' height='110' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='80' y='88' font-weight='700' fill='#14213d'>1. Frage</text><text x='80' y='110' fill='#333'>Urteilsfrage</text><text x='80' y='128' fill='#333'>präzise</text><text x='80' y='146' fill='#333'>formulieren</text>
<rect x='165' y='60' width='130' height='110' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='230' y='88' font-weight='700' fill='#14213d'>2. Kriterien</text><text x='230' y='110' fill='#333'>z. B. Effektivität,</text><text x='230' y='128' fill='#333'>Effizienz,</text><text x='230' y='146' fill='#333'>Legitimität</text>
<rect x='315' y='60' width='130' height='110' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='380' y='88' font-weight='700' fill='#14213d'>3. Prüfen</text><text x='380' y='110' fill='#333'>Pro und Contra</text><text x='380' y='128' fill='#333'>je Kriterium mit</text><text x='380' y='146' fill='#333'>Fachwissen + Beleg</text>
<rect x='465' y='60' width='130' height='110' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='530' y='88' font-weight='700' fill='#14213d'>4. Abwägen</text><text x='530' y='110' fill='#333'>Gewichten:</text><text x='530' y='128' fill='#333'>Was wiegt</text><text x='530' y='146' fill='#333'>schwerer? Warum?</text>
<rect x='615' y='60' width='130' height='110' rx='12' fill='#14213d'/><text x='680' y='88' font-weight='700' fill='#fff'>5. Fazit</text><text x='680' y='110' fill='#dfe6f7'>klares,</text><text x='680' y='128' fill='#dfe6f7'>begründetes</text><text x='680' y='146' fill='#dfe6f7'>Urteil</text>
</g>
<g stroke='#14213d' stroke-width='1.6'><path d='M145 115 H163' marker-end='url(#a5)'/><path d='M295 115 H313' marker-end='url(#a5)'/><path d='M445 115 H463' marker-end='url(#a5)'/><path d='M595 115 H613' marker-end='url(#a5)'/></g>
<rect x='15' y='200' width='730' height='70' rx='12' fill='#fff7e0' stroke='#d9a400'/>
<text x='380' y='226' text-anchor='middle' font-weight='700' fill='#6a4b00'>Sachurteil = Urteil über die Sache auf Basis von Kriterien, Fachwissen und Fachmethoden.</text>
<text x='380' y='250' text-anchor='middle' fill='#333'>Die eigenen Wertmaßstäbe müssen (anders als beim Werturteil) nicht offengelegt werden.</text>
</svg>"""

TOPIC = {
    "id": "g2",
    "begriffe": [
        {"b": "Sachurteil", "kurz": "begründete Einschätzung eines Sachverhalts auf Basis von Kriterien, Fachwissen und Fachmethoden (Operator „beurteilen“).",
         "lang": "Ein <b>Sachurteil</b> beantwortet z. B., ob eine Maßnahme ihr Ziel erreicht, welche Folgen sie hat oder ob eine Aussage zutrifft. Es stützt sich auf <b>Kriterien, Fachwissen und Belege</b>. Laut Operatorenliste entspricht es dem Operator <b>„beurteilen“</b>: „… eine begründete Einschätzung geben“."},
        {"b": "Werturteil", "kurz": "Urteil, das zusätzlich die eigenen Wertmaßstäbe begründet offenlegt (Operatoren „bewerten“, „Stellung nehmen“).",
         "lang": "Ein <b>Werturteil</b> geht über das Sachurteil hinaus: Du legst offen, <b>welche Werte</b> dir bei der Entscheidung wichtig sind (z. B. Freiheit, Gerechtigkeit, Sicherheit) und warum. Operatoren: <b>„bewerten“ / „Stellung nehmen“</b> = „wie ‚beurteilen‘, aber zusätzlich die eigenen Maßstäbe begründet darlegen“."},
        {"b": "Urteilskriterium", "kurz": "Maßstab, nach dem ein Sachverhalt beurteilt wird (z. B. Effektivität, Effizienz, Legitimität, Akzeptanz).",
         "lang": "Ein <b>Kriterium</b> ist der Prüfmaßstab deines Urteils. Ohne Kriterien bleibt ein Urteil eine bloße Meinung. Nenne deine Kriterien ausdrücklich („Im Hinblick auf die Effektivität …“) und prüfe den Sachverhalt an jedem Kriterium."},
        {"b": "Effektivität", "kurz": "Wirksamkeit: Wird das angestrebte Ziel tatsächlich erreicht?",
         "lang": "<b>Effektivität</b> fragt: <b>Wirkt</b> eine Maßnahme? Erreicht z. B. ein Handyverbot wirklich mehr Konzentration im Unterricht? Belege können Studien, Erfahrungen anderer Länder oder Daten sein."},
        {"b": "Effizienz", "kurz": "Wirtschaftlichkeit: Steht der Aufwand (Kosten, Zeit) in einem guten Verhältnis zum Nutzen?",
         "lang": "<b>Effizienz</b> fragt nach dem <b>Verhältnis von Aufwand und Ertrag</b>: Wird das Ziel mit möglichst geringen Kosten erreicht, oder gäbe es günstigere Wege? Eine Maßnahme kann effektiv, aber ineffizient sein (wirksam, aber sehr teuer)."},
        {"b": "Legitimität", "kurz": "Rechtmäßigkeit und Anerkennungswürdigkeit einer Entscheidung (Verfassungskonformität, demokratisches Verfahren).",
         "lang": "<b>Legitimität</b> fragt: Ist eine Entscheidung <b>rechtmäßig</b> (vereinbar mit Grundgesetz und Gesetzen) und auf einem <b>fairen, demokratischen Weg</b> zustande gekommen (Beteiligung, Transparenz, Zuständigkeit)? In der Politikdidaktik wird Legitimität oft der Effizienz als zweite Hauptkategorie gegenübergestellt."},
        {"b": "Akzeptanz", "kurz": "Grad der Zustimmung der Betroffenen und der Bevölkerung zu einer Maßnahme.",
         "lang": "<b>Akzeptanz</b> fragt, ob die Betroffenen eine Maßnahme mittragen. Ohne Akzeptanz werden Regeln umgangen oder es entsteht Protest. Achtung: Akzeptanz allein macht eine Maßnahme nicht richtig – auch unpopuläre Entscheidungen können sachlich geboten sein."},
        {"b": "Durchsetzbarkeit", "kurz": "Frage, ob eine Maßnahme praktisch umgesetzt und kontrolliert werden kann (Machbarkeit).",
         "lang": "Die <b>Durchsetzbarkeit</b> oder Machbarkeit prüft: Gibt es Mehrheiten (Bundestag, Bundesrat)? Ist die Maßnahme rechtlich möglich (EU-Recht, GG)? Gibt es Personal und Geld? Lässt sich ihre Einhaltung kontrollieren?"},
        {"b": "Nebenfolgen", "kurz": "unbeabsichtigte Auswirkungen einer Maßnahme, die bei der Beurteilung berücksichtigt werden müssen.",
         "lang": "Jede Maßnahme hat <b>Nebenfolgen</b>: Ein Verbot kann Ausweichverhalten erzeugen, eine Steuer kann Arbeitsplätze verlagern. Gute Urteile schätzen auch mögliche Folgen unterschiedlicher Lösungsansätze ab (Kompetenz „U2“ in den Lösungshinweisen des Landesabiturs)."},
        {"b": "Perspektivenwechsel", "kurz": "Betrachtung eines Problems aus Sicht verschiedener Akteure und Betroffener.",
         "lang": "Ein differenziertes Urteil berücksichtigt <b>verschiedene Perspektiven</b>: Betroffene (z. B. Schüler, Eltern, Lehrkräfte), politische Akteure (Regierung, Opposition, Verbände) und die <b>Systemperspektive</b> (Was bedeutet das für Demokratie, Wirtschaft, Gesellschaft insgesamt?)."},
        {"b": "Abwägung", "kurz": "Gewichtung der Pro- und Contra-Argumente, um zu einem begründeten Ergebnis zu kommen.",
         "lang": "Bei der <b>Abwägung</b> zählst du nicht einfach Argumente, sondern <b>gewichtest</b> sie: Welches Argument ist stärker, weil es z. B. mehr Menschen betrifft, langfristiger wirkt oder besser belegt ist? Formulierung: „Schwerer wiegt jedoch …, weil …“."},
        {"b": "Differenziertes Urteil", "kurz": "Urteil, das Einschränkungen und Bedingungen benennt (z. B. „grundsätzlich ja, aber nur wenn …“).",
         "lang": "Ein <b>differenziertes Urteil</b> ist kein Ausweichen, sondern eine präzise Antwort mit <b>Bedingungen</b>: „Ein Handyverbot ist für jüngere Jahrgänge sinnvoll, in der Oberstufe aber nur mit Ausnahmen für den Unterricht.“ Wichtig: Am Ende muss trotzdem eine klare Position stehen."},
        {"b": "Kontroversität", "kurz": "Grundsatz, dass das, was in Wissenschaft und Politik umstritten ist, auch im Unterricht kontrovers dargestellt werden muss.",
         "lang": "Das <b>Kontroversitätsgebot</b> ist Teil des <b>Beutelsbacher Konsenses</b> (1976) der politischen Bildung. Für dein Urteil heißt das: Berücksichtige auch Gegenpositionen fair, statt nur Argumente für deine Sicht zu sammeln."},
        {"b": "Beleg", "kurz": "Fakt, Zahl, Beispiel, Studie oder Materialbezug, der ein Argument stützt.",
         "lang": "<b>Belege</b> machen Argumente überzeugend: Statistiken, Fallbeispiele, Studienergebnisse, Gesetzestexte (z. B. ein GG-Artikel) oder Zitate aus dem Material. Ohne Beleg bleibt ein Argument eine Behauptung."},
    ],
    "inhalte": [
        {"t": "text", "art": "Erklärung", "titel": "Was ist ein Sachurteil?",
         "html": "<p>In Teilaufgaben des Anforderungsbereichs III sollst du urteilen. Die Operatorenliste des Landes Hessen unterscheidet dabei genau:</p><ul><li><b>beurteilen:</b> „zu einem Sachverhalt oder einer Aussage auf Basis von Kriterien und unter Verwendung von Fachwissen und Fachmethoden eine begründete Einschätzung geben“ → <b>Sachurteil</b></li><li><b>bewerten/Stellung nehmen:</b> „wie Operator ‚beurteilen‘, aber zusätzlich die eigenen Maßstäbe begründet darlegen“ → <b>Werturteil</b> (siehe G3)</li></ul><p>Ein Sachurteil fragt also vor allem: <b>Stimmt das? Wirkt das? Ist das rechtmäßig und machbar? Welche Folgen hat das?</b> Es ist kein Bauchgefühl, sondern eine nachvollziehbare Prüfung.</p>"},
        {"t": "svg", "art": "Schaubild", "titel": "Das Sachurteil in fünf Schritten", "svg": SVG_URTEIL,
         "caption": "Nach diesem Schema kannst du jede „beurteilen“-Aufgabe gliedern."},
        {"t": "table", "art": "Merke", "titel": "Typische Kriterien für Sachurteile",
         "kopf": ["Kriterium", "Leitfrage", "Beispiel (Handyverbot an Schulen)"],
         "zeilen": [
             ["Effektivität", "Erreicht die Maßnahme ihr Ziel?", "Verbessert sich die Konzentration? Sinkt Cybermobbing in der Schule?"],
             ["Effizienz", "Stimmt das Verhältnis von Aufwand und Nutzen?", "Wie viel Kontrollaufwand entsteht für Lehrkräfte?"],
             ["Legitimität / Rechtmäßigkeit", "Ist die Maßnahme verfassungs- und rechtskonform, demokratisch beschlossen?", "Eingriff in Grundrechte (allgemeine Handlungsfreiheit, Eigentum) verhältnismäßig? Gesetzgebungskompetenz des Landes (Schule = Ländersache)?"],
             ["Akzeptanz", "Tragen Betroffene die Maßnahme mit?", "Wie reagieren Schüler/innen, Eltern, Lehrkräfte?"],
             ["Durchsetzbarkeit", "Kann sie umgesetzt und kontrolliert werden?", "Wie wird kontrolliert? Was gilt in Pausen?"],
             ["Folgen / Nebenfolgen", "Welche erwünschten und unerwünschten Folgen hat sie?", "Weniger Medienkompetenz-Training? Probleme in Notfällen?"],
         ],
         "html": "<p>Wähle für jede Aufgabe <b>zwei bis vier passende Kriterien</b> – nicht alle passen immer.</p>"},
        {"t": "text", "art": "Fachtext", "titel": "Vom Meinen zum Urteilen",
         "html": "<p>Politische Urteilsfähigkeit gilt als zentrales Ziel des Politikunterrichts. Ein politisches Urteil unterscheidet sich von einer bloßen Meinung dadurch, dass es <b>begründet</b>, <b>überprüfbar</b> und <b>reflektiert</b> ist. Wer meint, sagt, was er denkt. Wer urteilt, zeigt, warum er so denkt, auf welche Fakten er sich stützt und welche Gegenargumente er bedacht hat.</p><p>Für das Sachurteil heißt das zunächst, die <b>Urteilsfrage</b> genau zu klären. „Ist das Handyverbot gut?“ ist zu ungenau. Präziser wäre: „Ist ein grundsätzliches Verbot der privaten Smartphone-Nutzung an Schulen ein geeignetes Mittel, um Lernbedingungen und soziales Miteinander zu verbessern?“ Daraus ergeben sich die Kriterien fast von selbst: Wirksamkeit für das Lernen, Folgen für das soziale Miteinander, Rechtmäßigkeit und Umsetzbarkeit.</p><p>Im zweiten Schritt wird jedes Kriterium mit <b>Fachwissen und Belegen</b> geprüft, und zwar in beide Richtungen. Entscheidend ist dann die <b>Abwägung</b>. Argumente werden nicht gezählt, sondern gewichtet. Ein gut belegtes Argument, das viele Menschen langfristig betrifft, wiegt schwerer als eine Vermutung über einen Einzelfall. Am Ende steht ein <b>klares Fazit</b>, das sich ausdrücklich auf die Urteilsfrage bezieht. Es darf differenziert sein („grundsätzlich ja, aber …“), muss aber eine erkennbare Position enthalten.</p><p>Typische Schwächen in Abiturklausuren sind Urteile ohne erkennbare Kriterien, die bloße Aneinanderreihung von Pro- und Contra-Argumenten ohne Abwägung sowie ein Fazit, das plötzlich ein neues Argument einführt oder der vorherigen Argumentation widerspricht.</p>",
         "quelle": "Selbst verfasster Fachtext (Feibitur)."},
        {"t": "text", "art": "Beispiel", "titel": "Formulierungshilfen für das Sachurteil",
         "html": "<ul><li><b>Einleitung:</b> „Im Folgenden wird beurteilt, ob … Als Kriterien dienen dabei die Effektivität, die Legitimität und die Durchsetzbarkeit.“</li><li><b>Pro:</b> „Hinsichtlich der Effektivität spricht für …, dass … Dies belegen …“</li><li><b>Contra:</b> „Dagegen lässt sich einwenden, dass … / Problematisch erscheint jedoch …“</li><li><b>Abwägung:</b> „Zwar …, jedoch wiegt … schwerer, da …“ / „Entscheidend ist …“</li><li><b>Fazit:</b> „Insgesamt ist … deshalb als (eingeschränkt) geeignet zu beurteilen, sofern …“</li></ul>"},
        {"t": "text", "art": "Merke", "titel": "Checkliste vor der Abgabe",
         "html": "<ul><li>Habe ich die Urteilsfrage aus der Aufgabe aufgegriffen?</li><li>Habe ich meine Kriterien ausdrücklich genannt?</li><li>Habe ich Fachwissen (Begriffe, Theorien, GG-Artikel) eingebracht?</li><li>Habe ich Pro <i>und</i> Contra berücksichtigt und mit Belegen gestützt?</li><li>Habe ich gewichtet statt nur aufgezählt?</li><li>Ist mein Fazit klar und passt es zur Argumentation?</li></ul>"},
    ],
    "aufgaben": [
        {
            "id": "g2-a1",
            "titel": "Methodentraining Sachurteil: Smartphone-Verbot an Schulen",
            "kurs": "Grundkurs und Leistungskurs (Methodentraining)",
            "bezug": "Urteilskompetenz (Sachurteil nach Kriterien); inhaltlicher Bezug zu Bildungspolitik als Landeskompetenz (Q1.1 Bundesstaatsprinzip) und Grundrechten.",
            "standards": "Urteilskompetenz: mögliche Folgen unterschiedlicher Lösungsansätze abschätzen; eigene Entscheidungen argumentativ begründen. Analysekompetenz: Interessen relevanter Akteure einschätzen.",
            "aufgaben": [
                {"nr": 1, "operator": "wiedergeben", "afb": "I", "be": 20, "text": "Geben Sie die im Material dargestellten Positionen wieder."},
                {"nr": 2, "operator": "herausarbeiten", "afb": "II", "be": 25, "text": "Arbeiten Sie heraus, welche Urteilskriterien den Positionen der Beteiligten zugrunde liegen."},
                {"nr": 3, "operator": "erläutern", "afb": "II", "be": 20, "text": "Erläutern Sie am Beispiel des Materials den Unterschied zwischen einem Sachurteil und einem Werturteil."},
                {"nr": 4, "operator": "beurteilen", "afb": "III", "be": 35, "text": "Beurteilen Sie, ob ein grundsätzliches Verbot der privaten Smartphone-Nutzung an Schulen ein geeignetes Mittel ist, um die Lernbedingungen zu verbessern."},
            ],
            "material": [
                {"titel": "Material: Bericht „Handy weg – Problem gelöst?“ (2025)",
                 "absaetze": [
                     "Seit Beginn des Schuljahres gilt an den Schulen in Hessen eine neue Regel: Die private Nutzung von Smartphones ist grundsätzlich untersagt. Ausnahmen sind möglich, etwa wenn Lehrkräfte die Geräte für den Unterricht einsetzen oder Schulen eigene Regeln für ältere Jahrgänge beschließen. Andere Bundesländer haben ähnliche Regeln eingeführt oder planen sie.",
                     "Die Landesregierung verweist auf mehr Konzentration und weniger Ablenkung. Schon nach wenigen Wochen hätten viele Schulen berichtet, dass in den Pausen wieder mehr miteinander gesprochen und gespielt werde. Zudem lasse sich Cybermobbing, das häufig während der Schulzeit beginne, besser eindämmen. Ein Sprecher erklärte: „Das Gesetz schafft Klarheit für alle. Lehrkräfte müssen nicht mehr jeden Tag neu verhandeln.“",
                     "Die Schülervertretung sieht das kritisch. „Wir lernen, mit Social Media umzugehen, nicht indem man es uns verbietet, sondern indem wir es üben“, sagt ein Landesschulsprecher. Gerade in der Oberstufe seien Smartphones ein Arbeitsmittel. Außerdem werde über die Köpfe der Schülerinnen und Schüler hinweg entschieden.",
                     "Ein Elternvertreter begrüßt die Regel grundsätzlich, fragt aber nach der Umsetzung: Wer kontrolliert? Was passiert mit eingesammelten Geräten? Und wie erreichen Eltern ihre Kinder im Notfall? Eine Lehrerin aus Kassel berichtet, die Kontrolle koste Zeit, insgesamt sei die Stimmung aber ruhiger geworden.",
                     "Wissenschaftlich ist die Lage weniger eindeutig, als es die Debatte vermuten lässt. Studien deuten darauf hin, dass ablenkende Geräte das Lernen beeinträchtigen können. Ob ein Verbot die Leistungen messbar verbessert, ist jedoch umstritten. Forschende empfehlen, Verbote mit Medienbildung zu verbinden.",
                 ],
                 "quelle": "Übungsmaterial: eigens für Feibitur verfasster Bericht (2025). Hintergrund: Hessen hat die private Smartphone-Nutzung an Schulen zum Schuljahr 2025/26 grundsätzlich untersagt; Aussagen der zitierten Personen sind fiktiv."},
            ],
            "loesung": [
                {"vorbemerkung": "Einleitungssatz: Bericht „Handy weg – Problem gelöst?“ (2025) über das Verbot privater Smartphone-Nutzung an hessischen Schulen.",
                 "punkte": [
                     "Regel: grundsätzliches Verbot privater Nutzung, Ausnahmen für Unterricht/ältere Jahrgänge; andere Länder ähnlich [1].",
                     "Landesregierung: mehr Konzentration, weniger Ablenkung, mehr soziales Miteinander, weniger Cybermobbing, Klarheit für Lehrkräfte [2].",
                     "Schülervertretung: Medienkompetenz durch Üben statt Verbieten; Smartphone als Arbeitsmittel in der Oberstufe; mangelnde Beteiligung [3].",
                     "Eltern: grundsätzliche Zustimmung, Fragen zu Kontrolle, Aufbewahrung, Erreichbarkeit im Notfall [4].",
                     "Lehrerin: Kontrollaufwand, aber ruhigere Stimmung [4].",
                     "Wissenschaft: Ablenkung belegt, Leistungseffekt eines Verbots umstritten; Empfehlung, Verbot mit Medienbildung zu verbinden [5].",
                 ],
                 "hinweis": "Wiedergeben: eigene Worte, indirekte Rede, keine Wertung."},
                {"punkte": [
                    "Landesregierung: Effektivität (Konzentration, weniger Mobbing), Akzeptanz/Praktikabilität (Klarheit, Entlastung der Lehrkräfte).",
                    "Schülervertretung: Effektivität bzgl. des Ziels Medienkompetenz (Verbot ungeeignet), Zweckmäßigkeit (Arbeitsmittel), Legitimität des Verfahrens (Beteiligung).",
                    "Eltern: Durchsetzbarkeit, Rechtssicherheit (Umgang mit Geräten), Sicherheit/Nebenfolgen (Notfall).",
                    "Lehrerin: Effizienz (Aufwand vs. Nutzen), Effektivität (Klima).",
                    "Wissenschaft: empirische Belegbarkeit/Effektivität; Hinweis auf alternative bzw. ergänzende Maßnahmen.",
                    "Die Kriterien werden im Material meist nicht ausdrücklich genannt und müssen erschlossen werden.",
                ],
                 "hinweis": "Herausarbeiten: nicht explizit genannte Sachverhalte erschließen – die Kriterien sind fachsprachlich zu benennen und mit Belegen aus dem Material zu verknüpfen."},
                {"punkte": [
                    "Sachurteil (beurteilen): begründete Einschätzung auf Basis von Kriterien, Fachwissen und Belegen, z. B. „Studien zeigen Ablenkung; ob Leistungen steigen, ist unklar – daher ist die Wirksamkeit begrenzt belegt.“",
                    "Werturteil (bewerten/Stellung nehmen): zusätzlich Offenlegung eigener Wertmaßstäbe, z. B. Vorrang von Selbstbestimmung/Freiheit der Schüler (Schülervertretung) vs. Schutz und Gemeinschaft (Landesregierung).",
                    "Beispiele aus dem Material zuordnen: Aussagen der Wissenschaft eher sachbezogen [5], Kritik an fehlender Beteiligung berührt Werte wie Mitbestimmung [3].",
                    "Zusammenhang: Werturteil baut auf Sachurteil auf; beide gehören zur politischen Urteilskompetenz; Bezug zur hessischen Operatorenliste.",
                ],
                 "hinweis": "Erläutern: Unterschied muss mit Beispielen aus dem Material veranschaulicht werden."},
                {"punkte": [
                    "Präzisierung der Urteilsfrage und Benennung von Kriterien (z. B. Effektivität für Lernbedingungen, Legitimität/Rechtmäßigkeit, Durchsetzbarkeit/Effizienz, Nebenfolgen).",
                    "Effektivität: weniger Ablenkung, ruhigeres Klima, mehr soziale Interaktion vs. unklarer Leistungseffekt, Ausweichverhalten, fehlende Übung von Selbstregulation.",
                    "Legitimität: Schule ist Ländersache (Bundesstaatsprinzip); Landesgesetz demokratisch beschlossen; Eingriff in Grundrechte (allgemeine Handlungsfreiheit Art. 2 Abs. 1 GG, ggf. Eigentum) muss verhältnismäßig sein – Ausnahmen sprechen für Verhältnismäßigkeit; Kritik an mangelnder Beteiligung.",
                    "Durchsetzbarkeit/Effizienz: Kontrollaufwand vs. Entlastung durch klare Regeln; Notfallerreichbarkeit lösbar.",
                    "Nebenfolgen und Alternativen: Medienbildung, schulinterne Regeln, altersdifferenzierte Lösungen.",
                    "Abwägung und klares, ggf. differenziertes Fazit (z. B. für Unter- und Mittelstufe geeignet, für Oberstufe nur mit Ausnahmen und in Verbindung mit Medienbildung).",
                ],
                 "hinweis": "Beurteilen: Kriterien müssen ausdrücklich erkennbar sein; Abwägung statt bloßer Aufzählung; die Offenlegung eigener Wertmaßstäbe ist nicht erforderlich."},
            ],
            "bewertung": {
                "ausreichend": ["die Positionen im Ansatz korrekt wiedergegeben werden,",
                                "einige Urteilskriterien ansatzweise zutreffend herausgearbeitet werden,",
                                "der Unterschied von Sach- und Werturteil ansatzweise erläutert wird,",
                                "ein ansatzweise kriteriengeleitetes und nachvollziehbar begründetes Urteil formuliert wird."],
                "gut": ["die Positionen weitgehend vollständig, strukturiert und in eigenen Worten wiedergegeben werden,",
                        "die Urteilskriterien differenziert, fachsprachlich präzise und mit Belegen herausgearbeitet werden,",
                        "der Unterschied von Sach- und Werturteil differenziert und mit Beispielen aus dem Material erläutert wird,",
                        "das Urteil ausdrücklich kriteriengeleitet, abwägend und schlüssig begründet ist und ein klares Fazit enthält."],
            },
        },
    ],
}
