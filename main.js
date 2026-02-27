// ══════════════════════════════════════
// INGINERUL CU AI — main.js
// ══════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {

  // ══════════════════════════════════════
  // LENIS SMOOTH SCROLLING
  // ══════════════════════════════════════
  let lenis;
  if (typeof Lenis !== 'undefined') {
    lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // https://www.desmos.com/calculator/brs54l4xou
      direction: 'vertical',
      gestureDirection: 'vertical',
      smooth: true,
      mouseMultiplier: 1,
      smoothTouch: false,
      touchMultiplier: 2,
      infinite: false,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  // ══════════════════════════════════════
  // GSAP SCROLLTRIGGER ANIMATIONS
  // ══════════════════════════════════════
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Sync Lenis with ScrollTrigger
    if (lenis) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => {
        lenis.raf(time * 1000);
      });
      gsap.ticker.lagSmoothing(0);
    }

    // ── HERO PARALLAX DISPERSE EFFECT (Desktop Only) ──
    let mm = gsap.matchMedia();
    mm.add("(min-width: 992px)", () => {
      const heroTl = gsap.timeline({
        scrollTrigger: {
          trigger: ".hero",
          start: "top top",
          end: "bottom top",
          scrub: 1
        }
      });

      heroTl.to(".hero-center", {
        scale: 0.85,
        opacity: 0,
        y: 100,
        ease: "none"
      }, 0);

      heroTl.to(".hero-books-left", {
        x: -150,
        y: -200,
        rotation: -15,
        opacity: 0,
        ease: "none"
      }, 0);

      heroTl.to(".hero-books-right", {
        x: 150,
        y: -200,
        rotation: 15,
        opacity: 0,
        ease: "none"
      }, 0);

      return () => {
        // Cleanup if needed
      };
    });


    // ── PRODUCTS 3D STAGGER REVEAL (Unified for all screens) ──
    const productCards = gsap.utils.toArray('.product-card:not(.card-featured)');

    gsap.set(productCards, { autoAlpha: 0, y: 80, rotationX: -15, scale: 0.95, transformPerspective: 1000 });
    ScrollTrigger.batch(productCards, {
      start: "top 95%", // Trigger lower so it always catches on mobile
      onEnter: batch => gsap.to(batch, { autoAlpha: 1, y: 0, rotationX: 0, scale: 1, stagger: 0.1, ease: "power3.out", duration: 1.2, overwrite: true }),
      onLeaveBack: batch => gsap.to(batch, { autoAlpha: 0, y: 40, rotationX: -10, ease: "power2.in", overwrite: true })
    });

    // Handle featured cards separately for more impact
    const featuredCards = gsap.utils.toArray('.card-featured');
    featuredCards.forEach(card => {
      gsap.fromTo(card,
        { autoAlpha: 0, scale: 0.95, y: 50 },
        {
          autoAlpha: 1,
          scale: 1,
          y: 0,
          duration: 1.5,
          ease: "elastic.out(1, 0.75)",
          scrollTrigger: {
            trigger: card,
            start: "top 80%",
            toggleActions: "play none none reverse"
          }
        }
      );
    });

    // ── 1. LINE MASK REVEAL (H2 TITLES) ──
    const h2Titles = gsap.utils.toArray('h2');
    h2Titles.forEach(h2 => {
      const text = h2.innerHTML;
      h2.innerHTML = `<span class="line-mask-wrapper"><span class="gsap-reveal-title" style="display:inline-block">${text}</span></span>`;
      const innerText = h2.querySelector('.gsap-reveal-title');

      gsap.fromTo(innerText,
        { y: "120%", autoAlpha: 0, rotationX: -20 },
        {
          y: "0%",
          autoAlpha: 1,
          rotationX: 0,
          duration: 1.2,
          ease: "power4.out",
          scrollTrigger: {
            trigger: h2,
            start: "top 95%",
            toggleActions: "play none none reverse"
          }
        }
      );
    });

    // ── 2. STAGGERED FEATURES & TESTIMONIALS (Rezultate) ──
    const resultCases = gsap.utils.toArray('.result-case');
    resultCases.forEach((box) => {
      gsap.fromTo(box,
        { autoAlpha: 0, y: 60, rotationX: -10, scale: 0.96 },
        {
          autoAlpha: 1, y: 0, rotationX: 0, scale: 1,
          duration: 1.2,
          ease: "power3.out",
          scrollTrigger: {
            trigger: box,
            start: "top 95%",
            toggleActions: "play none none reverse"
          }
        }
      );
    });

    // ── 2.5 SITE-WIDE FADE-IN ELEMENTS ──
    const fadeElements = gsap.utils.toArray('.fade-in');
    fadeElements.forEach((el) => {
      gsap.fromTo(el,
        { autoAlpha: 0, y: 30 },
        {
          autoAlpha: 1, y: 0,
          duration: 1,
          ease: "power2.out",
          scrollTrigger: {
            trigger: el,
            start: "top 95%",
            toggleActions: "play none none reverse"
          }
        }
      );
    });

    // ── 3. BACKGROUND GLOW PARALLAX ──
    const glows = gsap.utils.toArray('.glow');
    glows.forEach(glow => {
      gsap.to(glow, {
        y: "20vh", // Subtle slow move down on scroll
        ease: "none",
        scrollTrigger: {
          trigger: glow.parentElement,
          start: "top top",
          end: "bottom top",
          scrub: true
        }
      });
    });

    // ── 4. MAGNETIC HOVER BUTTONS ──
    if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
      const magneticBtns = document.querySelectorAll('.btn-primary, .btn-nav, .btn-product');
      magneticBtns.forEach(btn => {
        btn.classList.add('magnetic-btn');

        const xSetter = gsap.quickSetter(btn, "x", "px");
        const ySetter = gsap.quickSetter(btn, "y", "px");

        btn.addEventListener('mousemove', (e) => {
          const rect = btn.getBoundingClientRect();
          const centerX = rect.left + rect.width / 2;
          const centerY = rect.top + rect.height / 2;
          const distX = e.clientX - centerX;
          const distY = e.clientY - centerY;

          xSetter(distX * 0.25);
          ySetter(distY * 0.25);
        });

        btn.addEventListener('mouseleave', () => {
          gsap.to(btn, {
            x: 0,
            y: 0,
            duration: 0.7,
            ease: "elastic.out(1, 0.3)"
          });
        });
      });
    }

    // ── 5. FLOATING ANIMATION FOR MODAL IMAGES ──
    const modalImages = gsap.utils.toArray('.modal-image');
    modalImages.forEach(img => {
      gsap.to(img, {
        y: -15,
        rotation: 1,
        duration: 2.5,
        ease: "sine.inOut",
        yoyo: true,
        repeat: -1
      });
    });

  }

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
    const xSetter = gsap.quickSetter(card, "--mouse-x", "%");
    const ySetter = gsap.quickSetter(card, "--mouse-y", "%");

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      xSetter(x);
      ySetter(y);
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

  // ── 12H HERO TIMER (NO LOOP) ────────────
  const heroTimer = document.querySelector('#heroTimer .time-bold');
  if (heroTimer) {
    const totalTime = 12 * 60 * 60 * 1000; // 12 hours in ms

    let endTime = localStorage.getItem('heroTimerEnd12h');
    if (!endTime) {
      endTime = Date.now() + totalTime;
      localStorage.setItem('heroTimerEnd12h', endTime);
    } else {
      endTime = parseInt(endTime);
    }

    let intervalId; // To stop the timer once it hits 0

    function updateHeroTimer() {
      const now = Date.now();
      let diff = endTime - now;

      if (diff <= 0) {
        // Evergreen timer: automatically reset to 12h when expired
        endTime = Date.now() + totalTime;
        localStorage.setItem('heroTimerEnd12h', endTime);
        diff = totalTime;
      }

      const hours = Math.floor(diff / (1000 * 60 * 60));
      const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((diff % (1000 * 60)) / 1000);

      const fh = hours.toString().padStart(2, '0');
      const fm = mins.toString().padStart(2, '0');
      const fs = secs.toString().padStart(2, '0');

      heroTimer.textContent = `${fh}h ${fm}m ${fs}s`;
    }

    updateHeroTimer(); // Initial call to avoid 1s delay
    intervalId = setInterval(updateHeroTimer, 1000);
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

  // ── LEGACY FADE-IN OBSERVER (For remaining pages like despre, blog) ──
  const fadeEls = document.querySelectorAll('.fade-in');
  if (fadeEls.length > 0) {
    const fadeObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, i * 80);
          fadeObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    fadeEls.forEach(el => fadeObserver.observe(el));
  }

  // ── 3D TILT EFFECT (BENTO BOX) ────────
  const tiltCards = document.querySelectorAll('.product-card, .card-featured');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left; // x position within the element.
      const y = e.clientY - rect.top; // y position within the element.

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const tiltX = ((y - centerY) / centerY) * -5; // Max rotation 5deg
      const tiltY = ((x - centerX) / centerX) * 5; // Max rotation 5deg

      card.style.setProperty('--rx', `${tiltX}deg`);
      card.style.setProperty('--ry', `${tiltY}deg`);
    });

    card.addEventListener('mouseleave', () => {
      card.style.setProperty('--rx', `0deg`);
      card.style.setProperty('--ry', `0deg`);
    });
  });

});
