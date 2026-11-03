# KI-Chatbot für Feibitur einrichten (kostenlos, ca. 10 Minuten)

Der Chatbot läuft über einen **Cloudflare Worker** mit **Cloudflare Workers AI**.
Beides ist im kostenlosen Tarif nutzbar: Workers AI enthält **10.000 „Neurons“ pro Tag** (Rücksetzung um 0 Uhr UTC).
Mit dem voreingestellten Modell **Mistral Small 3.1** reicht das grob für 200–270 Antworten pro Tag (Schätzung).
Ist das Kontingent aufgebraucht, meldet der Chatbot das bis zum nächsten Tag.

Die Beschriftungen im Cloudflare-Dashboard ändern sich gelegentlich; sinngemäß gleiche Knöpfe sind gemeint.

## 1. Worker anlegen
1. Unter <https://dash.cloudflare.com> anmelden.
2. Links **Compute (Workers)** bzw. **Workers & Pages** öffnen → **Create** / **Create application**.
3. Die Vorlage **Hello World** („Start with Hello World!“) wählen.
4. Als Namen `feibitur-chat` eintragen → **Deploy**.

## 2. Code einfügen
1. Im neuen Worker **Edit code** wählen.
2. Den gesamten Beispielcode löschen und den Inhalt von `tools/chat-worker/worker.js` einfügen.
3. **Deploy** klicken.

## 3. Workers AI verbinden
1. Im Worker **Settings** (bzw. **Bindings**) → **Add binding** → **Workers AI**.
2. Als Variablennamen exakt `AI` eintragen → **Add binding** / speichern.

## 4. Variablen (optional)
Unter **Settings** → **Variables and Secrets**:
- `ALLOWED_ORIGINS` = `https://feibitur.janrickmer.de` (Standard; nur ändern, wenn sich die Adresse ändert)
- `MODEL` = anderes Modell, falls gewünscht (Standard: `@cf/mistralai/mistral-small-3.1-24b-instruct`;
  Alternative mit höherem Verbrauch: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`).

## 5. Protokolle ausgeschaltet lassen
Unter **Settings** → **Observability** die Workers-Logs **deaktiviert** lassen, damit keine Anfragen protokolliert werden.

## 6. Adresse in Feibitur eintragen
1. Die Adresse des Workers kopieren (z. B. `https://feibitur-chat.DEINNAME.workers.dev`).
2. In `assets/js/config.js` bei `chatEndpoint` eintragen, committen und mit `sh tools/deploy.sh` veröffentlichen.
   Danach erscheint auf der Seite die Einwilligungsabfrage für den Chatbot.

## Datenschutz
- Der Worker speichert und protokolliert keine Gesprächsinhalte.
- Die Verarbeitung erfolgt bei Cloudflare, Inc. (USA). Die Datenschutzerklärung von Feibitur weist darauf hin; die Nutzung erfolgt nur nach ausdrücklicher Einwilligung.
