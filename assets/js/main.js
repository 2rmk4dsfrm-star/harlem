/* Harlem Group · site behaviour
   1. WhatsApp links: any <a data-wa="message"> gets a pre-filled chat link.
   2. Mobile menu toggle.
   3. Pay calculator.
   4. Header border + mobile "apply" bar on scroll.
*/
(function () {
  'use strict';

  // ---- Settings: change the number or rates here -------------------------
  var WHATSAPP_NUMBER = '447548547193'; // 07548 547193 in international format, no "+" or spaces
  var TARGET_DAILY = 200;               // used for "X parcels a day makes £200"
  var METER_MAX = 300;                  // right-hand end of the pay meter, in £
  // --------------------------------------------------------------------------

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

    var checked = function (name) {
      var el = form.querySelector('input[name="' + name + '"]:checked');
      return el ? parseFloat(el.value) : 0;
    };
    var rateLabel = function (rate) { return rate < 1 ? Math.round(rate * 100) + 'p' : gbp.format(rate).replace(/^£(\d+)$/, '£$1.00'); };

    var update = function () {
      var rate = checked('rate');
      var days = checked('days');
      var n = parseInt(parcels.value, 10);
      var daily = Math.round(n * rate * 100) / 100;
      var weekly = daily * days;

      parcelsOut.textContent = n;
      outDay.textContent = gbp.format(daily);
      outWeek.textContent = gbp.format(weekly);
      outHelp.textContent = 'At ' + rateLabel(rate) + ', ' + Math.ceil(TARGET_DAILY / rate) + ' parcels a day makes ' + gbp.format(TARGET_DAILY) + '.';

      var pct = Math.min(100, (daily / METER_MAX) * 100);
      mark.style.left = pct.toFixed(2) + '%';
      var fill = ((n - parcels.min) / (parcels.max - parcels.min)) * 100;
      parcels.style.setProperty('--fill', fill.toFixed(1) + '%');
    };
    form.addEventListener('input', update);
    form.addEventListener('change', update);
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
})();
