from flask import Flask, request, jsonify
from bmi import calculate_bmi, get_bmi_category

app = Flask(__name__)

@app.route('/bmi', methods=['GET', 'POST'])
@app.route('/bmi/weight:<float:weight>/height:<float:height>', methods=['GET'])
def bmi_endpoint(weight=None, height=None):
    if request.method == 'POST':
        try:
            data = request.get_json()
            weight = float(data['weight'])
            height = float(data['height'])
        except:
            return jsonify({'error': 'Invalid JSON payload'}), 400
    elif weight is None or height is None:
        return jsonify({
            'message': 'BMI Calculator API',
            'instructions': 'Send a POST request with JSON payload or use URL parameters',
            'examples': {
                'POST': 'POST /bmi {"weight": 70, "height": 1.75}',
                'GET': 'GET /bmi/weight:70/height:1.75'
            }
        })
    
    try:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'weight': weight,
            'height': height
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

