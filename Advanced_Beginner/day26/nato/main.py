#create a divctionary from the csv file
# create a list of the phonetic code words from the eord the user inputs

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

phonetic_dict = {row.letter:row.code for(index, row) in data.iterrows()}
#print(phonetic_dict)

word = input("enter a word\n").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)