import re

with open('rezultate.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Active Link
# Remove active class from Despre
content = content.replace('<a href="despre.html" class="active">Despre</a>', '<a href="despre.html">Despre</a>')

# Add active class to Rezultate only in the desktop nav-links block
# We can find the desktop block by looking for the <li> structure
# <li><a href="rezultate.html">Rezultate</a></li> becomes <li><a href="rezultate.html" class="active">Rezultate</a></li>
desktop_rez_link = '<li><a href="rezultate.html">Rezultate</a></li>'
if desktop_rez_link in content:
    content = content.replace(desktop_rez_link, '<li><a href="rezultate.html" class="active">Rezultate</a></li>')

# 2. Fix Animation / Static first item
# The wrapper has a fade-in that delays everything
wrapper_str = '<section class="results-page-wrapper container fade-in hb-delay-3">'
if wrapper_str in content:
    content = content.replace(wrapper_str, '<section class="results-page-wrapper container">')

# 3. Add fade-in to the remaining result-cases (so they appear on scroll)
# We have 8 result-cases. The first one is static, the 2nd through 8th should have `fade-in`.
# Let's split by class="result-case" and "result-case reverse" and rebuild.

new_content = ""
# We can find the result cases using a regex or simple split. But since some are 'result-case' and some form are 'result-case reverse', let's just replace them.
cases = re.findall(r'<div class="result-case.*?">', content)

# We want to keep the FIRST case as is (no fade-in added).
# Wait, some cases might already have it? No, they don't right now.
case_count = 0
def replace_case(match):
    global case_count
    case_count += 1
    match_str = match.group(0)
    # the first case should not have fade-in
    if case_count == 1:
        return match_str
    
    # insert fade-in
    if 'fade-in' not in match_str:
        return match_str.replace('class="', 'class="fade-in ')
    return match_str

content = re.sub(r'<div class="result-case.*?">', replace_case, content)

with open('rezultate.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Bugs fixed in rezultate.html")
