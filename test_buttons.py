import re

def check_buttons(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all buttons with data-modal-target
    matches = re.findall(r'data-modal-target="(.*?)"(.*?)>(.*?)<', content, re.DOTALL)
    
    print(f"Buttons in {filepath}:")
    for target, attrs, text in matches:
        if 'bundle' in target:
            clean_text = re.sub(r'\s+', ' ', text).strip()
            print(f"  Target: {target} | Text: {clean_text}")

check_buttons('index.html')
check_buttons('shop.html')
