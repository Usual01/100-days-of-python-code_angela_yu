"""
write a tip calculator
"""

print("Welcome to the tip calculator\n") 
bill  = float(input("what was the total bill\n"))
percent = int(input("What percentage tip would you give? 10, 12 or 15?\n"))
nump = int(input("How many peaople are to split this bill"))
amount = float( bill / nump)
tip = (percent / 100) * bill
print(f"Each person should pay ${round(amount, 2)} and the tip is ${tip}")