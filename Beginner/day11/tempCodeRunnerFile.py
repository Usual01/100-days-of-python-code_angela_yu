    user_cards = []
    computer_cards = []
    game = False
    for r in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your{user_cards} current score{user_score}\n")
        print(f"computer card is {computer_cards}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game = True
        else:
            a_card = input("Type 'y' for another card 'n' for pass\n")
            if a_card == "y":
                user_cards.append(deal_card())
            else:
                game = True
    while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(f"your{user_cards}, final score{user_score} and computer is {computer_score}\n")
    print(f"Computer's final hand is {computer_cards} final score{computer_score}\n")
    print(compare(user_score, computer_score))
