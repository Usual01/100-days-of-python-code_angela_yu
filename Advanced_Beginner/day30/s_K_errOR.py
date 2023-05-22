facebook_p = [
    {'likes': 21 , "comment": 2 },
    {'likes': 13, "comment":2 , "shares": 1},
    {'likes': 33, "comment": 8, "shares": 3},
    {'likes': 20, "comment": 20, "shares": 20 },
    {'likes': 2, "shares": 2},
    {'likes': 4, 'shares': 2},
    {'likes': 1, 'shares':1},
    {'likes': 19, "comment": 3 }
]
# trying to skip a keyerror incase a value not present in the dict
total = 0
for p in facebook_p:
    try:
        total = total + p["likes"]
    except KeyError:
        pass

print(total)