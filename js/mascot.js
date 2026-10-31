/* "Petit nettoyeur": a cartoon cleaner who walks to the buttons on screen, climbs a small ladder and wipes them with a rag. */
(function () {
  if (!window.requestAnimationFrame || !document.querySelector) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  try { if (localStorage.getItem('el-mascot-off') === '1') return; } catch (e) {}
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var H = innerWidth < 600 ? 82 : 100, W = Math.round(H * 0.8), SPEED = 300;
  var svg = '<svg viewBox="0 0 80 100" aria-hidden="true">'
    + '<g class="m-leg l"><rect x="28" y="72" width="9" height="20" rx="4" fill="#0E4C82"/><rect x="25" y="88" width="15" height="7" rx="3.5" fill="#0F2A44"/></g>'
    + '<g class="m-leg r"><rect x="43" y="72" width="9" height="20" rx="4" fill="#0E4C82"/><rect x="41" y="88" width="15" height="7" rx="3.5" fill="#0F2A44"/></g>'
    + '<rect x="22" y="46" width="36" height="32" rx="10" fill="#1E7FC0"/><rect x="29" y="52" width="22" height="14" rx="3" fill="#1565A8"/>'
    + '<circle cx="40" cy="30" r="17" fill="#F6CFA8"/><circle cx="34" cy="30" r="2.6" fill="#0F2A44"/><circle cx="46" cy="30" r="2.6" fill="#0F2A44"/>'
    + '<path d="M33 40q7-5 14 0" stroke="#0F2A44" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M29 25l8 3.5M51 25l-8 3.5" stroke="#0F2A44" stroke-width="3" stroke-linecap="round"/><g class="m-steam" fill="#fff" stroke="#9FB6CC" stroke-width="1.5"><circle cx="16" cy="14" r="4"/><circle cx="10" cy="7" r="3"/><circle cx="64" cy="10" r="3.5"/></g><circle cx="29" cy="35" r="3" fill="#F2A0A0" opacity=".7"/><circle cx="51" cy="35" r="3" fill="#F2A0A0" opacity=".7"/>'
    + '<path d="M22 24q18-20 36 0z" fill="#1565A8"/><rect x="38" y="20" width="26" height="5" rx="2.5" fill="#1565A8"/>'
    + '<g class="m-arm"><rect x="52" y="50" width="20" height="8" rx="4" fill="#1E7FC0"/><circle cx="72" cy="54" r="5" fill="#F6CFA8"/>'
    + '<path d="M68 44q10-4 12 6q2 10-8 12q-8 1-9-8z" fill="#E94F64"/><path d="M70 47l8 4M69 53l8 3" stroke="#F7C948" stroke-width="2"/></g>'
    + '</svg>';
  var m = document.createElement('div'); m.className = 'mascot'; m.style.width = W + 'px'; m.style.height = H + 'px';
  m.innerHTML = '<div class="m-body">' + svg + '<div class="m-carry"></div></div><button type="button" class="m-close" aria-label="' + (fr ? 'Cacher le petit nettoyeur' : 'Hide the little cleaner') + '">×</button>';
  var lad = document.createElement('div'); lad.className = 'm-ladder';
  document.body.appendChild(lad); document.body.appendChild(m);
  var body = m.firstChild, x = 16, y = 0, run = 0, last = null;
  var floor = function () { return innerHeight - H - 6; };
  var place = function () { m.style.transform = 'translate(' + x + 'px,' + y + 'px)'; };
  y = floor(); place();
  m.querySelector('.m-close').addEventListener('click', function () {
    run = -1; m.remove(); lad.remove(); try { localStorage.setItem('el-mascot-off', '1'); } catch (e) {}
  });
  var wait = function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); };
  function tween(tx, ty, ms, id) {
    return new Promise(function (res) {
      var sx = x, sy = y, t0 = performance.now();
      (function step(now) {
        if (id !== run) return res(false);
        var k = Math.min(1, (now - t0) / Math.max(ms, 1));
        x = sx + (tx - sx) * k; y = sy + (ty - sy) * k; place();
        k < 1 ? requestAnimationFrame(step) : res(true);
      })(t0);
    });
  }
  function sparkle(r) {
    for (var i = 0; i < 4; i++) {
      var s = document.createElement('span'); s.className = 'm-spark'; s.textContent = '✦';
      s.style.left = (r.left + Math.random() * r.width) + 'px'; s.style.top = (r.top + Math.random() * r.height) + 'px';
      s.style.animationDelay = (i * 120) + 'ms'; document.body.appendChild(s);
      setTimeout(function (el) { el.remove(); }.bind(null, s), 1400);
    }
  }
  function targets() {
    var top = 80, bot = innerHeight - 10;
    return [].filter.call(document.querySelectorAll('main .btn, section .btn, .qform .btn, .chip, .prod, .card, .jstep, main h2, main h3, main img, main th'), function (b) {
      var r = b.getBoundingClientRect();
      return r.width > 0 && r.height < 260 && r.top > top && r.bottom < bot && b !== last;
    });
  }
  var pending = null, justScrolled = false;
  async function cycle() {
    var id = ++run, b = null, r;
    if (pending) {
      b = pending.el; r = b ? b.getBoundingClientRect() : { left: pending.x - 30, right: pending.x + 30, top: pending.y - 14, height: 28, width: 60 };
      pending = null;
    } else {
      var list = targets();
      if (list.length) {
        // right after a scroll he grabs the closest thing to clean; otherwise any visible one
        if (justScrolled) list.sort(function (a, c) { return Math.abs(a.getBoundingClientRect().left - x) - Math.abs(c.getBoundingClientRect().left - x); });
        b = justScrolled ? list[0] : list[Math.floor(Math.random() * list.length)]; last = b; r = b.getBoundingClientRect();
      } else {
        var sx = 40 + Math.random() * (innerWidth - 80), sy = innerHeight * (0.3 + Math.random() * 0.3);
        r = { left: sx - 30, right: sx + 30, top: sy - 14, height: 28, width: 60 };
      }
      justScrolled = false;
    }
    var left = r.left > W + 10;
    var tx = left ? r.left - W + 6 : Math.min(r.right - 6, innerWidth - W - 4);
    var ty = r.top + r.height / 2 - H * 0.5, fy = floor();
    body.classList.toggle('flip', !left);
    body.classList.add('walk', 'carry');
    if (!(await tween(tx, fy, Math.abs(tx - x) / SPEED * 1000, id))) return;
    body.classList.remove('walk', 'carry');
    if (fy - ty > 30) {
      lad.style.left = (tx + W * 0.2) + 'px'; lad.style.width = Math.round(W * 0.38) + 'px'; lad.style.top = (ty + H * 0.9) + 'px';
      lad.style.height = (fy - ty) + 'px'; lad.classList.add('on');
      await wait(350);
      body.classList.add('walk');
      if (!(await tween(tx, ty, (fy - ty) / 140 * 1000, id))) return;
      body.classList.remove('walk');
    }
    body.classList.add('wipe'); if (b) b.classList.add('m-clean'); sparkle(r);
    await wait(1500);
    body.classList.remove('wipe'); if (b) b.classList.remove('m-clean');
    if (id !== run) return;
    if (y < fy - 1) {
      body.classList.add('walk');
      if (!(await tween(tx, fy, (fy - y) / 220 * 1000, id))) return;
      body.classList.remove('walk');
    }
    lad.classList.remove('on');
    await wait(150);
  }
  var scrolled = 0, lastY = scrollY;
  function reset() {
    run++; lad.classList.remove('on'); body.classList.remove('wipe');
    document.querySelectorAll('.m-clean').forEach(function (e) { e.classList.remove('m-clean'); });
  }
  // the visitor scrolls: he runs along with them, ladder on his shoulder
  addEventListener('scroll', function () {
    var d = scrollY - lastY; lastY = scrollY; scrolled = Date.now(); justScrolled = true;
    reset(); body.classList.add('walk', 'carry');
    if (Math.abs(d) > 2) body.classList.toggle('flip', d < 0);
    x = Math.max(4, Math.min(x + (d > 0 ? 1.5 : -1.5), innerWidth - W - 4));
    y = floor() - Math.min(26, Math.abs(d) * 0.35); place();
  }, { passive: true });
  // the visitor clicks: he goes there and cleans that spot
  document.addEventListener('click', function (e) {
    if (m.contains(e.target)) return;
    var b = e.target.closest && e.target.closest('.btn, button, .chip, .prod, .card, .jstep');
    pending = { x: e.clientX, y: e.clientY, el: b && b.getBoundingClientRect().height < 260 ? b : null };
    reset(); scrolled = 0;
  }, true);
  addEventListener('resize', function () { y = floor(); place(); });
  (async function loop() {
    await wait(500);
    while (run >= 0) {
      if (Date.now() - scrolled < 600 || document.hidden) { await wait(150); continue; }
      if (y < floor() - 1 && !lad.classList.contains('on')) { body.classList.add('walk', 'carry'); await tween(x, floor(), 250, ++run); }
      body.classList.remove('walk', 'carry');
      await cycle(); await wait(50);
    }
  })();
})();
