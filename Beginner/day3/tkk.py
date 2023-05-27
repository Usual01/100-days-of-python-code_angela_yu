import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Snake and Ladders")

# Define the game board dimensions
board_width = 10
board_height = 10

# Create the game board GUI
board_frame = tk.Frame(window)
board_frame.pack()

for row in range(board_height):
    for col in range(board_width):
        position = row * board_width + col + 1
        label_text = str(position)

        # Create a label for each position on the board
        position_label = tk.Label(
            board_frame, text=label_text, width=5, height=2, relief="solid"
        )
        position_label.grid(row=row, column=col)

# Add snakes and ladders
snakes_and_ladders = {
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
    99: 80,
}

for start, end in snakes_and_ladders.items():
    # Calculate the row and column of the start and end positions
    start_row, start_col = divmod(start - 1, board_width)
    end_row, end_col = divmod(end - 1, board_width)

    rowspan = end_row - start_row + 1 if start_row < end_row else 1

    # Create an arrow to represent the snake or ladder
    arrow = tk.Label(
        board_frame,
        text="↓" if start > end else "↑",
        font=("Arial", 12, "bold"),
    )
    arrow.grid(row=start_row, column=start_col, rowspan=rowspan)

# Start the Tkinter event loop
window.mainloop()
