import re

# Read original
with open("/Users/samurai/Desktop/AI PROMPTS/last version website/index.html", "r", encoding="utf-8") as f:
    orig_html = f.read()

# Read current
with open("index.html", "r", encoding="utf-8") as f:
    curr_html = f.read()

# Let's extract original testimonials block
match_orig = re.search(r'(<div class="testimonials-scroll" id="row1">.*?</div>\n    </div>)', orig_html, re.DOTALL)
if match_orig:
    orig_testi_block = match_orig.group(1)
    
    # We will build the new testimonies block manually to be 100% correct
    # We can parse the t-cards from orig_testi_block
    cards = re.findall(r'<div class="t-card">.*?<p>"(.*?)"</p>.*?<img src="(.*?)" alt="(.*?)".*?<strong>(.*?)</strong>.*?<span>(.*?)</span>.*?</div>\s*</div>', orig_testi_block, re.DOTALL)
    
    new_testi_block = '<div class="testimonials-scroll" id="row1">\n'
    for text, img, alt, name, role in cards:
        # User wants "Doar numele Laura, diana, cosmin... fara S. T. V."
        # Name is like "Radu D.", "Maria P."
        first_name = name.split()[0]
        
        wa_card = f"""        <div class="wa-card">
          <div class="wa-header">
            <img src="{img}" alt="{first_name}" class="wa-avatar">
            <div class="wa-contact">
              <strong>{first_name}</strong>
              <span>Online</span>
            </div>
          </div>
          <div class="wa-body">
            <div class="wa-msg wa-received">
              <p>{text}</p>
              <span class="wa-time">14:24</span>
            </div>
            <div class="wa-msg wa-sent">
              <p>Top! 🔥 Mă bucur enorm să aud asta!</p>
              <span class="wa-time">14:30 <svg viewBox="0 0 16 11" width="16" height="11"><path d="M11.8 1.6L6.5 7.4 4.1 4.7 2.8 5.8 6.5 9.9 13.1 2.7zM15.4 2.7L8.8 9.9 7.5 8.5 8.8 7.1 14.1 1.6z" fill="#53BCDA"></path></svg></span>
            </div>
          </div>
        </div>\n"""
        new_testi_block += wa_card
        
    new_testi_block += '    </div>'
    
    # Now replace the broken testimonials block in curr_html with new_testi_block
    # But wait, how do we find the broken block in curr_html? 
    # It starts with <div class="testimonials-scroll" id="row1"> and ends with </div>\n    </div>
    curr_html = re.sub(r'<div class="testimonials-scroll" id="row1">.*?</div>\n    </div>', new_testi_block.replace('\\', '\\\\'), curr_html, flags=re.DOTALL)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(curr_html)
    print("Fixed testimonials HTML")
else:
    print("Could not find original testimonies")
