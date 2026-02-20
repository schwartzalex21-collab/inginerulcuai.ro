import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'rezultate.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace in desktop menu
    # Need to handle the 'active' class nicely, but we can just insert after 'Despre'
    # Existing: <li><a href="despre.html" class="active">Despre</a></li> or <li><a href="despre.html">Despre</a></li>
    
    # regex to find Despre link in nav-links
    content = re.sub(r'(<li><a href="despre\.html".*?>Despre</a></li>)', 
                     r'\1\n        <li><a href="rezultate.html">Rezultate</a></li>', 
                     content, flags=re.MULTILINE)
                     
    # Mobile menu
    # <a href="despre.html">Despre</a>
    content = re.sub(r'(<a href="despre\.html".*?>Despre</a>)', 
                     r'\1\n      <a href="rezultate.html">Rezultate</a>', 
                     content, flags=re.MULTILINE)
                     
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print(f"Updated {len(html_files)} files.")
