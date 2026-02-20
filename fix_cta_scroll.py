import glob

# 1. Update CSS to force the scroll-to-top button higher on mobile
css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the previous bottom: 90px rule to a stronger one.
old_css_rule = """.scroll-to-top {
    bottom: 90px;
  }"""
new_css_rule = """.scroll-to-top {
    bottom: 95px !important;
  }"""

if old_css_rule in css_content:
    css_content = css_content.replace(old_css_rule, new_css_rule)
else:
    # Just in case it's formatted differently
    css_content += "\n@media (max-width: 768px) { .scroll-to-top { bottom: 95px !important; } }\n"

# The user wants the CTA to be a single button: "Cumpără 8 volume colecția completă"
# We also want to update the styling of the container to center this single button perfectly.
css_new_cta_layout = """
/* Mobile CTA Full Width Override */
.mobile-floating-cta .m-cta-btn {
  width: 100%;
  text-align: center;
  font-size: 15px;
  font-weight: 800;
  text-transform: uppercase;
  padding: 14px 20px;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 15px rgba(243, 156, 18, 0.4);
}
.mobile-floating-cta .m-cta-content {
  justify-content: center;
}
"""
if "/* Mobile CTA Full Width Override */" not in css_content:
    css_content += css_new_cta_layout

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update all HTML files that have the Mobile Floating CTA, and add to results page
# First, define what the new HTML looks like:
new_mobile_cta_html = """  <!-- MOBILE FLOATING CTA -->
  <div class="mobile-floating-cta" id="mobileCta">
    <div class="m-cta-content">
      <a href="shop.html#collection" class="btn-primary m-cta-btn">Cumpără 8 Volume Colecția Completă</a>
    </div>
  </div>"""

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False

    # If it already has the old CTA, replace it entirely
    if 'id="mobileCta"' in content:
        import re
        content = re.sub(r'<!-- MOBILE FLOATING CTA -->.*?</div>\s*</div>', new_mobile_cta_html, content, flags=re.DOTALL)
        modified = True
    else:
        # If it doesn't have it (like dezvoltate.html / rezultate.html), inject it right above the scrollToTop button
        if '<button id="scrollToTop"' in content:
            content = content.replace('<button id="scrollToTop"', new_mobile_cta_html + '\n  <button id="scrollToTop"')
            modified = True

    # ensuring scroll to top is actually there just in case
    scroll_btn = '<button id="scrollToTop"'
    if scroll_btn not in content and '</body>' in content:
        content = content.replace('</body>', '<button id="scrollToTop" class="scroll-to-top" aria-label="Scroll to top">↑</button>\n</body>')
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated Mobile CTA and Scroll-to-Top CSS logic on all pages.")
