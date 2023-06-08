"""
write a program that interprets the bmi of the user's weigth/ height
it should tell
under 18.5 if overweight
over 18.5 but below 25 have normal weight 
over 25 but below 30 are overweight
over 30 but below 35 are obese 
above 35 are clincally obese

"""

height = float(input('enter your height\n'))
weight = float(input('enter your weight\n'))

bmi = weight/(height ** 2)

if(bmi < 18.5):
    print(f'your bmi is {bmi} and you are underweight')
elif( bmi > 18.5 and bmi <= 25):
    print(f'your bmi is {bmi} and you have normal weight')
elif( bmi > 25 and bmi <= 30):
    print(f'your bmi is {bmi} and you are overweight')
elif( bmi > 30 or bmi <= 35):
    print(f'your bmi is {bmi} and you are obese')
else:
    print(f"your bmi is {bmi} and you are clinically obese")