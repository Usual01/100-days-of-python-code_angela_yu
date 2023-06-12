def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation = {
    "/" : div,
    "*" : mul,
    "-" : sub,
    "+" : add,
}
def calc():
    n1 = int(input("Enter a number"))
    for s in operation:
        print(s)
    game = True
    while game:
        operation_symbol = input("pick an operation from the symbol above") 
        n2 = int(input("enter another number"))
        
        cf = operation[operation_symbol]
        answer = cf(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        if input(f"should continue y to continue") == 'y':
            n1 = answer
        else:
            game = False
            calc()

calc()
