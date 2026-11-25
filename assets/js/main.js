/* Harlem Group · site behaviour
   1. WhatsApp links: any <a data-wa="message"> gets a pre-filled chat link.
   2. Mobile menu toggle.
   3. Pay calculator.
   4. Header border + mobile "apply" bar on scroll.
   5. Tap feedback on iPhone.
   6. "Get it here" insurance links open the insurance box under "You need".
*/
(function () {
  'use strict';

  // ---- Settings: change the number or rates here -------------------------
  var WHATSAPP_NUMBER = '447933997943'; // 07933 997943 in international format, no "+" or spaces
  var TARGET_DAILY = 200;               // used for "X parcels a day makes £200"
  var METER_MAX = 300;                  // right-hand end of the pay meter, in £
  // --------------------------------------------------------------------------

  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gbp = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP', maximumFractionDigits: 0 });

  function waLink(message) {
    return 'https://wa.me/' + WHATSAPP_NUMBER + (message ? '?text=' + encodeURIComponent(message) : '');
  }

  // 1. WhatsApp links ---------------------------------------------------------
  document.querySelectorAll('a[data-wa]').forEach(function (a) {
    a.href = waLink(a.getAttribute('data-wa'));
  });

  // 2. Mobile menu -----------------------------------------------------------
  var menuBtn = document.getElementById('menu-btn');
  var nav = document.getElementById('nav');
  if (menuBtn && nav) {
    var setOpen = function (open) {
      menuBtn.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
    };
    menuBtn.addEventListener('click', function () {
      setOpen(menuBtn.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { setOpen(false); menuBtn.focus(); }
    });
  }

  // 3. Pay calculator --------------------------------------------------------
  var form = document.getElementById('calc');
  if (form) {
    var parcels = document.getElementById('parcels');
    var parcelsOut = document.getElementById('parcels-out');
    var outDay = document.getElementById('out-day');
    var outWeek = document.getElementById('out-week');
    var outHelp = document.getElementById('out-help');
    var mark = document.getElementById('meter-mark');

    var result = form.querySelector('.calc-result');
    var shown = {};   // the £ figure each output currently shows
    var timers = {};

    // Set a £ figure. When a rate or day button is tapped, the figure ticks
    // quickly to the new amount so the change is easy to spot. While the
    // slider is dragged (or with reduced motion on) it changes straight away.
    var setMoney = function (el, value, tick) {
      var from = shown[el.id];
      shown[el.id] = value;
      if (timers[el.id]) cancelAnimationFrame(timers[el.id]);
      if (!tick || reduceMotion || from === undefined || from === value) {
        el.textContent = gbp.format(value);
        return;
      }
      var start = null, DURATION = 280;
      result.setAttribute('aria-busy', 'true'); // screen readers hear only the final figure
      var step = function (now) {
        if (start === null) start = now;
        var t = Math.min(1, (now - start) / DURATION);
        var eased = 1 - Math.pow(1 - t, 3);
        el.textContent = gbp.format(from + (value - from) * eased);
        if (t < 1) { timers[el.id] = requestAnimationFrame(step); }
        else { timers[el.id] = null; if (!timers['out-day'] && !timers['out-week']) result.removeAttribute('aria-busy'); }
      };
      timers[el.id] = requestAnimationFrame(step);
    };

    var checked = function (name) {
      var el = form.querySelector('input[name="' + name + '"]:checked');
      return el ? parseFloat(el.value) : 0;
    };
    var rateLabel = function (rate) { return rate < 1 ? Math.round(rate * 100) + 'p' : gbp.format(rate).replace(/^£(\d+)$/, '£$1.00'); };

    var update = function (e) {
      var tick = !!(e && e.target && e.target.type === 'radio');
      var rate = checked('rate');
      var days = checked('days');
      var n = parseInt(parcels.value, 10);
      var daily = Math.round(n * rate * 100) / 100;
      var weekly = daily * days;

      parcelsOut.textContent = n;
      setMoney(outDay, daily, tick);
      setMoney(outWeek, weekly, tick);
      outHelp.textContent = 'At ' + rateLabel(rate) + ', ' + Math.ceil(TARGET_DAILY / rate) + ' parcels a day makes ' + gbp.format(TARGET_DAILY) + '.';

      var pct = Math.min(100, (daily / METER_MAX) * 100);
      mark.style.left = pct.toFixed(2) + '%';
      var fill = ((n - parcels.min) / (parcels.max - parcels.min)) * 100;
      parcels.style.setProperty('--fill', fill.toFixed(1) + '%');
    };
    form.addEventListener('input', update);
    update();
  }

  // 4. Header border + mobile apply bar ----------------------------------------
  // On phones the bottom bar is the main WhatsApp button. It shows from the
  // top of the page and hides once the business section comes on screen or is passed.
  var header = document.querySelector('.site-header');
  var bar = document.querySelector('.mobile-bar');
  var biz = document.getElementById('business');

  var setBar = function (on) {
    if (bar) bar.classList.toggle('show', on);
    document.body.classList.toggle('bar-on', on);
  };
  if (biz && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      var e = entries[0];
      setBar(!(e.isIntersecting || e.boundingClientRect.top < 0));
    }).observe(biz);
  } else {
    setBar(true);
  }
  var onScroll = function () { if (header) header.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // 5. Tap feedback ------------------------------------------------------------
  // iPhone Safari only shows the pressed (:active) style when the page listens for touches.
  document.addEventListener('touchstart', function () {}, { passive: true });

  // 6. Insurance links ---------------------------------------------------------
  // Links to #get-cover (on this page or from a town page) open the
  // "No hire & reward cover yet?" box so the insurers are visible straight away.
  var cover = document.getElementById('get-cover');
  if (cover) {
    var openCover = function () { cover.open = true; };
    if (location.hash === '#get-cover') openCover();
    window.addEventListener('hashchange', function () { if (location.hash === '#get-cover') openCover(); });
    document.querySelectorAll('a[href="#get-cover"]').forEach(function (a) { a.addEventListener('click', openCover); });
  }
})();
