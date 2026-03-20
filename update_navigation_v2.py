import os
import re

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
    return f'      <ul class="nav-links">\n{links_html}        <li></li>\n      </ul>'

def generate_mobile_menu(active_page):
    mobile_html = "".join([f'<a href="{href}">{label}</a>' for href, label in links])
    return f'<div class="mobile-menu" id="mobileMenu">{mobile_html}<a href="shop.html" class="btn-mobile">Vezi Produsele →</a></div>'

for filename in os.listdir("."):
    if filename.endswith(".html"):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Robust replacement for nav-links - matching regardless of leading whitespace
        nav_pattern = r'\s*<ul class="nav-links">[\s\S]*?</ul>'
        new_nav = generate_nav_html(filename)
        content = re.sub(nav_pattern, "\n" + new_nav, content)
        
        # Robust replacement for mobile-menu
        mobile_pattern = r'\s*<div class="mobile-menu" id="mobileMenu">[\s\S]*?</div>'
        new_mobile = generate_mobile_menu(filename)
        content = re.sub(mobile_pattern, "\n    " + new_mobile, content)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Standardized navigation in {filename}")
