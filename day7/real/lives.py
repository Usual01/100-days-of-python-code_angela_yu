
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
        elif letter not in choice_word:
            lives = lives - 1
            if lives == 0:
                end = True
                print("you lose")

    print(f"correct word was {choice_word} your word was {display}")
    print(display)
    if not '_' in display:
        end_of_game = True
        print("you win")
    print(stages[lives])