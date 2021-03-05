
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


def usingBoardCreated(rows, col):
    if(drawPlayingBoard(rows, col)):
        print("Enjoy! Here is your playing board.")

    else:
        "No playing board for you."




usingBoardCreated(5, 5)