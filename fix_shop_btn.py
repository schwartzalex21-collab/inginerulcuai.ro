import re

def fix_btn(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue: Pro Pack button in shop.html points to modal-bundle1
    # <div class="bundle-card">
    #   <span class="bundle-tag tag-pro">Pro Pack</span>
    # ...
    #   <a href="#" data-modal-target="modal-bundle1" class="btn-product">Cumpără Pro Pack →</a>
    
    # We need to change `data-modal-target="modal-bundle1"` to `data-modal-target="modal-bundle2"` for the Pro Pack.
    # We'll use a specific replacement around "Cumpără Pro Pack".
    
    content = re.sub(r'data-modal-target="modal-bundle1"(.*?)>Cumpără Pro Pack',
                     r'data-modal-target="modal-bundle2"\1>Cumpără Pro Pack', 
                     content, flags=re.MULTILINE|re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_btn('shop.html')
print("Fixed shop btn")
