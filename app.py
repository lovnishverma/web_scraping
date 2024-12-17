from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Home Route - Display the Form
@app.route("/")
def index():
    return render_template("index.html")

# Scraping Route - Process URL and Display Results
@app.route("/scrape", methods=["POST"])
def scrape():
    if request.method == "POST":
        # Get URL from the Form
        url = request.form["url"]
        try:
            # Fetch page content
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for invalid responses
            
            # Parse content with BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract Title and All Paragraph Texts
            title = soup.title.string if soup.title else "No Title Found"
            paragraphs = [p.get_text() for p in soup.find_all("p")]
            
            return render_template("result.html", title=title, paragraphs=paragraphs, url=url)
        
        except Exception as e:
            error_message = "An error occurred: {str(e)}"
            return render_template("result.html", error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
