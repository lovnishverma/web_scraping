from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# URL of the target website
URL = "https://www.punjabkesari.in/"

# Function to scrape h3 tags
def scrape_h3_tags(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract and clean h3 tags
        h3_tags = [h3.get_text(strip=True) for h3 in soup.find_all('h3') if h3.get_text(strip=True)]
        return h3_tags

    except Exception as e:
        print("Error occurred: {e}")
        return []

# Flask route to display scraped h3 tags
@app.route("/")
def display_h3_tags():
    h3_data = scrape_h3_tags(URL)

    # HTML template for displaying data
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scraped H3 Tags</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background-color: #f9f9f9; color: #333; }
            h1 { text-align: center; }
            .container { max-width: 800px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px #ddd; }
            .item { margin: 10px 0; padding: 10px; border: 1px solid #ddd; background-color: #f4f4f4; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Scraped H3 Tags from PunjabKesari</h1>
        <div class="container">
            {% if h3_tags %}
                {% for tag in h3_tags %}
                    <div class="item">{{ tag }}</div>
                {% endfor %}
            {% else %}
                <p>No H3 tags found.</p>
            {% endif %}
        </div>
    </body>
    </html>
    """

    # Render the HTML template with scraped data
    return render_template_string(html_template, h3_tags=h3_data)

# Run the Flask app
if __name__ == "__main__":
    print("Starting Flask server")
    app.run(debug=True)
