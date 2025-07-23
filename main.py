from flask import Flask, request, send_file
from PIL import Image, ImageDraw
import io

app = Flask(__name__)

@app.route('/mask', methods=['POST'])
def make_mask():
    data = request.get_json()
    mask = Image.new("L", (2048, 2048), 0)
    draw = ImageDraw.Draw(mask)

    for item in data:
        if "v" in item:
            coords = [tuple(point) for point in item["v"]]
            draw.polygon(coords, fill=255)

    output = io.BytesIO()
    mask.save(output, format='PNG')
    output.seek(0)
    return send_file(output, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)