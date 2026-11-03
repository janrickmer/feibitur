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
    cards: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="11" height="15" rx="2" transform="rotate(-8 8.5 12.5)"/><rect x="10" y="4" width="11" height="15" rx="2" transform="rotate(8 15.5 11.5)"/></svg>',
    tools: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 0 5 5L22 13.6 13.6 22l-2.3-2.3a4 4 0 0 0-5-5L4 12.4 12.4 4z" transform="scale(.9) translate(1 1)"/><path d="M3 21l5-5"/></svg>',
    speaker: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg>',
    chev: '<svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    columns: '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M8 26 32 10l24 16z"/><path d="M12 26v24M22 26v24M32 26v24M42 26v24M52 26v24"/><path d="M6 54h52"/></svg>',
    cross: '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M32 8v48M18 22h28"/></svg>',
    arrow: '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
    download: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>',
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
    if (!SITE) return; // Daten noch nicht geladen – start() ruft route() danach auf
    var h = (location.hash || "#/").replace(/^#\/?/, "").split("/").filter(Boolean);
    if (h[0] === "powi") return renderPowi(h[1] || "grundlagen", h[2] || null, h[3] || "begriffe");
    if (h[0] === "religion") return renderReligion();
    if (h[0] === "lerntools") return go("powi/tools/" + (h[1] || ""));
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
    return '<header class="topbar"><a class="brand" href="#/" aria-label="Feibitur – zur Startseite">Feibitur</a><nav>' + (extra || "") + '</nav></header>';
  }
  // Kurswahl: "GK", "LK" oder null (noch nicht gewählt -> alles anzeigen)
  function kursWahl() { var k = store("kurs"); return k === "GK" || k === "LK" ? k : null; }
  function zeigeLK() { return kursWahl() !== "GK"; }
  function kursSwitchHTML() {
    var k = kursWahl();
    return '<div class="kurs-switch"><span>Mein Kurs:</span><div class="seg" role="group" aria-label="Kurs wählen"><button data-kurswahl="GK" aria-pressed="' + (k === "GK") + '">Grundkurs</button><button data-kurswahl="LK" aria-pressed="' + (k === "LK") + '">Leistungskurs</button></div></div>' +
      (k ? "" : '<p class="kurs-hint">Wähle deinen Kurs – dann blenden wir aus, was für dich nicht relevant ist.</p>');
  }
  function bindKursWahl(root) {
    $all("[data-kurswahl]", root).forEach(function (b) {
      b.addEventListener("click", function () {
        store("kurs", b.getAttribute("data-kurswahl"));
        var pr = $("#powi-root"); if (pr) pr.remove();
        app.innerHTML = ""; route();
      });
    });
  }
  function toolsBtn() { return '<a class="btn btn-small btn-tools" href="#/lerntools" aria-label="Lerntools">' + ICON.tools + "<span>Lerntools</span></a>"; }
  var SEC_NAME = { begriffe: "Fachbegriffe", inhalte: "Inhalte", aufgaben: "Übungsaufgaben" };
  function hjShort(t) { return t.id === "grundlagen" ? "G" : t.kurz; }
  var TOOL_TAB = { id: "tools", kurz: "Tools", titel: "Vorbereitungs-Tools", themen: [] };
  function renderToolsTab(tab, slug) {
    var T = window.FeibiturTools, tools = T ? T.tools : [], groups = [];
    current.topic = null;
    tools.forEach(function (t) { if (groups.indexOf(t.g) < 0) groups.push(t.g); });
    var valid = slug && (slug === "lernstand" || tools.some(function (t) { return t.slug === slug; }));
    var side = '<aside class="sidebar sidebar-tools"><h2>Vorbereitungs-Tools</h2>' + groups.map(function (g) {
      return '<h3 class="tool-grp">' + esc(g) + "</h3>" + tools.filter(function (t) { return t.g === g; }).map(function (t) {
        return '<button class="topic-btn" data-tool="' + t.slug + '" aria-expanded="' + (t.slug === slug) + '"><span class="topic-nr">' + esc(t.k) + '</span><span class="topic-title">' + esc(t.t) + "</span></button>";
      }).join("");
    }).join("") + "</aside>";
    var panel = $("#tabpanel");
    var wasSlug = panel.getAttribute("data-tool");
    panel.className = "tabpanel tabpanel-tools" + (valid ? " has-topic" : "");
    panel.setAttribute("data-tool", slug || "");
    panel.innerHTML = side + '<div class="stage" id="stage"><div class="tools-bar"><a class="btn btn-primary btn-ls" href="#/powi/tools/lernstand"' + (slug === "lernstand" ? ' aria-current="page"' : "") + ">" + ICON.download + "<span>Aktuellen Leistungsstand laden / speichern</span></a></div><div id=\"tool-host\"></div></div>";
    $all(".topic-btn", panel).forEach(function (b) {
      b.addEventListener("click", function () { var id = b.getAttribute("data-tool"); go("powi/tools/" + (id === slug ? "" : id)); });
    });
    if (T) T.renderInto(valid ? slug : "");
    var tp = $(".tool-panel", panel);
    if (tp && valid && wasSlug !== slug) {
      tp.classList.add("paste");
      var r = $("#stage").getBoundingClientRect();
      if (r.top < 0 || r.top > window.innerHeight * 0.5) $("#stage").scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
  function hjName(t) { return String(t.titel).replace(/^Q\d:\s*/, ""); }
  function footer() {
    return '<footer class="site-foot"><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a> · Feibitur speichert deinen Lernstand nur in deinem Browser.</footer>';
  }

  // ---------------------------------------------------------------- Startseite
  function renderHome() {
    document.title = "Feibitur";
    var z = store("zuletzt"), zm = z && TOPIC_META[z.topic];
    var weiter = zm ? '<a class="weiter" href="#/powi/' + z.tab + "/" + z.topic + "/" + z.sec + '"><span>Weiter, wo du aufgehört hast:</span> <b>' + esc(zm.nr) + " · " + esc(SEC_NAME[z.sec] || "") + "</b>" + ICON.arrow + "</a>" : "";
    app.innerHTML = '<div class="home"><header class="home-head"><h1 class="wordmark">Feibitur</h1><p>Deine Vorbereitung auf das Landesabitur</p></header>' +
      '<main class="home-choices">' +
      '<button class="choice choice-powi" data-go="powi"><span class="choice-title">Politik und Wirtschaft</span><span class="choice-sub">Fachbegriffe, Inhalte, Übungsaufgaben und Vorbereitungs-Tools für Q1–Q4</span>' +
      '<span class="hj-strip" aria-hidden="true"><i data-hj="tools">Tools</i><i data-hj="grundlagen">G</i><i data-hj="q1">Q1</i><i data-hj="q2">Q2</i><i data-hj="q3">Q3</i><i data-hj="q4">Q4</i></span></button>' +
      '<button class="choice choice-rel" data-go="religion"><span class="choice-title">ev. Religion</span><span class="choice-sub">Noch keine Inhalte</span></button>' +
      weiter + '</main>' + footer() + '</div>';
    $all("[data-go]", app).forEach(function (b) { b.addEventListener("click", function () { go(b.getAttribute("data-go")); }); });
    window.scrollTo(0, 0);
  }

  // ---------------------------------------------------------------- Religion
  function renderReligion() {
    document.title = "ev. Religion – Feibitur";
    app.innerHTML = topbar('<a class="btn btn-small" href="#/">Startseite</a>') + '<section class="rel-hero"><h1>Evangelische Religion</h1></section>' +
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
    // Beim ersten Besuch offen, danach geschlossen – außer man hat ihn zuletzt selbst geöffnet gelassen
    var open = !store("hinweisGesehen") || store("hinweisZu") === false ? " open" : "";
    store("hinweisGesehen", true);
    return '<div class="abi-wrap"><details class="abi" id="abi"' + open + '><summary>' + h.titel + ' ' + ICON.chev + '</summary><div class="abi-body">' +
      '<ul>' + h.allgemein.map(function (p) { return "<li>" + p + "</li>"; }).join("") + '</ul>' +
      (kursWahl() === "GK" ? '<div class="abi-cols abi-one">' + col(h.grundkurs, "gk", "Wichtig für den Grundkurs") + "</div>" :
        '<div class="abi-cols">' + col(h.grundkurs, "gk", "Wichtig für den Grundkurs") + col(h.leistungskurs, "lk", "Wichtig für den Leistungskurs") + '</div>') +
      '<div class="abi-tipps"><b>Tipps:</b><ul>' + h.tipps.map(function (p) { return "<li>" + p + "</li>"; }).join("") + '</ul></div>' +
      '<p class="abi-src">Quelle: ' + h.quelle + '</p></div></details></div>';
  }

  function renderPowi(tabId, topicId, section) {
    document.title = "Politik und Wirtschaft – Feibitur";
    var TABS = [TOOL_TAB].concat(SITE.tabs);
    var tab = TABS.filter(function (t) { return t.id === tabId; })[0] || SITE.tabs[0];
    var existing = $("#powi-root");
    if (!existing) {
      app.innerHTML = topbar('<a class="btn btn-small" href="#/">Startseite</a>') +
        '<div id="powi-root"><section class="powi-hero"><div class="powi-hero-in"><h1>Politik und Wirtschaft</h1><p>Vorbereitung auf das Landesabitur 2027 in Hessen</p></div>' +
        kursSwitchHTML() + "</section>" +
        renderHinweis() + '<div class="tabs-wrap"><div class="tabs" role="tablist" aria-label="Kurshalbjahre"></div></div><div id="tabpanel"></div></div>' + footer();
      $("#abi").addEventListener("toggle", function (e) { store("hinweisZu", !e.target.open); });
      bindKursWahl(app);
      preloadGlossar();
    }
    $("#powi-root").setAttribute("data-hj", tab.id);
    var tabsEl = $(".tabs");
    tabsEl.innerHTML = TABS.map(function (t) {
      return '<button class="tab" role="tab" data-hj="' + t.id + '" aria-selected="' + (t.id === tab.id) + '" data-tab="' + t.id + '"><span class="tab-nr">' + esc(hjShort(t)) + '</span><span class="tab-long">' + esc(hjName(t)) + "</span></button>";
    }).join("");
    var sel = $(".tab[aria-selected=true]", tabsEl);
    if (sel && tabsEl.scrollWidth > tabsEl.clientWidth) tabsEl.scrollLeft = Math.max(0, sel.offsetLeft - 16);
    $all(".tab", tabsEl).forEach(function (b) { b.addEventListener("click", function () { go("powi/" + b.getAttribute("data-tab")); }); });
    if (tab.id === "tools") return renderToolsTab(tab, topicId);
    var valid = topicId && TOPIC_META[topicId];
    if (valid) store("zuletzt", { tab: tab.id, topic: topicId, sec: TOPIC_META[topicId].methode ? "inhalte" : section });
    var z = store("zuletzt") || {};

    var panel = $("#tabpanel");
    var side = '<aside class="sidebar"><h2>Unterthemen</h2>' + tab.themen.map(function (t) {
      var badges = "";
      if (t.methode) badges += '<span class="badge badge-abi">für alle Aufgaben wichtig</span>';
      else if (t.erlass) badges += '<span class="badge badge-abi">Abi 2027: Schwerpunkt</span>';
      else badges += '<span class="badge badge-noabi">kein Schwerpunkt 2027</span>';
      if (!t.content) badges += '<span class="badge badge-noabi">noch ohne Inhalte</span>';
      var flag = z.topic === t.id && t.id !== topicId ? '<span class="zuletzt">Zuletzt hier</span>' : "";
      return '<button class="topic-btn" data-topic="' + t.id + '" aria-expanded="' + (t.id === topicId) + '">' + flag + '<span class="topic-nr">' + esc(t.nr) + '</span><span class="topic-title">' + esc(t.titel) + '</span><span class="badges">' + badges + "</span></button>";
    }).join("") + "</aside>";
    panel.className = "tabpanel" + (valid ? " has-topic" : "");
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
      var zt = z.tab === tab.id && TOPIC_META[z.topic];
      stage.innerHTML = '<div class="stage-empty"><p class="stage-big">Wähle ein Unterthema.</p><p>Es klappt hier als Plakat auf und zeigt dir ' + (tab.id === "grundlagen" ? "die Inhalte" : "die Bereiche Fachbegriffe, Inhalte und Übungsaufgaben") + '. Ein weiterer Klick auf das Unterthema klappt es wieder zu.</p>' +
        (zt ? '<a class="btn btn-primary" href="#/powi/' + tab.id + "/" + z.topic + "/" + z.sec + '">Weiter bei ' + esc(zt.nr) + " · " + esc(SEC_NAME[z.sec] || "") + ICON.arrow + "</a>" : "") + "</div>";
      return;
    }
    var isNew = current.topic !== topicId;
    current.topic = topicId;
    renderTopic(stage, tab, TOPIC_META[topicId], section);
    if (isNew) { var tp = $(".topic-panel", stage); if (tp) tp.classList.add("paste"); }
    if (isNew) {
      var r = stage.getBoundingClientRect();
      if (r.top < 0 || r.top > window.innerHeight * 0.5) stage.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function renderTopic(stage, tab, meta, section) {
    var kcgo = "";
    if (meta.kcgo) {
      kcgo = '<details class="kcgo"><summary>Stichworte laut Kerncurriculum</summary><b>Grundkurs und Leistungskurs:</b><ul>' + meta.kcgo.gn.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") +
        "</ul>" + (zeigeLK() ? '<b>Nur Leistungskurs:</b><ul>' + meta.kcgo.en.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" : "") + "</details>";
    }
    var note = meta.erlass_hinweis ? '<div class="erlass-note">' + esc(meta.erlass_hinweis) + "</div>" : "";
    var badge = meta.methode ? '<span class="badge badge-abi">Methode</span>' : (meta.erlass ? '<span class="badge badge-abi">Abi 2027: Schwerpunkt</span>' : '<span class="badge badge-noabi">kein Schwerpunkt 2027</span>');
    var secs = [["begriffe", ICON.bubble, "Fachbegriffe"], ["inhalte", ICON.book, "Inhalte"], ["aufgaben", ICON.pencil, "Übungsaufgaben"]];
    if (meta.methode) { // Grundlagen: nur Inhalte (ohne Fachbegriffe und Übungsaufgaben)
      secs = [secs[1]];
      section = "inhalte";
    }
    stage.innerHTML = '<article class="topic-panel"><header class="topic-head"><span class="tie tie-l" aria-hidden="true"></span><span class="tie tie-r" aria-hidden="true"></span>' +
      '<div class="row"><span class="poster-nr" aria-hidden="true">' + esc(meta.nr) + "</span>" + badge + '</div><h2><span class="visually-hidden">' + esc(meta.nr) + " </span>" + esc(meta.titel) + "</h2>" + note + kcgo + "</header>" +
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
      ts.forEach(function (t, i) { if (!t) return; t.begriffe.forEach(function (b) { GLOSSAR.push({ b: b.b, kurz: b.kurz, topic: metas[i].nr, lk: !!b.lk }); }); });
    });
  }

  function emptySection(text) { return '<div class="placeholder"><p><b>Noch keine Inhalte.</b></p><p>' + text + "</p></div>"; }

  // ---------------------------------------------------------------- Fachbegriffe
  // ---------------------------------------------------------------- Lernkartei (Leitner-System, 5 Fächer)
  // Fach 1: täglich (sofort wieder), Fach 2: nach 1 Tag, Fach 3: nach 3, Fach 4: nach 7, Fach 5: nach 14 Tagen.
  var INTERVALL = [0, 0, 1, 3, 7, 14];
  function isoDate(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function today() { return isoDate(new Date()); }
  function addDays(n) { var d = new Date(); d.setDate(d.getDate() + n); return isoDate(d); }
  function leitner() { return store("leitner") || {}; }
  function saveLeitner(l) { store("leitner", l); }
  function cardKey(tid, b) { return tid + "|" + b; }
  function migrateKarten(tid) { // Lernstand aus der alten Zwei-Stapel-Version übernehmen
    var old = store("karten." + tid);
    if (!old || !old.s) return;
    var l = leitner();
    Object.keys(old.s).forEach(function (b) {
      var k = cardKey(tid, b);
      if (!l[k]) l[k] = old.s[b] === "gut" ? { f: 2, d: addDays(1) } : { f: 1, d: today() };
    });
    saveLeitner(l); unstore("karten." + tid);
  }
  function rateCard(key, gut) {
    var l = leitner(), e = l[key] || {};
    var f = gut ? Math.min(5, (e.f || 1) + 1) : 1;
    l[key] = { f: f, d: addDays(INTERVALL[f]) };
    saveLeitner(l);
    return f;
  }
  function fachStats(cards) {
    var l = leitner(), t = today(), st = { neu: 0, faellig: 0, f: [0, 0, 0, 0, 0, 0] };
    cards.forEach(function (c) {
      var e = l[c.key];
      if (!e) { st.neu++; return; }
      st.f[e.f]++;
      if (e.d <= t) st.faellig++;
    });
    return st;
  }

  // Wiederverwendbare Lernsitzung (Themenansicht und tägliche Wiederholung)
  function cardSession(el, cards, opts) {
    opts = opts || {};
    var practice = !!opts.practice;
    function buildQueue() {
      var l = leitner(), t = today();
      if (practice) return shuffle(cards.slice());
      var neu = shuffle(cards.filter(function (c) { return !l[c.key]; }));
      var due = shuffle(cards.filter(function (c) { return l[c.key] && l[c.key].d <= t; }));
      due.sort(function (a, b) { return l[a.key].f - l[b.key].f; });
      return (opts.dueFirst ? due.concat(neu) : neu.concat(due)).slice(0, opts.limit || 9999);
    }
    var queue = buildQueue();
    function statsHTML() {
      var st = fachStats(cards);
      var fach = [1, 2, 3, 4, 5].map(function (i) { return '<span class="pill fach fach-' + i + '" title="Fach ' + i + '">F' + i + ": " + st.f[i] + "</span>"; }).join("");
      return '<div class="cards-top"><div class="progress"><span class="pill">' + cards.length + ' Begriffe</span><span class="pill">' + st.neu + ' neu</span><span class="pill pill-bad">' + st.faellig + " heute fällig</span>" + fach + "</div>" +
        (opts.onReset ? '<button class="linklike" data-cs="reset">Lernstand zurücksetzen</button>' : "") + "</div>" +
        '<p class="muted leitner-hint">Lernkartei mit 5 Fächern: „Klappt schon relativ gut“ schiebt eine Karte ein Fach weiter (später wiederholen), „Klappt noch nicht so gut“ legt sie zurück in Fach 1 (heute noch einmal).</p>';
    }
    function draw() {
      var c = queue[0];
      var html = statsHTML();
      if (!c) {
        current.card = null;
        var l = leitner(), next = null;
        cards.forEach(function (x) { var e = l[x.key]; if (e && (!next || e.d < next)) next = e.d; });
        html += '<div class="cards-done"><h3>' + (practice ? "Durchgang geschafft!" : "Für heute ist alles erledigt.") + "</h3>" +
          (next && !practice ? '<p class="muted">Nächste fällige Wiederholung: ' + next.split("-").reverse().join(".") + "</p>" : "") +
          '<button class="btn btn-primary" data-cs="practice">Alle Begriffe trotzdem üben</button></div>';
      } else {
        current.card = c.b;
        var e = leitner()[c.key];
        html += (queue.length ? '<p class="muted" style="text-align:center">Noch ' + queue.length + " Karte" + (queue.length === 1 ? "" : "n") + " in dieser Runde" + (e ? " · aktuell in Fach " + e.f : " · neue Karte") + "</p>" : "") +
          '<div class="flash-wrap"><button class="flash" id="flash" aria-label="Karteikarte umdrehen"><div class="face face-front">' + (c.nr ? '<div class="card-topic">' + esc(c.nr) + "</div>" : "") + '<div class="term">' + esc(c.b) + '</div><div class="hint">Antippen zum Umdrehen</div></div>' +
          '<div class="face face-back"><div class="term-small">' + esc(c.b) + '</div><div class="def">' + c.lang + '</div></div></button></div>' +
          '<div class="rate" id="rate" hidden><button class="btn btn-good" data-r="gut">Klappt schon relativ gut</button><button class="btn btn-bad" data-r="nicht">Klappt noch nicht so gut</button></div>' +
          '<p class="muted" style="text-align:center" id="rate-hint">Überlege dir zuerst selbst eine Erklärung – dann dreh die Karte um.</p>';
      }
      el.innerHTML = html;
      var rs = $('[data-cs="reset"]', el);
      if (rs) rs.addEventListener("click", function () { if (confirm("Möchtest du den Lernstand für diese Begriffe wirklich zurücksetzen?")) { opts.onReset(); practice = false; queue = buildQueue(); draw(); } });
      var pr = $('[data-cs="practice"]', el);
      if (pr) pr.addEventListener("click", function () { practice = true; queue = buildQueue(); draw(); });
      var flash = $("#flash", el);
      if (!flash) return;
      flash.addEventListener("click", function () {
        flash.classList.toggle("flipped");
        if (flash.classList.contains("flipped")) { $("#rate", el).hidden = false; $("#rate-hint", el).hidden = true; }
      });
      $all("#rate [data-r]", el).forEach(function (b) {
        b.addEventListener("click", function () {
          var gut = b.getAttribute("data-r") === "gut";
          rateCard(c.key, gut);
          queue.shift();
          if (!gut) queue.push(c); // nicht so gut: in dieser Runde später noch einmal
          draw();
        });
      });
    }
    draw();
  }

  // ---------------------------------------------------------------- Fachbegriffe-Memory (2 Spieler, ein Gerät)
  function memoText(t) {
    if (t.memo) return t.memo;
    var w = t.b.split(/[\s(/-]/)[0];
    return String(t.kurz).replace(/<[^>]+>/g, "").replace(new RegExp(w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi"), "…");
  }
  function openMemory(terms, titel) {
    if (terms.length < 4) { alert("Für ein Memory werden mindestens 4 Fachbegriffe benötigt."); return; }
    var reduce = !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
    var EASE_OUT = "cubic-bezier(0.23, 1, 0.32, 1)", EASE_IO = "cubic-bezier(0.77, 0, 0.175, 1)";
    var ov = document.createElement("div");
    ov.className = "memory-overlay";
    ov.setAttribute("role", "dialog"); ov.setAttribute("aria-modal", "true"); ov.setAttribute("aria-label", "Fachbegriffe-Memory");
    document.body.appendChild(ov); document.body.classList.add("no-scroll");
    var G = null, timers = [], raf = 0, lastFocus = document.activeElement, prefs = { names: ["Spieler 1", "Spieler 2"], n: 0 };
    function later(fn, ms) { var t = setTimeout(fn, ms); timers.push(t); return t; }
    function clearTimers() { timers.forEach(clearTimeout); timers = []; if (raf) cancelAnimationFrame(raf); raf = 0; }
    function close() {
      if (G && !G.over && G.found > 0 && !confirm("Spiel wirklich beenden?")) return;
      clearTimers();
      ov.remove(); document.body.classList.remove("no-scroll");
      document.removeEventListener("keydown", onKey); window.removeEventListener("resize", onResize);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    function onKey(e) { if (e.key === "Escape") { var z = $(".m-zoom", ov); if (z) z.remove(); else close(); } }
    function onResize() { if (G && !G.over) fit(); }
    document.addEventListener("keydown", onKey); window.addEventListener("resize", onResize);
    var maxPairs = Math.min(12, terms.length);
    var LAMP = '<div class="m-lamp" aria-hidden="true"></div>';
    var X = '<button class="m-x" aria-label="Memory schließen">' + ICON.close + "</button>";

    // ------------------------------------------------ Einstellungen
    function setup() {
      clearTimers(); G = null;
      var opts = [4, 6, 8, 10, 12].filter(function (n) { return n <= maxPairs; });
      var def = prefs.n && opts.indexOf(prefs.n) >= 0 ? prefs.n : (opts.indexOf(8) >= 0 ? 8 : opts[opts.length - 1]);
      ov.innerHTML = '<div class="m-table">' + LAMP + '<div class="m-setup">' + X +
        '<form class="m-sheet" id="m-form" autocomplete="off"><h2>Fachbegriffe-Memory</h2><p class="m-topic">' + esc(titel) + "</p>" +
        '<ol class="m-rules"><li>Deckt abwechselnd zwei Karten auf: einen <b>Fachbegriff</b> und seine <b>Beschreibung</b>.</li>' +
        "<li>Passen sie zusammen, gibt es einen Punkt – und du bist gleich noch einmal dran.</li>" +
        "<li>Kein Paar? Dann tippt ihr auf „Nächster Spieler“. Aufgedeckte Karten vergrößerst du mit einem weiteren Tipp.</li></ol>" +
        '<div class="m-names"><label class="m-nameplate"><span>Spieler/in 1</span><input id="m-n1" value="' + esc(prefs.names[0]) + '" maxlength="20" required></label>' +
        '<span class="m-vs" aria-hidden="true">gegen</span><label class="m-nameplate"><span>Spieler/in 2</span><input id="m-n2" value="' + esc(prefs.names[1]) + '" maxlength="20" required></label></div>' +
        '<fieldset class="m-pairs"><legend>Wie viele Paare liegen auf dem Tisch?</legend>' + opts.map(function (n) {
          return '<label><input type="radio" name="m-pairs" value="' + n + '"' + (n === def ? " checked" : "") + "><span>" + n + "</span></label>";
        }).join("") + "</fieldset>" +
        '<p class="m-privacy">Die Namen werden nicht gespeichert.</p><button class="btn btn-primary m-go" id="m-start" type="submit">Karten austeilen</button></form></div></div>';
      $(".m-x", ov).addEventListener("click", close);
      $("#m-form", ov).addEventListener("submit", function (e) {
        e.preventDefault();
        var n = +(($("input[name=m-pairs]:checked", ov) || {}).value || def);
        start([$("#m-n1", ov).value.trim() || "Spieler 1", $("#m-n2", ov).value.trim() || "Spieler 2"], n, 0);
      });
      $("#m-start", ov).focus();
    }

    // ------------------------------------------------ Spiel
    function start(names, n, first) {
      clearTimers();
      prefs.names = names; prefs.n = n;
      var pick = shuffle(terms).slice(0, n), deck = [];
      pick.forEach(function (t, i) {
        var kurz = String(t.kurz || "").replace(/<[^>]+>/g, "");
        deck.push({ pair: i, kind: "b", text: t.b, term: t.b, kurz: kurz });
        deck.push({ pair: i, kind: "d", text: memoText(t), term: t.b, kurz: kurz });
      });
      deck = shuffle(deck).map(function (c, i) { c.id = i; c.rot = +(Math.random() * 5 - 2.5).toFixed(1); c.state = "down"; return c; });
      G = { names: names, deck: deck, n: n, player: first, first: first, scores: [0, 0], piles: [[], []], open: [], phase: "deal", found: 0, over: false,
        moves: 0, misses: [0, 0], run: [0, 0], best: [0, 0] };
      board();
      deal();
    }
    function plate(i) {
      return '<div class="m-player" data-p="' + i + '"><span class="m-pile" aria-hidden="true"></span><span class="m-who"><span class="m-name">' + esc(G.names[i]) + '</span><span class="m-turn">ist dran</span></span>' +
        '<span class="m-score" aria-label="Punkte">0</span><span class="m-streak" hidden></span></div>';
    }
    function board() {
      ov.innerHTML = '<div class="m-table">' + LAMP +
        '<header class="m-head">' + plate(0) + '<div class="m-mid"><div class="m-progress" aria-hidden="true"><span></span></div><div class="m-count"></div></div>' + plate(1) + X + "</header>" +
        '<main class="m-felt"><div class="m-grid">' + G.deck.map(cardHTML).join("") + '</div><div class="m-deck" aria-hidden="true"></div></main>' +
        '<footer class="m-foot"><div class="m-learn intro">Nach jedem gefundenen Paar steht hier die Kurzdefinition des Fachbegriffs – zum Mitlernen.</div><div class="m-bar"><p class="m-msg" aria-live="polite"></p><button class="btn btn-primary m-nextbtn" id="m-next" hidden>Nächster Spieler</button></div></footer></div>';
      $(".m-x", ov).addEventListener("click", close);
      $("#m-next", ov).addEventListener("click", next);
      $all(".m-card", ov).forEach(function (b) { b.addEventListener("click", function () { click(G.deck[+b.getAttribute("data-c")]); }); });
      fit(); status();
      if (window.ResizeObserver) { var ro = new ResizeObserver(function () { if (G && !G.over) fit(); }); ro.observe($(".m-felt", ov)); }
    }
    function cardHTML(c) {
      return '<button class="m-card" data-c="' + c.id + '" style="--rot:' + c.rot + 'deg" aria-label="verdeckte Karte">' +
        '<span class="m-inner"><span class="m-back"><span class="m-print">Feibitur</span><span class="m-logo">F</span><span class="m-stripes"><i></i><i></i><i></i><i></i></span></span>' +
        '<span class="m-front ' + (c.kind === "b" ? "m-term" : "m-def") + '"><span class="m-text">' + esc(c.text) + "</span></span></span></button>";
    }
    function el(c) { return $('.m-card[data-c="' + c.id + '"]', ov); }
    // Kartengröße so wählen, dass möglichst alle Karten ohne Scrollen auf den Tisch passen
    function fit() {
      var felt = $(".m-felt", ov), grid = $(".m-grid", ov);
      if (!felt || !grid) return;
      var W = felt.clientWidth - 24, H = felt.clientHeight - 24, N = G.deck.length, gap = W < 560 ? 8 : 16, best = null;
      for (var cols = 2; cols <= N; cols++) {
        var rows = Math.ceil(N / cols);
        var w = Math.min((W - gap * (cols - 1)) / cols, ((H - gap * (rows - 1)) / rows) * 0.75);
        if (!best || w > best.w) best = { cols: cols, w: w };
      }
      var minW = W < 400 ? 74 : (W < 560 ? 80 : 118);
      if (best.w < minW) { // lieber scrollen als winzige Karten – dann die Breite voll nutzen
        var c2 = Math.max(2, Math.floor((W + gap) / (minW + gap)));
        best = { cols: c2, w: (W - gap * (c2 - 1)) / c2 };
      }
      best.w = Math.min(best.w, 190);
      grid.style.setProperty("--cols", best.cols);
      grid.style.setProperty("--cw", Math.floor(best.w) + "px");
      grid.style.setProperty("--gap", gap + "px");
      grid.classList.toggle("small", best.w < 128);
    }
    function status(msg) {
      var p = G.player;
      $all(".m-player", ov).forEach(function (pl, i) {
        pl.classList.toggle("active", i === p && !G.over && G.phase !== "deal");
        $(".m-score", pl).textContent = G.scores[i];
        var st = $(".m-streak", pl);
        st.hidden = G.run[i] < 2; st.textContent = "Serie ×" + G.run[i];
      });
      $(".m-progress span", ov).style.transform = "scaleX(" + (G.found / G.n) + ")";
      $(".m-count", ov).textContent = G.found + " von " + G.n + " Paaren · Zug " + (G.moves + 1);
      $(".m-msg", ov).innerHTML = msg || (G.phase === "deal" ? "Die Karten werden ausgeteilt …" :
        "<b>" + esc(G.names[p]) + "</b> ist dran: " + (G.phase === "pick2" ? "Decke die zweite Karte auf." : "Decke eine Karte auf."));
    }
    function deal() {
      var cards = $all(".m-card", ov), deck = $(".m-deck", ov);
      if (reduce || !deck.animate) { G.phase = "pick1"; status(); return; }
      var d = deck.getBoundingClientRect();
      cards.forEach(function (b, i) {
        var r = b.getBoundingClientRect(), c = G.deck[i];
        var dx = d.left + d.width / 2 - (r.left + r.width / 2), dy = d.top + d.height / 2 - (r.top + r.height / 2);
        b.animate([
          { transform: "translate(" + dx + "px," + dy + "px) rotate(" + (c.rot * 4) + "deg) scale(.86)", opacity: 0 },
          { opacity: 1, offset: 0.15 },
          { transform: "rotate(" + c.rot + "deg)", opacity: 1 }
        ], { duration: 520, delay: i * 45, easing: EASE_OUT, fill: "backwards" });
      });
      later(function () { if (G && G.phase === "deal") { G.phase = "pick1"; status(); } }, 520 + cards.length * 45);
    }
    function flip(c, up) {
      c.state = up ? "up" : "down";
      var b = el(c); if (!b) return;
      b.classList.toggle("up", up);
      b.setAttribute("aria-label", up ? (c.kind === "b" ? "Fachbegriff: " : "Beschreibung: ") + c.text + " – zum Vergrößern erneut antippen" : "verdeckte Karte");
    }
    function zoom(c) {
      var z = document.createElement("div");
      z.className = "m-zoom";
      z.innerHTML = '<div class="m-zoom-card ' + (c.kind === "b" ? "m-term" : "m-def") + '" role="document" aria-label="' + (c.kind === "b" ? "Fachbegriff" : "Beschreibung") + '"><span class="m-text">' + esc(c.text) + '</span><span class="m-hint">Zum Schließen tippen</span></div>';
      z.addEventListener("click", function () { z.remove(); });
      ov.appendChild(z);
    }
    function learn(c) {
      var l = $(".m-learn", ov);
      l.innerHTML = '<span class="m-learn-k">Gut gemerkt?</span><b>' + esc(c.term) + "</b>" + (c.kurz ? " – " + esc(c.kurz) : "");
      l.classList.remove("intro", "in"); void l.offsetWidth; l.classList.add("in");
    }
    function click(c) {
      if (!G || G.over || c.state === "gone") return;
      if (c.state === "up") { zoom(c); return; }
      if (G.phase === "pick1") {
        flip(c, true); G.open = [c]; G.phase = "pick2"; status(); return;
      }
      if (G.phase !== "pick2") return;
      flip(c, true); G.open.push(c); G.moves++;
      var a = G.open[0], b = G.open[1], p = G.player;
      if (a.pair === b.pair && a.kind !== b.kind) {
        G.phase = "wait";
        G.run[p]++; G.best[p] = Math.max(G.best[p], G.run[p]);
        var serie = G.run[p] >= 2 ? " <span class=\"m-serie\">Serie ×" + G.run[p] + "!</span>" : "";
        status("<b>Paar!</b> " + esc(G.names[p]) + " bekommt einen Punkt und ist noch einmal dran." + serie);
        learn(a);
        later(function () { el(a).classList.add("hit"); el(b).classList.add("hit"); }, reduce ? 0 : 380);
        later(function () { collect([a, b], p); }, reduce ? 900 : 1500);
      } else {
        G.phase = "reveal"; G.misses[p]++; G.run[p] = 0;
        status("Kein Paar. Schaut euch beide Karten in Ruhe an – dann ist <b>" + esc(G.names[1 - p]) + "</b> dran.");
        later(function () { [a, b].forEach(function (x) { var e = el(x); e.classList.remove("miss"); void e.offsetWidth; e.classList.add("miss"); }); }, reduce ? 0 : 420);
        var nx = $("#m-next", ov); nx.hidden = false; nx.focus({ preventScroll: true });
      }
    }
    // Gefundenes Paar fliegt auf den Stapel des Spielers
    function collect(pair, p) {
      var pile = $('.m-player[data-p="' + p + '"] .m-pile', ov), pr = pile.getBoundingClientRect(), done = 0;
      function finish() {
        if (++done < pair.length) return;
        G.scores[p]++; G.found++;
        G.piles[p].push(pair[0].term);
        var mini = document.createElement("i");
        mini.style.setProperty("--r", (Math.random() * 16 - 8).toFixed(1) + "deg");
        pile.appendChild(mini);
        var sc = $('.m-player[data-p="' + p + '"] .m-score', ov);
        sc.classList.remove("bump"); void sc.offsetWidth; sc.classList.add("bump");
        G.open = []; G.phase = "pick1"; status();
        if (G.found === G.n) later(end, reduce ? 200 : 650);
      }
      pair.forEach(function (c, i) {
        var b = el(c); c.state = "gone";
        b.classList.remove("hit"); b.classList.add("gone"); b.disabled = true; b.setAttribute("aria-label", "Paar gefunden");
        if (reduce || !b.animate) { finish(); return; }
        var r = b.getBoundingClientRect();
        var fly = document.createElement("div");
        fly.className = "m-fly";
        fly.style.cssText = "left:" + r.left + "px;top:" + r.top + "px;width:" + r.width + "px;height:" + r.height + "px";
        fly.innerHTML = $(".m-front", b).outerHTML;
        ov.appendChild(fly);
        var dx = pr.left + pr.width / 2 - (r.left + r.width / 2), dy = pr.top + pr.height / 2 - (r.top + r.height / 2);
        var s = Math.max(0.12, pr.height / r.height);
        fly.animate([
          { transform: "rotate(" + c.rot + "deg)", offset: 0 },
          { transform: "translate(0,-14px) rotate(" + c.rot + "deg) scale(1.06)", offset: 0.18 },
          { transform: "translate(" + dx + "px," + dy + "px) rotate(" + (i ? 14 : -10) + "deg) scale(" + s + ")" }
        ], { duration: 640, delay: i * 70, easing: EASE_IO, fill: "forwards" }).onfinish = function () { fly.remove(); finish(); };
      });
    }
    function next() {
      if (!G || G.phase !== "reveal") return;
      G.open.forEach(function (c) { flip(c, false); var e = el(c); if (e) e.classList.remove("miss"); });
      G.open = []; G.player = 1 - G.player; G.phase = "pick1";
      $("#m-next", ov).hidden = true;
      status();
      var first = $(".m-card:not(.gone)", ov); if (first) first.focus({ preventScroll: true });
    }

    // ------------------------------------------------ Siegerehrung
    function end() {
      G.over = true; status("Alle Paare sind gefunden!");
      var s = G.scores, w = s[0] === s[1] ? -1 : (s[0] > s[1] ? 0 : 1);
      var order = w === 1 ? [1, 0] : [0, 1];
      function quote(i) { var t = s[i] + G.misses[i]; return t ? Math.round(100 * s[i] / t) + " %" : "–"; }
      function step(i, place) {
        return '<div class="m-step m-place-' + place + (w < 0 ? " m-tie" : "") + '"><span class="m-step-name">' + esc(G.names[i]) + '</span><span class="m-step-pairs">' + s[i] + (s[i] === 1 ? " Paar" : " Paare") + '</span><span class="m-step-block"><span>' + (w < 0 ? "1" : place) + "</span></span></div>";
      }
      var layer = document.createElement("div");
      layer.className = "m-end-layer";
      layer.innerHTML = '<canvas class="m-confetti" aria-hidden="true"></canvas><div class="m-end-scroll"><section class="m-sheet m-end" role="alertdialog" aria-labelledby="m-end-title">' + X +
        '<h2 id="m-end-title">' + (w < 0 ? "Unentschieden!" : "Herzlichen Glückwunsch, " + esc(G.names[w]) + "!") + "</h2>" +
        '<p class="m-end-sub">' + (w < 0 ? "Ihr habt beide gleich viele Paare gefunden." : esc(G.names[w]) + " gewinnt das Fachbegriffe-Memory mit " + s[w] + " zu " + s[1 - w] + ".") + "</p>" +
        '<div class="m-podium">' + step(order[1], 2) + step(order[0], 1) + "</div>" +
        '<table class="m-stats"><thead><tr><th scope="col"><span class="visually-hidden">Wert</span></th><th scope="col">' + esc(G.names[0]) + '</th><th scope="col">' + esc(G.names[1]) + "</th></tr></thead><tbody>" +
        "<tr><th scope=\"row\">Gefundene Paare</th><td>" + s[0] + "</td><td>" + s[1] + "</td></tr>" +
        "<tr><th scope=\"row\">Fehlversuche</th><td>" + G.misses[0] + "</td><td>" + G.misses[1] + "</td></tr>" +
        "<tr><th scope=\"row\">Längste Serie</th><td>" + G.best[0] + "</td><td>" + G.best[1] + "</td></tr>" +
        "<tr><th scope=\"row\">Trefferquote</th><td>" + quote(0) + "</td><td>" + quote(1) + "</td></tr></tbody></table>" +
        '<details class="m-found"><summary>Gefundene Fachbegriffe ansehen</summary><div class="m-found-cols">' + [0, 1].map(function (i) {
          return "<div><b>" + esc(G.names[i]) + "</b><ul>" + (G.piles[i].length ? G.piles[i].map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") : "<li>keine Paare</li>") + "</ul></div>";
        }).join("") + "</div></details>" +
        '<div class="m-end-actions"><button class="btn btn-primary" id="m-again">Revanche</button><button class="btn" id="m-setup">Neue Einstellungen</button><button class="btn" id="m-close">Schließen</button></div>' +
        '<p class="m-privacy">Bei der Revanche beginnt ' + esc(G.names[1 - G.first]) + ".</p></section></div>";
      $(".m-table", ov).appendChild(layer);
      $(".m-x", layer).addEventListener("click", close);
      $("#m-close", layer).addEventListener("click", close);
      $("#m-setup", layer).addEventListener("click", setup);
      $("#m-again", layer).addEventListener("click", function () { start(G.names, G.n, 1 - G.first); });
      $("#m-again", layer).focus({ preventScroll: true });
      if (!reduce) confetti($(".m-confetti", layer));
    }
    function confetti(cv) {
      var ctx = cv.getContext && cv.getContext("2d"); if (!ctx) return;
      var dpr = Math.min(2, window.devicePixelRatio || 1), W = cv.clientWidth, H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.scale(dpr, dpr);
      var cols = ["#D23A1F", "#2340C8", "#0A6E72", "#F2B300", "#ffffff"], P = [], t0 = performance.now();
      for (var i = 0, N = W < 600 ? 90 : 170; i < N; i++) {
        var left = i % 2 === 0;
        P.push({ x: left ? -10 : W + 10, y: H * (0.55 + Math.random() * 0.3), vx: (left ? 1 : -1) * (4 + Math.random() * 7), vy: -(9 + Math.random() * 8),
          w: 6 + Math.random() * 7, h: 9 + Math.random() * 10, a: Math.random() * 6.28, va: (Math.random() - 0.5) * 0.3, c: cols[i % cols.length], d: Math.random() * 350 });
      }
      function frame(now) {
        var t = now - t0; ctx.clearRect(0, 0, W, H); var alive = false;
        P.forEach(function (p) {
          if (t < p.d) { alive = true; return; }
          p.vy += 0.32; p.vx *= 0.985; p.vy *= 0.985; p.x += p.vx; p.y += p.vy; p.a += p.va;
          if (p.y < H + 30) alive = true;
          ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.a); ctx.scale(1, Math.cos(p.a * 2));
          ctx.fillStyle = p.c; ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h); ctx.restore();
        });
        if (alive && t < 6000 && cv.isConnected) raf = requestAnimationFrame(frame); else { ctx.clearRect(0, 0, W, H); raf = 0; }
      }
      raf = requestAnimationFrame(frame);
    }
    setup();
  }
  function memoryBtnHTML() { return '<div class="memory-launch"><button class="btn btn-memory" data-memory>' + ICON.cards + " Fachbegriffe-Memory gegen eine weitere Person spielen</button></div>"; }

  function renderBegriffe(body, meta, topic) {
    if (!topic || !topic.begriffe.length) {
      body.innerHTML = emptySection("Die Fachbegriffe zu diesem Unterthema werden noch eingepflegt.") + glossarHTML();
      bindGlossar(body);
      return;
    }
    migrateKarten(meta.id);
    var terms = topic.begriffe.filter(function (t) { return zeigeLK() || !t.lk; });
    var cards = terms.map(function (t) { return { key: cardKey(meta.id, t.b), b: t.b, lang: t.lang, kurz: t.kurz }; });
    body.innerHTML = memoryBtnHTML() + '<div id="cs"></div>' + glossarHTML();
    bindGlossar(body);
    $("[data-memory]", body).addEventListener("click", function () { openMemory(terms, meta.nr + " " + meta.titel); });
    cardSession($("#cs", body), cards, {
      onReset: function () { var l = leitner(); cards.forEach(function (c) { delete l[c.key]; }); saveLeitner(l); }
    });
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
        if (g.lk && !zeigeLK()) return false;
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
  function wrapTables(html) { return String(html).replace(/<table>/g, '<div class="table-scroll"><table>').replace(/<\/table>/g, "</table></div>"); }
  var KIND = { "Erklärung": "k-erklaerung", "Fachtext": "k-fachtext", "Merke": "k-merke", "Beispiel": "k-beispiel", "Gesetzestext": "k-gesetz", "Grafik": "k-grafik", "Schaubild": "k-grafik" };
  function renderBlock(b) {
    var lk = b.lk ? '<span class="stoerer lk-tag">Nur LK</span>' : "";
    var cls = "block" + (b.art === "Fachtext" ? " fachtext" : "") + (b.art === "Merke" ? " merke" : "") + (b.art === "Gesetzestext" ? " gesetz" : "") + (b.lk ? " lk" : "");
    var kind = '<span class="block-kind ' + (KIND[b.art] || "k-erklaerung") + '">' + esc(b.art) + "</span>";
    var inner = "";
    if (b.t === "svg") inner = '<figure class="figure" style="margin:0">' + b.svg + (b.caption ? "<figcaption>" + b.caption + "</figcaption>" : "") + "</figure>";
    else if (b.t === "table") inner = '<div class="table-scroll"><table><thead><tr>' + b.kopf.map(function (k) { return "<th>" + k + "</th>"; }).join("") + "</tr></thead><tbody>" +
      b.zeilen.map(function (z) { return "<tr>" + z.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table></div>" + (b.html || "");
    else inner = wrapTables(b.html);
    var sp = speechOn() ? '<button class="speak-btn" data-speak aria-label="Abschnitt vorlesen" title="Vorlesen">' + ICON.speaker + "</button>" : "";
    var head = '<header class="block-head' + (b.titel ? "" : " bare") + '">' + (b.titel ? "<h3>" + b.titel + "</h3>" : "") + kind + sp + "</header>";
    return '<section class="' + cls + '">' + lk + head + inner + (b.quelle ? '<p class="src">' + b.quelle + "</p>" : "") + "</section>";
  }
  function renderInhalte(body, meta, topic) {
    var blocks = topic ? topic.inhalte.filter(function (b) { return zeigeLK() || !b.lk; }) : [];
    var weg = topic ? topic.inhalte.length - blocks.length : 0;
    var main = (!topic || !topic.inhalte.length) ? emptySection("Die Inhalte zu diesem Unterthema werden noch eingepflegt.") : blocks.map(renderBlock).join("") +
      (weg ? '<p class="muted kurs-note">' + weg + " Abschnitt" + (weg === 1 ? "" : "e") + " nur für den Leistungskurs ausgeblendet (du hast „Grundkurs“ gewählt).</p>" : "");
    body.innerHTML = '<div class="content-grid"><div class="content-main">' + (meta.podcast ? radioHTML(meta) : "") + main + '</div><aside class="chat" id="chat"></aside></div>';
    bindSpeak(body);
    if (meta.podcast) bindRadio(body, meta);
    renderChat($("#chat", body), meta);
  }

  // ---------------------------------------------------------------- Podcast-Radio (Röhrenradio mit Start- und Pause-Taste)
  var RADIO_TEMPI = [1, 1.2, 1.5];
  function mmss(t) { t = Math.max(0, Math.round(t || 0)); return Math.floor(t / 60) + ":" + ("0" + (t % 60)).slice(-2); }
  function radioHTML(meta) {
    var p = meta.podcast, dauer = p.dauer, labels = "";
    for (var m = 0; m * 60 <= dauer; m += 5) labels += '<span style="left:' + (m * 60 / dauer * 100).toFixed(2) + '%">' + m + "</span>";
    return '<section class="radio" aria-label="Podcast zum Unterthema ' + esc(meta.nr) + '">' +
      '<div class="radio-cab"><span class="radio-eye" aria-hidden="true"></span>' +
      '<div class="radio-dial" role="slider" tabindex="0" aria-label="Abspielposition (Pfeiltasten: 15 Sekunden vor oder zurück)" aria-valuemin="0" aria-valuemax="' + dauer + '" aria-valuenow="0" aria-valuetext="0:00 von ' + mmss(dauer) + '" style="--tick:' + (60 / dauer * 100).toFixed(3) + '%">' +
      '<span class="radio-scale" aria-hidden="true"></span><span class="radio-labels" aria-hidden="true">' + labels + '<i>Min.</i></span>' +
      '<span class="radio-needle" aria-hidden="true"></span><span class="radio-brand" aria-hidden="true">Feibitur · Podcast</span></div>' +
      '<div class="radio-grille" aria-hidden="true"><span class="radio-badge">F</span></div>' +
      '<div class="radio-keys"><button class="radio-key" data-radio="play" aria-pressed="false">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l12.5-7.5z" fill="currentColor"/></svg><span>Start</span></button>' +
      '<button class="radio-key" data-radio="pause" aria-pressed="true"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 4.5h4v15h-4zM13.5 4.5h4v15h-4z" fill="currentColor"/></svg><span>Pause</span></button></div>' +
      '<div class="radio-tempo" role="group" aria-label="Abspielgeschwindigkeit"><span class="radio-tempo-label" aria-hidden="true">Tempo</span>' +
      RADIO_TEMPI.map(function (r) { return '<button class="radio-speed" data-speed="' + r + '" aria-pressed="false" aria-label="Geschwindigkeit ' + String(r).replace(".", ",") + '-fach">' + String(r).replace(".", ",") + "×</button>"; }).join("") + "</div>" +
      '<div class="radio-plate"><span class="radio-title">Podcast zu ' + esc(meta.nr) + ": „" + esc(p.titel) + '“</span> <span class="radio-time" aria-live="off">0:00 / ' + mmss(dauer) + "</span></div></div>" +
      '<p class="radio-note">KI-generierter Podcast (Google NotebookLM) auf Grundlage eines geprüften Feibitur-Informationstextes. KI kann sich irren – im Zweifel gilt der Text unten.</p>' +
      '<audio preload="none" src="' + esc(p.src) + '"></audio></section>';
  }
  function bindRadio(root, meta) {
    var box = $(".radio", root), audio = $("audio", box), dial = $(".radio-dial", box), time = $(".radio-time", box);
    var play = $('[data-radio="play"]', box), pause = $('[data-radio="pause"]', box), key = "podcast." + meta.id;
    var dauer = meta.podcast.dauer, saved = +(store(key) || 0), lastSave = 0;
    function dur() { return isFinite(audio.duration) && audio.duration > 0 ? audio.duration : dauer; }
    function show(t) {
      var d = dur(), p = Math.min(1, Math.max(0, t / d));
      box.style.setProperty("--p", p.toFixed(4));
      time.textContent = mmss(t) + " / " + mmss(d);
      dial.setAttribute("aria-valuenow", Math.round(t));
      dial.setAttribute("aria-valuetext", mmss(t) + " von " + mmss(d));
    }
    function setPos(t) {
      t = Math.max(0, Math.min(dur() - 1, t));
      if (audio.readyState >= 1) audio.currentTime = t; else saved = t;
      store(key, Math.round(t)); show(t);
    }
    var rate = +(store("podcastTempo") || 1);
    if (RADIO_TEMPI.indexOf(rate) < 0) rate = 1;
    function tempo(r) {
      rate = r; audio.defaultPlaybackRate = r; audio.playbackRate = r; store("podcastTempo", r);
      $all(".radio-speed", box).forEach(function (bt) { bt.setAttribute("aria-pressed", String(+bt.getAttribute("data-speed") === r)); });
    }
    tempo(rate);
    $all(".radio-speed", box).forEach(function (bt) { bt.addEventListener("click", function () { tempo(+bt.getAttribute("data-speed")); }); });
    function state(on) {
      box.classList.toggle("on", on);
      play.setAttribute("aria-pressed", String(on)); pause.setAttribute("aria-pressed", String(!on));
    }
    show(saved);
    audio.addEventListener("loadedmetadata", function () { audio.playbackRate = rate; if (saved > 0 && saved < audio.duration - 2) audio.currentTime = saved; show(audio.currentTime); });
    audio.addEventListener("timeupdate", function () {
      show(audio.currentTime);
      if (Math.abs(audio.currentTime - lastSave) >= 5) { lastSave = audio.currentTime; store(key, Math.round(audio.currentTime)); }
    });
    audio.addEventListener("play", function () { if (audio.playbackRate !== rate) audio.playbackRate = rate; state(true); if (speechSupported()) speechSynthesis.cancel(); });
    audio.addEventListener("pause", function () { state(false); store(key, Math.round(audio.currentTime || saved)); });
    audio.addEventListener("ended", function () { state(false); unstore(key); saved = 0; show(0); });
    audio.addEventListener("error", function () { state(false); time.textContent = "Der Podcast konnte nicht geladen werden."; });
    play.addEventListener("click", function () { var pr = audio.play(); if (pr && pr.catch) pr.catch(function () { state(false); }); });
    pause.addEventListener("click", function () { audio.pause(); });
    dial.addEventListener("click", function (e) {
      var r = $(".radio-scale", dial).getBoundingClientRect();
      setPos((e.clientX - r.left) / r.width * dur());
    });
    dial.addEventListener("keydown", function (e) {
      var t = audio.readyState >= 1 ? audio.currentTime : saved;
      if (e.key === "ArrowRight" || e.key === "ArrowUp") { e.preventDefault(); setPos(t + 15); }
      else if (e.key === "ArrowLeft" || e.key === "ArrowDown") { e.preventDefault(); setPos(t - 15); }
      else if (e.key === "Home") { e.preventDefault(); setPos(0); }
      else if (e.key === " " || e.key === "Enter") { e.preventDefault(); if (audio.paused) play.click(); else pause.click(); }
    });
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
      '<form class="chat-form" id="chat-form"><label class="visually-hidden" for="chat-in">Frage an den Chatbot</label><textarea id="chat-in" rows="2" placeholder="Deine Frage zum Thema …" maxlength="1200"></textarea><button class="btn btn-primary" type="submit" aria-label="Senden">' + ICON.arrow + '</button></form>' +
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

  function matHTML(m) {
    var inner;
    if (m.typ === "tabelle") inner = '<div class="table-scroll block" style="padding:.5rem"><table><thead><tr>' + m.kopf.map(function (k) { return "<th>" + k + "</th>"; }).join("") + "</tr></thead><tbody>" + m.zeilen.map(function (z) { return "<tr>" + z.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table></div>";
    else if (m.typ === "bild") inner = '<figure class="figure mat-bild">' + m.svg + "</figure>";
    else inner = '<div class="mat-text">' + m.absaetze.map(function (p, n) { return '<div class="mat-p"><span class="pn">[' + (n + 1) + "]</span><div>" + p + "</div></div>"; }).join("") + "</div>";
    return "<h4>" + m.titel + "</h4>" + inner + (m.quelle ? '<p class="mat-src">' + m.quelle + "</p>" : "");
  }

  // ---------------------------------------------------------------- Vorlesen (Sprachausgabe des Geräts)
  function speechSupported() { return "speechSynthesis" in window && "SpeechSynthesisUtterance" in window; }
  function speechPrefs() { var p = store("vorlesen") || {}; return { on: p.on !== false, rate: p.rate || 1, voice: p.voice || "", online: !!p.online }; }
  function speechOn() { return speechSupported() && speechPrefs().on; }
  function pickVoice() {
    var pr = speechPrefs(), vs = speechSynthesis.getVoices().filter(function (v) { return /^de/i.test(v.lang); });
    if (!pr.online) vs = vs.filter(function (v) { return v.localService; });
    return vs.filter(function (v) { return v.voiceURI === pr.voice; })[0] || vs[0] || null;
  }
  function speak(text, onEnd) {
    if (!speechSupported()) return false;
    speechSynthesis.cancel();
    var v = pickVoice();
    if (!v) { alert("Auf diesem Gerät ist keine lokale deutsche Stimme verfügbar. In den Vorbereitungs-Tools unter „Vorlesen“ kannst du die Einstellungen anpassen."); return false; }
    var chunks = String(text).replace(/\s+/g, " ").match(/[^.!?]+[.!?]*\s*/g) || [text];
    chunks.forEach(function (c, i) {
      var u = new SpeechSynthesisUtterance(c);
      u.voice = v; u.lang = v.lang; u.rate = speechPrefs().rate;
      if (i === chunks.length - 1 && onEnd) u.onend = onEnd;
      speechSynthesis.speak(u);
    });
    return true;
  }
  function textOf(el) {
    var c = el.cloneNode(true);
    $all("svg, .speak-btn, .block-kind, .lk-tag, .src", c).forEach(function (x) { x.remove(); });
    return c.textContent;
  }
  function bindSpeak(root) {
    $all("[data-speak]", root).forEach(function (b) {
      b.addEventListener("click", function (e) {
        e.stopPropagation();
        if (b.classList.contains("speaking")) { speechSynthesis.cancel(); b.classList.remove("speaking"); return; }
        $all(".speak-btn.speaking").forEach(function (x) { x.classList.remove("speaking"); });
        var sec = b.closest("section, article, .speakable");
        if (speak(textOf(sec), function () { b.classList.remove("speaking"); })) b.classList.add("speaking");
      });
    });
  }
  window.addEventListener("hashchange", function () { if (speechSupported()) speechSynthesis.cancel(); $all(".radio audio").forEach(function (a) { a.pause(); }); });

  // ---------------------------------------------------------------- Übungsaufgaben
  function renderAufgaben(body, meta, topic) {
    var howto = '<section class="howto"><h3>So funktioniert das Üben mit den Übungsaufgaben</h3><ol>' +
      "<li><span>Aufgabe und Material genau anschauen und dann eine Lösung verfassen (in einem Schreibprogramm oder leserlich auf GoodNotes etc.).</span></li>" +
      "<li><span>Eigene Lösung inkl. der hier zu jeder Aufgabe herunterladbaren „Korrekturdatei“ in einem KI-System des Vertrauens hochladen und die KI bitten, die Hintergrunddaten der Korrekturdatei zu nutzen, um eine Rückmeldung zu formulieren.</span></li>" +
      "<li><span>KI-Rückmeldung nutzen und reflektieren.</span></li></ol>" +
      '<p class="muted" style="margin:.7rem 0 0">Tipp für Schritt 2: Schreib z. B. „Hier sind meine Lösung und die Korrekturdatei. Bitte lies die Hintergrunddaten der Korrekturdatei und gib mir danach eine Rückmeldung.“ Lade keine Dateien mit deinem Namen hoch.</p></section>';
    if (!topic || !topic.aufgaben.length) { body.innerHTML = howto + '<div style="margin-top:1rem">' + emptySection("Übungsaufgaben zu diesem Unterthema werden noch erstellt.") + "</div>"; return; }
    var matById = {};
    (topic.materialien || []).forEach(function (m) { matById[m.id] = m; });
    var AFB = [
      ["I", "Anforderungsbereich I", "Wiedergeben und Beschreiben: Inhalte aus dem Material oder Gelerntes korrekt, strukturiert und in eigenen Worten darstellen."],
      ["II", "Anforderungsbereich II", "Erklären, Analysieren und Anwenden: Gelerntes selbstständig ordnen, mit Fachwissen verknüpfen und auf neue Zusammenhänge übertragen."],
      ["III", "Anforderungsbereich III", "Urteilen und Reflektieren: Sachverhalte begründet beurteilen, bewerten und eigene Urteile kriteriengeleitet entwickeln."],
    ];
    var html = howto;
    AFB.forEach(function (g) {
      var list = topic.aufgaben.filter(function (a) { return a.afb === g[0] && (zeigeLK() || !a.lk); });
      if (!list.length) return;
      html += '<section class="afb-group"><h3 class="afb-head"><span class="afb-tag">AFB ' + g[0] + "</span>" + g[1] + '</h3><p class="muted afb-desc">' + g[2] + "</p>";
      list.forEach(function (a) {
        var o = SITE.operatoren[a.operator];
        var mats = a.material.length ? a.material.map(function (id) { return matById[id] ? matHTML(matById[id]) : ""; }).join("")
          : '<p class="muted no-mat">Zu dieser Aufgabe gibt es kein Material. Nutze dein Fachwissen und eigene Beispiele.</p>';
        var refs = a.material.length ? '<span class="mat-refs">' + a.material.map(function (id) { return id.toUpperCase(); }).join(", ") + "</span>" : "";
        var done = !!(store("erledigt") || {})[a.id];
        html += '<article class="task2' + (done ? " is-done" : "") + '" id="task-' + a.id + '">' +
          '<button class="task2-head" aria-expanded="false" aria-controls="tb-' + a.id + '">' +
          '<span class="tnum">' + a.nr + '</span><span class="tmain"><span class="tops"><span class="op-badge">' + esc(a.operator) + "</span>" +
          (a.lk ? '<span class="badge badge-lk">LK-Niveau</span>' : "") + refs + '<span class="done-badge">bearbeitet</span></span><span class="ttext">' + a.text + "</span></span>" + ICON.chev + "</button>" +
          '<div class="task2-body" id="tb-' + a.id + '" hidden><label class="done-check"><input type="checkbox" data-done="' + a.id + '"' + (done ? " checked" : "") + "> Diese Aufgabe habe ich bearbeitet (für deinen Lernfortschritt)</label>" + '<div class="mat-top"><div class="op-box"><h4>Was verlangt der Operator? (Definition des Landes Hessen)</h4><dl><dt>' + esc(a.operator) +
          ' <span class="muted">(AFB ' + o.afb + ")</span></dt><dd>" + esc(o.def) + '</dd></dl><p class="src">' + esc(SITE.operatorenVorbemerkung) + "<br>Quelle: " + esc(SITE.operatorenQuelle) + "</p></div>" +
          '<a class="btn btn-green" href="' + a.pdf + '" download>' + ICON.download + 'Korrekturdatei herunterladen</a></div><div class="mat-doc">' + mats + "</div></div></article>";
      });
      html += "</section>";
    });
    body.innerHTML = html;
    $all("[data-done]", body).forEach(function (cb) {
      cb.addEventListener("change", function () {
        var d = store("erledigt") || {}, id = cb.getAttribute("data-done");
        if (cb.checked) d[id] = today(); else delete d[id];
        store("erledigt", d);
        document.getElementById("task-" + id).classList.toggle("is-done", cb.checked);
      });
    });
    $all(".task2-head", body).forEach(function (b) {
      b.addEventListener("click", function () {
        var tb = document.getElementById(b.getAttribute("aria-controls"));
        tb.hidden = !tb.hidden;
        b.setAttribute("aria-expanded", String(!tb.hidden));
      });
    });
  }

  ["g1", "g2", "g3"].forEach(function (id) { unstore("karten." + id); }); // alter Lernstand der früheren Grundlagen-Karteikarten

  // Schnittstelle für die Lerntools (assets/js/tools.js)
  window.Feibitur = {
    site: function () { return SITE; }, meta: TOPIC_META, loadTopic: loadTopic, fetchJSON: fetchJSON,
    kursWahl: kursWahl, zeigeLK: zeigeLK,
    store: store, unstore: unstore, esc: esc, $: $, $all: $all, go: go, norm: norm, shuffle: shuffle,
    topbar: topbar, toolsBtn: toolsBtn, footer: footer, icon: ICON, current: current, app: app,
    renderBlock: renderBlock, matHTML: matHTML, wrapTables: wrapTables,
    leitner: leitner, saveLeitner: saveLeitner, cardKey: cardKey, migrateKarten: migrateKarten, rateCard: rateCard,
    fachStats: fachStats, cardSession: cardSession, openMemory: openMemory, memoryBtnHTML: memoryBtnHTML, today: today, addDays: addDays, isoDate: isoDate,
    glossarHTML: glossarHTML, bindGlossar: bindGlossar, preloadGlossar: preloadGlossar,
    speechSupported: speechSupported, speechPrefs: speechPrefs, speak: speak, bindSpeak: bindSpeak, pickVoice: pickVoice
  };
  initGate();
})();
