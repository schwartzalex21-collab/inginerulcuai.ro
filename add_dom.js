const fs = require('fs');

const files = [
    'shop.html',
    'despre.html',
    'blog.html',
    'rezultate.html',
    'contact.html',
    'termeni.html',
    'confidentialitate.html',
    'retur.html',
    'blog-business-digital-30-zile.html',
    'blog-chatgpt-vs-claude.html',
    'blog-planificare-saptamana-ai.html',
    'blog-prompturi-design.html',
    'blog-prompturi-eficiente.html',
    'blog-prompturi-social-media.html'
];

const awwwardsHTML = `
  <!-- 🎨 AWWWARDS FEATURES -->
  <div class="film-grain"></div>
  <div class="site-preloader">
    <div class="preloader-content">
      <div class="preloader-logo">AI</div>
      <div class="preloader-progress"><div class="preloader-bar"></div></div>
    </div>
  </div>
  <div class="custom-cursor"></div>
  <!-- 🎨 END AWWWARDS FEATURES -->`;

for (const file of files) {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        if (!content.includes('class="film-grain"')) {
            content = content.replace(/<body>/i, `<body>${awwwardsHTML}`);
            fs.writeFileSync(file, content);
            console.log(`Updated ${file}`);
        } else {
            console.log(`${file} already updated`);
        }
    }
}
