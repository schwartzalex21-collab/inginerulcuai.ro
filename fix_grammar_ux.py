import re
import glob

# 1. Grammar Fixes across all HTML files
html_files = glob.glob('*.html')

corrections = [
    ("ceva ce nutri i ionist mi-ar fi luat ore", "ceva ce unui nutriționist i-ar fi luat ore"),
    ("Arsenalu COMPLET", "Arsenalul COMPLET"),
    ("astea în română sunt net superioare", "acestea în română sunt net superioare"),
    ("Îmbină skill-urile pe care le vrei", "Combină skill-urile de care ai nevoie"),
    ("Am folosit inteligența artificială exact așa cum te învățăm pe tine", "Am folosit inteligența artificială exact așa cum te învățăm și pe tine")
]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in corrections:
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    # Add scroll to top button right before closing body tag in all HTML files
    scroll_btn = '<button id="scrollToTop" class="scroll-to-top" aria-label="Scroll to top">↑</button>\n</body>'
    if 'id="scrollToTop"' not in content and '</body>' in content:
        content = content.replace('</body>', scroll_btn)
        modified = True
            
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed grammar and added scroll button in: {file}")

print("All HTML grammar fixes and scroll button injections applied.")
