# KI-Chatbot für Feibitur einrichten (kostenlos, ca. 10 Minuten)

Der Chatbot läuft über einen **Cloudflare Worker** mit **Cloudflare Workers AI**.
Beides ist im kostenlosen Tarif nutzbar; Workers AI hat ein kostenloses Tageskontingent.
Ist es aufgebraucht, meldet der Chatbot das bis zum nächsten Tag.

## 1. Cloudflare-Konto anlegen
1. Auf <https://dash.cloudflare.com/sign-up> ein kostenloses Konto erstellen (E-Mail bestätigen).

## 2. Worker erstellen
1. Im Dashboard links **Workers & Pages** → **Create** → **Create Worker** (Vorlage „Hello World“).
2. Als Namen `feibitur-chat` eintragen → **Deploy**.
3. Auf **Edit code** klicken, den gesamten Beispielcode löschen und den Inhalt von
   `tools/chat-worker/worker.js` aus diesem Repository einfügen → **Deploy**.

## 3. Workers AI verbinden
1. Im Worker auf **Settings** → **Bindings** → **Add** → **Workers AI**.
2. Als Variablennamen exakt `AI` eintragen → speichern/deployen.

## 4. (Optional) Variablen
Unter **Settings** → **Variables and Secrets**:
- `ALLOWED_ORIGINS` = `https://feibitur.janrickmer.de` (Standard, nur ändern, wenn sich die Adresse ändert)
- `MODEL` = anderes Modell, falls gewünscht (Standard: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`).
  Ein kleineres Modell (z. B. `@cf/meta/llama-3.1-8b-instruct-fast`) verbraucht weniger Kontingent, antwortet aber schwächer auf Deutsch.

## 5. Adresse in Feibitur eintragen
1. Die Adresse des Workers kopieren (z. B. `https://feibitur-chat.DEINNAME.workers.dev`).
2. In `assets/js/config.js` bei `chatEndpoint` eintragen und committen.
   Danach erscheint auf der Seite die Einwilligungsabfrage für den Chatbot.

## Datenschutz
- Der Worker speichert und protokolliert keine Gesprächsinhalte (in den Worker-Einstellungen **Observability/Logs** ausgeschaltet lassen).
- Die Verarbeitung erfolgt bei Cloudflare, Inc. (USA). Die Datenschutzerklärung von Feibitur weist darauf hin; die Nutzung erfolgt nur nach ausdrücklicher Einwilligung.
