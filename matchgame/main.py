import random
import tkinter as tk
import tkinter.messagebox

# Define the game board
board_size = 4
cards = list(range(board_size**2 // 2)) * 2
random.shuffle(cards)
board = [cards[i:i+board_size] for i in range(0, board_size**2, board_size)]

# Initialize GUI
root = tk.Tk()
root.title("Memory Game")

# Define card click event
def flip_card(row, col):
    global first_card, num_flips
    if buttons[row][col]["text"] != " " or len(flipped) == 2:
        return
    buttons[row][col]["text"] = str(board[row][col])
    flipped.append((row, col))
    if len(flipped) == 1:
        first_card = board[row][col]
    else:
        num_flips += 1
        if board[row][col] == first_card:
            flipped.clear()
            if all(button["text"] != " " for row in buttons for button in row):
                play_again = tkinter.messagebox.askyesno("Memory Game", "You win! Play again?")
                if play_again:
                    new_game()
                else:
                    root.destroy()
        else:
            root.after(1000, unflip_cards)

# Define card unflip event
def unflip_cards():
    global flipped
    for row, col in flipped:
        buttons[row][col]["text"] = " "
    flipped.clear()

# Create game board buttons
buttons = []
for row in range(board_size):
    button_row = []
    for col in range(board_size):
        button = tk.Button(root, text=" ", width=4, height=2,
                           command=lambda row=row, col=col: flip_card(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Start game loop
flipped = []
first_card = None
num_flips = 0

def new_game():
    global flipped, first_card, num_flips, board
    flipped = []
    first_card = None
    num_flips = 0
    random.shuffle(cards)
    board = [cards[i:i+board_size] for i in range(0, board_size**2, board_size)]
    for row in range(board_size):
        for col in range(board_size):
            buttons[row][col]["text"] = " "
    root.update()

new_game()

root.mainloop()
