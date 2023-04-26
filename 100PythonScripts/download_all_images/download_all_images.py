"""
    using beatifulsoup to get img from any link the user wants
"""
# import the libraries
import requests
from bs4 import BeautifulSoup as bs
import os
import re

# get the link from the user
def get_link():
    link = input("Enter the link: ")
    return link

# get the img's from the link create a folder name img and save the img's in it
def get_img(link):
    r = requests.get(link)
    soup = bs(r.content, 'html.parser')
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:  # Check if 'src' attribute exists
            img_link = img['src']
            
            # Add 'https:' if the scheme is missing
            if img_link.startswith('//'):
                img_link = 'https:' + img_link
            
            img_name = img_link.split('/')[-1]
            img_name = sanitize_filename(img_name)
            with open('img/' + img_name, 'wb') as f:
                img_r = requests.get(img_link)
                f.write(img_r.content)


# Sanitize the file name
def sanitize_filename(filename):
    # Remove invalid characters
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# main function
def main():
    link = get_link()
    get_img(link)

# Create the 'img' folder if it doesn't exist
if not os.path.exists('img'):
    os.makedirs('img')

# Call the main function
main()
