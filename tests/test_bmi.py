import unittest
from bmi import calculate_bmi, get_bmi_category

# --- PyTest Tests (Works with `pytest`) ---
def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86  # 70kg, 1.75m → BMI ≈ 22.86

def test_bmi_category():
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(22) == "Normal weight"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(32) == "Obese"

# --- PyUnit (unittest) Tests (Works with `python -m unittest`) ---
class TestBMI(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_bmi_category(self):
        self.assertEqual(get_bmi_category(17), "Underweight")
        self.assertEqual(get_bmi_category(22), "Normal weight")
        self.assertEqual(get_bmi_category(27), "Overweight")
        self.assertEqual(get_bmi_category(32), "Obese")

if __name__ == "__main__":
    unittest.main()
