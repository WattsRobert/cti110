# CTI-110
# Robert Watts
# 4/20/2023
# P4HW2
#

# Calculations to copy and paste:
# regular_pay = hours_worked * pay_rate (if no overtime hours)
# overtime_pay = overtime_hours * overtime_rate (if overtime hours)
# gross_pay = regular_pay + overtime_pay (if overtime hours)

# Variable defining for Totals and user_name
employees = 0
overtime_pay_total = 0
regular_pay_total = 0
gross_pay_total = 0

# Initial Loop Start
user_name = input("Enter employee's name or Done to terminate: ")

# While loop to repeat until "Done" or "done" is entered
while user_name != "Done" or user_name != "done":
    
    # Variable defining for Employee Information
    overtime_rate = 1.5
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0
    gross_pay = 0

    # Entered information
    hours_worked = int(input("How many hours did " + user_name + " work?: "))
    pay_rate = int(input("What is " + user_name + "'s pay rate: "))
    
    # if statement for overtime pay if applicable
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * overtime_rate
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay + overtime_pay
    
    # Adds employee info to total variables
    employees += 1
    overtime_pay_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    
    # Prints Employee numbers out
    print("Employee name: ", user_name)
    print("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay")
    print(hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, gross_pay)

    # Restarts loop by getting input
    user_name = input("Enter employee's name or Done to terminate: ")

# Prints Total Employee numbers out
print("Total number of employees entered: ", employees)
print("Total amount paid for overtime: ", overtime_pay_total)
print("Total amount paid for regular hours: ", regular_pay_total)
print("Total amount paid in gross: ", gross_pay_total)
