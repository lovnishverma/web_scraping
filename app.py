from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Handle the default web page request
@app.route("/")
def index():
    json_data = scrape()
    return render_template("index.html", headings=json_data['headings'])

# Function to scrape a page
def scrape():
    # Specify the URL of the page we want to scrape
    # url = "https://www.thinkcreatelearn.co.uk/resources/node/web-scraping/sample1.html"
    url = "https://nielitropar.000webhostapp.com/"
    
    # Make the HTTP request to the URL to get the data
    response = requests.get(url)
    data = response.content
    
    # Load the HTML into BeautifulSoup web scraper
    soup = BeautifulSoup(data, 'html.parser')
    
    # Create a dictionary to store the scraped data
    json_data = {'headings': []}
    
    # Search for the elements we want
    selection = soup.find_all('h3')
    
    # Add the elements to the dictionary
    for el in selection:
        text = el.get_text()
        json_data['headings'].append(text)
    
    return json_data

# Start the app running on the web server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
