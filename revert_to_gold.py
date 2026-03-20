import re
import os

files = ["style.css", "main.js"]
replacements = [
    ("#10b981", "#E2B75E"),
    ("rgba(16, 185, 129", "rgba(226, 183, 94"),
    ("16, 185, 129", "226, 183, 94") # Catch raw comma separated values
]

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        # Also catch lowercase hex just in case
        content = content.replace(old.lower(), new)
        content = content.replace(old.upper(), new)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Color reversion to Gold complete.")
