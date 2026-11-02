/* Feibitur – Konfiguration
 * chatEndpoint: URL des Cloudflare Workers für den KI-Chatbot (siehe tools/chat-worker/ANLEITUNG.md).
 * Leer lassen, solange der Worker nicht eingerichtet ist – dann zeigt die Seite einen Hinweis statt des Chats.
 * Beispiel: "https://feibitur-chat.DEINNAME.workers.dev"
 */
window.FEIBITUR_CONFIG = {
  chatEndpoint: ""
};
