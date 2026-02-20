import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'rezultate.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The previous regex inserted:
    # <li><a href="despre.html">Despre</a>
    #       <a href="rezultate.html">Rezultate</a></li>
    #         <li><a href="rezultate.html">Rezultate</a></li>
    
    # Let's clean up any Rezultate links first
    content = re.sub(r'\s*<a href="rezultate\.html">Rezultate</a>\s*', '', content)
    content = re.sub(r'\s*<li><a href="rezultate\.html">Rezultate</a></li>\s*', '', content)
    content = content.replace('      </li>\n', '</li>\n') # cleanup
    
    # Now let's carefully insert it.
    # Desktop menu
    content = re.sub(r'(<li><a href="despre\.html".*?>Despre</a></li>)', 
                     r'\1\n        <li><a href="rezultate.html">Rezultate</a></li>', 
                     content)

    # Mobile menu
    content = re.sub(r'(<a href="despre\.html".*?>Despre</a>)', 
                     r'\1<a href="rezultate.html">Rezultate</a>', 
                     content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed navigation.")
