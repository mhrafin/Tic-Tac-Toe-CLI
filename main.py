# Players will choose between who will go first. X or O.
# Players will play their turn with the input from 1 to 9

# Removed unused import
# import pandas as pd

board_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def update_board():
    global board
    board = f"""
-------------
| {board_slots[0]} | {board_slots[1]} | {board_slots[2]} |
-------------
| {board_slots[3]} | {board_slots[4]} | {board_slots[5]} |
-------------
| {board_slots[6]} | {board_slots[7]} | {board_slots[8]} |
-------------
"""


def check_win_pattern(symbol):
    global board_slots
    win_cons = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for cons in win_cons:
        if (
            board_slots[cons[0]] == symbol
            and board_slots[cons[1]] == symbol
            and board_slots[cons[2]] == symbol
        ):
            print(f"{symbol} has won!")
            return True
    return False


current_player = None
player_one = None
player_two = None

game_mode = "on"
win = False

while game_mode != "exit":
    # Set player one and two.
    print("You have to select who goes first. X or O?")
    player_one = input().upper()
    while player_one != "X" and player_one != "O":
        player_one = input("Only insert X or O to select who goes first: ").upper()

    if player_one == "X":
        player_two = "O"
    else:
        player_two = "X"

    current_player = player_one

    update_board()
    print(board)
    while not win:
        try:
            choice = int(input(f"Player {current_player}, place your {current_player} (0-8): "))
            if board_slots[choice] == 0:
                board_slots[choice] = current_player
                update_board()
                print(board)
                win = check_win_pattern(current_player)
                if win:
                    print(f"Player {current_player} wins!")
                    break
                current_player = player_two if current_player == player_one else player_one
            else:
                print("Slot already taken, choose another slot.")
        except ValueError:
            print("Invalid input, please enter a number between 0 and 8.")
