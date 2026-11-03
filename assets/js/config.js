/* Feibitur – Konfiguration
 * chatEndpoint: URL des Cloudflare Workers für den KI-Chatbot (siehe tools/chat-worker/ANLEITUNG.md).
 * Leer lassen, solange der Worker nicht eingerichtet ist – dann zeigt die Seite einen Hinweis statt des Chats.
 * memoryEndpoint: WebSocket-Adresse des Vermittlers für das Online-Memory (siehe tools/memory-online/ANLEITUNG.md),
 * z. B. "wss://feibitur-memory.DEINNAME.workers.dev/spiel". Leer lassen = Online-Modus wird nicht angeboten.
 */
window.FEIBITUR_CONFIG = {
  chatEndpoint: "https://feibitur-chat.feindt.workers.dev",
  memoryEndpoint: "wss://feibitur-memory.feindt.workers.dev/spiel"
};
