import re

def fix_targets(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # In shop.html
    # Cumpără Pro Pack &rarr; is currently pointing to modal-bundle1
    # Actually, Pro Pack should point to modal-bundle2
    # Starter Pack should point to modal-bundle1
    
    # In index.html, let's verify them too
    # Cumpără Starter Pack &rarr;
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"\s+class="btn-product"\n*\s*style="background:#2980b9(.*?)>Cumpără Starter Pack',
                     r'data-modal-target="modal-bundle1" class="btn-product"\n                style="background:#2980b9\1>Cumpără Starter Pack', 
                     content, flags=re.MULTILINE|re.DOTALL)
                     
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)Cumpără Starter Pack',
                     r'data-modal-target="modal-bundle1"\1Cumpără Starter Pack', 
                     content, flags=re.MULTILINE|re.DOTALL)

    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)Cumpără Pro Pack',
                     r'data-modal-target="modal-bundle2"\1Cumpără Pro Pack', 
                     content, flags=re.MULTILINE|re.DOTALL)
                     
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)Cumpără 8 Volumes Full Collection',
                     r'data-modal-target="modal-bundle3"\1Cumpără 8 Volumes Full Collection', 
                     content, flags=re.MULTILINE|re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_targets('index.html')
fix_targets('shop.html')
print("Fixed targets")
