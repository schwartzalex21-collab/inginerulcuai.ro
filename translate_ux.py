import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Translate English "8 Volumes Full Collection" -> "Colecția Completă (8 Volume)"
    replacements = {
        "8 Volumes Full Collection": "8 Volume Colecția Completă",
        "Orice 3 Volume": "Oricare 3 Volume",
        "Orice 5 Volume": "Oricare 5 Volume",
    }

    for old_text, new_text in replacements.items():
        if old_text in content:
            content = content.replace(old_text, new_text)
            modified = True
            
    # Verify Math inside prices - let's make sure the display discounts are correct
    # Single is 49. 3x=147, 5x=245, 8x=392.
    # The normal values on the site are based on 69 RON to show a higher discount value which is a standard marketing tactic. 
    # Current Starter: Old 207, New 79, Save 128 (61%). 207-79 = 128. Correct.
    # Current Pro 5: Old 345, New 139, Save 206 (59%). 345-139 = 206. Correct.
    # Current Full 8: Old 552, New 199, Save 353 (64%). 552-199=353. Correct.
    # We will leave math as is, it's correct based on a 69/vol reference price.

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Translated phrases in {file}")

print("Translation script complete.")
