import glob

files = glob.glob('*.html')

# 3 Vol old price: 207 -> 147
# 5 Vol old price: 345 -> 245
# 8 Vol old price: 319 (or 552) -> 392

replacements = {
    # 3 Vol:
    '207 RON': '147 RON',
    'Economisești 128 RON': 'Economisești 68 RON', # Already ran script might have missed if HTML was split

    # 5 Vol:
    '345 RON': '245 RON',
    'Economisești 206 RON': 'Economisești 106 RON',

    # 8 Vol:
    '319 RON': '392 RON',
    '342 RON': '392 RON', # Just in case
    '552 RON': '392 RON',
    'Economisești 353 RON': 'Economisești 193 RON',
    'Economisești 120 RON': 'Economisești 193 RON',
}

for file in files:
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
        print(f"Updated fixed math in {file}")

