/* "Petit nettoyeur": a cartoon cleaner who walks to the buttons on screen, climbs a small ladder and wipes them with a rag. */
(function () {
  if (!window.requestAnimationFrame || !document.querySelector) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  try { if (localStorage.getItem('el-mascot-off') === '1') return; } catch (e) {}
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var H = innerWidth < 600 ? 82 : 100, W = Math.round(H * 0.7), SPEED = 150;
  var svg = '<svg viewBox="0 0 80 114" aria-hidden="true"><g fill="none" stroke="#0F2A44" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'
    + '<g class="m-leg l"><path d="M39 72L32 90L30 108M30 108h-6"/></g>'
    + '<g class="m-leg r"><path d="M41 72L47 90L50 108M50 108h6"/></g>'
    + '<path d="M40 38L40 72"/><path d="M40 46L31 58L28 70"/>'
    + '<circle cx="40" cy="27" r="11"/>'
    + '<g class="m-front"><circle cx="36" cy="27" r="1.6" fill="#0F2A44" stroke="none"/><circle cx="44" cy="27" r="1.6" fill="#0F2A44" stroke="none"/><path d="M33 22l5 2.5M47 22l-5 2.5" stroke-width="2.2"/><path d="M36 33q4-3 8 0" stroke-width="2"/></g>'
    + '<g class="m-side"><circle cx="46" cy="26" r="1.6" fill="#0F2A44" stroke="none"/><path d="M42 21.5l6 2.5" stroke-width="2.2"/><path d="M51 27l2 2.5l-2 .5" stroke-width="2"/><path d="M44 33q3-2 6-1" stroke-width="2"/></g>'
    + '<g class="m-steam" stroke="#9FB6CC" stroke-width="1.5"><circle cx="22" cy="12" r="3.5"/><circle cx="16" cy="6" r="2.5"/><circle cx="60" cy="9" r="3"/></g>'
    + '<g class="m-arm"><path d="M40 46L53 52L64 54"/>'
    + '<path d="M58 42q16-6 19 9q3 15-12 18q-13 2-14-12z" fill="#E94F64" stroke="#B5283E" stroke-width="2"/><path d="M61 47l13 6M60 56l13 5M62 63l9 2" stroke="#F7C948" stroke-width="2.4"/></g>'
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
