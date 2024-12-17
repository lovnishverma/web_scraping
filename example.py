from bs4 import BeautifulSoup
import requests

# URL of the Punjab Police Whats New page
url = 'https://www.punjabpolice.gov.in/WhatsNew.aspx'

# Send GET request to the website
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

# Setup retries
retries = Retry(total=5, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retries)

# Create session
session = requests.Session()
session.mount('https://', adapter)

# Send request
response = session.get(url, timeout=30)



# Parse the website content
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Find all <a> tags (or other tags you're interested in)
# This will find all the links in the page
links = soup.find_all('a')

# Iterate through all found links and extract the link text and href
for link in links:
    link_text = link.get_text(strip=True)  # Get the visible text inside the <a> tag
    link_href = link.get('href')  # Get the href attribute (URL of the link)
    
    # Only print links with meaningful text
    if link_text:
        print("Link Text: {link_text}")
        print("Link Href: {link_href}")
        print("-" * 40)

# Alternatively, if you're looking for specific sections like headlines:
# Example: Extract news items or titles from a specific section
news_items = soup.find_all('div', class_='whats-new-item-class')  # Update the class as per actual page structure

for item in news_items:
    title = item.get_text(strip=True)
    print("News Title: {title}")
