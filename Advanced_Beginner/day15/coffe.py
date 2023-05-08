MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        }, 
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
not_off = True
# def resourse(water_r, milk_r, coffee_r, money_r):
#     return f'water {water_r}ml milk {milk_r}ml coffee {coffee_r}g money ${money_r}'
def r_drink(ingredients):
   for items in ingredients:
    if ingredients[items] >= resources[items]:
        print("insufficient")
        return False
    return True
def transaction(money, drink_cost):
   if money >= drink_cost:
      change = round(money - drink_cost, 2)
      print(f"Your change is ${change}")
      global profit
      profit += drink_cost
      return True
   else:
      print("not enough")
      return False
def make_coffee(drink_name, ingredients):
    for item in ingredients:
      resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}")

def coins():
   print("please insert coins")
   total = int(input("how many quaters?")) * 0.25
   total += int(input("how many quaters?")) * 0.1
   total += int(input("how many quaters?")) * 0.05
   total += int(input("how many quaters?")) * 0.01
   return total
while not_off:
    prompt = input(f"“ What would you like?(espresso/latte/cappuccino): ”")
    if prompt == 'off':
     off = False
    elif prompt == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['milk']}g")
        print(f"Money: ${profit}")
    else:
       drink = MENU[prompt]
       if r_drink(drink["ingredients"]):
        payment = coins()
        if transaction(payment, drink["cost"]):
           make_coffee(prompt, drink["ingredients"])

   

# for a, b in MENU.items():
#     print(f"\nDrikk: {a}" )
#     for key in b:
#         print(f"{key}: {b[key]}")