# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Schülerinnen und Schüler der hessischen gymnasialen Oberstufe (Qualifikationsphase), die sich selbstständig auf das Landesabitur 2027 vorbereiten, im Grundkurs (GK) oder im Leistungskurs (LK). Sie lernen auf dem **Smartphone zu Hause** in kurzen Einheiten, am **Laptop/PC am Schreibtisch** in längeren Lernphasen (Aufgaben bearbeiten, Korrekturdateien mit einer KI nutzen) und auf dem **Tablet/iPad**. Herausgeber und Autor ist ihr Lehrer Jan-Rickmer Feindt (Politik und Wirtschaft, ev. Religion).

## Product Purpose

Feibitur („Feindt“ + „Abitur“) ist eine kostenlose, passwortgeschützte Lernseite fürs Abitur. Sie bündelt alle prüfungsrelevanten Inhalte eines Fachs entlang des hessischen Kerncurriculums (KCGO) und des Abiturerlasses 2027 und macht daraus selbstständiges Lernen: Fachbegriffe trainieren, Inhalte lesen, Abituraufgaben üben und korrigieren lassen.

Erfolg bedeutet:
- Schüler kommen **gern wieder**, weil sich das Lernen motivierend und nicht nach Schulbuch anfühlt,
- sie finden **sofort** Thema, Bereich und ihren Lernstand,
- lange Fachtexte, Tabellen und Materialien lesen sich **mühelos**,
- die Seite wirkt **hochwertig und seriös**, sodass man sie Kollegen, Schulleitung und Eltern zeigen kann.

## Positioning

Eine Lernseite von der eigenen Lehrkraft, genau zugeschnitten auf das hessische Landesabitur 2027: Abiturerlass-Schwerpunkte getrennt nach GK und LK, Operatoren nach der hessischen Liste, Aufgaben nach Anforderungsbereichen mit Korrekturdateien für die KI-Selbstkorrektur, aktuelle Fakten bis Herbst 2026 und eine Kurswahl, die irrelevante LK-Inhalte ausblendet.

## Operating Context

- Zugang über das Passwort „Feindt“ (Session Storage), dann Startseite mit der Wahl zwischen „Politik und Wirtschaft“, „ev. Religion“ (noch ohne Inhalte) und „Lerntools“.
- PoWi: Hinweis zum Abitur 2027 (getrennt nach Grundkurs und Leistungskurs), Reiter Grundlagen, Q1–Q4. Die Unterthemen stehen links in einer Liste und werden rechts auf- und zugeklappt. Jedes Unterthema hat die drei Bereiche Fachbegriffe (Lernkartei mit Leitner-System, Glossar, Fachbegriffe-Memory für zwei Personen), Inhalte (Text, Tabellen, Schaubilder, optionaler KI-Chatbot) und Übungsaufgaben (nach AFB gruppiert, Material, Operator-Definition, Korrekturdatei als PDF).
- 12 Lerntools: Lernplan, Fortschritt, Kann-Listen, Operatoren-Trainer, Schnelltest, Wiederholung, Abi-Simulation, Formulierungs-Baukasten, Beispiele, Begriffsnetz, Lernzettel, Vorlesen.
- Kurswahl GK/LK wird im Browser gespeichert und blendet LK-Inhalte im GK aus.

## Capabilities and Constraints

- Statische Seite auf GitHub Pages (feibitur.janrickmer.de), Vanilla-JS-SPA mit Hash-Router (`assets/js/app.js`, `assets/js/tools.js`, `assets/css/style.css`). Inhalte entstehen in Python (`tools/content/*.py`) und werden per `tools/build.py` zu JSON und PDFs gebaut.
- Kostenlos und DSGVO-freundlich: keine externen Ressourcen beim Laden (keine Webfonts von Fremdservern, kein Tracking, keine CDNs). Schriften und Bilder müssen selbst gehostet werden. Lernstand nur in `localStorage` (Präfix `feibitur.`).
- Der KI-Chatbot läuft nur nach ausdrücklicher Einwilligung über einen Cloudflare Worker.
- Das Memory hat keine Sounds (Entscheidung des Herausgebers).
- Fester Aufbau aus dem ursprünglichen Auftrag: Unterthemen-Liste links mit Aufklappen rechts, drei Bereiche je Unterthema, Inhalte etwa 2/3 mit Chatbot rechts, Anleitung in drei Schritten über den Übungsaufgaben, grüner Knopf „Korrekturdatei herunterladen“.
- Ev. Religion folgt später und bekommt eine **eigene visuelle Welt**. Jedes Fach hat seine eigene Gestaltung, die Startseite verbindet sie.

## Brand Commitments

- Name „Feibitur“, Domain feibitur.janrickmer.de.
- Jedes Fach bekommt eine eigene Welt (ausdrücklicher Wunsch); PoWi bekommt „ein PoWi-Design“.
- Impressum und Datenschutz mit den Angaben von Jan-Rickmer Feindt, die auch bei seinen Escape-Rooms verwendet werden.
- Ton: Du-Ansprache, sachlich-freundlich, fachlich präzise.

## Evidence on Hand

- Vollständige Inhalte für Grundlagen G1–G3 und Q1.1–Q4.3 (`tools/content/`), Operatoren und Abiturhinweise aus dem Abiturerlass 2027 (`tools/content/meta.py`), SVG-Schaubilder und Karikaturen als Materialien.
- Keine Fotos, kein Logo außer `assets/img/favicon.svg`, keine Testimonials oder Nutzerzahlen. Solche Angaben dürfen nicht erfunden werden.

## Product Principles

1. **Lernen vor Dekoration:** Jede Gestaltung muss Orientierung, Lesbarkeit oder Motivation dienen; konzentriertes Lesen darf nie gestört werden.
2. **Erwachsen, nicht kindlich:** Die Zielgruppe ist 17–19 Jahre alt. Nichts Verspieltes und kein Comic-Look, aber auch nichts Behördliches und Trockenes.
3. **Ein Fach, eine Welt:** Jedes Fach ist sofort an seiner eigenen Gestaltung erkennbar.
4. **Datensparsam und selbst gehostet:** Keine Fremdressourcen, kein Tracking, Lernstand nur auf dem Gerät.
5. **Fakten sind geprüft:** Inhalte und Zahlen werden nicht erfunden; Demonstrationsmaterial ist als fiktiv gekennzeichnet.

## Accessibility & Inclusion

Gute Lesbarkeit auf kleinen Bildschirmen (ab 320 px), ausreichende Kontraste, Tastaturbedienung, Vorlesefunktion vorhanden; Bewegungen respektieren `prefers-reduced-motion`.
