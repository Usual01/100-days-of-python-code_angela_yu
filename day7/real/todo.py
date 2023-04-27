import random
wordlist = ["ardvack", "baboon", "camel"]
user_word = input("choose a word\t").lower()
chosen_word = random.choice(wordlist)
display = []
for count in chosen_word:
    display += "-"
print(display)
for letter in range(len(chosen_word)):
    lettera = chosen_word[letter] 

    if user_word == chosen_word:
        display[letter] = lettera   
print(display)