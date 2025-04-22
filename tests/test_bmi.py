from unittest.mock import patch
from bmi import calculate_bmi, get_bmi_category

with patch('builtins.input', side_effect=['1.75', '70']):
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"BMI: {bmi:.2f}")
    print(f"BMI Category: {category}")

