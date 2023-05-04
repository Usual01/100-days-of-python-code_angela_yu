for n in range(1, 101):
    if (n % 3 == 0 or n % 5 == 0):
        print("fizz")
    if n % 5 == 0:
        print("buzz")
    if n % 3 == 0:
        print("fizzbuzz")
    else:
        print([n])
    #correct
    for n in range(1, 101):
        if (n % 3 == 0 and n % 5 == 0):
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        elif n % 3 == 0:
            print("fizzbuzz")
        else:
            print(n)