import re

with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

scramble_code = """
    // ══════════════════════════════════════
    // GSAP CYBER SCRAMBLE (Hacker Text Reveal)
    // ══════════════════════════════════════
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,./<>?";
    
    document.querySelectorAll('.mono-cyber').forEach(el => {
      const originalText = el.innerText;
      
      ScrollTrigger.create({
        trigger: el,
        start: "top 95%",
        onEnter: () => {
          let iteration = 0;
          let interval = setInterval(() => {
            el.innerText = originalText
              .split("")
              .map((letter, index) => {
                if(index < iteration) return originalText[index];
                return chars[Math.floor(Math.random() * chars.length)];
              })
              .join("");
            
            if(iteration >= originalText.length) {
              clearInterval(interval);
            }
            iteration += 1 / 3; // Speed control
          }, 30);
        },
        once: true // Decode strictly once to not be annoying
      });
    });

"""

# Insert right after DOMContentLoaded and tsParticles
js = re.sub(r"(// ── L1: HERO ──)", scramble_code + r"\1", js)

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Scramble logic injected.")
