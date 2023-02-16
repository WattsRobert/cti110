#This program calculates and displays travel expenses
#2-16-2023
#CTI-110 P1HW2 - Travel Expense
#Anthony Cameron

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter budget: "))
print()
dest = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
roof = float(input("Appromimately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

print("------------Travel Expenses------------")
print("Location:", dest)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", roof)
print("Food:", food)

cost = gas + roof + food
remain = budget - cost
print("Remaining Balance:", remain)
