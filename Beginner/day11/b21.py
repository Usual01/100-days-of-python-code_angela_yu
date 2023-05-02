"""create a blackjack game
# create a deal_card() function that returns a card a random card from this list
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
#deal the user and computer each  2cards using the deal card function
user_cards = []
computer_cards = []

#create a calculate_score() function that takes in a list and returns score
# Inside calculate_score() check for blackjack and return 0 instead of the actual 
score, 0 will represent blackjack in our game.

#Inside calculate_score() check for a ace and if the score is over 21 remove 11 and replace it 
with 1. you might need to look up apped() and remove()

#call calculate_score(). If the computer or the user has a blackjack
 or if the user"s score is over21 the game ends
 #deal another card if game hasnt ended
 # the computer has to keep drawing cards if its less than 17
"""
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
user_cards = []
computer_cards = []
is_game = True
def calculate_score(cards):
    if sum(cards) and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    
    return sum(cards)

for c in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while not is_game:
        
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"your{user_cards} computer{computer_cards}")
    print(f"Computer's first card is {computer_cards[0]}")
if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game = True
else:
    a_card = input("Type 'y' for another card 'n' for pass")
    if a_card == "y":
        user_cards.append(deal_card())
    else:
        is_game = True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_score)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
#while input("Do you want another game? Type y or n") == y:
#    playgame()