const fs = require('fs');

const path = '/Users/samurai/Desktop/AI PROMPTS/Last Version Website/style.css';
let content = fs.readFileSync(path, 'utf8');

// Increase hero timer size
content = content.replace(
  /\.hob-timer\s*\{\s*text-align:\s*center;\s*color:\s*var\(--gray\);\s*font-size:\s*12px;/s,
  `.hob-timer {\n  text-align: center;\n  color: var(--gray);\n  font-size: 13px;`
);

// Better red color for timer
content = content.replace(
  /\.hob-timer\sspan\.time-bold\s*\{\s*display:\s*inline-block;\s*font-family:\s*var\(--font-head\);\s*font-size:\s*18px;\s*font-weight:\s*800;\s*color:\s*#e74c3c;/s,
  `.hob-timer span.time-bold {\n  display: inline-block;\n  font-family: var(--font-head);\n  font-size: 20px;\n  font-weight: 800;\n  color: #ff6b6b;`
);

// Add visual banner to 'In curand' cards
content = content.replace(
  /\.product-card\s*\{\s*background:\s*var\(--card-bg\);\s*border:\s*1px\ssolid\svar\(--border-dim\);\s*border-radius:\s*var\(--radius-lg\);\s*padding:\s*28px\s24px;\s*position:\s*relative;\s*transition:\s*var\(--transition\);\s*display:\s*flex;\s*flex-direction:\s*column;\s*gap:\s*12px;\s*\}/s,
  `.product-card {\n  background: var(--card-bg);\n  border: 1px solid var(--border-dim);\n  border-radius: var(--radius-lg);\n  padding: 28px 24px;\n  position: relative;\n  transition: var(--transition);\n  display: flex;\n  flex-direction: column;\n  gap: 12px;\n  overflow: hidden;\n}`
);

// Smoother modals open
content = content.replace(
  /\.modal-overlay\s*\{\s*position:\s*fixed;\s*inset:\s*0;\s*background:\s*rgba\(6,\s*10,\s*18,\s*0\.85\);\s*backdrop-filter:\s*blur\(12px\);\s*-webkit-backdrop-filter:\s*blur\(12px\);\s*z-index:\s*9999;\s*display:\s*flex;\s*align-items:\s*center;\s*justify-content:\s*center;\s*opacity:\s*0;\s*visibility:\s*hidden;\s*transition:\s*0\.4s\sease;\s*padding:\s*20px;\s*\}/s,
  `.modal-overlay {\n  position: fixed;\n  inset: 0;\n  background: rgba(6, 10, 18, 0.85);\n  backdrop-filter: blur(12px);\n  -webkit-backdrop-filter: blur(12px);\n  z-index: 9999;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  opacity: 0;\n  visibility: hidden;\n  transition: opacity 0.3s ease-out, visibility 0.3s ease-out;\n  padding: 20px;\n}`
);

// Fix Testimonials layout
if (!content.includes('.testimonials-scroll')) {
  // Add Snap Scroll to testimonials if not found
  content += `\n/* Snap Scroll */\n.testimonials-scroll { scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; }\n.t-card { scroll-snap-align: center; }\n`;
}


fs.writeFileSync(path, content, 'utf8');
console.log("style.css second batch updated");
