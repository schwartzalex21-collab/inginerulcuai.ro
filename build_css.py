css_rules = """

/* ── UX ENHANCEMENTS PHASE 2 ── */

/* FAQ Section */
.faq-section {
  padding: 80px 0;
  position: relative;
  border-top: 1px solid var(--border-dim);
}
.faq-grid {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.faq-item {
  background: var(--card-bg);
  border: 1px solid var(--border-dim);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}
.faq-item[open] {
  border-color: var(--gold);
  box-shadow: 0 4px 20px rgba(243, 156, 18, 0.08);
}
.faq-item summary {
  padding: 20px 24px;
  font-family: var(--font-head);
  font-weight: 600;
  font-size: 18px;
  color: var(--white);
  cursor: pointer;
  list-style: none; /* Hide default arrow */
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.faq-item summary::-webkit-details-marker {
  display: none;
}
.faq-item summary::after {
  content: '+';
  font-size: 24px;
  color: var(--gold);
  transition: transform 0.3s ease;
}
.faq-item[open] summary::after {
  transform: rotate(45deg);
}
.faq-answer {
  padding: 0 24px 24px 24px;
  color: var(--text-dim);
  font-size: 16px;
  line-height: 1.6;
}

/* Mobile Floating CTA */
.mobile-floating-cta {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(10, 15, 26, 0.95);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-top: 1px solid var(--border-dim);
  padding: 12px 20px;
  z-index: 1000;
  box-shadow: 0 -4px 25px rgba(0, 0, 0, 0.5);
}
.m-cta-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 100%;
}
.m-cta-text {
  display: flex;
  flex-direction: column;
}
.m-cta-title {
  font-size: 12px;
  color: var(--dgray);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.m-cta-price {
  font-size: 18px;
  color: var(--white);
  font-weight: 700;
  font-family: var(--font-head);
}
.m-cta-btn {
  padding: 10px 20px;
  font-size: 14px;
  border-radius: 8px;
  white-space: nowrap;
}

@media (max-width: 768px) {
  .mobile-floating-cta {
    display: block;
  }
  /* Adaug padding la body ca sa nu acopere continutul bara de jos */
  body {
    padding-bottom: 70px;
  }
  /* Ridicam ScrollToTop ca sa nu se suprapuna peste Mobile CTA */
  .scroll-to-top {
    bottom: 90px;
  }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_rules)

print("CSS UX phase 2 injected into style.css")
