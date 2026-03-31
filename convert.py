import base64
import os

img_path = os.path.join("images", "LMT00847 (1).jpeg")
svg_path = os.path.join("svg", "profile-avatar.svg")

# Read image and convert to base64
with open(img_path, 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

# Create SVG with embedded image
svg_content = f'''<svg width="75" height="75" viewBox="0 0 90 90" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="roundedCorners">
      <rect x="1" y="1" width="88" height="88" rx="45" ry="45"/>
    </clipPath>
  </defs>
  <image href="data:image/jpeg;base64,{image_data}" x="1" y="1" width="88" height="88" clip-path="url(#roundedCorners)"/>
  <circle cx="45" cy="45" r="44" fill="none" stroke="#61dafb" stroke-width="2"/>
</svg>'''

# Write SVG
with open(svg_path, 'w') as f:
    f.write(svg_content)

print("Done! Avatar SVG updated with embedded image")
