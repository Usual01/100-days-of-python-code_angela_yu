# travel_log = [
#     {
#     "country": "france",
#     "visits": 12,
#     "cities": ["paris", "lille", "Dijon"]
#     }, 
#     {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Sttugart"]
#     }
# ]
#TypeError: travel_log.append({"Russia", 2, ["Moscow", "saint-petersburg"]})

#print(travel_log)
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

new_entry = {
    "country": "Russia",
    "visits": 2,
    "cities": ["Moscow", "Saint Petersburg"]
}

travel_log.append(new_entry)

print(travel_log)





# A TypeError occurs when you try to perform an operation or use a function/method with an argument of an incorrect type. Here are a few common scenarios where a TypeError can occur:

# Incorrect argument type: If you pass an argument of an unexpected or incompatible type to a function or method, it can result in a TypeError. For example, if a function expects an integer as an argument but you pass a string, it will raise a TypeError.

# Unhashable type: Certain data types, such as lists or dictionaries, are mutable and unhashable, meaning they cannot be used as keys in dictionaries or elements in sets. If you try to use an unhashable type as a key or element, a TypeError will be raised.

# Incorrect usage of operators: If you use an operator with operands of incompatible types, a TypeError can occur. For example, trying to add a string and an integer using the + operator will raise a TypeError.

# Incorrect indexing or slicing: If you try to index or slice a data structure using an invalid index or slice, a TypeError can be raised. For example, accessing an index that is out of range for a list or string will result in a TypeError.

# It's important to carefully check the types of variables and arguments being used in your code to avoid TypeError exceptions.