import random

# boards = [
#     100 99  98  97  96  95  94  93  92  91
#   81 82  83  84  85  86  87  88  89  90
#   80 79  78  77  76  75  74  73  72  71
#   61 62  63  64  65  66  67  68  69  70
#   60 59  58  57  56  55  54  53  52  51
#   41 42  43  44  45  46  47  48  49  50
#   40 39  38  37  36  35  34  33  32  31
#   21 22  23  24  25  26  27  28  29  30
#   20 19  18  17  16  15  14  13  12  11
#    1  2   3   4   5   6   7   8   9  10
#    ]

board = {
    3: 22,
    5: 8,
    11: 26,
    17: 4,
    19: 7,
    20: 29,
    27: 1,
    21: 9,
    32: 16,
    34: 30,
    24: 38,
    36: 23,
    48: 51,
    50: 13,
    62: 45,
    64: 60,
    71: 92,
    74: 53,
    83: 97,
    89: 68,
    95: 75,
    99: 80
}

# Initialize players
player1 = 0
player2 = 0

# Game loop
while True:
    # Player 1's turn
    print("Player 1's turn")
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print(f"Player 1 rolled: {dice}")
    player1 += dice

    if player1 in board:
        player1 = board[player1]
        print("Oops! You landed on a snake or ladder.")

    if player1 >= 100:
        print("Player 1 wins!")
        break

    print(f"Player 1 is now at position {player1}\n")

    # Player 2's turn
    print("Player 2's turn")
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print(f"Player 2 rolled: {dice}")
    player2 += dice

    if player2 in board:
        player2 = board[player2]
        print("Oops! You landed on a snake or ladder.")

    if player2 >= 100:
        print("Player 2 wins!")
        break

    print(f"Player 2 is now at position {player2}\n")