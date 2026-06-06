from PIL import Image, ImageDraw, ImageFont

# Create image
img = Image.new("RGB", (1200, 400), color=(25, 118, 210))

draw = ImageDraw.Draw(img)

# Title
title = "Medical Device Failure Analytics"
subtitle = "Monitor • Analyze • Predict"

try:
    title_font = ImageFont.truetype("arial.ttf", 60)
    sub_font = ImageFont.truetype("arial.ttf", 35)
except:
    title_font = ImageFont.load_default()
    sub_font = ImageFont.load_default()

draw.text((80, 120), title, fill="white", font=title_font)
draw.text((80, 220), subtitle, fill="white", font=sub_font)

# Save image
img.save("medical_banner.png")

print("medical_banner.png created successfully!")
