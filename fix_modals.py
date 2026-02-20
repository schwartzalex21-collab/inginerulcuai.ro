import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The HTML for modal-bundle1 was commented out using:
    # <div class="modal-overlay" id="modal-bundle1" -->
    # ...
    # <!--
    # >
    
    # We need to replace the broken start tag for modal-bundle1 and remove the broken comment ending.
    # We'll just carefully replace the exact strings.
    
    # Let's replace the broken start of modal-bundle1
    broken_start = '<div class="modal-overlay" id="modal-bundle1" -->'
    fixed_start = '<div class="modal-overlay" id="modal-bundle1">'
    content = content.replace(broken_start, fixed_start)
    
    # We also have an extra `<!--` and `>` around the `modal-bundle2` ending and `modal-bundle1` content starting
    # Let's extract everything from the end of modal-vol8 to the end of the file, and rebuild the bundles safely
    
    # Since regex can be tricky with large HTML blocks, let's use a simpler approach. 
    # Let's replace the exact broken comment parts.
    
    content = content.replace('    <!--\n>\n', '')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('index.html')
fix_file('shop.html')
print("Fixed modals")
