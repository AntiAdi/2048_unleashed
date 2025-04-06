"""
    2048 Algorithm Implementation : Look Ahead for Max Merges
    Author : Aadityaraj Kaushal
    Date   : 04.04.25
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


def lookahead_move(matrix, depth):
    if depth == 0:
        return 0, None  # Base case: Evaluate board
    
    best_score = float('-inf')
    best_move = None
    
    moves = {
        'u': dummy_move_up,
        'd': dummy_move_down,
        'l': dummy_move_left,
        'r': dummy_move_right
    }
    
    for move, func in moves.items():
        new_matrix = copy.deepcopy(matrix)
        move_possible, merges = func(new_matrix)
        
        if not move_possible:
            continue
        
        future_merges, _ = lookahead_move(new_matrix, depth - 1)  
        
        total_merges = merges + future_merges 
        
        if total_merges > best_score:
            best_score = total_merges
            best_move = move
    
    return best_score, best_move


def make_best_move():
    """Runs lookahead search and executes the best move."""
    _, best_move = lookahead_move(global_variables.matrix, depth=4)
    
    if best_move:
        match best_move:
            case 'u': move_up()
            case 'd': move_down()
            case 'l': move_left()
            case 'r': move_right()
    else:
        print(f"\n\tScore = {global_variables.score}\n\tMoves = {global_variables.moves}\n\tLargest Tile = {max(max(row) for row in global_variables.matrix)}\n")
        root.after(finish_wait_time, root.quit())
    
    root.after(time_between_moves, make_best_move)

# Start automation
root.after(1, make_best_move)
root.mainloop()







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



# Need to check if a move is valid or not.
# moves = [move_left, move_right, move_up, move_down]
# dummy_moves = [dummy_move_left, dummy_move_right, dummy_move_up, dummy_move_down]

# def valid_move():
#     valid_moves = [
#         move for move, dummy_move in zip(moves, dummy_moves)
#         if dummy_move(copy.deepcopy(global_variables.matrix))  # Only include valid moves
#     ]
#     return valid_moves


# def random_move():
#     # move_count = 0
#     if not global_variables.game_over : 
#         move = valid_random_move()
#         if move != None :
#             move() 
#         elif move==None :
#             global_variables.game_over = True
#             print(f"\n\tMoves = {global_variables.moves}\n\tScore = {global_variables.score}\n")
#             root.after(400, root.quit())
#             # dummy_game_over_check(copy.deepcopy(global_variables.matrix))

#         # move_count += 1
#         root.after(3000, random_move)  # Schedule next move


# Making the dummy functions (that virtually check the next move), return the num of merges on that move.
# def greedy_for_most_merges() :
#     num_merges = 0
#     move = 'N'

#     move_possible_up, merges_up = dummy_move_up(copy.deepcopy(global_variables.matrix))
#     move_possible_down, merges_down = dummy_move_down(copy.deepcopy(global_variables.matrix))
#     move_possible_left, merges_left = dummy_move_left(copy.deepcopy(global_variables.matrix))
#     move_possible_right, merges_right = dummy_move_right(copy.deepcopy(global_variables.matrix))


#     if ((not move_possible_down) and (not move_possible_up) and (not move_possible_left) and (not move_possible_right)) :
#         print(f"\n\tMoves = {global_variables.moves}\n\tScore = {global_variables.score}\n\tLargest Tile = {max(max(row) for row in global_variables.matrix)}\n")
#         root.after(1, root.quit())
    
#     good_moves = []

#     if move_possible_up and merges_up>=num_merges:
#         if merges_up==num_merges :
#             good_moves.append('u')
#         else :
#             good_moves =['u']
#             num_merges = merges_up
    
#     if move_possible_down and merges_down>=num_merges:
#         if merges_down==num_merges :
#             good_moves.append('d')
#         else :
#             good_moves =['d']
#             num_merges = merges_down
    
#     if move_possible_left and merges_left>=num_merges:
#         if merges_left==num_merges :
#             good_moves.append('l')
#         else :
#             good_moves =['l']
#             num_merges = merges_left
    
#     if move_possible_right and merges_right>=num_merges:
#         if merges_right==num_merges :
#             good_moves.append('r')
#         else :
#             good_moves =['r']
#             num_merges = merges_right
    

#     move = random.choice(good_moves) if good_moves!=[] else 'N'
    
#     match move :
#         case 'N' :
#             fn = random.choice([move_left, move_right, move_up, move_down])
#             fn()
#         case 'u' :
#             move_up()
#         case 'd' :
#             move_down()
#         case 'r' :
#             move_right()
#         case 'l' :
#             move_left()
        
#     root.after(1, greedy_for_most_merges)
    

# # Start automation
# root.after(1, greedy_for_most_merges)  # Start after 1 msecond
# root.mainloop()


# def evaluate_board(matrix):
#     return  sum(num**10 for row in matrix for num in row) 












