# 2048 Unleashed
***

## Author

**Aadityaraj Kaushal**
**_IITKGP CSE '28_**

## Links

1. [2048 Wikipedia](https://en.wikipedia.org/wiki/2048_(video_game))
2. [My CodeForces](https://codeforces.com/profile/aadityarajK1)

*** 

## Change Log

#### Version 0

![2048 v0](https://drive.google.com/uc?export=view&id=1PSxOJa9RioHAYHr1KpJacEwTtgW9bG-J)


Implemented a basic 2048 game in **Python** using **Tkinter**.
- Keyboard Arrow Keys Only.
- No Animations.
- No OOPs.
- Fairly Fast.
- No Different Colors for Different Values.
- Probabilities of 2 and 4 spawning are 50% each.
- No Game Over Dialog Box. Manual judging required.

#### Version 1
![2048 v1](https://drive.google.com/uc?export=view&id=1vA2pXsEhnMTToTJd4FmtTfOVERgxbB37)

- Added Beautiful Colors.
- Improved Visibility.
- Empty tiles are Plain Solid Color instead of showing the number zero.
- Changed the probabilities of 2 and 4 spawning according to the original rules.
    - 2 : 90%
    - 4 : 10%

#### Version 2
- Fixed a __MAJOR__ bug in the tile movement logic, For all three Versions 0, 1 and 2.
Major Bugs Included :
    1. __Double Merging__ of some tiles in the same move.
    2. __Generating a Random 2/4__ even though there was __no movement__ of tiles by pressing a key.
- __Split__ the __main function__ into :
    1. __config__ : Different settings and Color Settings.
    2. __fn__ : All the functions used.
    3. __global_variables__ : All Global Variables Definitions and Declarations.
    3. __main__ : To send commands via Key Input.