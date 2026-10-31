# BMI calculator
# The BMI thresholds below are illustrative and may not reflect official medical guidelines.
gender = input("What is your gender? Male/Female: ").lower()
height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))
bmi = weight / (height**2)
bmi = round(bmi, 2)

if gender == "male":
    if bmi < 21:
        print("You are underweight.")
    elif bmi < 27:
        print("You are normal weight.")
    else:
        print("You are overweight.")
elif gender == "female":
    if bmi < 18:
        print("You are underweight.")
    elif bmi < 24:
        print("You are normal weight.")
    else:
        print("You are overweight.")
print("Your BMI is:", bmi)
