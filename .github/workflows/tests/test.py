import unittest
from bmi import calculate_bmi, get_bmi_category

class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_bmi_category(self):
        self.assertEqual(get_bmi_category(17), "Underweight")
        self.assertEqual(get_bmi_category(22), "Normal weight")
        self.assertEqual(get_bmi_category(27), "Overweight")
        self.assertEqual(get_bmi_category(32), "Obese")

if __name__ == "__main__":
    unittest.main()
