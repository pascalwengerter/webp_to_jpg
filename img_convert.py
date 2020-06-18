import os
import sys
from PIL import Image

# Replace with applicable folder name
target_dir = "../images_to_convert/"

def convert_webp_to_jpg(file):
    im = Image.open(file).convert("RGB")
    im.save(file.replace("webp", "jpg"), "jpeg")
    print(file + "successfully converted")

# On macOS, you might want to remove '.DS_Store' first, word
for filename in os.listdir(target_dir):
    full_path = os.path.abspath(target_dir + filename)
    convert_webp_to_jpg(full_path)
