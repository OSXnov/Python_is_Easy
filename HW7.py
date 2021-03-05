#               Details:
 
# Return to your first homework assignments, when you described your favorite song.
#  Refactor that code so all the variables are held as dictionary keys and value. 
# Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.


#               Extra Credit:

# Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. 
# This function should accept two parameters: Key and Value. 
# If the key exists in the dictionary and that value is the correct value, then the function should return true. In all other cases, it should return false.


#Homework #7: Dictionares and Sets

song = {"Genre":"Progressive Rock", "Artist":"Pink Floyd", "Album":" Wish you were here", 
"Year":"1975",}

def printSongMD():
    print("\n *** Song Info ***\n")
    for key in song:
        print(key, ":", song[key])
    print("\n *** End ***\n")

# def askQuestion():
#     key = input("\nGreat, let\'s start the game, guess the key?\n")
#     value = input("\nWhat you think is the value of " + key + "?\n")
#     if key and value:
#         key = key.lower()
#         value = value.lower()
#         if key in song and song[key].lower() == value:
#             return True
#     return False

# def startGuessingGame():
#     if askQuestion():
#         print("Bingo! You guessed it right...")
#     else:
#         print("Oops... You missed!")
#         repeat = input("\nWanna try again? Say 'yes' to continue or say 'no'.\n")
#         if repeat.lower() == "yes":
#             startGuessingGame()
#         else:
#             print("\nSee you again!")


printSongMD()
# print("Starting game....\n")
# startGuessingGame()