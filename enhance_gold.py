import re
import os

files = ["style.css", "main.js"]
# Old "faded" gold: #E2B75E -> Vibrant Gold: #FFB800
# RGBA: 226, 183, 94 -> 255, 184, 0
replacements = [
    ("#E2B75E", "#FFB800"),
    ("rgba(226, 183, 94", "rgba(255, 184, 0"),
    ("226, 183, 94", "255, 184, 0")
]

for filename in files:
    if not os.path.exists(filename):
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        content = content.replace(old.lower(), new)
        content = content.replace(old.upper(), new)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Gold contrast enhancement complete.")
