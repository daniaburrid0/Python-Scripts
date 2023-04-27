"""
Giving a link to a page, save all the link from the page to a csv. If the csv exists append it to it.

- Use of an if main and a corresponding main() function
- Use **Beautiful Soup** to scrap
"""

# Importing the libraries
import requests
from bs4 import BeautifulSoup
import csv

# Defining the main function
def main():
    # Getting the url
    url = input("Enter the url: ")

    # Getting the page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Getting all the links
    links = soup.find_all('a')

    # Getting the file name
    file_name = input("Enter the file name: ")

    # Checking if the file exists
    try:
        with open(file_name, 'r') as file:
            # Getting the old links
            reader = csv.reader(file)
            old_links = list(reader)

        # Checking if the link is already present
        for link in links:
            if link.get('href') not in old_links:
                # Appending the new link
                with open(file_name, 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow([link.get('href')])
    except:
        # Creating a new file
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            for link in links:
                writer.writerow([link.get('href')])

if __name__ == '__main__':
    main()