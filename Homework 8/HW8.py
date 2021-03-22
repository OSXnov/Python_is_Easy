# Homework Assignment #8: Input and Output (I/O)
# Details:
 
# Create a note-taking program. When a user starts it up, it should prompt them for a filename.
# If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
# If they enter a file name that already exists, it should ask the user if they want:
# A) Read the file
# B) Delete the file and start over
# C) Append the file
# If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 

# Extra Credit:

# Allow the user to select a 4th option:
# D) Replace a single line
# If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
# 1) The line number they want to update.
# 2) The text that should replace that line.

import os

def startNote():
    print("Starting to take note.")
    ask4File()

def ask4File():
    file_name = input("Please enter the file name:\n")
    file_path = "./" + file_name + ".txt"
    if fileExists(file_path):
        askFileMode(file_path)
    else:
        askFileInput(file_path)

def fileExists(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    return False

def askFileInput(file_path):
    txt = input('Please write down the content:\n')
    writeToFile(file_path, txt+"\n")
    print('Content written...')


def askFileMode(file_path):
    choice = input('\nWhat do you wish to do? Enter the number against the choice.\n1 read the file\n2 delete the file and start over\n3 append the file\n4 replace a single line\n\n')
    if choice == "1":
        txt = readFile(file_path)
        print('*****YOUR FILE******')
        print(txt)
        print('***********')
    elif choice == "2":
        deleteFile(file_path)
        createEmptyFile(file_path)
        print('File is deleted and empty one is made.')
    elif choice == "3":
        txt = input("Please enter the content, you wish to add:\n\n")
        appendToFile(file_path, txt)
        print('Content added!')
    elif choice == "4":
        updateLineInFile(file_path)
    else:
        print('Sorry, this is not an acceptable option!')

def updateLineInFile(file_path):
    line_counter = 1
    line_array = []
    with open(file_path, "r") as file:
        for line in file:
            print(line_counter , " " , line)
            line_counter += 1
            line_array.append(line)
    line_num = input('\nEnter the line number you wish to replace:\n')
    line_num = int(line_num)
    if line_num <= len(line_array):
        txt = input('Enter the new line:\n')
        line_array[line_num - 1] = txt   
        paragraph = ("\n").join(line_array)
        writeToFile(file_path, paragraph)
        print('\nFile content replaced!')
    else:
        print('Sorry, invalid line number.')
        


def writeToFile(file_path, content):
    file = open(file_path, "w")
    file.write(content)
    file.close()


def readFile(file_path):
    content = ""
    with open(file_path, "r") as file:
        for line in file:
            content = content + line
    return content


def appendToFile(file_path, txt):
    file = open(file_path, "a")
    file.write(txt)
    file.close()


def deleteFile(file_path):
    os.remove(file_path)


def createEmptyFile(file_path):
    file = open(file_path, "w")
    file.close()


startNote()