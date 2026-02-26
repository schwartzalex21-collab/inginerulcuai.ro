const fs = require('fs');

function addBanners(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    const bannerHTML = '\n          <div class="coming-soon-banner">COMING SOON</div>';

    // For index.html
    let target1 = '<div class="product-card fade-in" style="opacity: 0.7; filter: grayscale(50%);">';
    // For shop.html
    let target2 = '<div class="product-card" style="opacity: 0.7; filter: grayscale(50%);">';

    if (content.includes(target1)) {
        content = content.split(target1).join(target1 + bannerHTML);
    }
    if (content.includes(target2)) {
        content = content.split(target2).join(target2 + bannerHTML);
    }

    fs.writeFileSync(filePath, content, 'utf8');
}

addBanners('/Users/samurai/Desktop/AI PROMPTS/Last Version Website/index.html');
addBanners('/Users/samurai/Desktop/AI PROMPTS/Last Version Website/shop.html');
console.log("Added banners to HTML files.");
