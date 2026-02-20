import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Replace 🛡️ Garanție 14 Zile with ♾️ Acces pe Viață
    if "Garanție 14 Zile" in content:
        content = content.replace("Garanție 14 Zile", "Acces pe Viață")
        content = content.replace("🛡️", "♾️") # Ensure the icon changes too, or we can just replace the whole span if needed.
        # Actually, let's just do a direct string replace of the exact text to be safe.
        modified = True

    # 2. In CTA note: "Garanție 14 zile" -> "Acces pe Viață"
    if "Garanție 14 zile" in content:
        content = content.replace("Garanție 14 zile", "Acces pe Viață")
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated text guarantees in HTML files.")
