from flask import Flask, request, Response
import sys
from Pillow import Image
from io import BytesIO

app = Flask(__name__)

if sys.version_info.major == 2:
    import urllib2 as urllib
else:
    import urllib.request as urllib

@app.route("/rotate-image")
def rotate_image():
    try:
        degree = int(request.args.get('degree', 0))
        url = request.args.get('url')

        response = urllib.urlopen(url) if sys.version_info.major == 2 else urllib.urlopen(url)
        img_data = response.read()
        img = Image.open(BytesIO(img_data))

        rotated_img = img.rotate(degree, expand=True)

        output = BytesIO()
        rotated_img.save(output, format='JPEG')
        output.seek(0)

        return Response(output, content_type='image/jpeg')
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(debug=True)
