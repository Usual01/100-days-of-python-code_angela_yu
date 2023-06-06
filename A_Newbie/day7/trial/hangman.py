import random
word = [ 'ardvack', 'camel', 'little']

choice = random.choice(word)

display = []

for w in choice:
    display += "_"

print(display)
user_word = input("what is the word\n").lower()
for a in range(len(choice)):
    letter = choice[a]
    if letter == user_word:
        #display[a] = letter
        #display[a].replace(letter)
        display.replace(display[a], letter)
print(display)