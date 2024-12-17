from bs4 import BeautifulSoup
import requests

# Example URL (this could be the URL you want to scrape)
url = 'YOUR_TARGET_URL'

# Send GET request to the website
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the website content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the <a> tag using its unique ID
link = soup.find('a', id='ctl00_ContentPlaceHolder1_DataListNews_ctl00_LnkbtnNews')

# Check if the link is found
if link:
    link_text = link.get_text()  # Extract the text inside the <a> tag
    link_href = link.get('href')  # Extract the href attribute of the <a> tag
    print("Link Text:", link_text)
    print("Link Href:", link_href)
else:
    print("Link not found.")
