const fs = require('fs');
const jsFile = 'main.js';

let js = fs.readFileSync(jsFile, 'utf8');

if (!js.includes('AWWWARDS FEATURES')) {
    // Inject at the beginning of DOMContentLoaded
    js = js.replace("document.addEventListener('DOMContentLoaded', () => {", 
`document.addEventListener('DOMContentLoaded', () => {

  // ══════════════════════════════════════
  // AWWWARDS FEATURES (Preloader, Cursor)
  // ══════════════════════════════════════

  // 1. Immersive Preloader
  const preloader = document.querySelector('.site-preloader');
  const preloaderBar = document.querySelector('.preloader-bar');
  
  if (preloader && preloaderBar) {
    // Lock scroll initially
    if (typeof lenis !== 'undefined') lenis.stop();
    document.body.style.overflow = 'hidden';

    // Simulate loading progress
    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.random() * 15;
      if (progress > 100) progress = 100;
      preloaderBar.style.width = progress + '%';

      if (progress === 100) {
        clearInterval(interval);
        setTimeout(() => {
          preloader.classList.add('is-loaded');
          document.body.style.overflow = '';
          if (typeof lenis !== 'undefined') lenis.start();
          
          // Re-trigger scrolltrigger to fix any calculations after preloader
          if (typeof ScrollTrigger !== 'undefined') {
            setTimeout(() => ScrollTrigger.refresh(), 800);
          }
        }, 400);
      }
    }, 100);
  }

  // 2. Custom Interactive Cursor (Desktop Only)
  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    const cursor = document.querySelector('.custom-cursor');
    if (cursor && typeof gsap !== 'undefined') {
      document.body.classList.add('has-custom-cursor');
      
      // GSAP quick setter for performance
      gsap.set(cursor, {xPercent: -50, yPercent: -50});
      const xTo = gsap.quickTo(cursor, "x", {duration: 0.15, ease: "power3"});
      const yTo = gsap.quickTo(cursor, "y", {duration: 0.15, ease: "power3"});

      window.addEventListener("mousemove", e => {
        xTo(e.clientX);
        yTo(e.clientY);
      });

      // Interactive states
      const interactives = document.querySelectorAll('a, button, .product-card, .hbook');
      interactives.forEach(el => {
        el.addEventListener("mouseenter", () => cursor.classList.add('is-active'));
        el.addEventListener("mouseleave", () => cursor.classList.remove('is-active'));
      });
      
      // Also scale it down globally when clicking
      window.addEventListener("mousedown", () => gsap.to(cursor, {scale: 0.8, duration: 0.1}));
      window.addEventListener("mouseup", () => gsap.to(cursor, {scale: 1, duration: 0.1}));
    }
  }
`);
    fs.writeFileSync(jsFile, js);
    console.log("main.js updated");
} else {
    console.log("main.js already has AWWWARDS FEATURES");
}
