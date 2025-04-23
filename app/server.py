from flask import Flask, request, jsonify
from bmi import calculate_bmi, get_bmi_category

app = Flask(__name__)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi_endpoint():
    # Handle GET requests with query parameters
    if request.method == 'GET':
        weight = request.args.get('weight', type=float)
        height = request.args.get('height', type=float)
        
        if weight is None or height is None:
            return jsonify({
                'message': 'BMI Calculator API',
                'instructions': {
                    'GET': 'Send weight and height as query parameters: /bmi?weight=70&height=1.75',
                    'POST': 'Send JSON payload: {"weight": 70, "height": 1.75}'
                },
                'example_request': {
                    'GET': 'GET /bmi?weight=70&height=1.75',
                    'POST': 'POST /bmi {"weight": 70, "height": 1.75}'
                },
                'example_response': {
                    'bmi': 22.86,
                    'category': 'Normal weight'
                }
            })
    
    # Handle POST requests with JSON body
    elif request.method == 'POST':
        try:
            data = request.get_json()
            weight = float(data['weight'])
            height = float(data['height'])
        except:
            return jsonify({'error': 'Invalid JSON payload'}), 400
    
    # Calculate BMI for both GET and POST
    try:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'weight': weight,
            'height': height,
            'units': {
                'weight': 'kg',
                'height': 'meters'
            }
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

