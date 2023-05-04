import random
from datam import data

def reap(user_input, c, d):
    if c > d:
        return c == user_input
    else:
        return d == user_input
def format(acc):
    account_name = acc["name"]
    account_descr = acc["description"]
    account_co = acc["country"]
    return f"{account_name}, a {account_descr} from {account_co}"
game = True
score = 0
while game:
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    
    c = a["follower_count"]
    d = b["follower_count"]
    user_input = input("who has more input? Type 'A or 'B'" ).lower()
    print(reap(c,d))
    print(f"Compare A: {format(a)}")
    print(f"Compare B: {format(b)}")