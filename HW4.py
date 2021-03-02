# Homework Assignment #4: Lists
# Create a global variable called myUniqueList. It should be an empty list to start.

# Next, create a function that allows you to add things to that list. 
# Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList.
# If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it 
# should not be added, and the function should return False;

# Finally, add some code below your function that tests it out. It should add a few different elements, 
# showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.

#                                      Extra credit
# Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. 
# If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness),
# it should get added to myLeftovers instead.



myUniqueList = [1,77,32,66]
print("Printing the list",myUniqueList)
myLeftovers = []

def AddList():
    i = int(input("Input a number: "))
    #e = input(eval("hello:"))
    if i == myUniqueList[0]  or myUniqueList[1]:  
        print ("This number exists run the program again; Adding to leftovers")
        myLeftovers.append(i)
        print(myLeftovers)
    elif i != myUniqueList:    
        myUniqueList.append(i)
    
        print("This is the new list, ",myUniqueList)
    

AddList()
    
