# Online-Memory: Vermittler bei Cloudflare einrichten (kostenlos)

Der Vermittler verbindet zwei Geräte für das Online-Fachbegriffe-Memory. Er läuft als Cloudflare Worker
mit einem „Durable Object“ im kostenlosen Workers-Tarif (100.000 Anfragen pro Tag; ein Spiel braucht nur einige Dutzend).
Es wird nichts gespeichert und nichts protokolliert.

## Einmalig: Worker aus dem GitHub-Repository anlegen
Die Beschriftungen stehen hier so, wie sie im deutschen Cloudflare-Dashboard ungefähr heißen; in Klammern der englische Originalname.

1. <https://dash.cloudflare.com> → **Workers & Pages** → **Anwendung erstellen** (Create application).
2. **GitHub** bzw. **Repository importieren** wählen, GitHub verbinden und das Repository `janrickmer/feibitur` auswählen
   (dazu einmalig der Cloudflare-App auf GitHub Zugriff auf dieses Repository geben).
3. Einstellungen:
   - **Projektname** (Project name): `feibitur-memory` – muss genau zum Namen in `wrangler.jsonc` passen, sonst bricht der Build ab
   - **Git-Branch** (Git branch): `gh-pages` – Cloudflare schlägt `main` vor; diesen Branch gibt es hier nicht
   - **Build-Befehl** (Build command): leer lassen
   - **Bereitstellungsbefehl** (Deploy command): `npx wrangler deploy` (Standard)
   - **Stammverzeichnis / Pfad** (Root directory, ggf. unter „Erweiterte Einstellungen“): `tools/memory-online`
   - **API-Token:** nichts ändern, Cloudflare legt ihn selbst an
   - **Vorschau-Builds aktivieren:** aus (nicht nötig)
   - **Mit Cloudflare Access schützen:** **aus** – sonst steht eine Anmeldeseite vor dem Worker und kein Spiel kann verbinden
4. **Speichern und bereitstellen** (Save and Deploy). Nach etwa einer Minute ist der Worker unter
   `https://feibitur-memory.DEINNAME.workers.dev` erreichbar (die Seite zeigt dann „Feibitur-Memory: Vermittler für Online-Spiele …“).
5. Die Adresse in `assets/js/config.js` bei `memoryEndpoint` eintragen – mit `wss://` und `/spiel` am Ende,
   z. B. `wss://feibitur-memory.feindt.workers.dev/spiel` – und veröffentlichen (`sh tools/deploy.sh`).

Danach baut Cloudflare den Worker bei jedem Push auf `gh-pages` (also bei jeder Veröffentlichung) automatisch neu.
Das ist im kostenlosen Tarif unbedenklich; ändert sich `tools/memory-online` nicht, bleibt der Worker inhaltlich gleich.

## Lokal testen
```
cd tools/memory-online
npx wrangler dev --port 8787 --var ALLOWED_ORIGINS:http://localhost:8765
```
