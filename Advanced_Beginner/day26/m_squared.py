"""
you are doing to write a list comprehension to create a new list called result.
This new list should only contain the even numbers from the list
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num**2 for num in numbers if num % 2 == 0]
print(result)