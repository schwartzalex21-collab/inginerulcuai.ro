import re

with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

particles_code = """
  // ══════════════════════════════════════
  // WEBGGL PARTICLES (Neural Network)
  // ══════════════════════════════════════
  if (typeof tsParticles !== 'undefined') {
    tsParticles.load("tsparticles", {
      preset: "links",
      background: {
        color: { value: "transparent" },
      },
      particles: {
        color: { value: "#10b981" },
        links: {
          color: "#10b981",
          distance: 150,
          enable: true,
          opacity: 0.2,
          width: 1,
        },
        move: {
          enable: true,
          speed: 1,
          direction: "none",
          random: false,
          straight: false,
          outModes: "out",
        },
        number: {
          density: { enable: true, area: 800 },
          value: 60,
        },
        opacity: { value: 0.5 },
        shape: { type: "circle" },
        size: { value: { min: 1, max: 3 } },
      },
      interactivity: {
        events: {
          onHover: { enable: true, mode: "grab" },
        },
        modes: {
          grab: { distance: 200, links: { opacity: 0.5 } },
        },
      },
      detectRetina: true,
    });
  }

"""

# Insert right after DOMContentLoaded
js = re.sub(r"document\.addEventListener\('DOMContentLoaded', \(\) => \{\n", "document.addEventListener('DOMContentLoaded', () => {\n" + particles_code, js)

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("tsParticles logic injected.")
