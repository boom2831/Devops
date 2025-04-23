from flask import Flask, request, jsonify
from bmi import calculate_bmi, get_bmi_category

app = Flask(__name__)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi_endpoint():
    try:
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
                    'example_response': {
                        'bmi': 22.86,
                        'category': 'Normal weight'
                    }
                })
        
        # Handle POST requests with JSON body
        elif request.method == 'POST':
            if not request.is_json:
                return jsonify({'error': 'Content-Type must be application/json'}), 400
                
            data = request.get_json()
            
            if not data or 'weight' not in data or 'height' not in data:
                return jsonify({'error': 'Missing weight or height in JSON'}), 400
                
            weight = float(data['weight'])
            height = float(data['height'])
        
        # Calculate BMI for both methods
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        return jsonify({
            'method': request.method,
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
        return jsonify({'error': f'Invalid number: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)