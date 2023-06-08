enemies = 1

print(f"enemies before: {enemies}")
def increase_enemies():
    print(f"enemies inside : {enemies}")
    return enemies + 1
print(f"enemies after block: {enemies}")

enemies = increase_enemies()
print(f"enemies after: {enemies}")

print(f"enemies outside : {enemies}")
