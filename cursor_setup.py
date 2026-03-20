import re

# 1. Add cursor element to HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

cursor_div = '<div class="cursor-dot"><span class="cursor-text"></span></div>\n'
html = re.sub(r'(<body[^>]*>)', r'\1\n' + cursor_div, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Add cursor JS to main.js
with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

cursor_js = """
  // ══════════════════════════════════════
  // CUSTOM CURSOR LOGIC
  // ══════════════════════════════════════
  const cursorDot = document.querySelector('.cursor-dot');
  const cursorText = document.querySelector('.cursor-text');
  
  if(cursorDot) {
    // Follow mouse
    window.addEventListener('mousemove', (e) => {
      // Small delay for smooth trailing effect
      gsap.to(cursorDot, {
        x: e.clientX,
        y: e.clientY,
        duration: 0.15,
        ease: "power2.out"
      });
    });

    // Hover States for Products
    const products = document.querySelectorAll('.product-card, .bundle-card');
    products.forEach(p => {
      p.addEventListener('mouseenter', () => {
        cursorDot.classList.add('cursor-hover-product');
        cursorText.innerText = "EXAMINEAZĂ";
      });
      p.addEventListener('mouseleave', () => {
        cursorDot.classList.remove('cursor-hover-product');
        cursorText.innerText = "";
      });
    });

    // Hover logic for normal links/buttons
    const links = document.querySelectorAll('a, button');
    links.forEach(l => {
      l.addEventListener('mouseenter', () => {
        if(!l.closest('.product-card') && !l.closest('.bundle-card')) {
          cursorDot.classList.add('cursor-hover-arrow');
        }
      });
      l.addEventListener('mouseleave', () => {
         cursorDot.classList.remove('cursor-hover-arrow');
      });
    });
  }

"""
# Append right before end of init GSAP
js = js.replace('// ── CLEANUP ON UNLOAD ──', cursor_js + '\n// ── CLEANUP ON UNLOAD ──')

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Cursor Logic Included.")
