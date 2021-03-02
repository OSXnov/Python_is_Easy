#Homework Assignment #3: "IF" Statements

# Create a function that accepts 3 parameters and checks for equality 
# between any two of them.

# Your function should return True if 2 or more of the parameters are equal,
#  and false is none of them are equal to any of the other

def Check():
    a = int(input("Enter the value for a:"))
    b = int(input("Enter the values for b:"))
    c = int(input("Enter the value for c:"))
    

    if a == b:
        print("True")
    elif b == c:
        print("True")
    elif c == a:
        print("True")
    else:
        print("False")
Check()
