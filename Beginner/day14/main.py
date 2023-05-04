"""
create a higher lower game
"""

from datam import data
import random


def format(acc):
    account_name = acc["name"]
    account_descr = acc["description"]
    account_co = acc["country"]
    return f"{account_name}, a {account_descr} from {account_co}"
def check(guess, a_fc, b_fc):
    if a_fc > b_fc:
        return guess == "a"
    else:
        return guess =="b"
score = 0
game = True
account_b = random.choice(data)
while game:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)}")
    print(f"Compare B: {format(account_b)}")

    guess = input("who has more input? Type 'A or 'B'" ).lower()
    a_fc = account_a["follower_count"]
    b_fc = account_b["follower_count"]
    ans = check(guess, a_fc, b_fc)
    if ans:
        score += 1
        print(f"correct {score}")
    else:

        print(f"wrong {score}")
        game = False