const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const js = fs.readFileSync('main.js', 'utf8');
const css = fs.readFileSync('style.css', 'utf8');
console.log('HTML has awwwards:', html.includes('class="film-grain"'));
console.log('JS has awwwards:', js.includes('AWWWARDS FEATURES'));
console.log('CSS has awwwards:', css.includes('.film-grain'));
