print("Welcome to love calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is your crushes name? \n").lower()
length = name1 + name2

t = length.count("t")
u = length.count("r")
r = length.count("u")
e = length.count("e")

true = t + r + u + e

l = length.count("l")
o = length.count("o")
v = length.count("v")
e = length.count("e")

love = l + o + v + e
score = true + love
love_score = str(true) + str(love)

if score < 10 or score > 90:
    print(f"Your score is {love_score}%, you go together like coke and mentos")

elif score > 40 or score < 50:
    print(f"Your score is {love_score}%, you're alright together ")

else:
    print(f"Your score is {love_score}%")