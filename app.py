from flask import Flask, render_template, request, jsonify
import qrcode
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json.get("data")

    if not data:
        return jsonify({"error": "No data"}), 400

    img = qrcode.make(data)

    path = "static/qr.png"
    img.save(path)

    return jsonify({"image": "/static/qr.png"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)