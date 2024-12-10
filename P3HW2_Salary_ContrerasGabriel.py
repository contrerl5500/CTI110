# Gabriel
# 24OCT2024
# P3HW2
# Calculate reg and OT pay, given an employees hours worked

'''
Input: Get the e_name as a string
Input: Get the hours_worked as an integer
Input: Get the pay_rate as a float
Output: Print Employee Name

If hours worked is greater than 40:
    Calculate any OT hours worked by subtracting 40 from hours_worked
    Calculate OT pay (OT hours * (payrate * 1.5))
    Calculate regular pay (40 * original payrate)
    Calculate gross pay adding ot pay and reg pay

else (employee worked 40 or less hours)
    overtime hours = 0
    overtime pay = 0
    calculate regular pay by multiplying original hours_worked by regular pay_rate
    calculate gross pay is equal to regular pay

Output:
Display total hours worked
Display regular payrate
Display overtime hours worked
Display overtime pay rate
Display pay for regular hours worked at reg pay rate
Display gross pay - both reg pay and OT pay
'''

# Values
reg_hrs = 40
ot_pay = 1.5

# Request employee income 
emp = input("Enter employee's name: ")
hrs_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-------------------------------------------")
print()
print(f"Employee name: {emp}")

if hrs_worked > reg_hrs:
    ot_hrs = hrs_worked - reg_hrs
    ot_pay = (ot_hrs * (pay_rate * ot_pay))
    reg_pay = reg_hrs * pay_rate
    gross_pay = ot_pay + reg_pay
else:
    ot_hrs = 0
    ot_pay = 0
    reg_pay = reg_hrs * pay_rate
    gross_pay = reg_pay
 
print("\nHours Worked  Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("---------------------------------------------------------------------------")
print(f"   {hrs_worked:<12}{pay_rate:<12}{ot_hrs:<10} {ot_pay:<14} ${reg_pay:<12} ${gross_pay}")

