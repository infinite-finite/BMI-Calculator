print("Welcome to BMI Calculator - Global Edition!")
system_choice = input("Enter your measurement system, 'I' for Imperial or 'M' for Metric: ")

if system_choice.upper() == 'I':
    weight = input("What is your weight in pounds: ")
    height = input("What is your height in inches: ")
    BMI = round((float(weight) / (float(height) ** 2) * 703), 1)

elif system_choice.upper() == 'M':
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