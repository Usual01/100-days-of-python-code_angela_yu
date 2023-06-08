"""
mak a number guessing game keeping account of the scope and the current value
"""
import random
print("Welcome to the Number Guessing Game!")

print("I am thinking of a number between 1 and 100")
guess = input("choose a difficulty . Type Easy or Hard\n")



if guess == 'easy':
    diff = 5
elif guess == 'Hard':
    diff = 2 
else:
    print("entry was incorrect")
diffint = int(diff)
print (f"you have {diff} attempt")
def play(diffint):
    if diffint == 0:
        return
    
    guessed = int(input("input enter num"))
    c_guess = random.randint(1, 101)
    while diffint != 0:
        if guessed > c_guess:
            print(f"{guessed}is higher than number")
            print (f"you have {diffint} attempt")
            diffint -= 1
        elif guessed < c_guess:
            print(f"{guessed} is lower than number")
            diffint -= 1
            print (f"you have {diffint} attempt")
        elif guessed == c_guess:
            print("correct") 
play(diffint)