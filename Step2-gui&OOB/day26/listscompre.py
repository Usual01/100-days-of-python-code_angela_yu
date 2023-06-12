range_list = [n * 2 for n in range(1, 10)]
print(range_list)
names = ["dami", "kemi", "sina", "tobi", "tosin", "moyo", "tope", "ayo"]
short_names = [name.upper() for name in names if len(name) > 3]
print(short_names)