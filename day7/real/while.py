import random
wordlist = ["ardvack", "baboon", "camel"]
chosen_word = random.choice(wordlist)
display = []
for count in chosen_word:
        display += "-"
print(display)
end = False
while not end:
    user_word = input("choose a word\t").lower()

    
    for letter in range(len(chosen_word)):
        lettera = chosen_word[letter] 

        if user_word == chosen_word:
            display[letter] = lettera   
    print(display)
    if "-" not in display:
        end = True
    print("you won")
