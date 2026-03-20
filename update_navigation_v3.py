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
        # We only mark active if the filename exactly matches the href
        # This is simple but works for flat structures
        active_class = ' class="active"' if href == active_page else ''
        links_html += f'        <li><a href="{href}"{active_class}>{label}</a></li>\n'
    return f'      <ul class="nav-links">\n{links_html}        <li></li>\n      </ul>'

def generate_mobile_menu(active_page):
    mobile_html = "".join([f'<a href="{href}">{label}</a>' for href, label in links])
    return f'<div class="mobile-menu" id="mobileMenu">{mobile_html}<a href="shop.html" class="btn-mobile">Vezi Produsele →</a></div>'

# WALK through all subdirectories
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".html"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Use original filename as active_page for class="active" logic
            # This works if the subdirectories mirror the root structure (which dev_archives seems to do)
            active_page = filename 
            
            # Robust replacement for nav-links
            nav_pattern = r'\s*<ul class="nav-links">[\s\S]*?</ul>'
            new_nav = generate_nav_html(active_page)
            if re.search(nav_pattern, content):
                content = re.sub(nav_pattern, "\n" + new_nav, content)
            
            # Robust replacement for mobile-menu
            mobile_pattern = r'\s*<div class="mobile-menu" id="mobileMenu">[\s\S]*?</div>'
            new_mobile = generate_mobile_menu(active_page)
            if re.search(mobile_pattern, content):
                content = re.sub(mobile_pattern, "\n    " + new_mobile, content)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated: {file_path}")
