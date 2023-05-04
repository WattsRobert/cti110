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
    finished = 0
    guess = 0
    attempts = 0
    
    print("Addition Function")
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1 + num2
    print(' ',num1)
    print("+", num2)
    print("Enter answer: ")
    guess = int(input())
    
    while finished != 1:
        if guess < answer:
            attempts += 1
            print("Sorry, guess is too low")
            print()
            print("Try again: ",end='')
            guess = int(input())
        elif guess > answer:
            attempts += 1
            print("Sorry, guess is too high")
            print()
            print("Try again: ",end='')
            guess = int(input())
        else:
            attempts += 1
            print("Congrats!! Your guess is correct")
            print("Number of guess: ", attempts)
            print()
            finished = 1
    
def subtract():
    finished = 0
    guess = 0
    attempts = 0
    
    print("Subtraction Function")
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1 - num2
    print(' ',num1)
    print("-", num2)
    print("Enter answer: ")
    guess = int(input())
    
    while finished != 1:
        if guess < answer:
            attempts += 1
            print("Sorry, guess is too low")
            print()
            print("Try again: ",end='')
            guess = int(input())
        elif guess > answer:
            attempts += 1
            print("Sorry, guess is too high")
            print()
            print("Try again: ",end='')
            guess = int(input())
        else:
            attempts += 1
            print("Congrats!! Your guess is correct")
            print("Number of guess: ", attempts)
            print()
            finished = 1
    
main()

