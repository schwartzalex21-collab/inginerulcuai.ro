import re

with open('rezultate.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the inner content between the <nav> (around line 210) and the <footer>
# The <main> or the sections inside 'despre.html' are `<section class="about-hero">` and `<section class="about-content">`.
# Let's extract everything from `<section class="about-hero">` to `<footer>`

new_content = """
<!-- HERO 2 -->
  <section class="page-hero">
    <div class="container hero-inner text-center">
      <div class="hero-badge fade-in">100% PRACTICE</div>
      <h1 class="fade-in hb-delay-1">Rezultate Reale Obținute</h1>
      <p class="hero-desc fade-in hb-delay-2">Descoperă puterea prompturilor noastre prin exemple concrete. Am folosit inteligența artificială exact așa cum te învățăm pe tine, iar mai jos poți vedea rezultatele generate pentru fiecare volum din <strong>Inginerul Cu AI</strong>.</p>
    </div>
  </section>

  <section class="results-page-wrapper container fade-in hb-delay-3">

    <!-- VOL 1: MARKETING -->
    <div class="result-case">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 1 — Marketing & Social Media</span>
        <h3>Analize și strategii vizuale pentru campanii</h3>
        <p>Folosind prompturile avansate din volumul de marketing, am generat instantaneu un dashboard conceptual care ne ajută să monitorizăm performanța. Designul, datele și structura campaniei au fost rafinate prin AI.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Marketing & Social Media</strong> pentru a defini KPI-urile și calendarul de content care au ghidat această strategie.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_marketing.png" alt="Rezultat Marketing">
      </div>
    </div>

    <!-- VOL 2: COPYWRITING -->
    <div class="result-case reverse">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 2 — Copywriting</span>
        <h3>Campanii de e-mail cu conversie ridicată</h3>
        <p>Acest draft pentru o campanie de e-mail a fost structurat folosind framework-uri consacrate de copywriting pe care AI-ul le-a aplicat perfect pentru o lansare de produs premium.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Copywriting</strong> pentru a genera titlurile, body-copy-ul și call-to-action-ul persuasiv.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_copywriting.png" alt="Rezultat Copywriting">
      </div>
    </div>

    <!-- VOL 3: DESIGN -->
    <div class="result-case">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 3 — Design & Creative</span>
        <h3>Identități vizuale complete generate rapid</h3>
        <p>Am instruit inteligența artificială să gândească precum un Art Director, generând un logo modern, palete de culori și mockup-uri pentru brandingul unui nou startup tech, economisind zeci de ore de muncă.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Design & Creative</strong>.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_design.png" alt="Rezultat Design">
      </div>
    </div>

    <!-- VOL 4: PRODUCTIVITY -->
    <div class="result-case reverse">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 4 — Productivity</span>
        <h3>Sisteme avansate de organizare a muncii</h3>
        <p>Am implementat structuri de productivitate pe device-uri mobile, construite și optimizate cu ajutorul AI. Notițele, task-urile și timeboxing-ul au fost generate pentru eficiență maximă.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Productivity & Organization</strong>.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_productivity.png" alt="Rezultat Productivitate">
      </div>
    </div>

    <!-- VOL 5: BUSINESS -->
    <div class="result-case">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 5 — Business</span>
        <h3>Pitch deck-uri și previziuni financiare</h3>
        <p>Un executive summary impecabil. Inteligența artificială ne-a structurat slide-urile, ne-a sumarizat punctele forte ale modelului de afaceri și ne-a generat structura proiecțiilor financiare.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Business & Strategy</strong>.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_business.png" alt="Rezultat Business">
      </div>
    </div>

    <!-- VOL 6: HEALTH -->
    <div class="result-case reverse">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 6 — Health & Wellness</span>
        <h3>Aplicații concepute pentru stilul tău de viață</h3>
        <p>Folosind un prompt specializat, creativitatea a fost deblocată pentru a structura interfața și trackerele unui plan de nutriție și fitness personalizat.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Health & Wellness</strong>.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_health.png" alt="Rezultat Health">
      </div>
    </div>

    <!-- VOL 7: PERSONAL DEV -->
    <div class="result-case">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 7 — Personal Development</span>
        <h3>Harta de dezvoltare și skill-uri</h3>
        <p>Această vizualizare a progresului personal a fost generată conceptual printr-un dialog socratic cu AI-ul, evidențiind obiceiurile zilnice care aduc cel mai mare impact pe termen lung.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Personal Development</strong>.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_personal_dev.png" alt="Rezultat Personal Dev">
      </div>
    </div>

    <!-- VOL 8: VIBE CODING -->
    <div class="result-case reverse">
      <div class="result-info">
        <span class="result-vol-tag">Vol. 8 — Vibe Coding</span>
        <h3>Cod scris de AI, coordonat de tine</h3>
        <p>De la asistență în arhitectură la sintaxe complexe. Asistentul tău personal stă în IDE-ul tău, gata să-ți accelereze dezvoltarea de soft fără să recurgi la boilerplate code manual.</p>
        <div class="used-prompt">S-a folosit un prompt din pachetul <strong>Vibe Coding</strong>.</div>
      </div>
      <div class="result-visual">
        <img src="assets/images/results/result_vibe.png" alt="Rezultat Vibe Coding">
      </div>
    </div>

  </section>
"""

# Replace between the start of <section class="about-hero"> and the start of <footer class="footer">
start_idx = content.find('<section class="page-hero">')
if start_idx == -1:
    start_idx = content.find('<section class="about-hero">')

end_idx = content.find('<footer class="footer">')

if start_idx != -1 and end_idx != -1:
    final_content = content[:start_idx] + new_content + "\n  " + content[end_idx:]
    with open('rezultate.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Rebuilt rezultate.html")
else:
    print(f"Could not find boundaries. start: {start_idx}, end: {end_idx}")

