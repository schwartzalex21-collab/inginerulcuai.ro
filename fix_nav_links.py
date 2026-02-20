import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mobile menu adds Rezultate after Despre
    # Currently it's `<a href="despre.html">Despre</a><a href="blog.html">Blog</a>`
    # Wait, some pages might have active class on Despre in mobile menu (usually they don't, but let's be careful)
    
    # Replace in mobile menu
    if '<a href="rezultate.html">Rezultate</a>' not in content.split('mobileMenu')[1]:
        content = content.replace('<a href="despre.html">Despre</a><a href="blog.html">Blog</a>', 
                                  '<a href="despre.html">Despre</a><a href="rezultate.html">Rezultate</a><a href="blog.html">Blog</a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored Rezultate once in mobile menu.")

