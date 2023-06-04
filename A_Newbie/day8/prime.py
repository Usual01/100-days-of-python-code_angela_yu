"""
write a prime number checker
"""
def prime(n):
    for i in range(2, n):
        is_prime = True
        if n % i == 0:
            is_prime = False
    if is_prime:
        print("prime number")
    else:
        print("not a prime number")
num = int(input("what is the number"))
prime(n = num)

