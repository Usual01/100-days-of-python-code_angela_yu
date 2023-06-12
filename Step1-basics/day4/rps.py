"""
build a rock paper scissors game
"""
import random
choice_list = ["rock", "paper", "scissors"]

choice = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
choice_user = choice_list[choice]
c_num_index = random.randint(0,2)
choice_computer = choice_list[c_num_index]
if choice_computer == choice_user:
    print(f"computer chose {choice_computer} you chose {choice_user}, its a draw!")
    
elif choice_computer == "rock":
    if choice_user == "scissors":
        print(f"computer chose {choice_computer} you chose {choice_user}, you loose!")
    else:
        print(f"computer chose {choice_computer} you chose {choice_user}, you win!")
elif choice_computer == "paper":
    if choice_user == "rock":
        print(f"computer chose {choice_computer} you chose {choice_user}, you loose!")
    else:
        print(f"computer chose {choice_computer} you chose {choice_user}, you win!")
elif choice_computer == "scissors":
    if choice_user == "paper":
        print(f"computer chose {choice_computer} you chose {choice_user}, you loose!")
    else:
        print(f"computer chose {choice_computer} you chose {choice_user}, you win!")