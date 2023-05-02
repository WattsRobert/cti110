# Math Quiz Program
# 5-2-2023
# CTI-110 P5HW - Math Quiz
# Robert Watts
# (In Class version of program)

import random


def main():
    menu()

def menu():
    choice = 0
    while choice != 3:  
        print("Welcome to the Math Quiz")
        print()
        print("Main Menu")
        print("-" * 25)
        print("1. Adding Numbers")
        print("2. Subtracting Numbers")
        print("3. Exit")
        print()
        print("Please choose one of the menu options: ", end='')
        choice = int(input())

        if choice == 1:
            add()
            print("")
        elif choice == 2:
            subtract()
            print("")
        elif choice == 3:
            print("exit")
            print("The program has ended")
        else:
            print("bad choice, Try Again!!")

def add():
    print("Addition Function")

def subtract():
    print("Subtraction Function")

main()

