import random

print("Welcome to the password Generator")
letters_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
'y', 'z']

symbols_a = [ '[', '\\', ']', '^', '_', '`', '!', '@', '#', '$', '%', '&', '*', '(', ')' ]

numbers_a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letters = int(input("How many letters would you like in you password?"))

symbols = int(input("How many symbols would you like in you password?"))

numbers = int(input("How many numbers would you like in you password?"))

leta = []
for l in range(1, (letters + 1)):
    letta = random.choice(letters_a)
    leta.append(letta)

numbas = []
for l in range(1, (numbers + 1)):
    letta = random.choice(numbers_a)
    numbas.append(letta)

symbls = []
for l in range(1, (symbols + 1)):
    letta = random.choice(symbols_a)
    symbls.append(letta)

words = symbls + numbas + leta
wordss = ''.join(words)

hard_p = []
for w in range(len(wordss)):
    adds = random.choice(wordss)
    hard_p.append(adds)
a_hard_p = ''.join(hard_p)

print(f"your simple password is {wordss}")
print(f"hard password is {a_hard_p}")
#print("here is yoour password")