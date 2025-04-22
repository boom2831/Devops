def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be positive")
    return weight / (height ** 2)
