const fs = require('fs');
const path = require('path');

const indexFile = path.join(__dirname, 'index.html');
const styleFile = path.join(__dirname, 'style.css');
const mainFile = path.join(__dirname, 'main.js');

let html = fs.readFileSync(indexFile, 'utf8');
let css = fs.readFileSync(styleFile, 'utf8');
let js = fs.readFileSync(mainFile, 'utf8');

// --- HTML Modifications ---
// 1. Add Preloader and Film Grain right after <body>
if (!html.includes('class="film-grain"')) {
    html = html.replace(/<body>/i, `<body>
  <!-- 🎨 AWWWARDS FEATURES -->
  <div class="film-grain"></div>
  <div class="site-preloader">
    <div class="preloader-content">
      <div class="preloader-logo">AI</div>
      <div class="preloader-progress"><div class="preloader-bar"></div></div>
    </div>
  </div>
  <div class="custom-cursor"></div>
  <!-- 🎨 END AWWWARDS FEATURES -->`);
}

// --- CSS Modifications ---
if (!css.includes('.film-grain')) {
    css += `

/* ══════════════════════════════════════
   AWWWARDS FEATURES
══════════════════════════════════════ */
/* 1. Cinematic Film Grain */
.film-grain {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}

/* 2. Immersive Preloader */
.site-preloader {
  position: fixed;
  inset: 0;
  background: var(--bg);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.8s cubic-bezier(0.77, 0, 0.175, 1);
  will-change: transform;
}

.site-preloader.is-loaded {
  transform: translateY(-100%);
  pointer-events: none;
}

.preloader-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.preloader-logo {
  font-family: var(--font-head);
  font-size: 32px;
  font-weight: 800;
  color: var(--gold);
  border: 3px solid var(--gold);
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
}

.preloader-logo::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  100% { left: 100%; }
}

.preloader-progress {
  width: 120px;
  height: 2px;
  background: rgba(255, 255, 255, 0.1);
  overflow: hidden;
  border-radius: 2px;
}

.preloader-bar {
  width: 0%;
  height: 100%;
  background: var(--gold);
  transition: width 0.1s;
}

/* 3. Custom Interactive Cursor (Desktop Only) */
.custom-cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 30px;
  height: 30px;
  border: 2px solid var(--gold);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9998;
  transform: translate(-50%, -50%);
  transition: width 0.3s ease, height 0.3s ease, background 0.3s ease, mix-blend-mode 0.3s ease, border-color 0.3s ease;
  will-change: width, height, transform;
  display: none;
}

.custom-cursor.is-active {
  background: rgba(243, 156, 18, 0.15);
  width: 50px;
  height: 50px;
  /* border-color: transparent; */
}

/* Hide native cursor when custom is active */
@media (hover: hover) and (pointer: fine) {
  body.has-custom-cursor {
    cursor: none;
  }
  body.has-custom-cursor a,
  body.has-custom-cursor button,
  body.has-custom-cursor .btn-primary,
  body.has-custom-cursor .product-card,
  body.has-custom-cursor .hbook {
    cursor: none;
  }
  .custom-cursor {
    display: block;
  }
}
`;
}

// --- JS Modifications ---
if (!js.includes('AWWWARDS FEATURES')) {
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
      preloaderBar.style.width = \`\${progress}%\`;

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
}

fs.writeFileSync(indexFile, html);
fs.writeFileSync(styleFile, css);
fs.writeFileSync(mainFile, js);

console.log("Awwwards changes applied successfully!");
