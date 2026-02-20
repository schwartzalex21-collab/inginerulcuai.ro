import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# LEFT BOOKS:
# <div class="hero-books-left" aria-hidden="true">
#   <div class="hbook hb-l1">
#     <div class="hbook-spine"></div>
#     <div class="hbook-label">MARKETING</div>
#   </div>
#   <div class="hbook hb-l2">
#     <div class="hbook-spine"></div>
#     <div class="hbook-label">BUSINESS</div>
#   </div>
#   <div class="hbook hb-l3">
#     <div class="hbook-spine"></div>
#     <div class="hbook-label">COPYWRITING</div>
#   </div>
# </div>

new_left_books = """<div class="hero-books-left" aria-hidden="true">
      <div class="hbook hb-l1">
        <div class="hbook-spine hbook-spine-green"></div>
        <div class="hbook-label">MARKETING</div>
      </div>
      <div class="hbook hb-l2">
        <div class="hbook-spine"></div>
        <div class="hbook-label">BUSINESS</div>
      </div>
      <div class="hbook hb-l3">
        <div class="hbook-spine hbook-spine-dim"></div>
        <div class="hbook-label">COPYWRITING</div>
      </div>
      <div class="hbook hb-l4">
        <div class="hbook-spine hbook-spine-green"></div>
        <div class="hbook-label">HEALTH</div>
      </div>
    </div>"""

left_pattern = r'<div class="hero-books-left".*?</div>\s*</div>\s*</div>\s*</div>'
content = re.sub(left_pattern, new_left_books, content, flags=re.DOTALL)

# Let's manually find and replace because regex with greedy matches might fail.
start_left = content.find('<div class="hero-books-left"')
if start_left != -1:
    end_left = content.find('</div>\n\n    <!-- Conținut centrat -->', start_left) + 6
    if end_left > 6:
        content = content[:start_left] + new_left_books + content[end_left:]


# RIGHT BOOKS:
# <div class="hero-books-right" aria-hidden="true">
#   <div class="hbook hb-r1">
#     <div class="hbook-spine hbook-spine-green"></div>
#     <div class="hbook-label">DESIGN</div>
#   </div>
#   <div class="hbook hb-r2">
#     <div class="hbook-spine hbook-spine-dim"></div>
#     <div class="hbook-label">PRODUCTIVITY</div>
#   </div>
#   <div class="hbook hb-r3">
#     <div class="hbook-spine"></div>
#     <div class="hbook-label">PERSONAL DEV</div>
#   </div>
# </div>

new_right_books = """<div class="hero-books-right" aria-hidden="true">
      <div class="hbook hb-r1">
        <div class="hbook-spine hbook-spine-green"></div>
        <div class="hbook-label">DESIGN</div>
      </div>
      <div class="hbook hb-r2">
        <div class="hbook-spine hbook-spine-dim"></div>
        <div class="hbook-label">PRODUCTIVITY</div>
      </div>
      <div class="hbook hb-r3">
        <div class="hbook-spine"></div>
        <div class="hbook-label">PERSONAL DEV</div>
      </div>
      <div class="hbook hb-r4">
        <div class="hbook-spine hbook-spine-dim"></div>
        <div class="hbook-label">VIBE CODING</div>
      </div>
    </div>"""

start_right = content.find('<div class="hero-books-right"')
if start_right != -1:
    end_right = content.find('</div>\n\n  </section>', start_right) + 6
    if end_right > 6:
        content = content[:start_right] + new_right_books + content[end_right:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero books updated.")
