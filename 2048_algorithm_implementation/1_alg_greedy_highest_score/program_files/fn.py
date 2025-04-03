from global_variables import *
import global_variables
import random
from config import *
import copy
from tkinter import messagebox
import csv



# To seed 
random.seed(random_seed)



def move_up( event=0) :
    any_movement = False


    for column in range(4) :
        merged = [False] * 4
        for main_row in range(3) :
            if global_variables.matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row+1, 4) :
                if global_variables.matrix[second_row][column] == 0 :
                    continue
                
                if global_variables.matrix[main_row][column] != global_variables.matrix[second_row][column] :
                    break

                if global_variables.matrix[main_row][column] == global_variables.matrix[second_row][column] and not merged[second_row] :
                    global_variables.matrix[main_row][column] *= 2
                    global_variables.score += global_variables.matrix[main_row][column]
                    global_variables.matrix[second_row][column] = 0
                    any_movement = True
                    merged[main_row] = True
                    break


    for column in range(4) :
        # Any movement check.
        for row in range(3) :
            if global_variables.matrix[row][column] == 0 :
                for second_row in range(row+1, 4) :
                    if global_variables.matrix[second_row][column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 0
        for row in range(4) :
            if global_variables.matrix[row][column] != 0 :
                global_variables.matrix[index_counter][column] = global_variables.matrix[row][column]
                if index_counter != row :
                    global_variables.matrix[row][column] = 0
                index_counter += 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1   
        add_2_or_4()
        log_move(global_variables.moves, global_variables.score, global_variables.matrix, filename=log_filename, direction="up")
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))
    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def move_down( event=0) :
    any_movement = False


    for column in range(4) :
        merged = [False] * 4
        for main_row in range(3,0,-1) :
            if global_variables.matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row-1,-1,-1) :
                if global_variables.matrix[second_row][column] == 0 :
                    continue
                
                if global_variables.matrix[main_row][column] != global_variables.matrix[second_row][column] :
                    break

                if global_variables.matrix[main_row][column] == global_variables.matrix[second_row][column] and not merged[second_row]:
                    global_variables.matrix[main_row][column] *= 2
                    global_variables.score += global_variables.matrix[second_row][column]
                    global_variables.matrix[second_row][column] = 0
                    any_movement = True
                    merged[second_row] = True
                    break

    for column in range(4) :
        # Any movement check.
        for row in range(3,0,-1) :
            if global_variables.matrix[row][column] == 0 :
                for second_row in range(row-1, -1,-1) :
                    if global_variables.matrix[second_row][column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 3
        for row in range(3,-1, -1) :
            if global_variables.matrix[row][column] != 0 :
                global_variables.matrix[index_counter][column] = global_variables.matrix[row][column]
                if index_counter != row :
                    global_variables.matrix[row][column] = 0
                index_counter -= 1


            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1 
        add_2_or_4()
        log_move(global_variables.moves, global_variables.score, global_variables.matrix, filename=log_filename, direction="down")
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))
    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def move_left( event=0) :
    any_movement = False


    for row in range(4) :
        merged = [False] * 4
        for main_column in range(3) :
            if global_variables.matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column+1, 4) :
                if global_variables.matrix[row][second_column] == 0 :
                    continue

                if global_variables.matrix[row][main_column] != global_variables.matrix[row][second_column] :
                    break
                
                if global_variables.matrix[row][main_column] == global_variables.matrix[row][second_column] and not merged[second_column] :
                    global_variables.matrix[row][main_column] *= 2
                    global_variables.score += global_variables.matrix[row][main_column]
                    global_variables.matrix[row][second_column] = 0
                    any_movement = True
                    merged[main_column] = True
                    break

    for row in range(4) :
        # Any movement check.
        for column in range(3) :
            if global_variables.matrix[row][column] == 0 :
                for second_column in range(column+1, 4) :
                    if global_variables.matrix[row][second_column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 0
        for column in range(4) :
            if global_variables.matrix[row][column] != 0 :
                global_variables.matrix[row][index_counter] = global_variables.matrix[row][column]
                if index_counter != column :
                    global_variables.matrix[row][column] = 0
                index_counter += 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1 
        add_2_or_4()
        log_move(global_variables.moves, global_variables.score, global_variables.matrix, filename=log_filename, direction="left")
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))
    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def move_right( event=0) :
    any_movement = False

    for row in range(4) :


        for main_column in range(3,0,-1) :
            merged = [False] * 4
            if global_variables.matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column-1,-1,-1) :
                if global_variables.matrix[row][second_column] == 0 :
                    continue

                if global_variables.matrix[row][main_column] != global_variables.matrix[row][second_column] :
                    break
                
                if global_variables.matrix[row][main_column] == global_variables.matrix[row][second_column] and not merged[second_column] :
                    global_variables.matrix[row][main_column] *= 2
                    global_variables.score += global_variables.matrix[row][main_column]
                    global_variables.matrix[row][second_column] = 0
                    any_movement = True
                    merged[main_column] = True
                    break

    for row in range(4) :
        # Any movement check.
        for column in range(3, 0,-1) :
            if global_variables.matrix[row][column] == 0 :
                for second_column in range(column-1, -1, -1) :
                    if global_variables.matrix[row][second_column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 3
        for column in range(3,-1,-1) :
            if global_variables.matrix[row][column] != 0 :
                global_variables.matrix[row][index_counter] = global_variables.matrix[row][column]
                if index_counter != column :
                    global_variables.matrix[row][column] = 0
                index_counter -= 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1 
        add_2_or_4()
        log_move(global_variables.moves, global_variables.score, global_variables.matrix, filename=log_filename, direction="right")
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))


    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def add_2_or_4() :
    # Set the moves label.
    lab_moves.config(text=f"Number of Moves = {global_variables.moves}", font=("", 16), bg="#F5F5F5", fg="#333333", width=50)

    # Set the score label.
    lab_score.config(text=f"Current Score = {global_variables.score}", font=("", 16), bg="#F5F5F5", fg="#333333", width=50)

    # First Know the zero indices. Then do a random.choice from them.
    zero_indices = []
    for row in range(4) :
        for column in range(4) :
            if global_variables.matrix[row][column] == 0 :
                zero_indices.append([row,column])
    
    if len(zero_indices) == 0 :
        return False
    else :
        row_column = random.choice(zero_indices)
        global_variables.matrix[row_column[0]][row_column[1]] = random.choice([2,2,2,2,2,2,2,2,2,4])
        set_label_equal_matrix()
        return True

def set_label_equal_matrix() :

    var_00.set(int(global_variables.matrix[0][0]))
    var_01.set(int(global_variables.matrix[0][1]))
    var_02.set(int(global_variables.matrix[0][2]))
    var_03.set(int(global_variables.matrix[0][3]))

    var_10.set(int(global_variables.matrix[1][0]))
    var_11.set(int(global_variables.matrix[1][1]))
    var_12.set(int(global_variables.matrix[1][2]))
    var_13.set(int(global_variables.matrix[1][3]))

    var_20.set(int(global_variables.matrix[2][0]))
    var_21.set(int(global_variables.matrix[2][1]))
    var_22.set(int(global_variables.matrix[2][2]))
    var_23.set(int(global_variables.matrix[2][3]))

    var_30.set(int(global_variables.matrix[3][0]))
    var_31.set(int(global_variables.matrix[3][1]))
    var_32.set(int(global_variables.matrix[3][2]))
    var_33.set(int(global_variables.matrix[3][3])) 

    # Changing the colors of tiles based on the value on them.
    lab_00.config( bg=TILE_COLORS.get(global_variables.matrix[0][0]), fg=TEXT_COLORS.get(global_variables.matrix[0][0]))
    lab_01.config( bg=TILE_COLORS.get(global_variables.matrix[0][1]), fg=TEXT_COLORS.get(global_variables.matrix[0][1]))
    lab_02.config( bg=TILE_COLORS.get(global_variables.matrix[0][2]), fg=TEXT_COLORS.get(global_variables.matrix[0][2]))
    lab_03.config( bg=TILE_COLORS.get(global_variables.matrix[0][3]), fg=TEXT_COLORS.get(global_variables.matrix[0][3]))

    lab_10.config( bg=TILE_COLORS.get(global_variables.matrix[1][0]), fg=TEXT_COLORS.get(global_variables.matrix[1][0]))
    lab_11.config( bg=TILE_COLORS.get(global_variables.matrix[1][1]), fg=TEXT_COLORS.get(global_variables.matrix[1][1]))
    lab_12.config( bg=TILE_COLORS.get(global_variables.matrix[1][2]), fg=TEXT_COLORS.get(global_variables.matrix[1][2]))
    lab_13.config( bg=TILE_COLORS.get(global_variables.matrix[1][3]), fg=TEXT_COLORS.get(global_variables.matrix[1][3]))

    lab_20.config( bg=TILE_COLORS.get(global_variables.matrix[2][0]), fg=TEXT_COLORS.get(global_variables.matrix[2][0]))
    lab_21.config( bg=TILE_COLORS.get(global_variables.matrix[2][1]), fg=TEXT_COLORS.get(global_variables.matrix[2][1]))
    lab_22.config( bg=TILE_COLORS.get(global_variables.matrix[2][2]), fg=TEXT_COLORS.get(global_variables.matrix[2][2]))
    lab_23.config( bg=TILE_COLORS.get(global_variables.matrix[2][3]), fg=TEXT_COLORS.get(global_variables.matrix[2][3]))

    lab_30.config( bg=TILE_COLORS.get(global_variables.matrix[3][0]), fg=TEXT_COLORS.get(global_variables.matrix[3][0]))
    lab_31.config( bg=TILE_COLORS.get(global_variables.matrix[3][1]), fg=TEXT_COLORS.get(global_variables.matrix[3][1]))
    lab_32.config( bg=TILE_COLORS.get(global_variables.matrix[3][2]), fg=TEXT_COLORS.get(global_variables.matrix[3][2]))
    lab_33.config( bg=TILE_COLORS.get(global_variables.matrix[3][3]), fg=TEXT_COLORS.get(global_variables.matrix[3][3]))


# Dummy Functions for Back Testing.

def dummy_move_left(dummy_matrix) :
    any_movement = False
    score_change = 0
    

    for row in range(4) :
        merged = [False] * 4
        for main_column in range(3) :
            if dummy_matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column+1, 4) :
                if dummy_matrix[row][second_column] == 0 :
                    continue

                if dummy_matrix[row][main_column] != dummy_matrix[row][second_column] :
                    break
                
                if dummy_matrix[row][main_column] == dummy_matrix[row][second_column] and not merged[second_column] :
                    dummy_matrix[row][main_column] *= 2
                    dummy_matrix[row][second_column] = 0
                    score_change += dummy_matrix[row][main_column] 
            
                    any_movement = True
                    merged[main_column] = True
                    break

    for row in range(4) :
        # Any movement check.
        for column in range(3) :
            if dummy_matrix[row][column] == 0 :
                for second_column in range(column+1, 4) :
                    if dummy_matrix[row][second_column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 0
        for column in range(4) :
            if dummy_matrix[row][column] != 0 :
                dummy_matrix[row][index_counter] = dummy_matrix[row][column]
                if index_counter != column :
                    dummy_matrix[row][column] = 0
                index_counter += 1
            
    if any_movement :
        # dummy_add_2_or_4()
        pass
    return any_movement, score_change

def dummy_move_right(dummy_matrix) :
    any_movement = False
    score_change = 0
    


    for row in range(4) :


        for main_column in range(3,0,-1) :
            merged = [False] * 4
            if dummy_matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column-1,-1,-1) :
                if dummy_matrix[row][second_column] == 0 :
                    continue

                if dummy_matrix[row][main_column] != dummy_matrix[row][second_column] :
                    break
                
                if dummy_matrix[row][main_column] == dummy_matrix[row][second_column] and not merged[second_column] :
                    dummy_matrix[row][main_column] *= 2
                
                    score_change += dummy_matrix[row][main_column]
                    dummy_matrix[row][second_column] = 0
                    any_movement = True
                    merged[main_column] = True
                    break

    for row in range(4) :
        # Any movement check.
        for column in range(3, 0,-1) :
            if dummy_matrix[row][column] == 0 :
                for second_column in range(column-1, -1, -1) :
                    if dummy_matrix[row][second_column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 3
        for column in range(3,-1,-1) :
            if dummy_matrix[row][column] != 0 :
                dummy_matrix[row][index_counter] = dummy_matrix[row][column]
                if index_counter != column :
                    dummy_matrix[row][column] = 0
                index_counter -= 1
            
    if any_movement :
        # dummy_add_2_or_4()
        pass


    return any_movement, score_change

def dummy_move_down(dummy_matrix) :
    any_movement = False
    score_change = 0
   


    for column in range(4) :
        merged = [False] * 4
        for main_row in range(3) :
            if dummy_matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row+1, 4) :
                if dummy_matrix[second_row][column] == 0 :
                    continue
                
                if dummy_matrix[main_row][column] != dummy_matrix[second_row][column] :
                    break

                if dummy_matrix[main_row][column] == dummy_matrix[second_row][column] and not merged[second_row]:
                    dummy_matrix[second_row][column] *= 2
            
                    score_change += dummy_matrix[second_row][column]
                    dummy_matrix[main_row][column] = 0
                    any_movement = True
                    merged[main_row] = True
                    break

    for column in range(4) :
        # Any movement check.
        for row in range(3,0,-1) :
            if dummy_matrix[row][column] == 0 :
                for second_row in range(row-1, -1,-1) :
                    if dummy_matrix[second_row][column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 3
        for row in range(3,-1, -1) :
            if dummy_matrix[row][column] != 0 :
                dummy_matrix[index_counter][column] = dummy_matrix[row][column]
                if index_counter != row :
                    dummy_matrix[row][column] = 0
                index_counter -= 1
            

    if any_movement :
        # dummy_add_2_or_4()
        pass
    return any_movement, score_change

def dummy_move_up(dummy_matrix) :


    any_movement = False
    score_change = 0
    


    for column in range(4) :
        merged = [False] * 4
        for main_row in range(3) :
            if dummy_matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row+1, 4) :
                if dummy_matrix[second_row][column] == 0 :
                    continue
                
                if dummy_matrix[main_row][column] != dummy_matrix[second_row][column] :
                    break

                if dummy_matrix[main_row][column] == dummy_matrix[second_row][column] and not merged[second_row] :
                    dummy_matrix[main_row][column] *= 2
                    
                    score_change += dummy_matrix[main_row][column]
                    dummy_matrix[second_row][column] = 0
                    any_movement = True
                    merged[main_row] = True
                    break


    for column in range(4) :
        # Any movement check.
        for row in range(3) :
            if dummy_matrix[row][column] == 0 :
                for second_row in range(row+1, 4) :
                    if dummy_matrix[second_row][column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 0
        for row in range(4) :
            if dummy_matrix[row][column] != 0 :
                dummy_matrix[index_counter][column] = dummy_matrix[row][column]
                if index_counter != row :
                    dummy_matrix[row][column] = 0
                index_counter += 1
            

    # set_label_equal_matrix()
    if any_movement : 
        # dummy_add_2_or_4()
        pass
    return any_movement ,score_change

def dummy_add_2_or_4(dummy_matrix) :
    # First Know the zero indices. Then do a random.choice from them.
    zero_indices = []
    for row in range(4) :
        for column in range(4) :
            if dummy_matrix[row][column] == 0 :
                zero_indices.append([row,column])
    
    if len(zero_indices) == 0 :
        return False
    else :
        row_column = random.choice(zero_indices)
        dummy_matrix[row_column[0]][row_column[1]] = random.choice([2,2,2,2,2,2,2,2,2,4])
        return True
    
def dummy_game_over_check(dummy_matrix) : 
    
    if not (dummy_move_up(dummy_matrix)[0] or dummy_move_down(dummy_matrix)[0] or dummy_move_left(dummy_matrix)[0] or dummy_move_right(dummy_matrix)[0]) :
        # messagebox.showerror("", "Game Over !")
        global_variables.game_over = True
        return True
    else :
        return False




def log_move(move_number, score, matrix, filename, direction):
    # Flatten the 4x4 matrix into a single list
    flattened_matrix = [num for row in matrix for num in row]

    # Open the CSV file
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writerow(["Move", "Score", "Matrix", "Previous_Move", "Largest_Tile"])

        # Log the move
        writer.writerow([move_number, score, str(flattened_matrix), str(direction), max(max(row) for row in matrix)])


def clear_screen() :
    if messagebox.askokcancel("Alert !", "Reset the Game ?") :
        global_variables.score = 0
        global_variables.moves = 0
        global_variables.matrix.clear()
        global_variables.matrix = [[0]*4 for _ in range(4)]

        # Initialise the grid with zeroes.
        global_variables.var_00.set(int(global_variables.matrix[0][0]))
        global_variables.var_01.set(int(global_variables.matrix[0][1]))
        global_variables.var_02.set(int(global_variables.matrix[0][2]))
        global_variables.var_03.set(int(global_variables.matrix[0][3]))

        global_variables.var_10.set(int(global_variables.matrix[1][0]))
        global_variables.var_11.set(int(global_variables.matrix[1][1]))
        global_variables.var_12.set(int(global_variables.matrix[1][2]))
        global_variables.var_13.set(int(global_variables.matrix[1][3]))

        global_variables.var_20.set(int(global_variables.matrix[2][0]))
        global_variables.var_21.set(int(global_variables.matrix[2][1]))
        global_variables.var_22.set(int(global_variables.matrix[2][2]))
        global_variables.var_23.set(int(global_variables.matrix[2][3]))

        global_variables.var_30.set(int(global_variables.matrix[3][0]))
        global_variables.var_31.set(int(global_variables.matrix[3][1]))
        global_variables.var_32.set(int(global_variables.matrix[3][2]))
        global_variables.var_33.set(int(global_variables.matrix[3][3])) 


        lab_00.config(textvariable=global_variables.var_00 , bg=TILE_COLORS.get(global_variables.matrix[0][0]), fg=TEXT_COLORS.get(global_variables.matrix[0][0]))
        lab_01.config(textvariable=global_variables.var_01 , bg=TILE_COLORS.get(global_variables.matrix[0][1]), fg=TEXT_COLORS.get(global_variables.matrix[0][1]))
        lab_02.config(textvariable=global_variables.var_02 , bg=TILE_COLORS.get(global_variables.matrix[0][2]), fg=TEXT_COLORS.get(global_variables.matrix[0][2]))
        lab_03.config(textvariable=global_variables.var_03 , bg=TILE_COLORS.get(global_variables.matrix[0][3]), fg=TEXT_COLORS.get(global_variables.matrix[0][3]))

        lab_10.config(textvariable=global_variables.var_10 , bg=TILE_COLORS.get(global_variables.matrix[1][0]), fg=TEXT_COLORS.get(global_variables.matrix[1][0]))
        lab_11.config(textvariable=global_variables.var_11 , bg=TILE_COLORS.get(global_variables.matrix[1][1]), fg=TEXT_COLORS.get(global_variables.matrix[1][1]))
        lab_12.config(textvariable=global_variables.var_12 , bg=TILE_COLORS.get(global_variables.matrix[1][2]), fg=TEXT_COLORS.get(global_variables.matrix[1][2]))
        lab_13.config(textvariable=global_variables.var_13 , bg=TILE_COLORS.get(global_variables.matrix[1][3]), fg=TEXT_COLORS.get(global_variables.matrix[1][3]))

        lab_20.config(textvariable=global_variables.var_20 , bg=TILE_COLORS.get(global_variables.matrix[2][0]), fg=TEXT_COLORS.get(global_variables.matrix[2][0]))
        lab_21.config(textvariable=global_variables.var_21 , bg=TILE_COLORS.get(global_variables.matrix[2][1]), fg=TEXT_COLORS.get(global_variables.matrix[2][1]))
        lab_22.config(textvariable=global_variables.var_22 , bg=TILE_COLORS.get(global_variables.matrix[2][2]), fg=TEXT_COLORS.get(global_variables.matrix[2][2]))
        lab_23.config(textvariable=global_variables.var_23 , bg=TILE_COLORS.get(global_variables.matrix[2][3]), fg=TEXT_COLORS.get(global_variables.matrix[2][3]))

        lab_30.config(textvariable=global_variables.var_30 , bg=TILE_COLORS.get(global_variables.matrix[3][0]), fg=TEXT_COLORS.get(global_variables.matrix[3][0]))
        lab_31.config(textvariable=global_variables.var_31 , bg=TILE_COLORS.get(global_variables.matrix[3][1]), fg=TEXT_COLORS.get(global_variables.matrix[3][1]))
        lab_32.config(textvariable=global_variables.var_32 , bg=TILE_COLORS.get(global_variables.matrix[3][2]), fg=TEXT_COLORS.get(global_variables.matrix[3][2]))
        lab_33.config(textvariable=global_variables.var_33 , bg=TILE_COLORS.get(global_variables.matrix[3][3]), fg=TEXT_COLORS.get(global_variables.matrix[3][3]))

        # Generate a random 2/4 to start the game.
        add_2_or_4()
        root.update_idletasks()



# For Reset button.
but_reset.config(command=clear_screen)



















