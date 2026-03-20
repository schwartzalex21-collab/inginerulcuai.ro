import re

with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

svg_draw_logic = """
    // ══════════════════════════════════════
    // SVG LASER DRAW (Awwwards Effect)
    // ══════════════════════════════════════
    const icons = gsap.utils.toArray('.site-icon');
    icons.forEach(icon => {
      // Find the parent to use as trigger (usually product-card or feature-box)
      const triggerEl = icon.closest('.product-card, .bundle-card, .result-case, .feature-box') || icon;
      
      gsap.fromTo(icon, 
        { strokeDashoffset: 1000 },
        {
          strokeDashoffset: 0,
          duration: 1.5,
          ease: "power2.inOut",
          scrollTrigger: {
            trigger: triggerEl,
            start: "top 85%",
            onComplete: () => {
              // Add class to trigger fill transition defined in CSS
              icon.classList.add('drawn');
            }
          }
        }
      );
    });
"""

js = js.replace('// ── CLEANUP ON UNLOAD ──', svg_draw_logic + '\n// ── CLEANUP ON UNLOAD ──')

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("SVG Draw Logic Included.")
