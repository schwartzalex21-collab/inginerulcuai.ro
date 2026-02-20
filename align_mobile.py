css_append = """
/* Mobile Bundle Pricing Alignment */
@media (max-width: 768px) {
  .bundle-card {
    text-align: center;
  }
  .bundle-price {
    align-items: center;
    text-align: center;
  }
  .bundle-includes {
    text-align: left; /* Keep benefits left-aligned for readability */
    display: inline-block;
  }
  .bundle-tag {
    margin-left: auto;
    margin-right: auto;
  }
}
"""
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)
print("Appended Mobile CSS alignment.")
