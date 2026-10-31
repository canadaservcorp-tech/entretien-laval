/* "Petit nettoyeur": a cartoon cleaner who walks to the buttons on screen, climbs a small ladder and wipes them with a rag. */
(function () {
  if (!window.requestAnimationFrame || !document.querySelector) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  try { if (localStorage.getItem('el-mascot-off') === '1') return; } catch (e) {}
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var H = innerWidth < 600 ? 82 : 100, W = Math.round(H * 0.7), SPEED = 150;
  var svg = '<svg viewBox="0 0 80 114" aria-hidden="true"><g fill="none" stroke="#0F2A44" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
    + '<g class="m-leg l"><path d="M29 78v24M36 78v24"/><path d="M24 109v-4q0-3 3-3h10q3 0 3 3v4z"/></g>'
    + '<g class="m-leg r"><path d="M44 78v24M51 78v24"/><path d="M40 109v-4q0-3 3-3h10q3 0 3 3v4z"/></g>'
    + '<rect x="22" y="46" width="36" height="32" rx="10"/><rect x="29" y="52" width="22" height="13" rx="3"/><path d="M33 46v6M47 46v6"/>'
    + '<circle cx="40" cy="30" r="17"/>'
    + '<g class="m-front"><circle cx="34" cy="30" r="2.4" fill="#0F2A44" stroke="none"/><circle cx="46" cy="30" r="2.4" fill="#0F2A44" stroke="none"/><path d="M39 33q1.5 3 3 0"/><path d="M33 40q7-5 14 0"/><path d="M29 25l8 3.5M51 25l-8 3.5" stroke-width="3"/></g>'
    + '<g class="m-side"><circle cx="49" cy="30" r="2.4" fill="#0F2A44" stroke="none"/><path d="M44 25l9 3" stroke-width="3"/><path d="M56 30q5 2 1 5"/><path d="M47 40q4-3 8-1"/><path d="M28 27q-4 3 0 7"/></g>'
    + '<g class="m-steam" stroke="#9FB6CC" stroke-width="1.5"><circle cx="16" cy="14" r="4"/><circle cx="10" cy="7" r="3"/><circle cx="64" cy="10" r="3.5"/></g>'
    + '<path d="M22 24q18-20 36 0z"/><rect x="38" y="20" width="26" height="5" rx="2.5"/>'
    + '<g class="m-arm"><path d="M58 50h12M58 58h12"/><circle cx="72" cy="54" r="4.5"/>'
    + '<path d="M65 40q16-6 19 9q3 15-12 18q-13 2-14-12z" fill="#E94F64" stroke="#B5283E"/><path d="M68 45l13 6M67 54l13 5M69 61l9 2" stroke="#F7C948" stroke-width="2.4"/></g>'
    + '</g></svg>';
  var m = document.createElement('div'); m.className = 'mascot'; m.style.width = W + 'px'; m.style.height = H + 'px';
  m.innerHTML = '<div class="m-body">' + svg + '<div class="m-carry"></div></div><button type="button" class="m-close" aria-label="' + (fr ? 'Cacher le petit nettoyeur' : 'Hide the little cleaner') + '">×</button>';
  var lad = document.createElement('div'); lad.className = 'm-ladder';
  document.body.appendChild(lad); document.body.appendChild(m);
  var body = m.firstChild, x = 16, y = 0, run = 0, last = null;
  var RUNG = Math.round(H * 0.2), FOOT = H * 110 / 114;
  m.style.setProperty('--ru', (RUNG * 114 / H).toFixed(2));
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
  // rung by rung: one foot moves to the next rung, then the body follows while the other foot moves up; feet always land on a rung
  async function climb(ty, id) {
    m.style.setProperty('--dir', y > ty ? -1 : 1);
    body.classList.add('climb');
    await wait(240);
    while (Math.abs(y - ty) > 0.5) {
      if (id !== run) break;
      body.classList.toggle('rung');
      var ny = y > ty ? Math.max(ty, y - RUNG) : Math.min(ty, y + RUNG);
      if (!(await tween(x, ny, 240, id))) { body.classList.remove('climb', 'rung'); return false; }
      await wait(90);
    }
    body.classList.remove('climb', 'rung');
    await wait(200);
    return id === run;
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
  function dist(e) { var r = e.getBoundingClientRect(); return Math.abs(r.left - x) + (innerHeight - r.bottom) * 1.5; }
  async function cycle() {
    var id = ++run, b = null, r;
    if (pending) {
      b = pending.el; r = b ? b.getBoundingClientRect() : { left: pending.x - 30, right: pending.x + 30, top: pending.y - 14, height: 28, width: 60 };
      pending = null;
    } else {
      var list = targets();
      if (list.length) {
        // right after a scroll he grabs the closest thing to clean; otherwise any visible one
        if (justScrolled) list.sort(function (a, c) { return dist(a) - dist(c); });
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
    if (Math.abs(tx - x) > 2) body.classList.toggle('flip', tx < x);
    body.classList.add('walk', 'carry');
    if (!(await tween(tx, fy, Math.abs(tx - x) / SPEED * 1000, id))) return;
    body.classList.remove('walk', 'carry');
    body.classList.toggle('flip', !left);
    var k = Math.round((fy - ty) / RUNG);
    if (k >= 2) {
      ty = fy - k * RUNG;
      var lt = ty + H * 0.45, lb = fy + FOOT + 3;
      lad.style.left = Math.round(tx + W * 0.27) + 'px'; lad.style.width = Math.round(W * 0.46) + 'px';
      lad.style.top = lt + 'px'; lad.style.height = (lb - lt) + 'px';
      lad.style.backgroundImage = 'repeating-linear-gradient(to top,#C98A4B 0 3px,transparent 3px ' + RUNG + 'px)';
      lad.classList.add('on');
      await wait(350);
      if (!(await climb(ty, id))) return;
    }
    body.classList.add('wipe'); if (b) b.classList.add('m-clean'); sparkle(r);
    await wait(1500);
    body.classList.remove('wipe'); if (b) b.classList.remove('m-clean');
    if (id !== run) return;
    if (y < fy - 1 && !(await climb(fy, id))) return;
    lad.classList.remove('on');
    await wait(150);
  }
  var scrolled = 0, lastY = scrollY;
  function reset() {
    run++; lad.classList.remove('on'); body.classList.remove('wipe', 'climb', 'rung');
    document.querySelectorAll('.m-clean').forEach(function (e) { e.classList.remove('m-clean'); });
  }
  // the visitor scrolls: he runs along with them, ladder on his shoulder
  addEventListener('scroll', function () {
    var d = scrollY - lastY; lastY = scrollY; scrolled = Date.now(); justScrolled = true;
    reset(); body.classList.add('walk', 'carry');
    if (Math.abs(d) > 2) body.classList.toggle('flip', d < 0);
    x = Math.max(4, Math.min(x + (d > 0 ? 0.75 : -0.75), innerWidth - W - 4));
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
