"""
You are going to write a program that calculates the highest score in a list
"""

scores = input("input the list").split()
for n in range(0, len(scores)):
     scores[n] = int(scores[n])
print(scores)
highest = 0
for s in scores:
   if  s > highest:
     highest = s


print(f" The highest {highest}")