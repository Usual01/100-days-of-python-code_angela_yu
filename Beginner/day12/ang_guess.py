from random import randint
l_easy =  5
l_hard = 3
def check_answer(guess, ans, turns):
    if guess > ans:
        print("guess is too high")
        return turns - 1
    elif guess < ans:
        print("Too low")
    else:
        print(f"you got it! it is {ans}")
        return turns - 1
def set_diff():
    level = input("choose easy level or hard")
    if level == "easy":
        return l_easy
    elif level == "hard":
        return l_hard
    
def game():
    ans = randint(1, 100)
    turns = set_diff()
    
    guess = 0
    while guess != ans:
        print(f"you have {turns} remaining")
        guess = int(input("make a guess"))
        turns = check_answer(guess, ans, turns)
        if turns == 0:
            print("you outta guesses")
            return
game()