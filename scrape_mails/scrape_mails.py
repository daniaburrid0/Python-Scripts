import csv
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Sites to scrape path
sites = "sites.csv"

# Regular expression for finding email addresses
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Setup Selenium with ChromeDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

def find_emails_on_page(url):
    try:
        driver.get(url)
        return email_pattern.findall(driver.page_source)
    except TimeoutException:
        print(f"Timeout occurred while accessing {url}")
    except Exception as e:
        print(f"Error accessing {url}: {e}")
    return []

def find_contact_links(base_url):
    try:
        driver.get(base_url)
        # Find all links on the homepage
        links = driver.find_elements(By.TAG_NAME, "a")
        contact_links = [link.get_attribute('href') for link in links if 'contact' in link.get_attribute('href').lower()]
        return contact_links
    except TimeoutException:
        print(f"Timeout occurred while accessing {base_url}")
    except Exception as e:
        print(f"Error accessing {base_url}: {e}")
    return []

# Read the list of websites
site_list = []  # Replace with your list of sites
def load_sites():
    with open(site, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            site_list.append(row[0])
load_sites()

# Scraping and storing results
with open('emails_and_urls.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Site','URL', 'Email'])

    for site in site_list:
        contact_urls = find_contact_links(site)
        for contact_url in contact_urls:
            emails = find_emails_on_page(contact_url)
            for email in emails:
                writer.writerow([site, contact_url, email])

# Clean up
driver.quit()