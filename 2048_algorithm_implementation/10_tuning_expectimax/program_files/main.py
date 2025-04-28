"""
    2048 Algorithm Implementation : Look Ahead for Max Sum raised to powers
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
import numpy as np



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
    return valid_moves


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

# def lookahead_move(matrix, depth):
#     if depth == 0:
#         return 0, None  # Base case: Evaluate board
    
#     best_score = float('-inf')
#     best_move = None
    
#     moves = {
#         'u': dummy_move_up,
#         'd': dummy_move_down,
#         'l': dummy_move_left,
#         'r': dummy_move_right
#     }
    
#     for move, func in moves.items():
#         new_matrix = copy.deepcopy(matrix)
#         move_possible, merges = func(new_matrix)
        
#         if not move_possible:
#             continue
        
#         future_merges, _ = lookahead_move(new_matrix, depth - 1)  
        
#         total_merges = merges + future_merges 
        
#         if total_merges > best_score:
#             best_score = total_merges
#             best_move = move
    
#     return best_score, best_move

def get_empty_cells(matrix):
    return [(r, c) for r in range(4) for c in range(4) if matrix[r][c] == 0]

    
def simulate_random_spawn(matrix):
    empty_cells = get_empty_cells(matrix)
    if not empty_cells:
        return []  

    new_states = []
    for r, c in empty_cells:
        for value, prob in [(2, 0.9), (4, 0.1)]:  # 90% 2s, 10% 4s
            new_matrix = copy.deepcopy(matrix)
            new_matrix[r][c] = value
            new_states.append((new_matrix, prob))

    return new_states






# def lookahead_move(matrix, depth):
#     if depth == 0:
#         return evaluate_board(matrix), None  # Base case: Evaluate board
    
#     best_score = float('-inf')
#     best_move = None
    
#     moves = {
#         'u': dummy_move_up,
#         'd': dummy_move_down,
#         'l': dummy_move_left,
#         'r': dummy_move_right
#     }
    
#     for move, func in moves.items():
#         new_matrix = copy.deepcopy(matrix)
#         move_possible, score = func(new_matrix)
        
#         if not move_possible:
#             continue

#         possible_states = simulate_random_spawn(new_matrix)
        
#         if not possible_states:
#             continue

#         # Use Expectimax (weighted probability sum)
#         total_score = sum(state_score * prob for state, prob in possible_states for state_score, _ in [lookahead_move(state, depth - 1)])

#         if total_score > best_score:
#             best_score = total_score
#             best_move = move
    
#     return best_score, best_move




# def make_best_move():
#     """Runs lookahead search and executes the best move."""
#     _, best_move = lookahead_move(global_variables.matrix, depth=2)
    
#     if best_move:
#         match best_move:
#             case 'u': move_up()
#             case 'd': move_down()
#             case 'l': move_left()
#             case 'r': move_right()
#     else:
#         print(f"\n\tScore = {global_variables.score}\n\tMoves = {global_variables.moves}\n\tLargest Tile = {max(max(row) for row in global_variables.matrix)}\n")
#         root.after(1, root.quit())
    
#     root.after(1, make_best_move)

# # Start automation
# root.after(1, make_best_move)
# root.mainloop()



import numpy as np

def reset_game_state():
    global matrix, score, moves
    matrix = [[0] * 4 for _ in range(4)]
    score = 0
    moves = 0
    matrix = dummy_add_2_or_4(matrix)
    matrix = dummy_add_2_or_4(matrix)



def evaluate(matrix, weights=None):
    if weights is None:
        weights = {
            "empty": 5000,
            "smooth": 15,
            "monotonicity": 30,
            "weighted": 0.002,
            "corner": 5000,
            "value_square": 0.001
        }

    
    matrix = np.array(matrix)

    def count_empty(matrix):
        return np.sum(matrix == 0)

    def smoothness(matrix):
        smooth = 0
        for i in range(4):
            for j in range(3):
                if matrix[i][j] and matrix[i][j+1]:
                    smooth -= abs(np.log2(matrix[i][j]) - np.log2(matrix[i][j+1]))
                if matrix[j][i] and matrix[j+1][i]:
                    smooth -= abs(np.log2(matrix[j][i]) - np.log2(matrix[j+1][i]))
        return smooth

    def monotonicity(matrix):
        totals = [0, 0, 0, 0]
        for row in matrix:
            for i in range(3):
                if row[i] >= row[i+1]:
                    totals[0] += row[i] - row[i+1]
                else:
                    totals[1] += row[i+1] - row[i]
        for col in matrix.T:
            for i in range(3):
                if col[i] >= col[i+1]:
                    totals[2] += col[i] - col[i+1]
                else:
                    totals[3] += col[i+1] - col[i]
        return -min(totals[0], totals[1]) - min(totals[2], totals[3])

    def max_tile_corner(matrix):
        max_tile = np.max(matrix)
        corners = [matrix[0][0], matrix[0][3], matrix[3][0], matrix[3][3]]
        return 1 if max_tile in corners else 0

    def weighted_score(matrix):
        weights_matrix = np.array([
            [65536, 32768, 16384, 8192],
            [512,   1024,   2048, 4096],
            [256,   128,    64,   32],
            [2,     4,      8,    16]
        ])
        return np.sum(matrix * weights_matrix)

    def value_square_sum(matrix):
        return sum(num**2 for row in matrix for num in row)

    score = 0
    score += count_empty(matrix)      * weights["empty"]
    score += smoothness(matrix)       * weights["smooth"]
    score += monotonicity(matrix)     * weights["monotonicity"]
    score += weighted_score(matrix)   * weights["weighted"]
    score += max_tile_corner(matrix)  * weights["corner"]
    score += value_square_sum(matrix) * weights["value_square"]

    return score





def expectimax(matrix, depth, is_player_turn=True, weights=None):
    if depth == 0 or not get_empty_cells(matrix):
        return evaluate(matrix, weights), None

    if is_player_turn:
        best_score = float('-inf')
        best_move = None

        moves = {
            'up': dummy_move_up,
            'down': dummy_move_down,
            'left': dummy_move_left,
            'right': dummy_move_right
        }

        for move_name, move_func in moves.items():
            new_matrix, moved = move_func(copy.deepcopy(matrix))
            if not moved:
                continue

            score, _ = expectimax(new_matrix, depth - 1, False, weights)
            if score > best_score:
                best_score = score
                best_move = move_name

        return best_score, best_move

    else:
        total_score = 0
        possibilities = simulate_random_spawn(matrix)
        for new_state, prob in possibilities:
            score, _ = expectimax(new_state, depth - 1, True, weights)
            total_score += prob * score
        return total_score, None


def play_game_with_weights(weights, num_runs=5):
    total_score = 0
    max_tile = 0

    for _ in range(num_runs):  # Run multiple games for each weight configuration
        reset_game_state()
        matrix = global_variables.matrix

        while not dummy_game_over_check(matrix):
            _, move = expectimax(matrix, depth=3, weights=weights)
            if move:
                matrix, moved, gained = {
                    "up": dummy_move_up,
                    "down": dummy_move_down,
                    "left": dummy_move_left,
                    "right": dummy_move_right
                }[move](matrix)
                total_score += gained
                matrix = dummy_add_2_or_4(matrix)
            else:
                break
        
        max_tile_in_game = max(max(row) for row in matrix)
        max_tile = max(max_tile, max_tile_in_game)  # Track the max tile across multiple runs

    # Calculate average score and max tile
    avg_score = total_score / num_runs
    return avg_score, max_tile

def make_best_move():
    """Runs lookahead search and executes the best move."""

    if dummy_game_over_check(global_variables.matrix):
        # print(f"\n\tGame Over!")
        # print(f"\n\tScore = {global_variables.score}")
        # print(f"\tMoves = {global_variables.moves}")
        # print(f"\tLargest Tile = {max(max(row) for row in global_variables.matrix)}\n")
        # root.after(finish_wait_time, root.quit())
        return 

    _, best_move = expectimax(global_variables.matrix, depth=2)

    if best_move:
        match best_move:
            case 'up': move_up()
            case 'down': move_down()
            case 'left': move_left()
            case 'right': move_right()
    else:
        # Fallback in case best_move is None — pick any valid move
        valid = valid_move()
        if valid:
            fn = random.choice(valid)
            fn()
        else:
            # print("\n\tNo valid moves found — quitting.")
            root.after(10000, root.quit())
            return

    root.after(time_between_moves, make_best_move)


# Start automation
root.after(1, make_best_move)
root.mainloop()










