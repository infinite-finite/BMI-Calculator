print("Welcome to BMI Calculator - Metric Edition!")
weight = input("What is your weight in kilograms: ")
height = input("What is your height in meters: ")
BMI = round(float(weight) / (float(height) ** 2), 1)

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}. Your BMI is in the healthy range.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}. You are overweight.")
elif BMI >= 30:
    print(f"Your BMI is {BMI}. You are obese.")