"""
write a program that calculates the sum  of all even numbers from one to 100
including 1 and 100
"""
num = 0
for n in range(1, 101):
    if n % 2 == 0:
        num += n
print(num)
#### or ####
num2 = 0
for n in range(2,101,2):
    num2 += n
print(num2)