# Math Quiz Program
# 5-2-2023
# CTI-110 P5HW - Math Quiz
# Robert Watts
#

##### Defining functions and variables
# variables
option = 0

# adding function
def adding():
    print('adding test')

# subtraction function
def subtracting():
    print('subtracting test')

# Menu function (not being used rn)
def Math_Quiz():
    print()
    print("MAIN MENU")
    print("-" * 30)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    option = input(int("Please choose one of the menu options: "))

##### Program starts
print("Welcome to Math Quiz!")
print()
print("MAIN MENU")
print("-" * 30)
print("1. Adding Random Numbers")
print("2. Subtracting Random Numbers")
print("3. Exit")
print()
option = int(input("Please choose one of the menu options: "))

##### Loops program until option 3 is entered
while option != 3:
    
    if option == 1:
        print('test 1')
    elif option == 2:
        print('test 2')
    elif option > 3 or option < 1:
        print()
        print("Not an option, please input a number presented below")
    else:
        print()

    print()
    print("MAIN MENU")
    print("-" * 30)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    option = int(input("Please choose one of the menu options: "))

##### The end of the program
print("Thank you for playing...")
print("Bye!!")

h
