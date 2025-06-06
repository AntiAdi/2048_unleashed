"""
    2048 Version 0
    Author : Aadityaraj Kaushal
    Date   : 02.04.25
    Note   : No ChatGPT was used XD
"""


from tkinter import *
import random


# Main Instance
root = Tk()
root.title("2048 Version 0")
# root.geometry("400x400")

# 2D Array to store numbers.
global matrix
matrix = [[0]*4 for i in range(4)]


"""
    Functions
"""
# Function to set the labels in accordance to the 2D matrix values.
def set_label_equal_matrix() :
    var_00.set(matrix[0][0])
    var_01.set(matrix[0][1])
    var_02.set(matrix[0][2])
    var_03.set(matrix[0][3])

    var_10.set(matrix[1][0])
    var_11.set(matrix[1][1])
    var_12.set(matrix[1][2])
    var_13.set(matrix[1][3])

    var_20.set(matrix[2][0])
    var_21.set(matrix[2][1])
    var_22.set(matrix[2][2])
    var_23.set(matrix[2][3])

    var_30.set(matrix[3][0])
    var_31.set(matrix[3][1])
    var_32.set(matrix[3][2])
    var_33.set(matrix[3][3]) 

"""
    [0, 0][0, 1][0, 2][0, 3] 
    [1, 0][1, 1][1, 2][1, 3]
    [2, 0][2, 1][2, 2][2, 3]
    [3, 0][3, 1][3, 2][3, 3]
"""

# Movement Functions
def move_up(event) :
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
        add_2_or_4()
    return any_movement

def move_down(event) :
    any_movement = False

    merged = [False] * 4

    for column in range(4) :
        for main_row in range(3,0,-1) :
            if matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row-1, -1,-1) :
                if matrix[second_row][column] == 0 :
                    continue
                
                if matrix[main_row][column] != matrix[second_row][column] :
                    break

                if matrix[main_row][column] == matrix[second_row][column] and not merged[second_row]:
                    matrix[main_row][column] *= 2
                    matrix[second_row][column] = 0
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
        add_2_or_4()
    return any_movement

def move_left(event) :
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
        add_2_or_4()
    return any_movement

def move_right(event) :
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
        add_2_or_4()

    return any_movement

# Random 2 or 4 adder.
def add_2_or_4() :
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
        matrix[row_column[0]][row_column[1]] = random.choice([2,4])
        set_label_equal_matrix()
        return True






# Making var global.
global var_00
global var_01
global var_02
global var_03

global var_10
global var_11
global var_12
global var_13

global var_20
global var_21
global var_22
global var_23

global var_30
global var_31
global var_32
global var_33




# Variables for tkinter to use.
var_00 = IntVar()
var_01 = IntVar()
var_02 = IntVar()
var_03 = IntVar()

var_10 = IntVar()
var_11 = IntVar()
var_12 = IntVar()
var_13 = IntVar()

var_20 = IntVar()
var_21 = IntVar()
var_22 = IntVar()
var_23 = IntVar()

var_30 = IntVar()
var_31 = IntVar()
var_32 = IntVar()
var_33 = IntVar()

# Initialising these variables to zero.
set_label_equal_matrix()
# Calling a random 2/4 to start the game.
add_2_or_4()





# Declaring labels.
lab_00 = Label(root, textvariable=var_00, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_01 = Label(root, textvariable=var_01, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_02 = Label(root, textvariable=var_02, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_03 = Label(root, textvariable=var_03, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)

lab_10 = Label(root, textvariable=var_10, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_11 = Label(root, textvariable=var_11, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_12 = Label(root, textvariable=var_12, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_13 = Label(root, textvariable=var_13, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)

lab_20 = Label(root, textvariable=var_20, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_21 = Label(root, textvariable=var_21, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_22 = Label(root, textvariable=var_22, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_23 = Label(root, textvariable=var_23, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)

lab_30 = Label(root, textvariable=var_30, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_31 = Label(root, textvariable=var_31, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_32 = Label(root, textvariable=var_32, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)
lab_33 = Label(root, textvariable=var_33, width=3, font=("", 25), bg="black", fg="white", padx=40, pady=40)

"""
    [0, 0][0, 1][0, 2][0, 3] 
    [1, 0][1, 1][1, 2][1, 3]
    [2, 0][2, 1][2, 2][2, 3]
    [3, 0][3, 1][3, 2][3, 3]
"""

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




root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

# Mainloop
root.mainloop()