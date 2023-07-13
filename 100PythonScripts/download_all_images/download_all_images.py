import os
import re
import time
import argparse
import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


def get_link():
    link = input("Enter the link: ")
    return link


def get_img(link, folder_name):
    try:
        r = requests.get(link)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    soup = bs(r.content, 'html.parser')
    imgs = soup.find_all('img')
    for img in tqdm(imgs, desc="Downloading images"):
        if 'src' in img.attrs:
            img_link = img['src']
            if img_link.startswith('//'):
                img_link = 'https:' + img_link
            if not img_link.startswith('http'):
                continue
            img_name = img_link.split('/')[-1]
            img_name = sanitize_filename(img_name)
            with open(os.path.join(folder_name, img_name), 'wb') as f:
                img_r = requests.get(img_link)
                f.write(img_r.content)


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def main(link, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    get_img(link, folder_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="the link to download images from")
    parser.add_argument("-f", "--folder", help="the folder name to save the images in", default="img")
    args = parser.parse_args()
    main(args.link, args.folder)