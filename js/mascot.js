/* "Petit nettoyeur": a cartoon cleaner who walks to the buttons on screen, climbs a small ladder and wipes them with a rag. */
(function () {
  if (!window.requestAnimationFrame || !document.querySelector) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  try { if (localStorage.getItem('el-mascot-off') === '1') return; } catch (e) {}
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var H = innerWidth < 600 ? 164 : 200, W = Math.round(H * 0.7), SPEED = 150;
  var svg = '<svg viewBox="0 0 80 114" aria-hidden="true"><g fill="none" stroke="#0F2A44" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
    + '<g class="m-leg l"><g class="m-th"><path d="M39 72L37 90"/><g class="m-sh"><path d="M37 90L37 108"/><g class="m-ft"><path d="M37 108h7"/></g></g></g></g>'
    + '<g class="m-leg r"><g class="m-th"><path d="M41 72L43 90"/><g class="m-sh"><path d="M43 90L43 108"/><g class="m-ft"><path d="M43 108h7"/></g></g></g></g>'
    + '<path d="M40 38V48"/><g class="m-belly"><ellipse cx="41" cy="60" rx="10.5" ry="12.5"/><circle cx="43" cy="61" r=".9" fill="#0F2A44" stroke="none"/></g><g class="m-arm2"><path d="M40 46L29 57"/><g class="m-fa"><path d="M29 57L28 69"/></g></g>'
    + '<circle cx="40" cy="27" r="11"/>'
    + '<g class="m-front"><circle cx="36" cy="27" r="1.6" fill="#0F2A44" stroke="none"/><circle cx="44" cy="27" r="1.6" fill="#0F2A44" stroke="none"/><path d="M33 22l5 2.5M47 22l-5 2.5" stroke-width="2.2"/><path class="m-mouth" d="M36 33q4-3 8 0" stroke-width="2"/><ellipse class="m-oh" cx="40" cy="33" rx="2.2" ry="2.8" stroke-width="1.6"/></g>'
    + '<g class="m-fear"><circle cx="35.5" cy="27" r="3.2" fill="#fff"/><circle cx="44.5" cy="27" r="3.2" fill="#fff"/><circle cx="35.8" cy="27.6" r="1.1" fill="#0F2A44" stroke="none"/><circle cx="44.2" cy="27.6" r="1.1" fill="#0F2A44" stroke="none"/><path d="M31.5 22l5-2.5M48.5 22l-5-2.5" stroke-width="2"/><ellipse cx="40" cy="34" rx="2.4" ry="3" stroke-width="1.6"/>'
    + '<g class="m-sweat" fill="#7CC4F0" stroke="#3E8FC9" stroke-width="1"><path d="M53 20q2 3 0 5q-2-2 0-5z"/><path d="M27 24q2 3 0 5q-2-2 0-5z"/></g></g>'
    + '<g class="m-relax"><path d="M33.5 25.8h5M41.5 25.8h5" stroke-width="1.8"/><circle cx="36" cy="27.4" r="1.2" fill="#0F2A44" stroke="none"/><circle cx="44" cy="27.4" r="1.2" fill="#0F2A44" stroke="none"/><path d="M37 33.5q3.5 1.5 7-1.2" stroke-width="1.8"/></g>'
    + '<g class="m-sleep"><path d="M33.5 27q2.5 2 5 0M41.5 27q2.5 2 5 0" stroke-width="1.8"/><ellipse cx="40.5" cy="33.5" rx="1.4" ry="1.1" stroke-width="1.4"/></g>'
    + '<g class="m-zzz" fill="#1E7FC0" stroke="none" font-family="Arial,sans-serif" font-weight="700"><text x="51" y="18" font-size="11">Z</text><text x="60" y="10" font-size="8.5">z</text><text x="67" y="4" font-size="6.5">z</text></g>'
    + '<g class="m-side"><circle cx="46" cy="26" r="1.6" fill="#0F2A44" stroke="none"/><path d="M42 21.5l6 2.5" stroke-width="2.2"/><path d="M51 27l2 2.5l-2 .5" stroke-width="2"/><path d="M44 33q3-2 6-1" stroke-width="2"/></g>'
    + '<g class="m-hat"><path d="M29.5 18q0-11 10.5-11q10.5 0 10.5 11z"/><path d="M27 18h31"/><path d="M33 13.5q7-2.5 14 0" stroke-width="1.4"/></g>'
    + '<g class="m-steam" stroke="#9FB6CC" stroke-width="1.5"><circle cx="22" cy="12" r="3.5"/><circle cx="16" cy="6" r="2.5"/><circle cx="60" cy="9" r="3"/></g>'
    + '<g class="m-arm"><path d="M40 46L53 52L64 54"/>'
    + '<g class="m-rag"><path d="M60.5 51q4.5-4 9.5 0q2 3 4 7q4 8 3.5 18l-2.6-1.6-1.6 3-2.6-1.8-1.8 3-2.6-2-1.8 3-2.4-2.2-2 2.6q-2.5-9-.6-17q1-4 1.8-9.6z" fill="#E94F64" stroke="#B5283E" stroke-width="1.6"/>'
    + '<path d="M64 56q-1.5 9 .5 18M68 55q3 8 3 17M61.5 61q2 5 1 10" stroke="#B5283E" stroke-width="1.1"/><path d="M62 58l11 3M61.5 66l13 2" stroke="#F7C948" stroke-width="1.8"/>'
    + '<path d="M60 50q5-4 11 0q-1 3-5.5 3q-4.5 0-5.5-3z" fill="#D63F55" stroke="#B5283E" stroke-width="1.4"/></g><circle cx="65" cy="52" r="3.2" fill="#fff"/></g>'
    + '</g></svg>';
  var m = document.createElement('div'); m.className = 'mascot'; m.style.width = W + 'px'; m.style.height = H + 'px';
  m.innerHTML = '<div class="m-body">' + svg + '<div class="m-carry"></div></div><button type="button" class="m-close" aria-label="' + (fr ? 'Cacher le petit nettoyeur' : 'Hide the little cleaner') + '">×</button><button type="button" class="m-snd" aria-label="' + (fr ? 'Son du petit nettoyeur' : 'Little cleaner sound') + '">♪</button>';
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
  // glass-wiping squeak made with Web Audio (no file); browsers only allow sound after the visitor taps or clicks once
  var ac = null, snd = true;
  try { snd = localStorage.getItem('el-mascot-sound') !== '0'; } catch (e) {}
  var sb = m.querySelector('.m-snd'); sb.classList.toggle('off', !snd); sb.setAttribute('aria-pressed', snd);
  function unlock() {
    var A = window.AudioContext || window.webkitAudioContext;
    if (!A) return;
    try { if (!ac) ac = new A(); if (ac.state === 'suspended') ac.resume(); } catch (e) {}
  }
  addEventListener('pointerdown', unlock, true); addEventListener('keydown', unlock, true);
  sb.addEventListener('click', function () {
    snd = !snd; sb.classList.toggle('off', !snd); sb.setAttribute('aria-pressed', snd);
    try { localStorage.setItem('el-mascot-sound', snd ? '1' : '0'); } catch (e) {}
  });
  function squeak(ms) {
    if (!snd || !ac || ac.state !== 'running') return;
    var t = ac.currentTime + 0.02, n = Math.floor(ms / 280);
    for (var i = 0; i < n; i++) {
      var o = ac.createOscillator(), v = ac.createOscillator(), vg = ac.createGain(), g = ac.createGain(), s0 = t + i * 0.28 + Math.random() * 0.03, d = 0.11 + Math.random() * 0.05, f = 1500 + Math.random() * 500;
      o.type = 'triangle'; o.frequency.setValueAtTime(f, s0); o.frequency.linearRampToValueAtTime(f * (i % 2 ? 0.8 : 1.35), s0 + d);
      v.frequency.value = 38; vg.gain.value = 90; v.connect(vg); vg.connect(o.frequency);
      g.gain.setValueAtTime(0, s0); g.gain.linearRampToValueAtTime(0.045, s0 + 0.02); g.gain.linearRampToValueAtTime(0.03, s0 + d - 0.03); g.gain.linearRampToValueAtTime(0, s0 + d);
      o.connect(g); g.connect(ac.destination);
      o.start(s0); v.start(s0); o.stop(s0 + d + 0.02); v.stop(s0 + d + 0.02);
    }
  }
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
  var pending = null, justScrolled = false, drag = null, active = Date.now(), IDLE = 20000;
  // nobody scrolls or clicks for a while: he walks to the closest bottom corner, sits, swings his legs, then dozes off
  async function rest() {
    var id = ++run, cx = x + W / 2 < innerWidth / 2 ? 4 : innerWidth - W - 4;
    if (Math.abs(cx - x) > 2) body.classList.toggle('flip', cx < x);
    body.classList.add('walk', 'carry');
    if (!(await tween(cx, floor(), Math.abs(cx - x) / SPEED * 1000, id))) return;
    body.classList.remove('walk', 'carry');
    body.classList.toggle('flip', cx > innerWidth / 2);
    body.classList.add('rest');
    var t0 = Date.now();
    while (id === run) {
      if (Date.now() - t0 > 7000) body.classList.add('sleep');
      await wait(200);
    }
  }
  function wake() {
    active = Date.now();
    if (!body.classList.contains('rest')) return;
    body.classList.remove('rest', 'sleep'); body.classList.add('wake');
    setTimeout(function () { body.classList.remove('wake'); }, 450);
  }
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
    body.classList.add('wipe'); if (b) b.classList.add('m-clean'); sparkle(r); squeak(1500);
    await wait(1500);
    body.classList.remove('wipe'); if (b) b.classList.remove('m-clean');
    if (id !== run) return;
    if (y < fy - 1 && !(await climb(fy, id))) return;
    lad.classList.remove('on');
    await wait(150);
  }
  var scrolled = 0, lastY = scrollY;
  function reset() {
    run++; wake(); lad.classList.remove('on'); body.classList.remove('wipe', 'climb', 'rung');
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
  addEventListener('keydown', function () { active = Date.now(); }, true);
  addEventListener('resize', function () { y = floor(); place(); });
  // the visitor grabs him and moves him; when let go he drops down and cleans the closest thing
  body.addEventListener('pointerdown', function (e) {
    if (e.button > 0) return;
    e.preventDefault(); reset(); lad.classList.remove('on');
    drag = { dx: e.clientX - x, dy: e.clientY - y, id: e.pointerId, moved: false };
    try { body.setPointerCapture(e.pointerId); } catch (er) {}
    body.classList.remove('walk', 'carry', 'land'); body.classList.add('held');
  });
  body.addEventListener('pointermove', function (e) {
    if (!drag || e.pointerId !== drag.id) return;
    var nx = Math.max(0, Math.min(e.clientX - drag.dx, innerWidth - W)), ny = Math.max(0, Math.min(e.clientY - drag.dy, floor()));
    if (Math.abs(nx - x) > 1) body.classList.toggle('flip', nx < x);
    if (Math.abs(nx - x) + Math.abs(ny - y) > 1) drag.moved = true;
    x = nx; y = ny; place();
  });
  function release(e) {
    if (!drag || e.pointerId !== drag.id) return;
    drag = null; body.classList.remove('held');
    var cx = x + W / 2, cy = y + H / 2, best = null, bd = 1e9;
    targets().forEach(function (t) {
      var r = t.getBoundingClientRect(), d = Math.hypot(r.left + r.width / 2 - cx, r.top + r.height / 2 - cy);
      if (d < bd) { bd = d; best = t; }
    });
    pending = best ? { el: best } : { x: cx, y: cy, el: null };
    run++; scrolled = 0;
  }
  body.addEventListener('pointerup', release);
  body.addEventListener('pointercancel', release);
  (async function loop() {
    await wait(500);
    while (run >= 0) {
      if (drag || Date.now() - scrolled < 600 || document.hidden) { await wait(150); continue; }
      if (y < floor() - 1 && !lad.classList.contains('on')) {
        var fall = floor() - y > 40;
        if (!fall) body.classList.add('walk', 'carry');
        await tween(x, floor(), fall ? Math.min(600, 120 + (floor() - y) * 0.8) : 250, ++run);
        if (fall) { body.classList.add('land'); await wait(380); body.classList.remove('land'); }
      }
      body.classList.remove('walk', 'carry');
      if (Date.now() - active > IDLE) { await rest(); continue; }
      await cycle(); await wait(50);
    }
  })();
})();
