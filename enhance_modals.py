import re

# To make the package popups more "appealing", let's enhance their styling specifically.
# Since we just restored the HTML for modal-bundle1, it still has basically the same layout as the other packages.
# Let's add some inline style enhancements, or target the modal grid directly for bundles to make them stand out.

# We'll apply some glow effects and featured colors to the package modals.

def enhance_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Starter Pack (modal-bundle1)
    b1_old = '<div class="modal-content" style="border-color: rgba(46, 204, 113, 0.4);">'
    b1_new = '<div class="modal-content" style="border-color: var(--emerald); box-shadow: 0 20px 80px rgba(46, 204, 113, 0.15); border-width: 2px;">'
    content = content.replace(b1_old, b1_new)

    # Pro Pack (modal-bundle2)
    b2_old = '<div class="modal-content" style="border-color: rgba(155, 89, 182, 0.4);">'
    b2_new = '<div class="modal-content" style="border-color: #9b59b6; box-shadow: 0 20px 80px rgba(155, 89, 182, 0.15); border-width: 2px;">'
    content = content.replace(b2_old, b2_new)

    # Full Collection (modal-bundle3)
    b3_old = '<div class="modal-content" style="border-color: rgba(243, 156, 18, 0.6); box-shadow: 0 40px 100px rgba(243,156,18, 0.15);">'
    b3_new = '<div class="modal-content" style="border-color: var(--gold); box-shadow: 0 20px 100px rgba(243,156,18, 0.25); border-width: 2px; background: linear-gradient(145deg, var(--bg2), var(--card-bg));">'
    content = content.replace(b3_old, b3_new)
    
    # And we also need to ensure that bundle1 html actually has the `modal-close` button positioned right and content aligned
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

enhance_file('index.html')
enhance_file('shop.html')
print("Enhanced modals")
