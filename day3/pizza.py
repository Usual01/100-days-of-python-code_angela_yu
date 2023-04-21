"""
Congratulations, you have gotten a job at Python pizza. Your first job is to
build an automatic pizza order program
Based on the order work out the final bill
"""

print("Welcome to Python Pizza Deliveries")
print("choose between \n SMALL PIZZA $15\nMEDIUM PIZZA $20 \nLARGE PIZZA $25\n")

size = input("what size of pizza do you want?\nS, M OR L\n")
print("Do you want pepperonni ?\n Y OR N \n")
peporonni = input("Peperroni for small pizza: +$2 \n Pepperoni for medium or large pizza +$3\n")
print("Extra cheese for $1")
cheese = input("press Y or N ")


total_bill = 0
if size == 'S':
    total_bill += 15
    if peporonni == "Y":
        total_bill += 2
    if cheese == "Y":
        total_bill += 1

elif size == 'M':
    total_bill += 20
    if peporonni == "Y":
        total_bill += 3
    if cheese == "Y":
        total_bill += 1

elif size == "L":
    total_bill += 20
    if peporonni == "Y":
        total_bill += 3
    if cheese == "Y":
        total_bill += 1
print(f"your total bill is {total_bill} ")
################## OR ##############
total_bill = 0
if size == 'S':
    total_bill += 15
elif size == 'M':
    total_bill += 20
else:
    total_bill += 25
if peporonni == 'Y':
    if size == 'S':
        total_bill += 2
    else :
        total_bill += 3
if cheese == 'Y':
    total_bill += 1
print(f"your total bill is {total_bill} ")
