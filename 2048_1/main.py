"""
    2048 Version 1
    Author : Aadityaraj Kaushal
    Date   : 02.04.25
"""


from tkinter import *
import random






# Main Instance
root = Tk()
root.title("2048 Version 1")
# root.geometry("400x400")

# 2D Array to store numbers.
global matrix
matrix = [[0]*4 for i in range(4)]


TILE_COLORS = {
    0: "#5a5348",    
    2: "#d6c5b3",    
    4: "#cdb8a6",    
    8: "#d19158",    
    16: "#c77b4f",   
    32: "#c76352",   
    64: "#c14c32",   
    128: "#c4b15a",  
    256: "#c4ab54",  
    512: "#c4a84b",  
    1024: "#c4a23d", 
    2048: "#c4992d" ,
    4096: "#c4992d",
    8192: "#c4992d",
    16384: "#c4992d",
    32768: "#c4992d" 
}

TEXT_COLORS = {
    0: "#5a5348",    
    2: "#5a5348",    
    4: "#5a5348",    
    8: "#ece8e1",    
    16: "#ece8e1",   
    32: "#ece8e1",   
    64: "#ece8e1",   
    128: "#ece8e1",  
    256: "#ece8e1",  
    512: "#ece8e1",  
    1024: "#ece8e1", 
    2048: "#ece8e1",
    4096: "#ece8e1",
    8192: "#ece8e1",
    16384: "#ece8e1",
    32768: "#ece8e1"
}

#Declaring labels.
global lab_00
global lab_01
global lab_02
global lab_03

global lab_10
global lab_11
global lab_12
global lab_13

global lab_20
global lab_21
global lab_22
global lab_23

global lab_30
global lab_31
global lab_32
global lab_33

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


# Declaring Labels.
lab_00 = Label(root, textvariable=var_00, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_01 = Label(root, textvariable=var_01, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_02 = Label(root, textvariable=var_02, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_03 = Label(root, textvariable=var_03, width=3, font=("", 25),  fg="white", padx=40, pady=40)

lab_10 = Label(root, textvariable=var_10, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_11 = Label(root, textvariable=var_11, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_12 = Label(root, textvariable=var_12, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_13 = Label(root, textvariable=var_13, width=3, font=("", 25),  fg="white", padx=40, pady=40)

lab_20 = Label(root, textvariable=var_20, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_21 = Label(root, textvariable=var_21, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_22 = Label(root, textvariable=var_22, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_23 = Label(root, textvariable=var_23, width=3, font=("", 25),  fg="white", padx=40, pady=40)

lab_30 = Label(root, textvariable=var_30, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_31 = Label(root, textvariable=var_31, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_32 = Label(root, textvariable=var_32, width=3, font=("", 25),  fg="white", padx=40, pady=40)
lab_33 = Label(root, textvariable=var_33, width=3, font=("", 25),  fg="white", padx=40, pady=40)


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
        for main_row in range(3, 0 ,-1) :
            if matrix[main_row][column] == 0 :
                continue

            for second_row in range(main_row-1,-1,-1) :
                if matrix[second_row][column] == 0 :
                    continue
                
                if matrix[main_row][column] != matrix[second_row][column] :
                    break

                if matrix[main_row][column] == matrix[second_row][column] and not merged[second_row]:
                    matrix[second_row][column] = 0
                    matrix[main_row][column] *=2
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
        matrix[row_column[0]][row_column[1]] = random.choice([2,2,2,2,2,2,2,2,2,4])
        set_label_equal_matrix()
        return True



# Initialising the variables var to zero and making the labels colorful.
set_label_equal_matrix()
# Calling a random 2/4 to start the game.
add_2_or_4()


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