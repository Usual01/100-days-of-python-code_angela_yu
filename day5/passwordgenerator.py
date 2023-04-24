"""
write a password generator
"""
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9,', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

print("Welcome to the password Generator!")
nr_letters = int(input("how many letters would you like to input in your password?\n"))
nr_symbols = int(input("how many symbols would you like?\n"))
nr_numbers = int(input("how many numbers would you like?\n"))
total_p  = nr_letters + nr_numbers + nr_symbols

symbol_s = ''
number_s = ''
letter_s = ''
    
    
for nr in range(0, (nr_letters + 1)):
    letter_s += random.choice(letters)
for nr in range(0, (nr_numbers + 1)):
    number_s += random.choice(numbers)
for nr in range(0, (nr_symbols + 1)):
    symbol_s += random.choice(symbols)

hard = symbol_s + letter_s + number_s

angela_hard_p = []
string_hard_p = '' 
for a in range(0, total_p):
    string_hard_p += random.choice(hard)
    angela_hard_p.append(random.choice(hard))
angela_hard_pass = ''

angela_hard_po = random.shuffle(angela_hard_p)
for angela in angela_hard_p:
    angela_hard_pass += angela
print(f'your simple password is : {symbol_s}{number_s}{letter_s}')
print(f'your  hard password is : {string_hard_p} but angela list is {angela_hard_pass} ')

