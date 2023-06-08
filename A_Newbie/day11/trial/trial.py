import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
     
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, cpu_score):
    if user_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif cpu_score > 21:
        return "computer went over. You win"
    elif user_score > cpu_score:
        return "you win"
    else:
        return "you lose"

def playgame():
    user_cardss = []
    cpu_cardss = []
    game = True

    for c in range(2):    
        user_cardss.append(deal_card())    
        cpu_cardss.append(deal_card())
    while game:
        user_score = calc_score(user_cardss)
        cpu_score = calc_score(cpu_cardss)
        print(f"Your cards: {user_cardss} and score: {user_score}")
        print(f"{cpu_cardss}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            game = False
        else:
            another_card = input(" type y for yes")
            if another_card == 'y':
                user_cardss.append(deal_card())
            else:
                game = False
    while cpu_score != 0 and cpu_score < 17:
        cpu_cardss.append(deal_card())
        cpu_score = calc_score(cpu_cardss)
    print(f"your{user_cardss}, final score{user_score} and computer is {cpu_score}")
    print(f"Computer's final hand is {cpu_cardss} final score{cpu_score}")
    print(compare(user_score, cpu_score))
while input("Do you want another game? Type y or n\n") == "y":
   playgame()
