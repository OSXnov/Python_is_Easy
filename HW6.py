#                                      Details

# Create a function that takes in two parameters: rows, and columns, both of which are integers. 
# The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and 
# columns as specified. After drawing the board, your function should return True.


#                                      Extra Credit:

# Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. 
# If someone passes a value greater than either maximum, your function should return False.

# Homework Assignment #6: Advanced Loops


"""
Pattern:
 01234
  | |     0
 -----    1
  | |     2
 -----    3
  | |     4
"""  

MAX_ROWS = 50
MAX_COLUMN = 230

def drawPlayingBoard(rows, col):
    if rows != int or col != int:
        return False

    if rows <= 1 or col <=1:
        return False

    if rows > MAX_ROWS or col > MAX_COLUMN:
        return False


    for row in range(0,rows):
        if row % 2 == 0:
            for column in range (0, col):
                if column % 2 == 0:
                    endChar = ""

                    if column == col - 1:
                        endChar = "\n"
                    print(" ", end = endChar)

                else:
                    print("|", end="")

        

        else :

            for column in range (0, col):
                endChar = " "

                if column == col - 1:
                    endChar = "\n"

                print("-", end = endChar)


    print("")
    return True


def usingBoardCreated(rows,col):
    if(drawPlayingBoard(rows, col)):
        print("Enjoy! Here is your playing board.")

    else:
        "No playing board for you."

usingBoardCreated(5, 5)