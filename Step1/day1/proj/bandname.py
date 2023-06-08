import random

print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name\n")

new_name = (city + pet)
name = []
for letter in new_name:
    name.append(letter)

namr = []
for l in name:
    randomletter = random.choice(name)
    namr.append(randomletter)

band_name = ''.join(namr)
print(f"Your band name could be {band_name}")