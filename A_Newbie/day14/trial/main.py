from datam import data
import random

def accounts(acc):
    acc_name = acc["name"]
    acc_descr = acc["description"]
    acc_coun = acc["country"]
    return (f"{acc_name}, a {acc_descr}, from {acc_coun}")

def check(guess, a_f_c, b_f_c):
    if a_f_c > b_f_c:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
should_continue = True
acc_b = random.choice(data)

while should_continue:
    acc_a = acc_b
    acc_b = random.choice(data)
    if acc_a == acc_b:
        acc_b = random.choice(data)


    print(f"COMPARE A: {accounts(acc_a)}.")
    print(f"AGAINST B: {accounts(acc_b)}.")

    guess = input("Who has more followers? Type a for A or b for B").lower()
    a_f_c = acc_a["follower_count"]
    b_f_c = acc_b["follower_count"]
    is_correct = check(guess, a_f_c, b_f_c)

    if is_correct:
        score += 1
        print(f"you're right! Current score: {score}")

    else:
        print(f"Sorry, thats wrong. Final score: {score}")
        break