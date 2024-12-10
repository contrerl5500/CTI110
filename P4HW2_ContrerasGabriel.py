# Constants
reg_hrs = 40
ot_rate = 1.5  # Overtime rate multiplier

# Values totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

# Begin loop for multiple employees
while True:
    # Request employee information
    emp_name = input("Enter employee's name or 'Done' to finish): ")
    
    # Check for sentinel value to exit loop
    if emp_name.lower() == "done":
        break
    
    # Get hours worked and pay rate
    hrs_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    print("-------------------------------------------")
    print(f"Employee name: {emp_name}")

    # Calculate regular pay, overtime pay, and gross pay
    if hrs_worked > reg_hrs:
        ot_hrs = hrs_worked - reg_hrs
        ot_pay = ot_hrs * (pay_rate * ot_rate)
        reg_pay = reg_hrs * pay_rate
    else:
        ot_hrs = 0
        ot_pay = 0
        reg_pay = hrs_worked * pay_rate

    gross_pay = reg_pay + ot_pay

    # Display individual employee's pay information
    print("\nHours Worked  Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("---------------------------------------------------------------------------")
    print(f"   {hrs_worked:<12}{pay_rate:<12}{ot_hrs:<10} ${ot_pay:<14.2f} ${reg_pay:<12.2f} ${gross_pay:.2f}")
    print("-------------------------------------------\n")

    # Update totals
    total_overtime_pay += ot_pay
    total_regular_pay += reg_pay
    total_gross_pay += gross_pay
    num_employees += 1

# Display summary of all employees
print("\nSummary of all employees:")
print("---------------------------------------------------")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay:  ${total_regular_pay:.2f}")
print(f"Total Gross Pay:    ${total_gross_pay:.2f}")
print(f"Number of Employees: {num_employees}")
print("---------------------------------------------------")
