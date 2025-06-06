from global_variables import *
import global_variables
import random
from config import *
import copy
from tkinter import messagebox



def move_up( event=0) :
    any_movement = False

    merged = [False] * 4

    for column in range(4) :
        for main_row in range(3) :
            if matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row+1, 4) :
                if matrix[second_row][column] == 0 :
                    continue
                
                if matrix[main_row][column] != matrix[second_row][column] :
                    break

                if matrix[main_row][column] == matrix[second_row][column] and not merged[second_row] :
                    matrix[main_row][column] *= 2
                    matrix[second_row][column] = 0
                    any_movement = True
                    merged[main_row] = True
                    break


    for column in range(4) :
        # Any movement check.
        for row in range(3) :
            if matrix[row][column] == 0 :
                for second_row in range(row+1, 4) :
                    if matrix[second_row][column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 0
        for row in range(4) :
            if matrix[row][column] != 0 :
                matrix[index_counter][column] = matrix[row][column]
                if index_counter != row :
                    matrix[row][column] = 0
                index_counter += 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1   
        add_2_or_4()
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))
    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def move_down( event=0) :
    any_movement = False

    merged = [False] * 4

    for column in range(4) :
        for main_row in range(3,0,-1) :
            if matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row-1,-1,-1) :
                if matrix[second_row][column] == 0 :
                    continue
                
                if matrix[main_row][column] != matrix[second_row][column] :
                    break

                if matrix[main_row][column] == matrix[second_row][column] and not merged[second_row]:
                    matrix[second_row][column] =0
                    matrix[main_row][column] *= 2
                    any_movement = True
                    merged[second_row] = True
                    break

    for column in range(4) :
        # Any movement check.
        for row in range(3,0,-1) :
            if matrix[row][column] == 0 :
                for second_row in range(row-1, -1,-1) :
                    if matrix[second_row][column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 3
        for row in range(3,-1, -1) :
            if matrix[row][column] != 0 :
                matrix[index_counter][column] = matrix[row][column]
                if index_counter != row :
                    matrix[row][column] = 0
                index_counter -= 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1 
        add_2_or_4()
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))
    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def move_left( event=0) :
    any_movement = False

    merged = [False] * 4

    for row in range(4) :
        for main_column in range(3) :
            if matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column+1, 4) :
                if matrix[row][second_column] == 0 :
                    continue

                if matrix[row][main_column] != matrix[row][second_column] :
                    break
                
                if matrix[row][main_column] == matrix[row][second_column] and not merged[second_column] :
                    matrix[row][main_column] *= 2
                    matrix[row][second_column] = 0
                    any_movement = True
                    merged[main_column] = True
                    break

    for row in range(4) :
        # Any movement check.
        for column in range(3) :
            if matrix[row][column] == 0 :
                for second_column in range(column+1, 4) :
                    if matrix[row][second_column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 0
        for column in range(4) :
            if matrix[row][column] != 0 :
                matrix[row][index_counter] = matrix[row][column]
                if index_counter != column :
                    matrix[row][column] = 0
                index_counter += 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1 
        add_2_or_4()
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))
    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def move_right( event=0) :
    any_movement = False

    for row in range(4) :

        merged = [False] * 4

        for main_column in range(3,0,-1) :
            if matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column-1,-1,-1) :
                if matrix[row][second_column] == 0 :
                    continue

                if matrix[row][main_column] != matrix[row][second_column] :
                    break
                
                if matrix[row][main_column] == matrix[row][second_column] and not merged[second_column] :
                    matrix[row][main_column] *= 2
                    matrix[row][second_column] = 0
                    any_movement = True
                    merged[main_column] = True
                    break

    for row in range(4) :
        # Any movement check.
        for column in range(3, 0,-1) :
            if matrix[row][column] == 0 :
                for second_column in range(column-1, -1, -1) :
                    if matrix[row][second_column] != 0 :
                        any_movement = True

        # Merge zeroes.
        index_counter = 3
        for column in range(3,-1,-1) :
            if matrix[row][column] != 0 :
                matrix[row][index_counter] = matrix[row][column]
                if index_counter != column :
                    matrix[row][column] = 0
                index_counter -= 1
            

    # set_label_equal_matrix()
    if any_movement :
        global_variables.moves += 1 
        add_2_or_4()
    else :
        dummy_game_over_check(copy.deepcopy(global_variables.matrix))


    # print(dummy_game_over_check(copy.deepcopy(global_variables.matrix)))
    # print(f"L={dummy_move_left(copy.deepcopy(global_variables.matrix))} R={dummy_move_right(copy.deepcopy(global_variables.matrix))} U={dummy_move_up(copy.deepcopy(global_variables.matrix))} D={dummy_move_down(copy.deepcopy(global_variables.matrix))}")
    return any_movement

def add_2_or_4() :
    # Set the moves label.
    lab_moves.config(text=f"Number of Moves = {global_variables.moves}", font=("", 16), bg="#F5F5F5", fg="#333333", width=50)

    # First Know the zero indices. Then do a random.choice from them.
    zero_indices = []
    for row in range(4) :
        for column in range(4) :
            if matrix[row][column] == 0 :
                zero_indices.append([row,column])
    
    if len(zero_indices) == 0 :
        return False
    else :
        row_column = random.choice(zero_indices)
        matrix[row_column[0]][row_column[1]] = random.choice([2,2,2,2,2,2,2,2,2,4])
        set_label_equal_matrix()
        return True

def set_label_equal_matrix() :

    var_00.set(int(matrix[0][0]))
    var_01.set(int(matrix[0][1]))
    var_02.set(int(matrix[0][2]))
    var_03.set(int(matrix[0][3]))

    var_10.set(int(matrix[1][0]))
    var_11.set(int(matrix[1][1]))
    var_12.set(int(matrix[1][2]))
    var_13.set(int(matrix[1][3]))

    var_20.set(int(matrix[2][0]))
    var_21.set(int(matrix[2][1]))
    var_22.set(int(matrix[2][2]))
    var_23.set(int(matrix[2][3]))

    var_30.set(int(matrix[3][0]))
    var_31.set(int(matrix[3][1]))
    var_32.set(int(matrix[3][2]))
    var_33.set(int(matrix[3][3])) 

    # Changing the colors of tiles based on the value on them.
    lab_00.config(bg=TILE_COLORS.get(matrix[0][0]), fg=TEXT_COLORS.get(matrix[0][0]))
    lab_01.config(bg=TILE_COLORS.get(matrix[0][1]), fg=TEXT_COLORS.get(matrix[0][1]))
    lab_02.config(bg=TILE_COLORS.get(matrix[0][2]), fg=TEXT_COLORS.get(matrix[0][2]))
    lab_03.config(bg=TILE_COLORS.get(matrix[0][3]), fg=TEXT_COLORS.get(matrix[0][3]))

    lab_10.config(bg=TILE_COLORS.get(matrix[1][0]), fg=TEXT_COLORS.get(matrix[1][0]))
    lab_11.config(bg=TILE_COLORS.get(matrix[1][1]), fg=TEXT_COLORS.get(matrix[1][1]))
    lab_12.config(bg=TILE_COLORS.get(matrix[1][2]), fg=TEXT_COLORS.get(matrix[1][2]))
    lab_13.config(bg=TILE_COLORS.get(matrix[1][3]), fg=TEXT_COLORS.get(matrix[1][3]))

    lab_20.config(bg=TILE_COLORS.get(matrix[2][0]), fg=TEXT_COLORS.get(matrix[2][0]))
    lab_21.config(bg=TILE_COLORS.get(matrix[2][1]), fg=TEXT_COLORS.get(matrix[2][1]))
    lab_22.config(bg=TILE_COLORS.get(matrix[2][2]), fg=TEXT_COLORS.get(matrix[2][2]))
    lab_23.config(bg=TILE_COLORS.get(matrix[2][3]), fg=TEXT_COLORS.get(matrix[2][3]))

    lab_30.config(bg=TILE_COLORS.get(matrix[3][0]), fg=TEXT_COLORS.get(matrix[3][0]))
    lab_31.config(bg=TILE_COLORS.get(matrix[3][1]), fg=TEXT_COLORS.get(matrix[3][1]))
    lab_32.config(bg=TILE_COLORS.get(matrix[3][2]), fg=TEXT_COLORS.get(matrix[3][2]))
    lab_33.config(bg=TILE_COLORS.get(matrix[3][3]), fg=TEXT_COLORS.get(matrix[3][3]))


# Dummy Functions for Testing.

def dummy_move_left(dummy_matrix) :
    any_movement = False

    merged = [False] * 4

    for row in range(4) :
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
    return any_movement

def dummy_move_right(dummy_matrix) :
    any_movement = False

    for row in range(4) :

        merged = [False] * 4

        for main_column in range(3,0,-1) :
            if dummy_matrix[row][main_column] == 0 :
                continue

            for second_column in range(main_column-1,-1,-1) :
                if dummy_matrix[row][second_column] == 0 :
                    continue

                if dummy_matrix[row][main_column] != dummy_matrix[row][second_column] :
                    break
                
                if dummy_matrix[row][main_column] == dummy_matrix[row][second_column] and not merged[second_column] :
                    dummy_matrix[row][main_column] *= 2
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


    return any_movement

def dummy_move_down(dummy_matrix) :
    any_movement = False

    merged = [0] * 4

    for column in range(4) :
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
    return any_movement

def dummy_move_up(dummy_matrix) :


    any_movement = False

    merged = [False] * 4

    for column in range(4) :
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
    return any_movement

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
    
    if not (dummy_move_up(dummy_matrix) or dummy_move_down(dummy_matrix) or dummy_move_left(dummy_matrix) or dummy_move_right(dummy_matrix)) :
        messagebox.showerror("", "Game Over !")
        return True
    else :
        return False



