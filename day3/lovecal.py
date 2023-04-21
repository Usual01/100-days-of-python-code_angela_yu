"""
love calculator
count the total word occurence and store in a variable compare against true compare against love ;
concatenate two digits together
"""

print("Welcometo the love calculator")
name1 = input("what is your name\n").lower()
name2 = input("what is your name\n").lower()
names = name1 + name2
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = l + o + v + e

score = int(str(true) + str(love))


if score < 10 or score < 99:
    print(f"you have a love score of {score}! go together, love birds")
elif score >= 40 and score <= 50:
    print(f"you have a love score of {score}! go together, love")
else:
    print(f" This is your score {score}")
