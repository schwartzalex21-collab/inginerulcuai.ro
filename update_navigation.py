import os
import re

# Navigation labels mapping
links = [
    ("index.html", "Sisteme"),
    ("shop.html", "Pachete"),
    ("despre.html", "Povestea"),
    ("rezultate.html", "Rezultate"),
    ("blog.html", "Cazuri Reale"),
    ("contact.html", "Suport")
]

def generate_nav_html(active_page):
    links_html = ""
    for href, label in links:
        active_class = ' class="active"' if href == active_page else ''
        links_html += f'        <li><a href="{href}"{active_class}>{label}</a></li>\n'
    
    return f"""      <ul class="nav-links">
{links_html}        <li></li>
      </ul>"""

def generate_mobile_menu(active_page):
    mobile_html = ""
    for href, label in links:
        # Check if the href matches the active page
        # Note: mobile menu usually doesn't have an 'active' class in this template's existing code
        mobile_html += f'<a href="{href}">{label}</a>'
    
    return f"""    <div class="mobile-menu" id="mobileMenu">
      {mobile_html}
      <a href="shop.html" class="btn-mobile">Vezi Produsele →</a>
    </div>"""

# Iterate through all html files
for filename in os.listdir("."):
    if filename.endswith(".html"):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. Update Desktop Nav Links
        nav_pattern = r'      <ul class="nav-links">[\s\S]*?</ul>'
        new_nav = generate_nav_html(filename)
        content = re.sub(nav_pattern, new_nav, content)
        
        # 2. Update Mobile Menu
        mobile_pattern = r'    <div class="mobile-menu" id="mobileMenu">[\s\S]*?</div>'
        new_mobile = generate_mobile_menu(filename)
        content = re.sub(mobile_pattern, new_mobile, content)
        
        # 3. Update active class on index if necessary (some pages use Acasa instead of Sisteme)
        # The above logic already handles active class in generate_nav_html
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated navigation in {filename}")

