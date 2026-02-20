import os
import glob
import shutil

# 1. Create directory and copy images
assets_dir = 'assets/images/results'
os.makedirs(assets_dir, exist_ok=True)

artifact_dir = '/Users/samurai/.gemini/antigravity/brain/f2753424-86e9-459d-b7f3-d21059c13e41'
images = glob.glob(os.path.join(artifact_dir, 'result_*.png'))

for img in images:
    # Rename them slightly to be simpler: result_marketing_1234.png -> result_marketing.png
    basename = os.path.basename(img)
    parts = basename.split('_')
    # Parts: ['result', 'marketing', '177...png']
    if len(parts) >= 3:
        new_name = f"{parts[0]}_{parts[1]}.png"
        if parts[1] == 'personal':
            new_name = "result_personal_dev.png"
    else:
        new_name = basename
    
    shutil.copy(img, os.path.join(assets_dir, new_name))

print("Copied images.")

# 2. Append CSS to style.css
css = """
/* ══════════════════════════════════════
   REZULTATE PAGE
══════════════════════════════════════ */
.results-page-wrapper {
  padding: 60px 0 100px;
}

.result-case {
  display: flex;
  align-items: center;
  gap: 60px;
  margin-bottom: 80px;
  background: var(--card-bg);
  border: 1px solid var(--border-dim);
  border-radius: var(--radius-lg);
  padding: 40px;
  transition: var(--transition);
}

.result-case:hover {
  border-color: rgba(243, 156, 18, 0.3);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

.result-case.reverse {
  flex-direction: row-reverse;
}

.result-info {
  flex: 1;
}

.result-vol-tag {
  display: inline-block;
  background: rgba(243, 156, 18, 0.12);
  border: 1px solid rgba(243, 156, 18, 0.2);
  color: var(--gold);
  padding: 6px 14px;
  border-radius: 50px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.result-info h3 {
  font-family: var(--font-head);
  font-size: 32px;
  font-weight: 800;
  margin-bottom: 16px;
  line-height: 1.2;
}

.result-info p {
  font-size: 16px;
  color: var(--gray);
  margin-bottom: 24px;
  line-height: 1.7;
}

.result-info .used-prompt {
  background: rgba(46, 204, 113, 0.05);
  border-left: 3px solid var(--emerald);
  padding: 16px 20px;
  font-style: italic;
  font-size: 14px;
  color: #ccc;
  border-radius: 0 8px 8px 0;
}

.result-visual {
  flex: 1;
  position: relative;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(0,0,0,0.5);
  border: 1px solid rgba(255,255,255,0.05);
}

.result-visual img {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.5s ease;
}

.result-visual:hover img {
  transform: scale(1.03);
}

@media (max-width: 900px) {
  .result-case, .result-case.reverse {
    flex-direction: column;
    padding: 24px;
    gap: 30px;
  }
  
  .result-info h3 {
    font-size: 26px;
  }
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    style_content = f.read()

if ".results-page-wrapper" not in style_content:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(css)
    print("Appended CSS.")
else:
    print("CSS already there.")

