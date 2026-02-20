faq_html = """
  <!-- ══════════════════════════════════════
     ÎNTREBĂRI FRECVENTE (FAQ)
  ══════════════════════════════════════ -->
  <section class="faq-section" id="faq">
    <div class="container">
      <div class="section-header fade-in">
        <span class="section-tag">Întrebări Frecvente</span>
        <h2>Ai nelămuriri?<br><span class="gold">Avem răspunsurile.</span></h2>
        <p>Tot ce trebuie să știi înainte de a accesa colecția Inginerul Cu AI.</p>
      </div>
      
      <div class="faq-grid fade-in">
        <details class="faq-item">
          <summary>Este un abonament lunar?</summary>
          <div class="faq-answer">
            Nu. Plata este una unică (one-time fee). Odată ce achiziționezi un volum sau un pachet, prompturile îți rămân accesibile pe viață. Nu există costuri ascunse.
          </div>
        </details>
        <details class="faq-item">
          <summary>Primesc factură pe persoană juridică (firmă)?</summary>
          <div class="faq-answer">
            Sigur că da! La pagina de plată (Checkout) vei avea opțiunea de a introduce detaliile companiei tale (CUI, Registrul Comerțului etc.) și factura fiscală se va genera și trimite automat pe email.
          </div>
        </details>
        <details class="faq-item">
          <summary>Se potrivesc aceste prompturi chiar dacă sunt începător?</summary>
          <div class="faq-answer">
            Absolut. Am construit fiecare volum presupunând că utilizatorul nu a mai folosit ChatGPT la nivel avansat niciodată. Fiecare prompt vine la pachet cu instrucțiuni clare de tip "Copy & Paste" și o explicație a mecanismului din spate.
          </div>
        </details>
        <details class="faq-item">
          <summary>Primesc acces la viitoarele actualizări (Updates)?</summary>
          <div class="faq-answer">
            Da! Dacă achiziționezi <strong style="color:var(--gold)">8 Volumes Full Collection</strong>, ai garantate toate actualizările și edițiile noi pe care le vom lansa, direct în contul tău sau pe email, complet gratuit.
          </div>
        </details>
      </div>
    </div>
  </section>
"""

# Insert right before <section class="cta-section"> or before <footer>
# Let's insert it before the cta-section so the user reads FAQ, gets convinced, then hits the final CTA.

def add_faq(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="faq"' not in content:
        content = content.replace('<section class="cta-section">', faq_html + '\n  <section class="cta-section">')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

add_faq('index.html')
add_faq('shop.html')
print("FAQ Interactive Accordion injected.")
