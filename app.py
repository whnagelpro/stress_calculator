from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/calculate": {"origins": "*"}}, supports_credentials=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST", "OPTIONS"])  # Allow OPTIONS for CORS preflight
def calculate():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()

    data = request.get_json()

    if not data:
        return _corsify_actual_response(jsonify({"error": "Invalid JSON data received"}), 400)

    force = data.get("force")
    area = data.get("area")

    if force is None or area is None:
        return _corsify_actual_response(jsonify({"error": "Missing force or area"}), 400)
    if not isinstance(force, (int, float)) or not isinstance(area, (int, float)):
        return _corsify_actual_response(jsonify({"error": "Force and area must be numbers"}), 400)
    if area == 0:
        return _corsify_actual_response(jsonify({"error": "Area cannot be zero"}), 400)

    stress = force / area
    return _corsify_actual_response(jsonify({"stress": stress}))

def _build_cors_preflight_response():
    response = jsonify({"message": "CORS preflight successful"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    return response

def _corsify_actual_response(response, status=200):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, status

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(debug=True, host="0.0.0.0", port=port)