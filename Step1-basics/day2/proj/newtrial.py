print("Welcome to the tip calculator\n")
t_bill = float(input("What was the total bill $"))
p_tip = int(input("What percentage tip would you like to give? 10, 12, 15\t"))
people = int(input("how many people are spliting this bill?\t"))
tip = p_tip / 100 * t_bill
bill = (t_bill + tip) / people 
f_tip = "{:.2f}".format(bill)
print(f"Each person should pay ${f_tip}")