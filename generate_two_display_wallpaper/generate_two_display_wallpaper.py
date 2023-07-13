"""
merge two wallpaper horizontally and generates two monitor wallpaper.

Tips:

1. Use of an if main and corresponding main() function.
2. To parse command-line arguments with argparse.
3. Use image from PIL to resize.
4. Check for errors from the user.
5. make the code small
"""

import argparse
from PIL import Image
import fire

def merge_wallpapers(img1_path, img2_path, output_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    if img1.size[1] != img2.size[1]:
        raise ValueError("Both wallpapers must have the same height.")

    width = img1.size[0] + img2.size[0]
    height = img1.size[1]

    merged_img = Image.new("RGB", (width, height))
    merged_img.paste(img1, (0, 0))
    merged_img.paste(img2, (img1.size[0], 0))
    merged_img.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Merge two wallpapers horizontally.")
    parser.add_argument("img1", help="Path to the first wallpaper image")
    parser.add_argument("img2", help="Path to the second wallpaper image")
    parser.add_argument("-o", "--output", default="merged_wallpaper.jpg", help="Path to save the merged wallpaper")

    args = parser.parse_args()

    try:
        merge_wallpapers(args.img1, args.img2, args.output)
        print(f"Merged wallpapers saved to {args.output}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fire.Fire(main)
