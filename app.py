from flask import Flask, request, Response, render_template
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rotate-image", methods=['GET'])
def rotate_image():
    try:
    degree = int(request.args.get('degree', 0))
    url = request.args.get('url')
    print("Received URL:", url)  # Print URL for debugging

  
# @app.route("/rotate-image", methods=['GET'])
# def rotate_image():
#     try:
#         degree = int(request.args.get('degree', 0))
#         url = request.args.get('url')

#         response = requests.get(url)
#         img = Image.open(BytesIO(response.content))

#         rotated_img = img.rotate(degree, expand=True)

#         output = BytesIO()
#         rotated_img.save(output, format='JPEG')
#         output.seek(0)

#         return Response(output, content_type='image/jpeg')
#     except Exception as e:
#         return str(e), 400

if __name__ == "__main__":
    app.run(debug=True)
