# Project #3: Pick a Card Game!


# Details:
 
#  Everyone has their favorite card game. What's yours? For this assignment, choose a card game (other than Blackjack),
#  and turn it into a Python program. It doesn't matter if it's a 1-player game, or a 2 player game, or more! 
#  That's totally up to you. A few requirements:

# It's got to be a card game (no board games, etc)
# When the game starts up, you should ask for the players' names. 
# And after they enter their names, your game should refer to them by name only. ("It's John's turn" instead of "It's player 1's turn). 
# At any point during the game, someone should be able to type "--help" to be taken to a screen where they can read the rules of the game and instructions for how to play. 
# After they're done reading, they should be able to type "--resume" to go back to the game and pick up where they left off.

def choosingPlayer():
    choice= int(input("Welcome to the Game of War, please write 1 if its one player or write 2 if its two players: "))
    if choice == 1:
        player1= str(input("Please enter your name player 1:"))
        print(player1)
    elif choice == 2:
        player1 = str(input("Please enter your name player 1:"))
        player2 =str(input("Please enter your name player 2:"))
        print(player1)
        print(player2)
    elif choice != 1 or choice != 2:
        print("Sorry only two playered option. Try Again!")



choosingPlayer()