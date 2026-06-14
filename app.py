from flask import Flask, render_template, request, jsonify
import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)

GENERATED_FOLDER = "static/generated"
if not os.path.exists(GENERATED_FOLDER):
    os.makedirs(GENERATED_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- QR GENERATE ----------------
@app.route("/generate", methods=["POST"])
def generate():
    data = request.json.get("data")

    if not data:
        return jsonify({"error": "No data"}), 400

    filepath = os.path.join(GENERATED_FOLDER, "qr.png")

    img = qrcode.make(data)
    img.save(filepath)

    return jsonify({"image": "/static/generated/qr.png"})

# ---------------- QR SCAN FROM FILE ----------------
@app.route("/scan", methods=["POST"])
def scan():
    file = request.files["file"]

    img = Image.open(file)
    decoded = decode(img)

    if decoded:
        result = decoded[0].data.decode("utf-8")
        return jsonify({"result": result})

    return jsonify({"result": "No QR found"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)