def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kg: "))
    bmi = calculate_bmi(weight, height)
    
    print(f"Your BMI is {bmi:.2f}")
    category = get_bmi_category(bmi)
    print(category)

if __name__ == "__main__":
    main()
