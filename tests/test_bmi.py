import pytest
from unittest.mock import patch
from bmi import calculate_bmi, get_bmi_category

def test_calculate_bmi():
    with patch('builtins.input', side_effect=['1.75', '70']):  
        height = float(input("Enter height in meters: "))
        weight = float(input("Enter weight in kg: "))
        assert round(calculate_bmi(weight, height), 2) == 22.86  

def test_bmi_category():
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(22) == "Normal weight"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(32) == "Obese"


