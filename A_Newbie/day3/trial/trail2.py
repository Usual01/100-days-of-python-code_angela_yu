print("Welcome to pizza deliveries")
size = input("What size of pizza do you want? S, M, or L?")

bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N")
if add_pepperoni == "y":
        size_add_pepperoni = input("small peperroni $2 press s for small , l or m for large or medium $3 ")
        if size_add_pepperoni == "s":
            bill += 2
        elif size_add_pepperoni == "l" or "m":
            bill += 3

extra_chesse = input("Do you want extra cheese? Y or N")
if extra_chesse == "y":
    bill += 1
print(f"your final bill is {bill}")
