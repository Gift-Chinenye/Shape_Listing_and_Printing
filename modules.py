# Assign a function for greeting the user
def greeting(name):
    """This function welcomes/greets the user"""
    message = f"Welcome to shape selector, {name}."
    print()
    print(message)
    
# Function for Printing the Left Triangle Shape
def LeftTriangle(r):
    """This function prints the Left Triangle Shape"""
    for z in range(r):
        for a in range(1 + z):
            print("*", end = " ")
        print()

        
# Function for Printing the Inverted Left Triangle Shape
def InvertedLeftTriangle(r):
    """This function prints te Inverted Left Triangle Shape"""
    for z in range(r):
        for a in range(r - z):
            print("#", end = " ")
        print("#")
    print("#")

# Function for Printing the Diamond Shape
def Diamond(r):
    """This function prints the Diamond Shape"""
    for x in range(r):
        for y in range(r - x - 1):
            print(" ", end = "")
        for z in range(2 * x + 1):
            print("#", end = "")
        print()
    for x in range(r - 1):
        for y in range(x + 1):
            print(" ", end = "")
        for z in range(2* (r - x - 2) + 1):
            print("#", end = "")
        print()
        
# Function for printing the Hourglass Shape
def Hourglass(r):
    """This function prints the Hourglass Shape"""
    for x in range(r - 1):
        for y in range(x + 1):
            print(" ", end = "")
        for z in range(2* (r - x - 2) + 1):
            print("#", end = "")
        print()
    for x in range(r):
        for y in range(r - x - 1):
            print(" ", end = "")
        for z in range(2 * x + 1):
            print("#", end = "")
        print()
        
# Function for printing the Pyramid Shape
def Pyramid(r):
    """This function prints the Pyramid Shape"""
    for x in range(r):
        for y in range(r - x - 1):
            print(" ", end = "")
        for z in range(2 * x + 1):
            print("#", end = "")
        print()
        
# Function for printing the Inverted Pyramid
def InvertedPyramid(r):
    """This function prints the Inverted Pyramid Shape"""
    for x in range(r - 1):
        for y in range(x + 1):
            print(" ", end = "")
        for z in range(2* (r - x - 2) + 1):
            print("#", end = "")
        print()
        
# Function for printing the Double Pyramid Shape
def DoublePyramid(r):
    """This function prints the Double Pyramid Shape"""
    for i in range(r):
        for j in range(r - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("#", end="")
        for m in range(2 * (r - i - 1) + 1):
            print(" ", end="")
        for p in range(2 * i + 1):
            print("#", end="")
        print()   

# Function for printing the Inverted Double Pyramid
def InvertedDoublePyramid(r):
    """This function prints the Inverted Double Pyramid Shape"""
    for i in range(r):
        for y in range(i + 1):
            print(" ", end = "")
        for z in range(2 * i - 1):
            print("#", end = "")
        for z in range(2* (r - y - 2) + 1):
            print(" ", end = "")
        print()
    
# Function for printing Paschals Right Triangle
def PaschalsRightTriangle(r):
    """This function prints the Paschals Right Triangle"""

# Function for printing the Paschals left Triangle
def PaschalsLeftTriangle(r):
    """This function prints the Paschals Left Triangle"""
    
# Function for printing the Right Triangle
def RightTriangle(r):
    """This function prints a Right Triangle Shape"""
    
# Function for printing the Right Triangle
def InvertedRightTriangle(r):
    """This function prints an Inverted Right Triangle Shape"""
    
    
    
print(LeftTriangle.__doc__)