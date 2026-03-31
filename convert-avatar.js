const fs = require('fs');
const path = require('path');

const imagePath = path.join(__dirname, 'images', 'LMT00847 (1).jpeg');
const svgPath = path.join(__dirname, 'svg', 'profile-avatar.svg');

const imageData = fs.readFileSync(imagePath);
const base64 = imageData.toString('base64');

const svg = `<svg width="75" height="75" viewBox="0 0 90 90" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="roundedCorners">
      <rect x="1" y="1" width="88" height="88" rx="45" ry="45"/>
    </clipPath>
  </defs>
  <image href="data:image/jpeg;base64,${base64}" x="1" y="1" width="88" height="88" clip-path="url(#roundedCorners)"/>
  <circle cx="45" cy="45" r="44" fill="none" stroke="#61dafb" stroke-width="2"/>
</svg>`;

fs.writeFileSync(svgPath, svg);
console.log('Avatar SVG created successfully!');
