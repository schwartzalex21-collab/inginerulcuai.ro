import os
import re

# Montserrat Google Fonts link
# We'll use a wide range of weights for versatility
montserrat_link = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">'

# Pattern to find existing Google Fonts links in head
# Specifically looking for the ones that include Outfit or Plus Jakarta Sans
font_pattern = r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=(?:Outfit|Plus\+Jakarta\+Sans)[\s\S]*?rel="stylesheet">'

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".html"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace existing font links with Montserrat
            if re.search(font_pattern, content):
                content = re.sub(font_pattern, montserrat_link, content)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated font link in: {file_path}")

