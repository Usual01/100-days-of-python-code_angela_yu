#create a divctionary from the csv file
# create a list of the phonetic code words from the eord the user inputs

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for(index, row) in data.iterrows()}

def generate_word():
    word = input("enter a word\n").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, wrong input")
    else:
        print(output_list)
generate_word()