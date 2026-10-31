/* "Petit nettoyeur": a cartoon cleaner who walks to the buttons on screen, climbs a small ladder and wipes them with a rag. */
(function () {
  if (!window.requestAnimationFrame || !document.querySelector) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  try { if (localStorage.getItem('el-mascot-off') === '1') return; } catch (e) {}
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var H = innerWidth < 600 ? 82 : 100, W = Math.round(H * 0.7), SPEED = 150;
  var svg = '<svg viewBox="0 0 80 114" aria-hidden="true"><defs>'
    + '<radialGradient id="mg-skin" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#FFE6CC"/><stop offset=".55" stop-color="#F6CFA8"/><stop offset="1" stop-color="#D49A6E"/></radialGradient>'
    + '<radialGradient id="mg-suit" cx=".35" cy=".25" r=".9"><stop offset="0" stop-color="#5DB3EE"/><stop offset=".5" stop-color="#1E7FC0"/><stop offset="1" stop-color="#0B4F86"/></radialGradient>'
    + '<linearGradient id="mg-leg" x1="0" x2="1"><stop offset="0" stop-color="#2A7BC0"/><stop offset=".45" stop-color="#0E4C82"/><stop offset="1" stop-color="#062F55"/></linearGradient>'
    + '<radialGradient id="mg-hat" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#3A93D8"/><stop offset=".6" stop-color="#1565A8"/><stop offset="1" stop-color="#0A3F72"/></radialGradient>'
    + '<radialGradient id="mg-rag" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FF8A9A"/><stop offset="1" stop-color="#C23A50"/></radialGradient></defs>'
    + '<ellipse class="m-shadow" cx="40" cy="110" rx="24" ry="3.5" fill="#0F2A44" opacity=".22"/>'
    + '<g class="m-leg l"><rect x="28" y="72" width="9" height="34" rx="4" fill="url(#mg-leg)"/><rect x="24" y="102" width="17" height="8" rx="4" fill="#0F2A44"/><rect x="26" y="103" width="8" height="2" rx="1" fill="#fff" opacity=".25"/></g>'
    + '<g class="m-leg r"><rect x="43" y="72" width="9" height="34" rx="4" fill="url(#mg-leg)"/><rect x="40" y="102" width="17" height="8" rx="4" fill="#0F2A44"/><rect x="42" y="103" width="8" height="2" rx="1" fill="#fff" opacity=".25"/></g>'
    + '<rect x="22" y="46" width="36" height="32" rx="10" fill="url(#mg-suit)"/><rect x="29" y="52" width="22" height="14" rx="3" fill="#1565A8" opacity=".85"/><ellipse cx="31" cy="51" rx="6" ry="3" fill="#fff" opacity=".22"/>'
    + '<circle cx="40" cy="30" r="17" fill="url(#mg-skin)"/><ellipse cx="34" cy="22" rx="6" ry="3.5" fill="#fff" opacity=".3"/>'
    + '<g class="m-face"><circle cx="34" cy="30" r="2.6" fill="#0F2A44"/><circle cx="46" cy="30" r="2.6" fill="#0F2A44"/><circle cx="35" cy="29" r=".9" fill="#fff"/><circle cx="47" cy="29" r=".9" fill="#fff"/>'
    + '<ellipse cx="40.5" cy="34.5" rx="2.6" ry="2" fill="#E3A57A"/>'
    + '<path d="M33 40q7-5 14 0" stroke="#0F2A44" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M29 25l8 3.5M51 25l-8 3.5" stroke="#0F2A44" stroke-width="3" stroke-linecap="round"/><circle cx="29" cy="35" r="3" fill="#F2A0A0" opacity=".7"/><circle cx="51" cy="35" r="3" fill="#F2A0A0" opacity=".7"/></g>'
    + '<g class="m-steam" fill="#fff" stroke="#9FB6CC" stroke-width="1.5"><circle cx="16" cy="14" r="4"/><circle cx="10" cy="7" r="3"/><circle cx="64" cy="10" r="3.5"/></g>'
    + '<path d="M22 24q18-20 36 0z" fill="url(#mg-hat)"/><rect x="38" y="20" width="26" height="5" rx="2.5" fill="#0E528F"/>'
    + '<g class="m-arm"><rect x="52" y="50" width="20" height="8" rx="4" fill="url(#mg-suit)"/><circle cx="72" cy="54" r="5" fill="url(#mg-skin)"/>'
    + '<path d="M68 44q10-4 12 6q2 10-8 12q-8 1-9-8z" fill="url(#mg-rag)"/><path d="M70 47l8 4M69 53l8 3" stroke="#F7C948" stroke-width="2"/></g>'
    + '</svg>';
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
