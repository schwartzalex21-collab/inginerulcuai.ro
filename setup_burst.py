import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

burst_section = """
  <!-- 💥 PROMPT BURST SECTION (WOW EFFECT) 💥 -->
  <section class="prompt-burst-section" id="wow-effect">
    <div class="burst-container">
      
      <!-- Central Package Indicator (The source of the explosion) -->
      <div class="burst-center-pack">
        <div class="pack-glow"></div>
        <img src="img/inginerul_logo.png" alt="Inginerul cu AI Pack" class="pack-img" onerror="this.src='https://via.placeholder.com/200x250/111827/10b981?text=SISTEMUL+AI'">
        <div class="pack-label">DEBLOCHERI...</div>
      </div>

      <!-- Floating Prompt Snippets that will explode outward -->
      <div class="floating-prompt p-top-left">
        <div class="prompt-head"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <div class="prompt-body mono-cyber">Act as a 7-figure copywriter. Write a VSL for...</div>
      </div>

      <div class="floating-prompt p-top-right">
        <div class="prompt-head"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <div class="prompt-body mono-cyber">Analyze this data table and output a JSON...</div>
      </div>

      <div class="floating-prompt p-bottom-left">
         <div class="prompt-head"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <div class="prompt-body mono-cyber">Generate 30 days of viral TikTok hooks...</div>
      </div>

      <div class="floating-prompt p-bottom-right">
         <div class="prompt-head"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <div class="prompt-body mono-cyber">Create a Python script that scrapes competitor...</div>
      </div>

      <div class="floating-prompt p-far-left">
         <div class="prompt-head"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <div class="prompt-body mono-cyber">System Prompt: You are a ruthless negotiator...</div>
      </div>

      <div class="floating-prompt p-far-right">
         <div class="prompt-head"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
        <div class="prompt-body mono-cyber">Rewrite this email sequence to maximize click-throughs...</div>
      </div>

    </div>
  </section>
  <!-- END PROMPT BURST SECTION -->
"""

# Inject before the products section
if "<!-- PRODUSE -->" in html:
    html = html.replace("<!-- PRODUSE -->", burst_section + "\n  <!-- PRODUSE -->")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Prompt Burst Layout Injected.")
