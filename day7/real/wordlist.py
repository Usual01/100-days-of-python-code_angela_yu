import random
wordlist = ["ardvack", "baboon", "camel"]
user_word = input("choose a word\t").lower()
chosen_word = random.choice(wordlist)
for letter in chosen_word:
    if user_word == chosen_word:
        print('correct')
    else:
        print("wrong")