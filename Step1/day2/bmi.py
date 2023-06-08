"""
write a  program BMI from the height and weeight
"""
height = float(input("what is your height in m:\n"))
weight = int(input("what is yout weight kg:\n"))

bmi = (weight) / (height ** 2)
print(f"Your BMI is {int(bmi)}")