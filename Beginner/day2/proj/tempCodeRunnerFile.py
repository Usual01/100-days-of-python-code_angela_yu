print("Welcome to the tip calculator\n")
menu = {
    "eggroll": 50,
    "fishroll": 100,
    "sausage": 500
}

quantities = {}  # Empty dictionary to store the quantities

for item in menu:
    
    quantity = int(input(f"Enter the quantity of {item}: "))
    quantities[item] = quantity

for item in menu:
    total = 0
    quantity = quantities[item]
    cost = menu[item] * quantity
    total += cost
    print(f"Cost of {quantity} {item}(s): {cost}")
    print(f"the total was {total}")