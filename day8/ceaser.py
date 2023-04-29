"""
import art file
what if shift number is greater than the number in the alphabets
"""
#from art import logo
#print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode': to encrypt, decode to decrypt\n")
text = input("type your message here\n").lower()
shift = int(input("Type the shift number \n"))

def ceaser(pe_text, shift_nume, direction_c):
    cypher_text = ""
    if direction_c == "decode":
            shift_nume *= -1
    if shift_nume > 25:
         shift_nume = shift_nume % 26   
    for letter in pe_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if position > 25:
                position = 0
            if position < 0:
                position = 25    
            new_position = position + shift_nume
            new_letter = alphabet[new_position]
            cypher_text += new_letter
        else:
             cypher_text += letter
    print(f"The {direction_c} text is {cypher_text}")
ceaser(pe_text = text, shift_nume = shift, direction_c = direction)
