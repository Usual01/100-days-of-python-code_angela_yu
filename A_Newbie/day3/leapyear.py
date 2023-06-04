"""
Write a program that works out if a given year is a leap year
cleanly divisible by 4
not cleanly divisible by 100
cleanly divisible by 400

"""

year =  int(input( "check if year is a leap year\n"))
if (year % 4 == 0) and ( year % 100 != 0):
   print("leap year")
else:
  print("not a leap year")