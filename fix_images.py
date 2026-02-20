import re

def fix_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Revert emojis
    reverts = [
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 01</div>', 
         r'<div class="product-tag-vol">Vol. 01</div>\n          <div class="product-icon">📢</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 02</div>', 
         r'<div class="product-tag-vol">Vol. 02</div>\n          <div class="product-icon">✍️</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 03</div>', 
         r'<div class="product-tag-vol">Vol. 03</div>\n          <div class="product-icon">🎨</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 04</div>', 
         r'<div class="product-tag-vol">Vol. 04</div>\n          <div class="product-icon">⏱️</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 05</div>', 
         r'<div class="product-tag-vol">Vol. 05</div>\n          <div class="product-icon">🚀</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 06</div>', 
         r'<div class="product-tag-vol">Vol. 06</div>\n          <div class="product-icon">💪</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 07</div>', 
         r'<div class="product-tag-vol">Vol. 07</div>\n          <div class="product-icon">🧠</div>'),
        (r'<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 100%; border-radius: 8px; margin-bottom: 12px;">\s*<div class="product-tag-vol">Vol\. 08</div>', 
         r'<div class="product-tag-vol">Vol. 08</div>\n          <div class="product-icon">💻</div>'),
        # ALL 8
        (r'<div class="featured-left">\s*<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 140px; border-radius: 8px;">\s*</div>\s*<div class="featured-center">\s*<h3 style="font-size:24px; margin-bottom:8px">8 Volumes Full Collection', 
         r'<div class="featured-left">\n              <div class="product-tag-vol" style="background:var(--gold);color:#000;margin-bottom:12px">ALL 8</div>\n              <div class="product-icon">👑</div>\n            </div>\n            <div class="featured-center">\n              <h3 style="font-size:24px; margin-bottom:8px">8 Volumes Full Collection'),
        # ORICE 5
        (r'<div class="featured-left">\s*<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 140px; border-radius: 8px;">\s*</div>\s*<div class="featured-center">\s*<h3 style="font-size:24px; margin-bottom:8px">Pro Pack', 
         r'<div class="featured-left">\n              <div class="product-tag-vol"\n                style="background:rgba(155, 89, 182, 0.2);color:#c39bd3;border:1px solid rgba(155, 89, 182, 0.4);margin-bottom:12px">\n                ORICE 5</div>\n              <div class="product-icon">🔥</div>\n            </div>\n            <div class="featured-center">\n              <h3 style="font-size:24px; margin-bottom:8px">Pro Pack'),
        # ORICE 3
        (r'<div class="featured-left">\s*<img src="assets/laptop_vol1\.png" alt="Laptop" style="width: 140px; border-radius: 8px;">\s*</div>\s*<div class="featured-center">\s*<h3 style="font-size:24px; margin-bottom:8px">Starter Pack', 
         r'<div class="featured-left">\n              <div class="product-tag-vol"\n                style="background:rgba(41, 128, 185, 0.2);color:#5dade2;border:1px solid rgba(41, 128, 185, 0.4);margin-bottom:12px">\n                ORICE 3</div>\n              <div class="product-icon">🚀</div>\n            </div>\n            <div class="featured-center">\n              <h3 style="font-size:24px; margin-bottom:8px">Starter Pack')
    ]
    
    for pattern, repl in reverts:
        content = re.sub(pattern, repl, content, flags=re.MULTILINE)
        
    # 2. Update modal images in index.html
    # Find all modal-image that have prompt_example.png or laptop_vol[2-8].png
    content = re.sub(r'src="assets/laptop_vol[2-8]\.png"', 'src="assets/laptop_vol1.png"', content)
    content = re.sub(r'src="assets/prompt_example\.png"', 'src="assets/laptop_vol1.png"', content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
def fix_shop():
    with open('shop.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. Update modal images in shop.html
    content = re.sub(r'src="assets/laptop_vol[2-8]\.png"', 'src="assets/laptop_vol1.png"', content)
    content = re.sub(r'src="assets/prompt_example\.png"', 'src="assets/laptop_vol1.png"', content)

    with open('shop.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix_index()
fix_shop()
print("Done")
