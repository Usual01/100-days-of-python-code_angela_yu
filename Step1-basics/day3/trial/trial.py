print("Welcome to pizza deliveries")
size = input("What size of pizza do you want? S, M, or L?")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_chesse = input("Do you want extra cheese? Y or N")

bill = 0
if size == "s":
    bill += 15
    if add_pepperoni == "y":
        size_add_pepperoni = input("small peperroni $2 press s for small , l or m for large or medium $3 ")
        if size_add_pepperoni == "s":
            bill += 2
        elif size_add_pepperoni == "l" or "m":
            bill += 3
    if extra_chesse == "y":
        bill += 1
    print(f"your final bill is {bill}")

elif size == "m":
    bill += 20
    if add_pepperoni == "y":
        size_add_pepperoni = input("small peperroni $2 press s for small , l or m for large or medium $3 ")
        if size_add_pepperoni == "s":
            bill += 2
        elif size_add_pepperoni == "l" or "m":
            bill += 3
    if extra_chesse == "y":
        bill += 1
    print(f"your final bill is {bill}")

elif size == "l":
    bill += 25
    if add_pepperoni == "y":
        size_add_pepperoni = input("small peperroni $2 press s for small , l or m for large or medium $3 ")
        if size_add_pepperoni == "s":
            bill += 2
        elif size_add_pepperoni == "l" or "m":
            bill += 3
    if extra_chesse == "y":
        bill += 1
    print(f"your final bill is {bill}")
