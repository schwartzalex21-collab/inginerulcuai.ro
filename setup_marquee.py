import re

with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

marquee_logic = """
    // ══════════════════════════════════════
    // VELOCITY MARQUEE (Awwwards Effect)
    // ══════════════════════════════════════
    const marqueeParts = gsap.utils.toArray('.marquee-part');
    if(marqueeParts.length > 0) {
      // Create a seamless loop timeline for the marquee
      const marqueeTl = gsap.to(marqueeParts, {
        xPercent: -100,
        repeat: -1,
        duration: 20,
        ease: "none"
      });
      
      // Update timeScale based on Lenis scroll velocity
      if(lenis) {
        lenis.on('scroll', (e) => {
          // Base speed is 1. If velocity is high, add it to the speed.
          // Direction matters: scrolling down = positive velocity -> forward speed
          // scrolling up = negative velocity -> backward speed 
          let vel = e.velocity || 0;
          let newSpeed = 1 + (vel * 0.5); 
          
          gsap.to(marqueeTl, {
            timeScale: newSpeed,
            duration: 0.2, // smoothing the acceleration
            overwrite: true
          });
          
          // Return to normal speed when scroll stops
          gsap.to(marqueeTl, {
            timeScale: 1,
            duration: 1, // slower deceleration
            delay: 0.2, // wait a bit
            overwrite: "auto"
          });
        });
      }
    }
"""

js = js.replace('// ── CLEANUP ON UNLOAD ──', marquee_logic + '\n// ── CLEANUP ON UNLOAD ──')

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("Velocity Marquee configured.")
