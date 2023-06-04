"""
create a variable to keep track of lives whoch is equal to 6
if guess is not a letter in word reduce lives by 1
if 0 reduceto zero wnd game
"""

import random
word_list = ["ardvack", "baboon", "camel"]
choice_word = random.choice(word_list)
lives = 6
display = []
stages = ["you are hanged", "last chance!", "put its head","tie the noose","ready the rope","to the gallows"]
for replace in range(len(choice_word)):    
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    typed_letter = input("Guess a letter: \n").lower()
    for replaced in range(len(choice_word)):
        letter = choice_word[replaced]
        if letter in typed_letter:
            display[replaced] = letter
    if typed_letter not in choice_word :
        lives -= 1
        print(f'you have {lives} lives left') 
        if lives == 0:
            end_of_game = True
            print(f"correct word was {choice_word} your word was {display}")
    print(f"{''.join(display)}")
    
    if '_'not in display :
        end_of_game = True
        print("you win")
        print(display)
    print(stages[lives])