import re

def fix_btn(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The actual HTML in shop.html looks like this:
    # <div class="bundle-price">
    #   <span class="old">Valoare normală: 345 RON</span>
    #   <span class="new">139 RON</span>
    #   <span class="save">Economisești 206 RON (59%)</span>
    # </div>
    # <a href="#" data-modal-target="modal-bundle1" class="btn-product">Cumpără Pro Pack →</a>
    
    # We will search for 'data-modal-target="modal-bundle1"' followed by 'Cumpără Pro Pack'
    new_content = content.replace('data-modal-target="modal-bundle1" class="btn-product">Cumpără Pro Pack', 'data-modal-target="modal-bundle2" class="btn-product">Cumpără Pro Pack')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

fix_btn('shop.html')
print("Fixed shop btn exactly")
