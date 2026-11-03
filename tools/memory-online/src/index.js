/**
 * Feibitur – Vermittler für das Online-Fachbegriffe-Memory
 *
 * Zwei Geräte verbinden sich per WebSocket mit demselben „Raum“. Der Raum ergibt sich aus den
 * beiden 4-stelligen Codes (jede Person gibt den Code der anderen ein) und dem Unterthema.
 * Der Raum leitet Spielzüge nur an das jeweils andere Gerät weiter. Es wird nichts gespeichert
 * und nichts protokolliert; der Raum verschwindet, sobald beide Verbindungen getrennt sind.
 *
 * Läuft im kostenlosen Workers-Tarif (SQLite-basierte Durable Objects, WebSocket-Hibernation).
 */
import { DurableObject } from "cloudflare:workers";

const DEFAULT_ORIGINS = "https://feibitur.janrickmer.de";
const CODE_RE = /^[A-HJ-NP-Z2-9]{4}$/;   // ohne I, O, 0, 1 (Verwechslungsgefahr)
const THEMA_RE = /^[a-z0-9-]{1,24}$/;
const MAX_MSG = 16000;

function text(body, status) {
  return new Response(body, { status: status || 200, headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" } });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/") return text("Feibitur-Memory: Vermittler für Online-Spiele. Bitte über https://feibitur.janrickmer.de spielen.");
    if (url.pathname !== "/spiel") return text("Nicht gefunden.", 404);
    if ((request.headers.get("Upgrade") || "").toLowerCase() !== "websocket") return text("WebSocket erwartet.", 426);
    const allowed = (env.ALLOWED_ORIGINS || DEFAULT_ORIGINS).split(",").map((s) => s.trim()).filter(Boolean);
    if (!allowed.includes(request.headers.get("Origin") || "")) return text("Ursprung nicht erlaubt.", 403);
    const ich = (url.searchParams.get("ich") || "").toUpperCase();
    const du = (url.searchParams.get("du") || "").toUpperCase();
    const thema = url.searchParams.get("thema") || "";
    if (!CODE_RE.test(ich) || !CODE_RE.test(du) || ich === du || !THEMA_RE.test(thema)) return text("Ungültige Codes.", 400);
    const raum = [ich, du].sort().join("-") + ":" + thema;
    return env.RAUM.get(env.RAUM.idFromName(raum)).fetch(request);
  },
};

export class Raum extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    // Lebenszeichen der Geräte beantworten, ohne den Raum aufzuwecken (kostet nichts)
    this.ctx.setWebSocketAutoResponse(new WebSocketRequestResponsePair('{"t":"ping"}', '{"t":"pong"}'));
  }

  sockets() {
    return this.ctx.getWebSockets().map((ws) => ({ ws, a: ws.deserializeAttachment() || {} }));
  }

  send(ws, obj) {
    try { ws.send(JSON.stringify(obj)); } catch (e) { /* Verbindung bereits geschlossen */ }
  }

  async fetch(request) {
    const url = new URL(request.url);
    const ich = url.searchParams.get("ich").toUpperCase();
    const du = url.searchParams.get("du").toUpperCase();
    // Dasselbe Gerät verbindet sich neu: alte Verbindung ersetzen
    for (const s of this.sockets()) {
      if (s.a.code === ich) { s.ws.serializeAttachment({ code: s.a.code, peer: s.a.peer, alt: true }); try { s.ws.close(4000, "ersetzt"); } catch (e) {} }
    }
    const fremd = this.sockets().filter((s) => !s.a.alt && s.a.code !== ich && s.a.code !== du);
    if (fremd.length) return text("Raum belegt.", 409);
    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);
    this.ctx.acceptWebSocket(server);
    server.serializeAttachment({ code: ich, peer: du });
    const host = [ich, du].sort()[0];
    const partner = this.sockets().find((s) => !s.a.alt && s.a.code === du && s.a.peer === ich);
    if (partner) {
      this.send(partner.ws, { t: "paired", host });
      this.send(server, { t: "paired", host });
    } else {
      this.send(server, { t: "wait" });
    }
    return new Response(null, { status: 101, webSocket: client });
  }

  async webSocketMessage(ws, message) {
    if (typeof message !== "string" || message.length > MAX_MSG) return;
    const me = ws.deserializeAttachment() || {};
    if (me.alt) return;
    for (const s of this.sockets()) {
      if (s.ws !== ws && !s.a.alt && s.a.code === me.peer) { try { s.ws.send(message); } catch (e) {} }
    }
  }

  async webSocketClose(ws, code, reason) {
    this.left(ws);
    try { ws.close(code === 1005 || code === 1006 ? 1000 : code, reason); } catch (e) {}
  }

  async webSocketError(ws) {
    this.left(ws);
  }

  left(ws) {
    const me = ws.deserializeAttachment() || {};
    if (me.alt) return;   // ersetzte Verbindung: Partner nicht beunruhigen
    for (const s of this.sockets()) {
      if (s.ws !== ws && !s.a.alt && s.a.code === me.peer) this.send(s.ws, { t: "peer-left" });
    }
  }
}
