# this program inputs height and weight from user and then calculates the BMI
weight = float(input("Enter your weight in KGs"))
height = float(input("Enter your height in feet"))
height = height * 0.3048
bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is : {bmi}")
