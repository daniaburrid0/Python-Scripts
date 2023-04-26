"""
This script will generate different resolution icons for chrome extensions when you give a png or JPG as input and save it into a folder with same name as the input image.

Make 3 different files with 3 different resolutions:

1. 16x16 pixels
2. 48x48 pixels
3. 128x128 pixels

Save the files as [imput_name][resolution] for example if the input is “house.jpg” one of the outputs are “house16x16.jpg”

Use 

1. Use of an if main and corresponding main() function.
2. To parse command-line arguments with argparse.
3. Use image from PIL to resize.

To use it type in the terminal: python generate_icons.py "input".jpg
"""

import os
import sys
import argparse
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Generate different resolution icons for Chrome extensions.")
    parser.add_argument('input_image', type=str, help="Path to the input image (PNG or JPG format)")
    args = parser.parse_args()

    input_image_path = args.input_image
    if not os.path.exists(input_image_path):
        print(f"Error: '{input_image_path}' does not exist.")
        sys.exit(1)

    image_name, image_ext = os.path.splitext(os.path.basename(input_image_path))
    if image_ext.lower() not in ['.png', '.jpg', '.jpeg']:
        print("Error: Invalid image format. Only PNG and JPG formats are supported.")
        sys.exit(1)

    output_folder = image_name
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    resize_and_save_image(input_image_path, 16, 16, output_folder, image_name, image_ext)
    resize_and_save_image(input_image_path, 48, 48, output_folder, image_name, image_ext)
    resize_and_save_image(input_image_path, 128, 128, output_folder, image_name, image_ext)
    print("Icon generation complete.")

def resize_and_save_image(input_image_path, width, height, output_folder, image_name, image_ext):
    image = Image.open(input_image_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    output_image_name = f"{image_name}{width}x{height}{image_ext}"
    output_image_path = os.path.join(output_folder, output_image_name)
    resized_image.save(output_image_path)
    print(f"Saved {output_image_name} in {output_folder}.")

if __name__ == "__main__":
    main()
