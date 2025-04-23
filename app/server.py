from flask import Flask, request, jsonify
from bmi import calculate_bmi, get_bmi_category

app = Flask(__name__)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi_endpoint():
    if request.method == 'POST':
        try:
            data = request.get_json()
            weight = float(data['weight'])
            height = float(data['height'])
            
            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)
            
            return jsonify({
                'bmi': round(bmi, 2),
                'category': category
            }), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Invalid request'}), 400
    else:
        # Handle GET request - show a form or instructions
        return jsonify({
            'message': 'BMI Calculator API',
            'instructions': 'Send a POST request with JSON payload: {"weight": [kg], "height": [m]}',
            'example': {
                'request': 'POST /bmi {"weight": 70, "height": 1.75}',
                'response': '{"bmi": 22.86, "category": "Normal weight"}'
            }
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

