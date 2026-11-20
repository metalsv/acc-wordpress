/* ACC — interacciones del mockup */
(function () {
  'use strict';

  /* marca que el JS está activo: sin esto, el contenido se ve siempre */
  document.documentElement.classList.add('js-anim');

  /* ---------- header sticky ---------- */
  var header = document.querySelector('.header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- menú móvil ---------- */
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', nav.classList.contains('is-open'));
      document.body.style.overflow = nav.classList.contains('is-open') ? 'hidden' : '';
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('is-open');
        document.body.style.overflow = '';
      }
    });
  }

  /* ---------- toast ---------- */
  var toastEl = null;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      toastEl.innerHTML =
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16.5v.01"/></svg><span></span>';
      document.body.appendChild(toastEl);
    }
    toastEl.querySelector('span').textContent = msg;
    requestAnimationFrame(function () { toastEl.classList.add('is-on'); });
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(function () { toastEl.classList.remove('is-on'); }, 3600);
  }
  window.accToast = toast;

  /* selector de idioma (maqueta) */
  document.querySelectorAll('.lang button').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.lang button').forEach(function (x) { x.classList.remove('is-on'); });
      b.classList.add('is-on');
      if (b.dataset.lang === 'en') {
        toast('La versión en inglés se habilitará en la fase de desarrollo del sitio.');
      }
    });
  });

  /* ---------- reveal on scroll ---------- */
  var revs = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revs.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    revs.forEach(function (r) { io.observe(r); });
  } else {
    revs.forEach(function (r) { r.classList.add('is-in'); });
  }

  /* ---------- filtro de servicios ---------- */
  var svcWrap = document.querySelector('[data-services]');
  if (svcWrap) {
    var items = Array.prototype.slice.call(svcWrap.querySelectorAll('.svc[data-cat]'));
    var filters = document.querySelectorAll('.filter');
    var empty = document.querySelector('.empty');
    var counts = {};
    items.forEach(function (it) { counts[it.dataset.cat] = (counts[it.dataset.cat] || 0) + 1; });
    document.querySelectorAll('[data-count]').forEach(function (el) {
      var k = el.dataset.count;
      el.textContent = k === 'todos' ? items.length : (counts[k] || 0);
    });
    filters.forEach(function (f) {
      f.addEventListener('click', function () {
        filters.forEach(function (x) { x.classList.remove('is-on'); x.setAttribute('aria-pressed', 'false'); });
        f.classList.add('is-on');
        f.setAttribute('aria-pressed', 'true');
        var cat = f.dataset.filter, shown = 0;
        items.forEach(function (it, i) {
          var ok = cat === 'todos' || it.dataset.cat === cat;
          it.style.display = ok ? '' : 'none';
          if (ok) { shown++; it.style.animation = 'none'; void it.offsetWidth; it.style.animation = 'fadeUp .4s ' + (i * 0.02) + 's cubic-bezier(.22,.61,.36,1) both'; }
        });
        if (empty) empty.classList.toggle('is-on', shown === 0);
      });
    });
  }

  /* ---------- buscador de noticias ---------- */
  var newsSearch = document.querySelector('[data-news-search]');
  if (newsSearch) {
    var posts = Array.prototype.slice.call(document.querySelectorAll('[data-news-item]'));
    var noRes = document.querySelector('[data-news-empty]');
    newsSearch.addEventListener('input', function () {
      var q = newsSearch.value.trim().toLowerCase();
      var shown = 0;
      posts.forEach(function (p) {
        var ok = p.textContent.toLowerCase().indexOf(q) > -1;
        p.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      if (noRes) noRes.classList.toggle('is-on', shown === 0);
    });
  }

  /* ---------- acordeón FAQ ---------- */
  document.querySelectorAll('.faq__q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq__item');
      var panel = item.querySelector('.faq__a');
      var open = item.classList.contains('is-open');
      item.parentElement.querySelectorAll('.faq__item.is-open').forEach(function (o) {
        o.classList.remove('is-open');
        o.querySelector('.faq__a').style.maxHeight = null;
        o.querySelector('.faq__q').setAttribute('aria-expanded', 'false');
      });
      if (!open) {
        item.classList.add('is-open');
        panel.style.maxHeight = panel.scrollHeight + 'px';
        q.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------- formulario ---------- */
  document.querySelectorAll('form[data-demo]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = form.querySelector('.form__ok');
      if (ok) {
        ok.classList.add('is-on');
        ok.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.querySelectorAll('input:not([type=checkbox]),textarea,select').forEach(function (i) { i.value = ''; });
    });
  });

  /* newsletter */
  document.querySelectorAll('.nl-form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = f.querySelector('input');
      if (!input.value || input.value.indexOf('@') < 0) { toast('Escribe un correo válido para suscribirte.'); return; }
      toast('¡Listo! Te suscribiste al boletín de ACC.');
      input.value = '';
    });
  });

  /* ---------- año dinámico ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- utilidad de maqueta: enlaces no implementados ---------- */
  document.querySelectorAll('[data-pending]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      toast('Pantalla no incluida en esta entrega de maqueta.');
    });
  });
})();
