# Create a global variable called myUniqueList. It should be an empty list to start.

# Next, create a function that allows you to add things to that list. 
# Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList.
# If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it 
# should not be added, and the function should return False;

# Finally, add some code below your function that tests it out. It should add a few different elements, 
# showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.



myUniqueList = [88,77]

def AddList():
    i = eval(input("Input a number: "))
    #e = input(eval("hello:"))
    
    myUniqueList.append[i]
    
    print(myUniqueList)

AddList()
    
