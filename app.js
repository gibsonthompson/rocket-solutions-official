// Rocket Solutions - shared interactions

// sticky nav style on scroll
(function () {
  const nav = document.getElementById('nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 12);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }
})();

// mobile menu
(function () {
  const toggle = document.getElementById('menuToggle');
  const menu = document.getElementById('navMenu');
  if (!toggle || !menu) return;
  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => menu.classList.remove('open')));
})();

// scroll reveal
(function () {
  const els = document.querySelectorAll('.reveal');
  if (!els.length) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(el => io.observe(el));
})();

// rotating outcome word in hero
(function () {
  const el = document.getElementById('rotator');
  if (!el) return;
  const words = (el.dataset.words || '').split(',').map(w => w.trim()).filter(Boolean);
  if (words.length < 2) return;
  let i = 0;
  const swap = () => {
    el.style.transition = 'opacity .3s ease, transform .3s ease';
    el.style.opacity = '0';
    el.style.transform = 'translateY(8px)';
    setTimeout(() => {
      i = (i + 1) % words.length;
      el.textContent = words[i];
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 300);
  };
  setInterval(swap, 2400);
})();

// contact form -> /api/contact (texts a lead alert via Telnyx)
(function () {
  const form = document.getElementById('contactForm');
  if (!form) return;
  const statusEl = document.getElementById('formStatus');
  const submitBtn = document.getElementById('submitBtn');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    statusEl.className = 'form-status';

    const hp = form.querySelector('[name=botcheck]');
    if (hp && hp.checked) return; // honeypot

    const fd = new FormData(form);
    const payload = {
      name: (fd.get('name') || '').toString().trim(),
      company: (fd.get('company') || '').toString().trim(),
      email: (fd.get('email') || '').toString().trim(),
      phone: (fd.get('phone') || '').toString().trim(),
      interest: (fd.get('interest') || '').toString().trim(),
      message: (fd.get('message') || '').toString().trim(),
      botcheck: hp && hp.checked ? 'on' : ''
    };

    submitBtn.disabled = true;
    const original = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json().catch(() => ({}));
      if (res.ok && data.ok) {
        form.reset();
        statusEl.className = 'form-status ok';
        statusEl.textContent = 'Message received. We will be in touch within one business day.';
      } else {
        throw new Error(data.error || 'failed');
      }
    } catch (err) {
      statusEl.className = 'form-status err';
      statusEl.textContent = 'Something went wrong. Email hello@gorocketsolutions.com and we will pick it up.';
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = original;
    }
  });
})();