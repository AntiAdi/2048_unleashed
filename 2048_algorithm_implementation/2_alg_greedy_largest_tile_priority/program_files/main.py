"""
    2048 Algorithm Implementation : Greedy for Largest Tile Priority
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



# Need to check if a move is valid or not.
moves = [move_left, move_right, move_up, move_down]
dummy_moves = [dummy_move_left, dummy_move_right, dummy_move_up, dummy_move_down]

def valid_move():
    valid_moves = [
        move for move, dummy_move in zip(moves, dummy_moves)
        if dummy_move(copy.deepcopy(global_variables.matrix))  # Only include valid moves
    ]
    return random.choice(valid_moves)


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



# Making the dummy functions (that virtually check the next move), return the score change on that move.
# def greedy_for_biggest_score() :
#     score_change = 0
#     move = 'N'

#     move_possible_up, score_up = dummy_move_up(copy.deepcopy(global_variables.matrix))
#     move_possible_down, score_down = dummy_move_down(copy.deepcopy(global_variables.matrix))
#     move_possible_left, score_left = dummy_move_left(copy.deepcopy(global_variables.matrix))
#     move_possible_right, score_right = dummy_move_right(copy.deepcopy(global_variables.matrix))


#     if ((not move_possible_down) and (not move_possible_up) and (not move_possible_left) and (not move_possible_right)) :
#         print(f"\n\tMoves = {global_variables.moves}\n\tScore = {global_variables.score}\n\tLargest Tile = {max(max(row) for row in global_variables.matrix)}\n")
#         root.after(1, root.quit())
    

#     if move_possible_up :
#         if score_up>score_change :
#             move = 'u'
#             score_change = score_up
#         else :
#             pass
    
#     if move_possible_down :
#         if score_down>score_change :
#             move = 'd'
#             score_change = score_down
#         else :
#             pass

#     if move_possible_right :
#         if score_right>score_change :
#             move = 'r'
#             score_change = score_right
#         else :
#             pass

#     if move_possible_left :
#         if score_left>score_change :
#             move = 'l'
#             score_change = score_left
#         else :
#             pass
    
 

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
        
#     root.after(1, greedy_for_biggest_score)
    

# # Start automation
# root.after(1, greedy_for_biggest_score)  # Start after 1 second
# root.mainloop()








def greedy_for_largest_tile_priority() :
    move = None #u for up and so on. N for default.
    largest_tile_combination = 0

    up_possible, up_scorechange, up_largest_tile = dummy_move_up(copy.deepcopy(global_variables.matrix))
    down_possible, down_scorechange, down_largest_tile = dummy_move_down(copy.deepcopy(global_variables.matrix))
    left_possible, left_scorechange, left_largest_tile = dummy_move_left(copy.deepcopy(global_variables.matrix))
    right_possible, right_scorechange, right_largest_tile = dummy_move_right(copy.deepcopy(global_variables.matrix))

    if ((not down_possible) and (not up_possible) and (not left_possible) and (not right_possible)) :
        print(f"\n\tMoves = {global_variables.moves}\n\tScore = {global_variables.score}\n\tLargest Tile = {max(max(row) for row in global_variables.matrix)}\n")
        root.after(1, root.quit())
        return None

    valid_moves = []

    max_tile = max(up_largest_tile, down_largest_tile, left_largest_tile, right_largest_tile)

    if up_possible and up_largest_tile == max_tile:
        valid_moves.append('u')
    if down_possible and down_largest_tile == max_tile:
        valid_moves.append('d')
    if left_possible and left_largest_tile == max_tile:
        valid_moves.append('l')
    if right_possible and right_largest_tile == max_tile:
        valid_moves.append('r')



    move = random.choice(valid_moves) if valid_moves else None

  
    match move :
        case 'u' :
            move_up()
        case 'd' :
            move_down()
        case 'r' :
            move_right()
        case 'l' :
            move_left()

    
    root.after(1, greedy_for_largest_tile_priority)


# # Start automation
root.after(1, greedy_for_largest_tile_priority)  # Start after 1 second
root.mainloop()


    






























