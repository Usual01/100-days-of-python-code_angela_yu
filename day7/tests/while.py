"""
use a while loop to let the user guess again if wrong.the loop should stop once
the user has guessed allthe letters in the word the array 
"""
import random
word_list = ["ardvack", "baboon", "camel"]
choice_word = random.choice(word_list)

display = []
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
    print(f"correct word was {choice_word} your word was {display}")
    print(display)
    if not '_' in display:
        end_of_game = True
        print("you win")