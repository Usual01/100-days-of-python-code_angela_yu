"""
Create a program using maths and f=strings that tells us 
how many days, weeks, months we have left until 90 years old
you have 20000 days, 150 months and 1290 weeks left.
"""
age = int(input("\nhow old are you in years\n\n"))
days = (90 * 12 * 52 * 365) - (age * 12 * 52 * 365)
months = (90 * 12) - (age * 12 )
weeks = (90 * 12 * 52) - (age * 12 * 52)
 

print(f"You have {days} days {months} months and {weeks} weeks left.")