import re

# 1. Update Blog Read Times
with open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

read_times = {
    '15 Ian 2026': '15 Ian 2026 • ⏳ 4 min read',
    '20 Ian 2026': '20 Ian 2026 • ⏳ 3 min read',
    '25 Ian 2026': '25 Ian 2026 • ⏳ 6 min read',
    '1 Feb 2026': '1 Feb 2026 • ⏳ 5 min read',
    '5 Feb 2026': '5 Feb 2026 • ⏳ 3 min read',
    '10 Feb 2026': '10 Feb 2026 • ⏳ 4 min read'
}

for old, new in read_times.items():
    if old in blog_content:
        blog_content = blog_content.replace(f'<span>{old}</span>', f'<span>{new}</span>')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_content)


# 2. Add Trust Badges to Modals (index.html & shop.html)
# We look for: <a href="https://example.com/checkout" ... class="modal-btn"...>...</a>
# And insert trust badges right below it.
trust_badges_html = """
          <div class="trust-badges" style="display:flex; justify-content:center; gap:12px; margin-top:12px; opacity:0.8;">
            <div style="display:flex; align-items:center; gap:4px; font-size:11px; color:var(--gray);"><span style="color:var(--gold)">🔒</span> Plată Securizată</div>
            <div style="display:flex; align-items:center; gap:4px; font-size:11px; color:var(--gray);"><span style="color:var(--emerald)">⚡</span> Livrare Instant</div>
            <div style="display:flex; align-items:center; gap:4px; font-size:11px; color:var(--gray);"><span style="color:#3498db">🛡️</span> Garanție 14 Zile</div>
          </div>
"""

def add_trust_badges(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find the end of the modal-price-box closing div
    # Actually, let's just replace the closing </div> of modal-price-box.
    # Pattern: <div class="modal-price-box"> ... </div>
    # A robust way is to inject right after the modal-btn
    
    # We will replace `</a>\n          </div>` with `</a>\n` + trust_badges_html + `          </div>`
    # Check if we already injected
    if 'class="trust-badges"' not in content:
        content = re.sub(r'(<a href="[^"]*checkout".*?</a>)\s*</div>', r'\1' + trust_badges_html + '          </div>', content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

add_trust_badges('index.html')
add_trust_badges('shop.html')


# 3. Add Mobile Floating CTA (index.html & shop.html)
# Insert right before the closing </body> tag.
mobile_cta_html = """
  <!-- MOBILE FLOATING CTA -->
  <div class="mobile-floating-cta" id="mobileCta">
    <div class="m-cta-content">
      <div class="m-cta-text">
        <span class="m-cta-title">Alege Un Volum</span>
        <span class="m-cta-price">de la 49 RON</span>
      </div>
      <a href="shop.html" class="btn-primary m-cta-btn">Vezi Produsele</a>
    </div>
  </div>
"""

def add_mobile_cta(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'id="mobileCta"' not in content:
        content = content.replace('<button id="scrollToTop"', mobile_cta_html + '\n  <button id="scrollToTop"')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

add_mobile_cta('index.html')
add_mobile_cta('shop.html')
print("Blog times, Trust Badges, and Mobile CTA injected.")
