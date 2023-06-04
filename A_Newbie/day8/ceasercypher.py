"""
create function that rum encrypt snd decrypt function simultaneously
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode': to encrypt, decode to decrypt\n")
text = input("type your message here\n").lower()
shift = int(input("Type the shift number \n"))

def ceaser(pe_text, shift_nume, direction_c):
    cypher_text = ""
    if direction_c == "decode":
            shift_nume *= -1
    
    for letter in pe_text:
        position = alphabet.index(letter)
        if position > 25:
            position = 0
        if position < 0:
            position = 25    
        new_position = position + shift_nume
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The {direction_c} text is {cypher_text}")
ceaser(pe_text = text, shift_nume = shift, direction_c = direction)
