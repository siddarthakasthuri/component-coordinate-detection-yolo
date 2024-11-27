import os
from cairosvg import svg2png

# Path to the folder containing SVG files
svg_folder = r"C:\Users\manju\Downloads\New folder"  # Update this with your folder path
png_folder = r"C:\Users\manju\OneDrive\Desktop\siddu\jaajiproject\dataset\images\train"   # Update this with where you want to save PNGs

# Create the PNG folder if it doesn't exist
os.makedirs(png_folder, exist_ok=True)

# Convert SVG to PNG
for filename in os.listdir(svg_folder):
    if filename.endswith('.svg'):
        svg_file_path = os.path.join(svg_folder, filename)
        png_file_path = os.path.join(png_folder, filename.replace('.svg', '.png'))
        svg2png(url=svg_file_path, write_to=png_file_path)

print("Conversion completed!")
