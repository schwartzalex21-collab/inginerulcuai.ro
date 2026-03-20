import re

# 1. Scrap massive-arrow from HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Match the inserted arrow SVG exactly
arrow_regex = r'<svg class="massive-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">\s*<line x1="7" y1="17" x2="17" y2="7"></line>\s*<polyline points="7 7 17 7 17 17"></polyline>\s*</svg>'

html = re.sub(arrow_regex, "", html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Scrap massive-arrow styling from CSS
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Removing the specific arrow blocks appended earlier 
# including ".massive-arrow", ".arrow-hover-container .massive-arrow"
# and the "product-card > *:not(.massive-arrow)" overrides. Keep the brulatist tech cards styles.
css = re.sub(r'/\*\s*4\.\s*Massive Hover Arrows Fix\s*\*/[\s\S]*?/\*\s*5\.\s*Typography Tweaks\s*\*/', '/* 5. Typography Tweaks */', css)

# Make sure the earlier insertion in the first implementation plan is also caught
css = re.sub(r'/\*\s*Massive Hover Arrows \(Shift5 style\)\s*\*/[\s\S]*?/\*\s*Specific overrides for Product Cards to support massive arrows and cyber borders\s*\*/[\s\S]*?\}', '', css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Massive Arrows Removed.")

