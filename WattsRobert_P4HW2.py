
def main():
    overTime = 0
    overTimePay = 0
    numEmployees = 0
    totOverTimePay = 0
    totRegPay = 0
    totGrossPay = 0
    name = input("Enter employee's name or " + 'Done' + " to terminate: ")
    
    while name != "Done":
        hours = float(input("How many hours did " + name + " work? "))
        payRate = float(input("What is " + name + "'s pay rate? "))
        print()

        if hours > 40:
            regPay = 40 * payRate
            overTime = hours - 40
            overTimePay = overTime * 1.5 * payRate
            grossPay = regPay + overTimePay
        else:
            regPay = hours * payRate
            grossPay = regPay

        print("Employee's name:   " + name)
        print()
        print("Hours Worked    Pay Rate    OverTime     OverTime Pay    RegHourPay     Gross Pay")
        print("-" * 75)
        print(f'{hours:<16.2f}{payRate:<12.2f}{overTime:<13.2f}{overTimePay:<15.2f}{regPay:<15.2f}{grossPay:<12.2f}')
        
        numEmployees = numEmployees + 1
        totOverTimePay = overTimePay + totOverTimePay
        totRegPay = totRegPay + regPay
        totGrossPay = totGrossPay + grossPay

        name = input("Enter employee's name or " + 'Done' + " to terminate: ")
    print("Total number of employees entered: ", numEmployees)
    print("Total amount paid for overtime: ", totOverTimePay)
    print("Total amount paid for regular hours: ", totRegPay)
    print("Total amount paid in gross: ", totGrossPay)
    print()
    print("Program has terminated")

main()
