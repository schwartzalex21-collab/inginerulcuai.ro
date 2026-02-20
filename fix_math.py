import glob

html_files = glob.glob('*.html')

# We need to systematically replace the pricing text in the HTML pages.
# Starter Pack (3 vol) -> 147 RON old, 79 RON new. Save 68 RON (46%).
# Pro Pack (5 vol) -> 245 RON old, 139 RON new. Save 106 RON (43%).
# Full Pack (8 vol) -> 392 RON old, 199 RON new. Save 193 RON (49%).

replacements = {
    # Starter Pack
    "Valoare normală: 207 RON": "Valoare normală: 147 RON",
    "Economisești 128 RON (61%)": "Economisești 68 RON (46%)",
    "Economisești 128 RON": "Economisești 68 RON",
    
    # Pro Pack
    "Valoare normală: 345 RON": "Valoare normală: 245 RON",
    "Economisești 206 RON (59%)": "Economisești 106 RON (43%)",
    "Economisești 206 RON": "Economisești 106 RON",
    
    # Full Collection
    "Valoare normală: 552 RON": "Valoare normală: 392 RON",
    "Valoare totală: 552 RON": "Valoare totală: 392 RON",
    "Economisești 353 RON (64%)": "Economisești 193 RON (49%)",
    "Economisești 353 RON": "Economisești 193 RON"
}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated prices in {file}")

print("Price verification script finished.")
