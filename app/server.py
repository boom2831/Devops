from flask import Flask, request, jsonify
from bmi import calculate_bmi, get_bmi_category

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi_endpoint():
    try:
        # Get raw data first for debugging
        raw_data = request.get_data()
        print("Raw data received:", raw_data)  # For debugging
        
        # Try to parse JSON
        data = request.get_json(force=True)  # force=True makes it more lenient
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
            
        weight = float(data.get('weight'))
        height = float(data.get('height'))
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'weight': weight,
            'height': height
        })
    except ValueError as e:
        return jsonify({'error': f'Invalid value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

