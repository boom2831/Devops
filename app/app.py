from flask import request, jsonify
from .bmi import calculate_bmi, get_bmi_category

def configure_routes(app):
    @app.route('/bmi', methods=['POST'])
    def bmi_endpoint():
        data = request.json
        bmi = calculate_bmi(data['weight'], data['height'])
        return jsonify(bmi=round(bmi, 2), category=get_bmi_category(bmi))

