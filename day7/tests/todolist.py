"""
#1 create an empty list called display 
for each letter in chosen word add a "_" representing each letter to guess
#2 loop through each position  in the word
if the letter matches the guess reveal the letter 
#3 print display and you should see the guessed position and every letter
"""
import random
word_list = ["ardvack", "baboon", "camel"]
choice_word = random.choice(word_list)

display = []
for replace in range(len(choice_word)):    
    display += "_"
print(display)
typed_letter = input("Guess a letter: \n").lower()
for replaced in range(len(choice_word)):
    letter = choice_word[replaced]
    if letter in typed_letter:
        display[replaced] = letter
print(f"correct word was {choice_word} your word was {display}")
print(display)
