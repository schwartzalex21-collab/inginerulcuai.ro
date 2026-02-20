import re

def check_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify if modal grid is normally 2 columns
    matches = re.findall(r'\.modal-grid \{(.*?)\}', content, re.DOTALL)
    for index, match in enumerate(matches):
        print(f".modal-grid block {index+1}: {match.strip()}")

check_css('style.css')
