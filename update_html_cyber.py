import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inject Massive Arrow SVG into product-cards and bundle-cards
# Find <div class="product-card[*]"> and append arrow right inside
arrow_svg = '''\n      <svg class="massive-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <line x1="7" y1="17" x2="17" y2="7"></line>
        <polyline points="7 7 17 7 17 17"></polyline>
      </svg>'''

# Product cards
html = re.sub(r'(<div class="product-card[^>]*>)', r'\1' + arrow_svg, html)

# Bundle cards
html = re.sub(r'(<div class="bundle-card[^>]*>)', r'\1' + arrow_svg, html)

# 2. Add Monospace class to prices and stats
# Product Prices
html = re.sub(r'(<div class="product-price">)([^<]+</div>)', r'\1<span class="mono-cyber">\2</span>', html)
# Bundle Prices
html = re.sub(r'(<span class="bundle-price">)([^<]+</span>)', r'\1<span class="mono-cyber">\2</span>', html)
# CTA Prices
html = re.sub(r'(<span class="cta-price-new">)([^<]+</span>)', r'\1<span class="mono-cyber">\2</span>', html)
html = re.sub(r'(<span class="cta-old">)([^<]+</span>)', r'\1<span class="mono-cyber">\2</span>', html)

# Stats inside the hero section (X+ utilizatori)
html = re.sub(r'(<div class="hero-stat">)(\s*)(<strong>)(\s*)(<span class="stat-num[^"]*">[^<]+</span>[^<]*</strong>)', r'\1\2\3\4<span class="mono-cyber">\5</span>', html)
# Make sure we don't mess up existing formats - better to replace just the stat-num
html = re.sub(r'(<span class="stat-num"[^>]*>)([^<]+)(</span>)', r'\1<span class="mono-cyber">\2</span>\3', html)

# 3. Add pulsing dot to the first "Oportunitate Limitată" or near the CTA
# Let's replace the <span class="section-tag">Oportunitate Limitată</span> in the CTA with the pulsing dot version
dot_html = '''<div class="status-dot-wrap"><span class="status-dot"></span>Oportunitate Limitată</div>'''
html = html.replace('<span class="section-tag">Oportunitate Limitată</span>', dot_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML cyber injection complete.")
