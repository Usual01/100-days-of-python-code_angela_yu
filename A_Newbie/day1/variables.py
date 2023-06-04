"""
write a program that switches the values stored in the variables a,b 
print("a = " + a)
print("b = " + b)
"""
a = input("a: ")
b = input("b: ")

temp = a
a = b
b = temp
print("a = " + str(a))
print("b = " + str(b))
################# OR ###########
a = 4
b = 5

a, b = b, a
print("a = " , a)
print("b = " , b)

