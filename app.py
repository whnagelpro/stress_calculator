from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data received"}), 400

    force = data.get("force")
    area = data.get("area")

    if force is None or area is None:
        return jsonify({"error": "Missing force or area"}), 400

    if not isinstance(force, (int, float)) or not isinstance(area, (int, float)):
        return jsonify({"error": "Force and area must be numbers"}), 400

    if area == 0:
        return jsonify({"error": "Area cannot be zero"}), 400

    stress = force / area
    return jsonify({"stress": stress}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # Default to port 8080
    app.run(host="0.0.0.0", port=port)
