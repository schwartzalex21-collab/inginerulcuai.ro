import re

def check_buttons(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all buttons with data-modal-target
    matches = re.findall(r'<a href="#" data-modal-target="(.*?)" class="(.*?)">(.*?)</a>', content)
    
    print(f"Buttons in {filepath}:")
    for target, classes, text in matches:
        if 'bundle' in target:
            print(f"  Target: {target} | Text: {text.strip()}")

check_buttons('index.html')
check_buttons('shop.html')
