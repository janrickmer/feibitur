# -*- coding: utf-8 -*-
"""Q1.5 Gemeinwohl und organisierte Interessen"""

SVG_LOBBY = """<svg viewBox='0 0 760 340' xmlns='http://www.w3.org/2000/svg' font-family='system-ui, Arial, sans-serif' font-size='13' role='img' aria-labelledby='lbt'>
<title id='lbt'>Wege der Einflussnahme von Interessengruppen</title>
<rect width='760' height='340' fill='#fff'/>
<text x='380' y='24' text-anchor='middle' font-weight='700' font-size='15' fill='#14213d'>Wie Interessengruppen Einfluss nehmen</text>
<circle cx='380' cy='180' r='74' fill='#14213d'/>
<text x='380' y='172' text-anchor='middle' fill='#fff' font-weight='700'>Interessen-</text>
<text x='380' y='190' text-anchor='middle' fill='#fff' font-weight='700'>gruppen</text>
<text x='380' y='210' text-anchor='middle' fill='#dfe6f7' font-size='11'>Verbände, Unternehmen, NGOs</text>
<g text-anchor='middle'>
<rect x='30' y='50' width='220' height='70' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='140' y='75' font-weight='700' fill='#14213d'>Ministerien</text><text x='140' y='95' fill='#333'>Stellungnahmen zu</text><text x='140' y='111' fill='#333'>Referentenentwürfen</text>
<rect x='510' y='50' width='220' height='70' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='620' y='75' font-weight='700' fill='#14213d'>Parlament</text><text x='620' y='95' fill='#333'>Gespräche mit Abgeordneten,</text><text x='620' y='111' fill='#333'>Anhörungen in Ausschüssen</text>
<rect x='30' y='240' width='220' height='70' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='140' y='265' font-weight='700' fill='#14213d'>Parteien</text><text x='140' y='285' fill='#333'>Spenden, Mitgliedschaften,</text><text x='140' y='301' fill='#333'>Personalverflechtung</text>
<rect x='510' y='240' width='220' height='70' rx='12' fill='#eef2fb' stroke='#14213d'/><text x='620' y='265' font-weight='700' fill='#14213d'>Öffentlichkeit</text><text x='620' y='285' fill='#333'>Kampagnen, Studien,</text><text x='620' y='301' fill='#333'>Demonstrationen, Streiks</text>
</g>
<g stroke='#b5302a' stroke-width='2'><path d='M318 140 L250 100'/><path d='M442 140 L510 100'/><path d='M318 220 L250 265'/><path d='M442 220 L510 265'/></g>
<text x='380' y='330' text-anchor='middle' fill='#555' font-size='11'>Daneben: Klagen vor Gerichten, EU-Ebene (Brüssel gilt als zweitgrößter Lobbystandort der Welt nach Washington).</text>
</svg>"""

TOPIC = {
    "id": "q1-5",
    "begriffe": [
        {"b": "Gemeinwohl", "kurz": "das Wohl der gesamten Gesellschaft im Unterschied zu Einzel- oder Gruppeninteressen.",
         "lang": "Das <b>Gemeinwohl</b> ist das, was dem Wohl aller dient – nicht nur einer Gruppe. Strittig ist, <b>wer</b> es bestimmt: Ist es vorab erkennbar (a priori) oder entsteht es erst im Wettbewerb der Interessen (a posteriori)? Politikerinnen und Politiker berufen sich gern auf das Gemeinwohl, um ihre Position zu rechtfertigen."},
        {"b": "Gemeinwohl a priori", "kurz": "Vorstellung, dass das Gemeinwohl objektiv vorgegeben ist und erkannt werden kann (z. B. Rousseau).",
         "lang": "Nach der Vorstellung eines <b>Gemeinwohls a priori</b> gibt es ein „richtiges“ Gemeinwohl, das unabhängig von den Interessen der Einzelnen feststeht (vgl. Rousseaus volonté générale). Gefahr: Wer behauptet, es zu kennen, kann andere Meinungen als illegitim abwerten – typisch für autoritäre und populistische Positionen."},
        {"b": "Gemeinwohl a posteriori", "kurz": "Vorstellung, dass das Gemeinwohl erst nachträglich als Ergebnis eines fairen Interessenausgleichs entsteht (Fraenkel).",
         "lang": "In der Pluralismustheorie (Ernst Fraenkel) ist das <b>Gemeinwohl a posteriori</b> das Ergebnis eines fairen Wettbewerbs und Kompromisses zwischen vielen Interessen – auf Grundlage gemeinsamer Grundwerte und Spielregeln. Das passt zur repräsentativen Demokratie."},
        {"b": "Interessengruppe", "kurz": "organisierter Zusammenschluss, der gemeinsame Interessen gegenüber Politik und Öffentlichkeit vertritt (Verband).",
         "lang": "<b>Interessengruppen</b> (Verbände) bündeln die Interessen ihrer Mitglieder, z. B. Arbeitgeberverbände, Gewerkschaften, Sozialverbände, Umweltverbände, Berufsverbände (Ärzte, Bauern). Anders als Parteien wollen sie <b>nicht selbst regieren</b>, sondern Einfluss auf Entscheidungen nehmen."},
        {"b": "Lobbyismus", "kurz": "gezielte Einflussnahme von Interessenvertretern auf Politik und Gesetzgebung.",
         "lang": "<b>Lobbyismus</b> bezeichnet die direkte Einflussnahme auf Abgeordnete, Ministerien und Behörden – durch Gespräche, Stellungnahmen, Studien oder Veranstaltungen. Er liefert Politik Fachwissen und Informationen über Betroffene. Problematisch wird er bei <b>Intransparenz</b> und ungleichen Ressourcen (finanzstarke Gruppen dominieren)."},
        {"b": "Lobbyregister", "kurz": "öffentliches Register beim Bundestag, in das sich Interessenvertreter seit 2022 eintragen müssen.",
         "lang": "Seit dem 1. Januar 2022 müssen sich Interessenvertreterinnen und -vertreter, die Kontakt zu Bundestag oder Bundesregierung aufnehmen, im <b>Lobbyregister</b> eintragen und z. B. Auftraggeber und finanzielle Aufwendungen angeben. 2024 wurden die Regeln verschärft. Kritik: Es gibt weiterhin Lücken, etwa beim „exekutiven Fußabdruck“ (welche Lobbyisten an welchem Gesetz mitgewirkt haben)."},
        {"b": "Drehtüreffekt", "kurz": "Wechsel von Politikern in Lobbyjobs der Wirtschaft (oder umgekehrt), bei dem Insiderwissen und Kontakte mitgenommen werden.",
         "lang": "Beim <b>Drehtüreffekt</b> wechseln Ministerinnen oder Spitzenbeamte nach ihrer Amtszeit in Unternehmen oder Verbände, deren Interessen sie vorher mitregelt haben. Für Mitglieder der Bundesregierung gibt es deshalb eine <b>Karenzzeit</b>: Die Regierung kann einen Wechsel für bis zu 18 Monate untersagen."},
        {"b": "Pluralismus", "kurz": "Vielfalt gleichberechtigter Interessen, Meinungen und Gruppen in einer Gesellschaft.",
         "lang": "<b>Pluralismus</b> bedeutet, dass in einer freien Gesellschaft viele unterschiedliche Interessen legitim nebeneinander bestehen und um Einfluss konkurrieren dürfen. Grundlage sind Meinungs-, Versammlungs- und Vereinigungsfreiheit (Art. 5, 8, 9 GG)."},
        {"b": "Organisationsfähigkeit", "kurz": "Fähigkeit eines Interesses, Mitglieder und Ressourcen zu gewinnen und sich wirksam zu organisieren.",
         "lang": "Nicht alle Interessen lassen sich gleich gut organisieren. Kleine Gruppen mit konzentrierten Interessen (z. B. eine Branche) organisieren sich leichter als große, diffuse Gruppen (z. B. Verbraucher, Steuerzahler, künftige Generationen). Das beschreibt <b>Mancur Olson</b> in der „Logik des kollektiven Handelns“."},
        {"b": "Konfliktfähigkeit", "kurz": "Fähigkeit einer Gruppe, durch Leistungsverweigerung Druck auszuüben (z. B. Streik).",
         "lang": "Nach <b>Claus Offe</b> setzen sich Interessen besonders gut durch, wenn sie <b>konfliktfähig</b> sind – also glaubhaft mit einer Leistungsverweigerung drohen können (z. B. Lokführer, Ärzte, Landwirte). Arbeitslose, Kinder oder Pflegebedürftige können das kaum. Folge: <b>Asymmetrie</b> im Pluralismus."},
        {"b": "Trittbrettfahrerproblem", "kurz": "Menschen profitieren von den Erfolgen einer Gruppe, ohne selbst Mitglied zu sein oder beizutragen.",
         "lang": "Wenn eine Gewerkschaft einen höheren Lohn durchsetzt, profitieren oft auch Nichtmitglieder. Warum also Beitrag zahlen? Dieses <b>Trittbrettfahrerproblem</b> (free rider) erklärt, warum große Gruppen schwer zu organisieren sind. Gegenmittel sind <b>selektive Anreize</b> (z. B. Rechtsberatung nur für Mitglieder)."},
        {"b": "Neokorporatismus", "kurz": "enge, institutionalisierte Zusammenarbeit von Staat und großen Verbänden (z. B. Arbeitgeber und Gewerkschaften).",
         "lang": "Im <b>Neokorporatismus</b> verhandelt der Staat Politik direkt mit wenigen großen Dachverbänden, die dafür Verantwortung übernehmen (z. B. Tarifautonomie, Selbstverwaltung in der Sozialversicherung, frühere „Bündnisse für Arbeit“). Vorteil: Konsens und Umsetzung. Kritik: Nicht beteiligte Interessen bleiben außen vor."},
        {"b": "NGO", "kurz": "Nichtregierungsorganisation: zivilgesellschaftliche, nicht gewinnorientierte Organisation (z. B. Greenpeace, Amnesty International).",
         "lang": "<b>NGOs</b> (Non-Governmental Organisations) sind unabhängig vom Staat und nicht gewinnorientiert. Sie vertreten oft <b>allgemeine Interessen</b> (Umwelt, Menschenrechte, Verbraucher) und nutzen Kampagnen, Studien, Klagen und Lobbyarbeit. Auch sie sind Interessenvertreter und müssen sich ggf. im Lobbyregister eintragen."},
        {"b": "Klientelismus", "kurz": "Politik, die gezielt die Interessen der eigenen Unterstützergruppen bedient statt das Gemeinwohl.",
         "lang": "Von <b>Klientelismus</b> spricht man, wenn Parteien vor allem ihre Stammwählerschaft oder Spender begünstigen (z. B. Steuererleichterungen für bestimmte Branchen). Parteien stehen immer im Spannungsfeld zwischen <b>Gemeinwohlorientierung</b> und der Vertretung ihrer Wählergruppen. Im Erlass ist das Thema LK-Stoff (Q1.5, kein Schwerpunkt 2027)."},
        {"b": "Leistungsgerechtigkeit", "kurz": "Gerechtigkeitsprinzip: Wer mehr leistet, soll mehr bekommen.",
         "lang": "<b>Leistungsgerechtigkeit</b> heißt: Einkommen und Güter sollen nach Leistung verteilt werden (z. B. höherer Lohn für mehr Arbeit oder Verantwortung). Problem: Was ist „Leistung“? Pflegearbeit oder Kindererziehung werden oft gering bezahlt, obwohl sie gesellschaftlich wichtig sind. Wichtig auch für Q2.4!"},
        {"b": "Bedarfsgerechtigkeit", "kurz": "Gerechtigkeitsprinzip: Jeder soll bekommen, was er zum Leben braucht.",
         "lang": "<b>Bedarfsgerechtigkeit</b> orientiert sich an den Bedürfnissen der Menschen: Wer in Not ist, soll unterstützt werden – unabhängig von seiner Leistung (z. B. Grundsicherung, Wohngeld). Sie ist Grundlage des <b>Sozialstaats</b> (Art. 20 GG). Kritik: Leistungsanreize können sinken."},
        {"b": "Chancengerechtigkeit", "kurz": "Gerechtigkeitsprinzip: Alle sollen die gleichen Startchancen haben, unabhängig von Herkunft.",
         "lang": "<b>Chancengerechtigkeit</b> (Chancengleichheit) zielt darauf, dass Erfolg nicht von Herkunft, Geschlecht oder Einkommen der Eltern abhängt – z. B. durch kostenlose Bildung, BAföG, Kitas. In Deutschland hängt der Bildungserfolg im internationalen Vergleich stark von der sozialen Herkunft ab."},
        {"b": "Verteilungsgerechtigkeit", "kurz": "Frage, wie Einkommen, Vermögen und Lasten in einer Gesellschaft gerecht verteilt werden.",
         "lang": "<b>Verteilungsgerechtigkeit</b> fragt, wie Güter und Lasten verteilt sein sollen. Instrumente sind z. B. progressive Einkommensteuer, Sozialtransfers, Erbschaftsteuer. Je nachdem, ob man Leistung, Bedarf oder Gleichheit betont, kommt man zu unterschiedlichen Antworten."},
        {"b": "Generationengerechtigkeit", "kurz": "Gerechtigkeit zwischen heutigen und künftigen Generationen (z. B. bei Schulden, Rente, Klima).",
         "lang": "<b>Generationengerechtigkeit</b> verlangt, dass heutige Generationen künftigen nicht unzumutbare Lasten hinterlassen – etwa hohe Staatsschulden, ein nicht finanzierbares Rentensystem oder Klimaschäden. Das BVerfG hat im Klimabeschluss 2021 eine „intertemporale Freiheitssicherung“ gefordert."},
        {"b": "Schleier des Nichtwissens", "kurz": "Gedankenexperiment von John Rawls: Gerechte Regeln wählt, wer nicht weiß, welche Position er in der Gesellschaft haben wird.",
         "lang": "John Rawls (1971) schlägt vor: Stell dir vor, du müsstest die Regeln einer Gesellschaft festlegen, ohne zu wissen, ob du reich oder arm, gesund oder krank sein wirst (<b>Schleier des Nichtwissens</b>). Dann würdest du gleiche Grundfreiheiten wählen und Ungleichheiten nur zulassen, wenn sie auch den <b>am schlechtesten Gestellten</b> nützen (Differenzprinzip)."},
        {"b": "Sozialstaatsprinzip", "kurz": "Verfassungsauftrag (Art. 20 Abs. 1 GG), für soziale Sicherheit und soziale Gerechtigkeit zu sorgen.",
         "lang": "Das <b>Sozialstaatsprinzip</b> verpflichtet den Staat, ein menschenwürdiges Existenzminimum zu sichern und für sozialen Ausgleich zu sorgen. Wie das genau geschieht (Höhe von Leistungen, Rente, Gesundheit), entscheidet der Gesetzgeber – und darüber streiten Parteien und Interessengruppen."},
    ],
    "inhalte": [
        {"t": "text", "art": "Merke", "titel": "Hinweis zum Abitur 2027",
         "html": "<p>Q1.5 ist laut Abiturerlass <b>kein Schwerpunkt</b> im Landesabitur 2027. Aber: Die <b>konkurrierenden Gerechtigkeitsbegriffe</b> (Leistungs-, Bedarfs- und Chancengerechtigkeit, Diskriminierung) sind über <b>Q2.4 im Grund- und Leistungskurs prüfungsrelevant</b>. Außerdem helfen dir Pluralismus und Gemeinwohl bei Urteilsaufgaben in Q1.2 und Q1.4.</p>"},
        {"t": "text", "art": "Erklärung", "titel": "Worum geht es in Q1.5?",
         "html": "<p>In einer Demokratie gibt es viele Interessen: Autofahrer wollen niedrige Spritpreise, Umweltverbände mehr Klimaschutz, Ärztinnen bessere Bezahlung, Krankenkassen niedrigere Kosten. Wie entsteht daraus eine Politik, die dem <b>Gemeinwohl</b> dient? Und wer setzt sich durch? In Q1.5 untersuchst du</p><ul><li>einen <b>Fall aus der Sozialpolitik</b> (z. B. Gesundheits-, Familien- oder Migrationspolitik),</li><li>Interessengruppen zwischen legitimer <b>Interessenartikulation</b> und problematischem <b>Lobbyismus</b>,</li><li>(LK) Parteien zwischen Gemeinwohl und Klientelismus sowie konkurrierende Gerechtigkeitsbegriffe.</li></ul>"},
        {"t": "table", "art": "Merke", "titel": "Zwei Vorstellungen vom Gemeinwohl",
         "kopf": ["", "Gemeinwohl a priori", "Gemeinwohl a posteriori"],
         "zeilen": [
             ["Vertreter", "Jean-Jacques Rousseau (volonté générale)", "Ernst Fraenkel (Pluralismustheorie)"],
             ["Grundidee", "Das Gemeinwohl steht vorher fest und kann erkannt werden.", "Das Gemeinwohl entsteht erst als Ergebnis eines fairen Interessenausgleichs."],
             ["Rolle von Interessengruppen", "stören, weil sie Sonderinteressen vertreten", "legitim und notwendig"],
             ["Demokratiemodell", "identitäre Demokratie", "repräsentative, pluralistische Demokratie"],
             ["Gefahr", "Ausgrenzung Andersdenkender, Totalitarismus", "Übermacht gut organisierter Interessen"],
         ]},
        {"t": "svg", "art": "Schaubild", "titel": "Wege der Einflussnahme", "svg": SVG_LOBBY,
         "caption": "Interessengruppen setzen an allen Stellen des politischen Prozesses an – besonders früh, wenn Gesetzentwürfe in den Ministerien entstehen."},
        {"t": "text", "art": "Fachtext", "titel": "Fallbeispiel Gesundheitspolitik: Die Krankenhausreform",
         "html": "<p>Kaum ein Politikfeld ist so stark von organisierten Interessen geprägt wie die Gesundheitspolitik. Krankenhausträger, Ärzteverbände, Pflegeverbände, Krankenkassen, Pharmaunternehmen, Patientenorganisationen, Bund, Länder und Kommunen verfolgen jeweils eigene, oft gegensätzliche Ziele. Am Beispiel der <b>Krankenhausreform</b> lässt sich das gut nachvollziehen.</p><p>Ausgangspunkt war eine breit geteilte Problemdiagnose: Deutschland hat im europäischen Vergleich sehr viele Krankenhausbetten, viele Kliniken schreiben rote Zahlen, Fachkräfte fehlen, und die Vergütung über Fallpauschalen schafft Anreize, möglichst viele Behandlungen durchzuführen. Die damalige Bundesregierung wollte deshalb mit dem Krankenhausversorgungsverbesserungsgesetz die Finanzierung teilweise auf Vorhaltepauschalen umstellen und Leistungen stärker an Qualitätsvorgaben knüpfen. Komplizierte Eingriffe sollten auf spezialisierte Zentren konzentriert werden. Das Gesetz wurde Ende 2024 beschlossen; seine Umsetzung und Nachbesserungen beschäftigen die Politik seitdem weiter.</p><p>Die Interessenlage war vielschichtig. Die <b>Deutsche Krankenhausgesellschaft</b> warnte vor einem „kalten Strukturwandel“ und forderte mehr Geld für die Kliniken. Die <b>Länder</b>, die für die Krankenhausplanung zuständig sind, pochten auf ihre Kompetenzen und verlangten Ausnahmen für ländliche Regionen. Die <b>Krankenkassen</b> begrüßten mehr Qualität, wehrten sich aber gegen höhere Kosten für die Beitragszahler. Kommunalpolitikerinnen und Bürgerinitiativen kämpften gegen die Schließung „ihres“ Krankenhauses. Patientenvertreter betonten die Qualität der Behandlung, die bei Spezialisierung steigen könne.</p><p>Der Fall zeigt: Jede Gruppe beruft sich auf das Gemeinwohl, versteht darunter aber etwas anderes, etwa wohnortnahe Versorgung, Qualität, Bezahlbarkeit oder Arbeitsplätze. Politik muss zwischen diesen Interessen abwägen. Dabei setzen sich gut organisierte, konfliktfähige Akteure leichter durch als diffuse Interessen wie die der Beitragszahlenden oder künftiger Patientinnen und Patienten.</p>",
         "quelle": "Selbst verfasster Fachtext (Feibitur). Zur Vertiefung eignen sich die Stellungnahmen der beteiligten Verbände auf deren Webseiten und die Bundestagsdrucksachen."},
        {"t": "text", "art": "Erklärung", "titel": "Lobbyismus: notwendig oder gefährlich?",
         "html": "<table><thead><tr><th>Lobbyismus ist notwendig, weil …</th><th>Lobbyismus ist gefährlich, wenn …</th></tr></thead><tbody><tr><td>Politik auf Fachwissen der Betroffenen angewiesen ist</td><td>er intransparent ist („Hinterzimmer“)</td></tr><tr><td>Interessenartikulation in der Demokratie legitim ist (Art. 9 GG)</td><td>finanzstarke Gruppen viel mehr Zugang haben als schwache</td></tr><tr><td>Folgen von Gesetzen früh sichtbar werden</td><td>Gesetzestexte direkt von Lobbyisten formuliert werden</td></tr><tr><td>NGOs auch allgemeine Interessen einbringen</td><td>Drehtüreffekte und Spenden Abhängigkeiten schaffen</td></tr></tbody></table><p><b>Regulierung in Deutschland:</b> Lobbyregistergesetz (seit 2022, 2024 verschärft), Verhaltensregeln für Abgeordnete (nach der „Maskenaffäre“ 2021 verschärft), Karenzzeit für Regierungsmitglieder, Veröffentlichungspflicht für Parteispenden (ab 35.000 Euro sofort).</p>"},
        {"t": "table", "art": "Merke", "titel": "Konkurrierende Gerechtigkeitsbegriffe (auch für Q2.4!)",
         "kopf": ["Begriff", "Grundidee", "Beispiel", "Kritik"],
         "zeilen": [
             ["Leistungsgerechtigkeit", "Wer mehr leistet, soll mehr erhalten.", "Lohnunterschiede, Lohnabstandsgebot", "Leistung schwer messbar; ungleiche Startbedingungen"],
             ["Bedarfsgerechtigkeit", "Jeder erhält, was er zum Leben braucht.", "Grundsicherung, Wohngeld", "kann Leistungsanreize senken"],
             ["Chancengerechtigkeit", "gleiche Startchancen für alle", "BAföG, kostenfreie Kitas", "Ergebnisse bleiben ungleich"],
             ["Generationengerechtigkeit", "fairer Ausgleich zwischen Generationen", "Schuldenbremse, Rentenreform, Klimaschutz", "Abwägung mit heutigen Bedürfnissen"],
             ["Diskriminierungsfreiheit", "niemand darf wegen Merkmalen wie Geschlecht oder Herkunft benachteiligt werden", "Art. 3 GG, Allgemeines Gleichbehandlungsgesetz", "Durchsetzung schwierig (z. B. Gender Pay Gap)"],
         ]},
        {"t": "text", "art": "Erklärung", "titel": "Parteien zwischen Gemeinwohl und Klientelismus", "lk": True,
         "html": "<p>Parteien müssen Wahlen gewinnen und deshalb ihre Wählergruppen bedienen – sollen laut Verfassung aber am Willen des <i>ganzen</i> Volkes mitwirken. Beispiele für Klientelismus-Vorwürfe: Steuervergünstigungen für bestimmte Branchen, die Agrardiesel-Debatte 2024, Rentenpakete zugunsten älterer Wählergruppen. Gegenargument: In der Pluralismustheorie ist es legitim, dass Parteien unterschiedliche Interessen vertreten – das Gemeinwohl entsteht im Kompromiss. Problematisch wird es, wenn Spenden oder persönliche Vorteile Entscheidungen beeinflussen.</p>"},
    ],
    "aufgaben": [
        {
            "id": "q1-5-a1",
            "titel": "Lobbyismus – Gefahr für das Gemeinwohl?",
            "kurs": "Grundkurs (auch für LK geeignet)",
            "bezug": "Q1.5: Interessengruppen zwischen Interessenartikulation und Lobbyismus; Analyse eines exemplarischen Falles aus der Sozialpolitik (Gesundheitspolitik); (LK) konkurrierende Gerechtigkeitsbegriffe.",
            "standards": "Analysekompetenz: Interessen und Macht relevanter Akteure einschätzen. Urteilskompetenz: eigene Entscheidungen argumentativ begründen.",
            "aufgaben": [
                {"nr": 1, "operator": "zusammenfassen", "afb": "I", "be": 20, "text": "Fassen Sie die Aussagen des Kommentars zusammen. (Material)"},
                {"nr": 2, "operator": "erläutern", "afb": "II", "be": 25, "text": "Erläutern Sie Möglichkeiten, mit denen Interessengruppen Einfluss auf politische Entscheidungen nehmen."},
                {"nr": 3, "operator": "einordnen", "afb": "II", "be": 25, "text": "Ordnen Sie die Position des Autors in die Pluralismustheorie ein."},
                {"nr": 4, "operator": "beurteilen", "afb": "III", "be": 30, "text": "Beurteilen Sie, ob das deutsche Lobbyregister ausreicht, um das Gemeinwohl vor einseitiger Einflussnahme zu schützen."},
            ],
            "material": [
                {"titel": "Material: Kommentar „Wer laut ist, bekommt mehr“ (2025)",
                 "absaetze": [
                     "Lobbyismus hat in Deutschland einen schlechten Ruf. Man denkt an Hinterzimmer, Spendenkoffer und Gesetze, die von Konzernanwälten geschrieben werden. Dieses Bild ist zu einfach. Ohne den Austausch mit Verbänden, Unternehmen und Initiativen wüssten Ministerien oft gar nicht, welche Folgen ein Gesetz in der Praxis hat. Wer eine Krankenhausreform plant, muss mit Kliniken, Ärztinnen, Pflegekräften und Krankenkassen sprechen.",
                     "Das Problem liegt woanders: nicht darin, dass Interessen vertreten werden, sondern darin, wessen Interessen gehört werden. In der Gesundheitspolitik etwa sitzen mächtige Organisationen mit Hunderten Mitarbeitenden am Tisch. Sie können Studien in Auftrag geben, Kampagnen finanzieren und jeden Referentenentwurf binnen Tagen kommentieren. Wer vertritt dagegen die Beitragszahlerinnen und Beitragszahler, die am Ende die Rechnung bezahlen? Wer spricht für die Pflegebedürftige, die keine Zeit und Kraft für Demonstrationen hat?",
                     "Hinzu kommt die Macht des Streiks und der Drohung. Wenn Ärzte ihre Praxen schließen oder Landwirte Autobahnen blockieren, reagiert die Politik oft schnell. Die Interessen von Kindern, Arbeitslosen oder künftigen Generationen haben dagegen kein solches Druckmittel.",
                     "Mit dem Lobbyregister, das seit 2022 gilt, ist immerhin sichtbar geworden, wie viele Organisationen in Berlin Einfluss nehmen wollen und wie viel Geld sie dafür ausgeben. Das ist ein Fortschritt. Doch ein Register allein schafft noch keine Waffengleichheit. Es zeigt, wer an die Tür klopft, aber nicht, wer hereingelassen wird und was im Gespräch passiert.",
                     "Demokratie lebt vom Wettstreit der Interessen. Aber ein Wettstreit ist nur dann fair, wenn alle eine Chance haben, mitzuspielen. Der Staat sollte deshalb die Stimme der Schwachen gezielt stärken – etwa durch Förderung von Patienten- und Verbraucherorganisationen – und offenlegen, welche Stellungnahmen in welches Gesetz eingeflossen sind.",
                 ],
                 "quelle": "Übungsmaterial: eigens für Feibitur verfasster Kommentar eines fiktiven Autors (2025)."},
            ],
            "loesung": [
                {"vorbemerkung": "Einleitung: Kommentar „Wer laut ist, bekommt mehr“ (2025), fiktiver Autor; Thema: Lobbyismus, ungleiche Durchsetzungschancen, Lobbyregister.",
                 "punkte": [
                     "Der schlechte Ruf des Lobbyismus sei zu einfach; Austausch mit Verbänden liefere notwendiges Praxiswissen (Beispiel Krankenhausreform) [1].",
                     "Das eigentliche Problem sei die ungleiche Vertretung: ressourcenstarke Organisationen vs. Beitragszahlende und Pflegebedürftige [2].",
                     "Konfliktfähige Gruppen (Ärzte, Landwirte) könnten Druck ausüben, andere (Kinder, Arbeitslose, künftige Generationen) nicht [3].",
                     "Das Lobbyregister seit 2022 schaffe Transparenz über Akteure und Ausgaben, aber keine Waffengleichheit [4].",
                     "Forderung: fairer Wettstreit durch Stärkung schwacher Interessen (Förderung von Patienten-/Verbraucherorganisationen) und Offenlegung von Stellungnahmen (exekutiver Fußabdruck) [5].",
                 ],
                 "hinweis": "Indirekte Rede, eigene Worte, Struktur; keine Wertung."},
                {"punkte": [
                    "Ansatzpunkte: Ministerien (Stellungnahmen zu Referentenentwürfen, Fachgespräche, Expertenkommissionen), Parlament (Gespräche mit Abgeordneten, Anhörungen in Ausschüssen), Parteien (Spenden, Mitgliedschaften, Personalverflechtungen), Öffentlichkeit (Kampagnen, Studien, Pressearbeit, Demonstrationen, Streiks), Gerichte (Klagen), EU-Ebene.",
                    "Ressourcen: Fachwissen, Geld, Mitgliederzahl, Konfliktfähigkeit (Leistungsverweigerung), Zugang/Kontakte.",
                    "Formen: Lobbying (direkt), Public Affairs, Neokorporatismus (z. B. Tarifautonomie, Selbstverwaltung im Gesundheitswesen).",
                    "Beispiele: Krankenhausreform (DKG, Länder, Kassen), Bauernproteste 2023/24 (Agrardiesel), Tarifkonflikte, NGO-Kampagnen.",
                ],
                 "hinweis": "Erläutern: mit Beispielen veranschaulichen; Materialbezüge zu [2] und [3] möglich."},
                {"punkte": [
                    "Pluralismustheorie (Fraenkel): Vielfalt legitimer Interessen, Gemeinwohl a posteriori als Ergebnis fairen Wettbewerbs auf Basis eines Grundkonsenses (unstreitiger Sektor).",
                    "Übereinstimmung: Der Autor bejaht die Legitimität der Interessenvertretung [1] und den „Wettstreit der Interessen“ [5] – Grundgedanke des Pluralismus.",
                    "Pluralismuskritik: Der Autor greift die Kritik an ungleicher Organisations- und Konfliktfähigkeit auf (Olson: kleine Gruppen organisieren sich leichter; Offe: Konfliktfähigkeit) [2], [3]; Asymmetrie des Pluralismus („Der Chor des Pluralismus singt mit Oberschichtakzent“, Schattschneider – optional).",
                    "Lösungsansatz: Staat als Garant fairer Wettbewerbsbedingungen (Neopluralismus) [5].",
                    "Fazit: Autor als Vertreter eines (kritisch-reformerischen) Pluralismus, der nicht das System, sondern dessen Schieflagen kritisiert; Abgrenzung zur identitären Gemeinwohlvorstellung.",
                ],
                 "hinweis": "Einordnen: Position begründet in die Theorie stellen, Übereinstimmungen und Abweichungen belegen."},
                {"punkte": [
                    "Kriterien benennen (z. B. Transparenz, Chancengleichheit der Interessen, Wirksamkeit/Durchsetzbarkeit, Praktikabilität).",
                    "Leistungen des Registers: Registrierungspflicht seit 2022, Angaben zu Auftraggebern und Ausgaben, Verhaltenskodex, Verschärfung 2024; Transparenz über Akteure und Ressourcen; Sanktionen bei Verstößen.",
                    "Grenzen: keine Auskunft über Inhalte und Wirkung von Gesprächen; kein vollständiger exekutiver/legislativer Fußabdruck; Ausnahmen; ungleiche Ressourcen bleiben; Konfliktfähigkeit wird nicht berührt; Kontrolle und Sanktionen begrenzt.",
                    "Ergänzende Maßnahmen: Fußabdruck, Karenzzeiten, Spendenobergrenzen, Förderung schwacher Interessen, Bürgerräte.",
                    "Begründetes Urteil (z. B.: notwendiger, aber nicht hinreichender Schritt).",
                ],
                 "hinweis": "Beurteilen: kriteriengeleitete Einschätzung mit Fachwissen; Bezug auf Material [4], [5]."},
            ],
            "bewertung": {
                "ausreichend": ["die Aussagen des Kommentars im Ansatz korrekt zusammengefasst werden,",
                                "Möglichkeiten der Einflussnahme ansatzweise erläutert werden,",
                                "die Position des Autors ansatzweise in die Pluralismustheorie eingeordnet wird,",
                                "ein ansatzweise kriteriengeleitetes, nachvollziehbares Urteil formuliert wird."],
                "gut": ["die Aussagen des Kommentars weitgehend korrekt, strukturiert und in eigenen Worten zusammengefasst werden,",
                        "Möglichkeiten der Einflussnahme differenziert und mit Beispielen erläutert werden,",
                        "die Position des Autors differenziert und mit Belegen in die Pluralismustheorie und ihre Kritik eingeordnet wird,",
                        "das Urteil kriteriengeleitet, abwägend und schlüssig begründet ist."],
            },
        },
    ],
}
