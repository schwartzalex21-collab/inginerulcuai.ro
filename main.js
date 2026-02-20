// ══════════════════════════════════════
// INGINERUL CU AI — main.js
// ══════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {

  // ── NAVBAR SCROLL ─────────────────────
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.style.background = 'rgba(8,15,30,0.97)';
      navbar.style.boxShadow = '0 4px 30px rgba(0,0,0,0.4)';
    } else {
      navbar.style.background = 'rgba(8,15,30,0.85)';
      navbar.style.boxShadow = 'none';
    }
  });

  // ── HAMBURGER MOBILE MENU ──────────────
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      const spans = hamburger.querySelectorAll('span');
      if (mobileMenu.classList.contains('open')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });
  }

  // ── SCROLL ANIMATIONS ─────────────────
  const fadeEls = document.querySelectorAll('.fade-in');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  fadeEls.forEach(el => observer.observe(el));

  // ── SMOOTH ANCHOR SCROLL ───────────────
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ── PRODUCT CARD HOVER GLOW ───────────
  document.querySelectorAll('.product-card, .bundle-card, .testimonial').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      card.style.setProperty('--mouse-x', x + '%');
      card.style.setProperty('--mouse-y', y + '%');
    });
  });

  // ── CONTACT FORM ──────────────────────
  const btnSubmit = document.querySelector('.btn-submit');
  if (btnSubmit) {
    btnSubmit.addEventListener('click', (e) => {
      e.preventDefault();
      const originalText = btnSubmit.textContent;
      btnSubmit.textContent = '✅ Mesaj trimis! Îți răspundem în 24h.';
      btnSubmit.style.background = '#2ECC71';
      setTimeout(() => {
        btnSubmit.textContent = originalText;
        btnSubmit.style.background = '';
      }, 4000);
    });
  }

  // ── NEWSLETTER BUTTON ─────────────────
  document.querySelectorAll('button.btn-primary').forEach(btn => {
    if (btn.textContent.includes('Abonează')) {
      btn.addEventListener('click', () => {
        btn.textContent = '✅ Abonat!';
        btn.style.background = '#2ECC71';
      });
    }
  });

  // ── COUNTER ANIMATION ─────────────────
  function animateCounter(el, target, duration = 1500) {
    const start = performance.now();
    const startVal = 0;
    const update = (time) => {
      const progress = Math.min((time - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(startVal + (target - startVal) * eased);
      el.textContent = current + (el.dataset.suffix || '');
      if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  }

  const statNums = document.querySelectorAll('.stat-num');
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const text = el.textContent;
        const num = parseInt(text.replace(/\D/g, ''));
        const suffix = text.includes('%') ? '%' : '';
        el.dataset.suffix = suffix;
        if (!isNaN(num)) animateCounter(el, num);
        statsObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  statNums.forEach(el => statsObserver.observe(el));

  // ── DYNAMIC USER COUNTER ──────────────
  const dynamicCounter = document.getElementById('dynamic-counter');
  if (dynamicCounter) {
    let currentVal = 300; // Starting value

    // Check if there's a stored value and time
    const storedVal = localStorage.getItem('userCount');
    const lastUpdate = localStorage.getItem('lastUpdate');

    if (storedVal) {
      currentVal = parseInt(storedVal);
      // Ensure we don't show a stored value less than new baseline if reset
      if (currentVal < 300) currentVal = 300;
      dynamicCounter.textContent = currentVal;
    }

    setInterval(() => {
      currentVal++;
      dynamicCounter.textContent = currentVal;
      localStorage.setItem('userCount', currentVal);
      localStorage.setItem('lastUpdate', Date.now());
    }, 3600000); // 3600000 ms = 60 minutes
  }

  // ── MODAL / POPUP SYSTEM ──────────────
  const modalTriggers = document.querySelectorAll('[data-modal-target]');
  const modals = document.querySelectorAll('.modal-overlay');
  const modalCloses = document.querySelectorAll('.modal-close');

  function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.add('active');
      document.body.style.overflow = 'hidden'; // Prevent background scroll
    }
  }

  function closeModal(modal) {
    if (modal) {
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  modalTriggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = btn.getAttribute('data-modal-target');
      openModal(targetId);
    });
  });

  modalCloses.forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = btn.closest('.modal-overlay');
      closeModal(modal);
    });
  });

  modals.forEach(modal => {
    modal.addEventListener('click', (e) => {
      // Close only if clicking on the overlay background, not the content
      if (e.target === modal) {
        closeModal(modal);
      }
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const activeModal = document.querySelector('.modal-overlay.active');
      if (activeModal) closeModal(activeModal);
    }
  });

  // ── SCROLL TO TOP ─────────────────────
  const scrollToTopBtn = document.getElementById('scrollToTop');
  if (scrollToTopBtn) {
    window.addEventListener('scroll', () => {
      // Show button if scrolled more than 300px
      if (window.scrollY > 300) {
        scrollToTopBtn.classList.add('visible');
      } else {
        scrollToTopBtn.classList.remove('visible');
      }
    });

    scrollToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

});
