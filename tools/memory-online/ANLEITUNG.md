# Online-Memory: Vermittler bei Cloudflare einrichten (kostenlos)

Der Vermittler verbindet zwei Geräte für das Online-Fachbegriffe-Memory. Er läuft als Cloudflare Worker
mit einem „Durable Object“ im kostenlosen Workers-Tarif (100.000 Anfragen pro Tag; ein Spiel braucht nur einige Dutzend).
Es wird nichts gespeichert und nichts protokolliert.

## Einmalig: Worker aus dem GitHub-Repository anlegen
1. <https://dash.cloudflare.com> → **Workers & Pages** (bzw. **Compute (Workers)**) → **Create** / **Create application**.
2. **Import a repository** (bzw. „Mit Git verbinden“) wählen, GitHub verbinden und das Repository `janrickmer/feibitur` auswählen
   (dazu einmalig der Cloudflare-App auf GitHub Zugriff auf dieses Repository geben).
3. Einstellungen:
   - **Project name / Worker-Name:** `feibitur-memory` (muss zum Namen in `wrangler.jsonc` passen)
   - **Production branch:** `gh-pages`
   - **Root directory / Pfad:** `tools/memory-online`
   - **Build command:** leer lassen; **Deploy command:** `npx wrangler deploy` (Standard)
4. **Deploy** klicken. Nach etwa einer Minute ist der Worker unter `https://feibitur-memory.DEINNAME.workers.dev` erreichbar
   (die Seite zeigt dann „Feibitur-Memory: Vermittler für Online-Spiele …“).
5. Die Adresse in `assets/js/config.js` bei `memoryEndpoint` eintragen – mit `wss://` und `/spiel` am Ende,
   z. B. `wss://feibitur-memory.feindt.workers.dev/spiel` – und veröffentlichen (`sh tools/deploy.sh`).

Danach aktualisiert Cloudflare den Worker automatisch, sobald sich `tools/memory-online` im Branch `gh-pages` ändert.

## Lokal testen
```
cd tools/memory-online
npx wrangler dev --port 8787 --var ALLOWED_ORIGINS:http://localhost:8765
```
