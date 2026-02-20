import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Move <script src="main.js"></script> to the very end of the file, right before </body> or the CTA/scroll components.
    # It's safest to just place it right above </body>
    script_tag = '<script src="main.js"></script>'
    if script_tag in content:
        # Check if it's not already near </body>
        index_script = content.rfind(script_tag)
        index_body = content.rfind('</body>')
        if index_body != -1 and index_body - index_script > 1000:
            # It's too far up. Remove it from current place and put it above </body>
            content = content.replace(script_tag, '')
            content = content.replace('</body>', script_tag + '\n</body>')
            modified = True

    # 2. Make sure EVERY file has the <button id="scrollToTop" /> and it comes after main.js
    # Actually, main.js uses DOMContentLoaded, so placement *shouldn't* matter as long as it executes.
    # But just in case, we will ensure the scrollToTop is present.
    btn_html = '<button id="scrollToTop" class="scroll-to-top" aria-label="Scroll to top">↑</button>'
    if btn_html not in content and '</body>' in content:
        content = content.replace('</body>', btn_html + '\n</body>')
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")

print("Script execution ensured.")
