# CTI-110
# P4HW1 - Score List
# Robert Watts
# Date
#

#Sets scores and other variables to 0
scores = 0
scale = 0

scores = int(input('How many scores do you want to enter?'))

if scores <= 0:
    print("At least one score must be entered")
else:
    while scores >= scores:
        scores = scores - 1
        input("Enter score #", scores)
    
