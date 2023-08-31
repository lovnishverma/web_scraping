from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Handle the default web page request
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        tag = request.form['tag']
        if url and tag:
            json_data = scrape(url, tag)
            return render_template("index.html", headings=json_data['headings'], url=url, tag=tag)
    return render_template("index.html")

# Function to scrape a page
def scrape(url, tag):
    try:
        # Make the HTTP request to the URL to get the data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.content

        # Load the HTML into BeautifulSoup web scraper
        soup = BeautifulSoup(data, 'html.parser')

        # Create a dictionary to store the scraped data
        json_data = {'elements': []}

        # Search for the elements of the specified tag
        selection = soup.find_all(tag)

        # Add the elements to the dictionary
        for el in selection:
            text = el.get_text()
            json_data['elements'].append(text)

        return json_data
    except Exception as e:
        return {'error': str(e)}


# Start the app running on the web server
if __name__ == "__main__":
    app.run(debug=True)
