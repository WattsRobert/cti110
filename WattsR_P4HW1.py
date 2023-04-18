# CTI-110
# P4HW1 - Score List
# Robert Watts
# 4/18/2023
#

# sets function for ALL calculations done in program
def main():
    grade = 0
    total = 0
    grade_list = []

    # asks for amount of scores to be inputed
    num = int(input("How many scores do you want to enter: "))
    print()

    # for loop checking
    for i in range(0, num):
        grade = float(input("Enter score #" + str(i + 1) + ": "))
        while grade < 0 or grade > 100:
            print()
            print("INVALID Score entered!!!")
            print("Score should be between 0 and 100")
            grade = float(input("Enter score # " + str(i + 1) + " again: "))
        grade_list.append(grade)
    print()

    # variables set for lowest grade and average of grades minus the lowest one
    lowest = min(grade_list)
    grade_list.remove(lowest)
    average = sum(grade_list) / len(grade_list)

# calculate Letter Grade for Average Grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

# prints results of calculations
    print("------------Results--------------")
    print("Lowest Score         : ", lowest)
    print("Modified List         : ", grade_list)
    print("Scores Average      : ", average)
    print("Grade                    : ", grade)
    print("-----------------------------------")

    
main()
