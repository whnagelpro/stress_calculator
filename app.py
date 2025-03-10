from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_stress():
    try:
        force = float(request.json['force'])
        area = float(request.json['area'])
        if area == 0:
            return jsonify({'error': 'Area cannot be zero!'}), 400
        stress = force / area
        return jsonify({'stress': round(stress, 2)})
    except ValueError:
        return jsonify({'error': 'Invalid input!'}), 400

if __name__ == '__main__':
    app.run(debug=True)
