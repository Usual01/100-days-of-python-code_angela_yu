def add(*args):
    sum = 0
    for n in args:
        print(n)
        sum += n
    print(f"The sum is {sum}")
    return sum

print(add(2, 3, 4))