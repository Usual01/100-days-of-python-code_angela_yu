"""
you are going to write a program that calculate 
the average students height from a list of heights

"""
students_heights = input("input a list of students\n").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)
total = 0
num = 0
for s in students_heights:
    total += s
    num += 1
print(total)
print(num)
avg = round(total / num)
print(avg)