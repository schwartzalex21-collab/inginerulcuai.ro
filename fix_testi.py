import re

cards_data = [
    {
        "name": "Radu",
        "img": "radu-d.jpg",
        "text": "Am aplicat strategia din Volumul 1 pe un cont nou de Instagram. Aseară am pus un reel făcut cu sistemele voastre, dimineața aveam 3 comenzi de 100€ fiecare."
    },
    {
        "name": "Maria",
        "img": "maria-p.jpg",
        "text": "Nu credeam că poți face bani doar din prompturi de AI. Am trimis un singur email scris cu Volumul 2 unei liste mici, a generat vânzări de peste 3000 de lei în doar câteva ore. Nebunie curată!"
    },
    {
        "name": "Cosmin",
        "img": "cosmin-t.jpg",
        "text": "Folosesc Ultimate Pack de o lună. Am închis trei clienți internaționali pe design ($1500 fiecare), totul livrat prin tool-urile recomandate aici."
    },
    {
        "name": "Andrei",
        "img": "andrei-b.jpg",
        "text": "Sunt începător în business dar cu Volumul 5 m-am lansat. Prezentarea de pitch mi-a adus rapid un client imobiliar dispus să îmi plătească 500 Euro pe lună."
    },
    {
        "name": "Laura",
        "img": "laura-v.jpg",
        "text": "Mi-am amortizat investiția în 2 zile. Cu scripturile din Volumul 2 am reușit să cresc conversia site-ului meu cu 45%. Sute de euro profit extra zilnic."
    },
    {
        "name": "Gabi",
        "img": "gabriel-h.jpg",
        "text": "Luam 1500 lei salariu fix. Am creat o agenție mică, folosesc prompturile să generez campanii FB Ads pt clienți. După 2 luni fac de 4 ori mai mult stând pe laptop."
    },
    {
        "name": "Diana",
        "img": "diana-s.jpg",
        "text": "Am fost sceptic de mesaje, dar volumul despre Vibe Coding m-a ajutat să generez un script Python simplu pe care-l vând cu 20$ online. 40 vânzări luna asta automat."
    },
    {
        "name": "Florin",
        "img": "florin-c.jpg",
        "text": "Eu ofer consultanță fitness. Cu planurile alimentare generate curat în câteva secunde, pot lua de trei ori mai mulți clienți."
    },
    {
        "name": "Alex",
        "img": "alexandru-m.jpg",
        "text": "Cel mai bun pachet pentru cine vrea cash pasiv. Folosesc sistemele să structurez canale de YouTube Faceless. Creștere spectaculoasă, primii $800 făcuți noaptea."
    },
    {
        "name": "Ioana",
        "img": "ioana-c.jpg",
        "text": "Am aplicat strategiile de Business din Vol 5 și mi-am lansat un E-commerce. Profit 400 RON chiar din a treia zi de Ads."
    }
]

# We duplicate the first 3 for the infinite loop effect as in the original 
cards_data.extend(cards_data[:3])

wa_cards_html = ""
for c in cards_data:
    wa_cards_html += f"""        <div class="wa-card">
          <div class="wa-header">
            <img src="assets/images/{c['img']}" alt="{c['name']}" class="wa-avatar">
            <div class="wa-contact">
              <strong>{c['name']}</strong>
              <span>Online</span>
            </div>
          </div>
          <div class="wa-body">
            <div class="wa-msg wa-received">
              <p>{c['text']}</p>
              <span class="wa-time">14:24</span>
            </div>
            <div class="wa-msg wa-sent">
              <p>Top! 🔥 Mă bucur enorm să aud asta!</p>
              <span class="wa-time">14:30 <svg viewBox="0 0 16 11" width="16" height="11"><path d="M11.8 1.6L6.5 7.4 4.1 4.7 2.8 5.8 6.5 9.9 13.1 2.7zM15.4 2.7L8.8 9.9 7.5 8.5 8.8 7.1 14.1 1.6z" fill="#53BCDA"></path></svg></span>
            </div>
          </div>
        </div>\n"""

# Full testimonials block replacement
testimonials_full = f"""  <!-- TESTIMONIALE — CAROUSEL INFINIT -->
  <section class="testimonials-section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Ce Spun Clienții Noștri</span>
        <h2>Bani Făcuți Pe Bune</h2>
        <p>Avem peste 1200+ hustlers activi în ecosistem. Iată ce rezultate au obținut aplicând exact sistemele din interior.</p>
      </div>
    </div>

    <!-- ROW 1 -->
    <div class="testimonials-track-wrap">
      <div class="testimonials-scroll" id="row1">
{wa_cards_html}      </div>
    </div>
  </section>"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace block from <!-- TESTIMONIALE — CAROUSEL INFINIT --> to </section> 
# Careful: there is another section right after, usually 'Ghiduri' or 'Footer'
html = re.sub(r'<!-- TESTIMONIALE — CAROUSEL INFINIT -->.*?</section>', testimonials_full.replace('\\', '\\\\'), html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
