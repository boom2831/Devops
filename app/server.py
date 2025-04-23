from flask import Flask, request, jsonify
from bmi import calculate_bmi, get_bmi_category

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi_endpoint():
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

