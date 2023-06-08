enemies = 1

def increase_enemies():
    print(f"enemies inside : {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside : {enemies}")
