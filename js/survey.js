/* One short "did you find what you were looking for?" box per visitor. Answers go to the Netlify form "sondage". */
(function () {
  var fr = (document.documentElement.lang || 'fr').indexOf('en') !== 0;
  var path = location.pathname;
  if (/^\/(commander|merci|en\/order|en\/thanks)\//.test(path)) return;
  if (/bot|crawl|spider|lighthouse|headless/i.test(navigator.userAgent)) return;
  try { if (localStorage.getItem('el-svy')) return; } catch (e) { return; }
  var T = fr ? {
    q: 'Avez-vous trouvé ce que vous cherchiez?', yes: 'Oui', no: 'Non', close: 'Fermer',
    thanks_yes: 'Merci! Vous pouvez commander en ligne ou demander une soumission.', order: 'Commander en ligne', ohref: '/commander/',
    h: 'Aidez-nous à vous servir', p: 'Quel produit cherchiez-vous?', qty: 'Quantité approximative (sacs de 25 lb)', city: 'Votre ville',
    miss: "Qu'est-ce qui manquait sur le site?", mail: 'Courriel (facultatif, si vous voulez une réponse)', send: 'Envoyer',
    done: 'Merci! Votre réponse a été envoyée.', fine: 'Votre courriel sert seulement à vous répondre.'
  } : {
    q: 'Did you find what you were looking for?', yes: 'Yes', no: 'No', close: 'Close',
    thanks_yes: 'Thanks! You can order online or request a quote.', order: 'Order online', ohref: '/en/order/',
    h: 'Help us serve you', p: 'What product were you looking for?', qty: 'Rough quantity (25 lb bags)', city: 'Your city',
    miss: 'What was missing on the site?', mail: 'Email (optional, if you want an answer)', send: 'Send',
    done: 'Thank you! Your answer was sent.', fine: 'Your email is only used to answer you.'
  };
  var box, shown = false, t0 = Date.now();
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function send(data) {
    data['form-name'] = 'sondage'; data.langue = fr ? 'fr' : 'en'; data.page = path;
    return fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() });
  }
  function close() { if (box) box.remove(); }
  function body(html) { box.querySelector('.svy-b').innerHTML = html; }
  function show() {
    if (shown) return; shown = true;
    try { localStorage.setItem('el-svy', '1'); } catch (e) {}
    box = document.createElement('aside');
    box.className = 'svy'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-label', T.q);
    box.innerHTML = '<button type="button" class="svy-x" aria-label="' + T.close + '">×</button><div class="svy-b"><p class="svy-q">' + esc(T.q) +
      '</p><div class="svy-yn"><button type="button" class="btn btn-primary" data-a="oui">' + T.yes + '</button><button type="button" class="btn btn-ghost" data-a="non">' + T.no + '</button></div></div>';
    document.body.appendChild(box);
    box.querySelector('.svy-x').onclick = close;
    box.querySelector('[data-a=oui]').onclick = function () {
      send({ trouve: 'oui' });
      body('<p class="svy-q">' + esc(T.thanks_yes) + '</p><a class="btn btn-primary" href="' + T.ohref + '">' + T.order + '</a>');
    };
    box.querySelector('[data-a=non]').onclick = function () {
      body('<form class="qform svy-f"><p class="svy-q">' + esc(T.h) + '</p>' +
        '<label>' + T.p + '<input name="produit" maxlength="120"></label>' +
        '<label>' + T.qty + '<input name="quantite" maxlength="40" inputmode="numeric"></label>' +
        '<label>' + T.city + '<input name="ville" maxlength="60" autocomplete="address-level2"></label>' +
        '<label>' + T.miss + '<textarea name="commentaire" maxlength="600"></textarea></label>' +
        '<label>' + T.mail + '<input name="courriel" type="email" maxlength="120" autocomplete="email"></label>' +
        '<button class="btn btn-primary" type="submit">' + T.send + '</button><p class="fine">' + T.fine + '</p></form>');
      var f = box.querySelector('form');
      f.onsubmit = function (e) {
        e.preventDefault();
        var d = { trouve: 'non' };
        [].forEach.call(f.elements, function (el) { if (el.name) d[el.name] = el.value.trim(); });
        send(d).finally(function () { body('<p class="svy-q">' + esc(T.done) + '</p>'); setTimeout(close, 4000); });
      };
    };
  }
  setTimeout(show, 40000);
  document.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY <= 0 && Date.now() - t0 > 10000) show(); });
})();
