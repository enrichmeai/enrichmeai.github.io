/* Well Rounded Engineer: copy buttons, search on this page, and matches on the other pages.
   The search index (search.json) is fetched only when someone starts typing. */
(function () {
  "use strict";
  var BASE = "/well-rounded-engineer/";
  var here = document.body.dataset.tab;
  var q = document.getElementById("q");
  var empty = document.getElementById("empty");
  var elsewhere = document.getElementById("elsewhere");
  var cards = Array.prototype.slice.call(document.querySelectorAll("main .card"));

  // copy buttons on every snippet
  document.querySelectorAll(".snip").forEach(function (s) {
    var b = document.createElement("button");
    b.className = "copy"; b.type = "button"; b.textContent = "Copy";
    b.addEventListener("click", function () {
      var pre = s.querySelector("pre");
      var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1200); };
      var select = function () {
        var r = document.createRange(); r.selectNodeContents(pre);
        var sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(pre.innerText).then(done, select);
      else select();
    });
    s.appendChild(b);
  });

  // keep the current section's link in view in the scrolling tab row
  // (scroll only the tab row, never the page; again once fonts have loaded and widths have settled)
  var cur = document.querySelector('.eg-bar nav a[aria-current="page"]');
  function centre() {
    if (!cur) return;
    var nav = cur.parentElement;
    if (nav.scrollWidth > nav.clientWidth) nav.scrollLeft = cur.offsetLeft - nav.offsetLeft - (nav.clientWidth - cur.offsetWidth) / 2;
  }
  centre();
  window.addEventListener("load", centre);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(centre);

  var index = null, loading = null;
  function load() {
    if (!loading) {
      loading = fetch(BASE + "search.json").then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.json();
      }).then(function (d) { index = d; }, function () { index = "unavailable"; });
    }
    return loading;
  }

  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }

  function showElsewhere(term) {
    elsewhere.textContent = "";
    if (index === "unavailable") {
      elsewhere.appendChild(el("p", "note", "Search across the other pages could not load; this page is still filtered."));
      elsewhere.hidden = false; return;
    }
    var found = [];
    index.forEach(function (p) {
      if (p.t === here) return;
      var hits = p.c.filter(function (c) { return c.x.indexOf(term) >= 0; });
      if (hits.length) found.push([p, hits]);
    });
    if (!found.length) { elsewhere.hidden = true; return; }
    elsewhere.appendChild(el("h2", null, "On other pages"));
    var ul = el("ul");
    found.forEach(function (f) {
      var li = el("li");
      var a = el("a", null, f[0].l);
      a.href = f[0].u + "?q=" + encodeURIComponent(term);
      li.appendChild(a);
      li.appendChild(el("span", "lnote", " · " + f[1].slice(0, 3).map(function (c) { return c.h; }).join(" · ") + (f[1].length > 3 ? " · and " + (f[1].length - 3) + " more" : "")));
      ul.appendChild(li);
    });
    elsewhere.appendChild(ul);
    elsewhere.hidden = false;
  }

  function render() {
    var term = q.value.trim().toLowerCase();
    var hits = 0;
    cards.forEach(function (c) {
      var m = !term || c.textContent.toLowerCase().indexOf(term) >= 0;
      c.hidden = !m; if (m) hits++;
    });
    empty.hidden = !term || hits > 0;
    if (!term) { elsewhere.hidden = true; elsewhere.textContent = ""; return; }
    load().then(function () { if (q.value.trim().toLowerCase() === term) showElsewhere(term); });
  }

  q.addEventListener("input", render);
  var start = new URLSearchParams(location.search).get("q");
  if (start) { q.value = start; render(); }
})();
