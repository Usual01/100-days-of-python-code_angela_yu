""""
You are going to write a program which will select a random name .
The selected person will have to pay everybody's bill
"""
import random

names_string =input("Give me the names, separated by a comma and a space\n")
names = names_string.split(", ")
names_length = len(names)
name = random.randint(0, names_length)
print(f"{random.choice(names)} is going to buy the meal")
print(f'{names[name]} is going to buy the meal')
