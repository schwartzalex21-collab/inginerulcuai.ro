import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Tuples of (Volume Text or Bundle name, img_path)
replacements = [
    ("Vol. 01", "assets/popup_vol1_marketing.png"),
    ("Vol. 02", "assets/popup_vol2_copywriting.png"),
    ("Vol. 03", "assets/popup_vol3_design.png"),
    ("Vol. 04", "assets/popup_vol4_productivity.png"),
    ("Vol. 05", "assets/popup_vol5_business.png"),
    ("Vol. 06", "assets/popup_vol6_health.png"),
    ("Vol. 07", "assets/popup_vol7_personal_dev.png"),
    ("Vol. 08", "assets/popup_vol8_vibe_coding.png"),
    ("Starter", "assets/popup_starter_pack.png"),
    ("Pro", "assets/popup_pro_pack.png"),
    ("Full Collection", "assets/popup_full_collection.png")
]

# We need to find the <div class="product-icon"> that comes after each Vol. 0X
# The structure is:
# <div class="product-tag-vol">Vol. 01</div>
# <div class="product-icon"><svg class="site-icon"...</svg></div>

for keyword, img in replacements:
    # A bit complex because bundles have different tags, e.g. "Pachetul De Bază", "Starter"
    # Wait, the bundle structure might be different:
    # <h3>Pachetul "Starter"</h3>
    # Let's inspect index.html around line 700 for bundles.

    pass

# Safer way: split string by `<div class="product-icon"` and replace based on the preceding heading or tag.
# We'll handle this manually via regex for the first 8 volumes:
for i in range(1, 9):
    vol_text = f"Vol. 0{i}"
    img_name = [img for key, img in replacements if key == vol_text][0]
    
    # Regex: Look for the tag containing Vol. 0X, followed by whitespace, then <div class="product-icon">...</div>
    pattern = r'(<div class="product-tag-vol">{}</div>\s*<div class="product-icon"[^>]*>)(?:<svg[\s\S]*?</svg>(?:️)?)(</div>)'.format(vol_text)
    
    def repl(m):
        return m.group(1) + f'<img src="{img_name}" class="animated-pack-overlay" alt="{vol_text}">' + m.group(2)
        
    html = re.sub(pattern, repl, html)

# Bundle replacements (Starter, Pro, Full Collection):
bundle_replacements = [
    ("Starter", "assets/popup_starter_pack.png"),
    ("Pro", "assets/popup_pro_pack.png"),
    ("Absolut Tot", "assets/popup_full_collection.png")
]

# Bundles are mostly from line 700 onwards: <div class="bundle-card"> ... <h3>Pachetul "Starter"</h3>
for b_name, img_path in bundle_replacements:
    # Find <div class="bundle-card"> ... that contains the b_name in <h3> and swap its <div class="product-icon">
    # Because of multiline, we'll try to match the whole card block vaguely or just use exact string approach.
    pass

# For bundles, we can simply replace the site-icon svgs if we locate them accurately.
# Let's check the bundle card HTML directly:
# We know the first bundle has <svg><use href="#ico-layers"...
# Second bundle has <use href="#ico-diamond"...
# Third bundle has <use href="#ico-infinity"...

html = re.sub(r'(<div class="bundle-card"[^>]*>[\s\S]*?<div class="product-icon">)(<svg[\s\S]*?</svg>(?:️)?)(</div>[\s\S]*?<h3>Pachetul "Starter"</h3>)', 
              r'\1<img src="assets/popup_starter_pack.png" class="animated-pack-overlay" alt="Starter">\3', html)

html = re.sub(r'(<div class="bundle-card-pro"[^>]*>[\s\S]*?<div class="product-icon">)(<svg[\s\S]*?</svg>(?:️)?)(</div>[\s\S]*?<h3>Pachetul "Pro"</h3>)', 
              r'\1<img src="assets/popup_pro_pack.png" class="animated-pack-overlay" alt="Pro">\3', html)

html = re.sub(r'(<div class="bundle-card-vip"[^>]*>[\s\S]*?<div class="product-icon">)(<svg[\s\S]*?</svg>(?:️)?)(</div>[\s\S]*?<h3>Pachetul "Absolut Tot"</h3>)', 
              r'\1<img src="assets/popup_full_collection.png" class="animated-pack-overlay" alt="Full Collection">\3', html)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Product images injected.")
