import random

choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice)
user_choice = input("Enter your choice between ROCK, PAPER, SCISSORS\n").lower()

if user_choice == computer_choice:
    print(f"its a draw computer chose {computer_choice} and you chose {user_choice}")

elif user_choice == "rock":
    if computer_choice == "scissors":
        print(f"you win computer chose {computer_choice} and you chose {user_choice}")
    else:
        print(f"you loose computer chose {computer_choice} and you chose {user_choice}")

elif user_choice == "paper":
    if computer_choice == "rock":
        print(f"you win computer chose {computer_choice} and you chose {user_choice}")
    else:
        print(f"you loose computer chose {computer_choice} and you chose {user_choice}")
    
elif user_choice == "scissors":
    if computer_choice == "rock":
        print(f"you win computer chose {computer_choice} and you chose {user_choice}")
    else:
        print(f"you loose computer chose {computer_choice} and you chose {user_choice}")