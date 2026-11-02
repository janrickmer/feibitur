/* Feibitur – App-Logik (ohne externe Bibliotheken, ohne Tracking) */
(function () {
  "use strict";

  // SHA-256 von "Feindt" – reine Zugangsschranke, kein echter Schutz (statische Seite).
  var PW_HASH = "4e6d54b9d8cea7fb7b4c7c4d188c7d5ed24163ea305d4ed63bc2ceec55a01125";
  var LS = "feibitur.";
  var CFG = window.FEIBITUR_CONFIG || {};
  var CHAT_ENDPOINT = (CFG.chatEndpoint || "").trim();

  var app = document.getElementById("app");
  var gate = document.getElementById("gate");
  var SITE = null;
  var TOPICS = {};          // id -> topic json
  var TOPIC_META = {};      // id -> meta (aus site.json)
  var GLOSSAR = [];         // {b, kurz, topic}
  var current = { card: null, topic: null };
  var chatHistory = {};     // topicId -> [{role, content}] (nur im Arbeitsspeicher)

  // ---------------------------------------------------------------- Hilfen
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function store(key, val) { try { if (val === undefined) return JSON.parse(localStorage.getItem(LS + key)); localStorage.setItem(LS + key, JSON.stringify(val)); } catch (e) { return null; } }
  function unstore(key) { try { localStorage.removeItem(LS + key); } catch (e) {} }
  function sess(key, val) { try { if (val === undefined) return sessionStorage.getItem(LS + key); sessionStorage.setItem(LS + key, val); } catch (e) { return null; } }
  function norm(s) { return String(s).toLowerCase().replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss").replace(/[^a-z0-9]/g, ""); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function fetchJSON(url) { return fetch(url, { cache: "no-cache" }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }

  var ICON = {
    bubble: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.4A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14h4"/></svg>',
    book: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 5.5C4.5 4 8 4 12 6c4-2 7.5-2 10-.5V19c-2.5-1.5-6-1.5-10 .5-4-2-7.5-2-10-.5z"/><path d="M12 6v13.5"/></svg>',
    pencil: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L8 18l-4 1 1-4z"/><path d="M14.5 5.5l3 3"/></svg>',
    chev: '<svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    columns: '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M8 26 32 10l24 16z"/><path d="M12 26v24M22 26v24M32 26v24M42 26v24M52 26v24"/><path d="M6 54h52"/></svg>',
    cross: '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M32 8v48M18 22h28"/></svg>',
    dome: '<svg viewBox="0 0 200 120" fill="none" stroke="#fff" stroke-width="3" aria-hidden="true"><path d="M30 110h140M40 110V70h120v40M55 70V50h90v20"/><path d="M60 50a40 40 0 0 1 80 0"/><path d="M80 50a20 40 0 0 1 40 0M100 10v40M70 22c20 10 40 10 60 0"/></svg>'
  };

  // ---------------------------------------------------------------- Passwort
  function sha256(text) {
    var data = new TextEncoder().encode(text);
    return crypto.subtle.digest("SHA-256", data).then(function (buf) {
      return Array.prototype.map.call(new Uint8Array(buf), function (b) { return ("0" + b.toString(16)).slice(-2); }).join("");
    });
  }
  function initGate() {
    if (sess("ok") === "1") { gate.hidden = true; app.hidden = false; start(); return; }
    gate.hidden = false; app.hidden = true;
    var input = $("#gate-pw"); input.focus();
    $("#gate-form").addEventListener("submit", function (e) {
      e.preventDefault();
      sha256(input.value.trim()).then(function (h) {
        if (h === PW_HASH) { sess("ok", "1"); gate.hidden = true; app.hidden = false; start(); }
        else { $("#gate-error").hidden = false; input.select(); }
      });
    });
  }

  // ---------------------------------------------------------------- Router
  function route() {
    var h = (location.hash || "#/").replace(/^#\/?/, "").split("/").filter(Boolean);
    if (h[0] === "powi") return renderPowi(h[1] || "grundlagen", h[2] || null, h[3] || "begriffe");
    if (h[0] === "religion") return renderReligion();
    renderHome();
  }
  function go(path) { if (location.hash === "#/" + path) route(); else location.hash = "#/" + path; }

  function start() {
    window.addEventListener("hashchange", route);
    fetchJSON("data/site.json").then(function (s) {
      SITE = s;
      s.tabs.forEach(function (t) { t.themen.forEach(function (th) { th.tab = t.id; TOPIC_META[th.id] = th; }); });
      route();
    }).catch(function () { app.innerHTML = '<p class="placeholder">Die Inhalte konnten nicht geladen werden. Bitte lade die Seite neu.</p>'; });
  }

  function topbar(extra) {
    return '<header class="topbar"><a class="brand" href="#/">Feibitur</a><nav>' + (extra || "") + '</nav></header>';
  }
  function footer() {
    return '<footer class="site-foot"><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a> · Feibitur speichert deinen Lernstand nur in deinem Browser.</footer>';
  }

  // ---------------------------------------------------------------- Startseite
  function renderHome() {
    document.title = "Feibitur";
    app.innerHTML = '<div class="home"><div class="flagline"></div><header class="home-head"><div class="brand">Feibitur</div><p>Deine Vorbereitung auf das Landesabitur</p></header>' +
      '<main class="home-choices">' +
      '<button class="choice choice-powi" data-go="powi">' + ICON.columns + '<span class="choice-title">Politik und Wirtschaft</span><span class="choice-sub">Fachbegriffe, Inhalte und Übungsaufgaben für Q1–Q4</span></button>' +
      '<button class="choice choice-rel" data-go="religion">' + ICON.cross + '<span class="choice-title">ev. Religion</span><span class="choice-sub">Evangelische Religion</span></button>' +
      '</main>' + footer() + '</div>';
    $all("[data-go]", app).forEach(function (b) { b.addEventListener("click", function () { go(b.getAttribute("data-go")); }); });
    window.scrollTo(0, 0);
  }

  // ---------------------------------------------------------------- Religion
  function renderReligion() {
    document.title = "ev. Religion – Feibitur";
    app.innerHTML = topbar('<a class="btn btn-small" href="#/">Zur Startseite</a>') + '<section class="rel-hero"><h1>Evangelische Religion</h1></section>' +
      '<main class="rel-body"><div class="placeholder"><h2>Noch keine Inhalte</h2><p>Für evangelische Religion wurden bisher noch keine Inhalte eingepflegt. Schau bald wieder vorbei!</p></div></main>' + footer();
    window.scrollTo(0, 0);
  }

  // ---------------------------------------------------------------- PoWi
  function renderHinweis() {
    var h = SITE.hinweis;
    function col(list, cls, title) {
      return '<div class="abi-col ' + cls + '"><h3>' + title + '</h3>' + list.map(function (g) {
        return '<h4>' + g.tf + '</h4><ul>' + g.punkte.map(function (p) { return "<li>" + p + "</li>"; }).join("") + "</ul>";
      }).join("") + "</div>";
    }
    var open = store("hinweisZu") ? "" : " open";
    return '<div class="abi-wrap"><details class="abi" id="abi"' + open + '><summary>' + h.titel + ' ' + ICON.chev + '</summary><div class="abi-body">' +
      '<ul>' + h.allgemein.map(function (p) { return "<li>" + p + "</li>"; }).join("") + '</ul>' +
      '<div class="abi-cols">' + col(h.grundkurs, "gk", "Wichtig für den Grundkurs") + col(h.leistungskurs, "lk", "Wichtig für den Leistungskurs") + '</div>' +
      '<div class="abi-tipps"><b>Tipps:</b><ul>' + h.tipps.map(function (p) { return "<li>" + p + "</li>"; }).join("") + '</ul></div>' +
      '<p class="abi-src">Quelle: ' + h.quelle + '</p></div></details></div>';
  }

  function renderPowi(tabId, topicId, section) {
    document.title = "Politik und Wirtschaft – Feibitur";
    var tab = SITE.tabs.filter(function (t) { return t.id === tabId; })[0] || SITE.tabs[0];
    var existing = $("#powi-root");
    if (!existing) {
      app.innerHTML = topbar('<a class="btn btn-small" href="#/">Zur Startseite</a>') + '<div class="flagline"></div>' +
        '<div id="powi-root"><section class="powi-hero">' + ICON.dome.replace("<svg", '<svg class="dome"') + '<h1>Politik und Wirtschaft</h1><p>Vorbereitung auf das Landesabitur 2027 in Hessen</p></section>' +
        renderHinweis() + '<div class="tabs-wrap"><div class="tabs" role="tablist" aria-label="Kurshalbjahre"></div></div><div id="tabpanel"></div></div>' + footer();
      $("#abi").addEventListener("toggle", function (e) { store("hinweisZu", !e.target.open); });
      preloadGlossar();
    }
    var tabsEl = $(".tabs");
    tabsEl.innerHTML = SITE.tabs.map(function (t) {
      return '<button class="tab" role="tab" aria-selected="' + (t.id === tab.id) + '" data-tab="' + t.id + '"><span class="tab-long">' + esc(t.titel) + '</span><span class="tab-short">' + esc(t.kurz) + "</span></button>";
    }).join("");
    $all(".tab", tabsEl).forEach(function (b) { b.addEventListener("click", function () { go("powi/" + b.getAttribute("data-tab")); }); });

    var panel = $("#tabpanel");
    var side = '<aside class="sidebar"><h2>Unterthemen</h2>' + tab.themen.map(function (t) {
      var badges = "";
      if (t.methode) badges += '<span class="badge badge-abi">für alle Aufgaben wichtig</span>';
      else if (t.erlass) badges += '<span class="badge badge-abi">Abi 2027: Schwerpunkt</span>';
      else badges += '<span class="badge badge-noabi">kein Schwerpunkt 2027</span>';
      if (t.content) badges += '<span class="badge badge-content">Inhalte verfügbar</span>';
      return '<button class="topic-btn" data-topic="' + t.id + '" aria-expanded="' + (t.id === topicId) + '"><span class="topic-nr">' + esc(t.nr) + '</span><span class="topic-title">' + esc(t.titel) + '</span><div class="badges">' + badges + "</div></button>";
    }).join("") + "</aside>";
    panel.className = "tabpanel";
    panel.innerHTML = side + '<div class="stage" id="stage"></div>';
    $all(".topic-btn", panel).forEach(function (b) {
      b.addEventListener("click", function () {
        var id = b.getAttribute("data-topic");
        if (id === topicId) go("powi/" + tab.id); // erneuter Klick: zuklappen
        else go("powi/" + tab.id + "/" + id + "/" + (TOPIC_META[id].methode ? "inhalte" : "begriffe"));
      });
    });
    var stage = $("#stage");
    if (!topicId || !TOPIC_META[topicId]) {
      current.topic = null;
      stage.innerHTML = '<div class="stage-empty"><p><b>Wähle links ein Unterthema aus.</b></p><p>Es klappt hier auf und zeigt dir drei Bereiche: Fachbegriffe, Inhalte und Übungsaufgaben. Ein weiterer Klick auf das Unterthema klappt es wieder zu.</p></div>';
      return;
    }
    var isNew = current.topic !== topicId;
    current.topic = topicId;
    renderTopic(stage, tab, TOPIC_META[topicId], section);
    if (!isNew) { var tp = $(".topic-panel", stage); if (tp) tp.style.animation = "none"; }
    if (isNew) {
      var r = stage.getBoundingClientRect();
      if (r.top < 0 || r.top > window.innerHeight * 0.5) stage.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function renderTopic(stage, tab, meta, section) {
    var kcgo = "";
    if (meta.kcgo) {
      kcgo = '<details class="kcgo"><summary>Stichworte laut Kerncurriculum</summary><b>Grundkurs und Leistungskurs:</b><ul>' + meta.kcgo.gn.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") +
        '</ul><b>Nur Leistungskurs:</b><ul>' + meta.kcgo.en.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul></details>";
    }
    var note = meta.erlass_hinweis ? '<div class="erlass-note">' + esc(meta.erlass_hinweis) + "</div>" : "";
    var badge = meta.methode ? '<span class="badge badge-abi">Methode</span>' : (meta.erlass ? '<span class="badge badge-abi">Abi 2027: Schwerpunkt</span>' : '<span class="badge badge-noabi">kein Schwerpunkt 2027</span>');
    var secs = [["begriffe", ICON.bubble, "Fachbegriffe"], ["inhalte", ICON.book, "Inhalte"], ["aufgaben", ICON.pencil, "Übungsaufgaben"]];
    if (meta.methode) { // Grundlagen: ohne Fachbegriffe
      secs = secs.slice(1);
      if (section === "begriffe") section = "inhalte";
    }
    stage.innerHTML = '<article class="topic-panel"><header class="topic-head"><div class="row"><h2>' + esc(meta.nr) + " " + esc(meta.titel) + "</h2>" + badge + "</div>" + note + kcgo + "</header>" +
      '<div class="sections" role="tablist" style="grid-template-columns:repeat(' + secs.length + ',1fr)">' + secs.map(function (s) {
        return '<button class="sec-btn" role="tab" aria-selected="' + (s[0] === section) + '" data-sec="' + s[0] + '">' + s[1] + "<span>" + s[2] + "</span></button>";
      }).join("") + '</div><div class="sec-body" id="sec-body"><p class="muted">Lade Inhalte …</p></div></article>';
    $all(".sec-btn", stage).forEach(function (b) {
      b.addEventListener("click", function () { go("powi/" + tab.id + "/" + meta.id + "/" + b.getAttribute("data-sec")); });
    });
    var body = $("#sec-body");
    loadTopic(meta).then(function (topic) {
      if (section === "inhalte") renderInhalte(body, meta, topic);
      else if (section === "aufgaben") renderAufgaben(body, meta, topic);
      else renderBegriffe(body, meta, topic);
    });
  }

  function loadTopic(meta) {
    if (!meta.content) return Promise.resolve(null);
    if (TOPICS[meta.id]) return Promise.resolve(TOPICS[meta.id]);
    return fetchJSON("data/topics/" + meta.id + ".json").then(function (t) { TOPICS[meta.id] = t; return t; }).catch(function () { return null; });
  }

  function preloadGlossar() {
    if (GLOSSAR.length) return;
    var metas = Object.keys(TOPIC_META).map(function (k) { return TOPIC_META[k]; }).filter(function (m) { return m.content; });
    Promise.all(metas.map(loadTopic)).then(function (ts) {
      GLOSSAR = [];
      ts.forEach(function (t, i) { if (!t) return; t.begriffe.forEach(function (b) { GLOSSAR.push({ b: b.b, kurz: b.kurz, topic: metas[i].nr }); }); });
    });
  }

  function emptySection(text) { return '<div class="placeholder"><p><b>Noch keine Inhalte.</b></p><p>' + text + "</p></div>"; }

  // ---------------------------------------------------------------- Fachbegriffe
  function renderBegriffe(body, meta, topic) {
    if (!topic || !topic.begriffe.length) {
      body.innerHTML = emptySection("Die Fachbegriffe zu diesem Unterthema werden noch eingepflegt.") + glossarHTML();
      bindGlossar(body);
      return;
    }
    var key = "karten." + meta.id;
    var terms = topic.begriffe;
    function state() { return store(key) || { s: {} }; }
    var order = shuffle(terms.map(function (t) { return t.b; }));
    var queue2 = null;

    function draw() {
      var st = state();
      var s = st.s;
      var known = terms.filter(function (t) { return s[t.b] === "gut"; }).length;
      var notyet = terms.filter(function (t) { return s[t.b] === "nicht"; }).length;
      var open = terms.filter(function (t) { return !s[t.b]; }).length;
      var termName = null, phase = 1;
      var unsorted = order.filter(function (b) { return !s[b] && terms.some(function (t) { return t.b === b; }); });
      if (unsorted.length) termName = unsorted[0];
      else {
        phase = 2;
        if (!queue2) queue2 = shuffle(terms.filter(function (t) { return s[t.b] === "nicht"; }).map(function (t) { return t.b; }));
        queue2 = queue2.filter(function (b) { return s[b] === "nicht"; });
        termName = queue2[0] || null;
      }
      var top = '<div class="cards-top"><div class="progress"><span class="pill">' + terms.length + ' Begriffe</span><span class="pill">' + open + ' neu</span><span class="pill pill-good">' + known + ' klappt schon relativ gut</span><span class="pill pill-bad">' + notyet + ' klappt noch nicht so gut</span></div><button class="linklike" id="cards-reset">Lernstand zurücksetzen</button></div>';
      var html;
      if (!termName) {
        current.card = null;
        html = '<div class="cards-done"><h3>Stark! Alle ' + terms.length + ' Begriffe klappen schon relativ gut.</h3><p class="muted">Du kannst den Stapel jederzeit neu starten.</p><button class="btn btn-primary" id="cards-restart">Alle Begriffe noch einmal üben</button></div>';
      } else {
        var t = terms.filter(function (x) { return x.b === termName; })[0];
        current.card = t.b;
        html = (phase === 2 ? '<p class="muted" style="text-align:center">Wiederholung: Begriffe, die noch nicht so gut klappen (' + notyet + ' übrig)</p>' : "") +
          '<div class="flash-wrap"><button class="flash" id="flash" aria-label="Karteikarte umdrehen"><div class="face face-front"><div class="term">' + esc(t.b) + '</div><div class="hint">Antippen zum Umdrehen</div></div>' +
          '<div class="face face-back"><div class="term-small">' + esc(t.b) + '</div><div class="def">' + t.lang + '</div></div></button></div>' +
          '<div class="rate" id="rate" hidden><button class="btn btn-good" data-r="gut">Klappt schon relativ gut</button><button class="btn btn-bad" data-r="nicht">Klappt noch nicht so gut</button></div>' +
          '<p class="muted" style="text-align:center" id="rate-hint">Überlege dir zuerst selbst eine Erklärung – dann dreh die Karte um.</p>';
      }
      body.innerHTML = top + html + glossarHTML();
      bindGlossar(body);
      $("#cards-reset", body).addEventListener("click", function () {
        if (confirm("Möchtest du deinen Lernstand für dieses Unterthema wirklich zurücksetzen?")) { unstore(key); queue2 = null; order = shuffle(order); draw(); }
      });
      var restart = $("#cards-restart", body);
      if (restart) restart.addEventListener("click", function () { unstore(key); queue2 = null; order = shuffle(order); draw(); });
      var flash = $("#flash", body);
      if (flash) {
        flash.addEventListener("click", function () {
          flash.classList.toggle("flipped");
          if (flash.classList.contains("flipped")) { $("#rate", body).hidden = false; $("#rate-hint", body).hidden = true; }
        });
        $all("#rate [data-r]", body).forEach(function (b) {
          b.addEventListener("click", function () {
            var st2 = state();
            st2.s[termName] = b.getAttribute("data-r");
            store(key, st2);
            if (phase === 2 && queue2) { queue2 = queue2.filter(function (x) { return x !== termName; }); if (b.getAttribute("data-r") === "nicht") queue2.push(termName); }
            draw();
          });
        });
      }
    }
    draw();
  }

  function glossarHTML() {
    return '<section class="glossar"><h3>Glossar</h3><p class="muted">Gib einen Fachbegriff ein und erhalte die Kurzdefinition. (Der Begriff auf deiner aktuellen Karteikarte ist hier ausgeblendet.)</p>' +
      '<label class="visually-hidden" for="gl-q">Fachbegriff suchen</label><input id="gl-q" type="search" placeholder="z. B. Gewaltenteilung" autocomplete="off"><div class="glossar-results" id="gl-res" aria-live="polite"></div></section>';
  }
  function bindGlossar(root) {
    var q = $("#gl-q", root), res = $("#gl-res", root);
    if (!q) return;
    q.addEventListener("input", function () {
      var v = norm(q.value);
      if (v.length < 2) { res.innerHTML = ""; return; }
      var hidden = current.card ? norm(current.card) : null;
      var blocked = false;
      var hits = GLOSSAR.filter(function (g) {
        var n = norm(g.b);
        if (hidden && n === hidden) { if (n.indexOf(v) !== -1) blocked = true; return false; }
        return n.indexOf(v) !== -1;
      });
      hits.sort(function (a, b) { return norm(a.b).indexOf(v) - norm(b.b).indexOf(v) || a.b.length - b.b.length; });
      var seen = {};
      hits = hits.filter(function (g) { var k = norm(g.b) + "|" + g.kurz; if (seen[k]) return false; seen[k] = 1; return true; }).slice(0, 8);
      var out = hits.map(function (g) { return '<div class="gl-item"><b>' + esc(g.b) + "</b>: " + g.kurz + ' <span class="gl-src">(' + esc(g.topic) + ")</span></div>"; }).join("");
      if (blocked) out = '<div class="gl-item">Dieser Begriff liegt gerade auf deiner Karteikarte – versuche es erst selbst! 😉</div>' + out;
      if (!out) out = '<p class="muted">Kein passender Begriff gefunden.</p>';
      res.innerHTML = out;
    });
  }

  // ---------------------------------------------------------------- Inhalte
  var KIND = { "Erklärung": "k-erklaerung", "Fachtext": "k-fachtext", "Merke": "k-merke", "Beispiel": "k-beispiel", "Gesetzestext": "k-gesetz", "Grafik": "k-grafik", "Schaubild": "k-grafik" };
  function renderBlock(b) {
    var lk = b.lk ? '<span class="badge badge-lk lk-tag">nur LK</span>' : "";
    var cls = "block" + (b.art === "Fachtext" ? " fachtext" : "") + (b.art === "Merke" ? " merke" : "") + (b.art === "Gesetzestext" ? " gesetz" : "") + (b.lk ? " lk" : "");
    var kind = '<span class="block-kind ' + (KIND[b.art] || "k-erklaerung") + '">' + esc(b.art) + "</span>";
    var inner = "";
    if (b.t === "svg") inner = '<figure class="figure" style="margin:0">' + b.svg + (b.caption ? "<figcaption>" + b.caption + "</figcaption>" : "") + "</figure>";
    else if (b.t === "table") inner = '<div class="table-scroll"><table><thead><tr>' + b.kopf.map(function (k) { return "<th>" + k + "</th>"; }).join("") + "</tr></thead><tbody>" +
      b.zeilen.map(function (z) { return "<tr>" + z.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table></div>" + (b.html || "");
    else inner = b.html;
    return '<section class="' + cls + '">' + lk + kind + (b.titel ? "<h3>" + b.titel + "</h3>" : "") + inner + (b.quelle ? '<p class="src">' + b.quelle + "</p>" : "") + "</section>";
  }
  function renderInhalte(body, meta, topic) {
    var main = (!topic || !topic.inhalte.length) ? emptySection("Die Inhalte zu diesem Unterthema werden noch eingepflegt.") : topic.inhalte.map(renderBlock).join("");
    body.innerHTML = '<div class="content-grid"><div class="content-main">' + main + '</div><aside class="chat" id="chat"></aside></div>';
    renderChat($("#chat", body), meta);
  }

  // ---------------------------------------------------------------- Chatbot
  var PII = [
    { re: /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i, what: "eine E-Mail-Adresse" },
    { re: /(\+?\d[\d \/-]{7,}\d)/, what: "eine Telefonnummer" },
    { re: /\b[A-Z]{2}\d{2}(?: ?[A-Z0-9]{4}){3,}/i, what: "eine IBAN" },
    { re: /\b\S+(straße|strasse|str\.|weg|allee|platz|gasse)\s+\d+/i, what: "eine Adresse" },
    { re: /\b(ich hei(ß|ss)e|mein name ist|ich bin \d{1,2} jahre)/i, what: "Angaben zu deiner Person" }
  ];
  function renderChat(el, meta) {
    var consent = store("chatConsent") === true;
    var head = '<div class="chat-head"><b>KI-Tutor (Chatbot)</b><small>Fragen zum Thema ' + esc(meta.nr) + '</small></div>' +
      '<div class="chat-warn"><b>Wichtig:</b> Gib keine personenbezogenen Daten ein – also keinen Namen, keine Adresse, keine Schule, keine Kontaktdaten und nichts über Gesundheit, Religion oder Familie.</div>';
    if (!CHAT_ENDPOINT) {
      el.innerHTML = head + '<div class="chat-consent"><p><b>Der Chatbot wird gerade eingerichtet</b> und ist noch nicht verfügbar.</p><p class="muted">Bis dahin: Nutze die Erklärtexte links' + (meta.methode ? "" : " und das Glossar unter „Fachbegriffe“") + '.</p></div>';
      return;
    }
    if (!consent) {
      el.innerHTML = head + '<div class="chat-consent"><p>Der Chatbot ist <b>ausgeschaltet</b>. Du kannst ihn freiwillig aktivieren.</p>' +
        '<p>Wenn du ihn aktivierst, werden deine Eingaben an den externen Dienst <b>Cloudflare</b> (Cloudflare Workers AI, Cloudflare, Inc., USA) übertragen und dort von einem KI-Sprachmodell verarbeitet. Dabei wird technisch bedingt auch deine IP-Adresse übermittelt. Die Daten können auf Servern außerhalb der EU (z. B. in den USA) verarbeitet werden. <b>Diese Datenverarbeitung erfolgt nicht DSGVO-konform.</b></p>' +
        '<p>Bist du unter 16 Jahre alt, aktiviere den Chatbot bitte nur mit Zustimmung deiner Eltern. KI-Antworten können falsch sein – prüfe sie immer!</p>' +
        '<label><input type="checkbox" id="chat-ok"> <span>Ich habe die Hinweise gelesen und willige ausdrücklich ein, dass meine Eingaben wie beschrieben – nicht DSGVO-konform – an Cloudflare übertragen werden. Ich kann die Einwilligung jederzeit widerrufen, indem ich den Chatbot wieder deaktiviere.</span></label>' +
        '<button class="btn btn-primary" id="chat-on" disabled>Chatbot aktivieren</button><p class="muted" style="margin-top:.6rem">Mehr dazu in der <a href="datenschutz.html#chatbot">Datenschutzerklärung</a>.</p></div>';
      var cb = $("#chat-ok", el), on = $("#chat-on", el);
      cb.addEventListener("change", function () { on.disabled = !cb.checked; });
      on.addEventListener("click", function () { store("chatConsent", true); renderChat(el, meta); });
      return;
    }
    var hist = chatHistory[meta.id] || (chatHistory[meta.id] = []);
    el.innerHTML = head + '<div class="chat-log" id="chat-log" aria-live="polite"></div>' +
      '<form class="chat-form" id="chat-form"><label class="visually-hidden" for="chat-in">Frage an den Chatbot</label><textarea id="chat-in" rows="2" placeholder="Deine Frage zum Thema …" maxlength="1200"></textarea><button class="btn btn-primary" type="submit" aria-label="Senden">➤</button></form>' +
      '<div class="chat-foot"><span>KI kann Fehler machen. Verlauf wird nicht gespeichert.</span><button class="linklike" id="chat-off">Chatbot deaktivieren</button></div>';
    var log = $("#chat-log", el);
    function add(role, text) {
      var d = document.createElement("div");
      d.className = "msg " + (role === "user" ? "msg-user" : role === "err" ? "msg-err" : "msg-bot");
      if (role === "assistant") d.innerHTML = esc(text).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/^#{1,4}\s*(.+)$/gm, "<b>$1</b>");
      else d.textContent = text;
      log.appendChild(d); log.scrollTop = log.scrollHeight; return d;
    }
    if (!hist.length) add("assistant", "Hallo! Ich bin dein KI-Tutor für „" + meta.titel + "“. Stell mir eine Frage – z. B. „Erklär mir den Unterschied zwischen … und …“ oder „Was bedeutet …?“");
    hist.forEach(function (m) { add(m.role, m.content); });
    $("#chat-off", el).addEventListener("click", function () { unstore("chatConsent"); chatHistory[meta.id] = []; renderChat(el, meta); });
    var form = $("#chat-form", el), input = $("#chat-in", el), busy = false;
    input.addEventListener("keydown", function (e) { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); form.requestSubmit ? form.requestSubmit() : form.dispatchEvent(new Event("submit")); } });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var q = input.value.trim();
      if (!q || busy) return;
      for (var i = 0; i < PII.length; i++) {
        if (PII[i].re.test(q)) { add("err", "Deine Nachricht scheint " + PII[i].what + " zu enthalten. Bitte entferne personenbezogene Daten, bevor du sie abschickst."); return; }
      }
      input.value = ""; add("user", q); hist.push({ role: "user", content: q });
      busy = true; var wait = add("assistant", "… denkt nach …");
      var payload = { thema: meta.nr + " " + meta.titel,
        stichworte: meta.kcgo ? meta.kcgo.gn.join("; ") + " | Nur Leistungskurs: " + meta.kcgo.en.join("; ") : "",
        messages: hist.slice(-10) };
      fetch(CHAT_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json" }, referrerPolicy: "no-referrer", credentials: "omit",
        body: JSON.stringify(payload) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (j) {
          var txt = (j && j.reply) || "";
          txt = String(txt).trim() || "Ich konnte leider keine Antwort erzeugen. Versuch es bitte noch einmal.";
          wait.remove(); add("assistant", txt); hist.push({ role: "assistant", content: txt });
        })
        .catch(function (err) {
          wait.remove();
          hist.pop();
          add("err", String(err.message) === "429" ? "Das kostenlose Tageskontingent des Chatbots ist aufgebraucht oder es gab zu viele Anfragen. Versuch es später (spätestens morgen) noch einmal." : "Der Chatbot ist gerade nicht erreichbar. Versuch es später noch einmal.");
        })
        .then(function () { busy = false; });
    });
  }

  // ---------------------------------------------------------------- Übungsaufgaben
  function renderAufgaben(body, meta, topic) {
    var howto = '<section class="howto"><h3>So funktioniert das Üben mit den Übungsaufgaben</h3><ol>' +
      "<li><span>Aufgabe und Material genau anschauen und dann eine Lösung verfassen (in einem Schreibprogramm oder leserlich auf GoodNotes etc.).</span></li>" +
      "<li><span>Eigene Lösung inkl. der hier zu jeder Aufgabe herunterladbaren „Korrekturdatei“ in einem KI-System des Vertrauens hochladen und die KI bitten, die Hintergrunddaten der Korrekturdatei zu nutzen, um eine Rückmeldung zu formulieren.</span></li>" +
      "<li><span>KI-Rückmeldung nutzen und reflektieren.</span></li></ol>" +
      '<p class="muted" style="margin:.7rem 0 0">Tipp für Schritt 2: Schreib z. B. „Hier sind meine Lösung und die Korrekturdatei. Bitte lies die Hintergrunddaten der Korrekturdatei und gib mir danach eine Rückmeldung.“ Lade keine Dateien mit deinem Namen hoch.</p></section>';
    if (!topic || !topic.aufgaben.length) { body.innerHTML = howto + '<div style="margin-top:1rem">' + emptySection("Übungsaufgaben zu diesem Unterthema werden noch erstellt.") + "</div>"; return; }
    body.innerHTML = howto + topic.aufgaben.map(function (a, i) {
      var ops = a.operatoren.map(function (k) { var o = SITE.operatoren[k]; return "<dt>" + esc(k) + " <span class=\"muted\">(AFB " + o.afb + ")</span></dt><dd>" + esc(o.def) + "</dd>"; }).join("");
      var mats = a.material.map(function (m) {
        var inner;
        if (m.typ === "tabelle") inner = '<div class="table-scroll block" style="padding:.5rem"><table><thead><tr>' + m.kopf.map(function (k) { return "<th>" + k + "</th>"; }).join("") + "</tr></thead><tbody>" + m.zeilen.map(function (z) { return "<tr>" + z.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table></div>";
        else inner = '<div class="mat-text">' + m.absaetze.map(function (p, n) { return '<div class="mat-p"><span class="pn">[' + (n + 1) + "]</span><div>" + p + "</div></div>"; }).join("") + "</div>";
        return "<h4>" + m.titel + "</h4>" + inner + (m.quelle ? '<p class="mat-src">' + m.quelle + "</p>" : "") + (m.hinweis ? '<p class="mat-src">' + m.hinweis + "</p>" : "");
      }).join("");
      return '<article class="task"><div class="task-head"><h3>' + esc(a.titel) + '</h3><span class="badge ' + (a.kurs.indexOf("LK") === 0 ? "badge-lk" : "badge-noabi") + '">' + esc(a.kurs) + "</span></div>" +
        '<ol class="task-list">' + a.aufgaben.map(function (t) { return "<li><b>" + t.nr + "</b><div>" + t.text + '</div><span class="be">(' + t.be + " BE)</span></li>"; }).join("") + "</ol>" +
        '<div class="task-actions"><button class="btn btn-small btn-primary" data-mat="' + i + '" aria-expanded="false">Material anzeigen</button></div>' +
        '<div class="material" id="mat-' + i + '" hidden><div class="mat-top"><div class="op-box"><h4>Was verlangen die Operatoren? (Definitionen des Landes Hessen)</h4><dl>' + ops + '</dl><p class="src">' + esc(SITE.operatorenVorbemerkung) + "<br>Quelle: " + esc(SITE.operatorenQuelle) + '</p></div>' +
        '<a class="btn btn-green" href="' + a.pdf + '" download>Korrekturdatei herunterladen</a></div><div class="mat-doc">' + mats + "</div></div></article>";
    }).join("");
    $all("[data-mat]", body).forEach(function (b) {
      b.addEventListener("click", function () {
        var m = $("#mat-" + b.getAttribute("data-mat"), body);
        m.hidden = !m.hidden;
        b.setAttribute("aria-expanded", String(!m.hidden));
        b.textContent = m.hidden ? "Material anzeigen" : "Material ausblenden";
      });
    });
  }

  ["g1", "g2", "g3"].forEach(function (id) { unstore("karten." + id); }); // alter Lernstand der früheren Grundlagen-Karteikarten
  initGate();
})();
