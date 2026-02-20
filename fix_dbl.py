import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # The duplicate HTML is:
    # <li><a href="despre.html">Despre</a><a href="rezultate.html">Rezultate</a></li>
    #         <li><a href="rezultate.html">Rezultate</a></li>
    #
    # OR 
    # <li><a href="despre.html" class="active">Despre</a><a href="rezultate.html">Rezultate</a></li>
    
    # 1. We remove <a href="rezultate.html">Rezultate</a> immediately following Despre </a>
    content = re.sub(r'(<a href="despre\.html".*?>Despre</a>)%s*' % '', r'\1', content)
    content = content.replace('Despre</a><a href="rezultate.html">Rezultate</a>', 'Despre</a>')

    # Mobile menu:
    # <a href="despre.html">Despre</a><a href="rezultate.html">Rezultate</a><a href="rezultate.html">Rezultate</a>
    content = content.replace('Despre</a><a href="rezultate.html">Rezultate</a><a href="rezultate.html">Rezultate</a>', 'Despre</a><a href="rezultate.html">Rezultate</a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed duplicates.")
