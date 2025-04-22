import pytest
from bmi import calculate_bmi, get_bmi_category

def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86  # 70kg, 1.75m → BMI ≈ 22.86

def test_bmi_category():
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(22) == "Normal weight"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(32) == "Obese"


