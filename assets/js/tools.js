/* Feibitur – Lerntools (laufen komplett im Browser, Lernstände nur im localStorage) */
(function () {
  "use strict";
  var F = window.Feibitur;
  if (!F) return;
  var $ = F.$, $all = F.$all, esc = F.esc, store = F.store, I = F.icon;
  var LT = null, VS = null;

  function data() {
    if (LT && VS) return Promise.resolve();
    return Promise.all([F.fetchJSON("data/lerntools.json"), F.fetchJSON("data/vorschlaege.json")]).then(function (r) { LT = r[0]; VS = r[1]; });
  }
  function metas() {
    var out = [];
    F.site().tabs.forEach(function (tab) { tab.themen.forEach(function (t) { if (t.content) out.push(t); }); });
    return out;
  }
  function allTopics() {
    var ms = metas();
    return Promise.all(ms.map(F.loadTopic)).then(function (ts) {
      return ms.map(function (m, i) { return { meta: m, topic: ts[i] }; }).filter(function (x) { return x.topic; });
    });
  }
  function kurs() { return store("kurs") === "LK" ? "LK" : "GK"; }
  function kursSwitch() {
    var k = F.kursWahl();
    return '<div class="seg" role="group" aria-label="Kurs"><button data-kurs="GK" aria-pressed="' + (k === "GK") + '">Grundkurs</button><button data-kurs="LK" aria-pressed="' + (k === "LK") + '">Leistungskurs</button></div>' +
      (k ? "" : '<span class="kurs-hint-inline">Bitte wähle deinen Kurs.</span>');
  }
  function termOK(b) { return !b.lk || kurs() === "LK"; }
  function bindKurs(root, cb) {
    $all("[data-kurs]", root).forEach(function (b) {
      b.addEventListener("click", function () { store("kurs", b.getAttribute("data-kurs")); cb(); });
    });
  }
  function tabOf(meta) { return meta.tab; }
  function topicLink(meta, sec) { return "#/powi/" + tabOf(meta) + "/" + meta.id + "/" + (sec || (meta.methode ? "inhalte" : "begriffe")); }
  function topicSelect(id, sel, filter) {
    var html = '<select id="' + id + '">';
    F.site().tabs.forEach(function (tab) {
      var opts = tab.themen.filter(function (t) { return t.content && (!filter || filter(t)); });
      if (!opts.length) return;
      html += '<optgroup label="' + esc(tab.titel) + '">' + opts.map(function (t) {
        return '<option value="' + t.id + '"' + (t.id === sel ? " selected" : "") + ">" + esc(t.nr + " " + t.titel) + "</option>";
      }).join("") + "</optgroup>";
    });
    return html + "</select>";
  }
  function fmt(d) { return d.split("-").reverse().join("."); }
  function daysUntil(iso) { var a = new Date(F.today() + "T00:00:00"), b = new Date(iso + "T00:00:00"); return Math.round((b - a) / 86400000); }
  function download(name, text, type) {
    var blob = new Blob([text], { type: type || "text/plain;charset=utf-8" });
    var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function copy(text, btn) {
    function done() { if (btn) { var o = btn.textContent; btn.textContent = "Kopiert ✓"; setTimeout(function () { btn.textContent = o; }, 1400); } }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () { prompt("Zum Kopieren markieren:", text); });
    else prompt("Zum Kopieren markieren:", text);
  }
  function stripHTML(h) { var d = document.createElement("div"); d.innerHTML = h; return d.textContent; }

  // ------------------------------------------------------------------ Übersicht
  var TOOLS = [
    { slug: "lernplan", g: "Planen und Überblick behalten", t: "Abi-Countdown und Lernplan", d: "Tage bis zur Prüfung und ein Wochenplan, der die Schwerpunkte des Abiturerlasses zuerst abdeckt – mit Kalender-Export." },
    { slug: "fortschritt", g: "Planen und Überblick behalten", t: "Fortschritts-Dashboard", d: "Ampel je Unterthema: Karteikarten, bearbeitete Aufgaben und Selbsteinschätzung auf einen Blick." },
    { slug: "kannlisten", g: "Planen und Überblick behalten", t: "„Ich kann …“-Checklisten", d: "Kann-Sätze aus Kerncurriculum und Abiturerlass – schätze dich mit Rot, Gelb oder Grün ein." },
    { slug: "operatoren", g: "Üben mit sofortiger Rückmeldung", t: "Operatoren-Trainer", d: "Definitionen erkennen, Aufgaben verstehen und prüfen, ob eine Antwort den Operator erfüllt." },
    { slug: "schnelltest", g: "Üben mit sofortiger Rückmeldung", t: "Schnelltests", d: "10 Fragen je Unterthema mit Erklärung – falsche Begriffe wandern in deine Lernkartei." },
    { slug: "wiederholung", g: "Üben mit sofortiger Rückmeldung", t: "Tägliche Wiederholung (Lernkartei)", d: "Lernkartei mit 5 Fächern über alle Themen: Was heute fällig ist, kommt dran." },
    { slug: "simulation", g: "Abiturnah trainieren", t: "Abi-Simulation", d: "Drei komplette Vorschläge, einen auswählen, mit Timer schreiben – Korrekturdatei für den ganzen Vorschlag." },
    { slug: "baukasten", g: "Abiturnah trainieren", t: "Formulierungs-Baukasten", d: "Einleitungssatz-Generator und Satzbausteine für Analyse, Urteil und Fazit." },
    { slug: "beispiele", g: "Abiturnah trainieren", t: "Schwach vs. stark", d: "Musterantworten je Operator: Was macht den Unterschied zwischen einer schwachen und einer starken Lösung?" },
    { slug: "begriffsnetz", g: "Vernetzen und Wiederholen", t: "Begriffsnetz", d: "Sieh, wie Fachbegriffe über alle Halbjahre zusammenhängen – ideal für Querverbindungen im Abitur." },
    { slug: "lernzettel", g: "Vernetzen und Wiederholen", t: "Lernzettel und Karteikarten drucken", d: "Ein Lernzettel je Unterthema und Karteikarten zum Ausschneiden – als Ausdruck oder PDF." },
    { slug: "vorlesen", g: "Vernetzen und Wiederholen", t: "Vorlesen", d: "Lass dir Inhalte von der Sprachausgabe deines Geräts vorlesen – Einstellungen für Stimme und Tempo." },
  ];

  function shell(title, sub, inner, slug) {
    document.title = title + " – Feibitur";
    F.app.innerHTML = F.topbar((slug ? '<a class="btn btn-small btn-tools" href="#/lerntools" aria-label="Alle Lerntools">' + I.tools + "<span>Alle Lerntools</span></a>" : "") + '<a class="btn btn-small" href="#/powi">Politik und Wirtschaft</a>') +
      '<section class="tools-hero"><div class="tools-hero-in"><h1>' + esc(title) + "</h1>" + (sub ? "<p>" + sub + "</p>" : "") + "</div></section>" +
      '<main class="tools-main" id="tools-main">' + inner + "</main>" + F.footer();
    window.scrollTo(0, 0);
    return $("#tools-main");
  }

  function overview() {
    var groups = [];
    TOOLS.forEach(function (t) { if (groups.indexOf(t.g) < 0) groups.push(t.g); });
    var html = groups.map(function (g) {
      return '<section class="tool-group"><h2>' + esc(g) + '</h2><div class="tool-grid">' + TOOLS.filter(function (t) { return t.g === g; }).map(function (t) {
        return '<a class="tool-card" href="#/lerntools/' + t.slug + '"><span class="tool-title">' + esc(t.t) + '</span><span class="tool-desc">' + esc(t.d) + "</span>" + I.arrow + "</a>";
      }).join("") + "</div></section>";
    }).join("");
    shell("Lerntools", "Werkzeuge für dein Selbstlernen in Politik und Wirtschaft. Alles läuft in deinem Browser – dein Lernstand wird nur auf deinem Gerät gespeichert.", html);
  }

  // ------------------------------------------------------------------ 1. Lernplan
  function lernplan(main) {
    var p = store("lernplan") || {};
    var k = kurs(), exam = LT.termine[k], days = daysUntil(exam);
    var start = p.start || F.today(), wdh = p.wdh == null ? 2 : p.wdh, alle = !!p.alle;
    var ms = metas().filter(function (m) { return !m.methode && (alle || m.erlass); });
    function monday(iso) { var d = new Date(iso + "T00:00:00"); var wd = (d.getDay() + 6) % 7; d.setDate(d.getDate() - wd); return d; }
    var s0 = monday(start), ex = new Date(exam + "T00:00:00");
    var weeks = Math.floor((ex - s0) / (7 * 86400000));
    var lern = weeks - wdh;
    var plan = [];
    for (var w = 0; w < Math.max(weeks, 0); w++) {
      var a = new Date(s0); a.setDate(a.getDate() + 7 * w); var b = new Date(a); b.setDate(b.getDate() + 6);
      plan.push({ von: F.isoDate(a), bis: F.isoDate(b), themen: [], wdh: w >= lern });
    }
    if (lern > 0) ms.forEach(function (m, i) { plan[Math.floor(i * lern / ms.length)].themen.push(m); });
    var done = store("lernplanDone") || {};
    var html = '<div class="tools-controls">' + kursSwitch() +
      '<label>Start <input type="date" id="lp-start" value="' + start + '"></label>' +
      '<label>Wiederholungsphase <select id="lp-wdh">' + [0, 1, 2, 3].map(function (n) { return '<option value="' + n + '"' + (n === wdh ? " selected" : "") + ">" + n + " Woche" + (n === 1 ? "" : "n") + "</option>"; }).join("") + "</select></label>" +
      '<label class="chk"><input type="checkbox" id="lp-alle"' + (alle ? " checked" : "") + "> auch Themen ohne Erlass-Schwerpunkt</label></div>" +
      '<div class="countdown"><div class="cd-num">' + Math.max(days, 0) + '</div><div class="cd-text">Tage bis zur schriftlichen Prüfung im ' + (k === "LK" ? "Leistungskurs" : "Grundkurs") + " am " + fmt(exam) + " (Haupttermin laut Abiturerlass 2027)</div></div>";
    if (weeks <= 0) html += '<p class="placeholder">Der Prüfungstermin ist erreicht oder vorbei.</p>';
    else if (lern <= 0) html += '<p class="placeholder">Bis zur Prüfung bleibt nur noch die Wiederholungsphase. Konzentriere dich auf die tägliche Wiederholung und die Abi-Simulation.</p>';
    html += '<p class="muted">Wochenplan mit ' + ms.length + " Unterthemen" + (alle ? "" : " (nur Erlass-Schwerpunkte 2027)") + '. Methoden-Grundlagen (Materialanalyse, Sach- und Werturteil) stehen in Woche 1. Hake erledigte Wochen ab.</p><div class="plan">';
    plan.forEach(function (wk, i) {
      var items = wk.wdh ? ['<li>Tägliche Wiederholung der Lernkartei (<a href="#/lerntools/wiederholung">öffnen</a>)</li>', '<li>Mindestens eine <a href="#/lerntools/simulation">Abi-Simulation</a> unter Zeitdruck schreiben</li>', '<li>Kann-Listen durchgehen: Was ist noch rot oder gelb?</li>']
        : wk.themen.map(function (m) { return '<li><a href="' + topicLink(m) + '">' + esc(m.nr + " " + m.titel) + "</a></li>"; });
      if (i === 0 && !wk.wdh) items.unshift('<li><a href="#/powi/grundlagen">Grundlagen: Materialanalyse, Sachurteil, Werturteil</a></li>');
      var todo = wk.wdh ? "" : (wk.themen.length ? '<p class="muted small">Je Thema: Fachbegriffe bis mindestens Fach 3, Inhalte durcharbeiten, Kann-Liste auf Grün, je eine Aufgabe aus AFB I, II und III.</p>' : '<p class="muted small">Puffer: Liegengebliebenes nachholen und wiederholen.</p>');
      html += '<div class="plan-week' + (done[wk.von] ? " done" : "") + (wk.wdh ? " wdh" : "") + '"><label class="chk"><input type="checkbox" data-week="' + wk.von + '"' + (done[wk.von] ? " checked" : "") + "> <b>Woche " + (i + 1) + "</b> · " + fmt(wk.von) + " – " + fmt(wk.bis) + (wk.wdh ? " · Wiederholung" : "") + "</label><ul>" + items.join("") + "</ul>" + todo + "</div>";
    });
    html += '</div><div class="tools-actions"><button class="btn btn-primary" id="lp-ics">Plan als Kalenderdatei (.ics) herunterladen</button></div>';
    main.innerHTML = html;
    function save(ch) { var q = store("lernplan") || {}; Object.keys(ch).forEach(function (x) { q[x] = ch[x]; }); store("lernplan", q); lernplan(main); }
    bindKurs(main, function () { lernplan(main); });
    $("#lp-start", main).addEventListener("change", function (e) { if (e.target.value) save({ start: e.target.value }); });
    $("#lp-wdh", main).addEventListener("change", function (e) { save({ wdh: parseInt(e.target.value, 10) }); });
    $("#lp-alle", main).addEventListener("change", function (e) { save({ alle: e.target.checked }); });
    $all("[data-week]", main).forEach(function (cb) {
      cb.addEventListener("change", function () { var d = store("lernplanDone") || {}; if (cb.checked) d[cb.getAttribute("data-week")] = true; else delete d[cb.getAttribute("data-week")]; store("lernplanDone", d); cb.closest(".plan-week").classList.toggle("done", cb.checked); });
    });
    $("#lp-ics", main).addEventListener("click", function () {
      function d8(iso) { return iso.replace(/-/g, ""); }
      function next(iso) { var d = new Date(iso + "T00:00:00"); d.setDate(d.getDate() + 1); return d8(F.isoDate(d)); }
      function escI(t) { return String(t).replace(/[\\;,]/g, function (c) { return "\\" + c; }); }
      var L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Feibitur//Lernplan//DE", "CALSCALE:GREGORIAN"];
      var stamp = d8(F.today()) + "T000000Z";
      plan.forEach(function (wk, i) {
        var titel = wk.wdh ? "Feibitur: Wiederholung & Abi-Simulation" : "Feibitur Woche " + (i + 1) + ": " + (wk.themen.map(function (m) { return m.nr; }).join(", ") || "Puffer");
        L.push("BEGIN:VEVENT", "UID:feibitur-" + wk.von + "@feibitur", "DTSTAMP:" + stamp, "DTSTART;VALUE=DATE:" + d8(wk.von), "DTEND;VALUE=DATE:" + next(wk.von),
          "SUMMARY:" + escI(titel), "DESCRIPTION:" + escI(wk.wdh ? "Lernkartei wiederholen, Abi-Simulation schreiben" : wk.themen.map(function (m) { return m.nr + " " + m.titel; }).join(" | ")), "END:VEVENT");
      });
      L.push("BEGIN:VEVENT", "UID:feibitur-abi-" + exam + "@feibitur", "DTSTAMP:" + stamp, "DTSTART;VALUE=DATE:" + d8(exam), "DTEND;VALUE=DATE:" + next(exam),
        "SUMMARY:" + escI("Abitur Politik und Wirtschaft (" + (k === "LK" ? "LK" : "GK") + ")"), "END:VEVENT", "END:VCALENDAR");
      download("feibitur-lernplan.ics", L.join("\r\n"), "text/calendar;charset=utf-8");
    });
  }

  // ------------------------------------------------------------------ 2. Fortschritt
  function kannStatus(tid, list) {
    var st = store("kann") || {}, k = kurs(), c = { g: 0, y: 0, r: 0, n: 0, total: 0 };
    list.forEach(function (it, i) { if (it.lk && k !== "LK") return; c.total++; var v = st[tid + "|" + i]; if (v) c[v]++; else c.n++; });
    return c;
  }
  function fortschritt(main) {
    main.innerHTML = '<p class="muted">Lade deinen Lernstand …</p>';
    allTopics().then(function (all) {
      var l = F.leitner(), erl = store("erledigt") || {}, t = F.today(), dueAll = 0;
      var rows = all.map(function (x) {
        var m = x.meta, tp = x.topic;
        var cards = tp.begriffe.filter(termOK).map(function (b) { return F.cardKey(m.id, b.b); });
        F.migrateKarten(m.id);
        var sicher = 0, begonnen = 0;
        cards.forEach(function (key) { var e = l[key]; if (e) { begonnen++; if (e.f >= 4) sicher++; if (e.d <= t) dueAll++; } });
        var tasks = tp.aufgaben.filter(function (a) { return kurs() === "LK" || !a.lk; });
        var doneT = tasks.filter(function (a) { return erl[a.id]; }).length;
        var kc = kannStatus(m.id, LT.kann[m.id] || []);
        var parts = [];
        if (cards.length) parts.push(sicher / cards.length);
        if (tasks.length) parts.push(doneT / tasks.length);
        if (kc.total) parts.push(kc.g / kc.total);
        var score = parts.length ? parts.reduce(function (a, b) { return a + b; }, 0) / parts.length : 0;
        var started = begonnen || doneT || (kc.total - kc.n);
        var amp = !started ? "grau" : score >= 0.7 ? "gruen" : score >= 0.35 ? "gelb" : "rot";
        function bar(v, n, label) { var pct = n ? Math.round(100 * v / n) : 0; return n ? '<div class="pbar" title="' + label + '"><span style="width:' + pct + '%"></span></div><span class="pnum">' + v + "/" + n + "</span>" : '<span class="muted small">–</span>'; }
        return '<tr><td><span class="ampel ampel-' + amp + '" title="' + { grau: "noch nicht begonnen", gruen: "gut im Plan", gelb: "dranbleiben", rot: "noch viel zu tun" }[amp] + '"></span></td>' +
          '<td><a href="' + topicLink(m) + '">' + esc(m.nr) + "</a> " + esc(m.titel) + (m.erlass ? ' <span class="badge badge-abi">Abi 2027</span>' : "") + "</td>" +
          '<td class="pcell">' + bar(sicher, cards.length, "Karteikarten in Fach 4 oder 5") + "</td><td class=\"pcell\">" + bar(doneT, tasks.length, "bearbeitete Aufgaben") + "</td><td class=\"pcell\">" + bar(kc.g, kc.total, "Kann-Sätze auf Grün") + "</td></tr>";
      }).join("");
      main.innerHTML = '<div class="tools-controls">' + kursSwitch() + '<a class="btn btn-small btn-primary" href="#/lerntools/wiederholung">Heute fällige Karten: ' + dueAll + "</a></div>" +
        '<div class="table-scroll"><table class="ptable"><thead><tr><th></th><th>Unterthema</th><th>Karteikarten sicher<br><span class="muted small">(Fach 4–5)</span></th><th>Aufgaben bearbeitet</th><th>Kann-Liste grün</th></tr></thead><tbody>' + rows + "</tbody></table></div>" +
        '<p class="muted small">Ampel: Durchschnitt der drei Werte – Grün ab 70 %, Gelb ab 35 %, grau = noch nicht begonnen. Aufgaben hakst du in den Übungsaufgaben ab, Kann-Sätze in den <a href="#/lerntools/kannlisten">Kann-Listen</a>.</p>' +
        '<div class="tools-actions"><button class="btn btn-small" id="reset-all">Gesamten Lernstand auf diesem Gerät löschen</button></div>';
      bindKurs(main, function () { fortschritt(main); });
      $("#reset-all", main).addEventListener("click", function () {
        if (!confirm("Wirklich den gesamten Lernstand (Karteikarten, Aufgaben, Kann-Listen, Lernplan, Simulation) auf diesem Gerät löschen?")) return;
        ["leitner", "erledigt", "kann", "lernplan", "lernplanDone", "sim", "opBest"].forEach(F.unstore);
        fortschritt(main);
      });
    });
  }

  // ------------------------------------------------------------------ 3. Kann-Listen
  function kannlisten(main, sel) {
    var cur = sel || store("kannThema") || "q1-1";
    if (!LT.kann[cur]) cur = Object.keys(LT.kann)[0];
    var m = F.meta[cur], list = LT.kann[cur] || [], st = store("kann") || {}, k = kurs();
    var c = kannStatus(cur, list);
    var html = '<div class="tools-controls">' + kursSwitch() + '<label>Unterthema ' + topicSelect("kl-sel", cur, function (t) { return !!LT.kann[t.id]; }) + "</label></div>" +
      '<div class="kann-head"><h2>' + esc(m.nr + " " + m.titel) + '</h2><a class="btn btn-small" href="' + topicLink(m, m.methode ? "inhalte" : "inhalte") + '">Zu den Inhalten</a></div>' +
      '<p class="muted">Schätze dich ehrlich ein: <b>Rot</b> = kann ich noch nicht, <b>Gelb</b> = teilweise, <b>Grün</b> = sicher. ' + c.g + " von " + c.total + " grün.</p><ul class=\"kann-list\">";
    list.forEach(function (it, i) {
      if (it.lk && k !== "LK") return;
      var v = st[cur + "|" + i] || "";
      html += '<li class="kann-item kann-' + (v || "n") + '"><div class="kann-text">' + esc(it.t) + (it.lk ? ' <span class="badge badge-lk">LK</span>' : "") + (!it.abi ? ' <span class="badge badge-noabi">kein Schwerpunkt 2027</span>' : "") + "</div>" +
        '<div class="kann-btns" role="group" aria-label="Selbsteinschätzung">' + [["r", "Rot"], ["y", "Gelb"], ["g", "Grün"]].map(function (o) {
          return '<button class="kb kb-' + o[0] + '" data-k="' + i + '" data-v="' + o[0] + '" aria-pressed="' + (v === o[0]) + '" title="' + o[1] + '"><span class="visually-hidden">' + o[1] + "</span></button>";
        }).join("") + "</div></li>";
    });
    html += "</ul>";
    main.innerHTML = html;
    bindKurs(main, function () { kannlisten(main, cur); });
    $("#kl-sel", main).addEventListener("change", function (e) { store("kannThema", e.target.value); kannlisten(main, e.target.value); });
    $all("[data-k]", main).forEach(function (b) {
      b.addEventListener("click", function () {
        var s = store("kann") || {}, key = cur + "|" + b.getAttribute("data-k"), v = b.getAttribute("data-v");
        if (s[key] === v) delete s[key]; else s[key] = v;
        store("kann", s); kannlisten(main, cur);
      });
    });
  }

  // ------------------------------------------------------------------ 4. Operatoren-Trainer (ohne Anforderungsbereich)
  var GRUPPEN = [["beschreiben", "darstellen", "wiedergeben", "zusammenfassen", "nennen", "skizzieren"],
    ["erklären", "erläutern", "analysieren", "herausarbeiten", "untersuchen", "auswerten", "anwenden"],
    ["vergleichen/gegenüberstellen", "in Beziehung setzen", "einordnen/zuordnen", "charakterisieren", "interpretieren"],
    ["beurteilen", "bewerten/Stellung nehmen", "erörtern", "diskutieren/sich auseinandersetzen mit", "überprüfen", "entwickeln", "gestalten/entwerfen"]];
  var OPS_ALLOWED = null;
  function opKeys() {
    if (!OPS_ALLOWED) OPS_ALLOWED = Object.keys(F.site().operatoren).filter(function (k) { return k !== "berechnen"; });
    return OPS_ALLOWED;
  }
  function distractors(op, n) {
    var g = GRUPPEN.filter(function (x) { return x.indexOf(op) >= 0; })[0] || [];
    var same = F.shuffle(g.filter(function (x) { return x !== op && opKeys().indexOf(x) >= 0; }));
    var rest = F.shuffle(opKeys().filter(function (x) { return x !== op && same.indexOf(x) < 0; }));
    return same.concat(rest).slice(0, n);
  }
  function operatoren(main, mode) {
    mode = mode || "definition";
    var modes = [["definition", "Definition erkennen"], ["aufgabe", "Was ist zu tun?"], ["antwort", "Erfüllt die Antwort den Operator?"]];
    var best = store("opBest") || {};
    main.innerHTML = '<div class="tools-controls"><div class="seg" role="group" aria-label="Spielmodus">' + modes.map(function (m) { return '<button data-mode="' + m[0] + '" aria-pressed="' + (m[0] === mode) + '">' + m[1] + "</button>"; }).join("") + "</div></div>" +
      '<p class="muted">' + { definition: "Du siehst die offizielle Definition eines Operators (Land Hessen). Welcher Operator ist gemeint?", aufgabe: "Du siehst eine echte Aufgabe aus Feibitur. Was verlangt der Operator darin von dir?", antwort: "Du siehst eine Aufgabe und eine Schülerantwort. Erfüllt die Antwort, was der Operator verlangt?" }[mode] +
      (best[mode] != null ? " · Deine Bestleistung: " + best[mode] + "/10" : "") + '</p><div id="quiz"></div>';
    $all("[data-mode]", main).forEach(function (b) { b.addEventListener("click", function () { operatoren(main, b.getAttribute("data-mode")); }); });
    var quiz = $("#quiz", main);
    var build = mode === "aufgabe" ? allTopics().then(function (all) {
      var tasks = [];
      all.forEach(function (x) { x.topic.aufgaben.forEach(function (a) { tasks.push({ text: a.text, op: a.operator, nr: x.meta.nr }); }); });
      return F.shuffle(tasks).slice(0, 10).map(function (t) {
        var opts = F.shuffle([t.op].concat(distractors(t.op, 3)));
        return { q: '<div class="q-task"><span class="muted small">Aufgabe aus ' + esc(t.nr) + "</span><br>" + t.text + "</div><p><b>Was verlangt der Operator in dieser Aufgabe von dir?</b></p>",
          options: opts.map(function (o) { return { label: F.site().operatoren[o].def, ok: o === t.op }; }),
          explain: "Operator: <b>" + esc(t.op) + "</b> – " + esc(F.site().operatoren[t.op].def) };
      });
    }) : Promise.resolve(mode === "antwort" ? F.shuffle(LT.opCheck).slice(0, 10).map(function (x) {
      return { q: '<p><span class="op-badge">' + esc(x.op) + '</span></p><div class="q-task"><b>Aufgabe:</b> ' + esc(x.aufgabe) + '</div><div class="q-answer"><b>Antwort:</b> ' + esc(x.antwort) + "</div><p><b>Erfüllt diese Antwort den Operator?</b></p>",
        options: [{ label: "Ja, Operator erfüllt", ok: x.ok }, { label: "Nein, Operator nicht erfüllt", ok: !x.ok }], explain: esc(x.warum) + "<br><span class=\"muted small\">Definition: " + esc(F.site().operatoren[x.op].def) + "</span>" };
    }) : F.shuffle(opKeys()).slice(0, 10).map(function (op) {
      var opts = F.shuffle([op].concat(distractors(op, 3)));
      return { q: '<div class="q-task">„' + esc(F.site().operatoren[op].def) + "“</div><p><b>Welcher Operator wird so definiert?</b></p>",
        options: opts.map(function (o) { return { label: o, ok: o === op }; }), explain: "Richtig ist <b>" + esc(op) + "</b>." };
    }));
    build.then(function (qs) { runQuiz(quiz, qs, function (score) { var b2 = store("opBest") || {}; if (b2[mode] == null || score > b2[mode]) { b2[mode] = score; store("opBest", b2); } }, function () { operatoren(main, mode); }); });
  }
  function runQuiz(el, qs, onFinish, onRestart, extraEnd) {
    var i = 0, score = 0, wrong = [];
    function show() {
      if (i >= qs.length) {
        if (onFinish) onFinish(score, wrong);
        el.innerHTML = '<div class="quiz-end"><h3>' + score + " von " + qs.length + " richtig</h3><p>" + (score >= qs.length * 0.8 ? "Sehr gut – du bist sicher!" : score >= qs.length * 0.5 ? "Ordentlich – schau dir die Fehler noch einmal an." : "Dranbleiben – wiederhole die Grundlagen und versuch es noch einmal.") + "</p>" +
          (extraEnd ? extraEnd(score, wrong) : "") + '<button class="btn btn-primary" id="q-again">Neue Runde</button></div>';
        $("#q-again", el).addEventListener("click", onRestart);
        if (extraEnd && extraEnd.bind_) extraEnd.bind_(el, wrong);
        return;
      }
      var q = qs[i];
      el.innerHTML = '<div class="quiz-card"><div class="quiz-meta">Frage ' + (i + 1) + " von " + qs.length + " · " + score + " richtig</div>" + q.q +
        (q.match ? q.match.html : '<div class="q-opts">' + q.options.map(function (o, j) { return '<button class="q-opt" data-o="' + j + '">' + (o.html || esc(o.label)) + "</button>"; }).join("") + "</div>") +
        '<div class="q-feedback" hidden></div><button class="btn btn-primary q-next" hidden>' + (i + 1 < qs.length ? "Weiter" : "Auswertung") + "</button></div>";
      var fb = $(".q-feedback", el), nx = $(".q-next", el);
      function reveal(ok) {
        if (ok) score++; else if (q.ref) wrong.push(q.ref);
        fb.hidden = false; fb.className = "q-feedback " + (ok ? "ok" : "bad");
        fb.innerHTML = "<b>" + (ok ? "Richtig!" : "Leider falsch.") + "</b> " + q.explain;
        nx.hidden = false; nx.focus();
      }
      if (q.match) q.match.bind(el, reveal);
      else $all(".q-opt", el).forEach(function (b) {
        b.addEventListener("click", function () {
          if (!fb.hidden) return;
          var o = q.options[+b.getAttribute("data-o")];
          $all(".q-opt", el).forEach(function (x) { var oo = q.options[+x.getAttribute("data-o")]; x.disabled = true; if (oo.ok) x.classList.add("right"); });
          if (!o.ok) b.classList.add("wrong");
          reveal(o.ok);
        });
      });
      nx.addEventListener("click", function () { i++; show(); });
    }
    show();
  }

  // ------------------------------------------------------------------ 5. Schnelltests
  function schnelltest(main, sel) {
    var cur = sel || store("testThema") || "q1-1";
    if (!F.meta[cur] || !F.meta[cur].content || !F.meta[cur].content.begriffe) cur = "q1-1";
    main.innerHTML = '<div class="tools-controls"><label>Unterthema ' + topicSelect("st-sel", cur, function (t) { return t.content.begriffe > 4; }) + '</label></div><div id="quiz"><p class="muted">Lade Fragen …</p></div>';
    $("#st-sel", main).addEventListener("change", function (e) { store("testThema", e.target.value); schnelltest(main, e.target.value); });
    F.loadTopic(F.meta[cur]).then(function (tp) {
      var terms = tp.begriffe.filter(termOK);
      function mask(text, b) { var w = b.split(/[\s(]/)[0]; return text.replace(new RegExp(w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi"), "…"); }
      var pool = F.shuffle(terms), qs = [];
      pool.slice(0, 4).forEach(function (t) {
        var opts = F.shuffle([t].concat(F.shuffle(terms.filter(function (x) { return x !== t; })).slice(0, 3)));
        qs.push({ ref: t.b, q: '<div class="q-task">„' + esc(mask(stripHTML(t.kurz), t.b)) + "“</div><p><b>Welcher Fachbegriff passt zu dieser Definition?</b></p>",
          options: opts.map(function (o) { return { label: o.b, ok: o === t }; }), explain: "<b>" + esc(t.b) + ":</b> " + t.lang });
      });
      pool.slice(4, 8).forEach(function (t) {
        var opts = F.shuffle([t].concat(F.shuffle(terms.filter(function (x) { return x !== t; })).slice(0, 3)));
        qs.push({ ref: t.b, q: '<div class="q-task"><b>' + esc(t.b) + "</b></div><p><b>Welche Definition ist richtig?</b></p>",
          options: opts.map(function (o) { return { label: stripHTML(o.kurz), ok: o === t }; }), explain: t.lang });
      });
      [pool.slice(8, 12), pool.slice(12, 16)].forEach(function (grp) {
        if (grp.length < 4) return;
        var defs = F.shuffle(grp.slice());
        qs.push({ ref: null, q: "<p><b>Ordne jedem Begriff die passende Kurzdefinition zu.</b></p>",
          match: {
            html: '<div class="match">' + grp.map(function (t, j) {
              return '<div class="match-row"><div class="match-term">' + esc(t.b) + '</div><select data-m="' + j + '"><option value="">– Definition wählen –</option>' + defs.map(function (d, di) { return '<option value="' + di + '">' + esc(stripHTML(d.kurz)) + "</option>"; }).join("") + "</select></div>";
            }).join("") + '<button class="btn btn-small btn-primary" id="m-check">Prüfen</button></div>',
            bind: function (el, reveal) {
              $("#m-check", el).addEventListener("click", function () {
                var all = true;
                $all("[data-m]", el).forEach(function (s) {
                  var j = +s.getAttribute("data-m"), ok = s.value !== "" && defs[+s.value] === grp[j];
                  s.classList.add(ok ? "right" : "wrong"); s.disabled = true; if (!ok) all = false;
                });
                this.disabled = true;
                reveal(all);
              });
            }
          },
          explain: grp.map(function (t) { return "<br><b>" + esc(t.b) + ":</b> " + esc(stripHTML(t.kurz)); }).join("") });
      });
      qs = qs.slice(0, 10);
      var extra = function (score, wrong) { return wrong.length ? '<p>Falsch beantwortet: ' + wrong.map(esc).join(", ") + '</p><button class="btn btn-small" id="to-box">Diese Begriffe in Fach 1 der Lernkartei legen</button> ' : ""; };
      extra.bind_ = function (el, wrong) {
        var b = $("#to-box", el); if (!b) return;
        b.addEventListener("click", function () { wrong.forEach(function (w) { F.rateCard(F.cardKey(cur, w), false); }); b.textContent = "Erledigt ✓ – sie kommen in der Wiederholung dran"; b.disabled = true; });
      };
      runQuiz($("#quiz", main), qs, null, function () { schnelltest(main, cur); }, extra);
    });
  }

  // ------------------------------------------------------------------ 6. Wiederholung (Lernkartei über alle Themen)
  function wiederholung(main) {
    main.innerHTML = '<p class="muted">Lade Lernkartei …</p>';
    allTopics().then(function (all) {
      var cards = [];
      all.forEach(function (x) { F.migrateKarten(x.meta.id); x.topic.begriffe.filter(termOK).forEach(function (b) { cards.push({ key: F.cardKey(x.meta.id, b.b), b: b.b, lang: b.lang, kurz: b.kurz, nr: x.meta.nr, tid: x.meta.id }); }); });
      var l = F.leitner(), t = F.today();
      var known = cards.filter(function (c) { return l[c.key]; });
      var due = known.filter(function (c) { return l[c.key].d <= t; });
      var st = F.fachStats(cards);
      var perTopic = all.map(function (x) {
        var cs = cards.filter(function (c) { return c.tid === x.meta.id; }), s = F.fachStats(cs);
        return "<tr><td>" + esc(x.meta.nr) + "</td><td>" + (cs.length - s.neu) + "/" + cs.length + "</td><td>" + s.faellig + "</td><td>" + (s.f[4] + s.f[5]) + "</td></tr>";
      }).join("");
      main.innerHTML = '<div class="fach-row">' + [1, 2, 3, 4, 5].map(function (i) { return '<div class="fach-box fach-' + i + '"><div class="fb-n">' + st.f[i] + '</div><div class="fb-l">Fach ' + i + "</div></div>"; }).join("") + "</div>" +
        '<p class="muted">Fach 1: täglich · Fach 2: nach 1 Tag · Fach 3: nach 3 Tagen · Fach 4: nach 1 Woche · Fach 5: nach 2 Wochen. Heute fällig: <b>' + due.length + "</b> Karten.</p>" +
        '<div class="tools-actions"><button class="btn btn-primary" id="w-due"' + (due.length ? "" : " disabled") + ">Fällige Karten wiederholen (" + Math.min(due.length, 40) + ")</button>" +
        '<span class="add-new">Neue Karten aus ' + topicSelect("w-sel", store("wThema") || "q1-1", function (tt) { return tt.content.begriffe > 0; }) + ' <button class="btn btn-small" id="w-new">10 neue Karten lernen</button></span></div>' +
        F.memoryBtnHTML().replace("data-memory>", "data-memory> ").replace("spielen</button>", "spielen (Unterthema oben auswählen)</button>") +
        '<div id="w-session"></div><details class="w-details"><summary>Stand je Unterthema</summary><div class="table-scroll"><table class="ptable"><thead><tr><th>Thema</th><th>begonnen</th><th>heute fällig</th><th>sicher (F4–5)</th></tr></thead><tbody>' + perTopic + "</tbody></table></div></details>";
      var sess = $("#w-session", main);
      $("[data-memory]", main).addEventListener("click", function () {
        var tid = $("#w-sel", main).value; store("wThema", tid);
        var x = all.filter(function (y) { return y.meta.id === tid; })[0];
        F.openMemory(x.topic.begriffe.filter(termOK), x.meta.nr + " " + x.meta.titel);
      });
      $("#w-due", main).addEventListener("click", function () { F.cardSession(sess, due, { dueFirst: true, limit: 40 }); sess.scrollIntoView({ behavior: "smooth" }); });
      $("#w-new", main).addEventListener("click", function () {
        var tid = $("#w-sel", main).value; store("wThema", tid);
        var neu = cards.filter(function (c) { return c.tid === tid && !F.leitner()[c.key]; }).slice(0, 10);
        if (!neu.length) { sess.innerHTML = '<p class="placeholder">In diesem Unterthema hast du schon alle Karten begonnen. Wiederhole die fälligen Karten.</p>'; return; }
        F.cardSession(sess, neu, {}); sess.scrollIntoView({ behavior: "smooth" });
      });
    });
  }

  // ------------------------------------------------------------------ 7. Abi-Simulation
  function simulation(main) {
    var sim = store("sim");
    var k = kurs(), dauer = (k === "LK" ? 300 : 255) * 60000;
    if (!sim || !sim.ids) {
      var nurErlass = store("simErlass") !== false;
      main.innerHTML = '<div class="tools-controls">' + kursSwitch() + '<label class="chk"><input type="checkbox" id="sim-erl"' + (nurErlass ? " checked" : "") + "> nur Erlass-Schwerpunkte 2027 (empfohlen)</label></div>" +
        '<div class="sim-info"><p>So läuft die Simulation ab – wie im Landesabitur:</p><ol><li>Du bekommst <b>drei Aufgabenvorschläge</b> aus verschiedenen Kurshalbjahren.</li><li>Du wählst <b>einen</b> davon aus. Die Auswahlzeit gehört zur Bearbeitungszeit.</li><li>Bearbeitungszeit: <b>' + (k === "LK" ? "300" : "255") + " Minuten</b> (" + (k === "LK" ? "Leistungskurs" : "Grundkurs") + "). Der Timer läuft im Browser weiter, auch wenn du die Seite neu lädst.</li><li>Zum Schluss lädst du die <b>Korrekturdatei für den ganzen Vorschlag</b> herunter und lässt dir von einer KI eine Rückmeldung geben.</li></ol>" +
        '<p class="muted small">Erlaubte Hilfsmittel im Abitur: Rechtschreibwörterbuch, Grundgesetz und UN-Charta (unkommentiert), Operatorenliste.</p></div>' +
        '<div class="tools-actions"><button class="btn btn-primary" id="sim-go">Prüfung starten (Timer läuft ab jetzt)</button></div>';
      bindKurs(main, function () { simulation(main); });
      $("#sim-erl", main).addEventListener("change", function (e) { store("simErlass", e.target.checked); });
      $("#sim-go", main).addEventListener("click", function () {
        var pool = VS.filter(function (v) { return v.kurse.indexOf(k) >= 0 && (!$("#sim-erl", main).checked || v.erlass); });
        var byTab = {};
        pool.forEach(function (v) { (byTab[v.tab] = byTab[v.tab] || []).push(v); });
        var tabs = F.shuffle(Object.keys(byTab)), pick = [];
        tabs.forEach(function (t) { if (pick.length < 3) pick.push(F.shuffle(byTab[t])[0]); });
        var rest = F.shuffle(pool.filter(function (v) { return pick.indexOf(v) < 0 && !pick.some(function (p) { return p.topic === v.topic; }); }));
        while (pick.length < 3 && rest.length) pick.push(rest.shift());
        if (pick.length < 3) { alert("Für diese Auswahl gibt es noch nicht genug Vorschläge. Entferne den Haken bei „nur Erlass-Schwerpunkte“."); return; }
        store("sim", { kurs: k, ids: pick.map(function (p) { return p.id; }), start: Date.now(), dauer: dauer, chosen: null });
        simulation(main);
      });
      return;
    }
    var vs = sim.ids.map(function (id) { return VS.filter(function (v) { return v.id === id; })[0]; }).filter(Boolean);
    var timer = '<div class="sim-timer" id="sim-timer"><span id="sim-rest">--:--:--</span><span class="muted small">verbleibend</span><button class="btn btn-small" id="sim-end">Simulation beenden</button></div>';
    if (!sim.chosen) {
      main.innerHTML = timer + '<p class="muted">Lies alle drei Vorschläge und entscheide dich für einen.</p><div class="sim-choices">' + vs.map(function (v, i) {
        return '<article class="sim-card"><h3>Vorschlag ' + "ABC"[i] + "</h3><p class=\"muted small\">" + esc(v.nr + " " + v.themenTitel) + "</p><ol>" + v.aufgaben.map(function (a) { return "<li>" + a.text + ' <b class="nowrap">(' + a.be + " BE)</b></li>"; }).join("") + '</ol><button class="btn btn-primary" data-pick="' + v.id + '">Vorschlag ' + "ABC"[i] + " bearbeiten</button></article>";
      }).join("") + "</div>";
      $all("[data-pick]", main).forEach(function (b) { b.addEventListener("click", function () { sim.chosen = b.getAttribute("data-pick"); store("sim", sim); simulation(main); window.scrollTo(0, 0); }); });
    } else {
      var v = vs.filter(function (x) { return x.id === sim.chosen; })[0];
      main.innerHTML = timer + '<p class="muted">Bearbeite den Vorschlag in einem Schreibprogramm oder auf Papier. Material und Operatoren findest du unten.</p><div id="sim-doc"><p class="muted">Lade Material …</p></div>';
      F.loadTopic(F.meta[v.topic]).then(function (tp) {
        var mats = (tp.materialien || []).filter(function (m) { return v.material.indexOf(m.id) >= 0; });
        var ops = [];
        v.aufgaben.forEach(function (a) { if (ops.indexOf(a.operator) < 0) ops.push(a.operator); });
        $("#sim-doc", main).innerHTML = '<article class="sim-paper"><h2>' + esc(v.titel) + '</h2><p class="muted small">Politik und Wirtschaft · ' + (sim.kurs === "LK" ? "Leistungskurs" : "Grundkurs") + " · Schwerpunkt " + esc(v.nr + " " + v.themenTitel) + "</p><h3>Aufgaben</h3><ol class=\"sim-tasks\">" +
          v.aufgaben.map(function (a) { return "<li><div>" + a.text + '</div><b class="nowrap">(' + a.be + " BE)</b></li>"; }).join("") + "</ol>" +
          '<div class="op-box"><h4>Operatoren (Definitionen des Landes Hessen)</h4><dl>' + ops.map(function (o) { return "<dt>" + esc(o) + "</dt><dd>" + esc(F.site().operatoren[o].def) + "</dd>"; }).join("") + "</dl></div>" +
          '<div class="mat-doc">' + mats.map(F.matHTML).join("") + "</div>" +
          '<div class="tools-actions"><a class="btn btn-green" href="' + v.pdf + '" download>Korrekturdatei für den ganzen Vorschlag herunterladen</a></div>' +
          '<p class="muted small">Lade die Korrekturdatei zusammen mit deiner Lösung in einem KI-System deines Vertrauens hoch und bitte um eine Rückmeldung auf Grundlage der Hintergrunddaten. Keine persönlichen Daten hochladen.</p></article>';
      });
    }
    $("#sim-end", main).addEventListener("click", function () { if (confirm("Simulation beenden? Die Zeitmessung wird zurückgesetzt.")) { F.unstore("sim"); simulation(main); } });
    var restEl = $("#sim-rest", main), tEl = $("#sim-timer", main);
    function tick() {
      if (!document.body.contains(restEl)) { clearInterval(iv); return; }
      var rest = sim.start + sim.dauer - Date.now();
      if (rest <= 0) { restEl.textContent = "Zeit abgelaufen"; tEl.classList.add("over"); clearInterval(iv); return; }
      var h = Math.floor(rest / 3600000), m = Math.floor(rest % 3600000 / 60000), s = Math.floor(rest % 60000 / 1000);
      restEl.textContent = h + ":" + ("0" + m).slice(-2) + ":" + ("0" + s).slice(-2);
      tEl.classList.toggle("warn", rest < 30 * 60000);
    }
    var iv = setInterval(tick, 1000); tick();
  }

  // ------------------------------------------------------------------ 8. Formulierungs-Baukasten
  var TEXTSORTEN = [["Kommentar", "dem"], ["Leitartikel", "dem"], ["Bericht", "dem"], ["Gastbeitrag", "dem"], ["Essay", "dem"], ["Fachtext", "dem"], ["Zeitungsartikel", "dem"],
    ["Interview", "dem"], ["Rede", "der"], ["Karikatur", "der"], ["Statistik", "der"], ["Tabelle", "der"], ["Grafik", "der"]];
  function baukasten(main) {
    var v = store("baukasten") || {};
    function field(id, label, ph) { return '<label class="bk-f"><span>' + label + '</span><input id="bk-' + id + '" value="' + esc(v[id] || "") + '" placeholder="' + esc(ph) + '"></label>'; }
    main.innerHTML = '<section class="bk"><h2>Einleitungssatz-Generator</h2><div class="bk-grid">' +
      '<label class="bk-f"><span>Materialart</span><select id="bk-sorte">' + TEXTSORTEN.map(function (t) { return "<option" + (v.sorte === t[0] ? " selected" : "") + ">" + t[0] + "</option>"; }).join("") + "</select></label>" +
      '<label class="bk-f"><span>Autor/in</span><select id="bk-gen"><option value="m"' + (v.gen === "m" ? " selected" : "") + '>Autor (er)</option><option value="w"' + (v.gen === "w" ? " selected" : "") + '>Autorin (sie)</option><option value="p"' + (v.gen === "p" ? " selected" : "") + ">mehrere (sie)</option></select></label>" +
      field("autor", "Name", "z. B. Andrea Böhm") + field("titel", "Titel", "z. B. Alle wollen hier weg") + field("quelle", "Quelle", "z. B. Die Zeit (Online)") + field("datum", "Datum", "z. B. 30.08.2024") +
      field("thema", "Thema (… mit / zu …)", "z. B. den Folgen des Gaza-Kriegs für den Libanon") + field("inter", "nur Interview: Interviewer/in", "z. B. Evelin Ruhnow") +
      '</div><div id="bk-out" class="bk-out"></div></section>' +
      '<section class="bk"><h2>Satzbausteine</h2><div class="tools-controls"><label>Operator <select id="bk-op"><option value="">alle</option>' +
      uniq(LT.bausteine.reduce(function (a, b) { return a.concat(b.ops); }, [])).map(function (o) { return "<option>" + esc(o) + "</option>"; }).join("") + '</select></label><span class="muted small">Klick auf einen Baustein kopiert ihn.</span></div><div id="bk-bs"></div></section>';
    function out() {
      var d = {}; ["sorte", "gen", "autor", "titel", "quelle", "datum", "thema", "inter"].forEach(function (k) { d[k] = $("#bk-" + k, main).value.trim(); });
      store("baukasten", d);
      var art = (TEXTSORTEN.filter(function (t) { return t[0] === d.sorte; })[0] || ["", "dem"])[1];
      var er = { m: "der Autor", w: "die Autorin", p: "die Autorinnen und Autoren" }[d.gen || "m"], pr = { m: "er", w: "sie", p: "sie" }[d.gen || "m"];
      var setzt = d.gen === "p" ? "setzen" : "setzt";
      var A = d.autor || "[Autor/in]", T = "„" + (d.titel || "[Titel]") + "“", Q = d.quelle || "[Quelle]", D = d.datum || "[Datum]", TH = d.thema || "[Thema]";
      var s = [];
      if (d.sorte === "Interview") {
        s.push("In dem Interview " + T + ", geführt von " + (d.inter || "[Interviewer/in]") + " mit " + A + " und veröffentlicht am " + D + " in " + Q + ", äußert sich " + A + " zu " + TH + ".");
        s.push("Das Interview " + T + " (" + Q + ", " + D + ") gibt die Sicht von " + A + " auf " + TH + " wieder.");
      } else if (d.sorte === "Rede") {
        s.push("In der Rede " + T + ", gehalten von " + A + " am " + D + " (" + Q + "), thematisiert " + pr + " " + TH + ".");
        s.push("Die vorliegende Rede " + T + " von " + A + " aus dem Jahr " + (D.match(/\d{4}/) || ["[Jahr]"])[0] + " befasst sich mit " + TH + ".");
      } else if (["Karikatur"].indexOf(d.sorte) >= 0) {
        s.push("Die Karikatur " + T + " von " + A + ", erschienen am " + D + " in " + Q + ", thematisiert " + TH + ".");
        s.push("Die vorliegende Karikatur von " + A + " (" + Q + ", " + D + ") setzt sich kritisch mit " + TH + " auseinander.");
      } else if (["Statistik", "Tabelle", "Grafik"].indexOf(d.sorte) >= 0) {
        s.push("Die " + d.sorte + " " + T + " von " + (d.autor || "[Herausgeber]") + " (" + D + ") stellt " + TH + " dar.");
        s.push("Die vorliegende " + d.sorte + " " + T + " aus " + Q + " (Stand: " + D + ") informiert über " + TH + ".");
      } else {
        s.push("In " + art + " " + d.sorte + " " + T + " von " + A + ", erschienen am " + D + " in " + Q + ", " + setzt + " sich " + er + " mit " + TH + " auseinander.");
        s.push((art === "der" ? "Die" : "Der") + " vorliegende " + d.sorte + " " + T + " (" + Q + ", " + D + ") von " + A + " thematisiert " + TH + ".");
      }
      $("#bk-out", main).innerHTML = s.map(function (x, i) { return '<div class="bk-sent"><p>' + esc(x) + '</p><button class="btn btn-small" data-copy="' + i + '">Kopieren</button></div>'; }).join("") +
        '<p class="muted small">Tipp: Thema so formulieren, dass es zum Satz passt (z. B. „mit den Folgen …“ oder „zu der Frage, ob …“).</p>';
      $all("[data-copy]", main).forEach(function (b) { b.addEventListener("click", function () { copy(s[+b.getAttribute("data-copy")], b); }); });
    }
    $all(".bk-grid input, .bk-grid select", main).forEach(function (x) { x.addEventListener("input", out); x.addEventListener("change", out); });
    out();
    function bs() {
      var op = $("#bk-op", main).value;
      $("#bk-bs", main).innerHTML = LT.bausteine.filter(function (b) { return !op || b.ops.indexOf(op) >= 0; }).map(function (b) {
        return '<div class="bs-group"><h3>' + esc(b.titel) + '</h3><div class="bs-chips">' + b.saetze.map(function (s) { return '<button class="bs-chip">' + esc(s) + "</button>"; }).join("") + "</div></div>";
      }).join("");
      $all(".bs-chip", main).forEach(function (c) { c.addEventListener("click", function () { copy(c.textContent, null); c.classList.add("copied"); setTimeout(function () { c.classList.remove("copied"); }, 1200); }); });
    }
    $("#bk-op", main).addEventListener("change", bs);
    bs();
  }
  function uniq(a) { return a.filter(function (x, i) { return a.indexOf(x) === i; }); }

  // ------------------------------------------------------------------ 9. Schwach vs. stark
  function beispiele(main, sel) {
    var ops = LT.beispiele.map(function (b) { return b.op; });
    var cur = sel || ops[0], b = LT.beispiele.filter(function (x) { return x.op === cur; })[0];
    main.innerHTML = '<div class="tools-controls"><div class="seg seg-wrap" role="group" aria-label="Operator">' + ops.map(function (o) { return '<button data-op="' + esc(o) + '" aria-pressed="' + (o === cur) + '">' + esc(o) + "</button>"; }).join("") + "</div></div>" +
      '<div class="op-box"><b>' + esc(cur) + ":</b> " + esc(F.site().operatoren[cur].def) + '</div><div class="q-task"><b>Aufgabe:</b> ' + esc(b.aufgabe) + "</div>" +
      '<div class="ex-pair"><div class="ex ex-weak"><h3>Schwache Antwort</h3><p>' + esc(b.schwach) + '</p></div><div class="ex ex-strong" id="ex-strong" hidden><h3>Starke Antwort</h3><p>' + esc(b.stark) + "</p></div></div>" +
      '<div class="ex-think" id="ex-think"><p><b>Erst selbst überlegen:</b> Was fehlt der schwachen Antwort? Notiere dir zwei Punkte – dann vergleiche.</p><button class="btn btn-primary" id="ex-show">Starke Antwort und Merkmale zeigen</button></div>' +
      '<div class="ex-merk" id="ex-merk" hidden><h3>Daran erkennst du eine starke Antwort</h3><ul>' + b.merkmale.map(function (m) { return "<li>" + esc(m) + "</li>"; }).join("") + "</ul></div>";
    $all("[data-op]", main).forEach(function (x) { x.addEventListener("click", function () { beispiele(main, x.getAttribute("data-op")); }); });
    $("#ex-show", main).addEventListener("click", function () { $("#ex-strong", main).hidden = false; $("#ex-merk", main).hidden = false; $("#ex-think", main).hidden = true; });
  }

  // ------------------------------------------------------------------ 10. Begriffsnetz
  var NET = null;
  function buildNet(all) {
    var nodes = {}, list = [];
    all.forEach(function (x) {
      x.topic.begriffe.filter(termOK).forEach(function (b) {
        var key = F.norm(b.b);
        if (!nodes[key]) { nodes[key] = { key: key, name: b.b, kurz: b.kurz, lang: b.lang, topics: [], edges: {} }; list.push(nodes[key]); }
        if (nodes[key].topics.indexOf(x.meta) < 0) nodes[key].topics.push(x.meta);
      });
    });
    function low(s) { return " " + stripHTML(s).toLowerCase().replace(/[^a-zäöüß0-9 -]/g, " ") + " "; }
    list.forEach(function (n) { n.txt = low(n.kurz + " " + n.lang); n.pat = n.name.toLowerCase().replace(/\s*\(.*\)\s*/g, "").trim(); });
    list.forEach(function (a) {
      list.forEach(function (b) {
        if (a === b || b.pat.length < 4) return;
        var i = a.txt.indexOf(b.pat);
        if (i > 0 && !/[a-zäöüß]/.test(a.txt.charAt(i - 1))) { a.edges[b.key] = 1; b.edges[a.key] = 1; }
      });
    });
    return { nodes: nodes, list: list };
  }
  var TABCOL = { grundlagen: "#6b7280", q1: "#22355e", q2: "#1e7d45", q3: "#b5302a", q4: "#b07d00" };
  function begriffsnetz(main, start) {
    main.innerHTML = '<p class="muted">Baue das Begriffsnetz auf …</p>';
    allTopics().then(function (all) {
      if (!NET || NET.kurs !== kurs()) { NET = buildNet(all); NET.kurs = kurs(); }
      var cand = NET.list.filter(function (n) { return Object.keys(n.edges).length >= 4; });
      var center = (start && NET.nodes[start]) || NET.nodes[F.norm("Inflation")] || cand[0];
      draw(center);
    });
    function draw(c) {
      var nb = Object.keys(c.edges).map(function (k) { return NET.nodes[k]; });
      nb.sort(function (a, b) { var ca = a.topics[0].tab !== c.topics[0].tab, cb = b.topics[0].tab !== c.topics[0].tab; return (cb - ca) || (Object.keys(b.edges).length - Object.keys(a.edges).length); });
      var shown = nb.slice(0, 14), W = 760, H = 520, cx = W / 2, cy = H / 2, R = 200;
      var svg = '<svg viewBox="0 0 ' + W + " " + H + '" class="net-svg" role="img" aria-label="Begriffsnetz um ' + esc(c.name) + '"><rect width="' + W + '" height="' + H + '" fill="#fff"/>';
      shown.forEach(function (n, i) { var a = 2 * Math.PI * i / shown.length - Math.PI / 2; n._x = cx + R * Math.cos(a) * 1.35; n._y = cy + R * Math.sin(a) * 0.95; svg += '<line x1="' + cx + '" y1="' + cy + '" x2="' + n._x + '" y2="' + n._y + '" stroke="#c9d1e0" stroke-width="2"/>'; });
      shown.forEach(function (n) {
        var col = TABCOL[n.topics[0].tab] || "#22355e", label = n.name.length > 26 ? n.name.slice(0, 25) + "…" : n.name, w = Math.max(60, label.length * 7.4 + 18);
        svg += '<g class="net-node" data-n="' + esc(n.key) + '" tabindex="0" role="button" aria-label="' + esc(n.name) + '"><rect x="' + (n._x - w / 2) + '" y="' + (n._y - 15) + '" width="' + w + '" height="30" rx="15" fill="#fff" stroke="' + col + '" stroke-width="2"/><text x="' + n._x + '" y="' + (n._y + 5) + '" text-anchor="middle" font-size="13" fill="' + col + '" font-family="system-ui, Arial, sans-serif">' + esc(label) + "</text></g>";
      });
      var cw = Math.max(120, c.name.length * 9 + 30), ccol = TABCOL[c.topics[0].tab] || "#14213d";
      svg += '<rect x="' + (cx - cw / 2) + '" y="' + (cy - 22) + '" width="' + cw + '" height="44" rx="22" fill="' + ccol + '"/><text x="' + cx + '" y="' + (cy + 6) + '" text-anchor="middle" font-size="16" font-weight="700" fill="#fff" font-family="system-ui, Arial, sans-serif">' + esc(c.name) + "</text></svg>";
      var legend = Object.keys(TABCOL).map(function (t) { var tb = F.site().tabs.filter(function (x) { return x.id === t; })[0]; return tb ? '<span class="lg"><i style="background:' + TABCOL[t] + '"></i>' + esc(tb.kurz) + "</span>" : ""; }).join("");
      var narrow = window.innerWidth < 640;
      var graph = narrow ? '<div class="net-chips"><div class="net-center" style="background:' + ccol + '">' + esc(c.name) + '</div><p class="muted small">Verbunden mit:</p><div class="bs-chips">' +
        nb.map(function (n) { var col = TABCOL[n.topics[0].tab] || "#22355e"; return '<button class="net-chip" data-n="' + esc(n.key) + '" style="border-color:' + col + ";color:" + col + '">' + esc(n.name) + "</button>"; }).join("") + "</div></div>" : svg;
      main.innerHTML = '<div class="tools-controls"><label>Begriff suchen <input id="net-q" list="net-list" placeholder="z. B. Multiplikatoreffekt" autocomplete="off"></label><datalist id="net-list">' + NET.list.map(function (n) { return '<option value="' + esc(n.name) + '">'; }).join("") + '</datalist><button class="btn btn-small" id="net-rnd">Zufälliger Begriff</button></div>' +
        '<div class="net-wrap"><div class="net-graph">' + graph + '<div class="net-legend">' + legend + '<span class="muted small">Farbe = Kurshalbjahr. ' + (narrow ? "Tippe" : "Klick") + ' auf einen Begriff, um weiterzuwandern.</span></div></div>' +
        '<aside class="net-info"><h2>' + esc(c.name) + '</h2><p>' + c.lang + '</p><p class="muted small">Kommt vor in: ' + c.topics.map(function (m) { return '<a href="' + topicLink(m) + '">' + esc(m.nr) + "</a>"; }).join(", ") + "</p>" +
        (nb.length > shown.length && !narrow ? '<p class="muted small">Weitere Verbindungen: ' + nb.slice(shown.length).map(function (n) { return '<button class="linklike" data-n="' + esc(n.key) + '">' + esc(n.name) + "</button>"; }).join(", ") + "</p>" : "") +
        (nb.length ? "" : '<p class="muted">Für diesen Begriff wurden noch keine Verbindungen gefunden.</p>') + "</aside></div>" +
        '<p class="muted small">Verbindungen entstehen automatisch, wenn ein Begriff in der Erklärung eines anderen vorkommt.</p>';
      $all("[data-n]", main).forEach(function (g) {
        function go() { draw(NET.nodes[g.getAttribute("data-n")]); if (narrow) main.scrollIntoView({ behavior: "smooth" }); }
        g.addEventListener("click", go); g.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); } });
      });
      $("#net-q", main).addEventListener("change", function (e) { var n = NET.nodes[F.norm(e.target.value)]; if (n) draw(n); });
      $("#net-rnd", main).addEventListener("click", function () { var cand = NET.list.filter(function (n) { return Object.keys(n.edges).length >= 3; }); draw(cand[Math.floor(Math.random() * cand.length)]); });
    }
  }

  // ------------------------------------------------------------------ 11. Lernzettel und Karteikarten drucken
  function lernzettel(main, sel, art) {
    var cur = sel || store("lzThema") || "q1-1";
    art = art || "zettel";
    var k = kurs();
    main.innerHTML = '<div class="tools-controls no-print">' + kursSwitch() + '<label>Unterthema ' + topicSelect("lz-sel", cur, function (t) { return t.content.begriffe > 0; }) + '</label><div class="seg" role="group"><button data-art="zettel" aria-pressed="' + (art === "zettel") + '">Lernzettel</button><button data-art="karten" aria-pressed="' + (art === "karten") + '">Karteikarten</button></div><button class="btn btn-primary" id="lz-print">Drucken / als PDF speichern</button></div>' +
      '<p class="muted small no-print">' + (art === "karten" ? "Karteikarten: Vorderseiten (Begriffe) und Rückseiten (Kurzdefinitionen) stehen auf getrennten Seiten. Beidseitig drucken (an der langen Kante wenden) und ausschneiden." : "Der Lernzettel enthält Kann-Liste, Fachbegriffe mit Kurzdefinition und die Merke-Kästen des Unterthemas.") + '</p><div id="print-area" class="print-area"><p class="muted">Lade …</p></div>';
    bindKurs(main, function () { lernzettel(main, cur, art); });
    $("#lz-sel", main).addEventListener("change", function (e) { store("lzThema", e.target.value); lernzettel(main, e.target.value, art); });
    $all("[data-art]", main).forEach(function (b) { b.addEventListener("click", function () { lernzettel(main, cur, b.getAttribute("data-art")); }); });
    $("#lz-print", main).addEventListener("click", function () { document.body.classList.add("print-mode"); window.print(); setTimeout(function () { document.body.classList.remove("print-mode"); }, 500); });
    var m = F.meta[cur];
    F.loadTopic(m).then(function (tp) {
      var pa = $("#print-area", main);
      if (art === "karten") {
        var cards = tp.begriffe.filter(termOK), per = 10, html = "";
        for (var p = 0; p < cards.length; p += per) {
          var page = cards.slice(p, p + per);
          html += '<div class="pc-page">' + page.map(function (c) { return '<div class="pc-card pc-front"><span class="pc-nr">' + esc(m.nr) + "</span><b>" + esc(c.b) + "</b></div>"; }).join("") + "</div>";
          var back = [];
          for (var r = 0; r < page.length; r += 2) { back.push(page[r + 1] || null, page[r]); }
          html += '<div class="pc-page">' + back.map(function (c) { return c ? '<div class="pc-card pc-back"><b>' + esc(c.b) + "</b><span>" + esc(stripHTML(c.kurz)) + "</span></div>" : '<div class="pc-card pc-empty"></div>'; }).join("") + "</div>";
        }
        pa.innerHTML = html;
        return;
      }
      var kl = (LT.kann[cur] || []).filter(function (it) { return !it.lk || k === "LK"; });
      var merke = tp.inhalte.filter(function (b) { return b.art === "Merke" && (!b.lk || k === "LK"); });
      pa.innerHTML = '<div class="lz"><h2>' + esc(m.nr + " " + m.titel) + '</h2><p class="muted small">Feibitur-Lernzettel · ' + (k === "LK" ? "Leistungskurs" : "Grundkurs") + " · Landesabitur 2027" + (m.erlass ? " · Erlass-Schwerpunkt" : "") + "</p>" +
        (kl.length ? "<h3>Das solltest du können</h3><ul class=\"lz-kann\">" + kl.map(function (it) { return "<li>☐ " + esc(it.t) + "</li>"; }).join("") + "</ul>" : "") +
        "<h3>Fachbegriffe</h3><table class=\"lz-terms\"><tbody>" + tp.begriffe.filter(termOK).map(function (b) { return "<tr><th>" + esc(b.b) + "</th><td>" + esc(stripHTML(b.kurz)) + "</td></tr>"; }).join("") + "</tbody></table>" +
        (merke.length ? "<h3>Merke</h3>" + merke.map(function (b) { var bb = JSON.parse(JSON.stringify(b)); return F.renderBlock(bb).replace(/<button class="speak-btn"[\s\S]*?<\/button>/, ""); }).join("") : "") + "</div>";
    });
  }

  // ------------------------------------------------------------------ 12. Vorlesen
  function vorlesen(main) {
    if (!F.speechSupported()) { main.innerHTML = '<p class="placeholder">Dein Browser unterstützt keine Sprachausgabe. Probiere einen aktuellen Browser (z. B. Safari, Chrome, Edge oder Firefox).</p>'; return; }
    var p = F.speechPrefs();
    var voices = speechSynthesis.getVoices().filter(function (v) { return /^de/i.test(v.lang); });
    var shown = voices.filter(function (v) { return p.online || v.localService; });
    main.innerHTML = '<div class="vl"><p>Feibitur nutzt die <b>Sprachausgabe deines Geräts</b>. In den Inhalten erscheint oben rechts an jedem Abschnitt ein Lautsprecher-Knopf ' + I.speaker.replace("<svg", '<svg class="inline-ico"') + ". Ein zweiter Klick stoppt das Vorlesen.</p>" +
      '<label class="chk"><input type="checkbox" id="vl-on"' + (p.on ? " checked" : "") + "> Vorlese-Knöpfe in den Inhalten anzeigen</label>" +
      '<label class="bk-f"><span>Stimme</span><select id="vl-voice">' + (shown.length ? shown.map(function (v) { return '<option value="' + esc(v.voiceURI) + '"' + (v.voiceURI === p.voice ? " selected" : "") + ">" + esc(v.name + " (" + v.lang + ")" + (v.localService ? "" : " – online")) + "</option>"; }).join("") : '<option value="">keine passende deutsche Stimme gefunden</option>') + "</select></label>" +
      '<label class="bk-f"><span>Tempo: <b id="vl-rv">' + p.rate.toFixed(1) + '×</b></span><input type="range" id="vl-rate" min="0.6" max="1.6" step="0.1" value="' + p.rate + '"></label>' +
      '<label class="chk"><input type="checkbox" id="vl-online"' + (p.online ? " checked" : "") + "> auch Online-Stimmen erlauben</label>" +
      '<p class="muted small">Standardmäßig nutzt Feibitur nur Stimmen, die direkt auf deinem Gerät laufen. Online-Stimmen (z. B. in manchen Browsern von Google oder Microsoft) übertragen den vorgelesenen Text an den Hersteller des Browsers. Es handelt sich dabei nur um Lerntexte, nicht um persönliche Daten – entscheide trotzdem selbst. Fehlen deutsche Stimmen, kannst du sie in den Systemeinstellungen deines Geräts installieren (Sprache/Sprachausgabe).</p>' +
      '<div class="tools-actions"><button class="btn btn-primary" id="vl-test">Probe hören</button><button class="btn" id="vl-stop">Stopp</button></div></div>';
    function save(ch) { var q = store("vorlesen") || {}; Object.keys(ch).forEach(function (x) { q[x] = ch[x]; }); store("vorlesen", q); }
    $("#vl-on", main).addEventListener("change", function (e) { save({ on: e.target.checked }); });
    $("#vl-voice", main).addEventListener("change", function (e) { save({ voice: e.target.value }); });
    $("#vl-rate", main).addEventListener("input", function (e) { save({ rate: parseFloat(e.target.value) }); $("#vl-rv", main).textContent = parseFloat(e.target.value).toFixed(1) + "×"; });
    $("#vl-online", main).addEventListener("change", function (e) { save({ online: e.target.checked }); vorlesen(main); });
    $("#vl-test", main).addEventListener("click", function () { F.speak("Hallo! So klingt die Sprachausgabe. Die Würde des Menschen ist unantastbar."); });
    $("#vl-stop", main).addEventListener("click", function () { speechSynthesis.cancel(); });
    if (!voices.length && !vorlesen._waited) { vorlesen._waited = true; speechSynthesis.onvoiceschanged = function () { if (document.body.contains(main)) vorlesen(main); }; }
  }

  // ------------------------------------------------------------------ Router
  var FN = { lernplan: lernplan, fortschritt: fortschritt, kannlisten: kannlisten, operatoren: operatoren, schnelltest: schnelltest, wiederholung: wiederholung,
    simulation: simulation, baukasten: baukasten, beispiele: beispiele, begriffsnetz: begriffsnetz, lernzettel: lernzettel, vorlesen: vorlesen };
  function render(parts) {
    var slug = parts[0];
    var t = TOOLS.filter(function (x) { return x.slug === slug; })[0];
    if (!t) return data().then(overview, overview);
    var main = shell(t.t, t.d, '<p class="muted">Lade …</p>', slug);
    data().then(function () { FN[slug](main); }).catch(function () { main.innerHTML = '<p class="placeholder">Die Daten für die Lerntools konnten nicht geladen werden. Bitte lade die Seite neu.</p>'; });
  }
  window.FeibiturTools = { render: render };
})();
