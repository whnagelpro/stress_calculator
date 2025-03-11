from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    return jsonify({"message": "Route exists!", "data_received": data})

if __name__ == "__main__":
    print("✅ Available Routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")

    app.run(debug=True, host="0.0.0.0")