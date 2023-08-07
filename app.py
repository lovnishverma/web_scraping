from flask import Flask, request, Response, render_template
from PIL import Image
import requests
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rotate-image", methods=['GET'])
def rotate_image():
    try:
        degree = int(request.args.get('degree', 0))
        url = request.args.get('url')

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        rotated_img = img.rotate(degree, expand=True)

        # Convert RGBA image to RGB if necessary
        if rotated_img.mode == 'RGBA':
            rotated_img = rotated_img.convert('RGB')

        output = BytesIO()
        rotated_img.save(output, format='JPEG')
        output.seek(0)

        rotated_image_base64 = base64.b64encode(output.read()).decode('utf-8')

        return render_template("index.html", rotated_image=rotated_image_base64)

    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(debug=True)
