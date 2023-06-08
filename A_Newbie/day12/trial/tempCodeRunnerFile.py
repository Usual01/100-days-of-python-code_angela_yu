    print(f"{guessed_num}")
    user_guess = int(input("enter a guess"))
    if user_guess > guessed_num:
        print("you went too high")
        print(f"you have {difficulty} left" )
    elif user_guess < guessed_num:
        print("you went too low")
    else:
        print("you got it!")
        game = False
