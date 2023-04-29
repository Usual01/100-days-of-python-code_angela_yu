"""
create the decrypt function that takes text and shift as inputs
inside the decrypt shift each letter of the text backwards in the shift amount andprint the decrypted text 
check if wants to encrypt or decrypt by vhecking the direction vsrisble .Then the call function should be based on the 
direction you should be able to test the code on encrypt and decrypt message
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode': to encrypt, decode to decrypt\n")
text = input("type your message here\n").lower()
shift = int(input("Type the shift number \n"))
def encrypt(pe_text, shift_nume):
    cypher_text = ""
    for letter in pe_text:
        position = alphabet.index(letter)
        new_position = position + shift_nume
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The encoded text is {cypher_text}")

    
def decrypt(pd_text, shift_numd):
    cypher_text = ""
    for letter in pd_text:
        position = alphabet.index(letter)
        new_position = position - shift_numd
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The encoded text is {cypher_text}")

if direction == "encode":
    encrypt(pe_text= text, shift_nume = shift)

elif direction == "decode": 
    decrypt(pd_text= text, shift_numd = shift)
