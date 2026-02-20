import re

def fix_targets(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The previous regex might have been too specific or failed. Let's do a simpler replace.
    
    # 1. 8 Volumes
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)>Cumpără Colecția →',
                     r'data-modal-target="modal-bundle3"\1>Cumpără Colecția →', 
                     content, flags=re.MULTILINE|re.DOTALL)
                     
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)>Cumpără 8 Volumes Full Collection(.*?)>',
                     r'data-modal-target="modal-bundle3"\1>Cumpără 8 Volumes Full Collection\2>', 
                     content, flags=re.MULTILINE|re.DOTALL)

    # 2. Pro Pack
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)>Cumpără Pro Pack(.*?)>',
                     r'data-modal-target="modal-bundle2"\1>Cumpără Pro Pack\2>', 
                     content, flags=re.MULTILINE|re.DOTALL)

    # 3. Starter Pack
    content = re.sub(r'data-modal-target="modal-bundle[1-3]"(.*?)>Cumpără Starter Pack(.*?)>',
                     r'data-modal-target="modal-bundle1"\1>Cumpără Starter Pack\2>', 
                     content, flags=re.MULTILINE|re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_targets('index.html')
fix_targets('shop.html')
print("Fixed targets 2")
