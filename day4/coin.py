"""
write a vitrual coin toss program that tells the user if its heads or tails
"""
import random
coin = random.randint(1, 2)
if coin == 1:
    print('heads')
else:
    print("tails")