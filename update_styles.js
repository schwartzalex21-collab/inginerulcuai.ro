const fs = require('fs');

const path = '/Users/samurai/Desktop/AI PROMPTS/Last Version Website/style.css';
let content = fs.readFileSync(path, 'utf8');

// 1. Mobile body line-height
content = content.replace(
  /body\s*\{\s*background:\s*var\(--bg\);\s*color:\s*var\(--white\);\s*font-family:\s*var\(--font-body\);\s*font-size:\s*16px;\s*line-height:\s*1\.65;/s,
  `body {
  background: var(--bg);
  color: var(--white);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.65;
  
  /* UX/UI Improvement: Better mobile readability */
  @media (max-width: 768px) {
    line-height: 1.75;
  }`
);

// 2. Refined hover states for buttons (softer gold)
content = content.replace(
  /\.btn-primary:hover\s*\{\s*background:\s*var\(--gold-dim\);/s,
  `.btn-primary:hover {
  background: #f1c40f; /* Softer gold hover instead of dim */`
);

// 3. Modals Smooth Animation
content = content.replace(
  /\.modal-content\s*\{\s*background:\s*var\(--card-bg\);\s*width:\s*100%;/s,
  `.modal-content {
  background: var(--card-bg);
  width: 100%;
  transform: scale(0.95);
  opacity: 0;
  transition: transform 0.3s ease-out, opacity 0.3s ease-out;`
);

content = content.replace(
  /\.modal-overlay\.active\s*\{\s*opacity:\s*1;\s*visibility:\s*visible;\s*\}/s,
  `.modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

.modal-overlay.active .modal-content {
  transform: scale(1);
  opacity: 1;
}`
);

// 4. Products section 'În curând' Visual styling classes
// Add new helper classes at the end of the file
const helperClasses = `

/* ── UX/UI Helpers ── */
.coming-soon-banner {
  position: absolute;
  top: 20px;
  right: -30px;
  background: var(--gold);
  color: #000;
  font-weight: 800;
  font-family: var(--font-head);
  font-size: 12px;
  padding: 4px 40px;
  transform: rotate(45deg);
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
  z-index: 10;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.product-card {
  overflow: hidden; /* For the coming soon banner */
}
`;
if (!content.includes('.coming-soon-banner')) {
   content += helperClasses;
}

// 5. Testimonial Mobile Horizontal scroll fix
content = content.replace(
  /\.testimonials-scroll\s*\{\s*display:\s*flex;\s*gap:\s*24px;\s*padding-bottom:\s*40px;\s*\}/s,
  `.testimonials-scroll {
  display: flex;
  gap: 24px;
  padding-bottom: 40px;
  
  /* UX/UI Improvement: Snap scrolling on mobile */
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
}

.t-card {
  scroll-snap-align: center;
}`
);

fs.writeFileSync(path, content, 'utf8');
console.log("style.css updated");
