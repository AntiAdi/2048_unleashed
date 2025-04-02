from tkinter import *


# Global variable to keep track of the number of moves.
global moves 
moves = 0


# Main Instance
root = Tk()
root.title("2048 Version 3")
# root.geometry("400x400")



# 2D Array to store numbers.
global matrix
matrix = [[0]*4 for i in range(4)]



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


# Adding Label for Number of moves.
global lab_moves
lab_moves = Label(root, text=f"Number of Moves = {moves}", font=("", 16))





