print("Welcome to the tip calculator\n")
menu = {
    "eggroll": 50,
    "fishroll": 100,
    "sausage": 500
}

quantities = {}  # Empty dictionary to store the quantities
total = 0
for item in menu:
    
    quantity = int(input(f"Enter the quantity of {item}: "))
    quantities[item] = quantity

for item in menu:
    
    quantity = quantities[item]
    cost = menu[item] * quantity
    total += cost
    print(f"Cost of {quantity} {item}(s): {cost}")
print(f"the total was {total}")

bill  = total
percent = int(input("What percentage tip would you give? 10, 12 or 15?\n"))
nump = int(input("How many people are to split this bill\n"))
amount = float( bill / nump)
format_amount = "{:.2f}".format(amount)
tip = (percent / 100) * bill
print(f"\n")
print(f"The total bill was ${bill} Each person should pay ${format_amount} and the tip is ${tip}")