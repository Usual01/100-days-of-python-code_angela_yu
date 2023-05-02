"""
create functions for addition, substraction, multiplication and division
"""
def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def divide(a, b):
    result = a / b
    return result

def multiply(a, b):
    result = a * b
    return result
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = int(input("Enter first number\n"))
    continue_s = True
    while continue_s:
        num2 = int(input("Enter second nmber\n"))
        operation = input("What operation\n")
        calc = operations[operation]
        ans = calc(num1, num2)
        print(f"{num1} {operation} {num2} = {ans}")

        ca_co = input("Type Y to coontinue calculating")
        if ca_co == 'y':
            num1 = ans
        else:
            continue_s = False
            calculator()
calculator()
