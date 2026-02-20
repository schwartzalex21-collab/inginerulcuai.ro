import re

html_file = 'blog.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The user has 6 specific posts. We'll map emojis to image tags.
replacements = {
    '<div class="blog-thumb">🤖</div>': '<div class="blog-thumb"><img src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=800&auto=format&fit=crop" alt="AI Beginners"></div>',
    '<div class="blog-thumb">📢</div>': '<div class="blog-thumb"><img src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800&auto=format&fit=crop" alt="AI Social Media"></div>',
    '<div class="blog-thumb">🚀</div>': '<div class="blog-thumb"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800&auto=format&fit=crop" alt="Digital Business"></div>',
    '<div class="blog-thumb">✍️</div>': '<div class="blog-thumb"><img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=800&auto=format&fit=crop" alt="ChatGPT vs Claude"></div>',
    '<div class="blog-thumb">⏱️</div>': '<div class="blog-thumb"><img src="https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=800&auto=format&fit=crop" alt="AI Planning"></div>',
    '<div class="blog-thumb">🎨</div>': '<div class="blog-thumb"><img src="https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop" alt="AI Design"></div>'
}

for old_tag, new_tag in replacements.items():
    if old_tag in content:
        content = content.replace(old_tag, new_tag)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog emojis replaced with Unsplash image sources.")
