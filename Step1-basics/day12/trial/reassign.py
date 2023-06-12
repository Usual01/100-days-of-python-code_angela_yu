import random
easy_hardness = 5
hard_hardness = 10

def check(user_guess, guessed_num, turns):
    if user_guess > guessed_num:
        print("you went too high")
        return turns - 1
        
    elif user_guess < guessed_num:
        print("you went too low")
        return turns - 1
    else:
        print("you got it!")
        
def difficulty():
    diff = input("choose a difficulty, E for Easy and H for hard").upper()
    if diff == "E":
        return easy_hardness
    else:
        return hard_hardness

def game():
    print("Welcome to the number guessing game")
    
    guessed_num = random.randint(1, 101)

    user_guess = 0
    turns = difficulty()
    print(f"you have {turns} left")
    print("I'm thinking of a number between 1 and  100")


    while user_guess != guessed_num:
        print(f"{guessed_num}")
        print(f"you have {turns} left")
        
        
        user_guess = int(input("enter a guess"))

        turns = check(user_guess, guessed_num, turns)
        if turns == 0:
            print("you've run out of guesses, you loose")
            return
game()