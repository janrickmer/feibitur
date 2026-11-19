/* Feibitur – Bewegung
 * Prismenwender: die Plakatwand der Startseite dreht ihre Prismen-Lamellen und zeigt nacheinander
 * Wortmarke, Grundlagen, Q1–Q4 und die Vorbereitungs-Tools. Läuft nur, solange die Wand sichtbar ist,
 * lässt sich anhalten und steht bei „Bewegung reduzieren“ still.
 */
(function () {
  "use strict";

  var HOLD = 3800, FIRST = 700, TURN = 900, STAGGER = 55;
  var EASE = "cubic-bezier(0.77, 0, 0.175, 1)"; // --ease-io: mechanisch, wie die Lamellen einer Wendetafel

  function reduced() { return !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function markHTML() {
    return '<div class="wp wp-mark"><b class="wp-word">Feibitur</b>' +
      '<span class="wp-vier"><i data-hj="grundlagen"></i><i data-hj="q1"></i><i data-hj="q2"></i><i data-hj="q3"></i><i data-hj="q4"></i></span></div>';
  }
  function blankHTML() { return '<div class="wp wp-blank"></div>'; }
  function posterHTML(p) {
    return '<div class="wp" data-hj="' + p.hj + '"><b class="wp-code' + (p.code.length > 2 ? " is-long" : "") + '">' + esc(p.code) + '</b><b class="wp-title">' + esc(p.title) + "</b>" +
      '<span class="wp-foot">' + p.foot.map(function (x) { return "<span>" + esc(x) + "</span>"; }).join("") + "</span></div>";
  }
  function posters(site) {
    var list = [markHTML()];
    site.tabs.forEach(function (t) {
      list.push(posterHTML({
        hj: t.id,
        code: t.id === "grundlagen" ? "G" : t.kurz,
        title: t.id === "grundlagen" ? "Grundlagen" : String(t.titel).replace(/^Q\d:\s*/, ""),
        foot: t.themen.map(function (x) { return x.nr; })
      }));
    });
    var T = window.FeibiturTools && window.FeibiturTools.tools;
    if (T && T.length) {
      list.push(posterHTML({ hj: "tools", code: "Tools", title: T.length + " Vorbereitungs-Tools",
        foot: T.slice(0, 4).map(function (t) { return t.k || t.t; }).concat(["…"]) }));
    }
    return list;
  }

  function wender(host, site, pauseBtn) {
    var stage = host.querySelector(".wender-slats");
    if (!stage) return;
    var P = posters(site);
    if (reduced()) { stage.innerHTML = '<div class="wender-still">' + P[0] + "</div>"; if (pauseBtn) pauseBtn.hidden = true; return; }

    var slats = [], n = 0, step = 0, timer = null, busy = false, userPaused = false, inView = true, width = 0;
    function posterAt(k) { return k === 0 ? blankHTML() : P[(k - 1) % P.length]; }
    function count(w) { return w < 560 ? 6 : w < 900 ? 9 : 12; }

    function build() {
      width = stage.clientWidth;
      if (!width) return;
      n = count(width);
      var sw = width / n, d = sw / (2 * Math.sqrt(3));
      stage.innerHTML = "";
      slats = [];
      for (var i = 0; i < n; i++) {
        var slat = document.createElement("div");
        slat.className = "wender-slat";
        slat.style.left = (i * sw) + "px";
        slat.style.width = sw + "px";
        slat._d = d;
        slat.faces = [];
        for (var j = 0; j < 3; j++) {
          var f = document.createElement("div");
          f.className = "wender-face";
          f.style.transform = "rotateY(" + (j * 120) + "deg) translateZ(" + d + "px)";
          var clip = document.createElement("div");
          clip.className = "wp-clip";
          clip.style.width = width + "px";
          clip.style.left = (-i * sw) + "px";
          f.appendChild(clip);
          slat.appendChild(f);
          slat.faces.push(f);
        }
        slat.style.transform = "translateZ(" + (-d) + "px) rotateY(" + (-step * 120) + "deg)";
        stage.appendChild(slat);
        slats.push(slat);
      }
      fill(step % 3, posterAt(step));
      fill((step + 1) % 3, posterAt(step + 1));
    }
    function fill(face, html) { slats.forEach(function (s) { s.faces[face].firstChild.innerHTML = html; }); }

    function turn() {
      timer = null;
      if (!host.isConnected) return stop();
      if (userPaused || !inView || document.hidden || busy) return;
      busy = true;
      var from = step, to = step + 1, last = null;
      slats.forEach(function (s, i) {
        var a = s.animate([
          { transform: "translateZ(" + (-s._d) + "px) rotateY(" + (-from * 120) + "deg)" },
          { transform: "translateZ(" + (-s._d) + "px) rotateY(" + (-to * 120) + "deg)" }
        ], { duration: TURN, delay: i * STAGGER, easing: EASE, fill: "forwards" });
        [s.faces[from % 3], s.faces[to % 3]].forEach(function (f) {
          f.animate([{ filter: "brightness(1)" }, { filter: "brightness(.72)" }, { filter: "brightness(1)" }], { duration: TURN, delay: i * STAGGER, easing: "ease-in-out" });
        });
        last = a;
        a.onfinish = function () { s.style.transform = "translateZ(" + (-s._d) + "px) rotateY(" + (-to * 120) + "deg)"; a.cancel(); };
      });
      last.addEventListener("finish", function () {
        step = to;
        fill((step + 1) % 3, posterAt(step + 1)); // die Seite, die gerade hinten steht, bekommt das nächste Plakat
        busy = false;
        if (Math.abs(stage.clientWidth - width) > 1) build();
        schedule(HOLD);
      });
    }
    function schedule(ms) { clearTimeout(timer); timer = null; if (!userPaused && inView && !document.hidden) timer = setTimeout(turn, ms); }
    function stop() { clearTimeout(timer); timer = null; if (io) io.disconnect(); if (ro) ro.disconnect(); document.removeEventListener("visibilitychange", onVis); }
    function onVis() { if (!host.isConnected) return stop(); if (document.hidden) { clearTimeout(timer); timer = null; } else if (!busy) schedule(1200); }

    build();
    var io = "IntersectionObserver" in window ? new IntersectionObserver(function (e) {
      inView = e[0].isIntersecting;
      if (!inView) { clearTimeout(timer); timer = null; } else if (!busy && !timer) schedule(step === 0 ? FIRST : 1200);
    }, { threshold: 0.25 }) : null;
    if (io) io.observe(host);
    var ro = "ResizeObserver" in window ? new ResizeObserver(function () { if (!busy && Math.abs(stage.clientWidth - width) > 1) build(); }) : null;
    if (ro) ro.observe(stage);
    document.addEventListener("visibilitychange", onVis);
    if (!io) schedule(FIRST);

    if (pauseBtn) {
      pauseBtn.hidden = false;
      pauseBtn.addEventListener("click", function () {
        userPaused = !userPaused;
        pauseBtn.setAttribute("aria-pressed", String(userPaused));
        pauseBtn.querySelector("span").textContent = userPaused ? "Plakatwand weiterdrehen" : "Plakatwand anhalten";
        pauseBtn.classList.toggle("is-paused", userPaused);
        if (userPaused) { clearTimeout(timer); timer = null; } else if (!busy) schedule(400);
      });
    }
  }

  window.FeibiturMotion = { wender: wender, reduced: reduced, markHTML: markHTML };
})();
