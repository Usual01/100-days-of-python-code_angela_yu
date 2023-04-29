"""
creste a function called encrypt type tskes the text and shift as inputs
inside the encrypt shift each of the texts forward in the alphabet by the shift amount and print 
the encrypted text
call the encrypt functions and pass in the user in puts 
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode': to encrypt, decode to decrypt\n")
text = input("type your message here\n").lower()
shift = int(input("Type the shift number \n"))
    
def encrypt(p_text, shift_num):
    cypher_text = ""
    for letter in p_text:
        position = alphabet.index(letter)
        new_position = position + shift_num
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The encoded text is {cypher_text}")
encrypt(p_text= text, shift_num = shift)
