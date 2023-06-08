"""
#1 Randomly choose a word from word_list and assign it ro a variable 
called chosen word
#2 ask the user to guess a letter and assign it to a variable 
called guess lowercase
#3 check if the user guessed is one of the chosen word
"""
import random
word_list = ["ardvack", "baboon", "camel"]
choice_word = random.choice(word_list)
new_word = []
typed_letter = input("Guess a letter: \n").lower
for letter in choice_word:
    if letter in typed_letter:
        new_word += letter
        print("Right")
    else:
        print ("wrong")
        continue
print(f"correct word was {choice_word} your word was { new_word}")