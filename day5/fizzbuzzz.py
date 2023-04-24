"""
write a program that prints the fizz buzz game
print fizz when number is divisible by 3 print buzz if divisible by 5 and 
fizzbuzz if divisible by 3 ND 5
"""

for n in range(1, 101):
    if (n % 3 == 0 and n % 5 == 0):
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizzbuzz")
    else:
        print(n)