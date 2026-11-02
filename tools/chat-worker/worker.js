/**
 * Feibitur – KI-Tutor (Cloudflare Worker mit Workers AI)
 *
 * Nimmt Fragen von der Feibitur-Webseite entgegen und beantwortet sie mit einem
 * Sprachmodell von Cloudflare Workers AI (kostenloses Tageskontingent).
 * - Es wird nichts gespeichert und nichts protokolliert.
 * - Anfragen werden nur von den erlaubten Ursprüngen (ALLOWED_ORIGINS) angenommen.
 * - Der System-Prompt wird hier serverseitig festgelegt; die Webseite schickt nur
 *   Thema und Gesprächsverlauf.
 *
 * Benötigt im Worker:
 *   - Workers-AI-Bindung mit dem Variablennamen  AI
 *   - optional Variable ALLOWED_ORIGINS (kommagetrennt), Standard: https://feibitur.janrickmer.de
 *   - optional Variable MODEL, Standard: @cf/meta/llama-3.3-70b-instruct-fp8-fast
 */

const DEFAULT_ORIGINS = "https://feibitur.janrickmer.de";
const DEFAULT_MODEL = "@cf/meta/llama-3.3-70b-instruct-fp8-fast";

function systemPrompt(thema, stichworte) {
  return (
    "Du bist ein geduldiger KI-Tutor für das Fach Politik und Wirtschaft in der gymnasialen Oberstufe in Hessen " +
    "(Vorbereitung auf das Landesabitur 2027). " +
    (thema ? "Aktuelles Unterthema: " + thema + ". " : "") +
    (stichworte ? "Stichworte laut Kerncurriculum: " + stichworte + ". " : "") +
    "Antworte immer auf Deutsch, sachlich korrekt und verständlich für 17- bis 19-Jährige, eher kurz (höchstens etwa 200 Wörter), mit Beispielen. " +
    "Verwende Fachbegriffe und erkläre sie. Bleib politisch neutral (Beutelsbacher Konsens: Kontroverses kontrovers darstellen, nicht überwältigen). " +
    "Wenn du dir bei Fakten, Zahlen oder aktuellen Ereignissen unsicher bist, sag das deutlich und empfiehl, es nachzuprüfen. " +
    "Schreibe keine kompletten Hausaufgaben oder Klausurlösungen, sondern hilf beim Verstehen. " +
    "Frage niemals nach persönlichen Daten. Wenn jemand persönliche Daten nennt, weise freundlich darauf hin, dies nicht zu tun. " +
    "Beantworte nur Fragen mit Bezug zu Politik, Wirtschaft, Gesellschaft und Lernen für das Abitur."
  );
}

function json(obj, status, headers) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...headers, "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });
}

export default {
  async fetch(request, env) {
    const allowed = (env.ALLOWED_ORIGINS || DEFAULT_ORIGINS).split(",").map((s) => s.trim()).filter(Boolean);
    const origin = request.headers.get("Origin") || "";
    const cors = {
      "Access-Control-Allow-Origin": allowed.includes(origin) ? origin : allowed[0],
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400",
      Vary: "Origin",
    };

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (request.method !== "POST") return json({ error: "Nur POST erlaubt." }, 405, cors);
    if (!allowed.includes(origin)) return json({ error: "Ursprung nicht erlaubt." }, 403, cors);

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return json({ error: "Ungültige Anfrage." }, 400, cors);
    }

    const thema = typeof body.thema === "string" ? body.thema.slice(0, 300) : "";
    const stichworte = typeof body.stichworte === "string" ? body.stichworte.slice(0, 2000) : "";
    const verlauf = Array.isArray(body.messages) ? body.messages : [];
    const messages = verlauf
      .filter((m) => m && (m.role === "user" || m.role === "assistant") && typeof m.content === "string")
      .slice(-10)
      .map((m) => ({ role: m.role, content: m.content.slice(0, 2000) }));
    if (!messages.length || messages[messages.length - 1].role !== "user") {
      return json({ error: "Keine Frage gefunden." }, 400, cors);
    }

    try {
      const out = await env.AI.run(env.MODEL || DEFAULT_MODEL, {
        messages: [{ role: "system", content: systemPrompt(thema, stichworte) }, ...messages],
        max_tokens: 700,
        temperature: 0.4,
      });
      const reply = (out && (out.response || (out.choices && out.choices[0] && out.choices[0].message && out.choices[0].message.content))) || "";
      return json({ reply: String(reply).trim() }, 200, cors);
    } catch (e) {
      const msg = String(e && e.message ? e.message : e);
      const status = /limit|quota|capacity|429/i.test(msg) ? 429 : 502;
      return json({ error: status === 429 ? "Tageskontingent erreicht." : "KI-Dienst nicht erreichbar." }, status, cors);
    }
  },
};
