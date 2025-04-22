height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
