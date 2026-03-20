import re

with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

burst_js = """
    // ══════════════════════════════════════
    // WOW EFFECT: PROMPT BURST EXPLOSION
    // ══════════════════════════════════════
    const burstSection = document.querySelector('.prompt-burst-section');
    if(burstSection) {
      const packImg = burstSection.querySelector('.pack-img');
      const packLabel = burstSection.querySelector('.pack-label');
      const floatingPrompts = gsap.utils.toArray('.floating-prompt');
      
      // Setup initial state: everything is in the center, scale 0, opacity 0
      gsap.set(floatingPrompts, { 
        xPercent: -50, yPercent: -50, 
        scale: 0.1, autoAlpha: 0, 
        rotationX: 0, rotationY: 0, rotationZ: 0 
      });

      // The destination coordinates roughly spread out
      // 0: top-left, 1: top-right, 2: bottom-left, 3: bottom-right, 4: far-left, 5: far-right
      const dests = [
        { x: -350, y: -200, rZ: -15, scale: 0.9 },
        { x: 350, y: -180, rZ: 10, scale: 1 },
        { x: -300, y: 150, rZ: 8, scale: 0.8 },
        { x: 280, y: 200, rZ: -12, scale: 0.95 },
        { x: -550, y: -20, rZ: -5, scale: 0.7 },
        { x: 500, y: 40, rZ: 20, scale: 0.85 }
      ];

      const burstTl = gsap.timeline({
        scrollTrigger: {
          trigger: burstSection,
          start: "top 60%", 
          end: "bottom 80%",
          toggleActions: "play none none reverse"
        }
      });

      // 1. Pack vibrates/charges up
      burstTl.fromTo(packImg, 
        { scale: 1, filter: "brightness(1)", rotation: 0 },
        { scale: 1.1, filter: "brightness(1.5)", rotation: 2, duration: 0.4, yoyo: true, repeat: 1, ease: "power2.inOut" }
      )
      // 2. BOOM: Prompts fly out
      .to(floatingPrompts, {
        duration: 1.5,
        ease: "expo.out",
        autoAlpha: 1,
        x: (index) => dests[index % dests.length].x,
        y: (index) => dests[index % dests.length].y,
        scale: (index) => dests[index % dests.length].scale,
        rotationZ: (index) => dests[index % dests.length].rZ,
        stagger: 0.05
      }, "-=0.2")
      // 3. Make them float slightly afterwards
      .to(floatingPrompts, {
        y: "+=15",
        duration: 2,
        ease: "sine.inOut",
        yoyo: true,
        repeat: -1,
        stagger: { amount: 1, from: "random" }
      });
      
      // Floating pack animation constantly
      gsap.to(packImg, {
        y: -15,
        rotationY: 5,
        rotationX: 5,
        duration: 3,
        ease: "sine.inOut",
        yoyo: true,
        repeat: -1
      });
    }
"""

js = js.replace('// ── CLEANUP ON UNLOAD ──', burst_js + '\n// ── CLEANUP ON UNLOAD ──')

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Burst Animation Setup.")
