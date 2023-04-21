"""
#create a band name generator

Welcome to the Band Name Generator.
What's name of the city you grew up in?
Bristol
What's your pet's name
Rabbit
Your band name could be Bristol Rabbit
"""

print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
print(city)
pet = input("What's your pet's name\n")
print(pet)
print("Your band name could be",(city + pet))