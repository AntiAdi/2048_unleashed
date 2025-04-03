"""
    2048 Random Alg Implementation
    Author : Aadityaraj Kaushal
    Date   : 03.04.25
"""

from tkinter import *
import random
from config import TILE_COLORS, TEXT_COLORS
from fn import *
from global_variables import *
import global_variables
import copy



# Initialise the grid with zeroes.
set_label_equal_matrix()
# Generate a random 2/4 to start the game.
add_2_or_4()


# Gridding Labels.
lab_00.grid(row=0 , column=0, padx=10, pady=10)
lab_01.grid(row=0 , column=1, padx=10, pady=10)
lab_02.grid(row=0 , column=2, padx=10, pady=10)
lab_03.grid(row=0 , column=3, padx=10, pady=10)

lab_10.grid(row=1 , column=0, padx=10, pady=10)
lab_11.grid(row=1 , column=1, padx=10, pady=10)
lab_12.grid(row=1 , column=2, padx=10, pady=10)
lab_13.grid(row=1 , column=3, padx=10, pady=10)

lab_20.grid(row=2 , column=0, padx=10, pady=10)
lab_21.grid(row=2 , column=1, padx=10, pady=10)
lab_22.grid(row=2 , column=2, padx=10, pady=10)
lab_23.grid(row=2 , column=3, padx=10, pady=10)

lab_30.grid(row=3 , column=0, padx=10, pady=10)
lab_31.grid(row=3 , column=1, padx=10, pady=10)
lab_32.grid(row=3 , column=2, padx=10, pady=10)
lab_33.grid(row=3 , column=3, padx=10, pady=10)

lab_moves.grid(row=4, column=0, columnspan=4)
lab_score.grid(row=5, column=0, columnspan=4)

but_reset.grid(row=6, column=0, columnspan=2)
# but_undo.grid(row=6, column=2, columnspan=2)



# for _ in range(1000) :
#     a = random.randint(1,4)
#     match a :
#         case 1 :
#             move_down()
#         case 2 : 
#             move_left()
#         case 3 :
#             move_up()
#         case 4 : 
#             move_right()
#     print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")





# Keystroke Input.
# root.bind("<Left>", move_left)
# root.bind("<Right>", move_right)
# root.bind("<Up>", move_up)
# root.bind("<Down>", move_down)



# Need to check if a move is valid or not. Then choose a random move from the valid moves available.
moves = [move_left, move_right, move_up, move_down]
dummy_moves = [dummy_move_left, dummy_move_right, dummy_move_up, dummy_move_down]

def valid_random_move():
    valid_moves = [
        move for move, dummy_move in zip(moves, dummy_moves)
        if dummy_move(copy.deepcopy(global_variables.matrix))  # Only include valid moves
    ]
    return random.choice(valid_moves) if valid_moves else None  #


# With Game Over Check as well.
def random_move():
    # move_count = 0
    if not global_variables.game_over : 
        move = valid_random_move()
        if move != None :
            move() 
        elif move==None :
            global_variables.game_over = True
            print(f"\n\tMoves = {global_variables.moves}\n\tScore = {global_variables.score}\n\tLargest Tile = {max(max(row) for row in matrix)}\n")
            root.after(1, root.quit())
            # dummy_game_over_check(copy.deepcopy(global_variables.matrix))

        # move_count += 1
        root.after(1, random_move)  # Schedule next move


    

# Start automation
root.after(1000, random_move)  # Start after 1 second
root.mainloop()

