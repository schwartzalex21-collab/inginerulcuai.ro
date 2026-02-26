const fs = require('fs');

const path = '/Users/samurai/Desktop/AI PROMPTS/Last Version Website/style.css';
let content = fs.readFileSync(path, 'utf8');

// Replace .mobile-menu base setup
let targetBase = `.mobile-menu {
  display: none;
  flex-direction: column;
  padding: 16px 24px 24px;
  border-top: 1px solid var(--border-dim);
  gap: 4px;
}`;

let newBase = `.mobile-menu {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background: rgba(8, 15, 30, 0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  display: flex;
  flex-direction: column;
  padding: 24px;
  border-top: 1px solid var(--border-dim);
  border-bottom: 2px solid var(--gold);
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  gap: 12px;
  
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  pointer-events: none;
  transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s ease;
  z-index: 99;
}`;

content = content.replace(targetBase, newBase);

// Replace .mobile-menu a padding (make tap targets larger)
content = content.replace(
    /\.mobile-menu a \{\n\s*padding: 12px 0;\n\s*font-weight: 500;/s,
    `.mobile-menu a {\n  padding: 14px 16px;\n  font-weight: 500;`
);

// Under @media (max-width: 768px), fix .mobile-menu.open
let targetOpen = `  .mobile-menu.open {
    display: flex;
  }`;

let newOpen = `  .mobile-menu.open {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
    pointer-events: auto;
  }`;

content = content.replace(targetOpen, newOpen);

// Let's make sure #navbar is relative for absolute positioning of mobile menu
content = content.replace(
    /#navbar \{\n\s*position: fixed;/s,
    `#navbar {\n  position: fixed;`
); // It's fixed, so top 100% works perfectly.

// Mobile Floating CTA shadow and z-index improvement
content = content.replace(
    /\.mobile-floating-cta \{\n.*?\}/s,
    `.mobile-floating-cta {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 16px;
  background: rgba(6, 10, 18, 0.95);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-top: 1px solid var(--border-dim);
  z-index: 999;
  box-shadow: 0 -10px 30px rgba(0,0,0,0.4);
}`
);


fs.writeFileSync(path, content, 'utf8');
console.log("Updated mobile menu and CTA CSS");
