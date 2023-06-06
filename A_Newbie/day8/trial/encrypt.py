letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = input("Enter the word\t").upper()
shift_number = int(input("Enter shift amout"))

coded_word = ''
for l in word:
    position = letters.index(l)
    new_position = position + shift_number
    c_word = letters[new_position]
    coded_word += c_word
print(f"{coded_word}")