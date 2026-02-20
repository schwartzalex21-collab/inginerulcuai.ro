import re

def fix_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue might be with `.modal-grid` not stacking on mobile
    # Let's check if there's a mobile query for `.modal-grid`
    
    # In style.css, the existing media queries for mobile might need an update for modal-grid.
    # Usually, a grid with two columns needs to become 1 column.
    
    mobile_css = """
/* Mobile optimizations added for Modals and Bundles */
@media (max-width: 768px) {
  .modal-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
  }
  
  .modal-left {
    padding: 20px !important;
    text-align: center;
  }
  
  .modal-right {
    padding: 24px !important;
  }
  
  .modal-image {
    max-width: 200px !important;
    margin: 0 auto 20px !important;
    display: block;
  }
  
  .modal-left-features {
    text-align: left;
    display: inline-block;
  }
  
  .bundles-grid {
    grid-template-columns: 1fr !important;
    gap: 30px !important;
  }
  
  .bundle-card {
    padding: 30px 20px !important;
  }
  
  .featured-content-wrapper {
    flex-direction: column !important;
    text-align: center !important;
  }
  
  .featured-left {
    margin: 0 auto !important;
  }
  
  .featured-right {
    width: 100% !important;
    text-align: center !important;
    align-items: center !important;
  }
  
  .featured-price {
    justify-content: center !important;
  }
}
"""

    if "/* Mobile optimizations added for Modals and Bundles */" not in content:
        content += "\n" + mobile_css

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Mobile CSS added")
    else:
        print("Mobile CSS already present")

fix_css('style.css')
