import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The current structure has modal-bundle2 INSIDE modal-bundle1
    # <div class="modal-overlay" id="modal-bundle1">
    #
    #   <div class="modal-overlay" id="modal-bundle2">
    #     ... bundle2 content ...
    #   </div>
    #
    #   <div class="modal-content" style="border-color: rgba(46, 204, 113, 0.4);">
    #     ... bundle1 content ...
    #   </div>
    # </div>
    
    # We should extract bundle2 and place it AFTER bundle1, and correctly wrap bundle1 content
    
    # Let's just fix it by string replacement for the exact problem area
    
    old_structure = """  <div class="modal-overlay" id="modal-bundle1">

    <div class="modal-overlay" id="modal-bundle2">"""
    
    # This means bundle2 starts inside bundle1. Let's close bundle1 before bundle2, and put bundle1's content inside bundle1.
    # Actually, it's easier to just rebuild these two bundles completely using regex or simply replacing the whole block.
    
    # Find the block from modal-bundle1 to modal-bundle3
    start_idx = content.find('<div class="modal-overlay" id="modal-bundle1">')
    end_idx = content.find('<div class="modal-overlay" id="modal-bundle3">')
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        
        # bundle2 block
        b2_start = block.find('<div class="modal-overlay" id="modal-bundle2">')
        b2_end = block.find('<div class="modal-content" style="border-color: rgba(46, 204, 113, 0.4);">')
        
        bundle2_html = block[b2_start:b2_end]
        bundle1_content_html = block[b2_end:]
        
        # Now construct them properly
        new_block = f"""  <div class="modal-overlay" id="modal-bundle1">
{bundle1_content_html}
  <div class="modal-overlay" id="modal-bundle2">
{bundle2_html.replace('<div class="modal-overlay" id="modal-bundle2">', '')}"""
        
        content = content[:start_idx] + new_block + content[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('index.html')
fix_file('shop.html')
print("Fixed modals 2")
