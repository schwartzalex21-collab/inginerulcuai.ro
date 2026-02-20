import re

def test_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for i in range(1, 4):
        id_str = f'id="modal-bundle{i}"'
        if id_str in content:
            print(f"Found {id_str} in {filepath}")
        else:
            print(f"MISSING {id_str} in {filepath}")

test_file('index.html')
test_file('shop.html')
