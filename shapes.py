from modules import *

# Call the function for greeting the user
user = input("What's your name?: ").capitalize()
greeting(user)
            
Shapes = ["LeftTriangle", "Right Triangle", "Inverted Left Triangle", "Inverted Right Triangle", "Paschals Left Triangle", "Paschals Right Triangle", "Diamond", "Pyramid", "Double Pyramid", "Inverted Pyramid", "Inverted Double Pyramid", "Hour Glass"]

# This collects the user input choice
print("Select an option below: \n1). Left Triangle \n2). Right Triangle \n3). Inverted Left Triangle \n4). Inverted Right Triangle \n5). Paschals Left Triangle \n6). Paschals Right Triangle \n7). Diamond \n8). Pyramid \n9). Double Pyramid \n10). Inverted Pyramid \n11). Inverted Double Pyramid \n12). Hour Glass \n")
option = int(input("==> "))
while True:
    print("Enter a number of rows: ")
    r = int(input("==> "))
    print()
    if option == 1:
        print(LeftTriangle(r))
    elif option == 2:
        print(RightTriangle(r))
    elif option == 3:
        print(InvertedLeftTriangle(r))
    elif option == 4:
        print(InvertedRightTriangle(r))
    elif option == 5:
        print(PaschalsLeftTriangle(r))
    elif option == 6:
        print(PaschalsRightTriangle(r))
    elif option == 7:
        print(Diamond(r))
    elif option == 8:
        print(Pyramid(r))
    elif option == 9:
        print(DoublePyramid(r))
    elif option == 10:
        print(InvertedPyramid(r))
    elif option == 11:
        print(InvertedDoublePyramid(r))
    elif option == 12:
        print(Hourglass(r))
    else:
        print("Select a valid option")
    break