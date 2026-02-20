import re

html_to_insert = """
  <!-- BUNDLE 1: STARTER PACK -->
  <div class="modal-overlay" id="modal-bundle1">
    <div class="modal-content" style="border-color: rgba(46, 204, 113, 0.4); box-shadow: 0 20px 80px rgba(46, 204, 113, 0.15); border-width: 2px;">
      <button class="modal-close">&times;</button>
      <div class="modal-grid">
        <div class="modal-left">
          <img src="assets/laptop_vol1.png" alt="Exemplu Starter Pack" class="modal-image">
          <ul class="modal-left-features">
            <li>Echilibrul perfect pret-valoare</li>
            <li>Îmbină skill-urile pe care le vrei</li>
            <li>60 Prompturi premium totale</li>
          </ul>
        </div>
        <div class="modal-right">
          <span class="modal-tag" style="background: rgba(46,204,113,0.1); color: var(--emerald); border-color: rgba(46,204,113,0.3);">Pachet Promoțional</span>
          <h2 class="modal-title">Starter Pack (Orice 3 Volume)</h2>
          <p class="modal-desc">Ai nevoie doar de anumite arii pentru a performa? Pachetul Starter îți permite să selectezi exact cele 3 arii în care vrei să folosești inteligența artificială, la un preț redus masiv.</p>
          
          <div class="modal-includes">
            <h4>Ce este inclus:</h4>
            <ul>
              <li><strong>3 Volume</strong> (60 Prompturi)</li>
              <li>Acces nelimitat imediat</li>
              <li>Instrucțiuni complete per volum</li>
              <li>Format PDF pe orice device</li>
            </ul>
          </div>
          
          <div class="modal-price-box">
            <span class="modal-price-val">79 RON</span>
            <a href="https://example.com/checkout" class="modal-btn" style="background:#2ecc71; color:#fff;">Alege Volumele</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- BUNDLE 2: PRO PACK -->
  <div class="modal-overlay" id="modal-bundle2">
    <div class="modal-content" style="border-color: #9b59b6; box-shadow: 0 20px 80px rgba(155, 89, 182, 0.15); border-width: 2px;">
      <button class="modal-close">&times;</button>
      <div class="modal-grid">
        <div class="modal-left">
          <img src="assets/laptop_vol1.png" alt="Exemplu Pro Pack" class="modal-image">
          <ul class="modal-left-features">
            <li>Acoperi ariile majore de business</li>
            <li>Îmbină skill-urile pe care le vrei</li>
            <li>100 Prompturi premium totale</li>
          </ul>
        </div>
        <div class="modal-right">
          <span class="modal-tag" style="background: rgba(155,89,182,0.1); color: #c39bd3; border-color: rgba(155,89,182,0.3);">Pachet Pro</span>
          <h2 class="modal-title">Pro Pack (Orice 5 Volume)</h2>
          <p class="modal-desc">Fii pregătit pentru orice provocare. Pachetul Pro îți permite să selectezi 5 volume la alegere, oferindu-ți 100 de prompturi premium la un preț incredibil de bun.</p>

          <div class="modal-includes">
            <h4>Ce este inclus:</h4>
            <ul>
              <li><strong>5 Volume</strong> (100 Prompturi)</li>
              <li>Acces nelimitat imediat</li>
              <li>Instrucțiuni complete per volum</li>
              <li>Format PDF pe orice device</li>
            </ul>
          </div>

          <div class="modal-price-box">
            <span class="modal-price-val">139 RON</span>
            <a href="https://example.com/checkout" class="modal-btn" style="background:#9b59b6; color:#fff;">Alege Volumele</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- BUNDLE 3: FULL COLLECTION -->
  <div class="modal-overlay" id="modal-bundle3">
    <div class="modal-content" style="border-color: var(--gold); box-shadow: 0 20px 100px rgba(243,156,18, 0.25); border-width: 2px; background: linear-gradient(145deg, var(--bg2), var(--card-bg));">
      <button class="modal-close">&times;</button>
      <div class="modal-grid">
        <div class="modal-left">
          <img src="assets/laptop_vol1.png" alt="Exemplu Full Collection" class="modal-image">
          <ul class="modal-left-features">
            <li>Arsenalu COMPLET (160 Prompturi)</li>
            <li>Cea mai bună investiție garantată</li>
            <li>Actualizări suportate</li>
          </ul>
        </div>
        <div class="modal-right">
          <span class="modal-tag" style="background: rgba(243,156,18,0.2); border-color: var(--gold);">Ofertă de Nerefusat</span>
          <h2 class="modal-title">8 Volumes Full Collection</h2>
          <p class="modal-desc">Transformă-te într-un adevărat maestru al inteligenței artificiale. De la Marketing și Business, până la Vibe Coding și Dezvoltare Personală, cu acest pachet le ai absolut pe toate. Zeci de ore economisite garantat.</p>
          
          <div class="modal-includes">
            <h4>Ce obții azi:</h4>
            <ul>
              <li>🔥 MARKETING & SOCIAL MEDIA</li>
              <li>🔥 COPYWRITING</li>
              <li>🔥 DESIGN & CREATIVE</li>
              <li>🔥 PRODUCTIVITY</li>
              <li>🔥 BUSINESS</li>
              <li>🔥 HEALTH & WELLNESS</li>
              <li>🔥 PERSONAL DEVELOPMENT</li>
              <li>🔥 VIBE CODING</li>
            </ul>
          </div>
          
          <div class="modal-price-box">
            <span class="modal-price-val">199 RON</span>
            <a href="https://example.com/checkout" class="modal-btn">Cumpără Tot Acum</a>
          </div>
        </div>
      </div>
    </div>
  </div>
"""

def replace_modals(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where the bundle modals start
    start_tag = '<div class="modal-overlay" id="modal-bundle1">'
    end_tag = '</body>'
    
    start_idx = content.find(start_tag)
    end_idx = content.rfind(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + html_to_insert + "\n" + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced modals in {filepath}")
    else:
        print(f"Failed to find boundaries in {filepath} (len start_idx: {start_idx}, end_idx: {end_idx})")
        # Try finding bundle1 another way since it might have been mangled
        alt_start = '<div class="modal-overlay" id="modal-bundle'
        start_idx = content.find(alt_start)
        if start_idx != -1 and end_idx != -1:
            new_content = content[:start_idx] + html_to_insert + "\n" + content[end_idx:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced modals in {filepath} (alt match)")
            

replace_modals('index.html')
replace_modals('shop.html')
