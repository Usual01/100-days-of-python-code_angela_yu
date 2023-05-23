"""
write a tip calculator
"""

print("Welcome to the tip calculator\n") 
bill  = float(input("what was the total bill\n"))
percent = int(input("What percentage tip would you give? 10, 12 or 15?\n"))
nump = int(input("How many people are to split this bill\n"))
amount = float( bill / nump)
format_amount = "{:.2f}".format(amount)
tip = (percent / 100) * bill
print(f"The total bill was {bill} Each person should pay ${format_amount} and the tip is ${tip}")